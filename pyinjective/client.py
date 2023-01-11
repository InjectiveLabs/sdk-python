import os
import time
import grpc
import datetime
import threading
from http.cookies import SimpleCookie
from typing import List, Optional, Tuple, Union

from .exceptions import NotFoundError, EmptyMsgError

from .proto.cosmos.base.abci.v1beta1 import abci_pb2 as abci_type

from .proto.cosmos.base.tendermint.v1beta1 import (
    query_pb2_grpc as tendermint_query_grpc,
    query_pb2 as tendermint_query,
)
from .proto.cosmos.auth.v1beta1 import (
    query_pb2_grpc as auth_query_grpc,
    query_pb2 as auth_query,
    auth_pb2 as auth_type,
)
from .proto.cosmos.authz.v1beta1 import (
    query_pb2_grpc as authz_query_grpc,
    query_pb2 as authz_query,
    authz_pb2 as authz_type,
)
from .proto.cosmos.tx.v1beta1 import (
    service_pb2_grpc as tx_service_grpc,
    service_pb2 as tx_service,
)
from .proto.exchange import (
    injective_accounts_rpc_pb2 as exchange_accounts_rpc_pb,
    injective_accounts_rpc_pb2_grpc as exchange_accounts_rpc_grpc,
    injective_oracle_rpc_pb2 as oracle_rpc_pb,
    injective_oracle_rpc_pb2_grpc as oracle_rpc_grpc,
    injective_insurance_rpc_pb2 as insurance_rpc_pb,
    injective_insurance_rpc_pb2_grpc as insurance_rpc_grpc,
    injective_spot_exchange_rpc_pb2 as spot_exchange_rpc_pb,
    injective_spot_exchange_rpc_pb2_grpc as spot_exchange_rpc_grpc,
    injective_derivative_exchange_rpc_pb2 as derivative_exchange_rpc_pb,
    injective_derivative_exchange_rpc_pb2_grpc as derivative_exchange_rpc_grpc,
    injective_meta_rpc_pb2 as exchange_meta_rpc_pb,
    injective_meta_rpc_pb2_grpc as exchange_meta_rpc_grpc,
    injective_explorer_rpc_pb2 as explorer_rpc_pb,
    injective_explorer_rpc_pb2_grpc as explorer_rpc_grpc,
    injective_auction_rpc_pb2 as auction_rpc_pb,
    injective_auction_rpc_pb2_grpc as auction_rpc_grpc,
)

from .constant import Network

DEFAULT_TIMEOUTHEIGHT_SYNC_INTERVAL = 10 # seconds
DEFAULT_TIMEOUTHEIGHT = 20 # blocks
DEFAULT_SESSION_RENEWAL_OFFSET = 120 # seconds
DEFAULT_BLOCK_TIME = 3 # seconds

