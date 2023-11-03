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

    async def Markets(self, request: exchange_spot_pb.MarketsRequest, context=None, metadata=None):
        return self.markets_responses.pop()

    async def Market(self, request: exchange_spot_pb.MarketRequest, context=None, metadata=None):
        return self.market_responses.pop()

    async def OrderbookV2(self, request: exchange_spot_pb.OrderbookV2Request, context=None, metadata=None):
        return self.orderbook_v2_responses.pop()
