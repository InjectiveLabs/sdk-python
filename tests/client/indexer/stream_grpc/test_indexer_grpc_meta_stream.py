import asyncio

import grpc
import pytest

from pyinjective.client.indexer.grpc_stream.indexer_grpc_meta_stream import IndexerGrpcMetaStream
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.exchange import injective_meta_rpc_pb2 as exchange_meta_pb
from tests.client.indexer.configurable_meta_query_servicer import ConfigurableMetaQueryServicer


@pytest.fixture
def meta_servicer():
    return ConfigurableMetaQueryServicer()


class TestIndexerGrpcMetaStream:
    @pytest.mark.asyncio
    async def test_fetch_portfolio(
        self,
        meta_servicer,
    ):
        event = "test event"
        new_endpoint = "new test endpoint"
        timestamp = 1672218001897

        meta_servicer.stream_keepalive_responses.append(
            exchange_meta_pb.StreamKeepaliveResponse(
                event=event,
                new_endpoint=new_endpoint,
                timestamp=timestamp,
            )
        )

        api = self._api_instance(servicer=meta_servicer)

        keepalive_updates = asyncio.Queue()
        end_event = asyncio.Event()

        callback = lambda update: keepalive_updates.put_nowait(update)
        error_callback = lambda exception: pytest.fail(str(exception))
        end_callback = lambda: end_event.set()

        asyncio.get_event_loop().create_task(
            api.stream_keepalive(
                callback=callback,
                on_end_callback=end_callback,
                on_status_callback=error_callback,
            )
        )
        expected_update = {"event": event, "newEndpoint": new_endpoint, "timestamp": str(timestamp)}

        first_update = await asyncio.wait_for(keepalive_updates.get(), timeout=1)

        assert first_update == expected_update
        assert end_event.is_set()

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = IndexerGrpcMetaStream(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer

        return api
