import grpc
import pytest

from pyinjective.client.chain.grpc.chain_grpc_auction_api import ChainGrpcAuctionApi
from pyinjective.core.network import DisabledCookieAssistant, Network
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
            min_next_bid_increment_rate="2500000000000000",
            inj_basket_max_cap="100000",
            bidders_whitelist=["inj1pvt70tt7epjudnurkqlxu62flfgy46j2ytj7j5"],
        )
        auction_servicer.auction_params.append(auction_query_pb.QueryAuctionParamsResponse(params=params))

        api = self._api_instance(servicer=auction_servicer)

        module_params = await api.fetch_module_params()
        expected_params = {
            "params": {
                "auctionPeriod": str(params.auction_period),
                "minNextBidIncrementRate": params.min_next_bid_increment_rate,
                "injBasketMaxCap": str(params.inj_basket_max_cap),
                "biddersWhitelist": params.bidders_whitelist,
            }
        }

        assert expected_params == module_params

    @pytest.mark.asyncio
    async def test_fetch_module_state(
        self,
        auction_servicer,
    ):
        params = auction_pb.Params(
            auction_period=604800,
            min_next_bid_increment_rate="2500000000000000",
            inj_basket_max_cap="100000",
            bidders_whitelist=["inj1pvt70tt7epjudnurkqlxu62flfgy46j2ytj7j5"],
        )
        coin = coin_pb.Coin(denom="inj", amount="988987297011197594664")
        highest_bid = auction_pb.Bid(
            bidder="inj1pvt70tt7epjudnurkqlxu62flfgy46j2ytj7j5",
            amount=coin,
        )
        last_auction_result = auction_pb.LastAuctionResult(
            winner="inj1pvt70tt7epjudnurkqlxu62flfgy46j2ytj7j5",
            amount=coin,
            round=3,
        )
        state = genesis_pb.GenesisState(
            params=params,
            auction_round=50,
            highest_bid=highest_bid,
            auction_ending_timestamp=1687504387,
            last_auction_result=last_auction_result,
        )
        auction_servicer.module_states.append(auction_query_pb.QueryModuleStateResponse(state=state))

        api = self._api_instance(servicer=auction_servicer)

        module_state = await api.fetch_module_state()
        expected_state = {
            "state": {
                "auctionEndingTimestamp": "1687504387",
                "auctionRound": "50",
                "highestBid": {
                    "amount": {
                        "denom": coin.denom,
                        "amount": coin.amount,
                    },
                    "bidder": "inj1pvt70tt7epjudnurkqlxu62flfgy46j2ytj7j5",
                },
                "params": {
                    "auctionPeriod": str(params.auction_period),
                    "minNextBidIncrementRate": params.min_next_bid_increment_rate,
                    "injBasketMaxCap": str(params.inj_basket_max_cap),
                    "biddersWhitelist": params.bidders_whitelist,
                },
                "lastAuctionResult": {
                    "winner": last_auction_result.winner,
                    "amount": {
                        "denom": coin.denom,
                        "amount": coin.amount,
                    },
                    "round": str(last_auction_result.round),
                },
            }
        }

        assert expected_state == module_state

    @pytest.mark.asyncio
    async def test_fetch_module_state_when_no_highest_bid_present(
        self,
        auction_servicer,
    ):
        params = auction_pb.Params(
            auction_period=604800,
            min_next_bid_increment_rate="2500000000000000",
            inj_basket_max_cap="100000",
            bidders_whitelist=["inj1pvt70tt7epjudnurkqlxu62flfgy46j2ytj7j5"],
        )
        state = genesis_pb.GenesisState(
            params=params,
            auction_round=50,
            auction_ending_timestamp=1687504387,
        )
        auction_servicer.module_states.append(auction_query_pb.QueryModuleStateResponse(state=state))

        api = self._api_instance(servicer=auction_servicer)

        module_state = await api.fetch_module_state()
        expected_state = {
            "state": {
                "auctionEndingTimestamp": str(state.auction_ending_timestamp),
                "auctionRound": str(state.auction_round),
                "params": {
                    "auctionPeriod": str(params.auction_period),
                    "minNextBidIncrementRate": params.min_next_bid_increment_rate,
                    "injBasketMaxCap": str(params.inj_basket_max_cap),
                    "biddersWhitelist": params.bidders_whitelist,
                },
            }
        }

        assert expected_state == module_state

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

        auction_servicer.current_baskets.append(
            auction_query_pb.QueryCurrentAuctionBasketResponse(
                amount=[first_amount, second_amount],
                auctionRound=50,
                auctionClosingTime=1687504387,
                highestBidder="inj1pvt70tt7epjudnurkqlxu62flfgy46j2ytj7j5",
                highestBidAmount="2347518723906280000",
            )
        )

        api = self._api_instance(servicer=auction_servicer)

        current_basket = await api.fetch_current_basket()
        expected_basket = {
            "amount": [
                {
                    "amount": "15059786755",
                    "denom": "peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
                },
                {
                    "amount": "200000",
                    "denom": "peggy0xf9152067989BDc8783fF586624124C05A529A5D1",
                },
            ],
            "auctionClosingTime": "1687504387",
            "auctionRound": "50",
            "highestBidAmount": "2347518723906280000",
            "highestBidder": "inj1pvt70tt7epjudnurkqlxu62flfgy46j2ytj7j5",
        }

        assert expected_basket == current_basket

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = ChainGrpcAuctionApi(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer

        return api
