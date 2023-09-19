import asyncio
import time
from copy import deepcopy
from decimal import Decimal
from typing import Coroutine, Dict, List, Optional, Tuple, Union

import aiocron
import grpc

from pyinjective.composer import Composer

from . import constant
from .core.market import BinaryOptionMarket, DerivativeMarket, SpotMarket
from .core.network import Network
from .core.token import Token
from .exceptions import NotFoundError
from .proto.cosmos.auth.v1beta1 import query_pb2 as auth_query
from .proto.cosmos.auth.v1beta1 import query_pb2_grpc as auth_query_grpc
from .proto.cosmos.authz.v1beta1 import query_pb2 as authz_query
from .proto.cosmos.authz.v1beta1 import query_pb2_grpc as authz_query_grpc
from .proto.cosmos.bank.v1beta1 import query_pb2 as bank_query
from .proto.cosmos.bank.v1beta1 import query_pb2_grpc as bank_query_grpc
from .proto.cosmos.base.abci.v1beta1 import abci_pb2 as abci_type
from .proto.cosmos.base.tendermint.v1beta1 import query_pb2 as tendermint_query
from .proto.cosmos.base.tendermint.v1beta1 import query_pb2_grpc as tendermint_query_grpc
from .proto.cosmos.tx.v1beta1 import service_pb2 as tx_service
from .proto.cosmos.tx.v1beta1 import service_pb2_grpc as tx_service_grpc
from .proto.exchange import injective_accounts_rpc_pb2 as exchange_accounts_rpc_pb
from .proto.exchange import injective_accounts_rpc_pb2_grpc as exchange_accounts_rpc_grpc
from .proto.exchange import injective_auction_rpc_pb2 as auction_rpc_pb
from .proto.exchange import injective_auction_rpc_pb2_grpc as auction_rpc_grpc
from .proto.exchange import injective_derivative_exchange_rpc_pb2 as derivative_exchange_rpc_pb
from .proto.exchange import injective_derivative_exchange_rpc_pb2_grpc as derivative_exchange_rpc_grpc
from .proto.exchange import injective_explorer_rpc_pb2 as explorer_rpc_pb
from .proto.exchange import injective_explorer_rpc_pb2_grpc as explorer_rpc_grpc
from .proto.exchange import injective_insurance_rpc_pb2 as insurance_rpc_pb
from .proto.exchange import injective_insurance_rpc_pb2_grpc as insurance_rpc_grpc
from .proto.exchange import injective_meta_rpc_pb2 as exchange_meta_rpc_pb
from .proto.exchange import injective_meta_rpc_pb2_grpc as exchange_meta_rpc_grpc
from .proto.exchange import injective_oracle_rpc_pb2 as oracle_rpc_pb
from .proto.exchange import injective_oracle_rpc_pb2_grpc as oracle_rpc_grpc
from .proto.exchange import injective_portfolio_rpc_pb2 as portfolio_rpc_pb
from .proto.exchange import injective_portfolio_rpc_pb2_grpc as portfolio_rpc_grpc
from .proto.exchange import injective_spot_exchange_rpc_pb2 as spot_exchange_rpc_pb
from .proto.exchange import injective_spot_exchange_rpc_pb2_grpc as spot_exchange_rpc_grpc
from .proto.injective.types.v1beta1 import account_pb2
from .utils.logger import LoggerProvider

DEFAULT_TIMEOUTHEIGHT_SYNC_INTERVAL = 20  # seconds
DEFAULT_TIMEOUTHEIGHT = 30  # blocks
DEFAULT_SESSION_RENEWAL_OFFSET = 120  # seconds
DEFAULT_BLOCK_TIME = 2  # seconds


