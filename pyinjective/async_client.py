import asyncio
import base64
import time
from copy import deepcopy
from decimal import Decimal
from typing import Any, Callable, Coroutine, Dict, List, Optional, Tuple, Union
from warnings import warn

import grpc
from google.protobuf import json_format

from pyinjective.client.chain.grpc.chain_grpc_auth_api import ChainGrpcAuthApi
from pyinjective.client.chain.grpc.chain_grpc_authz_api import ChainGrpcAuthZApi
from pyinjective.client.chain.grpc.chain_grpc_bank_api import ChainGrpcBankApi
from pyinjective.client.chain.grpc.chain_grpc_distribution_api import ChainGrpcDistributionApi
from pyinjective.client.chain.grpc.chain_grpc_exchange_api import ChainGrpcExchangeApi
from pyinjective.client.chain.grpc.chain_grpc_token_factory_api import ChainGrpcTokenFactoryApi
from pyinjective.client.chain.grpc.chain_grpc_wasm_api import ChainGrpcWasmApi
from pyinjective.client.chain.grpc_stream.chain_grpc_chain_stream import ChainGrpcChainStream
from pyinjective.client.indexer.grpc.indexer_grpc_account_api import IndexerGrpcAccountApi
from pyinjective.client.indexer.grpc.indexer_grpc_auction_api import IndexerGrpcAuctionApi
from pyinjective.client.indexer.grpc.indexer_grpc_derivative_api import IndexerGrpcDerivativeApi
from pyinjective.client.indexer.grpc.indexer_grpc_explorer_api import IndexerGrpcExplorerApi
from pyinjective.client.indexer.grpc.indexer_grpc_insurance_api import IndexerGrpcInsuranceApi
from pyinjective.client.indexer.grpc.indexer_grpc_meta_api import IndexerGrpcMetaApi
from pyinjective.client.indexer.grpc.indexer_grpc_oracle_api import IndexerGrpcOracleApi
from pyinjective.client.indexer.grpc.indexer_grpc_portfolio_api import IndexerGrpcPortfolioApi
from pyinjective.client.indexer.grpc.indexer_grpc_spot_api import IndexerGrpcSpotApi
from pyinjective.client.indexer.grpc_stream.indexer_grpc_account_stream import IndexerGrpcAccountStream
from pyinjective.client.indexer.grpc_stream.indexer_grpc_auction_stream import IndexerGrpcAuctionStream
from pyinjective.client.indexer.grpc_stream.indexer_grpc_derivative_stream import IndexerGrpcDerivativeStream
from pyinjective.client.indexer.grpc_stream.indexer_grpc_explorer_stream import IndexerGrpcExplorerStream
from pyinjective.client.indexer.grpc_stream.indexer_grpc_meta_stream import IndexerGrpcMetaStream
from pyinjective.client.indexer.grpc_stream.indexer_grpc_oracle_stream import IndexerGrpcOracleStream
from pyinjective.client.indexer.grpc_stream.indexer_grpc_portfolio_stream import IndexerGrpcPortfolioStream
from pyinjective.client.indexer.grpc_stream.indexer_grpc_spot_stream import IndexerGrpcSpotStream
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.composer import Composer
from pyinjective.core.market import BinaryOptionMarket, DerivativeMarket, SpotMarket
from pyinjective.core.network import Network
from pyinjective.core.token import Token
from pyinjective.core.tx.grpc.tx_grpc_api import TxGrpcApi
from pyinjective.exceptions import NotFoundError
from pyinjective.proto.cosmos.auth.v1beta1 import query_pb2 as auth_query, query_pb2_grpc as auth_query_grpc
from pyinjective.proto.cosmos.authz.v1beta1 import query_pb2 as authz_query, query_pb2_grpc as authz_query_grpc
from pyinjective.proto.cosmos.bank.v1beta1 import query_pb2 as bank_query, query_pb2_grpc as bank_query_grpc
from pyinjective.proto.cosmos.base.abci.v1beta1 import abci_pb2 as abci_type
from pyinjective.proto.cosmos.base.tendermint.v1beta1 import (
    query_pb2 as tendermint_query,
    query_pb2_grpc as tendermint_query_grpc,
)
from pyinjective.proto.cosmos.tx.v1beta1 import service_pb2 as tx_service, service_pb2_grpc as tx_service_grpc
from pyinjective.proto.exchange import (
    injective_accounts_rpc_pb2 as exchange_accounts_rpc_pb,
    injective_accounts_rpc_pb2_grpc as exchange_accounts_rpc_grpc,
    injective_auction_rpc_pb2 as auction_rpc_pb,
    injective_auction_rpc_pb2_grpc as auction_rpc_grpc,
    injective_derivative_exchange_rpc_pb2 as derivative_exchange_rpc_pb,
    injective_derivative_exchange_rpc_pb2_grpc as derivative_exchange_rpc_grpc,
    injective_explorer_rpc_pb2 as explorer_rpc_pb,
    injective_explorer_rpc_pb2_grpc as explorer_rpc_grpc,
    injective_insurance_rpc_pb2 as insurance_rpc_pb,
    injective_insurance_rpc_pb2_grpc as insurance_rpc_grpc,
    injective_meta_rpc_pb2 as exchange_meta_rpc_pb,
    injective_meta_rpc_pb2_grpc as exchange_meta_rpc_grpc,
    injective_oracle_rpc_pb2 as oracle_rpc_pb,
    injective_oracle_rpc_pb2_grpc as oracle_rpc_grpc,
    injective_portfolio_rpc_pb2 as portfolio_rpc_pb,
    injective_portfolio_rpc_pb2_grpc as portfolio_rpc_grpc,
    injective_spot_exchange_rpc_pb2 as spot_exchange_rpc_pb,
    injective_spot_exchange_rpc_pb2_grpc as spot_exchange_rpc_grpc,
)
from pyinjective.proto.injective.stream.v1beta1 import (
    query_pb2 as chain_stream_query,
    query_pb2_grpc as stream_rpc_grpc,
)
from pyinjective.proto.injective.types.v1beta1 import account_pb2
from pyinjective.utils.logger import LoggerProvider

DEFAULT_TIMEOUTHEIGHT_SYNC_INTERVAL = 20  # seconds
DEFAULT_TIMEOUTHEIGHT = 30  # blocks
DEFAULT_SESSION_RENEWAL_OFFSET = 120  # seconds
DEFAULT_BLOCK_TIME = 2  # seconds


