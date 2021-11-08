import grpc

from typing import List, Optional

from .exceptions import NotFoundError

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
    injective_derivative_exchange_rpc_pb2_grpc as derivative_exchange_rpc_grpc

)

from .constant import Network


class AsyncClient:
    def __init__(
            self,
            network: Network,
            insecure: bool = False,
            credentials: grpc.ChannelCredentials = None,
    ):
        # chain stubs
        self.chain_channel = (
            grpc.aio.insecure_channel(network.grpc_endpoint)
            if insecure
            else grpc.aio.secure_channel(
                network.grpc_endpoint,
                credentials or grpc.ssl_channel_credentials(),
                )
        )
        self.stubCosmosTendermint = tendermint_query_grpc.ServiceStub(self.chain_channel)
        self.stubAuth = auth_query_grpc.QueryStub(self.chain_channel)
        self.stubTx = tx_service_grpc.ServiceStub(self.chain_channel)

        # exchange stubs
        self.exchange_channel = (
            grpc.aio.insecure_channel(network.grpc_exchange_endpoint)
            if insecure
            else grpc.secure_channel(
                network.grpc_endpoint,
                credentials or grpc.ssl_channel_credentials(),
                )
        )
        self.stubExchangeAccount = exchange_accounts_rpc_grpc.InjectiveAccountsRPCStub(self.exchange_channel)
        self.stubOracle = oracle_rpc_grpc.InjectiveOracleRPCStub(self.exchange_channel)
        self.stubInsurance = insurance_rpc_grpc.InjectiveInsuranceRPCStub(self.exchange_channel)
        self.stubSpotExchange = spot_exchange_rpc_grpc.InjectiveSpotExchangeRPCStub(self.exchange_channel)
        self.stubDerivativeExchange = derivative_exchange_rpc_grpc.InjectiveDerivativeExchangeRPCStub(self.exchange_channel)

    # default client methods
    async def get_latest_block(self) -> tendermint_query.GetLatestBlockResponse:
        return await self.stubCosmosTendermint.GetLatestBlock(tendermint_query.GetLatestBlockRequest())

    async def get_account(self, address: str) -> Optional[auth_type.BaseAccount]:
        try:
            account_any = await self.stubAuth.Account(auth_query.QueryAccountRequest(address=address)).account
            account = auth_type.BaseAccount()
            if account_any.Is(account.DESCRIPTOR):
                account_any.Unpack(account)
                return account
        except:
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

    async def simulate_tx(self, tx_byte: bytes) -> abci_type.SimulationResponse:
        try:
            return (await self.stubTx.Simulate(
                tx_service.SimulateRequest(tx_bytes=tx_byte)
            ), True)
        except grpc.RpcError as err:
            return (err, False)

    async def send_tx_sync_mode(self, tx_byte: bytes) -> abci_type.TxResponse:
        result = await self.stubTx.BroadcastTx(
            tx_service.BroadcastTxRequest(tx_bytes=tx_byte, mode=tx_service.BroadcastMode.BROADCAST_MODE_SYNC)
        )
        return result.tx_response

    async def send_tx_async_mode(self, tx_byte: bytes) -> abci_type.TxResponse:
        result = await self.stubTx.BroadcastTx(
            tx_service.BroadcastTxRequest(tx_bytes=tx_byte, mode=tx_service.BroadcastMode.BROADCAST_MODE_ASYNC)
        )
        return result.tx_response

    async def send_tx_block_mode(self, tx_byte: bytes) -> abci_type.TxResponse:
        result = await self.stubTx.BroadcastTx(
            tx_service.BroadcastTxRequest(tx_bytes=tx_byte, mode=tx_service.BroadcastMode.BROADCAST_MODE_BLOCK)
        )
        return result.tx_response

    async def get_chain_id(self) -> str:
        latest_block = await self.get_latest_block()
        return latest_block.block.header.chain_id

    # injective exchange client methods

    #AccountsRPC
    async def stream_subaccount_balance(self, subaccount_id: str):
        req = exchange_accounts_rpc_pb.StreamSubaccountBalanceRequest(subaccount_id=subaccount_id)
        return self.stubExchangeAccount.StreamSubaccountBalance(req)

    async def get_subaccount_balance(self, subaccount_id: str, denom: str):
        req = exchange_accounts_rpc_pb.SubaccountBalanceRequest(subaccount_id=subaccount_id, denom=denom)
        return await self.stubExchangeAccount.SubaccountBalanceEndpoint(req)

    async def get_subaccount_list(self, account_address: str):
        req = exchange_accounts_rpc_pb.SubaccountsListRequest(account_address=account_address)
        return await self.stubExchangeAccount.SubaccountsList(req)

    async def get_subaccount_balances_list(self, subaccount_id: str):
        req = exchange_accounts_rpc_pb.SubaccountBalancesListRequest(subaccount_id=subaccount_id)
        return await self.stubExchangeAccount.SubaccountBalancesList(req)

    async def get_subaccount_history(self, subaccount_id: str, denom: str = '', transfer_types: list = []):
        req = exchange_accounts_rpc_pb.SubaccountHistoryRequest(subaccount_id=subaccount_id, denom=denom, transfer_types=transfer_types)
        return await self.stubExchangeAccount.SubaccountHistory(req)

    async def get_subaccount_order_summary(self, subaccount_id: str, order_direction: str = '', market_id: str = ''):
        req = exchange_accounts_rpc_pb.SubaccountOrderSummaryRequest(subaccount_id=subaccount_id, order_direction=order_direction, market_id=market_id)
        return await self.stubExchangeAccount.SubaccountOrderSummary(req)

    #OracleRPC
    async def stream_oracle_prices(self, base_symbol: str, quote_symbol: str, oracle_type: str):
        req = oracle_rpc_pb.StreamPricesRequest(base_symbol=base_symbol, quote_symbol=quote_symbol, oracle_type=oracle_type)
        return self.stubOracle.StreamPrices(req)

    async def get_oracle_prices(self, base_symbol: str, quote_symbol: str, oracle_type: str, oracle_scale_factor: str):
        req = oracle_rpc_pb.PriceRequest(base_symbol=base_symbol, quote_symbol=quote_symbol, oracle_type=oracle_type, oracle_scale_factor=oracle_scale_factor)
        return await self.stubOracle.Price(req)

    async def get_oracle_list(self):
        req = oracle_rpc_pb.OracleListRequest()
        return await self.stubOracle.OracleList(req)

    #InsuranceRPC

    async def get_insurance_funds(self):
        req = insurance_rpc_pb.FundsRequest()
        return await self.stubInsurance.Funds(req)

    async def get_redemptions(self, redeemer: str = '', redemption_denom: str = '', status: str = ''):
        req = insurance_rpc_pb.RedemptionsRequest(redeemer=redeemer, redemption_denom=redemption_denom, status=status)
        return await self.stubInsurance.Redemptions(req)

    #SpotRPC

    async def get_spot_market(self, market_id: str):
        req = spot_exchange_rpc_pb.MarketRequest(market_id=market_id)
        return await self.stubSpotExchange.Market(req)

    async def get_spot_markets(self, market_status: str ='', base_denom: str = '', quote_denom: str =''):
        req = spot_exchange_rpc_pb.MarketsRequest(market_status=market_status, base_denom=base_denom, quote_denom=quote_denom)
        return await self.stubSpotExchange.Markets(req)

    async def stream_spot_markets(self):
        req = spot_exchange_rpc_pb.StreamMarketsRequest()
        return self.stubSpotExchange.StreamMarkets(req)

    async def get_spot_orderbook(self, market_id: str):
        req = spot_exchange_rpc_pb.OrderbookRequest(market_id=market_id)
        return await self.stubSpotExchange.Orderbook(req)

    async def get_spot_orders(self, market_id: str, order_side: str = '', subaccount_id: str = ''):
        req = spot_exchange_rpc_pb.OrdersRequest(market_id=market_id, order_side=order_side, subaccount_id=subaccount_id)
        return await self.stubSpotExchange.Orders(req)

    async def get_spot_trades(self, market_id: str, execution_side: str = '', direction: str = '', subaccount_id: str = ''):
        req = spot_exchange_rpc_pb.TradesRequest(market_id=market_id, execution_side=execution_side, direction=direction, subaccount_id=subaccount_id)
        return await self.stubSpotExchange.Trades(req)

    async def stream_spot_orderbook(self, market_id: str):
        req = spot_exchange_rpc_pb.StreamOrderbookRequest(market_id=market_id)
        return self.stubSpotExchange.StreamOrderbook(req)

    async def stream_spot_orders(self, market_id: str, order_side: str = '', subaccount_id: str =''):
        req = spot_exchange_rpc_pb.StreamOrdersRequest(market_id=market_id, order_side=order_side, subaccount_id=subaccount_id)
        return self.stubSpotExchange.StreamOrders(req)

    async def stream_spot_trades(self, market_id: str, execution_side: str = '', direction: str = '', subaccount_id: str = ''):
        req = spot_exchange_rpc_pb.StreamTradesRequest(market_id=market_id, execution_side=execution_side, direction=direction, subaccount_id=subaccount_id)
        return self.stubSpotExchange.StreamTrades(req)

    async def get_spot_subaccount_orders(self, subaccount_id: str, market_id: str =''):
        req = spot_exchange_rpc_pb.SubaccountOrdersListRequest(subaccount_id=subaccount_id, market_id=market_id)
        return await self.stubSpotExchange.SubaccountOrdersList(req)

    async def get_spot_subaccount_trades(self, subaccount_id: str, market_id: str = '', execution_type: str = '', direction: str = ''):
        req = spot_exchange_rpc_pb.SubaccountTradesListRequest(subaccount_id=subaccount_id, market_id=market_id, execution_type=execution_type, direction=direction)
        return await self.stubSpotExchange.SubaccountTradesList(req)

    #DerivativeRPC
    async def get_derivative_market(self, market_id: str):
        req = spot_exchange_rpc_pb.MarketRequest(market_id=market_id)
        return await self.stubDerivativeExchange.Market(req)

    async def get_derivative_markets(self, market_status: str ='', quote_denom: str = ''):
        req = derivative_exchange_rpc_pb.MarketsRequest(market_status=market_status, quote_denom=quote_denom)
        return await self.stubDerivativeExchange.Markets(req)

    async def stream_derivative_markets(self):
        req = derivative_exchange_rpc_pb.StreamMarketRequest()
        return self.stubDerivativeExchange.StreamMarket(req)

    async def get_derivative_orderbook(self, market_id: str):
        req = derivative_exchange_rpc_pb.OrderbookRequest(market_id=market_id)
        return await self.stubDerivativeExchange.Orderbook(req)

    async def get_derivative_orders(self, market_id: str, order_side: str = '', subaccount_id: str = ''):
        req = derivative_exchange_rpc_pb.OrdersRequest(market_id=market_id, order_side=order_side, subaccount_id=subaccount_id)
        return await self.stubDerivativeExchange.Orders(req)

    async def get_derivative_trades(self, market_id: str, subaccount_id: str = ''):
        req = derivative_exchange_rpc_pb.TradesRequest(market_id=market_id, subaccount_id=subaccount_id)
        return await self.stubDerivativeExchange.Trades(req)

    async def stream_derivative_orderbook(self, market_id: str):
        req = derivative_exchange_rpc_pb.StreamOrderbookRequest(market_id=market_id)
        return self.stubDerivativeExchange.StreamOrderbook(req)

    async def stream_derivative_orders(self, market_id: str, order_side: str = '', subaccount_id: str = ''):
        req = derivative_exchange_rpc_pb.StreamOrdersRequest(market_id=market_id, order_side=order_side, subaccount_id=subaccount_id)
        return self.stubDerivativeExchange.StreamOrders(req)

    async def stream_derivative_trades(self, market_id: str, subaccount_id: str = ''):
        req = derivative_exchange_rpc_pb.StreamTradesRequest(market_id=market_id, subaccount_id=subaccount_id)
        return self.stubDerivativeExchange.StreamTrades(req)

    async def get_derivative_positions(self, market_id: str, subaccount_id: str =''):
        req = derivative_exchange_rpc_pb.PositionsRequest(market_id=market_id, subaccount_id=subaccount_id)
        return await self.stubDerivativeExchange.Positions(req)

    async def stream_derivative_positions(self, market_id: str, subaccount_id: str = ''):
        req = derivative_exchange_rpc_pb.StreamPositionsRequest(market_id=market_id, subaccount_id=subaccount_id)
        return self.stubDerivativeExchange.StreamPositions(req)

    async def get_derivative_liquidable_positions(self, market_id: str = ''):
        req = derivative_exchange_rpc_pb.LiquidablePositionsRequest(market_id=market_id)
        return await self.stubDerivativeExchange.LiquidablePositions(req)

    async def get_derivative_subaccount_orders(self, subaccount_id: str, market_id: str = ''):
        req = derivative_exchange_rpc_pb.SubaccountOrdersListRequest(subaccount_id=subaccount_id, market_id=market_id)
        return await self.stubDerivativeExchange.SubaccountOrdersList(req)

    async def get_derivative_subaccount_trades(self, subaccount_id: str, market_id: str = '', execution_type: str = '', direction: str = ''):
        req = derivative_exchange_rpc_pb.SubaccountTradesListRequest(subaccount_id=subaccount_id, market_id=market_id, execution_type=execution_type, direction=direction)
        return await self.stubDerivativeExchange.SubaccountTradesList(req)

    async def get_funding_payments(self, subaccount_id: str, market_id: str = ''):
        req = derivative_exchange_rpc_pb.FundingPaymentsRequest(subaccount_id=subaccount_id, market_id=market_id)
        return await self.stubDerivativeExchange.FundingPayments(req)
