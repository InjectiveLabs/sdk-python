from typing import Any, Dict

from grpc.aio import Channel

from pyinjective.proto.injective.auction.v1beta1 import (
    query_pb2 as auction_query_pb,
    query_pb2_grpc as auction_query_grpc,
)


class ChainGrpcAuctionApi:
    def __init__(self, channel: Channel):
        self._stub = auction_query_grpc.QueryStub(channel)

    async def fetch_module_params(self) -> Dict[str, Any]:
        request = auction_query_pb.QueryAuctionParamsRequest()
        response = await self._stub.AuctionParams(request)

        module_params = {
            "auction_period": response.params.auction_period,
            "min_next_bid_increment_rate": response.params.min_next_bid_increment_rate,
        }

        return module_params

    async def fetch_module_state(self) -> Dict[str, Any]:
        request = auction_query_pb.QueryModuleStateRequest()
        response = await self._stub.AuctionModuleState(request)

        if response.state.highest_bid is None:
            highest_bid = {
                "bidder": "",
                "amount": "",
            }
        else:
            highest_bid = {
                "bidder": response.state.highest_bid.bidder,
                "amount": response.state.highest_bid.amount,
            }

        module_state = {
            "params": {
                "auction_period": response.state.params.auction_period,
                "min_next_bid_increment_rate": response.state.params.min_next_bid_increment_rate,
            },
            "auction_round": response.state.auction_round,
            "highest_bid": highest_bid,
            "auction_ending_timestamp": response.state.auction_ending_timestamp,
        }

        return module_state

    async def fetch_current_basket(self) -> Dict[str, Any]:
        request = auction_query_pb.QueryCurrentAuctionBasketRequest()
        response = await self._stub.CurrentAuctionBasket(request)

        current_basket = {
            "amount_list": [{"amount": coin.amount, "denom": coin.denom} for coin in response.amount],
            "auction_round": response.auctionRound,
            "auction_closing_time": response.auctionClosingTime,
            "highest_bidder": response.highestBidder,
            "highest_bid_amount": response.highestBidAmount,
        }

        return current_basket
