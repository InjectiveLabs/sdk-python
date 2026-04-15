from collections import deque

from pyinjective.proto.injective.auction.v1beta1 import (
    query_pb2 as auction_query_pb,
    query_pb2_grpc as auction_query_grpc,
)


class ConfigurableAuctionQueryServicer(auction_query_grpc.QueryServicer):
    def __init__(self):
        super().__init__()
        self.auction_params = deque()
        self.module_states = deque()
        self.current_baskets = deque()
        self.vouchers_responses = deque()
        self.voucher_responses = deque()
        self.last_auction_results = deque()

    async def AuctionParams(self, request: auction_query_pb.QueryAuctionParamsRequest, context=None, metadata=None):
        return self.auction_params.pop()

    async def AuctionModuleState(self, request: auction_query_pb.QueryModuleStateRequest, context=None, metadata=None):
        return self.module_states.pop()

    async def CurrentAuctionBasket(
        self, request: auction_query_pb.QueryCurrentAuctionBasketRequest, context=None, metadata=None
    ):
        return self.current_baskets.pop()

    async def LastAuctionResult(
        self, request: auction_query_pb.QueryLastAuctionResultRequest, context=None, metadata=None
    ):
        return self.last_auction_results.pop()

    async def Vouchers(self, request: auction_query_pb.QueryVouchersRequest, context=None, metadata=None):
        return self.vouchers_responses.pop()

    async def Voucher(self, request: auction_query_pb.QueryVoucherRequest, context=None, metadata=None):
        return self.voucher_responses.pop()
