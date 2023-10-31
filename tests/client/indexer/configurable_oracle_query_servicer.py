from collections import deque

from pyinjective.proto.exchange import (
    injective_oracle_rpc_pb2 as exchange_oracle_pb,
    injective_oracle_rpc_pb2_grpc as exchange_oracle_grpc,
)


class ConfigurableOracleQueryServicer(exchange_oracle_grpc.InjectiveOracleRPCServicer):
    def __init__(self):
        super().__init__()
        self.oracle_list_responses = deque()
        self.price_responses = deque()
        self.stream_prices_responses = deque()
        self.stream_prices_by_markets_responses = deque()

    async def OracleList(self, request: exchange_oracle_pb.OracleListRequest, context=None, metadata=None):
        return self.oracle_list_responses.pop()

    async def Price(self, request: exchange_oracle_pb.PriceRequest, context=None, metadata=None):
        return self.price_responses.pop()

    async def StreamPrices(self, request: exchange_oracle_pb.StreamPricesRequest, context=None, metadata=None):
        for event in self.stream_prices_responses:
            yield event

    async def StreamPricesByMarkets(
        self, request: exchange_oracle_pb.StreamPricesByMarketsRequest, context=None, metadata=None
    ):
        for event in self.stream_prices_by_markets_responses:
            yield event
