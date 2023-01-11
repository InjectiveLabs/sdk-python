import os
import time
import grpc
import aiocron
import logging
import datetime
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
from .proto.cosmos.authz.v1beta1 import (
    query_pb2_grpc as authz_query_grpc,
    query_pb2 as authz_query,
    authz_pb2 as authz_type,
)
from .proto.cosmos.bank.v1beta1 import (
    query_pb2_grpc as bank_query_grpc,
    query_pb2 as bank_query,
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

from .proto.injective.types.v1beta1 import (
    account_pb2
)

from .constant import Network

DEFAULT_TIMEOUTHEIGHT_SYNC_INTERVAL = 20  # seconds
DEFAULT_TIMEOUTHEIGHT = 30  # blocks
DEFAULT_SESSION_RENEWAL_OFFSET = 120  # seconds
DEFAULT_BLOCK_TIME = 2  # seconds

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)


class AsyncClient:
    def __init__(
            self,
            network: Network,
            insecure: bool = False,
            load_balancer: bool = False,
            credentials=grpc.ssl_channel_credentials(),
            chain_cookie_location=".chain_cookie",
    ):

        # use append mode to create file if not exist
        self.chain_cookie_location = chain_cookie_location
        cookie_file = open(chain_cookie_location, "a+")
        cookie_file.close()

        self.addr = ""
        self.number = 0
        self.sequence = 0

        self.cookie_type = None
        self.expiration_format = None
        self.load_balancer = load_balancer

        if self.load_balancer is False:
            self.cookie_type = "grpc-cookie"
            self.expiration_format = "20{}"

        else:
            self.cookie_type = "GCLB"
            self.expiration_format = "{}"

        # chain stubs
        self.chain_channel = (
            grpc.aio.insecure_channel(network.grpc_endpoint)
            if (insecure or credentials is None)
            else grpc.aio.secure_channel(network.grpc_endpoint, credentials)
        )
        self.insecure = insecure
        self.stubCosmosTendermint = tendermint_query_grpc.ServiceStub(
            self.chain_channel
        )
        self.stubAuth = auth_query_grpc.QueryStub(self.chain_channel)
        self.stubAuthz = authz_query_grpc.QueryStub(self.chain_channel)
        self.stubBank = bank_query_grpc.QueryStub(self.chain_channel)
        self.stubTx = tx_service_grpc.ServiceStub(self.chain_channel)

        # attempt to load from disk
        cookie_file = open(chain_cookie_location, "r+")
        self.chain_cookie = cookie_file.read()
        cookie_file.close()
        logging.info(
            "chain session cookie loaded from disk:{}".format(self.chain_cookie)
        )

        self.exchange_cookie = ""
        self.timeout_height = 1

        # exchange stubs
        self.exchange_channel = (
            grpc.aio.insecure_channel(network.grpc_exchange_endpoint)
            if (insecure or credentials is None)
            else grpc.aio.secure_channel(network.grpc_exchange_endpoint, credentials)
        )
        self.stubMeta = exchange_meta_rpc_grpc.InjectiveMetaRPCStub(
            self.exchange_channel
        )
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
        self.stubAuction = auction_rpc_grpc.InjectiveAuctionRPCStub(
            self.exchange_channel
        )

        # explorer stubs
        self.explorer_channel = (
            grpc.aio.insecure_channel(network.grpc_explorer_endpoint)
            if (insecure or credentials is None)
            else grpc.aio.secure_channel(network.grpc_explorer_endpoint, credentials)
        )
        self.stubExplorer = explorer_rpc_grpc.InjectiveExplorerRPCStub(
            self.explorer_channel
        )

        # timeout height update routine
        self.cron = aiocron.crontab(
            "* * * * * */{}".format(DEFAULT_TIMEOUTHEIGHT_SYNC_INTERVAL),
            func=self.sync_timeout_height,
            args=(),
            start=True,
        )

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
            logging.debug("error while fetching latest block, setting timeout height to 0:{}".format(e))
            self.timeout_height = 0

    # cookie helper methods
    async def fetch_cookie(self, type):
        metadata = None
        if type == "chain":
            req = tendermint_query.GetLatestBlockRequest()
            metadata = await self.stubCosmosTendermint.GetLatestBlock(
                req
            ).initial_metadata()
            time.sleep(DEFAULT_BLOCK_TIME)
        if type == "exchange":
            req = exchange_meta_rpc_pb.VersionRequest()
            metadata = await self.stubMeta.Version(req).initial_metadata()
        return metadata

    async def renew_cookie(self, existing_cookie, type):
        metadata = None
        # format cookie date into RFC1123 standard
        cookie = SimpleCookie()
        cookie.load(existing_cookie)

        expires_at = cookie.get(f"{self.cookie_type}").get("expires")
        expires_at = expires_at.replace("-", " ")
        yyyy = f"{self.expiration_format}".format(expires_at[12:14])
        expires_at = expires_at[:12] + yyyy + expires_at[14:]

        # parse expire field to unix timestamp
        expire_timestamp = datetime.datetime.strptime(
            expires_at, "%a, %d %b %Y %H:%M:%S GMT"
        ).timestamp()

        # renew session if timestamp diff < offset
        timestamp_diff = expire_timestamp - int(time.time())
        if timestamp_diff < DEFAULT_SESSION_RENEWAL_OFFSET:
            metadata = await self.fetch_cookie(type)
        else:
            metadata = (("cookie", existing_cookie),)
        return metadata

    async def load_cookie(self, type):
        metadata = None
        if self.insecure:
            return metadata

        if type == "chain":
            if self.chain_cookie != "":
                metadata = await self.renew_cookie(self.chain_cookie, type)
                self.set_cookie(metadata, type)
            else:
                metadata = await self.fetch_cookie(type)
                self.set_cookie(metadata, type)

        if type == "exchange":
            if self.exchange_cookie != "":
                metadata = await self.renew_cookie(self.exchange_cookie, type)
                self.set_cookie(metadata, type)
            else:
                metadata = await self.fetch_cookie(type)
                self.set_cookie(metadata, type)

        return metadata

    def set_cookie(self, metadata, type):
        new_cookie = None
        if self.insecure:
            return new_cookie

        for k, v in metadata:
            if k == "set-cookie":
                new_cookie = v

        if new_cookie == None:
            return

        if type == "chain":
            # write to client instance
            self.chain_cookie = new_cookie
            # write to disk
            cookie_file = open(self.chain_cookie_location, "w")
            cookie_file.write(new_cookie)
            cookie_file.close()
            logging.info("chain session cookie saved to disk")

        if type == "exchange":
            self.exchange_cookie = new_cookie

    # default client methods
    async def get_latest_block(self) -> tendermint_query.GetLatestBlockResponse:
        req = tendermint_query.GetLatestBlockRequest()
        return await self.stubCosmosTendermint.GetLatestBlock(req)

    async def get_account(self, address: str) -> Optional[account_pb2.EthAccount]:
        try:
            metadata = await self.load_cookie(type="chain")
            account_any = (await self.stubAuth.Account(
                auth_query.QueryAccountRequest.__call__(address=address), metadata=metadata
            )).account
            account = account_pb2.EthAccount()
            if account_any.Is(account.DESCRIPTOR):
                account_any.Unpack(account)
                self.number = int(account.base_account.account_number)
                self.sequence = int(account.base_account.sequence)
        except Exception as e:
            logging.debug("error while fetching sequence and number{}".format(e))
            return None

    async def get_request_id_by_tx_hash(self, tx_hash: bytes) -> List[int]:
        tx = await self.stubTx.GetTx(tx_service.GetTxRequest(hash=tx_hash))
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

    async def simulate_tx(
            self, tx_byte: bytes
    ) -> Tuple[Union[abci_type.SimulationResponse, grpc.RpcError], bool]:
        try:
            req = tx_service.SimulateRequest(tx_bytes=tx_byte)
            metadata = await self.load_cookie(type="chain")
            return await self.stubTx.Simulate.__call__(req, metadata=metadata), True
        except grpc.RpcError as err:
            return err, False

    async def send_tx_sync_mode(self, tx_byte: bytes) -> abci_type.TxResponse:
        req = tx_service.BroadcastTxRequest(
            tx_bytes=tx_byte, mode=tx_service.BroadcastMode.BROADCAST_MODE_SYNC
        )
        metadata = await self.load_cookie(type="chain")
        result = await self.stubTx.BroadcastTx.__call__(req, metadata=metadata)
        return result.tx_response

    async def send_tx_async_mode(self, tx_byte: bytes) -> abci_type.TxResponse:
        req = tx_service.BroadcastTxRequest(
            tx_bytes=tx_byte, mode=tx_service.BroadcastMode.BROADCAST_MODE_ASYNC
        )
        metadata = await self.load_cookie(type="chain")
        result = await self.stubTx.BroadcastTx.__call__(req, metadata=metadata)
        return result.tx_response

    async def send_tx_block_mode(self, tx_byte: bytes) -> abci_type.TxResponse:
        req = tx_service.BroadcastTxRequest(
            tx_bytes=tx_byte, mode=tx_service.BroadcastMode.BROADCAST_MODE_BLOCK
        )
        metadata = await self.load_cookie(type="chain")
        result = await self.stubTx.BroadcastTx.__call__(req, metadata=metadata)
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
        return await self.stubBank.AllBalances(
            bank_query.QueryAllBalancesRequest(address=address)
        )

    async def get_bank_balance(self, address: str, denom: str):
        return await self.stubBank.Balance(
            bank_query.QueryBalanceRequest(address=address, denom=denom)
        )

    # Injective Exchange client methods

    # Auction RPC

    async def get_auction(self, bid_round: int):
        req = auction_rpc_pb.AuctionRequest(round=bid_round)
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

    async def stream_subaccount_balance(self, subaccount_id: str):
        req = exchange_accounts_rpc_pb.StreamSubaccountBalanceRequest(
            subaccount_id=subaccount_id
        )
        return self.stubExchangeAccount.StreamSubaccountBalance(req)

    async def get_subaccount_balance(self, subaccount_id: str, denom: str):
        req = exchange_accounts_rpc_pb.SubaccountBalanceRequest(
            subaccount_id=subaccount_id, denom=denom
        )
        return await self.stubExchangeAccount.SubaccountBalanceEndpoint(req)

    async def get_subaccount_list(self, account_address: str):
        req = exchange_accounts_rpc_pb.SubaccountsListRequest(
            account_address=account_address
        )
        return await self.stubExchangeAccount.SubaccountsList(req)

    async def get_subaccount_balances_list(self, subaccount_id: str):
        req = exchange_accounts_rpc_pb.SubaccountBalancesListRequest(
            subaccount_id=subaccount_id
        )
        return await self.stubExchangeAccount.SubaccountBalancesList(req)

    async def get_subaccount_history(self, subaccount_id: str, **kwargs):
        req = exchange_accounts_rpc_pb.SubaccountHistoryRequest(
            subaccount_id=subaccount_id,
            denom=kwargs.get("denom"),
            transfer_types=kwargs.get("transfer_types"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
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

    async def stream_oracle_prices(
            self, base_symbol: str, quote_symbol: str, oracle_type: str
    ):
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
        req = spot_exchange_rpc_pb.StreamMarketsRequest(
            market_ids=kwargs.get("market_ids")
        )
        metadata = await self.load_cookie(type="exchange")
        return self.stubSpotExchange.StreamMarkets.__call__(req, metadata=metadata)

    async def get_spot_orderbook(self, market_id: str):
        req = spot_exchange_rpc_pb.OrderbookRequest(market_id=market_id)
        return await self.stubSpotExchange.Orderbook(req)

    async def get_spot_orderbooks(self, market_ids: List):
        req = spot_exchange_rpc_pb.OrderbooksRequest(market_ids=market_ids)
        return await self.stubSpotExchange.Orderbooks(req)

    async def get_spot_orders(self, market_id: str, **kwargs):
        req = spot_exchange_rpc_pb.OrdersRequest(
            market_id=market_id,
            order_side=kwargs.get("order_side"),
            subaccount_id=kwargs.get("subaccount_id"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
        )
        return await self.stubSpotExchange.Orders(req)

    async def get_historical_spot_orders(self, market_id: str, **kwargs):
        req = spot_exchange_rpc_pb.OrdersHistoryRequest(
            market_id=market_id,
            direction=kwargs.get("direction"),
            order_types=kwargs.get("order_types"),
            execution_types=kwargs.get("execution_types"),
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
        )
        return await self.stubSpotExchange.Trades(req)

    # deprecated: use stream_spot_orderbook_snapshot
    async def stream_spot_orderbook(self, market_id: str):
        req = spot_exchange_rpc_pb.StreamOrderbookRequest(market_ids=[market_id])
        metadata = await self.load_cookie(type="exchange")
        return self.stubSpotExchange.StreamOrderbook.__call__(req, metadata=metadata)

    async def stream_spot_orderbook_snapshot(self, market_ids: List[str]):
        req = spot_exchange_rpc_pb.StreamOrderbookV2Request(market_ids=market_ids)
        metadata = await self.load_cookie(type="exchange")
        return self.stubSpotExchange.StreamOrderbookV2.__call__(req, metadata=metadata)

    async def stream_spot_orderbook_update(self, market_ids: List[str]):
        req = spot_exchange_rpc_pb.StreamOrderbookUpdateRequest(market_ids=market_ids)
        metadata = await self.load_cookie(type="exchange")
        return self.stubSpotExchange.StreamOrderbookUpdate.__call__(req, metadata=metadata)

    async def stream_spot_orderbooks(self, market_ids: List[str]):
        req = spot_exchange_rpc_pb.StreamOrderbookRequest(market_ids=market_ids)
        metadata = await self.load_cookie(type="exchange")
        return self.stubSpotExchange.StreamOrderbook.__call__(req, metadata=metadata)

    async def stream_spot_orders(self, market_id: str, **kwargs):
        req = spot_exchange_rpc_pb.StreamOrdersRequest(
            market_id=market_id,
            order_side=kwargs.get("order_side"),
            subaccount_id=kwargs.get("subaccount_id"),
        )
        metadata = await self.load_cookie(type="exchange")
        return self.stubSpotExchange.StreamOrders.__call__(req, metadata=metadata)

    async def stream_historical_spot_orders(self, market_id: str, **kwargs):
        req = spot_exchange_rpc_pb.StreamOrdersHistoryRequest(
            market_id=market_id,
            direction=kwargs.get("direction"),
            subaccount_id=kwargs.get("subaccount_id"),
            order_types=kwargs.get("order_types"),
            state=kwargs.get("state"),
            execution_types=kwargs.get("execution_types")
        )
        metadata = await self.load_cookie(type="exchange")
        return self.stubSpotExchange.StreamOrdersHistory.__call__(req, metadata=metadata)

    async def stream_historical_derivative_orders(self, market_id: str, **kwargs):
        req = derivative_exchange_rpc_pb.StreamOrdersHistoryRequest(
            market_id=market_id,
            direction=kwargs.get("direction"),
            subaccount_id=kwargs.get("subaccount_id"),
            order_types=kwargs.get("order_types"),
            state=kwargs.get("state"),
            execution_types=kwargs.get("execution_types")
        )
        metadata = await self.load_cookie(type="exchange")
        return self.stubDerivativeExchange.StreamOrdersHistory.__call__(req, metadata=metadata)

    async def stream_spot_trades(self, **kwargs):
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
        metadata = await self.load_cookie(type="exchange")
        return self.stubSpotExchange.StreamTrades.__call__(req, metadata=metadata)

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
        req = derivative_exchange_rpc_pb.StreamMarketRequest(
            market_ids=kwargs.get("market_ids")
        )
        metadata = await self.load_cookie(type="exchange")
        return self.stubDerivativeExchange.StreamMarket.__call__(req, metadata=metadata)

    async def get_derivative_orderbook(self, market_id: str):
        req = derivative_exchange_rpc_pb.OrderbookRequest(market_id=market_id)
        return await self.stubDerivativeExchange.Orderbook(req)

    async def get_derivative_orderbooks(self, market_ids: List):
        req = derivative_exchange_rpc_pb.OrderbooksRequest(market_ids=market_ids)
        return await self.stubDerivativeExchange.Orderbooks(req)

    async def get_derivative_orders(self, market_id: str, **kwargs):
        req = derivative_exchange_rpc_pb.OrdersRequest(
            market_id=market_id,
            order_side=kwargs.get("order_side"),
            subaccount_id=kwargs.get("subaccount_id"),
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
        )
        return await self.stubDerivativeExchange.Orders(req)

    async def get_historical_derivative_orders(self, market_id: str, **kwargs):
        req = derivative_exchange_rpc_pb.OrdersHistoryRequest(
            market_id=market_id,
            direction=kwargs.get("direction"),
            order_types=kwargs.get("order_types"),
            execution_types=kwargs.get("execution_types"),
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
        )
        return await self.stubDerivativeExchange.Trades(req)

    # deprecated: use stream_derivative_orderbook_snapshot
    async def stream_derivative_orderbook(self, market_id: str):
        req = derivative_exchange_rpc_pb.StreamOrderbookRequest(market_ids=[market_id])
        metadata = await self.load_cookie(type="exchange")
        return self.stubDerivativeExchange.StreamOrderbook.__call__(
            req, metadata=metadata
        )

    async def stream_derivative_orderbook_snapshot(self, market_ids: List[str]):
        req = derivative_exchange_rpc_pb.StreamOrderbookV2Request(market_ids=market_ids)
        metadata = await self.load_cookie(type="exchange")
        return self.stubDerivativeExchange.StreamOrderbookV2.__call__(
            req, metadata=metadata
        )

    async def stream_derivative_orderbook_update(self, market_ids: List[str]):
        req = derivative_exchange_rpc_pb.StreamOrderbookUpdateRequest(market_ids=market_ids)
        metadata = await self.load_cookie(type="exchange")
        return self.stubDerivativeExchange.StreamOrderbookUpdate.__call__(
            req, metadata=metadata
        )

    async def stream_derivative_orderbooks(self, market_ids: List[str]):
        req = derivative_exchange_rpc_pb.StreamOrderbookRequest(market_ids=market_ids)
        metadata = await self.load_cookie(type="exchange")
        return self.stubDerivativeExchange.StreamOrderbook.__call__(
            req, metadata=metadata
        )

    async def stream_derivative_orders(self, market_id: str, **kwargs):
        req = derivative_exchange_rpc_pb.StreamOrdersRequest(
            market_id=market_id,
            order_side=kwargs.get("order_side"),
            subaccount_id=kwargs.get("subaccount_id"),
        )
        metadata = await self.load_cookie(type="exchange")
        return self.stubDerivativeExchange.StreamOrders.__call__(req, metadata=metadata)

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
        )
        metadata = await self.load_cookie(type="exchange")
        return self.stubDerivativeExchange.StreamTrades.__call__(req, metadata=metadata)

    async def get_derivative_positions(self, **kwargs):
        req = derivative_exchange_rpc_pb.PositionsRequest(
            market_id=kwargs.get("market_id"),
            subaccount_id=kwargs.get("subaccount_id"),
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
        metadata = await self.load_cookie(type="exchange")
        return self.stubDerivativeExchange.StreamPositions.__call__(
            req, metadata=metadata
        )

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
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
        )
        return await self.stubDerivativeExchange.FundingPayments(req)

    async def get_funding_rates(self, market_id: str, **kwargs):
        req = derivative_exchange_rpc_pb.FundingRatesRequest(
            market_id=market_id,
            skip=kwargs.get("skip"),
            limit=kwargs.get("limit"),
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
