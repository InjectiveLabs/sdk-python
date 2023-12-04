import asyncio

import grpc
import pytest

from pyinjective.client.indexer.grpc_stream.indexer_grpc_auction_stream import IndexerGrpcAuctionStream
from pyinjective.core.network import Network
from pyinjective.proto.exchange import injective_auction_rpc_pb2 as exchange_auction_pb
from tests.client.indexer.configurable_auction_query_servicer import ConfigurableAuctionQueryServicer


@pytest.fixture
def auction_servicer():
    return ConfigurableAuctionQueryServicer()


class TestIndexerGrpcAuctionStream:
    @pytest.mark.asyncio
    async def test_stream_oracle_prices_by_markets(
        self,
        auction_servicer,
    ):
        bidder = "inj1pdxq82m20fzkjn2th2mm5jp7t5ex6j6klf9cs5"
        amount = "1000000000000000000"
        round = 1
        timestamp = 1675426622603

        auction_servicer.stream_bids_responses.append(
            exchange_auction_pb.StreamBidsResponse(bidder=bidder, bid_amount=amount, round=round, timestamp=timestamp)
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcAuctionStream(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = auction_servicer

        bid_updates = asyncio.Queue()
        end_event = asyncio.Event()

        callback = lambda update: bid_updates.put_nowait(update)
        error_callback = lambda exception: pytest.fail(str(exception))
        end_callback = lambda: end_event.set()

        asyncio.get_event_loop().create_task(
            api.stream_bids(
                callback=callback,
                on_end_callback=end_callback,
                on_status_callback=error_callback,
            )
        )
        expected_update = {
            "bidAmount": amount,
            "bidder": bidder,
            "round": str(round),
            "timestamp": str(timestamp),
        }

        first_update = await asyncio.wait_for(bid_updates.get(), timeout=1)

        assert first_update == expected_update
        assert end_event.is_set()

    async def _dummy_metadata_provider(self):
        return None
