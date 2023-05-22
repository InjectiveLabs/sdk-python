from collections import deque

from pyinjective.proto.exchange.injective_spot_exchange_rpc_pb2 import (
    MarketsRequest,
    MarketsResponse,
)
from pyinjective.proto.exchange.injective_spot_exchange_rpc_pb2_grpc import InjectiveSpotExchangeRPCServicer


class ConfigurableInjectiveSpotExchangeRPCServicer(InjectiveSpotExchangeRPCServicer):

    def __init__(self):
        super().__init__()
        self.markets_queue = deque()

    def Markets(self, request: MarketsRequest, context):
        return self.markets_queue.pop()