class AsyncClient:
    def __init__(
        self,
        network: Network,
        insecure: bool = False,
        credentials=grpc.ssl_channel_credentials(),
    ):
        # the `insecure` parameter is ignored and will be deprecated soon. The value is taken directly from `network`

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

        # timeout height update routine
        self.cron = aiocron.crontab(
            "* * * * * */{}".format(DEFAULT_TIMEOUTHEIGHT_SYNC_INTERVAL),
            func=self.sync_timeout_height,
            args=(),
            start=True,
        )

        self._tokens_and_markets_initialization_lock = asyncio.Lock()
        self._tokens: Optional[Dict[str, Token]] = None
        self._spot_markets: Optional[Dict[str, SpotMarket]] = None
        self._derivative_markets: Optional[Dict[str, DerivativeMarket]] = None
        self._binary_option_markets: Optional[Dict[str, BinaryOptionMarket]] = None

    async def all_tokens(self) -> Dict[str, Token]:
        if self._tokens is None:
            async with self._tokens_and_markets_initialization_lock:
                if self._tokens is None:
                    await self._initialize_tokens_and_markets()
        return deepcopy(self._tokens)

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
        return await self.stubTx.GetTx(tx_service.GetTxRequest(hash=tx_hash))

    async def close_exchange_channel(self):
        await self.exchange_channel.close()
        self.cron.stop()

    async def close_chain_channel(self):
        await self.chain_channel.close()
        self.cron.stop()

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

    async def get_request_id_by_tx_hash(self, tx_hash: bytes) -> List[int]:
        tx = await self.stubTx.GetTx(tx_service.GetTxRequest(hash=tx_hash))
        request_ids = []
        for tx in tx.tx_response.logs:
            request_event = [event for event in tx.events if event.type == "request" or event.type == "report"]
            if len(request_event) == 1:
                attrs = request_event[0].attributes
                attr_id = [attr for attr in attrs if attr.key == "id"]
                if len(attr_id) == 1:
                    request_id = attr_id[0].value
                    request_ids.append(int(request_id))
        if len(request_ids) == 0:
            raise NotFoundError("Request Id is not found")
        return request_ids

    async def simulate_tx(self, tx_byte: bytes) -> Tuple[Union[abci_type.SimulationResponse, grpc.RpcError], bool]:
        try:
            req = tx_service.SimulateRequest(tx_bytes=tx_byte)
            metadata = await self.network.chain_metadata(metadata_query_provider=self._chain_cookie_metadata_requestor)
            return await self.stubTx.Simulate(request=req, metadata=metadata), True
        except grpc.RpcError as err:
            return err, False

    async def send_tx_sync_mode(self, tx_byte: bytes) -> abci_type.TxResponse:
        req = tx_service.BroadcastTxRequest(tx_bytes=tx_byte, mode=tx_service.BroadcastMode.BROADCAST_MODE_SYNC)
        metadata = await self.network.chain_metadata(metadata_query_provider=self._chain_cookie_metadata_requestor)
        result = await self.stubTx.BroadcastTx(request=req, metadata=metadata)
        return result.tx_response

    async def send_tx_async_mode(self, tx_byte: bytes) -> abci_type.TxResponse:
        req = tx_service.BroadcastTxRequest(tx_bytes=tx_byte, mode=tx_service.BroadcastMode.BROADCAST_MODE_ASYNC)
        metadata = await self.network.chain_metadata(metadata_query_provider=self._chain_cookie_metadata_requestor)
        result = await self.stubTx.BroadcastTx(request=req, metadata=metadata)
        return result.tx_response

    async def send_tx_block_mode(self, tx_byte: bytes) -> abci_type.TxResponse:
        req = tx_service.BroadcastTxRequest(tx_bytes=tx_byte, mode=tx_service.BroadcastMode.BROADCAST_MODE_BLOCK)
        metadata = await self.network.chain_metadata(metadata_query_provider=self._chain_cookie_metadata_requestor)
        result = await self.stubTx.BroadcastTx(request=req, metadata=metadata)
        return result.tx_response

    async def get_chain_id(self) -> str:
        latest_block = await self.get_latest_block()
        return latest_block.block.header.chain_id

    async def get_grants(self, granter: str, grantee: str, **kwargs):
        return await self.stubAuthz.Grants(
            authz_query.QueryGrantsRequest(
                granter=granter,
                grantee=grantee,
                msg_type_url=kwargs.get("msg_type_url"),
            )
        )

    async def get_bank_balances(self, address: str):
        return await self.stubBank.AllBalances(bank_query.QueryAllBalancesRequest(address=address))

    async def get_bank_balance(self, address: str, denom: str):
        return await self.stubBank.Balance(bank_query.QueryBalanceRequest(address=address, denom=denom))

    # Injective Exchange client methods

    # Auction RPC

    async def get_auction(self, bid_round: int):
        req = auction_rpc_pb.AuctionEndpointRequest(round=bid_round)
        return await self.stubAuction.AuctionEndpoint(req)

    async def get_auctions(self):
        req = auction_rpc_pb.AuctionsRequest()
        return await self.stubAuction.Auctions(req)

    async def stream_bids(self):
        req = auction_rpc_pb.StreamBidsRequest()
        return self.stubAuction.StreamBids(req)

    # Meta RPC

    async def ping(self):
        req = exchange_meta_rpc_pb.PingRequest()
        return await self.stubMeta.Ping(req)

    async def version(self):
        req = exchange_meta_rpc_pb.VersionRequest()
        return await self.stubMeta.Version(req)

    async def info(self):
        req = exchange_meta_rpc_pb.InfoRequest(
            timestamp=int(time.time() * 1000),
        )
        return await self.stubMeta.Info(req)

    async def stream_keepalive(self):
        req = exchange_meta_rpc_pb.StreamKeepaliveRequest()
        return self.stubMeta.StreamKeepalive(req)

    # Explorer RPC

    async def get_tx_by_hash(self, tx_hash: str):
        req = explorer_rpc_pb.GetTxByTxHashRequest(hash=tx_hash)
        return await self.stubExplorer.GetTxByTxHash(req)

    async def get_account_txs(self, address: str, **kwargs):
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

    async def get_blocks(self, **kwargs):
        req = explorer_rpc_pb.GetBlocksRequest(
            before=kwargs.get("before"),
            after=kwargs.get("after"),
            limit=kwargs.get("limit"),
        )
        return await self.stubExplorer.GetBlocks(req)

    async def get_block(self, block_height: str):
        req = explorer_rpc_pb.GetBlockRequest(id=block_height)
        return await self.stubExplorer.GetBlock(req)

    async def get_txs(self, **kwargs):
        req = explorer_rpc_pb.GetTxsRequest(
            before=kwargs.get("before"),
            after=kwargs.get("after"),
            limit=kwargs.get("limit"),
            skip=kwargs.get("skip"),
            type=kwargs.get("type"),
            module=kwargs.get("module"),
        )
        return await self.stubExplorer.GetTxs(req)

    async def stream_txs(self):
        req = explorer_rpc_pb.StreamTxsRequest()
        return self.stubExplorer.StreamTxs(req)

    async def stream_blocks(self):
        req = explorer_rpc_pb.StreamBlocksRequest()
        return self.stubExplorer.StreamBlocks(req)

    async def get_peggy_deposits(self, **kwargs):
        req = explorer_rpc_pb.GetPeggyDepositTxsRequest(
            sender=kwargs.get("sender"),
            receiver=kwargs.get("receiver"),
            limit=kwargs.get("limit"),
            skip=kwargs.get("skip"),
        )
        return await self.stubExplorer.GetPeggyDepositTxs(req)

    async def get_peggy_withdrawals(self, **kwargs):
        req = explorer_rpc_pb.GetPeggyWithdrawalTxsRequest(
            sender=kwargs.get("sender"),
            receiver=kwargs.get("receiver"),
            limit=kwargs.get("limit"),
            skip=kwargs.get("skip"),
        )
        return await self.stubExplorer.GetPeggyWithdrawalTxs(req)

    async def get_ibc_transfers(self, **kwargs):
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

    # AccountsRPC

    async def stream_subaccount_balance(self, subaccount_id: str, **kwargs):
        req = exchange_accounts_rpc_pb.StreamSubaccountBalanceRequest(
            subaccount_id=subaccount_id, denoms=kwargs.get("denoms")
        )
        return self.stubExchangeAccount.StreamSubaccountBalance(req)

    async def get_subaccount_balance(self, subaccount_id: str, denom: str):
        req = exchange_accounts_rpc_pb.SubaccountBalanceEndpointRequest(subaccount_id=subaccount_id, denom=denom)
        return await self.stubExchangeAccount.SubaccountBalanceEndpoint(req)

    async def get_subaccount_list(self, account_address: str):
        req = exchange_accounts_rpc_pb.SubaccountsListRequest(account_address=account_address)
        return await self.stubExchangeAccount.SubaccountsList(req)

    async def get_subaccount_balances_list(self, subaccount_id: str, **kwargs):
        req = exchange_accounts_rpc_pb.SubaccountBalancesListRequest(
            subaccount_id=subaccount_id, denoms=kwargs.get("denoms")
        )
        return await self.stubExchangeAccount.SubaccountBalancesList(req)

    async def get_subaccount_history(self, subaccount_id: str, **kwargs):
        req = exchange_accounts_rpc_pb.SubaccountHistoryRequest(
            subaccount_id=subaccount_id,
            denom=kwargs.get("denom"),
            transfer_types=kwargs.get("transfer_types"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
            end_time=kwargs.get("end_time"),
        )
        return await self.stubExchangeAccount.SubaccountHistory(req)

    async def get_subaccount_order_summary(self, subaccount_id: str, **kwargs):
        req = exchange_accounts_rpc_pb.SubaccountOrderSummaryRequest(
            subaccount_id=subaccount_id,
            order_direction=kwargs.get("order_direction"),
            market_id=kwargs.get("market_id"),
        )
        return await self.stubExchangeAccount.SubaccountOrderSummary(req)

    async def get_order_states(self, **kwargs):
        req = exchange_accounts_rpc_pb.OrderStatesRequest(
            spot_order_hashes=kwargs.get("spot_order_hashes"),
            derivative_order_hashes=kwargs.get("derivative_order_hashes"),
        )
        return await self.stubExchangeAccount.OrderStates(req)

    async def get_portfolio(self, account_address: str):
        req = exchange_accounts_rpc_pb.PortfolioRequest(account_address=account_address)
        return await self.stubExchangeAccount.Portfolio(req)

    async def get_rewards(self, **kwargs):
        req = exchange_accounts_rpc_pb.RewardsRequest(
            account_address=kwargs.get("account_address"), epoch=kwargs.get("epoch")
        )
        return await self.stubExchangeAccount.Rewards(req)

    # OracleRPC

    async def stream_oracle_prices(self, base_symbol: str, quote_symbol: str, oracle_type: str):
        req = oracle_rpc_pb.StreamPricesRequest(
            base_symbol=base_symbol, quote_symbol=quote_symbol, oracle_type=oracle_type
        )
        return self.stubOracle.StreamPrices(req)

    async def get_oracle_prices(
        self,
        base_symbol: str,
        quote_symbol: str,
        oracle_type: str,
        oracle_scale_factor: int,
    ):
        req = oracle_rpc_pb.PriceRequest(
            base_symbol=base_symbol,
            quote_symbol=quote_symbol,
            oracle_type=oracle_type,
            oracle_scale_factor=oracle_scale_factor,
        )
        return await self.stubOracle.Price(req)

    async def get_oracle_list(self):
        req = oracle_rpc_pb.OracleListRequest()
        return await self.stubOracle.OracleList(req)

    # InsuranceRPC

    async def get_insurance_funds(self):
        req = insurance_rpc_pb.FundsRequest()
        return await self.stubInsurance.Funds(req)

    async def get_redemptions(self, **kwargs):
        req = insurance_rpc_pb.RedemptionsRequest(
            redeemer=kwargs.get("redeemer"),
            redemption_denom=kwargs.get("redemption_denom"),
            status=kwargs.get("status"),
        )
        return await self.stubInsurance.Redemptions(req)

    # SpotRPC

    async def get_spot_market(self, market_id: str):
        req = spot_exchange_rpc_pb.MarketRequest(market_id=market_id)
        return await self.stubSpotExchange.Market(req)

    async def get_spot_markets(self, **kwargs):
        req = spot_exchange_rpc_pb.MarketsRequest(
            market_status=kwargs.get("market_status"),
            base_denom=kwargs.get("base_denom"),
            quote_denom=kwargs.get("quote_denom"),
        )
        return await self.stubSpotExchange.Markets(req)

    async def stream_spot_markets(self, **kwargs):
        req = spot_exchange_rpc_pb.StreamMarketsRequest(market_ids=kwargs.get("market_ids"))
        metadata = await self.network.exchange_metadata(
            metadata_query_provider=self._exchange_cookie_metadata_requestor
        )
        return self.stubSpotExchange.StreamMarkets(request=req, metadata=metadata)

    async def get_spot_orderbookV2(self, market_id: str):
        req = spot_exchange_rpc_pb.OrderbookV2Request(market_id=market_id)
        return await self.stubSpotExchange.OrderbookV2(req)

    async def get_spot_orderbooksV2(self, market_ids: List):
        req = spot_exchange_rpc_pb.OrderbooksV2Request(market_ids=market_ids)
        return await self.stubSpotExchange.OrderbooksV2(req)

    async def get_spot_orders(self, market_id: str, **kwargs):
        req = spot_exchange_rpc_pb.OrdersRequest(
            market_id=market_id,
            order_side=kwargs.get("order_side"),
            subaccount_id=kwargs.get("subaccount_id"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
        )
        return await self.stubSpotExchange.Orders(req)

    async def get_historical_spot_orders(self, market_id: Optional[str] = None, **kwargs):
        market_ids = kwargs.get("market_ids", [])
        if market_id is not None:
            market_ids.append(market_id)
        req = spot_exchange_rpc_pb.OrdersHistoryRequest(
            market_ids=kwargs.get("market_ids", []),
            direction=kwargs.get("direction"),
            order_types=kwargs.get("order_types", []),
            execution_types=kwargs.get("execution_types", []),
            subaccount_id=kwargs.get("subaccount_id"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
            start_time=kwargs.get("start_time"),
            end_time=kwargs.get("end_time"),
            state=kwargs.get("state"),
        )
        return await self.stubSpotExchange.OrdersHistory(req)

    async def get_spot_trades(self, **kwargs):
        req = spot_exchange_rpc_pb.TradesRequest(
            market_id=kwargs.get("market_id"),
            market_ids=kwargs.get("market_ids"),
            execution_side=kwargs.get("execution_side"),
            direction=kwargs.get("direction"),
            subaccount_id=kwargs.get("subaccount_id"),
            subaccount_ids=kwargs.get("subaccount_ids"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
            start_time=kwargs.get("start_time"),
            end_time=kwargs.get("end_time"),
            execution_types=kwargs.get("execution_types"),
        )
        return await self.stubSpotExchange.Trades(req)

    async def stream_spot_orderbook_snapshot(self, market_ids: List[str]):
        req = spot_exchange_rpc_pb.StreamOrderbookV2Request(market_ids=market_ids)
        metadata = await self.network.exchange_metadata(
            metadata_query_provider=self._exchange_cookie_metadata_requestor
        )
        return self.stubSpotExchange.StreamOrderbookV2(request=req, metadata=metadata)

    async def stream_spot_orderbook_update(self, market_ids: List[str]):
        req = spot_exchange_rpc_pb.StreamOrderbookUpdateRequest(market_ids=market_ids)
        metadata = await self.network.exchange_metadata(
            metadata_query_provider=self._exchange_cookie_metadata_requestor
        )
        return self.stubSpotExchange.StreamOrderbookUpdate(request=req, metadata=metadata)

    async def stream_spot_orders(self, market_id: str, **kwargs):
        req = spot_exchange_rpc_pb.StreamOrdersRequest(
            market_id=market_id,
            order_side=kwargs.get("order_side"),
            subaccount_id=kwargs.get("subaccount_id"),
        )
        metadata = await self.network.exchange_metadata(
            metadata_query_provider=self._exchange_cookie_metadata_requestor
        )
        return self.stubSpotExchange.StreamOrders(request=req, metadata=metadata)

    async def stream_historical_spot_orders(self, market_id: str, **kwargs):
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

    async def stream_historical_derivative_orders(self, market_id: str, **kwargs):
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

    async def stream_spot_trades(self, **kwargs):
        req = spot_exchange_rpc_pb.StreamTradesRequest(
            market_id=kwargs.get("market_id"),
            market_ids=kwargs.get("market_ids"),
            execution_side=kwargs.get("execution_side"),
            direction=kwargs.get("direction"),
            subaccount_id=kwargs.get("subaccount_id"),
            subaccount_ids=kwargs.get("subaccount_ids"),
            execution_types=kwargs.get("execution_types"),
        )
        metadata = await self.network.exchange_metadata(
            metadata_query_provider=self._exchange_cookie_metadata_requestor
        )
        return self.stubSpotExchange.StreamTrades(request=req, metadata=metadata)

    async def get_spot_subaccount_orders(self, subaccount_id: str, **kwargs):
        req = spot_exchange_rpc_pb.SubaccountOrdersListRequest(
            subaccount_id=subaccount_id,
            market_id=kwargs.get("market_id"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
        )
        return await self.stubSpotExchange.SubaccountOrdersList(req)

    async def get_spot_subaccount_trades(self, subaccount_id: str, **kwargs):
        req = spot_exchange_rpc_pb.SubaccountTradesListRequest(
            subaccount_id=subaccount_id,
            market_id=kwargs.get("market_id"),
            execution_type=kwargs.get("execution_type"),
            direction=kwargs.get("direction"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
        )
        return await self.stubSpotExchange.SubaccountTradesList(req)

    # DerivativeRPC

    async def get_derivative_market(self, market_id: str):
        req = derivative_exchange_rpc_pb.MarketRequest(market_id=market_id)
        return await self.stubDerivativeExchange.Market(req)

    async def get_derivative_markets(self, **kwargs):
        req = derivative_exchange_rpc_pb.MarketsRequest(
            market_status=kwargs.get("market_status"),
            quote_denom=kwargs.get("quote_denom"),
        )
        return await self.stubDerivativeExchange.Markets(req)

    async def stream_derivative_markets(self, **kwargs):
        req = derivative_exchange_rpc_pb.StreamMarketRequest(market_ids=kwargs.get("market_ids"))
        metadata = await self.network.exchange_metadata(
            metadata_query_provider=self._exchange_cookie_metadata_requestor
        )
        return self.stubDerivativeExchange.StreamMarket(request=req, metadata=metadata)

    async def get_derivative_orderbook(self, market_id: str):
        req = derivative_exchange_rpc_pb.OrderbookV2Request(market_id=market_id)
        return await self.stubDerivativeExchange.OrderbookV2(req)

    async def get_derivative_orderbooks(self, market_ids: List):
        req = derivative_exchange_rpc_pb.OrderbooksV2Request(market_ids=market_ids)
        return await self.stubDerivativeExchange.OrderbooksV2(req)

    async def get_derivative_orderbooksV2(self, market_ids: List):
        req = derivative_exchange_rpc_pb.OrderbooksV2Request(market_ids=market_ids)
        return await self.stubDerivativeExchange.OrderbooksV2(req)

    async def get_derivative_orders(self, market_id: str, **kwargs):
        req = derivative_exchange_rpc_pb.OrdersRequest(
            market_id=market_id,
            order_side=kwargs.get("order_side"),
            subaccount_id=kwargs.get("subaccount_id"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
        )
        return await self.stubDerivativeExchange.Orders(req)

    async def get_historical_derivative_orders(self, market_id: Optional[str] = None, **kwargs):
        market_ids = kwargs.get("market_ids", [])
        if market_id is not None:
            market_ids.append(market_id)
        order_types = kwargs.get("order_types", [])
        order_type = kwargs.get("order_type")
        if order_type is not None:
            order_types.append(market_id)
        req = derivative_exchange_rpc_pb.OrdersHistoryRequest(
            market_ids=market_ids,
            direction=kwargs.get("direction"),
            order_types=order_types,
            execution_types=kwargs.get("execution_types", []),
            subaccount_id=kwargs.get("subaccount_id"),
            is_conditional=kwargs.get("is_conditional"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
            start_time=kwargs.get("start_time"),
            end_time=kwargs.get("end_time"),
            state=kwargs.get("state"),
        )
        return await self.stubDerivativeExchange.OrdersHistory(req)

    async def get_derivative_trades(self, **kwargs):
        req = derivative_exchange_rpc_pb.TradesRequest(
            market_id=kwargs.get("market_id"),
            market_ids=kwargs.get("market_ids"),
            subaccount_id=kwargs.get("subaccount_id"),
            subaccount_ids=kwargs.get("subaccount_ids"),
            execution_side=kwargs.get("execution_side"),
            direction=kwargs.get("direction"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
            start_time=kwargs.get("start_time"),
            end_time=kwargs.get("end_time"),
            execution_types=kwargs.get("execution_types"),
        )
        return await self.stubDerivativeExchange.Trades(req)

    async def stream_derivative_orderbook_snapshot(self, market_ids: List[str]):
        req = derivative_exchange_rpc_pb.StreamOrderbookV2Request(market_ids=market_ids)
        metadata = await self.network.exchange_metadata(
            metadata_query_provider=self._exchange_cookie_metadata_requestor
        )
        return self.stubDerivativeExchange.StreamOrderbookV2(request=req, metadata=metadata)

    async def stream_derivative_orderbook_update(self, market_ids: List[str]):
        req = derivative_exchange_rpc_pb.StreamOrderbookUpdateRequest(market_ids=market_ids)
        metadata = await self.network.exchange_metadata(
            metadata_query_provider=self._exchange_cookie_metadata_requestor
        )
        return self.stubDerivativeExchange.StreamOrderbookUpdate(request=req, metadata=metadata)

    async def stream_derivative_orders(self, market_id: str, **kwargs):
        req = derivative_exchange_rpc_pb.StreamOrdersRequest(
            market_id=market_id,
            order_side=kwargs.get("order_side"),
            subaccount_id=kwargs.get("subaccount_id"),
        )
        metadata = await self.network.exchange_metadata(
            metadata_query_provider=self._exchange_cookie_metadata_requestor
        )
        return self.stubDerivativeExchange.StreamOrders(request=req, metadata=metadata)

    async def stream_derivative_trades(self, **kwargs):
        req = derivative_exchange_rpc_pb.StreamTradesRequest(
            market_id=kwargs.get("market_id"),
            market_ids=kwargs.get("market_ids"),
            subaccount_id=kwargs.get("subaccount_id"),
            subaccount_ids=kwargs.get("subaccount_ids"),
            execution_side=kwargs.get("execution_side"),
            direction=kwargs.get("direction"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
            execution_types=kwargs.get("execution_types"),
        )
        metadata = await self.network.exchange_metadata(
            metadata_query_provider=self._exchange_cookie_metadata_requestor
        )
        return self.stubDerivativeExchange.StreamTrades(request=req, metadata=metadata)

    async def get_derivative_positions(self, **kwargs):
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

    async def stream_derivative_positions(self, **kwargs):
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

    async def get_derivative_liquidable_positions(self, **kwargs):
        req = derivative_exchange_rpc_pb.LiquidablePositionsRequest(
            market_id=kwargs.get("market_id"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
        )
        return await self.stubDerivativeExchange.LiquidablePositions(req)

    async def get_derivative_subaccount_orders(self, subaccount_id: str, **kwargs):
        req = derivative_exchange_rpc_pb.SubaccountOrdersListRequest(
            subaccount_id=subaccount_id,
            market_id=kwargs.get("market_id"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
        )
        return await self.stubDerivativeExchange.SubaccountOrdersList(req)

    async def get_derivative_subaccount_trades(self, subaccount_id: str, **kwargs):
        req = derivative_exchange_rpc_pb.SubaccountTradesListRequest(
            subaccount_id=subaccount_id,
            market_id=kwargs.get("market_id"),
            execution_type=kwargs.get("execution_type"),
            direction=kwargs.get("direction"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
        )
        return await self.stubDerivativeExchange.SubaccountTradesList(req)

    async def get_funding_payments(self, subaccount_id: str, **kwargs):
        req = derivative_exchange_rpc_pb.FundingPaymentsRequest(
            subaccount_id=subaccount_id,
            market_id=kwargs.get("market_id"),
            market_ids=kwargs.get("market_ids"),
            skip=kwargs.get("skip"),
            end_time=kwargs.get("end_time"),
            limit=kwargs.get("limit"),
        )
        return await self.stubDerivativeExchange.FundingPayments(req)

    async def get_funding_rates(self, market_id: str, **kwargs):
        req = derivative_exchange_rpc_pb.FundingRatesRequest(
            market_id=market_id,
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
            end_time=kwargs.get("end_time"),
        )
        return await self.stubDerivativeExchange.FundingRates(req)

    async def get_binary_options_markets(self, **kwargs):
        req = derivative_exchange_rpc_pb.BinaryOptionsMarketsRequest(
            market_status=kwargs.get("market_status"),
            quote_denom=kwargs.get("quote_denom"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
        )
        return await self.stubDerivativeExchange.BinaryOptionsMarkets(req)

    async def get_binary_options_market(self, market_id: str):
        req = derivative_exchange_rpc_pb.BinaryOptionsMarketRequest(market_id=market_id)
        return await self.stubDerivativeExchange.BinaryOptionsMarket(req)

    # PortfolioRPC

    async def get_account_portfolio(self, account_address: str):
        req = portfolio_rpc_pb.AccountPortfolioRequest(account_address=account_address)
        return await self.stubPortfolio.AccountPortfolio(req)

    async def stream_account_portfolio(self, account_address: str, **kwargs):
        req = portfolio_rpc_pb.StreamAccountPortfolioRequest(
            account_address=account_address, subaccount_id=kwargs.get("subaccount_id"), type=kwargs.get("type")
        )
        metadata = await self.network.exchange_metadata(
            metadata_query_provider=self._exchange_cookie_metadata_requestor
        )
        return self.stubPortfolio.StreamAccountPortfolio(request=req, metadata=metadata)

    async def composer(self):
        return Composer(
            network=self.network.string(),
            spot_markets=await self.all_spot_markets(),
            derivative_markets=await self.all_derivative_markets(),
            binary_option_markets=await self.all_binary_option_markets(),
            tokens=await self.all_tokens(),
        )

    async def _initialize_tokens_and_markets(self):
        spot_markets = dict()
        derivative_markets = dict()
        binary_option_markets = dict()
        tokens = dict()
        tokens_by_denom = dict()
        markets_info = (await self.get_spot_markets()).markets

        for market_info in markets_info:
            if "/" in market_info.ticker:
                base_token_symbol, quote_token_symbol = market_info.ticker.split(constant.TICKER_TOKENS_SEPARATOR)
            else:
                base_token_symbol = market_info.base_token_meta.symbol
                quote_token_symbol = market_info.quote_token_meta.symbol

            base_token = self._token_representation(
                symbol=base_token_symbol,
                token_meta=market_info.base_token_meta,
                denom=market_info.base_denom,
                all_tokens=tokens,
            )
            if base_token.denom not in tokens_by_denom:
                tokens_by_denom[base_token.denom] = base_token

            quote_token = self._token_representation(
                symbol=quote_token_symbol,
                token_meta=market_info.quote_token_meta,
                denom=market_info.quote_denom,
                all_tokens=tokens,
            )
            if quote_token.denom not in tokens_by_denom:
                tokens_by_denom[quote_token.denom] = quote_token

            market = SpotMarket(
                id=market_info.market_id,
                status=market_info.market_status,
                ticker=market_info.ticker,
                base_token=base_token,
                quote_token=quote_token,
                maker_fee_rate=Decimal(market_info.maker_fee_rate),
                taker_fee_rate=Decimal(market_info.taker_fee_rate),
                service_provider_fee=Decimal(market_info.service_provider_fee),
                min_price_tick_size=Decimal(market_info.min_price_tick_size),
                min_quantity_tick_size=Decimal(market_info.min_quantity_tick_size),
            )

            spot_markets[market.id] = market

        markets_info = (await self.get_derivative_markets()).markets
        for market_info in markets_info:
            quote_token_symbol = market_info.quote_token_meta.symbol

            quote_token = self._token_representation(
                symbol=quote_token_symbol,
                token_meta=market_info.quote_token_meta,
                denom=market_info.quote_denom,
                all_tokens=tokens,
            )
            if quote_token.denom not in tokens_by_denom:
                tokens_by_denom[quote_token.denom] = quote_token

            market = DerivativeMarket(
                id=market_info.market_id,
                status=market_info.market_status,
                ticker=market_info.ticker,
                oracle_base=market_info.oracle_base,
                oracle_quote=market_info.oracle_quote,
                oracle_type=market_info.oracle_type,
                oracle_scale_factor=market_info.oracle_scale_factor,
                initial_margin_ratio=Decimal(market_info.initial_margin_ratio),
                maintenance_margin_ratio=Decimal(market_info.maintenance_margin_ratio),
                quote_token=quote_token,
                maker_fee_rate=Decimal(market_info.maker_fee_rate),
                taker_fee_rate=Decimal(market_info.taker_fee_rate),
                service_provider_fee=Decimal(market_info.service_provider_fee),
                min_price_tick_size=Decimal(market_info.min_price_tick_size),
                min_quantity_tick_size=Decimal(market_info.min_quantity_tick_size),
            )

            derivative_markets[market.id] = market

        markets_info = (await self.get_binary_options_markets()).markets
        for market_info in markets_info:
            quote_token = tokens_by_denom.get(market_info.quote_denom, None)

            market = BinaryOptionMarket(
                id=market_info.market_id,
                status=market_info.market_status,
                ticker=market_info.ticker,
                oracle_symbol=market_info.oracle_symbol,
                oracle_provider=market_info.oracle_provider,
                oracle_type=market_info.oracle_type,
                oracle_scale_factor=market_info.oracle_scale_factor,
                expiration_timestamp=market_info.expiration_timestamp,
                settlement_timestamp=market_info.settlement_timestamp,
                quote_token=quote_token,
                maker_fee_rate=Decimal(market_info.maker_fee_rate),
                taker_fee_rate=Decimal(market_info.taker_fee_rate),
                service_provider_fee=Decimal(market_info.service_provider_fee),
                min_price_tick_size=Decimal(market_info.min_price_tick_size),
                min_quantity_tick_size=Decimal(market_info.min_quantity_tick_size),
            )

            binary_option_markets[market.id] = market

        self._tokens = tokens
        self._spot_markets = spot_markets
        self._derivative_markets = derivative_markets
        self._binary_option_markets = binary_option_markets

    def _token_representation(self, symbol: str, token_meta, denom: str, all_tokens: Dict[str, Token]) -> Token:
        token = Token(
            name=token_meta.name,
            symbol=symbol,
            denom=denom,
            address=token_meta.address,
            decimals=token_meta.decimals,
            logo=token_meta.logo,
            updated=token_meta.updated_at,
        )

        existing_token = all_tokens.get(token.symbol, None)
        if existing_token is None:
            all_tokens[token.symbol] = token
            existing_token = token
        elif existing_token.denom != denom:
            existing_token = all_tokens.get(token.name, None)
            if existing_token is None:
                all_tokens[token.name] = token
                existing_token = token

        return existing_token

    def _chain_cookie_metadata_requestor(self) -> Coroutine:
        request = tendermint_query.GetLatestBlockRequest()
        return self.stubCosmosTendermint.GetLatestBlock(request).initial_metadata()

    def _exchange_cookie_metadata_requestor(self) -> Coroutine:
        request = exchange_meta_rpc_pb.VersionRequest()
        return self.stubMeta.Version(request).initial_metadata()
