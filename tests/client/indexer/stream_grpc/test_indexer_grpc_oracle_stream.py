import asyncio

import grpc
import pytest

from pyinjective.client.indexer.grpc_stream.indexer_grpc_oracle_stream import IndexerGrpcOracleStream
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.exchange import injective_oracle_rpc_pb2 as exchange_oracle_pb
from tests.client.indexer.configurable_oracle_query_servicer import ConfigurableOracleQueryServicer


@pytest.fixture
def oracle_servicer():
    return ConfigurableOracleQueryServicer()


class TestIndexerGrpcOracleStream:
    @pytest.mark.asyncio
    async def test_stream_oracle_prices(
        self,
        oracle_servicer,
    ):
        price = "0.00000000000002"
        timestamp = 1672218001897

        oracle_servicer.stream_prices_responses.append(
            exchange_oracle_pb.StreamPricesResponse(
                price=price,
                timestamp=timestamp,
            )
        )

        api = self._api_instance(servicer=oracle_servicer)

        price_updates = asyncio.Queue()
        end_event = asyncio.Event()

        callback = lambda update: price_updates.put_nowait(update)
        error_callback = lambda exception: pytest.fail(str(exception))
        end_callback = lambda: end_event.set()

        asyncio.get_event_loop().create_task(
            api.stream_oracle_prices(
                callback=callback,
                on_end_callback=end_callback,
                on_status_callback=error_callback,
                base_symbol="Gold",
                quote_symbol="USDT",
                oracle_type="pricefeed",
            )
        )
        expected_update = {"price": price, "timestamp": str(timestamp)}

        first_update = await asyncio.wait_for(price_updates.get(), timeout=1)

        assert first_update == expected_update
        assert end_event.is_set()

    @pytest.mark.asyncio
    async def test_stream_oracle_prices_by_markets(
        self,
        oracle_servicer,
    ):
        price = "0.00000000000002"
        timestamp = 1672218001897
        market_id = "0xa43d2be9861efb0d188b136cef0ae2150f80e08ec318392df654520dd359fcd7"

        oracle_servicer.stream_prices_by_markets_responses.append(
            exchange_oracle_pb.StreamPricesByMarketsResponse(
                price=price,
                timestamp=timestamp,
                market_id=market_id,
            )
        )

        api = self._api_instance(servicer=oracle_servicer)

        price_updates = asyncio.Queue()
        end_event = asyncio.Event()

        callback = lambda update: price_updates.put_nowait(update)
        error_callback = lambda exception: pytest.fail(str(exception))
        end_callback = lambda: end_event.set()

        asyncio.get_event_loop().create_task(
            api.stream_oracle_prices_by_markets(
                callback=callback,
                on_end_callback=end_callback,
                on_status_callback=error_callback,
                market_ids=[market_id],
            )
        )
        expected_update = {"price": price, "timestamp": str(timestamp), "marketId": market_id}

        first_update = await asyncio.wait_for(price_updates.get(), timeout=1)

        assert first_update == expected_update
        assert end_event.is_set()

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = IndexerGrpcOracleStream(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer

        return api
