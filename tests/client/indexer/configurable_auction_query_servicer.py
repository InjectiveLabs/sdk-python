from collections import deque

from pyinjective.proto.exchange import (
    injective_auction_rpc_pb2 as exchange_auction_pb,
    injective_auction_rpc_pb2_grpc as exchange_auction_grpc,
)


class ConfigurableAuctionQueryServicer(exchange_auction_grpc.InjectiveAuctionRPCServicer):
    def __init__(self):
        super().__init__()
        self.auction_endpoint_responses = deque()
        self.auctions_responses = deque()
        self.stream_bids_responses = deque()

    async def AuctionEndpoint(self, request: exchange_auction_pb.AuctionEndpointRequest, context=None, metadata=None):
        return self.auction_endpoint_responses.pop()

    async def Auctions(self, request: exchange_auction_pb.AuctionsRequest, context=None, metadata=None):
        return self.auctions_responses.pop()

    async def StreamBids(self, request: exchange_auction_pb.StreamBidsRequest, context=None, metadata=None):
        for event in self.stream_bids_responses:
            yield event
