from collections import deque

from pyinjective.proto.exchange import (
    injective_derivative_exchange_rpc_pb2 as exchange_derivative_pb,
    injective_derivative_exchange_rpc_pb2_grpc as exchange_derivative_grpc,
)


class ConfigurableDerivativeQueryServicer(exchange_derivative_grpc.InjectiveDerivativeExchangeRPCServicer):
    def __init__(self):
        super().__init__()
        self.markets_responses = deque()
        self.market_responses = deque()
        self.binary_options_markets_responses = deque()
        self.binary_options_market_responses = deque()
        self.orderbook_v2_responses = deque()
        self.orderbooks_v2_responses = deque()
        self.orders_responses = deque()
        self.positions_responses = deque()
        self.positions_v2_responses = deque()
        self.liquidable_positions_responses = deque()
        self.funding_payments_responses = deque()
        self.funding_rates_responses = deque()
        self.trades_responses = deque()
        self.trades_v2_responses = deque()
        self.subaccount_orders_list_responses = deque()
        self.subaccount_trades_list_responses = deque()
        self.orders_history_responses = deque()

        self.stream_market_responses = deque()
        self.stream_orderbook_v2_responses = deque()
        self.stream_orderbook_update_responses = deque()
        self.stream_positions_responses = deque()
        self.stream_orders_responses = deque()
        self.stream_trades_responses = deque()
        self.stream_trades_v2_responses = deque()
        self.stream_orders_history_responses = deque()

    async def Markets(self, request: exchange_derivative_pb.MarketsRequest, context=None, metadata=None):
        return self.markets_responses.pop()

    async def Market(self, request: exchange_derivative_pb.MarketRequest, context=None, metadata=None):
        return self.market_responses.pop()

    async def BinaryOptionsMarkets(
        self, request: exchange_derivative_pb.BinaryOptionsMarketsRequest, context=None, metadata=None
    ):
        return self.binary_options_markets_responses.pop()

    async def BinaryOptionsMarket(
        self, request: exchange_derivative_pb.BinaryOptionsMarketRequest, context=None, metadata=None
    ):
        return self.binary_options_market_responses.pop()

    async def OrderbookV2(self, request: exchange_derivative_pb.OrderbookV2Request, context=None, metadata=None):
        return self.orderbook_v2_responses.pop()

    async def OrderbooksV2(self, request: exchange_derivative_pb.OrderbooksV2Request, context=None, metadata=None):
        return self.orderbooks_v2_responses.pop()

    async def Orders(self, request: exchange_derivative_pb.OrdersRequest, context=None, metadata=None):
        return self.orders_responses.pop()

    async def Positions(self, request: exchange_derivative_pb.PositionsRequest, context=None, metadata=None):
        return self.positions_responses.pop()

    async def PositionsV2(self, request: exchange_derivative_pb.PositionsV2Request, context=None, metadata=None):
        return self.positions_v2_responses.pop()

    async def LiquidablePositions(
        self, request: exchange_derivative_pb.LiquidablePositionsRequest, context=None, metadata=None
    ):
        return self.liquidable_positions_responses.pop()

    async def FundingPayments(
        self, request: exchange_derivative_pb.FundingPaymentsRequest, context=None, metadata=None
    ):
        return self.funding_payments_responses.pop()

    async def FundingRates(self, request: exchange_derivative_pb.FundingRatesRequest, context=None, metadata=None):
        return self.funding_rates_responses.pop()

    async def Trades(self, request: exchange_derivative_pb.TradesRequest, context=None, metadata=None):
        return self.trades_responses.pop()

    async def TradesV2(self, request: exchange_derivative_pb.TradesV2Request, context=None, metadata=None):
        return self.trades_v2_responses.pop()

    async def SubaccountOrdersList(
        self, request: exchange_derivative_pb.SubaccountOrdersListRequest, context=None, metadata=None
    ):
        return self.subaccount_orders_list_responses.pop()

    async def SubaccountTradesList(
        self, request: exchange_derivative_pb.SubaccountTradesListRequest, context=None, metadata=None
    ):
        return self.subaccount_trades_list_responses.pop()

    async def OrdersHistory(self, request: exchange_derivative_pb.OrdersHistoryRequest, context=None, metadata=None):
        return self.orders_history_responses.pop()

    async def StreamMarket(self, request: exchange_derivative_pb.StreamMarketRequest, context=None, metadata=None):
        for event in self.stream_market_responses:
            yield event

    async def StreamOrderbookV2(
        self, request: exchange_derivative_pb.StreamOrderbookV2Request, context=None, metadata=None
    ):
        for event in self.stream_orderbook_v2_responses:
            yield event

    async def StreamOrderbookUpdate(
        self, request: exchange_derivative_pb.StreamOrderbookUpdateRequest, context=None, metadata=None
    ):
        for event in self.stream_orderbook_update_responses:
            yield event

    async def StreamPositions(
        self, request: exchange_derivative_pb.StreamPositionsRequest, context=None, metadata=None
    ):
        for event in self.stream_positions_responses:
            yield event

    async def StreamOrders(self, request: exchange_derivative_pb.StreamOrdersRequest, context=None, metadata=None):
        for event in self.stream_orders_responses:
            yield event

    async def StreamTrades(self, request: exchange_derivative_pb.StreamTradesRequest, context=None, metadata=None):
        for event in self.stream_trades_responses:
            yield event

    async def StreamTradesV2(self, request: exchange_derivative_pb.StreamTradesV2Request, context=None, metadata=None):
        for event in self.stream_trades_v2_responses:
            yield event

    async def StreamOrdersHistory(
        self, request: exchange_derivative_pb.StreamOrdersHistoryRequest, context=None, metadata=None
    ):
        for event in self.stream_orders_history_responses:
            yield event
