import grpc
import pytest

from pyinjective.client.chain.grpc.chain_grpc_auction_api import ChainGrpcAuctionApi
from pyinjective.constant import Network
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as coin_pb
from pyinjective.proto.injective.auction.v1beta1 import (
    auction_pb2 as auction_pb,
    genesis_pb2 as genesis_pb,
    query_pb2 as auction_query_pb,
)
from tests.client.chain.grpc.configurable_auction_query_servicer import ConfigurableAuctionQueryServicer


@pytest.fixture
def auction_servicer():
    return ConfigurableAuctionQueryServicer()


class TestChainGrpcAuctionApi:

    @pytest.mark.asyncio
    async def test_fetch_module_params(
            self,
            auction_servicer,
    ):
        params = auction_pb.Params(
            auction_period=604800,
            min_next_bid_increment_rate="2500000000000000"
        )
        auction_servicer.auction_params.append(auction_query_pb.QueryAuctionParamsResponse(
            params=params
        ))

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = ChainGrpcAuctionApi(channel=channel)
        api._stub = auction_servicer

        module_params = await api.fetch_module_params()
        expected_params = {
            "auction_period": 604800,
            "min_next_bid_increment_rate": "2500000000000000",
        }

        assert (expected_params == module_params)

    @pytest.mark.asyncio
    async def test_fetch_module_state(
            self,
            auction_servicer,
    ):
        params = auction_pb.Params(
            auction_period=604800,
            min_next_bid_increment_rate="2500000000000000"
        )
        highest_bid = auction_pb.Bid(
            bidder="inj1pvt70tt7epjudnurkqlxu62flfgy46j2ytj7j5",
            amount="\n\003inj\022\0232347518723906280000",
        )
        state = genesis_pb.GenesisState(
            params=params,
            auction_round=50,
            highest_bid=highest_bid,
            auction_ending_timestamp=1687504387,
        )
        auction_servicer.module_states.append(auction_query_pb.QueryModuleStateResponse(
            state=state
        ))

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = ChainGrpcAuctionApi(channel=channel)
        api._stub = auction_servicer

        module_state = await api.fetch_module_state()
        expected_state = {
            "params": {
                "auction_period": 604800,
                "min_next_bid_increment_rate": "2500000000000000",
            },
            "auction_round": 50,
            "highest_bid": {
                "bidder": "inj1pvt70tt7epjudnurkqlxu62flfgy46j2ytj7j5",
                "amount": "\n\003inj\022\0232347518723906280000",
            },
            "auction_ending_timestamp": 1687504387,
        }

        assert (expected_state == module_state)

    @pytest.mark.asyncio
    async def test_fetch_module_state_when_no_highest_bid_present(
            self,
            auction_servicer,
    ):
        params = auction_pb.Params(
            auction_period=604800,
            min_next_bid_increment_rate="2500000000000000"
        )
        state = genesis_pb.GenesisState(
            params=params,
            auction_round=50,
            auction_ending_timestamp=1687504387,
        )
        auction_servicer.module_states.append(auction_query_pb.QueryModuleStateResponse(
            state=state
        ))

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = ChainGrpcAuctionApi(channel=channel)
        api._stub = auction_servicer

        module_state = await api.fetch_module_state()
        expected_state = {
            "params": {
                "auction_period": 604800,
                "min_next_bid_increment_rate": "2500000000000000",
            },
            "auction_round": 50,
            "highest_bid": {
                "bidder": "",
                "amount": "",
            },
            "auction_ending_timestamp": 1687504387,
        }

        assert (expected_state == module_state)

    @pytest.mark.asyncio
    async def test_fetch_current_basket(
            self,
            auction_servicer,
    ):
        first_amount = coin_pb.Coin(
            amount="15059786755",
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
        )
        second_amount = coin_pb.Coin(
            amount="200000",
            denom="peggy0xf9152067989BDc8783fF586624124C05A529A5D1",
        )

        auction_servicer.current_baskets.append(auction_query_pb.QueryCurrentAuctionBasketResponse(
            amount=[first_amount, second_amount],
            auctionRound=50,
            auctionClosingTime=1687504387,
            highestBidder="inj1pvt70tt7epjudnurkqlxu62flfgy46j2ytj7j5",
            highestBidAmount="2347518723906280000",
        ))

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = ChainGrpcAuctionApi(channel=channel)
        api._stub = auction_servicer

        current_basket = await api.fetch_current_basket()
        expected_basket = {
            "amount_list": [{"amount": coin.amount, "denom": coin.denom} for coin in [first_amount, second_amount]],
            "auction_round": 50,
            "auction_closing_time": 1687504387,
            "highest_bidder": "inj1pvt70tt7epjudnurkqlxu62flfgy46j2ytj7j5",
            "highest_bid_amount": "2347518723906280000",
        }

        assert (expected_basket == current_basket)