class Client:
    def __init__(
        self,
        network: Network,
        insecure: bool = False,
        credentials = grpc.ssl_channel_credentials()
    ):

        # chain stubs
        self.chain_channel = (
            grpc.insecure_channel(network.grpc_endpoint)
            if insecure else grpc.secure_channel(network.grpc_endpoint, credentials)
        )
        self.stubCosmosTendermint = tendermint_query_grpc.ServiceStub(self.chain_channel)
        self.stubAuth = auth_query_grpc.QueryStub(self.chain_channel)
        self.stubAuthz = authz_query_grpc.QueryStub(self.chain_channel)
        self.stubTx = tx_service_grpc.ServiceStub(self.chain_channel)
        self.chain_cookie = ""
        self.exchange_cookie = ""
        self.timeout_height = 1

        # exchange stubs
        self.exchange_channel = (
            grpc.insecure_channel(network.grpc_exchange_endpoint)
            if insecure else grpc.secure_channel(network.grpc_exchange_endpoint, credentials)
        )

        self.stubMeta = exchange_meta_rpc_grpc.InjectiveMetaRPCStub(self.exchange_channel)
        self.stubExchangeAccount = exchange_accounts_rpc_grpc.InjectiveAccountsRPCStub(
            self.exchange_channel
        )
        self.stubOracle = oracle_rpc_grpc.InjectiveOracleRPCStub(self.exchange_channel)
        self.stubInsurance = insurance_rpc_grpc.InjectiveInsuranceRPCStub(
            self.exchange_channel
        )
        self.stubSpotExchange = spot_exchange_rpc_grpc.InjectiveSpotExchangeRPCStub(
            self.exchange_channel
        )
        self.stubDerivativeExchange = (
            derivative_exchange_rpc_grpc.InjectiveDerivativeExchangeRPCStub(
                self.exchange_channel
            )
        )
        self.stubExplorer = explorer_rpc_grpc.InjectiveExplorerRPCStub(self.exchange_channel)
        self.stubAuction = auction_rpc_grpc.InjectiveAuctionRPCStub(self.exchange_channel)

    def close_exchange_channel(self):
        self.exchange_channel.close()

    def close_chain_channel(self):
        self.chain_channel.close()

        # timeout height update routine
        self.sync_timeout_height()

    def sync_timeout_height(self):
        threading.Timer(DEFAULT_TIMEOUTHEIGHT_SYNC_INTERVAL, self.sync_timeout_height).start()
        block = self.get_latest_block()
        self.timeout_height = block.block.header.height + DEFAULT_TIMEOUTHEIGHT

    # cookie helper methods
    def get_cookie(self, type):
        metadata = None
        if type == "chain":
            if self.chain_cookie != "":
                metadata = (("cookie", self.chain_cookie),)

		        # format cookie date into RFC1123 standard
                cookie = SimpleCookie()
                cookie.load(self.chain_cookie)
                expires_at = cookie.get("grpc-cookie").get("expires")
                expires_at = expires_at.replace("-"," ")
                yyyy = "20{}".format(expires_at[12:14])
                expires_at = expires_at[:12] + yyyy + expires_at[14:]

                # parse expire field to unix timestamp
                expire_timestamp = datetime.datetime.strptime(expires_at, "%a, %d %b %Y %H:%M:%S GMT").timestamp()

                # renew session if timestamp diff < offset
                timestamp_diff = expire_timestamp - int(time.time())
                if timestamp_diff < DEFAULT_SESSION_RENEWAL_OFFSET:
                    # request and set new cookie
                    req = tendermint_query.GetLatestBlockRequest()
                    res, call = self.stubCosmosTendermint.GetLatestBlock.with_call(req)
                    self.set_cookie(call,type="chain")
                    time.sleep(DEFAULT_BLOCK_TIME)
                    metadata = (("cookie", self.chain_cookie),)
                    return metadata
            return metadata

        if type == "exchange":
            if self.exchange_cookie != "":
                metadata = (("cookie", self.exchange_cookie),)
        return metadata

    def set_cookie(self, call, type):
        new_cookie = None
        for k, v in call.initial_metadata():
            if k == "set-cookie":
                new_cookie = v

        if new_cookie == None:
            return

        if type == "chain":
            self.chain_cookie = new_cookie
        if type == "exchange":
            self.exchange_cookie = new_cookie

    # default client methods
    def get_latest_block(self) -> tendermint_query.GetLatestBlockResponse:
        return self.stubCosmosTendermint.GetLatestBlock(
            tendermint_query.GetLatestBlockRequest()
        )

    def get_account(self, address: str) -> Optional[auth_type.BaseAccount]:
        try:
            account_any = self.stubAuth.Account(
                auth_query.QueryAccountRequest(address=address)
            ).account
            account = auth_type.BaseAccount()
            if account_any.Is(account.DESCRIPTOR):
                account_any.Unpack(account)
                return account
        except:
            return None

    def get_request_id_by_tx_hash(self, tx_hash: bytes) -> List[int]:
        tx = self.stubTx.GetTx(tx_service.GetTxRequest(hash=tx_hash))
        request_ids = []
        for tx in tx.tx_response.logs:
            request_event = [
                event
                for event in tx.events
                if event.type == "request" or event.type == "report"
            ]
            if len(request_event) == 1:
                attrs = request_event[0].attributes
                attr_id = [attr for attr in attrs if attr.key == "id"]
                if len(attr_id) == 1:
                    request_id = attr_id[0].value
                    request_ids.append(int(request_id))
        if len(request_ids) == 0:
            raise NotFoundError("Request Id is not found")
        return request_ids

    def simulate_tx(
        self, tx_byte: bytes
    ) -> Tuple[Union[abci_type.SimulationResponse, grpc.RpcError], bool]:
        try:
            req = tx_service.SimulateRequest(tx_bytes=tx_byte)

            metadata = self.get_cookie(type="chain")
            res, call = self.stubTx.Simulate.with_call(req, metadata=metadata)
            self.set_cookie(call,type="chain")

            return res, True

        except grpc.RpcError as err:
            return err, False

    def send_tx_sync_mode(self, tx_byte: bytes) -> abci_type.TxResponse:
        req = tx_service.BroadcastTxRequest(
            tx_bytes=tx_byte, mode=tx_service.BroadcastMode.BROADCAST_MODE_SYNC
        )
        metadata = self.get_cookie(type="chain")
        res, call = self.stubTx.BroadcastTx.with_call(req, metadata=metadata)
        self.set_cookie(call,type="chain")

        return res.tx_response

    def send_tx_async_mode(self, tx_byte: bytes) -> abci_type.TxResponse:
        req = tx_service.BroadcastTxRequest(
            tx_bytes=tx_byte,
            mode=tx_service.BroadcastMode.BROADCAST_MODE_ASYNC
        )
        metadata = self.get_cookie(type="chain")
        res, call = self.stubTx.BroadcastTx.with_call(req, metadata=metadata)
        self.set_cookie(call,type="chain")

        return res.tx_response

    def send_tx_block_mode(self, tx_byte: bytes) -> abci_type.TxResponse:
        req = tx_service.BroadcastTxRequest(
            tx_bytes=tx_byte,
            mode=tx_service.BroadcastMode.BROADCAST_MODE_BLOCK
        )
        metadata = self.get_cookie(type="chain")
        res, call = self.stubTx.BroadcastTx.with_call(req, metadata=metadata)
        self.set_cookie(call,type="chain")

        return res.tx_response

    def get_chain_id(self) -> str:
        latest_block = self.get_latest_block()
        return latest_block.block.header.chain_id

    def get_grants(self, granter: str, grantee: str, **kwargs):
        return self.stubAuthz.Grants(
            authz_query.QueryGrantsRequest(
                granter=granter,
                grantee=grantee,
                msg_type_url=kwargs.get("msg_type_url"),
            )
        )

    # Injective Exchange client methods

    # Auction RPC

    def get_auction(self, bid_round: int):
        req = auction_rpc_pb.AuctionRequest(round=bid_round)
        return self.stubAuction.AuctionEndpoint(req)

    def get_auctions(self):
        req = auction_rpc_pb.AuctionsRequest()
        return self.stubAuction.Auctions(req)

    def stream_bids(self):
        req = auction_rpc_pb.StreamBidsRequest()
        return self.stubAuction.StreamBids(req)

    # Meta RPC

    def ping(self):
        req = exchange_meta_rpc_pb.PingRequest()
        return self.stubMeta.Ping(req)

    def version(self):
        req = exchange_meta_rpc_pb.VersionRequest()
        return self.stubMeta.Version(req)

    def info(self):
        req = exchange_meta_rpc_pb.InfoRequest(
            timestamp=int(time.time() * 1000),
        )
        return self.stubMeta.Info(req)

    def stream_keepalive(self):
        req = exchange_meta_rpc_pb.StreamKeepaliveRequest()
        return self.stubMeta.StreamKeepalive(req)

    # Explorer RPC

    def get_tx_by_hash(self, tx_hash: str):
        req = explorer_rpc_pb.GetTxByTxHashRequest(hash=tx_hash)
        return self.stubExplorer.GetTxByTxHash(req)

    # AccountsRPC

    def stream_subaccount_balance(self, subaccount_id: str):
        req = exchange_accounts_rpc_pb.StreamSubaccountBalanceRequest(
            subaccount_id=subaccount_id
        )
        return self.stubExchangeAccount.StreamSubaccountBalance(req)

    def get_subaccount_balance(self, subaccount_id: str, denom: str):
        req = exchange_accounts_rpc_pb.SubaccountBalanceRequest(
            subaccount_id=subaccount_id, denom=denom
        )
        return self.stubExchangeAccount.SubaccountBalanceEndpoint(req)

    def get_subaccount_list(self, account_address: str):
        req = exchange_accounts_rpc_pb.SubaccountsListRequest(
            account_address=account_address
        )
        return self.stubExchangeAccount.SubaccountsList(req)

    def get_subaccount_balances_list(self, subaccount_id: str):
        req = exchange_accounts_rpc_pb.SubaccountBalancesListRequest(
            subaccount_id=subaccount_id
        )
        return self.stubExchangeAccount.SubaccountBalancesList(req)

    def get_subaccount_history(self, subaccount_id: str, **kwargs):
        req = exchange_accounts_rpc_pb.SubaccountHistoryRequest(
            subaccount_id=subaccount_id,
            denom=kwargs.get("denom"),
            transfer_types=kwargs.get("transfer_types"),
        )
        return self.stubExchangeAccount.SubaccountHistory(req)

    def get_subaccount_order_summary(self, subaccount_id: str, **kwargs):
        req = exchange_accounts_rpc_pb.SubaccountOrderSummaryRequest(
            subaccount_id=subaccount_id,
            order_direction=kwargs.get("order_direction"),
            market_id=kwargs.get("market_id"),
        )
        return self.stubExchangeAccount.SubaccountOrderSummary(req)

    def get_order_states(self, **kwargs):
        req = exchange_accounts_rpc_pb.OrderStatesRequest(
            spot_order_hashes=kwargs.get("spot_order_hashes"),
            derivative_order_hashes=kwargs.get("derivative_order_hashes"),
        )
        return self.stubExchangeAccount.OrderStates(req)

    def get_portfolio(self, account_address: str):
        req = exchange_accounts_rpc_pb.PortfolioRequest(account_address=account_address)
        return self.stubExchangeAccount.Portfolio(req)

    def get_rewards(self, **kwargs):
        req = exchange_accounts_rpc_pb.RewardsRequest(
            account_address=kwargs.get("account_address"), epoch=kwargs.get("epoch")
        )
        return self.stubExchangeAccount.Rewards(req)

    # OracleRPC

    def stream_oracle_prices(
        self, base_symbol: str, quote_symbol: str, oracle_type: str
    ):
        req = oracle_rpc_pb.StreamPricesRequest(
            base_symbol=base_symbol, quote_symbol=quote_symbol, oracle_type=oracle_type
        )
        return self.stubOracle.StreamPrices(req)

    def get_oracle_prices(
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
        return self.stubOracle.Price(req)

    def get_oracle_list(self):
        req = oracle_rpc_pb.OracleListRequest()
        return self.stubOracle.OracleList(req)

    # InsuranceRPC

    def get_insurance_funds(self):
        req = insurance_rpc_pb.FundsRequest()
        return self.stubInsurance.Funds(req)

    def get_redemptions(self, **kwargs):
        req = insurance_rpc_pb.RedemptionsRequest(
            redeemer=kwargs.get("redeemer"),
            redemption_denom=kwargs.get("redemption_denom"),
            status=kwargs.get("status"),
        )
        return self.stubInsurance.Redemptions(req)

    # SpotRPC

    def get_spot_market(self, market_id: str):
        req = spot_exchange_rpc_pb.MarketRequest(market_id=market_id)
        return self.stubSpotExchange.Market(req)

    def get_spot_markets(self, **kwargs):
        req = spot_exchange_rpc_pb.MarketsRequest(
            market_status=kwargs.get("market_status"),
            base_denom=kwargs.get("base_denom"),
            quote_denom=kwargs.get("quote_denom"),
        )
        return self.stubSpotExchange.Markets(req)

    def stream_spot_markets(self, **kwargs):
        req = spot_exchange_rpc_pb.StreamMarketsRequest(
            market_ids=kwargs.get("market_ids"))
        metadata = self.get_cookie(type="exchange")
        res = self.stubSpotExchange.StreamMarkets(req, metadata=metadata)
        self.set_cookie(res,type="exchange")
        return res.tx_response

    def get_spot_orderbook(self, market_id: str):
        req = spot_exchange_rpc_pb.OrderbookRequest(market_id=market_id)
        return self.stubSpotExchange.Orderbook(req)

    def get_spot_orderbooks(self, market_ids: List):
        req = spot_exchange_rpc_pb.OrderbooksRequest(market_ids=market_ids)
        return self.stubSpotExchange.Orderbooks(req)

    def get_spot_orderbook_v2(self, market_id: str):
        req = spot_exchange_rpc_pb.OrderbookV2Request(market_id=market_id)
        return self.stubSpotExchange.OrderbookV2(req)

    def get_spot_orderbooks_v2(self, market_ids: List):
        req = spot_exchange_rpc_pb.OrderbooksV2Request(market_ids=market_ids)
        return self.stubSpotExchange.OrderbooksV2(req)

    def get_spot_orders(self, market_id: str, **kwargs):
        req = spot_exchange_rpc_pb.OrdersRequest(
            market_id=market_id,
            order_side=kwargs.get("order_side"),
            subaccount_id=kwargs.get("subaccount_id"),
        )
        return self.stubSpotExchange.Orders(req)

    def get_spot_trades(self, market_id: str, **kwargs):
        req = spot_exchange_rpc_pb.TradesRequest(
            market_id=market_id,
            execution_side=kwargs.get("execution_side"),
            direction=kwargs.get("direction"),
            subaccount_id=kwargs.get("subaccount_id"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
        )
        return self.stubSpotExchange.Trades(req)

    def stream_spot_orderbook(self, market_id: str):
        return self.stream_spot_orderbook_snapshot(market_ids=[market_id])

    def stream_spot_orderbook_snapshot(self, market_ids: List[str]):
        req = spot_exchange_rpc_pb.StreamOrderbookSnapshotRequest(market_ids=market_ids)
        metadata = self.get_cookie(type="exchange")
        res = self.stubSpotExchange.StreamOrderbookSnapshot(req, metadata=metadata)
        self.set_cookie(res, type="exchange")
        return res

    def stream_spot_orderbook_update(self, market_ids: List[str]):
        req = spot_exchange_rpc_pb.StreamOrderbookUpdateRequest(market_ids=market_ids)
        metadata = self.get_cookie(type="exchange")
        res = self.stubSpotExchange.StreamOrderbookUpdate(req, metadata=metadata)
        self.set_cookie(res, type="exchange")
        return res

    def stream_spot_orderbooks(self, market_ids: List):
        req = spot_exchange_rpc_pb.StreamOrderbookRequest(market_ids=market_ids)
        metadata = self.get_cookie(type="exchange")
        res = self.stubSpotExchange.StreamOrderbook(req, metadata=metadata)
        self.set_cookie(res,type="exchange")
        return res

    def stream_spot_orders(self, market_id: str, **kwargs):
        req = spot_exchange_rpc_pb.StreamOrdersRequest(
            market_id=market_id,
            order_side=kwargs.get("order_side"),
            subaccount_id=kwargs.get("subaccount_id"),
        )
        metadata = self.get_cookie(type="exchange")
        res = self.stubSpotExchange.StreamOrders(req, metadata=metadata)
        self.set_cookie(res,type="exchange")
        return res

    def stream_spot_trades(self, **kwargs):
        req = spot_exchange_rpc_pb.StreamTradesRequest(
            market_id=kwargs.get("market_id"),
            market_ids=kwargs.get("market_ids"),
            execution_side=kwargs.get("execution_side"),
            direction=kwargs.get("direction"),
            subaccount_id=kwargs.get("subaccount_id"),
            subaccount_ids=kwargs.get("subaccount_ids"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
        )
        metadata = self.get_cookie(type="exchange")
        res = self.stubSpotExchange.StreamTrades(req, metadata=metadata)
        self.set_cookie(res,type="exchange")
        return res

    def get_spot_subaccount_orders(self, subaccount_id: str, **kwargs):
        req = spot_exchange_rpc_pb.SubaccountOrdersListRequest(
            subaccount_id=subaccount_id, market_id=kwargs.get("market_id")
        )
        return self.stubSpotExchange.SubaccountOrdersList(req)

    def get_spot_subaccount_trades(self, subaccount_id: str, **kwargs):
        req = spot_exchange_rpc_pb.SubaccountTradesListRequest(
            subaccount_id=subaccount_id,
            market_id=kwargs.get("market_id"),
            execution_type=kwargs.get("execution_type"),
            direction=kwargs.get("direction"),
        )
        return self.stubSpotExchange.SubaccountTradesList(req)

    # DerivativeRPC

    def get_derivative_market(self, market_id: str):
        req = derivative_exchange_rpc_pb.MarketRequest(market_id=market_id)
        return self.stubDerivativeExchange.Market(req)

    def get_derivative_markets(self, **kwargs):
        req = derivative_exchange_rpc_pb.MarketsRequest(
            market_status=kwargs.get("market_status"),
            quote_denom=kwargs.get("quote_denom"),
        )
        return self.stubDerivativeExchange.Markets(req)

    def stream_derivative_markets(self, **kwargs):
        req = derivative_exchange_rpc_pb.StreamMarketRequest(
            market_ids=kwargs.get("market_ids"))
        metadata = self.get_cookie(type="exchange")
        res = self.stubDerivativeExchange.StreamMarket(req, metadata=metadata)
        self.set_cookie(res,type="exchange")
        return res

    def get_derivative_orderbook(self, market_id: str):
        req = derivative_exchange_rpc_pb.OrderbookRequest(market_id=market_id)
        return self.stubDerivativeExchange.Orderbook(req)

    def get_derivative_orderbooks(self, market_ids: List):
        req = derivative_exchange_rpc_pb.OrderbooksRequest(market_ids=market_ids)
        return self.stubDerivativeExchange.Orderbooks(req)

    def get_derivative_orderbook_v2(self, market_id: str):
        req = derivative_exchange_rpc_pb.OrderbookV2Request(market_id=market_id)
        return self.stubDerivativeExchange.OrderbookV2(req)

    def get_derivative_orderbooks_v2(self, market_ids: List):
        req = derivative_exchange_rpc_pb.OrderbooksV2Request(market_ids=market_ids)
        return self.stubDerivativeExchange.OrderbooksV2(req)

    def get_derivative_orders(self, market_id: str, **kwargs):
        req = derivative_exchange_rpc_pb.OrdersRequest(
            market_id=market_id,
            order_side=kwargs.get("order_side"),
            subaccount_id=kwargs.get("subaccount_id"),
        )
        return self.stubDerivativeExchange.Orders(req)

    def get_derivative_trades(self, market_id: str, **kwargs):
        req = derivative_exchange_rpc_pb.TradesRequest(
            market_id=market_id,
            subaccount_id=kwargs.get("subaccount_id"),
            execution_side=kwargs.get("execution_side"),
            direction=kwargs.get("direction"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
        )
        return self.stubDerivativeExchange.Trades(req)

    # deprecated: use stream_derivative_orderbook_snapshot
    def stream_derivative_orderbook(self, market_id: str):
        return self.stream_derivative_orderbook_snapshot(market_ids=[market_id])

    def stream_derivative_orderbook_snapshot(self, market_ids: List[str]):
        req = derivative_exchange_rpc_pb.StreamOrderbookSnapshotRequest(market_ids=market_ids)
        metadata = self.get_cookie(type="exchange")
        res = self.stubDerivativeExchange.StreamOrderbookSnapshot(req, metadata=metadata)
        self.set_cookie(res, type="exchange")
        return res

    def stream_derivative_orderbook_update(self, market_ids: List[str]):
        req = derivative_exchange_rpc_pb.StreamOrderbookUpdateRequest(market_ids=market_ids)
        metadata = self.get_cookie(type="exchange")
        res = self.stubDerivativeExchange.StreamOrderbookUpdate(req, metadata=metadata)
        self.set_cookie(res, type="exchange")
        return res

    def stream_derivative_orderbooks(self, market_ids: List):
        req = derivative_exchange_rpc_pb.StreamOrderbookRequest(market_ids=market_ids)
        metadata = self.get_cookie(type="exchange")
        res = self.stubDerivativeExchange.StreamOrderbook(req, metadata=metadata)
        self.set_cookie(res,type="exchange")
        return res

    def stream_derivative_orders(self, market_id: str, **kwargs):
        req = derivative_exchange_rpc_pb.StreamOrdersRequest(
            market_id=market_id,
            order_side=kwargs.get("order_side"),
            subaccount_id=kwargs.get("subaccount_id"),
        )
        metadata = self.get_cookie(type="exchange")
        res = self.stubDerivativeExchange.StreamOrders(req, metadata=metadata)
        self.set_cookie(res,type="exchange")
        return res

    def stream_derivative_trades(self, **kwargs):
        req = derivative_exchange_rpc_pb.StreamTradesRequest(
            market_id=kwargs.get("market_id"),
            market_ids=kwargs.get("market_ids"),
            subaccount_id=kwargs.get("subaccount_id"),
            subaccount_ids=kwargs.get("subaccount_ids"),
            execution_side=kwargs.get("execution_side"),
            direction=kwargs.get("direction"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
        )
        metadata = self.get_cookie(type="exchange")
        res = self.stubDerivativeExchange.StreamTrades(req, metadata=metadata)
        self.set_cookie(res,type="exchange")
        return res

    def get_derivative_positions(self, market_id: str, **kwargs):
        req = derivative_exchange_rpc_pb.PositionsRequest(
            market_id=market_id, subaccount_id=kwargs.get("subaccount_id")
        )
        return self.stubDerivativeExchange.Positions(req)

    def stream_derivative_positions(self, **kwargs):
        req = derivative_exchange_rpc_pb.StreamPositionsRequest(
            market_id=kwargs.get("market_id"),
            market_ids=kwargs.get("market_ids"),
            subaccount_id=kwargs.get("subaccount_id"),
            subaccount_ids=kwargs.get("subaccount_ids")
        )
        metadata = self.get_cookie(type="exchange")
        res = self.stubDerivativeExchange.StreamPositions(req, metadata=metadata)
        self.set_cookie(res,type="exchange")
        return res

    def get_derivative_liquidable_positions(self, **kwargs):
        req = derivative_exchange_rpc_pb.LiquidablePositionsRequest(
            market_id=kwargs.get("market_id")
        )
        return self.stubDerivativeExchange.LiquidablePositions(req)

    def get_derivative_subaccount_orders(self, subaccount_id: str, **kwargs):
        req = derivative_exchange_rpc_pb.SubaccountOrdersListRequest(
            subaccount_id=subaccount_id, market_id=kwargs.get("market_id")
        )
        return self.stubDerivativeExchange.SubaccountOrdersList(req)

    def get_derivative_subaccount_trades(self, subaccount_id: str, **kwargs):
        req = derivative_exchange_rpc_pb.SubaccountTradesListRequest(
            subaccount_id=subaccount_id,
            market_id=kwargs.get("market_id"),
            execution_type=kwargs.get("execution_type"),
            direction=kwargs.get("direction"),
        )
        return self.stubDerivativeExchange.SubaccountTradesList(req)

    def get_funding_payments(self, subaccount_id: str, **kwargs):
        req = derivative_exchange_rpc_pb.FundingPaymentsRequest(
            subaccount_id=subaccount_id,
            market_id=kwargs.get("market_id"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
        )
        return self.stubDerivativeExchange.FundingPayments(req)

    def get_funding_rates(self, market_id: str, **kwargs):
        req = derivative_exchange_rpc_pb.FundingRatesRequest(
            market_id=market_id,
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
        )
        return self.stubDerivativeExchange.FundingRates(req)
