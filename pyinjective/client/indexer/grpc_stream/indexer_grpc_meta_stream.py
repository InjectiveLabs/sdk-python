import asyncio
from typing import Callable, Optional

from google.protobuf import json_format
from grpc import RpcError
from grpc.aio import Channel

from pyinjective.proto.exchange import (
    injective_meta_rpc_pb2 as exchange_meta_pb,
    injective_meta_rpc_pb2_grpc as exchange_meta_grpc,
)


class IndexerGrpcMetaStream:
    def __init__(self, channel: Channel, metadata_provider: Callable):
        self._stub = self._stub = exchange_meta_grpc.InjectiveMetaRPCStub(channel)
        self._metadata_provider = metadata_provider

    async def stream_keepalive(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
    ):
        request = exchange_meta_pb.StreamKeepaliveRequest()
        metadata = await self._metadata_provider()
        stream = self._stub.StreamKeepalive(request=request, metadata=metadata)

        try:
            async for keepalive_update in stream:
                update = json_format.MessageToDict(
                    message=keepalive_update,
                    including_default_value_fields=True,
                )
                if asyncio.iscoroutinefunction(callback):
                    await callback(update)
                else:
                    callback(update)
        except RpcError as ex:
            if on_status_callback is not None:
                if asyncio.iscoroutinefunction(on_status_callback):
                    await on_status_callback(ex)
                else:
                    on_status_callback(ex)

        if on_end_callback is not None:
            if asyncio.iscoroutinefunction(on_end_callback):
                await on_end_callback()
            else:
                on_end_callback()
