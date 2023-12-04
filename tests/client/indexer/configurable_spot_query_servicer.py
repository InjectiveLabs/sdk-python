from collections import deque

from pyinjective.proto.exchange import (
    injective_spot_exchange_rpc_pb2 as exchange_spot_pb,
    injective_spot_exchange_rpc_pb2_grpc as exchange_spot_grpc,
)


class ConfigurableSpotQueryServicer(exchange_spot_grpc.InjectiveSpotExchangeRPCServicer):
    def __init__(self):
        super().__init__()
        self.markets_responses = deque()
        self.market_responses = deque()
        self.orderbook_v2_responses = deque()
        self.orderbooks_v2_responses = deque()
        self.orders_responses = deque()
        self.trades_responses = deque()
        self.subaccount_orders_list_responses = deque()
        self.subaccount_trades_list_responses = deque()
        self.orders_history_responses = deque()
        self.atomic_swap_history_responses = deque()

        self.stream_markets_responses = deque()
        self.stream_orderbook_v2_responses = deque()
        self.stream_orderbook_update_responses = deque()
        self.stream_orders_responses = deque()
        self.stream_trades_responses = deque()
        self.stream_orders_history_responses = deque()

    async def Markets(self, request: exchange_spot_pb.MarketsRequest, context=None, metadata=None):
        return self.markets_responses.pop()

    async def Market(self, request: exchange_spot_pb.MarketRequest, context=None, metadata=None):
        return self.market_responses.pop()

    async def OrderbookV2(self, request: exchange_spot_pb.OrderbookV2Request, context=None, metadata=None):
        return self.orderbook_v2_responses.pop()

    async def OrderbooksV2(self, request: exchange_spot_pb.OrderbooksV2Request, context=None, metadata=None):
        return self.orderbooks_v2_responses.pop()

    async def Orders(self, request: exchange_spot_pb.OrdersRequest, context=None, metadata=None):
        return self.orders_responses.pop()

    async def Trades(self, request: exchange_spot_pb.TradesRequest, context=None, metadata=None):
        return self.trades_responses.pop()

    async def SubaccountOrdersList(
        self, request: exchange_spot_pb.SubaccountOrdersListRequest, context=None, metadata=None
    ):
        return self.subaccount_orders_list_responses.pop()

    async def SubaccountTradesList(
        self, request: exchange_spot_pb.SubaccountTradesListRequest, context=None, metadata=None
    ):
        return self.subaccount_trades_list_responses.pop()

    async def OrdersHistory(self, request: exchange_spot_pb.OrdersHistoryRequest, context=None, metadata=None):
        return self.orders_history_responses.pop()

    async def AtomicSwapHistory(self, request: exchange_spot_pb.AtomicSwapHistoryRequest, context=None, metadata=None):
        return self.atomic_swap_history_responses.pop()

    async def StreamMarkets(self, request: exchange_spot_pb.StreamMarketsRequest, context=None, metadata=None):
        for event in self.stream_markets_responses:
            yield event

    async def StreamOrderbookV2(self, request: exchange_spot_pb.StreamOrderbookV2Request, context=None, metadata=None):
        for event in self.stream_orderbook_v2_responses:
            yield event

    async def StreamOrderbookUpdate(
        self, request: exchange_spot_pb.StreamOrderbookUpdateRequest, context=None, metadata=None
    ):
        for event in self.stream_orderbook_update_responses:
            yield event

    async def StreamOrders(self, request: exchange_spot_pb.StreamOrdersRequest, context=None, metadata=None):
        for event in self.stream_orders_responses:
            yield event

    async def StreamTrades(self, request: exchange_spot_pb.StreamTradesRequest, context=None, metadata=None):
        for event in self.stream_trades_responses:
            yield event

    async def StreamOrdersHistory(
        self, request: exchange_spot_pb.StreamOrdersHistoryRequest, context=None, metadata=None
    ):
        for event in self.stream_orders_history_responses:
            yield event
