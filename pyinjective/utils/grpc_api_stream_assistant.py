import asyncio
from typing import Callable, Optional

from google.protobuf import json_format
from grpc import RpcError


class GrpcApiStreamAssistant:
    def __init__(self, metadata_provider: Callable):
        super().__init__()
        self._metadata_provider = metadata_provider

    async def listen_stream(
        self,
        call: Callable,
        request,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
    ):
        metadata = await self._metadata_provider()
        stream = call(request, metadata=metadata)

        try:
            async for event in stream:
                parsed_event = json_format.MessageToDict(
                    message=event,
                    including_default_value_fields=True,
                )
                if asyncio.iscoroutinefunction(callback):
                    await callback(parsed_event)
                else:
                    callback(parsed_event)
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
