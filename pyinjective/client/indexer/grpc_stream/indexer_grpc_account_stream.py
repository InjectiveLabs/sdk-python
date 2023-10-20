import asyncio
from typing import Callable, Coroutine, List, Optional

from google.protobuf import json_format
from grpc import RpcError
from grpc.aio import Channel

from pyinjective.proto.exchange import (
    injective_accounts_rpc_pb2 as exchange_accounts_pb,
    injective_accounts_rpc_pb2_grpc as exchange_accounts_grpc,
)


class IndexerGrpcAccountStream:
    def __init__(self, channel: Channel, metadata_provider: Coroutine):
        self._stub = self._stub = exchange_accounts_grpc.InjectiveAccountsRPCStub(channel)
        self._metadata_provider = metadata_provider

    async def stream_subaccount_balance(
        self,
        subaccount_id: str,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        denoms: Optional[List[str]] = None,
    ):
        request = exchange_accounts_pb.StreamSubaccountBalanceRequest(
            subaccount_id=subaccount_id,
            denoms=denoms,
        )
        metadata = await self._metadata_provider
        stream = self._stub.StreamSubaccountBalance(request=request, metadata=metadata)

        try:
            async for balance_update in stream:
                update = json_format.MessageToDict(
                    message=balance_update,
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