class AsyncClient:
    def __init__(
        self,
        network: Network,
        insecure: Optional[bool] = None,
        credentials=grpc.ssl_channel_credentials(),
    ):
        # the `insecure` parameter is ignored and will be deprecated soon. The value is taken directly from `network`
        if insecure is not None:
            warn(
                "insecure parameter in AsyncClient is no longer used and will be deprecated",
                DeprecationWarning,
                stacklevel=2,
            )

        self.addr = ""
        self.number = 0
        self.sequence = 0

        self.network = network

        # chain stubs
        self.chain_channel = (
            grpc.aio.secure_channel(network.grpc_endpoint, credentials)
            if (network.use_secure_connection and credentials is not None)
            else grpc.aio.insecure_channel(network.grpc_endpoint)
        )

        self.stubCosmosTendermint = tendermint_query_grpc.ServiceStub(self.chain_channel)
        self.stubAuth = auth_query_grpc.QueryStub(self.chain_channel)
        self.stubAuthz = authz_query_grpc.QueryStub(self.chain_channel)
        self.stubBank = bank_query_grpc.QueryStub(self.chain_channel)
        self.stubTx = tx_service_grpc.ServiceStub(self.chain_channel)

        self.exchange_cookie = ""
        self.timeout_height = 1

        # exchange stubs
        self.exchange_channel = (
            grpc.aio.secure_channel(network.grpc_exchange_endpoint, credentials)
            if (network.use_secure_connection and credentials is not None)
            else grpc.aio.insecure_channel(network.grpc_exchange_endpoint)
        )
        self.stubMeta = exchange_meta_rpc_grpc.InjectiveMetaRPCStub(self.exchange_channel)
        self.stubExchangeAccount = exchange_accounts_rpc_grpc.InjectiveAccountsRPCStub(self.exchange_channel)
        self.stubOracle = oracle_rpc_grpc.InjectiveOracleRPCStub(self.exchange_channel)
        self.stubInsurance = insurance_rpc_grpc.InjectiveInsuranceRPCStub(self.exchange_channel)
        self.stubSpotExchange = spot_exchange_rpc_grpc.InjectiveSpotExchangeRPCStub(self.exchange_channel)
        self.stubDerivativeExchange = derivative_exchange_rpc_grpc.InjectiveDerivativeExchangeRPCStub(
            self.exchange_channel
        )
        self.stubAuction = auction_rpc_grpc.InjectiveAuctionRPCStub(self.exchange_channel)
        self.stubPortfolio = portfolio_rpc_grpc.InjectivePortfolioRPCStub(self.exchange_channel)

        # explorer stubs
        self.explorer_channel = (
            grpc.aio.secure_channel(network.grpc_explorer_endpoint, credentials)
            if (network.use_secure_connection and credentials is not None)
            else grpc.aio.insecure_channel(network.grpc_explorer_endpoint)
        )
        self.stubExplorer = explorer_rpc_grpc.InjectiveExplorerRPCStub(self.explorer_channel)

        self.chain_stream_channel = (
            grpc.aio.secure_channel(network.chain_stream_endpoint, credentials)
            if (network.use_secure_connection and credentials is not None)
            else grpc.aio.insecure_channel(network.chain_stream_endpoint)
        )
        self.chain_stream_stub = stream_rpc_grpc.StreamStub(channel=self.chain_stream_channel)

        self._timeout_height_sync_task = None
        self._initialize_timeout_height_sync_task()

        self._tokens_and_markets_initialization_lock = asyncio.Lock()
        self._tokens_by_denom: Optional[Dict[str, Token]] = None
        self._tokens_by_symbol: Optional[Dict[str, Token]] = None
        self._spot_markets: Optional[Dict[str, SpotMarket]] = None
        self._derivative_markets: Optional[Dict[str, DerivativeMarket]] = None
        self._binary_option_markets: Optional[Dict[str, BinaryOptionMarket]] = None

        self.bank_api = ChainGrpcBankApi(
            channel=self.chain_channel,
            metadata_provider=lambda: self.network.chain_metadata(
                metadata_query_provider=self._chain_cookie_metadata_requestor
            ),
        )
        self.auth_api = ChainGrpcAuthApi(
            channel=self.chain_channel,
            metadata_provider=lambda: self.network.chain_metadata(
                metadata_query_provider=self._chain_cookie_metadata_requestor
            ),
        )
        self.authz_api = ChainGrpcAuthZApi(
            channel=self.chain_channel,
            metadata_provider=lambda: self.network.chain_metadata(
                metadata_query_provider=self._chain_cookie_metadata_requestor
            ),
        )
        self.distribution_api = ChainGrpcDistributionApi(
            channel=self.chain_channel,
            metadata_provider=lambda: self.network.chain_metadata(
                metadata_query_provider=self._chain_cookie_metadata_requestor
            ),
        )
        self.chain_exchange_api = ChainGrpcExchangeApi(
            channel=self.chain_channel,
            metadata_provider=lambda: self.network.chain_metadata(
                metadata_query_provider=self._chain_cookie_metadata_requestor
            ),
        )
        self.token_factory_api = ChainGrpcTokenFactoryApi(
            channel=self.chain_channel,
            metadata_provider=lambda: self.network.chain_metadata(
                metadata_query_provider=self._chain_cookie_metadata_requestor
            ),
        )
        self.tx_api = TxGrpcApi(
            channel=self.chain_channel,
            metadata_provider=lambda: self.network.chain_metadata(
                metadata_query_provider=self._chain_cookie_metadata_requestor
            ),
        )
        self.wasm_api = ChainGrpcWasmApi(
            channel=self.chain_channel,
            metadata_provider=lambda: self.network.chain_metadata(
                metadata_query_provider=self._chain_cookie_metadata_requestor
            ),
        )

        self.chain_stream_api = ChainGrpcChainStream(
            channel=self.chain_stream_channel,
            metadata_provider=lambda: self.network.chain_metadata(
                metadata_query_provider=self._chain_cookie_metadata_requestor
            ),
        )

        self.exchange_account_api = IndexerGrpcAccountApi(
            channel=self.exchange_channel,
            metadata_provider=lambda: self.network.exchange_metadata(
                metadata_query_provider=self._exchange_cookie_metadata_requestor
            ),
        )
        self.exchange_auction_api = IndexerGrpcAuctionApi(
            channel=self.exchange_channel,
            metadata_provider=lambda: self.network.exchange_metadata(
                metadata_query_provider=self._exchange_cookie_metadata_requestor
            ),
        )
        self.exchange_derivative_api = IndexerGrpcDerivativeApi(
            channel=self.exchange_channel,
            metadata_provider=lambda: self.network.exchange_metadata(
                metadata_query_provider=self._exchange_cookie_metadata_requestor
            ),
        )
        self.exchange_insurance_api = IndexerGrpcInsuranceApi(
            channel=self.exchange_channel,
            metadata_provider=lambda: self.network.exchange_metadata(
                metadata_query_provider=self._exchange_cookie_metadata_requestor
            ),
        )
        self.exchange_meta_api = IndexerGrpcMetaApi(
            channel=self.exchange_channel,
            metadata_provider=lambda: self.network.exchange_metadata(
                metadata_query_provider=self._exchange_cookie_metadata_requestor
            ),
        )
        self.exchange_oracle_api = IndexerGrpcOracleApi(
            channel=self.exchange_channel,
            metadata_provider=lambda: self.network.exchange_metadata(
                metadata_query_provider=self._exchange_cookie_metadata_requestor
            ),
        )
        self.exchange_portfolio_api = IndexerGrpcPortfolioApi(
            channel=self.exchange_channel,
            metadata_provider=lambda: self.network.exchange_metadata(
                metadata_query_provider=self._exchange_cookie_metadata_requestor
            ),
        )
        self.exchange_spot_api = IndexerGrpcSpotApi(
            channel=self.exchange_channel,
            metadata_provider=lambda: self.network.exchange_metadata(
                metadata_query_provider=self._exchange_cookie_metadata_requestor
            ),
        )

        self.exchange_account_stream_api = IndexerGrpcAccountStream(
            channel=self.exchange_channel,
            metadata_provider=lambda: self.network.exchange_metadata(
                metadata_query_provider=self._exchange_cookie_metadata_requestor
            ),
        )
        self.exchange_auction_stream_api = IndexerGrpcAuctionStream(
            channel=self.exchange_channel,
            metadata_provider=lambda: self.network.exchange_metadata(
                metadata_query_provider=self._exchange_cookie_metadata_requestor
            ),
        )
        self.exchange_derivative_stream_api = IndexerGrpcDerivativeStream(
            channel=self.exchange_channel,
            metadata_provider=lambda: self.network.exchange_metadata(
                metadata_query_provider=self._exchange_cookie_metadata_requestor
            ),
        )
        self.exchange_meta_stream_api = IndexerGrpcMetaStream(
            channel=self.exchange_channel,
            metadata_provider=lambda: self.network.exchange_metadata(
                metadata_query_provider=self._exchange_cookie_metadata_requestor
            ),
        )
        self.exchange_oracle_stream_api = IndexerGrpcOracleStream(
            channel=self.exchange_channel,
            metadata_provider=lambda: self.network.exchange_metadata(
                metadata_query_provider=self._exchange_cookie_metadata_requestor
            ),
        )
        self.exchange_portfolio_stream_api = IndexerGrpcPortfolioStream(
            channel=self.exchange_channel,
            metadata_provider=lambda: self.network.exchange_metadata(
                metadata_query_provider=self._exchange_cookie_metadata_requestor
            ),
        )
        self.exchange_spot_stream_api = IndexerGrpcSpotStream(
            channel=self.exchange_channel,
            metadata_provider=lambda: self.network.exchange_metadata(
                metadata_query_provider=self._exchange_cookie_metadata_requestor
            ),
        )

        self.exchange_explorer_api = IndexerGrpcExplorerApi(
            channel=self.explorer_channel,
            metadata_provider=lambda: self.network.exchange_metadata(
                metadata_query_provider=self._explorer_cookie_metadata_requestor
            ),
        )
        self.exchange_explorer_stream_api = IndexerGrpcExplorerStream(
            channel=self.explorer_channel,
            metadata_provider=lambda: self.network.exchange_metadata(
                metadata_query_provider=self._explorer_cookie_metadata_requestor
            ),
        )

    async def all_tokens(self) -> Dict[str, Token]:
        if self._tokens_by_symbol is None:
            async with self._tokens_and_markets_initialization_lock:
                if self._tokens_by_symbol is None:
                    await self._initialize_tokens_and_markets()
        return deepcopy(self._tokens_by_symbol)

    async def all_spot_markets(self) -> Dict[str, SpotMarket]:
        if self._spot_markets is None:
            async with self._tokens_and_markets_initialization_lock:
                if self._spot_markets is None:
                    await self._initialize_tokens_and_markets()
        return deepcopy(self._spot_markets)

    async def all_derivative_markets(self) -> Dict[str, DerivativeMarket]:
        if self._derivative_markets is None:
            async with self._tokens_and_markets_initialization_lock:
                if self._derivative_markets is None:
                    await self._initialize_tokens_and_markets()
        return deepcopy(self._derivative_markets)

    async def all_binary_option_markets(self) -> Dict[str, BinaryOptionMarket]:
        if self._binary_option_markets is None:
            async with self._tokens_and_markets_initialization_lock:
                if self._binary_option_markets is None:
                    await self._initialize_tokens_and_markets()
        return deepcopy(self._binary_option_markets)

    def get_sequence(self):
        current_seq = self.sequence
        self.sequence += 1
        return current_seq

    def get_number(self):
        return self.number

    async def get_tx(self, tx_hash):
        """
        This method is deprecated and will be removed soon. Please use `fetch_tx` instead
        """
        warn("This method is deprecated. Use fetch_tx instead", DeprecationWarning, stacklevel=2)
        return await self.stubTx.GetTx(tx_service.GetTxRequest(hash=tx_hash))

    async def fetch_tx(self, hash: str) -> Dict[str, Any]:
        return await self.tx_api.fetch_tx(hash=hash)

    async def close_exchange_channel(self):
        await self.exchange_channel.close()
        self._cancel_timeout_height_sync_task()

    async def close_chain_channel(self):
        await self.chain_channel.close()
        self._cancel_timeout_height_sync_task()

    async def sync_timeout_height(self):
        try:
            block = await self.get_latest_block()
            self.timeout_height = block.block.header.height + DEFAULT_TIMEOUTHEIGHT
        except Exception as e:
            LoggerProvider().logger_for_class(logging_class=self.__class__).debug(
                f"error while fetching latest block, setting timeout height to 0: {e}"
            )
            self.timeout_height = 0

    # default client methods
    async def get_latest_block(self) -> tendermint_query.GetLatestBlockResponse:
        req = tendermint_query.GetLatestBlockRequest()
        return await self.stubCosmosTendermint.GetLatestBlock(req)

    async def get_account(self, address: str) -> Optional[account_pb2.EthAccount]:
        """
        This method is deprecated and will be removed soon. Please use `fetch_account` instead
        """
        warn("This method is deprecated. Use fetch_account instead", DeprecationWarning, stacklevel=2)

        try:
            metadata = await self.network.chain_metadata(metadata_query_provider=self._chain_cookie_metadata_requestor)
            account_any = (
                await self.stubAuth.Account(auth_query.QueryAccountRequest(address=address), metadata=metadata)
            ).account
            account = account_pb2.EthAccount()
            if account_any.Is(account.DESCRIPTOR):
                account_any.Unpack(account)
                self.number = int(account.base_account.account_number)
                self.sequence = int(account.base_account.sequence)
        except Exception as e:
            LoggerProvider().logger_for_class(logging_class=self.__class__).debug(
                f"error while fetching sequence and number {e}"
            )
            return None

    async def fetch_account(self, address: str) -> Optional[account_pb2.EthAccount]:
        result_account = None
        try:
            account = await self.auth_api.fetch_account(address=address)
            parsed_account = account_pb2.EthAccount()
            if parsed_account.DESCRIPTOR.full_name in account["account"]["@type"]:
                json_format.ParseDict(js_dict=account["account"], message=parsed_account, ignore_unknown_fields=True)
                self.number = parsed_account.base_account.account_number
                self.sequence = parsed_account.base_account.sequence
                result_account = parsed_account
        except Exception as e:
            LoggerProvider().logger_for_class(logging_class=self.__class__).debug(
                f"error while fetching sequence and number {e}"
            )

        return result_account

    async def get_request_id_by_tx_hash(self, tx_hash: str) -> List[int]:
        tx = await self.tx_api.fetch_tx(hash=tx_hash)
        request_ids = []
        for log in tx["txResponse"].get("logs", []):
            request_event = [
                event for event in log.get("events", []) if event["type"] == "request" or event["type"] == "report"
            ]
            if len(request_event) == 1:
                attrs = request_event[0].get("attributes", [])
                attr_id = [attr for attr in attrs if attr["key"] == "id"]
                if len(attr_id) == 1:
                    request_id = attr_id[0]["value"]
                    request_ids.append(int(request_id))
        if len(request_ids) == 0:
            raise NotFoundError("Request Id is not found")
        return request_ids

    async def simulate_tx(self, tx_byte: bytes) -> Tuple[Union[abci_type.SimulationResponse, grpc.RpcError], bool]:
        """
        This method is deprecated and will be removed soon. Please use `simulate` instead
        """
        warn("This method is deprecated. Use simulate instead", DeprecationWarning, stacklevel=2)
        try:
            req = tx_service.SimulateRequest(tx_bytes=tx_byte)
            metadata = await self.network.chain_metadata(metadata_query_provider=self._chain_cookie_metadata_requestor)
            return await self.stubTx.Simulate(request=req, metadata=metadata), True
        except grpc.RpcError as err:
            return err, False

    async def simulate(self, tx_bytes: bytes) -> Dict[str, Any]:
        return await self.tx_api.simulate(tx_bytes=tx_bytes)

    async def send_tx_sync_mode(self, tx_byte: bytes) -> abci_type.TxResponse:
        """
        This method is deprecated and will be removed soon. Please use `broadcast_tx_sync_mode` instead
        """
        warn("This method is deprecated. Use broadcast_tx_sync_mode instead", DeprecationWarning, stacklevel=2)
        req = tx_service.BroadcastTxRequest(tx_bytes=tx_byte, mode=tx_service.BroadcastMode.BROADCAST_MODE_SYNC)
        metadata = await self.network.chain_metadata(metadata_query_provider=self._chain_cookie_metadata_requestor)
        result = await self.stubTx.BroadcastTx(request=req, metadata=metadata)
        return result.tx_response

    async def broadcast_tx_sync_mode(self, tx_bytes: bytes) -> Dict[str, Any]:
        return await self.tx_api.broadcast(tx_bytes=tx_bytes, mode=tx_service.BroadcastMode.BROADCAST_MODE_SYNC)

    async def send_tx_async_mode(self, tx_byte: bytes) -> abci_type.TxResponse:
        """
        This method is deprecated and will be removed soon. Please use `broadcast_tx_async_mode` instead
        """
        warn("This method is deprecated. Use broadcast_tx_async_mode instead", DeprecationWarning, stacklevel=2)
        req = tx_service.BroadcastTxRequest(tx_bytes=tx_byte, mode=tx_service.BroadcastMode.BROADCAST_MODE_ASYNC)
        metadata = await self.network.chain_metadata(metadata_query_provider=self._chain_cookie_metadata_requestor)
        result = await self.stubTx.BroadcastTx(request=req, metadata=metadata)
        return result.tx_response

    async def broadcast_tx_async_mode(self, tx_bytes: bytes) -> Dict[str, Any]:
        return await self.tx_api.broadcast(tx_bytes=tx_bytes, mode=tx_service.BroadcastMode.BROADCAST_MODE_ASYNC)

    async def send_tx_block_mode(self, tx_byte: bytes) -> abci_type.TxResponse:
        """
        This method is deprecated and will be removed soon. BLOCK broadcast mode should not be used
        """
        warn("This method is deprecated. BLOCK broadcast mode should not be used", DeprecationWarning, stacklevel=2)
        req = tx_service.BroadcastTxRequest(tx_bytes=tx_byte, mode=tx_service.BroadcastMode.BROADCAST_MODE_BLOCK)
        metadata = await self.network.chain_metadata(metadata_query_provider=self._chain_cookie_metadata_requestor)
        result = await self.stubTx.BroadcastTx(request=req, metadata=metadata)
        return result.tx_response

    async def get_chain_id(self) -> str:
        latest_block = await self.get_latest_block()
        return latest_block.block.header.chain_id

    async def get_grants(self, granter: str, grantee: str, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_grants` instead
        """
        warn("This method is deprecated. Use fetch_grants instead", DeprecationWarning, stacklevel=2)
        return await self.stubAuthz.Grants(
            authz_query.QueryGrantsRequest(
                granter=granter,
                grantee=grantee,
                msg_type_url=kwargs.get("msg_type_url"),
            )
        )

    async def fetch_grants(
        self,
        granter: str,
        grantee: str,
        msg_type_url: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.authz_api.fetch_grants(
            granter=granter,
            grantee=grantee,
            msg_type_url=msg_type_url,
            pagination=pagination,
        )

    async def get_bank_balances(self, address: str):
        """
        This method is deprecated and will be removed soon. Please use `fetch_balances` instead
        """
        warn("This method is deprecated. Use fetch_bank_balances instead", DeprecationWarning, stacklevel=2)
        return await self.stubBank.AllBalances(bank_query.QueryAllBalancesRequest(address=address))

    async def fetch_bank_balances(self, address: str) -> Dict[str, Any]:
        return await self.bank_api.fetch_balances(account_address=address)

    async def get_bank_balance(self, address: str, denom: str):
        """
        This method is deprecated and will be removed soon. Please use `fetch_bank_balance` instead
        """
        warn("This method is deprecated. Use fetch_bank_balance instead", DeprecationWarning, stacklevel=2)
        return await self.stubBank.Balance(bank_query.QueryBalanceRequest(address=address, denom=denom))

    async def fetch_bank_balance(self, address: str, denom: str) -> Dict[str, Any]:
        return await self.bank_api.fetch_balance(account_address=address, denom=denom)

    async def fetch_spendable_balances(
        self,
        address: str,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.bank_api.fetch_spendable_balances(account_address=address, pagination=pagination)

    async def fetch_spendable_balances_by_denom(
        self,
        address: str,
        denom: str,
    ) -> Dict[str, Any]:
        return await self.bank_api.fetch_spendable_balances_by_denom(account_address=address, denom=denom)

    async def fetch_total_supply(self, pagination: Optional[PaginationOption] = None) -> Dict[str, Any]:
        return await self.bank_api.fetch_total_supply(pagination=pagination)

    async def fetch_supply_of(self, denom: str) -> Dict[str, Any]:
        return await self.bank_api.fetch_supply_of(denom=denom)

    async def fetch_denom_metadata(self, denom: str) -> Dict[str, Any]:
        return await self.bank_api.fetch_denom_metadata(denom=denom)

    async def fetch_denoms_metadata(self, pagination: Optional[PaginationOption] = None) -> Dict[str, Any]:
        return await self.bank_api.fetch_denoms_metadata(pagination=pagination)

    async def fetch_denom_owners(self, denom: str, pagination: Optional[PaginationOption] = None) -> Dict[str, Any]:
        return await self.bank_api.fetch_denom_owners(denom=denom, pagination=pagination)

    async def fetch_send_enabled(
        self,
        denoms: Optional[List[str]] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.bank_api.fetch_send_enabled(denoms=denoms, pagination=pagination)

    async def fetch_validator_distribution_info(self, validator_address: str) -> Dict[str, Any]:
        return await self.distribution_api.fetch_validator_distribution_info(validator_address=validator_address)

    async def fetch_validator_outstanding_rewards(self, validator_address: str) -> Dict[str, Any]:
        return await self.distribution_api.fetch_validator_outstanding_rewards(validator_address=validator_address)

    async def fetch_validator_commission(self, validator_address: str) -> Dict[str, Any]:
        return await self.distribution_api.fetch_validator_commission(validator_address=validator_address)

    async def fetch_validator_slashes(
        self,
        validator_address: str,
        starting_height: Optional[int] = None,
        ending_height: Optional[int] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.distribution_api.fetch_validator_slashes(
            validator_address=validator_address,
            starting_height=starting_height,
            ending_height=ending_height,
            pagination=pagination,
        )

    async def fetch_delegation_rewards(
        self,
        delegator_address: str,
        validator_address: str,
    ) -> Dict[str, Any]:
        return await self.distribution_api.fetch_delegation_rewards(
            delegator_address=delegator_address,
            validator_address=validator_address,
        )

    async def fetch_delegation_total_rewards(
        self,
        delegator_address: str,
    ) -> Dict[str, Any]:
        return await self.distribution_api.fetch_delegation_total_rewards(
            delegator_address=delegator_address,
        )

    async def fetch_delegator_validators(
        self,
        delegator_address: str,
    ) -> Dict[str, Any]:
        return await self.distribution_api.fetch_delegator_validators(
            delegator_address=delegator_address,
        )

    async def fetch_delegator_withdraw_address(
        self,
        delegator_address: str,
    ) -> Dict[str, Any]:
        return await self.distribution_api.fetch_delegator_withdraw_address(
            delegator_address=delegator_address,
        )

    async def fetch_community_pool(self) -> Dict[str, Any]:
        return await self.distribution_api.fetch_community_pool()

    # Exchange module

    async def fetch_subaccount_deposits(
        self,
        subaccount_id: Optional[str] = None,
        subaccount_trader: Optional[str] = None,
        subaccount_nonce: Optional[int] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_subaccount_deposits(
            subaccount_id=subaccount_id,
            subaccount_trader=subaccount_trader,
            subaccount_nonce=subaccount_nonce,
        )

    async def fetch_subaccount_deposit(
        self,
        subaccount_id: str,
        denom: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_subaccount_deposit(
            subaccount_id=subaccount_id,
            denom=denom,
        )

    async def fetch_exchange_balances(self) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_exchange_balances()

    async def fetch_aggregate_volume(self, account: str) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_aggregate_volume(account=account)

    async def fetch_aggregate_volumes(
        self,
        accounts: Optional[List[str]] = None,
        market_ids: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_aggregate_volumes(
            accounts=accounts,
            market_ids=market_ids,
        )

    async def fetch_aggregate_market_volume(
        self,
        market_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_aggregate_market_volume(
            market_id=market_id,
        )

    async def fetch_aggregate_market_volumes(
        self,
        market_ids: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_aggregate_market_volumes(
            market_ids=market_ids,
        )

    async def fetch_denom_decimal(self, denom: str) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_denom_decimal(denom=denom)

    async def fetch_denom_decimals(self, denoms: Optional[List[str]] = None) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_denom_decimals(denoms=denoms)

    async def fetch_chain_spot_markets(
        self,
        status: Optional[str] = None,
        market_ids: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_spot_markets(
            status=status,
            market_ids=market_ids,
        )

    async def fetch_chain_spot_market(
        self,
        market_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_spot_market(
            market_id=market_id,
        )

    async def fetch_chain_full_spot_markets(
        self,
        status: Optional[str] = None,
        market_ids: Optional[List[str]] = None,
        with_mid_price_and_tob: Optional[bool] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_full_spot_markets(
            status=status,
            market_ids=market_ids,
            with_mid_price_and_tob=with_mid_price_and_tob,
        )

    async def fetch_chain_full_spot_market(
        self,
        market_id: str,
        with_mid_price_and_tob: Optional[bool] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_full_spot_market(
            market_id=market_id,
            with_mid_price_and_tob=with_mid_price_and_tob,
        )

    async def fetch_chain_spot_orderbook(
        self,
        market_id: str,
        order_side: Optional[str] = None,
        limit_cumulative_notional: Optional[str] = None,
        limit_cumulative_quantity: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        # Order side could be "Side_Unspecified", "Buy", "Sell"
        return await self.chain_exchange_api.fetch_spot_orderbook(
            market_id=market_id,
            order_side=order_side,
            limit_cumulative_notional=limit_cumulative_notional,
            limit_cumulative_quantity=limit_cumulative_quantity,
            pagination=pagination,
        )

    async def fetch_chain_trader_spot_orders(
        self,
        market_id: str,
        subaccount_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_trader_spot_orders(
            market_id=market_id,
            subaccount_id=subaccount_id,
        )

    async def fetch_chain_account_address_spot_orders(
        self,
        market_id: str,
        account_address: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_account_address_spot_orders(
            market_id=market_id,
            account_address=account_address,
        )

    async def fetch_chain_spot_orders_by_hashes(
        self,
        market_id: str,
        subaccount_id: str,
        order_hashes: List[str],
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_spot_orders_by_hashes(
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hashes=order_hashes,
        )

    async def fetch_chain_subaccount_orders(
        self,
        subaccount_id: str,
        market_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_subaccount_orders(
            subaccount_id=subaccount_id,
            market_id=market_id,
        )

    async def fetch_chain_trader_spot_transient_orders(
        self,
        market_id: str,
        subaccount_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_trader_spot_transient_orders(
            market_id=market_id,
            subaccount_id=subaccount_id,
        )

    async def fetch_spot_mid_price_and_tob(
        self,
        market_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_spot_mid_price_and_tob(
            market_id=market_id,
        )

    async def fetch_derivative_mid_price_and_tob(
        self,
        market_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_derivative_mid_price_and_tob(
            market_id=market_id,
        )

    async def fetch_chain_derivative_orderbook(
        self,
        market_id: str,
        limit_cumulative_notional: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_derivative_orderbook(
            market_id=market_id,
            limit_cumulative_notional=limit_cumulative_notional,
            pagination=pagination,
        )

    async def fetch_chain_trader_derivative_orders(
        self,
        market_id: str,
        subaccount_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_trader_derivative_orders(
            market_id=market_id,
            subaccount_id=subaccount_id,
        )

    async def fetch_chain_account_address_derivative_orders(
        self,
        market_id: str,
        account_address: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_account_address_derivative_orders(
            market_id=market_id,
            account_address=account_address,
        )

    async def fetch_chain_derivative_orders_by_hashes(
        self,
        market_id: str,
        subaccount_id: str,
        order_hashes: List[str],
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_derivative_orders_by_hashes(
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hashes=order_hashes,
        )

    async def fetch_chain_trader_derivative_transient_orders(
        self,
        market_id: str,
        subaccount_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_trader_derivative_transient_orders(
            market_id=market_id,
            subaccount_id=subaccount_id,
        )

    async def fetch_chain_derivative_markets(
        self,
        status: Optional[str] = None,
        market_ids: Optional[List[str]] = None,
        with_mid_price_and_tob: Optional[bool] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_derivative_markets(
            status=status,
            market_ids=market_ids,
            with_mid_price_and_tob=with_mid_price_and_tob,
        )

    async def fetch_chain_derivative_market(
        self,
        market_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_derivative_market(
            market_id=market_id,
        )

    async def fetch_derivative_market_address(self, market_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_derivative_market_address(market_id=market_id)

    async def fetch_subaccount_trade_nonce(self, subaccount_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_subaccount_trade_nonce(subaccount_id=subaccount_id)

    async def fetch_chain_positions(self) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_positions()

    async def fetch_chain_subaccount_positions(self, subaccount_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_subaccount_positions(subaccount_id=subaccount_id)

    async def fetch_chain_subaccount_position_in_market(self, subaccount_id: str, market_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_subaccount_position_in_market(
            subaccount_id=subaccount_id,
            market_id=market_id,
        )

    async def fetch_chain_subaccount_effective_position_in_market(
        self, subaccount_id: str, market_id: str
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_subaccount_effective_position_in_market(
            subaccount_id=subaccount_id,
            market_id=market_id,
        )

    async def fetch_chain_perpetual_market_info(self, market_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_perpetual_market_info(market_id=market_id)

    async def fetch_chain_expiry_futures_market_info(self, market_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_expiry_futures_market_info(market_id=market_id)

    async def fetch_chain_perpetual_market_funding(self, market_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_perpetual_market_funding(market_id=market_id)

    async def fetch_subaccount_order_metadata(self, subaccount_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_subaccount_order_metadata(subaccount_id=subaccount_id)

    async def fetch_trade_reward_points(
        self,
        accounts: Optional[List[str]] = None,
        pending_pool_timestamp: Optional[int] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_trade_reward_points(
            accounts=accounts,
            pending_pool_timestamp=pending_pool_timestamp,
        )

    async def fetch_pending_trade_reward_points(
        self,
        accounts: Optional[List[str]] = None,
        pending_pool_timestamp: Optional[int] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_pending_trade_reward_points(
            accounts=accounts,
            pending_pool_timestamp=pending_pool_timestamp,
        )

    async def fetch_trade_reward_campaign(self) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_trade_reward_campaign()

    async def fetch_fee_discount_account_info(self, account: str) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_fee_discount_account_info(account=account)

    async def fetch_fee_discount_schedule(self) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_fee_discount_schedule()

    async def fetch_balance_mismatches(self, dust_factor: int) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_balance_mismatches(dust_factor=dust_factor)

    async def fetch_balance_with_balance_holds(self) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_balance_with_balance_holds()

    async def fetch_fee_discount_tier_statistics(self) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_fee_discount_tier_statistics()

    async def fetch_mito_vault_infos(self) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_mito_vault_infos()

    async def fetch_market_id_from_vault(self, vault_address: str) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_market_id_from_vault(vault_address=vault_address)

    async def fetch_historical_trade_records(self, market_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_historical_trade_records(market_id=market_id)

    async def fetch_is_opted_out_of_rewards(self, account: str) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_is_opted_out_of_rewards(account=account)

    async def fetch_opted_out_of_rewards_accounts(self) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_opted_out_of_rewards_accounts()

    async def fetch_market_volatility(
        self,
        market_id: str,
        trade_grouping_sec: Optional[int] = None,
        max_age: Optional[int] = None,
        include_raw_history: Optional[bool] = None,
        include_metadata: Optional[bool] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_market_volatility(
            market_id=market_id,
            trade_grouping_sec=trade_grouping_sec,
            max_age=max_age,
            include_raw_history=include_raw_history,
            include_metadata=include_metadata,
        )

    async def fetch_chain_binary_options_markets(self, status: Optional[str] = None) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_binary_options_markets(status=status)

    async def fetch_trader_derivative_conditional_orders(
        self,
        subaccount_id: Optional[str] = None,
        market_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_trader_derivative_conditional_orders(
            subaccount_id=subaccount_id,
            market_id=market_id,
        )

    async def fetch_market_atomic_execution_fee_multiplier(
        self,
        market_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_market_atomic_execution_fee_multiplier(
            market_id=market_id,
        )

    # Injective Exchange client methods

    # Auction RPC

    async def get_auction(self, bid_round: int):
        """
        This method is deprecated and will be removed soon. Please use `fetch_auction` instead
        """
        warn("This method is deprecated. Use fetch_auction instead", DeprecationWarning, stacklevel=2)
        req = auction_rpc_pb.AuctionEndpointRequest(round=bid_round)
        return await self.stubAuction.AuctionEndpoint(req)

    async def fetch_auction(self, round: int) -> Dict[str, Any]:
        return await self.exchange_auction_api.fetch_auction(round=round)

    async def get_auctions(self):
        """
        This method is deprecated and will be removed soon. Please use `fetch_auctions` instead
        """
        warn("This method is deprecated. Use fetch_auctions instead", DeprecationWarning, stacklevel=2)
        req = auction_rpc_pb.AuctionsRequest()
        return await self.stubAuction.Auctions(req)

    async def fetch_auctions(self) -> Dict[str, Any]:
        return await self.exchange_auction_api.fetch_auctions()

    async def stream_bids(self):
        """
        This method is deprecated and will be removed soon. Please use `listen_bids_updates` instead
        """
        warn("This method is deprecated. Use listen_bids_updates instead", DeprecationWarning, stacklevel=2)
        req = auction_rpc_pb.StreamBidsRequest()
        return self.stubAuction.StreamBids(req)

    async def listen_bids_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
    ):
        await self.exchange_auction_stream_api.stream_bids(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
        )

    # Meta RPC

    async def ping(self):
        """
        This method is deprecated and will be removed soon. Please use `fetch_ping` instead
        """
        warn("This method is deprecated. Use fetch_ping instead", DeprecationWarning, stacklevel=2)
        req = exchange_meta_rpc_pb.PingRequest()
        return await self.stubMeta.Ping(req)

    async def fetch_ping(self) -> Dict[str, Any]:
        return await self.exchange_meta_api.fetch_ping()

    async def version(self):
        """
        This method is deprecated and will be removed soon. Please use `fetch_version` instead
        """
        warn("This method is deprecated. Use fetch_version instead", DeprecationWarning, stacklevel=2)
        req = exchange_meta_rpc_pb.VersionRequest()
        return await self.stubMeta.Version(req)

    async def fetch_version(self) -> Dict[str, Any]:
        return await self.exchange_meta_api.fetch_version()

    async def info(self):
        """
        This method is deprecated and will be removed soon. Please use `fetch_info` instead
        """
        warn("This method is deprecated. Use fetch_info instead", DeprecationWarning, stacklevel=2)
        req = exchange_meta_rpc_pb.InfoRequest(
            timestamp=int(time.time() * 1000),
        )
        return await self.stubMeta.Info(req)

    async def fetch_info(self) -> Dict[str, Any]:
        return await self.exchange_meta_api.fetch_info()

    async def stream_keepalive(self):
        """
        This method is deprecated and will be removed soon. Please use `listen_keepalive` instead
        """
        warn("This method is deprecated. Use listen_keepalive instead", DeprecationWarning, stacklevel=2)
        req = exchange_meta_rpc_pb.StreamKeepaliveRequest()
        return self.stubMeta.StreamKeepalive(req)

    async def listen_keepalive(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
    ):
        await self.exchange_meta_stream_api.stream_keepalive(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
        )

    # Wasm module
    async def fetch_contract_info(self, address: str) -> Dict[str, Any]:
        return await self.wasm_api.fetch_contract_info(address=address)

    async def fetch_contract_history(
        self,
        address: str,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.wasm_api.fetch_contract_history(
            address=address,
            pagination=pagination,
        )

    async def fetch_contracts_by_code(
        self,
        code_id: int,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.wasm_api.fetch_contracts_by_code(
            code_id=code_id,
            pagination=pagination,
        )

    async def fetch_all_contracts_state(
        self,
        address: str,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.wasm_api.fetch_all_contracts_state(
            address=address,
            pagination=pagination,
        )

    async def fetch_raw_contract_state(self, address: str, query_data: str) -> Dict[str, Any]:
        return await self.wasm_api.fetch_raw_contract_state(address=address, query_data=query_data)

    async def fetch_smart_contract_state(self, address: str, query_data: str) -> Dict[str, Any]:
        return await self.wasm_api.fetch_smart_contract_state(address=address, query_data=query_data)

    async def fetch_code(self, code_id: int) -> Dict[str, Any]:
        return await self.wasm_api.fetch_code(code_id=code_id)

    async def fetch_codes(
        self,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.wasm_api.fetch_codes(
            pagination=pagination,
        )

    async def fetch_pinned_codes(
        self,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.wasm_api.fetch_pinned_codes(
            pagination=pagination,
        )

    async def fetch_contracts_by_creator(
        self,
        creator_address: str,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.wasm_api.fetch_contracts_by_creator(
            creator_address=creator_address,
            pagination=pagination,
        )

    # Token Factory module

    async def fetch_denom_authority_metadata(
        self,
        creator: str,
        sub_denom: Optional[str] = None,
    ) -> Dict[str, Any]:
        return await self.token_factory_api.fetch_denom_authority_metadata(creator=creator, sub_denom=sub_denom)

    async def fetch_denoms_from_creator(
        self,
        creator: str,
    ) -> Dict[str, Any]:
        return await self.token_factory_api.fetch_denoms_from_creator(creator=creator)

    async def fetch_tokenfactory_module_state(self) -> Dict[str, Any]:
        return await self.token_factory_api.fetch_tokenfactory_module_state()

    # Explorer RPC

    async def get_tx_by_hash(self, tx_hash: str):
        """
        This method is deprecated and will be removed soon. Please use `fetch_tx_by_tx_hash` instead
        """
        warn("This method is deprecated. Use fetch_tx_by_tx_hash instead", DeprecationWarning, stacklevel=2)

        req = explorer_rpc_pb.GetTxByTxHashRequest(hash=tx_hash)
        return await self.stubExplorer.GetTxByTxHash(req)

    async def fetch_tx_by_tx_hash(self, tx_hash: str) -> Dict[str, Any]:
        return await self.exchange_explorer_api.fetch_tx_by_tx_hash(tx_hash=tx_hash)

    async def get_account_txs(self, address: str, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_account_txs` instead
        """
        warn("This method is deprecated. Use fetch_account_txs instead", DeprecationWarning, stacklevel=2)
        req = explorer_rpc_pb.GetAccountTxsRequest(
            address=address,
            before=kwargs.get("before"),
            after=kwargs.get("after"),
            limit=kwargs.get("limit"),
            skip=kwargs.get("skip"),
            type=kwargs.get("type"),
            module=kwargs.get("module"),
        )
        return await self.stubExplorer.GetAccountTxs(req)

    async def fetch_account_txs(
        self,
        address: str,
        before: Optional[int] = None,
        after: Optional[int] = None,
        message_type: Optional[str] = None,
        module: Optional[str] = None,
        from_number: Optional[int] = None,
        to_number: Optional[int] = None,
        status: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_explorer_api.fetch_account_txs(
            address=address,
            before=before,
            after=after,
            message_type=message_type,
            module=module,
            from_number=from_number,
            to_number=to_number,
            status=status,
            pagination=pagination,
        )

    async def get_blocks(self, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_blocks` instead
        """
        warn("This method is deprecated. Use fetch_blocks instead", DeprecationWarning, stacklevel=2)
        req = explorer_rpc_pb.GetBlocksRequest(
            before=kwargs.get("before"),
            after=kwargs.get("after"),
            limit=kwargs.get("limit"),
        )
        return await self.stubExplorer.GetBlocks(req)

    async def fetch_blocks(
        self,
        before: Optional[int] = None,
        after: Optional[int] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_explorer_api.fetch_blocks(before=before, after=after, pagination=pagination)

    async def get_block(self, block_height: str):
        """
        This method is deprecated and will be removed soon. Please use `fetch_block` instead
        """
        warn("This method is deprecated. Use fetch_block instead", DeprecationWarning, stacklevel=2)
        req = explorer_rpc_pb.GetBlockRequest(id=block_height)
        return await self.stubExplorer.GetBlock(req)

    async def fetch_block(self, block_id: str) -> Dict[str, Any]:
        return await self.exchange_explorer_api.fetch_block(block_id=block_id)

    async def get_txs(self, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_txs` instead
        """
        warn("This method is deprecated. Use fetch_txs instead", DeprecationWarning, stacklevel=2)
        req = explorer_rpc_pb.GetTxsRequest(
            before=kwargs.get("before"),
            after=kwargs.get("after"),
            limit=kwargs.get("limit"),
            skip=kwargs.get("skip"),
            type=kwargs.get("type"),
            module=kwargs.get("module"),
        )
        return await self.stubExplorer.GetTxs(req)

    async def fetch_txs(
        self,
        before: Optional[int] = None,
        after: Optional[int] = None,
        message_type: Optional[str] = None,
        module: Optional[str] = None,
        from_number: Optional[int] = None,
        to_number: Optional[int] = None,
        status: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_explorer_api.fetch_txs(
            before=before,
            after=after,
            message_type=message_type,
            module=module,
            from_number=from_number,
            to_number=to_number,
            status=status,
            pagination=pagination,
        )

    async def stream_txs(self):
        """
        This method is deprecated and will be removed soon. Please use `listen_txs_updates` instead
        """
        warn("This method is deprecated. Use listen_txs_updates instead", DeprecationWarning, stacklevel=2)
        req = explorer_rpc_pb.StreamTxsRequest()
        return self.stubExplorer.StreamTxs(req)

    async def listen_txs_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
    ):
        await self.exchange_explorer_stream_api.stream_txs(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
        )

    async def stream_blocks(self):
        """
        This method is deprecated and will be removed soon. Please use `listen_blocks_updates` instead
        """
        warn("This method is deprecated. Use listen_blocks_updates instead", DeprecationWarning, stacklevel=2)
        req = explorer_rpc_pb.StreamBlocksRequest()
        return self.stubExplorer.StreamBlocks(req)

    async def listen_blocks_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
    ):
        await self.exchange_explorer_stream_api.stream_blocks(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
        )

    async def get_peggy_deposits(self, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_peggy_deposit_txs` instead
        """
        warn("This method is deprecated. Use fetch_peggy_deposit_txs instead", DeprecationWarning, stacklevel=2)
        req = explorer_rpc_pb.GetPeggyDepositTxsRequest(
            sender=kwargs.get("sender"),
            receiver=kwargs.get("receiver"),
            limit=kwargs.get("limit"),
            skip=kwargs.get("skip"),
        )
        return await self.stubExplorer.GetPeggyDepositTxs(req)

    async def fetch_peggy_deposit_txs(
        self,
        sender: Optional[str] = None,
        receiver: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_explorer_api.fetch_peggy_deposit_txs(
            sender=sender,
            receiver=receiver,
            pagination=pagination,
        )

    async def get_peggy_withdrawals(self, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_peggy_withdrawal_txs` instead
        """
        warn("This method is deprecated. Use fetch_peggy_withdrawal_txs instead", DeprecationWarning, stacklevel=2)
        req = explorer_rpc_pb.GetPeggyWithdrawalTxsRequest(
            sender=kwargs.get("sender"),
            receiver=kwargs.get("receiver"),
            limit=kwargs.get("limit"),
            skip=kwargs.get("skip"),
        )
        return await self.stubExplorer.GetPeggyWithdrawalTxs(req)

    async def fetch_peggy_withdrawal_txs(
        self,
        sender: Optional[str] = None,
        receiver: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_explorer_api.fetch_peggy_withdrawal_txs(
            sender=sender,
            receiver=receiver,
            pagination=pagination,
        )

    async def get_ibc_transfers(self, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_ibc_transfer_txs` instead
        """
        warn("This method is deprecated. Use fetch_ibc_transfer_txs instead", DeprecationWarning, stacklevel=2)
        req = explorer_rpc_pb.GetIBCTransferTxsRequest(
            sender=kwargs.get("sender"),
            receiver=kwargs.get("receiver"),
            src_channel=kwargs.get("src_channel"),
            src_port=kwargs.get("src_port"),
            dest_channel=kwargs.get("dest_channel"),
            dest_port=kwargs.get("dest_port"),
            limit=kwargs.get("limit"),
            skip=kwargs.get("skip"),
        )
        return await self.stubExplorer.GetIBCTransferTxs(req)

    async def fetch_ibc_transfer_txs(
        self,
        sender: Optional[str] = None,
        receiver: Optional[str] = None,
        src_channel: Optional[str] = None,
        src_port: Optional[str] = None,
        dest_channel: Optional[str] = None,
        dest_port: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_explorer_api.fetch_ibc_transfer_txs(
            sender=sender,
            receiver=receiver,
            src_channel=src_channel,
            src_port=src_port,
            dest_channel=dest_channel,
            dest_port=dest_port,
            pagination=pagination,
        )

    # AccountsRPC

    async def stream_subaccount_balance(self, subaccount_id: str, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `listen_subaccount_balance_updates` instead
        """
        warn(
            "This method is deprecated. Use listen_subaccount_balance_updates instead", DeprecationWarning, stacklevel=2
        )
        req = exchange_accounts_rpc_pb.StreamSubaccountBalanceRequest(
            subaccount_id=subaccount_id, denoms=kwargs.get("denoms")
        )
        return self.stubExchangeAccount.StreamSubaccountBalance(req)

    async def listen_subaccount_balance_updates(
        self,
        subaccount_id: str,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        denoms: Optional[List[str]] = None,
    ):
        await self.exchange_account_stream_api.stream_subaccount_balance(
            subaccount_id=subaccount_id,
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            denoms=denoms,
        )

    async def get_subaccount_balance(self, subaccount_id: str, denom: str):
        """
        This method is deprecated and will be removed soon. Please use `fetch_subaccount_balance` instead
        """
        warn("This method is deprecated. Use fetch_subaccount_balance instead", DeprecationWarning, stacklevel=2)
        req = exchange_accounts_rpc_pb.SubaccountBalanceEndpointRequest(subaccount_id=subaccount_id, denom=denom)
        return await self.stubExchangeAccount.SubaccountBalanceEndpoint(req)

    async def fetch_subaccount_balance(self, subaccount_id: str, denom: str) -> Dict[str, Any]:
        return await self.exchange_account_api.fetch_subaccount_balance(subaccount_id=subaccount_id, denom=denom)

    async def get_subaccount_list(self, account_address: str):
        """
        This method is deprecated and will be removed soon. Please use `fetch_subaccounts_list` instead
        """
        warn("This method is deprecated. Use fetch_subaccounts_list instead", DeprecationWarning, stacklevel=2)
        req = exchange_accounts_rpc_pb.SubaccountsListRequest(account_address=account_address)
        return await self.stubExchangeAccount.SubaccountsList(req)

    async def fetch_subaccounts_list(self, address: str) -> Dict[str, Any]:
        return await self.exchange_account_api.fetch_subaccounts_list(address=address)

    async def get_subaccount_balances_list(self, subaccount_id: str, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_subaccount_balances_list` instead
        """
        warn("This method is deprecated. Use fetch_subaccount_balances_list instead", DeprecationWarning, stacklevel=2)
        req = exchange_accounts_rpc_pb.SubaccountBalancesListRequest(
            subaccount_id=subaccount_id, denoms=kwargs.get("denoms")
        )
        return await self.stubExchangeAccount.SubaccountBalancesList(req)

    async def fetch_subaccount_balances_list(
        self, subaccount_id: str, denoms: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        return await self.exchange_account_api.fetch_subaccount_balances_list(
            subaccount_id=subaccount_id, denoms=denoms
        )

    async def get_subaccount_history(self, subaccount_id: str, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_subaccount_history` instead
        """
        warn("This method is deprecated. Use fetch_subaccount_history instead", DeprecationWarning, stacklevel=2)
        req = exchange_accounts_rpc_pb.SubaccountHistoryRequest(
            subaccount_id=subaccount_id,
            denom=kwargs.get("denom"),
            transfer_types=kwargs.get("transfer_types"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
            end_time=kwargs.get("end_time"),
        )
        return await self.stubExchangeAccount.SubaccountHistory(req)

    async def fetch_subaccount_history(
        self,
        subaccount_id: str,
        denom: Optional[str] = None,
        transfer_types: Optional[List[str]] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_account_api.fetch_subaccount_history(
            subaccount_id=subaccount_id,
            denom=denom,
            transfer_types=transfer_types,
            pagination=pagination,
        )

    async def get_subaccount_order_summary(self, subaccount_id: str, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_subaccount_order_summary` instead
        """
        warn("This method is deprecated. Use fetch_subaccount_order_summary instead", DeprecationWarning, stacklevel=2)
        req = exchange_accounts_rpc_pb.SubaccountOrderSummaryRequest(
            subaccount_id=subaccount_id,
            order_direction=kwargs.get("order_direction"),
            market_id=kwargs.get("market_id"),
        )
        return await self.stubExchangeAccount.SubaccountOrderSummary(req)

    async def fetch_subaccount_order_summary(
        self,
        subaccount_id: str,
        market_id: Optional[str] = None,
        order_direction: Optional[str] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_account_api.fetch_subaccount_order_summary(
            subaccount_id=subaccount_id,
            market_id=market_id,
            order_direction=order_direction,
        )

    async def get_order_states(self, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_order_states` instead
        """
        warn("This method is deprecated. Use fetch_order_states instead", DeprecationWarning, stacklevel=2)
        req = exchange_accounts_rpc_pb.OrderStatesRequest(
            spot_order_hashes=kwargs.get("spot_order_hashes"),
            derivative_order_hashes=kwargs.get("derivative_order_hashes"),
        )
        return await self.stubExchangeAccount.OrderStates(req)

    async def fetch_order_states(
        self,
        spot_order_hashes: Optional[List[str]] = None,
        derivative_order_hashes: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_account_api.fetch_order_states(
            spot_order_hashes=spot_order_hashes,
            derivative_order_hashes=derivative_order_hashes,
        )

    async def get_portfolio(self, account_address: str):
        """
        This method is deprecated and will be removed soon. Please use `fetch_portfolio` instead
        """
        warn("This method is deprecated. Use fetch_portfolio instead", DeprecationWarning, stacklevel=2)

        req = exchange_accounts_rpc_pb.PortfolioRequest(account_address=account_address)
        return await self.stubExchangeAccount.Portfolio(req)

    async def fetch_portfolio(self, account_address: str) -> Dict[str, Any]:
        return await self.exchange_account_api.fetch_portfolio(account_address=account_address)

    async def get_rewards(self, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_rewards` instead
        """
        warn("This method is deprecated. Use fetch_rewards instead", DeprecationWarning, stacklevel=2)
        req = exchange_accounts_rpc_pb.RewardsRequest(
            account_address=kwargs.get("account_address"), epoch=kwargs.get("epoch")
        )
        return await self.stubExchangeAccount.Rewards(req)

    async def fetch_rewards(self, account_address: Optional[str] = None, epoch: Optional[int] = None) -> Dict[str, Any]:
        return await self.exchange_account_api.fetch_rewards(account_address=account_address, epoch=epoch)

    # OracleRPC

    async def stream_oracle_prices(self, base_symbol: str, quote_symbol: str, oracle_type: str):
        """
        This method is deprecated and will be removed soon. Please use `listen_subaccount_balance_updates` instead
        """
        warn("This method is deprecated. Use listen_oracle_prices_updates instead", DeprecationWarning, stacklevel=2)
        req = oracle_rpc_pb.StreamPricesRequest(
            base_symbol=base_symbol, quote_symbol=quote_symbol, oracle_type=oracle_type
        )
        return self.stubOracle.StreamPrices(req)

    async def listen_oracle_prices_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        base_symbol: Optional[str] = None,
        quote_symbol: Optional[str] = None,
        oracle_type: Optional[str] = None,
    ):
        await self.exchange_oracle_stream_api.stream_oracle_prices(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            base_symbol=base_symbol,
            quote_symbol=quote_symbol,
            oracle_type=oracle_type,
        )

    async def get_oracle_prices(
        self,
        base_symbol: str,
        quote_symbol: str,
        oracle_type: str,
        oracle_scale_factor: int,
    ):
        """
        This method is deprecated and will be removed soon. Please use `fetch_oracle_price` instead
        """
        warn("This method is deprecated. Use fetch_oracle_price instead", DeprecationWarning, stacklevel=2)
        req = oracle_rpc_pb.PriceRequest(
            base_symbol=base_symbol,
            quote_symbol=quote_symbol,
            oracle_type=oracle_type,
            oracle_scale_factor=oracle_scale_factor,
        )
        return await self.stubOracle.Price(req)

    async def fetch_oracle_price(
        self,
        base_symbol: Optional[str] = None,
        quote_symbol: Optional[str] = None,
        oracle_type: Optional[str] = None,
        oracle_scale_factor: Optional[int] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_oracle_api.fetch_oracle_price(
            base_symbol=base_symbol,
            quote_symbol=quote_symbol,
            oracle_type=oracle_type,
            oracle_scale_factor=oracle_scale_factor,
        )

    async def get_oracle_list(self):
        """
        This method is deprecated and will be removed soon. Please use `fetch_oracle_list` instead
        """
        warn("This method is deprecated. Use fetch_oracle_list instead", DeprecationWarning, stacklevel=2)
        req = oracle_rpc_pb.OracleListRequest()
        return await self.stubOracle.OracleList(req)

    async def fetch_oracle_list(self) -> Dict[str, Any]:
        return await self.exchange_oracle_api.fetch_oracle_list()

    # InsuranceRPC

    async def get_insurance_funds(self):
        """
        This method is deprecated and will be removed soon. Please use `fetch_insurance_funds` instead
        """
        warn("This method is deprecated. Use fetch_insurance_funds instead", DeprecationWarning, stacklevel=2)
        req = insurance_rpc_pb.FundsRequest()
        return await self.stubInsurance.Funds(req)

    async def fetch_insurance_funds(self) -> Dict[str, Any]:
        return await self.exchange_insurance_api.fetch_insurance_funds()

    async def get_redemptions(self, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_redemptions` instead
        """
        warn("This method is deprecated. Use fetch_redemptions instead", DeprecationWarning, stacklevel=2)
        req = insurance_rpc_pb.RedemptionsRequest(
            redeemer=kwargs.get("redeemer"),
            redemption_denom=kwargs.get("redemption_denom"),
            status=kwargs.get("status"),
        )
        return await self.stubInsurance.Redemptions(req)

    async def fetch_redemptions(
        self,
        address: Optional[str] = None,
        denom: Optional[str] = None,
        status: Optional[str] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_insurance_api.fetch_redemptions(
            address=address,
            denom=denom,
            status=status,
        )

    # SpotRPC

    async def get_spot_market(self, market_id: str):
        """
        This method is deprecated and will be removed soon. Please use `fetch_spot_market` instead
        """
        warn("This method is deprecated. Use fetch_spot_market instead", DeprecationWarning, stacklevel=2)
        req = spot_exchange_rpc_pb.MarketRequest(market_id=market_id)
        return await self.stubSpotExchange.Market(req)

    async def fetch_spot_market(self, market_id: str) -> Dict[str, Any]:
        return await self.exchange_spot_api.fetch_market(market_id=market_id)

    async def get_spot_markets(self, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_spot_markets` instead
        """
        warn("This method is deprecated. Use fetch_spot_markets instead", DeprecationWarning, stacklevel=2)
        req = spot_exchange_rpc_pb.MarketsRequest(
            market_status=kwargs.get("market_status"),
            base_denom=kwargs.get("base_denom"),
            quote_denom=kwargs.get("quote_denom"),
        )
        return await self.stubSpotExchange.Markets(req)

    async def fetch_spot_markets(
        self,
        market_statuses: Optional[List[str]] = None,
        base_denom: Optional[str] = None,
        quote_denom: Optional[str] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_spot_api.fetch_markets(
            market_statuses=market_statuses, base_denom=base_denom, quote_denom=quote_denom
        )

    async def stream_spot_markets(self, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `listen_spot_markets_updates` instead
        """
        warn("This method is deprecated. Use listen_spot_markets_updates instead", DeprecationWarning, stacklevel=2)

        req = spot_exchange_rpc_pb.StreamMarketsRequest(market_ids=kwargs.get("market_ids"))
        metadata = await self.network.exchange_metadata(
            metadata_query_provider=self._exchange_cookie_metadata_requestor
        )
        return self.stubSpotExchange.StreamMarkets(request=req, metadata=metadata)

    async def listen_spot_markets_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        market_ids: Optional[List[str]] = None,
    ):
        await self.exchange_spot_stream_api.stream_markets(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            market_ids=market_ids,
        )

    async def get_spot_orderbookV2(self, market_id: str):
        """
        This method is deprecated and will be removed soon. Please use `fetch_spot_orderbook_v2` instead
        """
        warn("This method is deprecated. Use fetch_spot_orderbook_v2 instead", DeprecationWarning, stacklevel=2)
        req = spot_exchange_rpc_pb.OrderbookV2Request(market_id=market_id)
        return await self.stubSpotExchange.OrderbookV2(req)

    async def fetch_spot_orderbook_v2(self, market_id: str) -> Dict[str, Any]:
        return await self.exchange_spot_api.fetch_orderbook_v2(market_id=market_id)

    async def get_spot_orderbooksV2(self, market_ids: List):
        """
        This method is deprecated and will be removed soon. Please use `fetch_spot_orderbooks_v2` instead
        """
        warn("This method is deprecated. Use fetch_spot_orderbooks_v2 instead", DeprecationWarning, stacklevel=2)
        req = spot_exchange_rpc_pb.OrderbooksV2Request(market_ids=market_ids)
        return await self.stubSpotExchange.OrderbooksV2(req)

    async def fetch_spot_orderbooks_v2(self, market_ids: List[str]) -> Dict[str, Any]:
        return await self.exchange_spot_api.fetch_orderbooks_v2(market_ids=market_ids)

    async def get_spot_orders(self, market_id: str, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_spot_orders` instead
        """
        warn("This method is deprecated. Use fetch_spot_orders instead", DeprecationWarning, stacklevel=2)
        req = spot_exchange_rpc_pb.OrdersRequest(
            market_id=market_id,
            order_side=kwargs.get("order_side"),
            subaccount_id=kwargs.get("subaccount_id"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
            start_time=kwargs.get("start_time"),
            end_time=kwargs.get("end_time"),
            market_ids=kwargs.get("market_ids"),
            include_inactive=kwargs.get("include_inactive"),
            subaccount_total_orders=kwargs.get("subaccount_total_orders"),
            trade_id=kwargs.get("trade_id"),
            cid=kwargs.get("cid"),
        )
        return await self.stubSpotExchange.Orders(req)

    async def fetch_spot_orders(
        self,
        market_ids: Optional[List[str]] = None,
        order_side: Optional[str] = None,
        subaccount_id: Optional[str] = None,
        include_inactive: Optional[bool] = None,
        subaccount_total_orders: Optional[bool] = None,
        trade_id: Optional[str] = None,
        cid: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_spot_api.fetch_orders(
            market_ids=market_ids,
            order_side=order_side,
            subaccount_id=subaccount_id,
            include_inactive=include_inactive,
            subaccount_total_orders=subaccount_total_orders,
            trade_id=trade_id,
            cid=cid,
            pagination=pagination,
        )

    async def get_historical_spot_orders(self, market_id: Optional[str] = None, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_spot_orders_history` instead
        """
        warn("This method is deprecated. Use fetch_spot_orders_history instead", DeprecationWarning, stacklevel=2)
        market_ids = kwargs.get("market_ids", [])
        if market_id is not None:
            market_ids.append(market_id)
        order_types = kwargs.get("order_types", [])
        order_type = kwargs.get("order_type")
        if order_type is not None:
            order_types.append(market_id)
        req = spot_exchange_rpc_pb.OrdersHistoryRequest(
            subaccount_id=kwargs.get("subaccount_id"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
            order_types=order_types,
            direction=kwargs.get("direction"),
            start_time=kwargs.get("start_time"),
            end_time=kwargs.get("end_time"),
            state=kwargs.get("state"),
            execution_types=kwargs.get("execution_types", []),
            market_ids=market_ids,
            trade_id=kwargs.get("trade_id"),
            active_markets_only=kwargs.get("active_markets_only"),
            cid=kwargs.get("cid"),
        )
        return await self.stubSpotExchange.OrdersHistory(req)

    async def fetch_spot_orders_history(
        self,
        subaccount_id: Optional[str] = None,
        market_ids: Optional[List[str]] = None,
        order_types: Optional[List[str]] = None,
        direction: Optional[str] = None,
        state: Optional[str] = None,
        execution_types: Optional[List[str]] = None,
        trade_id: Optional[str] = None,
        active_markets_only: Optional[bool] = None,
        cid: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_spot_api.fetch_orders_history(
            subaccount_id=subaccount_id,
            market_ids=market_ids,
            order_types=order_types,
            direction=direction,
            state=state,
            execution_types=execution_types,
            trade_id=trade_id,
            active_markets_only=active_markets_only,
            cid=cid,
            pagination=pagination,
        )

    async def get_spot_trades(self, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_spot_trades` instead
        """
        warn("This method is deprecated. Use fetch_spot_trades instead", DeprecationWarning, stacklevel=2)
        req = spot_exchange_rpc_pb.TradesRequest(
            market_id=kwargs.get("market_id"),
            execution_side=kwargs.get("execution_side"),
            direction=kwargs.get("direction"),
            subaccount_id=kwargs.get("subaccount_id"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
            start_time=kwargs.get("start_time"),
            end_time=kwargs.get("end_time"),
            market_ids=kwargs.get("market_ids"),
            subaccount_ids=kwargs.get("subaccount_ids"),
            execution_types=kwargs.get("execution_types"),
            trade_id=kwargs.get("trade_id"),
            account_address=kwargs.get("account_address"),
            cid=kwargs.get("cid"),
        )
        return await self.stubSpotExchange.Trades(req)

    async def fetch_spot_trades(
        self,
        market_ids: Optional[List[str]] = None,
        subaccount_ids: Optional[List[str]] = None,
        execution_side: Optional[str] = None,
        direction: Optional[str] = None,
        execution_types: Optional[List[str]] = None,
        trade_id: Optional[str] = None,
        account_address: Optional[str] = None,
        cid: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_spot_api.fetch_trades_v2(
            market_ids=market_ids,
            subaccount_ids=subaccount_ids,
            execution_side=execution_side,
            direction=direction,
            execution_types=execution_types,
            trade_id=trade_id,
            account_address=account_address,
            cid=cid,
            pagination=pagination,
        )

    async def stream_spot_orderbook_snapshot(self, market_ids: List[str]):
        """
        This method is deprecated and will be removed soon. Please use `listen_spot_orderbook_snapshots` instead
        """
        warn("This method is deprecated. Use listen_spot_orderbook_snapshots instead", DeprecationWarning, stacklevel=2)
        req = spot_exchange_rpc_pb.StreamOrderbookV2Request(market_ids=market_ids)
        metadata = await self.network.exchange_metadata(
            metadata_query_provider=self._exchange_cookie_metadata_requestor
        )
        return self.stubSpotExchange.StreamOrderbookV2(request=req, metadata=metadata)

    async def listen_spot_orderbook_snapshots(
        self,
        market_ids: List[str],
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
    ):
        await self.exchange_spot_stream_api.stream_orderbook_v2(
            market_ids=market_ids,
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
        )

    async def stream_spot_orderbook_update(self, market_ids: List[str]):
        """
        This method is deprecated and will be removed soon. Please use `listen_spot_orderbook_updates` instead
        """
        warn("This method is deprecated. Use listen_spot_orderbook_updates instead", DeprecationWarning, stacklevel=2)
        req = spot_exchange_rpc_pb.StreamOrderbookUpdateRequest(market_ids=market_ids)
        metadata = await self.network.exchange_metadata(
            metadata_query_provider=self._exchange_cookie_metadata_requestor
        )
        return self.stubSpotExchange.StreamOrderbookUpdate(request=req, metadata=metadata)

    async def listen_spot_orderbook_updates(
        self,
        market_ids: List[str],
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
    ):
        await self.exchange_spot_stream_api.stream_orderbook_update(
            market_ids=market_ids,
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
        )

    async def stream_spot_orders(self, market_id: str, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `listen_spot_orders_updates` instead
        """
        warn("This method is deprecated. Use listen_spot_orders_updates instead", DeprecationWarning, stacklevel=2)
        req = spot_exchange_rpc_pb.StreamOrdersRequest(
            market_id=market_id,
            order_side=kwargs.get("order_side"),
            subaccount_id=kwargs.get("subaccount_id"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
            start_time=kwargs.get("start_time"),
            end_time=kwargs.get("end_time"),
            market_ids=kwargs.get("market_ids"),
            include_inactive=kwargs.get("include_inactive"),
            subaccount_total_orders=kwargs.get("subaccount_total_orders"),
            trade_id=kwargs.get("trade_id"),
            cid=kwargs.get("cid"),
        )
        metadata = await self.network.exchange_metadata(
            metadata_query_provider=self._exchange_cookie_metadata_requestor
        )
        return self.stubSpotExchange.StreamOrders(request=req, metadata=metadata)

    async def listen_spot_orders_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        market_ids: Optional[List[str]] = None,
        order_side: Optional[str] = None,
        subaccount_id: Optional[PaginationOption] = None,
        include_inactive: Optional[bool] = None,
        subaccount_total_orders: Optional[bool] = None,
        trade_id: Optional[str] = None,
        cid: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ):
        await self.exchange_spot_stream_api.stream_orders(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            market_ids=market_ids,
            order_side=order_side,
            subaccount_id=subaccount_id,
            include_inactive=include_inactive,
            subaccount_total_orders=subaccount_total_orders,
            trade_id=trade_id,
            cid=cid,
            pagination=pagination,
        )

    async def stream_historical_spot_orders(self, market_id: str, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `listen_spot_orders_history_updates` instead
        """
        warn(
            "This method is deprecated. Use listen_spot_orders_history_updates instead",
            DeprecationWarning,
            stacklevel=2,
        )
        req = spot_exchange_rpc_pb.StreamOrdersHistoryRequest(
            market_id=market_id,
            direction=kwargs.get("direction"),
            subaccount_id=kwargs.get("subaccount_id"),
            order_types=kwargs.get("order_types"),
            state=kwargs.get("state"),
            execution_types=kwargs.get("execution_types"),
        )
        metadata = await self.network.exchange_metadata(
            metadata_query_provider=self._exchange_cookie_metadata_requestor
        )
        return self.stubSpotExchange.StreamOrdersHistory(request=req, metadata=metadata)

    async def listen_spot_orders_history_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        subaccount_id: Optional[str] = None,
        market_id: Optional[str] = None,
        order_types: Optional[List[str]] = None,
        direction: Optional[str] = None,
        state: Optional[str] = None,
        execution_types: Optional[List[str]] = None,
    ):
        await self.exchange_spot_stream_api.stream_orders_history(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            subaccount_id=subaccount_id,
            market_id=market_id,
            order_types=order_types,
            direction=direction,
            state=state,
            execution_types=execution_types,
        )

    async def stream_historical_derivative_orders(self, market_id: str, **kwargs):
        """
        This method is deprecated and will be removed soon.
        Please use `listen_derivative_orders_history_updates` instead
        """
        warn(
            "This method is deprecated. Use listen_derivative_orders_history_updates instead",
            DeprecationWarning,
            stacklevel=2,
        )
        req = derivative_exchange_rpc_pb.StreamOrdersHistoryRequest(
            market_id=market_id,
            direction=kwargs.get("direction"),
            subaccount_id=kwargs.get("subaccount_id"),
            order_types=kwargs.get("order_types"),
            state=kwargs.get("state"),
            execution_types=kwargs.get("execution_types"),
        )
        metadata = await self.network.exchange_metadata(
            metadata_query_provider=self._exchange_cookie_metadata_requestor
        )
        return self.stubDerivativeExchange.StreamOrdersHistory(request=req, metadata=metadata)

    async def listen_derivative_orders_history_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        subaccount_id: Optional[str] = None,
        market_id: Optional[str] = None,
        order_types: Optional[List[str]] = None,
        direction: Optional[str] = None,
        state: Optional[str] = None,
        execution_types: Optional[List[str]] = None,
    ):
        await self.exchange_derivative_stream_api.stream_orders_history(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            subaccount_id=subaccount_id,
            market_id=market_id,
            order_types=order_types,
            direction=direction,
            state=state,
            execution_types=execution_types,
        )

    async def stream_spot_trades(self, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `listen_spot_trades_updates` instead
        """
        warn("This method is deprecated. Use listen_spot_trades_updates instead", DeprecationWarning, stacklevel=2)
        req = spot_exchange_rpc_pb.StreamTradesRequest(
            market_id=kwargs.get("market_id"),
            execution_side=kwargs.get("execution_side"),
            direction=kwargs.get("direction"),
            subaccount_id=kwargs.get("subaccount_id"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
            start_time=kwargs.get("start_time"),
            end_time=kwargs.get("end_time"),
            market_ids=kwargs.get("market_ids"),
            subaccount_ids=kwargs.get("subaccount_ids"),
            execution_types=kwargs.get("execution_types"),
            trade_id=kwargs.get("trade_id"),
            account_address=kwargs.get("account_address"),
            cid=kwargs.get("cid"),
        )
        metadata = await self.network.exchange_metadata(
            metadata_query_provider=self._exchange_cookie_metadata_requestor
        )
        return self.stubSpotExchange.StreamTrades(request=req, metadata=metadata)

    async def listen_spot_trades_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        market_ids: Optional[List[str]] = None,
        subaccount_ids: Optional[List[str]] = None,
        execution_side: Optional[str] = None,
        direction: Optional[str] = None,
        execution_types: Optional[List[str]] = None,
        trade_id: Optional[str] = None,
        account_address: Optional[str] = None,
        cid: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ):
        await self.exchange_spot_stream_api.stream_trades_v2(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            market_ids=market_ids,
            subaccount_ids=subaccount_ids,
            execution_side=execution_side,
            direction=direction,
            execution_types=execution_types,
            trade_id=trade_id,
            account_address=account_address,
            cid=cid,
            pagination=pagination,
        )

    async def get_spot_subaccount_orders(self, subaccount_id: str, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_spot_subaccount_orders_list` instead
        """
        warn(
            "This method is deprecated. Use fetch_spot_subaccount_orders_list instead", DeprecationWarning, stacklevel=2
        )
        req = spot_exchange_rpc_pb.SubaccountOrdersListRequest(
            subaccount_id=subaccount_id,
            market_id=kwargs.get("market_id"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
        )
        return await self.stubSpotExchange.SubaccountOrdersList(req)

    async def fetch_spot_subaccount_orders_list(
        self,
        subaccount_id: str,
        market_id: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_spot_api.fetch_subaccount_orders_list(
            subaccount_id=subaccount_id, market_id=market_id, pagination=pagination
        )

    async def get_spot_subaccount_trades(self, subaccount_id: str, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_spot_subaccount_trades_list` instead
        """
        warn(
            "This method is deprecated. Use fetch_spot_subaccount_trades_list instead", DeprecationWarning, stacklevel=2
        )
        req = spot_exchange_rpc_pb.SubaccountTradesListRequest(
            subaccount_id=subaccount_id,
            market_id=kwargs.get("market_id"),
            execution_type=kwargs.get("execution_type"),
            direction=kwargs.get("direction"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
        )
        return await self.stubSpotExchange.SubaccountTradesList(req)

    async def fetch_spot_subaccount_trades_list(
        self,
        subaccount_id: str,
        market_id: Optional[str] = None,
        execution_type: Optional[str] = None,
        direction: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_spot_api.fetch_subaccount_trades_list(
            subaccount_id=subaccount_id,
            market_id=market_id,
            execution_type=execution_type,
            direction=direction,
            pagination=pagination,
        )

    # DerivativeRPC

    async def get_derivative_market(self, market_id: str):
        """
        This method is deprecated and will be removed soon. Please use `fetch_derivative_market` instead
        """
        warn("This method is deprecated. Use fetch_derivative_market instead", DeprecationWarning, stacklevel=2)
        req = derivative_exchange_rpc_pb.MarketRequest(market_id=market_id)
        return await self.stubDerivativeExchange.Market(req)

    async def fetch_derivative_market(self, market_id: str) -> Dict[str, Any]:
        return await self.exchange_derivative_api.fetch_market(market_id=market_id)

    async def get_derivative_markets(self, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_derivative_markets` instead
        """
        warn("This method is deprecated. Use fetch_derivative_markets instead", DeprecationWarning, stacklevel=2)
        req = derivative_exchange_rpc_pb.MarketsRequest(
            market_status=kwargs.get("market_status"),
            quote_denom=kwargs.get("quote_denom"),
        )
        return await self.stubDerivativeExchange.Markets(req)

    async def fetch_derivative_markets(
        self,
        market_statuses: Optional[List[str]] = None,
        quote_denom: Optional[str] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_derivative_api.fetch_markets(
            market_statuses=market_statuses,
            quote_denom=quote_denom,
        )

    async def stream_derivative_markets(self, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `listen_derivative_market_updates` instead
        """
        warn(
            "This method is deprecated. Use listen_derivative_market_updates instead", DeprecationWarning, stacklevel=2
        )
        req = derivative_exchange_rpc_pb.StreamMarketRequest(market_ids=kwargs.get("market_ids"))
        metadata = await self.network.exchange_metadata(
            metadata_query_provider=self._exchange_cookie_metadata_requestor
        )
        return self.stubDerivativeExchange.StreamMarket(request=req, metadata=metadata)

    async def listen_derivative_market_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        market_ids: Optional[List[str]] = None,
    ):
        await self.exchange_derivative_stream_api.stream_markets(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            market_ids=market_ids,
        )

    async def get_derivative_orderbook(self, market_id: str):
        """
        This method is deprecated and will be removed soon. Please use `fetch_derivative_orderbook_v2` instead
        """
        warn("This method is deprecated. Use fetch_derivative_orderbook_v2 instead", DeprecationWarning, stacklevel=2)
        req = derivative_exchange_rpc_pb.OrderbookV2Request(market_id=market_id)
        return await self.stubDerivativeExchange.OrderbookV2(req)

    async def fetch_derivative_orderbook_v2(self, market_id: str) -> Dict[str, Any]:
        return await self.exchange_derivative_api.fetch_orderbook_v2(market_id=market_id)

    async def get_derivative_orderbooksV2(self, market_ids: List[str]):
        """
        This method is deprecated and will be removed soon. Please use `fetch_derivative_orderbooks_v2` instead
        """
        warn("This method is deprecated. Use fetch_derivative_orderbooks_v2 instead", DeprecationWarning, stacklevel=2)
        req = derivative_exchange_rpc_pb.OrderbooksV2Request(market_ids=market_ids)
        return await self.stubDerivativeExchange.OrderbooksV2(req)

    async def fetch_derivative_orderbooks_v2(self, market_ids: List[str]) -> Dict[str, Any]:
        return await self.exchange_derivative_api.fetch_orderbooks_v2(market_ids=market_ids)

    async def get_derivative_orders(self, market_id: str, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_derivative_orders` instead
        """
        warn("This method is deprecated. Use fetch_derivative_orders instead", DeprecationWarning, stacklevel=2)
        req = derivative_exchange_rpc_pb.OrdersRequest(
            market_id=market_id,
            order_side=kwargs.get("order_side"),
            subaccount_id=kwargs.get("subaccount_id"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
            start_time=kwargs.get("start_time"),
            end_time=kwargs.get("end_time"),
            market_ids=kwargs.get("market_ids"),
            is_conditional=kwargs.get("is_conditional"),
            order_type=kwargs.get("order_type"),
            include_inactive=kwargs.get("include_inactive"),
            subaccount_total_orders=kwargs.get("subaccount_total_orders"),
            trade_id=kwargs.get("trade_id"),
            cid=kwargs.get("cid"),
        )
        return await self.stubDerivativeExchange.Orders(req)

    async def fetch_derivative_orders(
        self,
        market_ids: Optional[List[str]] = None,
        order_side: Optional[str] = None,
        subaccount_id: Optional[str] = None,
        is_conditional: Optional[str] = None,
        order_type: Optional[str] = None,
        include_inactive: Optional[bool] = None,
        subaccount_total_orders: Optional[bool] = None,
        trade_id: Optional[str] = None,
        cid: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_derivative_api.fetch_orders(
            market_ids=market_ids,
            order_side=order_side,
            subaccount_id=subaccount_id,
            is_conditional=is_conditional,
            order_type=order_type,
            include_inactive=include_inactive,
            subaccount_total_orders=subaccount_total_orders,
            trade_id=trade_id,
            cid=cid,
            pagination=pagination,
        )

    async def get_historical_derivative_orders(self, market_id: Optional[str] = None, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_derivative_orders_history` instead
        """
        warn("This method is deprecated. Use fetch_derivative_orders_history instead", DeprecationWarning, stacklevel=2)
        market_ids = kwargs.get("market_ids", [])
        if market_id is not None:
            market_ids.append(market_id)
        order_types = kwargs.get("order_types", [])
        order_type = kwargs.get("order_type")
        if order_type is not None:
            order_types.append(market_id)
        req = derivative_exchange_rpc_pb.OrdersHistoryRequest(
            subaccount_id=kwargs.get("subaccount_id"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
            order_types=order_types,
            direction=kwargs.get("direction"),
            start_time=kwargs.get("start_time"),
            end_time=kwargs.get("end_time"),
            is_conditional=kwargs.get("is_conditional"),
            state=kwargs.get("state"),
            execution_types=kwargs.get("execution_types", []),
            market_ids=market_ids,
            trade_id=kwargs.get("trade_id"),
            active_markets_only=kwargs.get("active_markets_only"),
            cid=kwargs.get("cid"),
        )
        return await self.stubDerivativeExchange.OrdersHistory(req)

    async def fetch_derivative_orders_history(
        self,
        subaccount_id: Optional[str] = None,
        market_ids: Optional[List[str]] = None,
        order_types: Optional[List[str]] = None,
        direction: Optional[str] = None,
        is_conditional: Optional[str] = None,
        state: Optional[str] = None,
        execution_types: Optional[List[str]] = None,
        trade_id: Optional[str] = None,
        active_markets_only: Optional[bool] = None,
        cid: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_derivative_api.fetch_orders_history(
            subaccount_id=subaccount_id,
            market_ids=market_ids,
            order_types=order_types,
            direction=direction,
            is_conditional=is_conditional,
            state=state,
            execution_types=execution_types,
            trade_id=trade_id,
            active_markets_only=active_markets_only,
            cid=cid,
            pagination=pagination,
        )

    async def get_derivative_trades(self, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_derivative_trades` instead
        """
        warn("This method is deprecated. Use fetch_derivative_trades instead", DeprecationWarning, stacklevel=2)
        req = derivative_exchange_rpc_pb.TradesRequest(
            market_id=kwargs.get("market_id"),
            execution_side=kwargs.get("execution_side"),
            direction=kwargs.get("direction"),
            subaccount_id=kwargs.get("subaccount_id"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
            start_time=kwargs.get("start_time"),
            end_time=kwargs.get("end_time"),
            market_ids=kwargs.get("market_ids"),
            subaccount_ids=kwargs.get("subaccount_ids"),
            execution_types=kwargs.get("execution_types"),
            trade_id=kwargs.get("trade_id"),
            account_address=kwargs.get("account_address"),
            cid=kwargs.get("cid"),
        )
        return await self.stubDerivativeExchange.Trades(req)

    async def fetch_derivative_trades(
        self,
        market_ids: Optional[List[str]] = None,
        subaccount_ids: Optional[List[str]] = None,
        execution_side: Optional[str] = None,
        direction: Optional[str] = None,
        execution_types: Optional[List[str]] = None,
        trade_id: Optional[str] = None,
        account_address: Optional[str] = None,
        cid: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_derivative_api.fetch_trades_v2(
            market_ids=market_ids,
            subaccount_ids=subaccount_ids,
            execution_side=execution_side,
            direction=direction,
            execution_types=execution_types,
            trade_id=trade_id,
            account_address=account_address,
            cid=cid,
            pagination=pagination,
        )

    async def stream_derivative_orderbook_snapshot(self, market_ids: List[str]):
        """
        This method is deprecated and will be removed soon. Please use `listen_derivative_orderbook_snapshots` instead
        """
        warn(
            "This method is deprecated. Use listen_derivative_orderbook_snapshots instead",
            DeprecationWarning,
            stacklevel=2,
        )
        req = derivative_exchange_rpc_pb.StreamOrderbookV2Request(market_ids=market_ids)
        metadata = await self.network.exchange_metadata(
            metadata_query_provider=self._exchange_cookie_metadata_requestor
        )
        return self.stubDerivativeExchange.StreamOrderbookV2(request=req, metadata=metadata)

    async def listen_derivative_orderbook_snapshots(
        self,
        market_ids: List[str],
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
    ):
        await self.exchange_derivative_stream_api.stream_orderbook_v2(
            market_ids=market_ids,
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
        )

    async def stream_derivative_orderbook_update(self, market_ids: List[str]):
        """
        This method is deprecated and will be removed soon. Please use `listen_derivative_orderbook_updates` instead
        """
        warn(
            "This method is deprecated. Use listen_derivative_orderbook_updates instead",
            DeprecationWarning,
            stacklevel=2,
        )
        req = derivative_exchange_rpc_pb.StreamOrderbookUpdateRequest(market_ids=market_ids)
        metadata = await self.network.exchange_metadata(
            metadata_query_provider=self._exchange_cookie_metadata_requestor
        )
        return self.stubDerivativeExchange.StreamOrderbookUpdate(request=req, metadata=metadata)

    async def listen_derivative_orderbook_updates(
        self,
        market_ids: List[str],
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
    ):
        await self.exchange_derivative_stream_api.stream_orderbook_update(
            market_ids=market_ids,
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
        )

    async def stream_derivative_orders(self, market_id: str, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `listen_derivative_orders_updates` instead
        """
        warn(
            "This method is deprecated. Use listen_derivative_orders_updates instead", DeprecationWarning, stacklevel=2
        )
        req = derivative_exchange_rpc_pb.StreamOrdersRequest(
            market_id=market_id,
            order_side=kwargs.get("order_side"),
            subaccount_id=kwargs.get("subaccount_id"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
            start_time=kwargs.get("start_time"),
            end_time=kwargs.get("end_time"),
            market_ids=kwargs.get("market_ids"),
            is_conditional=kwargs.get("is_conditional"),
            order_type=kwargs.get("order_type"),
            include_inactive=kwargs.get("include_inactive"),
            subaccount_total_orders=kwargs.get("subaccount_total_orders"),
            trade_id=kwargs.get("trade_id"),
            cid=kwargs.get("cid"),
        )
        metadata = await self.network.exchange_metadata(
            metadata_query_provider=self._exchange_cookie_metadata_requestor
        )
        return self.stubDerivativeExchange.StreamOrders(request=req, metadata=metadata)

    async def listen_derivative_orders_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        market_ids: Optional[List[str]] = None,
        order_side: Optional[str] = None,
        subaccount_id: Optional[PaginationOption] = None,
        is_conditional: Optional[str] = None,
        order_type: Optional[str] = None,
        include_inactive: Optional[bool] = None,
        subaccount_total_orders: Optional[bool] = None,
        trade_id: Optional[str] = None,
        cid: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ):
        await self.exchange_derivative_stream_api.stream_orders(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            market_ids=market_ids,
            order_side=order_side,
            subaccount_id=subaccount_id,
            is_conditional=is_conditional,
            order_type=order_type,
            include_inactive=include_inactive,
            subaccount_total_orders=subaccount_total_orders,
            trade_id=trade_id,
            cid=cid,
            pagination=pagination,
        )

    async def stream_derivative_trades(self, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `listen_derivative_trades_updates` instead
        """
        warn(
            "This method is deprecated. Use listen_derivative_trades_updates instead", DeprecationWarning, stacklevel=2
        )
        req = derivative_exchange_rpc_pb.StreamTradesRequest(
            market_id=kwargs.get("market_id"),
            execution_side=kwargs.get("execution_side"),
            direction=kwargs.get("direction"),
            subaccount_id=kwargs.get("subaccount_id"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
            start_time=kwargs.get("start_time"),
            end_time=kwargs.get("end_time"),
            market_ids=kwargs.get("market_ids"),
            subaccount_ids=kwargs.get("subaccount_ids"),
            execution_types=kwargs.get("execution_types"),
            trade_id=kwargs.get("trade_id"),
            account_address=kwargs.get("account_address"),
            cid=kwargs.get("cid"),
        )
        metadata = await self.network.exchange_metadata(
            metadata_query_provider=self._exchange_cookie_metadata_requestor
        )
        return self.stubDerivativeExchange.StreamTrades(request=req, metadata=metadata)

    async def listen_derivative_trades_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        market_ids: Optional[List[str]] = None,
        execution_side: Optional[str] = None,
        direction: Optional[str] = None,
        subaccount_ids: Optional[List[str]] = None,
        execution_types: Optional[List[str]] = None,
        trade_id: Optional[str] = None,
        account_address: Optional[str] = None,
        cid: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ):
        return await self.exchange_derivative_stream_api.stream_trades_v2(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            market_ids=market_ids,
            subaccount_ids=subaccount_ids,
            execution_side=execution_side,
            direction=direction,
            execution_types=execution_types,
            trade_id=trade_id,
            account_address=account_address,
            cid=cid,
            pagination=pagination,
        )

    async def get_derivative_positions(self, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_derivative_positions_v2` instead
        """
        warn("This method is deprecated. Use fetch_derivative_positions_v2 instead", DeprecationWarning, stacklevel=2)
        req = derivative_exchange_rpc_pb.PositionsRequest(
            market_id=kwargs.get("market_id"),
            market_ids=kwargs.get("market_ids"),
            subaccount_id=kwargs.get("subaccount_id"),
            direction=kwargs.get("direction"),
            subaccount_total_positions=kwargs.get("subaccount_total_positions"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
        )
        return await self.stubDerivativeExchange.Positions(req)

    async def fetch_derivative_positions_v2(
        self,
        market_ids: Optional[List[str]] = None,
        subaccount_id: Optional[str] = None,
        direction: Optional[str] = None,
        subaccount_total_positions: Optional[bool] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_derivative_api.fetch_positions_v2(
            market_ids=market_ids,
            subaccount_id=subaccount_id,
            direction=direction,
            subaccount_total_positions=subaccount_total_positions,
            pagination=pagination,
        )

    async def stream_derivative_positions(self, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `listen_derivative_positions_updates` instead
        """
        warn(
            "This method is deprecated. Use listen_derivative_positions_updates instead",
            DeprecationWarning,
            stacklevel=2,
        )
        req = derivative_exchange_rpc_pb.StreamPositionsRequest(
            market_id=kwargs.get("market_id"),
            market_ids=kwargs.get("market_ids"),
            subaccount_id=kwargs.get("subaccount_id"),
            subaccount_ids=kwargs.get("subaccount_ids"),
        )
        metadata = await self.network.exchange_metadata(
            metadata_query_provider=self._exchange_cookie_metadata_requestor
        )
        return self.stubDerivativeExchange.StreamPositions(request=req, metadata=metadata)

    async def listen_derivative_positions_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        market_ids: Optional[List[str]] = None,
        subaccount_ids: Optional[List[str]] = None,
    ):
        await self.exchange_derivative_stream_api.stream_positions(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            market_ids=market_ids,
            subaccount_ids=subaccount_ids,
        )

    async def get_derivative_liquidable_positions(self, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_derivative_liquidable_positions` instead
        """
        warn(
            "This method is deprecated. Use fetch_derivative_liquidable_positions instead",
            DeprecationWarning,
            stacklevel=2,
        )
        req = derivative_exchange_rpc_pb.LiquidablePositionsRequest(
            market_id=kwargs.get("market_id"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
        )
        return await self.stubDerivativeExchange.LiquidablePositions(req)

    async def fetch_derivative_liquidable_positions(
        self,
        market_id: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_derivative_api.fetch_liquidable_positions(
            market_id=market_id,
            pagination=pagination,
        )

    async def get_derivative_subaccount_orders(self, subaccount_id: str, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_derivative_subaccount_orders` instead
        """
        warn(
            "This method is deprecated. Use fetch_derivative_subaccount_orders instead",
            DeprecationWarning,
            stacklevel=2,
        )
        req = derivative_exchange_rpc_pb.SubaccountOrdersListRequest(
            subaccount_id=subaccount_id,
            market_id=kwargs.get("market_id"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
        )
        return await self.stubDerivativeExchange.SubaccountOrdersList(req)

    async def fetch_subaccount_orders_list(
        self,
        subaccount_id: str,
        market_id: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_derivative_api.fetch_subaccount_orders_list(
            subaccount_id=subaccount_id, market_id=market_id, pagination=pagination
        )

    async def get_derivative_subaccount_trades(self, subaccount_id: str, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_derivative_subaccount_trades` instead
        """
        warn(
            "This method is deprecated. Use fetch_derivative_subaccount_trades instead",
            DeprecationWarning,
            stacklevel=2,
        )
        req = derivative_exchange_rpc_pb.SubaccountTradesListRequest(
            subaccount_id=subaccount_id,
            market_id=kwargs.get("market_id"),
            execution_type=kwargs.get("execution_type"),
            direction=kwargs.get("direction"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
        )
        return await self.stubDerivativeExchange.SubaccountTradesList(req)

    async def fetch_derivative_subaccount_trades_list(
        self,
        subaccount_id: str,
        market_id: Optional[str] = None,
        execution_type: Optional[str] = None,
        direction: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_derivative_api.fetch_subaccount_trades_list(
            subaccount_id=subaccount_id,
            market_id=market_id,
            execution_type=execution_type,
            direction=direction,
            pagination=pagination,
        )

    async def get_funding_payments(self, subaccount_id: str, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_funding_payments` instead
        """
        warn("This method is deprecated. Use fetch_funding_payments instead", DeprecationWarning, stacklevel=2)
        req = derivative_exchange_rpc_pb.FundingPaymentsRequest(
            subaccount_id=subaccount_id,
            market_id=kwargs.get("market_id"),
            market_ids=kwargs.get("market_ids"),
            skip=kwargs.get("skip"),
            end_time=kwargs.get("end_time"),
            limit=kwargs.get("limit"),
        )
        return await self.stubDerivativeExchange.FundingPayments(req)

    async def fetch_funding_payments(
        self,
        market_ids: Optional[List[str]] = None,
        subaccount_id: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_derivative_api.fetch_funding_payments(
            market_ids=market_ids, subaccount_id=subaccount_id, pagination=pagination
        )

    async def get_funding_rates(self, market_id: str, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_funding_rates` instead
        """
        warn("This method is deprecated. Use fetch_funding_rates instead", DeprecationWarning, stacklevel=2)
        req = derivative_exchange_rpc_pb.FundingRatesRequest(
            market_id=market_id,
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
            end_time=kwargs.get("end_time"),
        )
        return await self.stubDerivativeExchange.FundingRates(req)

    async def fetch_funding_rates(
        self,
        market_id: str,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_derivative_api.fetch_funding_rates(market_id=market_id, pagination=pagination)

    async def get_binary_options_markets(self, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `fetch_binary_options_markets` instead
        """
        warn("This method is deprecated. Use fetch_binary_options_markets instead", DeprecationWarning, stacklevel=2)
        req = derivative_exchange_rpc_pb.BinaryOptionsMarketsRequest(
            market_status=kwargs.get("market_status"),
            quote_denom=kwargs.get("quote_denom"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
        )
        return await self.stubDerivativeExchange.BinaryOptionsMarkets(req)

    async def fetch_binary_options_markets(
        self,
        market_status: Optional[str] = None,
        quote_denom: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.exchange_derivative_api.fetch_binary_options_markets(
            market_status=market_status,
            quote_denom=quote_denom,
            pagination=pagination,
        )

    async def get_binary_options_market(self, market_id: str):
        """
        This method is deprecated and will be removed soon. Please use `fetch_binary_options_market` instead
        """
        warn("This method is deprecated. Use fetch_binary_options_market instead", DeprecationWarning, stacklevel=2)
        req = derivative_exchange_rpc_pb.BinaryOptionsMarketRequest(market_id=market_id)
        return await self.stubDerivativeExchange.BinaryOptionsMarket(req)

    async def fetch_binary_options_market(self, market_id: str) -> Dict[str, Any]:
        return await self.exchange_derivative_api.fetch_binary_options_market(market_id=market_id)

    # PortfolioRPC

    async def get_account_portfolio(self, account_address: str):
        """
        This method is deprecated and will be removed soon. Please use `fetch_account_portfolio_balances` instead
        """
        warn(
            "This method is deprecated. Use fetch_account_portfolio_balances instead", DeprecationWarning, stacklevel=2
        )
        req = portfolio_rpc_pb.AccountPortfolioRequest(account_address=account_address)
        return await self.stubPortfolio.AccountPortfolio(req)

    async def fetch_account_portfolio_balances(self, account_address: str) -> Dict[str, Any]:
        return await self.exchange_portfolio_api.fetch_account_portfolio_balances(account_address=account_address)

    async def stream_account_portfolio(self, account_address: str, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `listen_account_portfolio_updates` instead
        """
        warn(
            "This method is deprecated. Use listen_account_portfolio_updates instead", DeprecationWarning, stacklevel=2
        )
        req = portfolio_rpc_pb.StreamAccountPortfolioRequest(
            account_address=account_address, subaccount_id=kwargs.get("subaccount_id"), type=kwargs.get("type")
        )
        metadata = await self.network.exchange_metadata(
            metadata_query_provider=self._exchange_cookie_metadata_requestor
        )
        return self.stubPortfolio.StreamAccountPortfolio(request=req, metadata=metadata)

    async def listen_account_portfolio_updates(
        self,
        account_address: str,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        subaccount_id: Optional[str] = None,
        update_type: Optional[str] = None,
    ):
        await self.exchange_portfolio_stream_api.stream_account_portfolio(
            account_address=account_address,
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            subaccount_id=subaccount_id,
            update_type=update_type,
        )

    async def chain_stream(
        self,
        bank_balances_filter: Optional[chain_stream_query.BankBalancesFilter] = None,
        subaccount_deposits_filter: Optional[chain_stream_query.SubaccountDepositsFilter] = None,
        spot_trades_filter: Optional[chain_stream_query.TradesFilter] = None,
        derivative_trades_filter: Optional[chain_stream_query.TradesFilter] = None,
        spot_orders_filter: Optional[chain_stream_query.OrdersFilter] = None,
        derivative_orders_filter: Optional[chain_stream_query.OrdersFilter] = None,
        spot_orderbooks_filter: Optional[chain_stream_query.OrderbookFilter] = None,
        derivative_orderbooks_filter: Optional[chain_stream_query.OrderbookFilter] = None,
        positions_filter: Optional[chain_stream_query.PositionsFilter] = None,
        oracle_price_filter: Optional[chain_stream_query.OraclePriceFilter] = None,
    ):
        """
        This method is deprecated and will be removed soon. Please use `listen_chain_stream_updates` instead
        """
        warn("This method is deprecated. Use listen_chain_stream_updates instead", DeprecationWarning, stacklevel=2)
        request = chain_stream_query.StreamRequest(
            bank_balances_filter=bank_balances_filter,
            subaccount_deposits_filter=subaccount_deposits_filter,
            spot_trades_filter=spot_trades_filter,
            derivative_trades_filter=derivative_trades_filter,
            spot_orders_filter=spot_orders_filter,
            derivative_orders_filter=derivative_orders_filter,
            spot_orderbooks_filter=spot_orderbooks_filter,
            derivative_orderbooks_filter=derivative_orderbooks_filter,
            positions_filter=positions_filter,
            oracle_price_filter=oracle_price_filter,
        )
        metadata = await self.network.chain_metadata(metadata_query_provider=self._chain_cookie_metadata_requestor)
        return self.chain_stream_stub.Stream(request=request, metadata=metadata)

    async def listen_chain_stream_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        bank_balances_filter: Optional[chain_stream_query.BankBalancesFilter] = None,
        subaccount_deposits_filter: Optional[chain_stream_query.SubaccountDepositsFilter] = None,
        spot_trades_filter: Optional[chain_stream_query.TradesFilter] = None,
        derivative_trades_filter: Optional[chain_stream_query.TradesFilter] = None,
        spot_orders_filter: Optional[chain_stream_query.OrdersFilter] = None,
        derivative_orders_filter: Optional[chain_stream_query.OrdersFilter] = None,
        spot_orderbooks_filter: Optional[chain_stream_query.OrderbookFilter] = None,
        derivative_orderbooks_filter: Optional[chain_stream_query.OrderbookFilter] = None,
        positions_filter: Optional[chain_stream_query.PositionsFilter] = None,
        oracle_price_filter: Optional[chain_stream_query.OraclePriceFilter] = None,
    ):
        return await self.chain_stream_api.stream(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            bank_balances_filter=bank_balances_filter,
            subaccount_deposits_filter=subaccount_deposits_filter,
            spot_trades_filter=spot_trades_filter,
            derivative_trades_filter=derivative_trades_filter,
            spot_orders_filter=spot_orders_filter,
            derivative_orders_filter=derivative_orders_filter,
            spot_orderbooks_filter=spot_orderbooks_filter,
            derivative_orderbooks_filter=derivative_orderbooks_filter,
            positions_filter=positions_filter,
            oracle_price_filter=oracle_price_filter,
        )

    async def composer(self):
        return Composer(
            network=self.network.string(),
            spot_markets=await self.all_spot_markets(),
            derivative_markets=await self.all_derivative_markets(),
            binary_option_markets=await self.all_binary_option_markets(),
            tokens=await self.all_tokens(),
        )

    async def initialize_tokens_from_chain_denoms(self):
        # force initialization of markets and tokens
        await self.all_tokens()

        all_denoms_metadata = []

        query_result = await self.fetch_denoms_metadata()

        all_denoms_metadata.extend(query_result.get("metadatas", []))
        next_key = query_result.get("pagination", {}).get("nextKey", "")

        while next_key != "":
            query_result = await self.fetch_denoms_metadata(pagination=PaginationOption(key=next_key))

            all_denoms_metadata.extend(query_result.get("metadatas", []))
            result_next_key = query_result.get("pagination", {}).get("nextKey", "")
            next_key = base64.b64decode(result_next_key).decode()

        for token_metadata in all_denoms_metadata:
            symbol = token_metadata["symbol"]
            denom = token_metadata["base"]

            if denom != "" and symbol != "" and denom not in self._tokens_by_denom:
                name = token_metadata["name"] or symbol
                decimals = max({denom_unit["exponent"] for denom_unit in token_metadata["denomUnits"]})

                unique_symbol = denom
                for symbol_candidate in [symbol, name]:
                    if symbol_candidate not in self._tokens_by_symbol:
                        unique_symbol = symbol_candidate
                        break

                token = Token(
                    name=name,
                    symbol=symbol,
                    denom=denom,
                    address="",
                    decimals=decimals,
                    logo=token_metadata["uri"],
                    updated=-1,
                )

                self._tokens_by_denom[denom] = token
                self._tokens_by_symbol[unique_symbol] = token

    async def _initialize_tokens_and_markets(self):
        spot_markets = dict()
        derivative_markets = dict()
        binary_option_markets = dict()
        tokens_by_symbol = dict()
        tokens_by_denom = dict()
        markets_info = (await self.fetch_spot_markets(market_statuses=["active"]))["markets"]
        valid_markets = (
            market_info
            for market_info in markets_info
            if len(market_info.get("baseTokenMeta", {}).get("symbol", "")) > 0
            and len(market_info.get("quoteTokenMeta", {}).get("symbol", "")) > 0
        )

        for market_info in valid_markets:
            base_token = self._token_representation(
                token_meta=market_info["baseTokenMeta"],
                denom=market_info["baseDenom"],
                tokens_by_denom=tokens_by_denom,
                tokens_by_symbol=tokens_by_symbol,
            )
            quote_token = self._token_representation(
                token_meta=market_info["quoteTokenMeta"],
                denom=market_info["quoteDenom"],
                tokens_by_denom=tokens_by_denom,
                tokens_by_symbol=tokens_by_symbol,
            )

            market = SpotMarket(
                id=market_info["marketId"],
                status=market_info["marketStatus"],
                ticker=market_info["ticker"],
                base_token=base_token,
                quote_token=quote_token,
                maker_fee_rate=Decimal(market_info["makerFeeRate"]),
                taker_fee_rate=Decimal(market_info["takerFeeRate"]),
                service_provider_fee=Decimal(market_info["serviceProviderFee"]),
                min_price_tick_size=Decimal(market_info["minPriceTickSize"]),
                min_quantity_tick_size=Decimal(market_info["minQuantityTickSize"]),
            )

            spot_markets[market.id] = market

        markets_info = (await self.fetch_derivative_markets(market_statuses=["active"]))["markets"]
        valid_markets = (
            market_info
            for market_info in markets_info
            if len(market_info.get("quoteTokenMeta", {}).get("symbol", "")) > 0
        )

        for market_info in valid_markets:
            quote_token = self._token_representation(
                token_meta=market_info["quoteTokenMeta"],
                denom=market_info["quoteDenom"],
                tokens_by_denom=tokens_by_denom,
                tokens_by_symbol=tokens_by_symbol,
            )

            market = DerivativeMarket(
                id=market_info["marketId"],
                status=market_info["marketStatus"],
                ticker=market_info["ticker"],
                oracle_base=market_info["oracleBase"],
                oracle_quote=market_info["oracleQuote"],
                oracle_type=market_info["oracleType"],
                oracle_scale_factor=market_info["oracleScaleFactor"],
                initial_margin_ratio=Decimal(market_info["initialMarginRatio"]),
                maintenance_margin_ratio=Decimal(market_info["maintenanceMarginRatio"]),
                quote_token=quote_token,
                maker_fee_rate=Decimal(market_info["makerFeeRate"]),
                taker_fee_rate=Decimal(market_info["takerFeeRate"]),
                service_provider_fee=Decimal(market_info["serviceProviderFee"]),
                min_price_tick_size=Decimal(market_info["minPriceTickSize"]),
                min_quantity_tick_size=Decimal(market_info["minQuantityTickSize"]),
            )

            derivative_markets[market.id] = market

        markets_info = (await self.fetch_binary_options_markets(market_status="active"))["markets"]
        for market_info in markets_info:
            quote_token = tokens_by_denom.get(market_info["quoteDenom"], None)

            market = BinaryOptionMarket(
                id=market_info["marketId"],
                status=market_info["marketStatus"],
                ticker=market_info["ticker"],
                oracle_symbol=market_info["oracleSymbol"],
                oracle_provider=market_info["oracleProvider"],
                oracle_type=market_info["oracleType"],
                oracle_scale_factor=market_info["oracleScaleFactor"],
                expiration_timestamp=market_info["expirationTimestamp"],
                settlement_timestamp=market_info["settlementTimestamp"],
                quote_token=quote_token,
                maker_fee_rate=Decimal(market_info["makerFeeRate"]),
                taker_fee_rate=Decimal(market_info["takerFeeRate"]),
                service_provider_fee=Decimal(market_info["serviceProviderFee"]),
                min_price_tick_size=Decimal(market_info["minPriceTickSize"]),
                min_quantity_tick_size=Decimal(market_info["minQuantityTickSize"]),
                settlement_price=None
                if market_info["settlementPrice"] == ""
                else Decimal(market_info["settlementPrice"]),
            )

            binary_option_markets[market.id] = market

        self._tokens_by_denom = tokens_by_denom
        self._tokens_by_symbol = tokens_by_symbol
        self._spot_markets = spot_markets
        self._derivative_markets = derivative_markets
        self._binary_option_markets = binary_option_markets

    def _token_representation(
        self,
        token_meta: Dict[str, Any],
        denom: str,
        tokens_by_denom: Dict[str, Token],
        tokens_by_symbol: Dict[str, Token],
    ) -> Token:
        if denom not in tokens_by_denom:
            unique_symbol = denom
            for symbol_candidate in [token_meta["symbol"], token_meta["name"]]:
                if symbol_candidate not in tokens_by_symbol:
                    unique_symbol = symbol_candidate
                    break

            token = Token(
                name=token_meta["name"],
                symbol=token_meta["symbol"],
                denom=denom,
                address=token_meta["address"],
                decimals=token_meta["decimals"],
                logo=token_meta["logo"],
                updated=int(token_meta["updatedAt"]),
            )

            tokens_by_denom[denom] = token
            tokens_by_symbol[unique_symbol] = token

        return tokens_by_denom[denom]

    def _chain_cookie_metadata_requestor(self) -> Coroutine:
        request = tendermint_query.GetLatestBlockRequest()
        return self.stubCosmosTendermint.GetLatestBlock(request).initial_metadata()

    def _exchange_cookie_metadata_requestor(self) -> Coroutine:
        request = exchange_meta_rpc_pb.VersionRequest()
        return self.stubMeta.Version(request).initial_metadata()

    def _explorer_cookie_metadata_requestor(self) -> Coroutine:
        request = explorer_rpc_pb.GetBlocksRequest()
        return self.stubExplorer.GetBlocks(request).initial_metadata()

    def _initialize_timeout_height_sync_task(self):
        self._cancel_timeout_height_sync_task()
        self._timeout_height_sync_task = asyncio.get_event_loop().create_task(self._timeout_height_sync_process())

    async def _timeout_height_sync_process(self):
        while True:
            await self.sync_timeout_height()
            await asyncio.sleep(DEFAULT_TIMEOUTHEIGHT_SYNC_INTERVAL)

    def _cancel_timeout_height_sync_task(self):
        if self._timeout_height_sync_task is not None:
            self._timeout_height_sync_task.cancel()
        self._timeout_height_sync_task = None
