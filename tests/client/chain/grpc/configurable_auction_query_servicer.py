from collections import deque

from pyinjective.proto.injective.auction.v1beta1 import (
    query_pb2_grpc as auction_query_grpc,
    query_pb2 as auction_query_pb,
)


class ConfigurableAuctionQueryServicer(auction_query_grpc.QueryServicer):

    def __init__(self):
        super().__init__()
        self.auction_params = deque()
        self.module_states = deque()
        self.current_baskets = deque()

    async def AuctionParams(self, request: auction_query_pb.QueryAuctionParamsRequest, context=None):
        return self.auction_params.pop()

    async def AuctionModuleState(self, request: auction_query_pb.QueryModuleStateRequest, context=None):
        return self.module_states.pop()

    async def CurrentAuctionBasket(self, request: auction_query_pb.QueryCurrentAuctionBasketRequest, context=None):
        return self.current_baskets.pop()
