import asyncio
import time
from copy import deepcopy
from decimal import Decimal
from typing import Any, Callable, Dict, List, Optional, Tuple, Union
from warnings import warn

import grpc
from google.protobuf import json_format

from pyinjective.client.chain.grpc.chain_grpc_auth_api import ChainGrpcAuthApi
from pyinjective.client.chain.grpc.chain_grpc_authz_api import ChainGrpcAuthZApi
from pyinjective.client.chain.grpc.chain_grpc_bank_api import ChainGrpcBankApi
from pyinjective.client.chain.grpc.chain_grpc_distribution_api import ChainGrpcDistributionApi
from pyinjective.client.chain.grpc.chain_grpc_exchange_api import ChainGrpcExchangeApi
from pyinjective.client.chain.grpc.chain_grpc_permissions_api import ChainGrpcPermissionsApi
from pyinjective.client.chain.grpc.chain_grpc_token_factory_api import ChainGrpcTokenFactoryApi
from pyinjective.client.chain.grpc.chain_grpc_wasm_api import ChainGrpcWasmApi
from pyinjective.client.chain.grpc_stream import ChainGrpcChainStream
from pyinjective.client.model import PaginationOption
from pyinjective.composer import Composer
from pyinjective.core.ibc.channel.grpc import IBCChannelGrpcApi
from pyinjective.core.ibc.client.grpc import IBCClientGrpcApi
from pyinjective.core.ibc.connection.grpc import IBCConnectionGrpcApi
from pyinjective.core.ibc.transfer.grpc import IBCTransferGrpcApi
from pyinjective.core.market import BinaryOptionMarket, DerivativeMarket, SpotMarket
from pyinjective.core.network import Network
from pyinjective.core.tendermint.grpc import TendermintGrpcApi
from pyinjective.core.token import Token
from pyinjective.core.tokens_file_loader import TokensFileLoader
from pyinjective.core.tx.grpc import TxGrpcApi
from pyinjective.exceptions import NotFoundError
from pyinjective.proto.cosmos.auth.v1beta1 import query_pb2 as auth_query, query_pb2_grpc as auth_query_grpc
from pyinjective.proto.cosmos.authz.v1beta1 import query_pb2 as authz_query, query_pb2_grpc as authz_query_grpc
from pyinjective.proto.cosmos.bank.v1beta1 import query_pb2 as bank_query, query_pb2_grpc as bank_query_grpc
from pyinjective.proto.cosmos.base.abci.v1beta1 import abci_pb2 as abci_type
from pyinjective.proto.cosmos.base.tendermint.v1beta1 import (
    query_pb2 as tendermint_query,
    query_pb2_grpc as tendermint_query_grpc,
)
from pyinjective.proto.cosmos.crypto.ed25519 import keys_pb2 as ed25519_keys  # noqa: F401 for validator set responses
from pyinjective.proto.cosmos.tx.v1beta1 import service_pb2 as tx_service, service_pb2_grpc as tx_service_grpc

