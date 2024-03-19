import grpc
import pytest

from pyinjective.client.indexer.grpc.indexer_grpc_auction_api import IndexerGrpcAuctionApi
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.exchange import injective_auction_rpc_pb2 as exchange_auction_pb
from tests.client.indexer.configurable_auction_query_servicer import ConfigurableAuctionQueryServicer


@pytest.fixture
def auction_servicer():
    return ConfigurableAuctionQueryServicer()


class TestIndexerGrpcAuctionApi:
    @pytest.mark.asyncio
    async def test_fetch_auction(
        self,
        auction_servicer,
    ):
        coin = exchange_auction_pb.Coin(
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            amount="2322098",
        )
        auction = exchange_auction_pb.Auction(
            winner="inj1uyk56r3xdcf60jwrmn7p9rgla9dc4gam56ajrq",
            basket=[coin],
            winning_bid_amount="2000000000000000000",
            round=31,
            end_timestamp=1676013187000,
            updated_at=1677075140258,
        )

        bid = exchange_auction_pb.Bid(
            bidder="inj1pdxq82m20fzkjn2th2mm5jp7t5ex6j6klf9cs5",
            amount="1000000000000000000",
            timestamp=1675426622603,
        )

        auction_servicer.auction_endpoint_responses.append(
            exchange_auction_pb.AuctionEndpointResponse(
                auction=auction,
                bids=[bid],
            )
        )

        api = self._api_instance(servicer=auction_servicer)

        result_auction = await api.fetch_auction(round=auction.round)
        expected_auction = {
            "auction": {
                "winner": auction.winner,
                "basket": [
                    {
                        "denom": coin.denom,
                        "amount": coin.amount,
                    }
                ],
                "winningBidAmount": auction.winning_bid_amount,
                "round": str(auction.round),
                "endTimestamp": str(auction.end_timestamp),
                "updatedAt": str(auction.updated_at),
            },
            "bids": [{"amount": bid.amount, "bidder": bid.bidder, "timestamp": str(bid.timestamp)}],
        }

        assert result_auction == expected_auction

    @pytest.mark.asyncio
    async def test_fetch_auctions(
        self,
        auction_servicer,
    ):
        coin = exchange_auction_pb.Coin(
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            amount="2322098",
        )
        auction = exchange_auction_pb.Auction(
            winner="inj1uyk56r3xdcf60jwrmn7p9rgla9dc4gam56ajrq",
            basket=[coin],
            winning_bid_amount="2000000000000000000",
            round=31,
            end_timestamp=1676013187000,
            updated_at=1677075140258,
        )

        auction_servicer.auctions_responses.append(exchange_auction_pb.AuctionsResponse(auctions=[auction]))

        api = self._api_instance(servicer=auction_servicer)

        result_auctions = await api.fetch_auctions()
        expected_auctions = {
            "auctions": [
                {
                    "winner": auction.winner,
                    "basket": [
                        {
                            "denom": coin.denom,
                            "amount": coin.amount,
                        }
                    ],
                    "winningBidAmount": auction.winning_bid_amount,
                    "round": str(auction.round),
                    "endTimestamp": str(auction.end_timestamp),
                    "updatedAt": str(auction.updated_at),
                }
            ]
        }

        assert result_auctions == expected_auctions

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = IndexerGrpcAuctionApi(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer

        return api
