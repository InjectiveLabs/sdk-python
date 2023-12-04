from typing import Callable, Optional

from grpc.aio import Channel

from pyinjective.proto.exchange import (
    injective_meta_rpc_pb2 as exchange_meta_pb,
    injective_meta_rpc_pb2_grpc as exchange_meta_grpc,
)
from pyinjective.utils.grpc_api_stream_assistant import GrpcApiStreamAssistant


class IndexerGrpcMetaStream:
    def __init__(self, channel: Channel, metadata_provider: Callable):
        self._stub = self._stub = exchange_meta_grpc.InjectiveMetaRPCStub(channel)
        self._assistant = GrpcApiStreamAssistant(metadata_provider=metadata_provider)

    async def stream_keepalive(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
    ):
        request = exchange_meta_pb.StreamKeepaliveRequest()

        await self._assistant.listen_stream(
            call=self._stub.StreamKeepalive,
            request=request,
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
        )