from pyinjective.proto.ibc.lightclients.tendermint.v1 import (  # noqa: F401 for validator set responses
    tendermint_pb2 as ibc_tendermint,
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
        credentials=None,
    ):
        # the `insecure` parameter is ignored and will be deprecated soon. The value is taken directly from `network`
        if insecure is not None:
            warn(
                "insecure parameter in AsyncClient is no longer used and will be deprecated",
                DeprecationWarning,
                stacklevel=2,
            )
        # the `credentials` parameter is ignored and will be deprecated soon. The value is taken directly from `network`
        if credentials is not None:
            warn(
                "credentials parameter in AsyncClient is no longer used and will be deprecated",
                DeprecationWarning,
                stacklevel=2,
            )

        self.addr = ""
        self.number = 0
        self.sequence = 0

        self.network = network

        # chain stubs
        self.chain_channel = self.network.create_chain_grpc_channel()

        self.stubCosmosTendermint = tendermint_query_grpc.ServiceStub(self.chain_channel)
        self.stubAuth = auth_query_grpc.QueryStub(self.chain_channel)
        self.stubAuthz = authz_query_grpc.QueryStub(self.chain_channel)
        self.stubBank = bank_query_grpc.QueryStub(self.chain_channel)
        self.stubTx = tx_service_grpc.ServiceStub(self.chain_channel)

        self.exchange_cookie = ""
        self.timeout_height = 1

        # exchange stubs

        self.chain_stream_channel = self.network.create_chain_stream_grpc_channel()
        self.chain_stream_stub = stream_rpc_grpc.StreamStub(channel=self.chain_stream_channel)

        self._timeout_height_sync_task = None
        self._initialize_timeout_height_sync_task()

        self._tokens_and_markets_initialization_lock = asyncio.Lock()
        self._tokens_by_denom = dict()
        self._tokens_by_symbol = dict()
        self._spot_markets: Optional[Dict[str, SpotMarket]] = None
        self._derivative_markets: Optional[Dict[str, DerivativeMarket]] = None
        self._binary_option_markets: Optional[Dict[str, BinaryOptionMarket]] = None

        self.bank_api = ChainGrpcBankApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.auth_api = ChainGrpcAuthApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.authz_api = ChainGrpcAuthZApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.distribution_api = ChainGrpcDistributionApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.chain_exchange_api = ChainGrpcExchangeApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.ibc_channel_api = IBCChannelGrpcApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.ibc_client_api = IBCClientGrpcApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.ibc_connection_api = IBCConnectionGrpcApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.ibc_transfer_api = IBCTransferGrpcApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.permissions_api = ChainGrpcPermissionsApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.tendermint_api = TendermintGrpcApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.token_factory_api = ChainGrpcTokenFactoryApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.tx_api = TxGrpcApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.wasm_api = ChainGrpcWasmApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )

        self.chain_stream_api = ChainGrpcChainStream(
            channel=self.chain_stream_channel,
            cookie_assistant=network.chain_cookie_assistant,
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
            block = await self.fetch_latest_block()
            self.timeout_height = int(block["block"]["header"]["height"]) + DEFAULT_TIMEOUTHEIGHT
        except Exception as e:
            LoggerProvider().logger_for_class(logging_class=self.__class__).debug(
                f"error while fetching latest block, setting timeout height to 0: {e}"
            )
            self.timeout_height = 0

    # default client methods

    async def get_account(self, address: str) -> Optional[account_pb2.EthAccount]:
        """
        This method is deprecated and will be removed soon. Please use `fetch_account` instead
        """
        warn("This method is deprecated. Use fetch_account instead", DeprecationWarning, stacklevel=2)

        try:
            metadata = self.network.chain_cookie_assistant.metadata()
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
            metadata = self.network.chain_cookie_assistant.metadata()
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
        metadata = self.network.chain_cookie_assistant.metadata()
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
        metadata = self.network.chain_cookie_assistant.metadata()
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
        metadata = self.network.chain_cookie_assistant.metadata()
        result = await self.stubTx.BroadcastTx(request=req, metadata=metadata)
        return result.tx_response

    async def get_chain_id(self) -> str:
        latest_block = await self.fetch_latest_block()
        return latest_block["block"]["header"]["chainId"]

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

    async def fetch_spot_markets(
        self,
        status: Optional[str] = None,
        market_ids: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_spot_markets(
            status=status,
            market_ids=market_ids,
        )

    async def fetch_spot_market(
        self,
        market_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_spot_market(
            market_id=market_id,
        )

    async def fetch_full_spot_markets(
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

    async def fetch_full_spot_market(
        self,
        market_id: str,
        with_mid_price_and_tob: Optional[bool] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_full_spot_market(
            market_id=market_id,
            with_mid_price_and_tob=with_mid_price_and_tob,
        )

    async def fetch_spot_orderbook(
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

    async def fetch_trader_spot_orders(
        self,
        market_id: str,
        subaccount_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_trader_spot_orders(
            market_id=market_id,
            subaccount_id=subaccount_id,
        )

    async def fetch_account_address_spot_orders(
        self,
        market_id: str,
        account_address: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_account_address_spot_orders(
            market_id=market_id,
            account_address=account_address,
        )

    async def fetch_spot_orders_by_hashes(
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

    async def fetch_subaccount_orders(
        self,
        subaccount_id: str,
        market_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_subaccount_orders(
            subaccount_id=subaccount_id,
            market_id=market_id,
        )

    async def fetch_trader_spot_transient_orders(
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

    async def fetch_derivative_orderbook(
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

    async def fetch_trader_derivative_orders(
        self,
        market_id: str,
        subaccount_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_trader_derivative_orders(
            market_id=market_id,
            subaccount_id=subaccount_id,
        )

    async def fetch_account_address_derivative_orders(
        self,
        market_id: str,
        account_address: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_account_address_derivative_orders(
            market_id=market_id,
            account_address=account_address,
        )

    async def fetch_derivative_orders_by_hashes(
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

    async def fetch_trader_derivative_transient_orders(
        self,
        market_id: str,
        subaccount_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_trader_derivative_transient_orders(
            market_id=market_id,
            subaccount_id=subaccount_id,
        )

    async def fetch_derivative_markets(
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

    async def fetch_derivative_market(
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

    async def fetch_positions(self) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_positions()

    async def fetch_subaccount_positions(self, subaccount_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_subaccount_positions(subaccount_id=subaccount_id)

    async def fetch_subaccount_position_in_market(self, subaccount_id: str, market_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_subaccount_position_in_market(
            subaccount_id=subaccount_id,
            market_id=market_id,
        )

    async def fetch_subaccount_effective_position_in_market(self, subaccount_id: str, market_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_subaccount_effective_position_in_market(
            subaccount_id=subaccount_id,
            market_id=market_id,
        )

    async def fetch_perpetual_market_info(self, market_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_perpetual_market_info(market_id=market_id)

    async def fetch_expiry_futures_market_info(self, market_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_expiry_futures_market_info(market_id=market_id)

    async def fetch_perpetual_market_funding(self, market_id: str) -> Dict[str, Any]:
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

    async def fetch_binary_options_markets(self, status: Optional[str] = None) -> Dict[str, Any]:
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

    # ------------------------------
    # region Tendermint module
    async def fetch_node_info(self) -> Dict[str, Any]:
        return await self.tendermint_api.fetch_node_info()

    async def fetch_syncing(self) -> Dict[str, Any]:
        return await self.tendermint_api.fetch_syncing()

    async def get_latest_block(self) -> tendermint_query.GetLatestBlockResponse:
        """
        This method is deprecated and will be removed soon. Please use `fetch_latest_block` instead
        """
        warn("This method is deprecated. Use fetch_latest_block instead", DeprecationWarning, stacklevel=2)
        req = tendermint_query.GetLatestBlockRequest()
        return await self.stubCosmosTendermint.GetLatestBlock(req)

    async def fetch_latest_block(self) -> Dict[str, Any]:
        return await self.tendermint_api.fetch_latest_block()

    async def fetch_block_by_height(self, height: int) -> Dict[str, Any]:
        return await self.tendermint_api.fetch_block_by_height(height=height)

    async def fetch_latest_validator_set(self) -> Dict[str, Any]:
        return await self.tendermint_api.fetch_latest_validator_set()

    async def fetch_validator_set_by_height(
        self, height: int, pagination: Optional[PaginationOption] = None
    ) -> Dict[str, Any]:
        return await self.tendermint_api.fetch_validator_set_by_height(height=height, pagination=pagination)

    async def abci_query(
        self, path: str, data: Optional[bytes] = None, height: Optional[int] = None, prove: bool = False
    ) -> Dict[str, Any]:
        return await self.tendermint_api.abci_query(path=path, data=data, height=height, prove=prove)

    # endregion

    # ------------------------------
    # Explorer RPC
    # AccountsRPC
    # OracleRPC
    # InsuranceRPC
    # SpotRPC
    async def fetch_spot_market(self, market_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_market(market_id=market_id)

    async def fetch_spot_markets(
        self,
        market_statuses: Optional[List[str]] = None,
        base_denom: Optional[str] = None,
        quote_denom: Optional[str] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_markets(
            market_statuses=market_statuses, base_denom=base_denom, quote_denom=quote_denom
        )

    async def fetch_spot_orderbook(self, market_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_api.fetch_orderbook_v2(market_id=market_id)

    # DerivativeRPC
    ####MASSIVE TODO : NEED TO WRITE A LIQUIDABLE POSITIONS WATCHER#######
    # async def get_derivative_liquidable_positions(self, **kwargs):
    #    """
    #    This method is deprecated and will be removed soon. Please use `fetch_derivative_liquidable_positions` instead
    #    """
    #    warn(
    #        "This method is deprecated. Use fetch_derivative_liquidable_positions instead",
    #        DeprecationWarning,
    #        stacklevel=2,
    #    )
    #    req = derivative_exchange_rpc_pb.LiquidablePositionsRequest(
    #        market_id=kwargs.get("market_id"),
    #        skip=kwargs.get("skip"),
    #        limit=kwargs.get("limit"),
    #    )
    #    return await self.stubDerivativeExchange.LiquidablePositions(req)

    # async def fetch_derivative_liquidable_positions(
    #    self,
    #    market_id: Optional[str] = None,
    #    pagination: Optional[PaginationOption] = None,
    # ) -> Dict[str, Any]:
    #    return await self.exchange_derivative_api.fetch_liquidable_positions(
    #        market_id=market_id,
    #        pagination=pagination,
    #    )
    # PortfolioRPC
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
        metadata = self.network.chain_cookie_assistant.metadata()
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

    # region IBC Transfer module
    async def fetch_denom_trace(self, hash: str) -> Dict[str, Any]:
        return await self.ibc_transfer_api.fetch_denom_trace(hash=hash)

    async def fetch_denom_traces(self, pagination: Optional[PaginationOption] = None) -> Dict[str, Any]:
        return await self.ibc_transfer_api.fetch_denom_traces(pagination=pagination)

    async def fetch_denom_hash(self, trace: str) -> Dict[str, Any]:
        return await self.ibc_transfer_api.fetch_denom_hash(trace=trace)

    async def fetch_escrow_address(self, port_id: str, channel_id: str) -> Dict[str, Any]:
        return await self.ibc_transfer_api.fetch_escrow_address(port_id=port_id, channel_id=channel_id)

    async def fetch_total_escrow_for_denom(self, denom: str) -> Dict[str, Any]:
        return await self.ibc_transfer_api.fetch_total_escrow_for_denom(denom=denom)

    # endregion

    # region IBC Channel module
    async def fetch_ibc_channel(self, port_id: str, channel_id: str) -> Dict[str, Any]:
        return await self.ibc_channel_api.fetch_channel(port_id=port_id, channel_id=channel_id)

    async def fetch_ibc_channels(self, pagination: Optional[PaginationOption] = None) -> Dict[str, Any]:
        return await self.ibc_channel_api.fetch_channels(pagination=pagination)

    async def fetch_ibc_connection_channels(
        self, connection: str, pagination: Optional[PaginationOption] = None
    ) -> Dict[str, Any]:
        return await self.ibc_channel_api.fetch_connection_channels(connection=connection, pagination=pagination)

    async def fetch_ibc_channel_client_state(self, port_id: str, channel_id: str) -> Dict[str, Any]:
        return await self.ibc_channel_api.fetch_channel_client_state(port_id=port_id, channel_id=channel_id)

    async def fetch_ibc_channel_consensus_state(
        self,
        port_id: str,
        channel_id: str,
        revision_number: int,
        revision_height: int,
    ) -> Dict[str, Any]:
        return await self.ibc_channel_api.fetch_channel_consensus_state(
            port_id=port_id,
            channel_id=channel_id,
            revision_number=revision_number,
            revision_height=revision_height,
        )

    async def fetch_ibc_packet_commitment(self, port_id: str, channel_id: str, sequence: int) -> Dict[str, Any]:
        return await self.ibc_channel_api.fetch_packet_commitment(
            port_id=port_id, channel_id=channel_id, sequence=sequence
        )

    async def fetch_ibc_packet_commitments(
        self, port_id: str, channel_id: str, pagination: Optional[PaginationOption] = None
    ) -> Dict[str, Any]:
        return await self.ibc_channel_api.fetch_packet_commitments(
            port_id=port_id, channel_id=channel_id, pagination=pagination
        )

    async def fetch_ibc_packet_receipt(self, port_id: str, channel_id: str, sequence: int) -> Dict[str, Any]:
        return await self.ibc_channel_api.fetch_packet_receipt(
            port_id=port_id, channel_id=channel_id, sequence=sequence
        )

    async def fetch_ibc_packet_acknowledgement(self, port_id: str, channel_id: str, sequence: int) -> Dict[str, Any]:
        return await self.ibc_channel_api.fetch_packet_acknowledgement(
            port_id=port_id, channel_id=channel_id, sequence=sequence
        )

    async def fetch_ibc_packet_acknowledgements(
        self,
        port_id: str,
        channel_id: str,
        packet_commitment_sequences: Optional[List[int]] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.ibc_channel_api.fetch_packet_acknowledgements(
            port_id=port_id,
            channel_id=channel_id,
            packet_commitment_sequences=packet_commitment_sequences,
            pagination=pagination,
        )

    async def fetch_ibc_unreceived_packets(
        self, port_id: str, channel_id: str, packet_commitment_sequences: Optional[List[int]] = None
    ) -> Dict[str, Any]:
        return await self.ibc_channel_api.fetch_unreceived_packets(
            port_id=port_id, channel_id=channel_id, packet_commitment_sequences=packet_commitment_sequences
        )

    async def fetch_ibc_unreceived_acks(
        self, port_id: str, channel_id: str, packet_ack_sequences: Optional[List[int]] = None
    ) -> Dict[str, Any]:
        return await self.ibc_channel_api.fetch_unreceived_acks(
            port_id=port_id, channel_id=channel_id, packet_ack_sequences=packet_ack_sequences
        )

    async def fetch_next_sequence_receive(self, port_id: str, channel_id: str) -> Dict[str, Any]:
        return await self.ibc_channel_api.fetch_next_sequence_receive(port_id=port_id, channel_id=channel_id)

    # endregion

    # region IBC Client module
    async def fetch_ibc_client_state(self, client_id: str) -> Dict[str, Any]:
        return await self.ibc_client_api.fetch_client_state(client_id=client_id)

    async def fetch_ibc_client_states(self, pagination: Optional[PaginationOption] = None) -> Dict[str, Any]:
        return await self.ibc_client_api.fetch_client_states(pagination=pagination)

    async def fetch_ibc_consensus_state(
        self,
        client_id: str,
        revision_number: int,
        revision_height: int,
        latest_height: Optional[bool] = None,
    ) -> Dict[str, Any]:
        return await self.ibc_client_api.fetch_consensus_state(
            client_id=client_id,
            revision_number=revision_number,
            revision_height=revision_height,
            latest_height=latest_height,
        )

    async def fetch_ibc_consensus_states(
        self,
        client_id: str,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.ibc_client_api.fetch_consensus_states(client_id=client_id, pagination=pagination)

    async def fetch_ibc_consensus_state_heights(
        self,
        client_id: str,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.ibc_client_api.fetch_consensus_state_heights(client_id=client_id, pagination=pagination)

    async def fetch_ibc_client_status(self, client_id: str) -> Dict[str, Any]:
        return await self.ibc_client_api.fetch_client_status(client_id=client_id)

    async def fetch_ibc_client_params(self) -> Dict[str, Any]:
        return await self.ibc_client_api.fetch_client_params()

    async def fetch_ibc_upgraded_client_state(self) -> Dict[str, Any]:
        return await self.ibc_client_api.fetch_upgraded_client_state()

    async def fetch_ibc_upgraded_consensus_state(self) -> Dict[str, Any]:
        return await self.ibc_client_api.fetch_upgraded_consensus_state()

    # endregion

    # region IBC Connection module
    async def fetch_ibc_connection(self, connection_id: str) -> Dict[str, Any]:
        return await self.ibc_connection_api.fetch_connection(connection_id=connection_id)

    async def fetch_ibc_connections(self, pagination: Optional[PaginationOption] = None) -> Dict[str, Any]:
        return await self.ibc_connection_api.fetch_connections(pagination=pagination)

    async def fetch_ibc_client_connections(self, client_id: str) -> Dict[str, Any]:
        return await self.ibc_connection_api.fetch_client_connections(client_id=client_id)

    async def fetch_ibc_connection_client_state(self, connection_id: str) -> Dict[str, Any]:
        return await self.ibc_connection_api.fetch_connection_client_state(connection_id=connection_id)

    async def fetch_ibc_connection_consensus_state(
        self,
        connection_id: str,
        revision_number: int,
        revision_height: int,
    ) -> Dict[str, Any]:
        return await self.ibc_connection_api.fetch_connection_consensus_state(
            connection_id=connection_id, revision_number=revision_number, revision_height=revision_height
        )

    async def fetch_ibc_connection_params(self) -> Dict[str, Any]:
        return await self.ibc_connection_api.fetch_connection_params()

    # endregion

    # ------------------------------
    # region Permissions module

    async def fetch_all_permissions_namespaces(self) -> Dict[str, Any]:
        return await self.permissions_api.fetch_all_namespaces()

    async def fetch_permissions_namespace_by_denom(
        self, denom: str, include_roles: Optional[bool] = None
    ) -> Dict[str, Any]:
        return await self.permissions_api.fetch_namespace_by_denom(denom=denom, include_roles=include_roles)

    async def fetch_permissions_address_roles(self, denom: str, address: str) -> Dict[str, Any]:
        return await self.permissions_api.fetch_address_roles(denom=denom, address=address)

    async def fetch_permissions_addresses_by_role(self, denom: str, role: str) -> Dict[str, Any]:
        return await self.permissions_api.fetch_addresses_by_role(denom=denom, role=role)

    async def fetch_permissions_vouchers_for_address(self, address: str) -> Dict[str, Any]:
        return await self.permissions_api.fetch_vouchers_for_address(address=address)

    # endregion

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
            query_result = await self.fetch_denoms_metadata(pagination=PaginationOption(encoded_page_key=next_key))

            all_denoms_metadata.extend(query_result.get("metadatas", []))
            next_key = query_result.get("pagination", {}).get("nextKey", "")

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
        tokens_by_symbol, tokens_by_denom = await self._tokens_from_official_lists(network=self.network)
        self._tokens_by_denom.update(tokens_by_denom)
        self._tokens_by_symbol.update(tokens_by_symbol)

        markets_info = (await self.fetch_spot_markets(status="Active"))["markets"]
        for market_info in markets_info:
            base_token = self._tokens_by_denom.get(market_info["baseDenom"])
            quote_token = self._tokens_by_denom.get(market_info["quoteDenom"])

            market = SpotMarket(
                id=market_info["marketId"],
                status=market_info["status"],
                ticker=market_info["ticker"],
                base_token=base_token,
                quote_token=quote_token,
                maker_fee_rate=Token.convert_value_from_extended_decimal_format(Decimal(market_info["makerFeeRate"])),
                taker_fee_rate=Token.convert_value_from_extended_decimal_format(Decimal(market_info["takerFeeRate"])),
                service_provider_fee=Token.convert_value_from_extended_decimal_format(
                    Decimal(market_info["relayerFeeShareRate"])
                ),
                min_price_tick_size=Token.convert_value_from_extended_decimal_format(
                    Decimal(market_info["minPriceTickSize"])
                ),
                min_quantity_tick_size=Token.convert_value_from_extended_decimal_format(
                    Decimal(market_info["minQuantityTickSize"])
                ),
                min_notional=Token.convert_value_from_extended_decimal_format(Decimal(market_info["minNotional"])),
            )

            spot_markets[market.id] = market

        markets_info = (await self.fetch_derivative_markets(status="Active", with_mid_price_and_tob=False))["markets"]
        for market_info in markets_info:
            market = market_info["market"]
            quote_token = self._tokens_by_denom.get(market["quoteDenom"])

            derivative_market = DerivativeMarket(
                id=market["marketId"],
                status=market["status"],
                ticker=market["ticker"],
                oracle_base=market["oracleBase"],
                oracle_quote=market["oracleQuote"],
                oracle_type=market["oracleType"],
                oracle_scale_factor=market["oracleScaleFactor"],
                initial_margin_ratio=Token.convert_value_from_extended_decimal_format(
                    Decimal(market["initialMarginRatio"])
                ),
                maintenance_margin_ratio=Token.convert_value_from_extended_decimal_format(
                    Decimal(market["maintenanceMarginRatio"])
                ),
                quote_token=quote_token,
                maker_fee_rate=Token.convert_value_from_extended_decimal_format(Decimal(market["makerFeeRate"])),
                taker_fee_rate=Token.convert_value_from_extended_decimal_format(Decimal(market["takerFeeRate"])),
                service_provider_fee=Token.convert_value_from_extended_decimal_format(
                    Decimal(market["relayerFeeShareRate"])
                ),
                min_price_tick_size=Token.convert_value_from_extended_decimal_format(
                    Decimal(market["minPriceTickSize"])
                ),
                min_quantity_tick_size=Token.convert_value_from_extended_decimal_format(
                    Decimal(market["minQuantityTickSize"])
                ),
                min_notional=Token.convert_value_from_extended_decimal_format(Decimal(market["minNotional"])),
            )

            derivative_markets[derivative_market.id] = derivative_market

        markets_info = (await self.fetch_binary_options_markets(status="Active"))["markets"]
        for market_info in markets_info:
            quote_token = self._tokens_by_denom.get(market_info["quoteDenom"])

            market = BinaryOptionMarket(
                id=market_info["marketId"],
                status=market_info["status"],
                ticker=market_info["ticker"],
                oracle_symbol=market_info["oracleSymbol"],
                oracle_provider=market_info["oracleProvider"],
                oracle_type=market_info["oracleType"],
                oracle_scale_factor=market_info["oracleScaleFactor"],
                expiration_timestamp=market_info["expirationTimestamp"],
                settlement_timestamp=market_info["settlementTimestamp"],
                quote_token=quote_token,
                maker_fee_rate=Token.convert_value_from_extended_decimal_format(Decimal(market_info["makerFeeRate"])),
                taker_fee_rate=Token.convert_value_from_extended_decimal_format(Decimal(market_info["takerFeeRate"])),
                service_provider_fee=Token.convert_value_from_extended_decimal_format(
                    Decimal(market_info["relayerFeeShareRate"])
                ),
                min_price_tick_size=Token.convert_value_from_extended_decimal_format(
                    Decimal(market_info["minPriceTickSize"])
                ),
                min_quantity_tick_size=Token.convert_value_from_extended_decimal_format(
                    Decimal(market_info["minQuantityTickSize"])
                ),
                min_notional=Token.convert_value_from_extended_decimal_format(Decimal(market_info["minNotional"])),
                settlement_price=(
                    None
                    if market_info["settlementPrice"] == ""
                    else Token.convert_value_from_extended_decimal_format(Decimal(market_info["settlementPrice"]))
                ),
            )

            binary_option_markets[market.id] = market

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

    async def _tokens_from_official_lists(
        self,
        network: Network,
    ) -> Tuple[Dict[str, Token], Dict[str, Token]]:
        tokens_by_symbol = dict()
        tokens_by_denom = dict()

        loader = TokensFileLoader()
        tokens = await loader.load_tokens(network.official_tokens_list_url)

        for token in tokens:
            if token.denom is not None and token.denom != "" and token.denom not in tokens_by_denom:
                unique_symbol = token.denom
                for symbol_candidate in [token.symbol, token.name]:
                    if symbol_candidate not in tokens_by_symbol:
                        unique_symbol = symbol_candidate
                        break

                tokens_by_denom[token.denom] = token
                tokens_by_symbol[unique_symbol] = token

        return tokens_by_symbol, tokens_by_denom

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
