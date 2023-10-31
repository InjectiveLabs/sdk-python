import asyncio
from typing import Callable, List, Optional

from google.protobuf import json_format
from grpc import RpcError
from grpc.aio import Channel

from pyinjective.proto.exchange import (
    injective_oracle_rpc_pb2 as exchange_oracle_pb,
    injective_oracle_rpc_pb2_grpc as exchange_oracle_grpc,
)


class IndexerGrpcOracleStream:
    def __init__(self, channel: Channel, metadata_provider: Callable):
        self._stub = self._stub = exchange_oracle_grpc.InjectiveOracleRPCStub(channel)
        self._metadata_provider = metadata_provider

    async def stream_oracle_prices(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        base_symbol: Optional[str] = None,
        quote_symbol: Optional[str] = None,
        oracle_type: Optional[str] = None,
    ):
        request = exchange_oracle_pb.StreamPricesRequest(
            base_symbol=base_symbol,
            quote_symbol=quote_symbol,
            oracle_type=oracle_type,
        )
        metadata = await self._metadata_provider()
        stream = self._stub.StreamPrices(request=request, metadata=metadata)

        try:
            async for price_update in stream:
                update = json_format.MessageToDict(
                    message=price_update,
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

    async def stream_oracle_prices_by_markets(
        self,
        market_ids: List[str],
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
    ):
        request = exchange_oracle_pb.StreamPricesByMarketsRequest(
            market_ids=market_ids,
        )
        metadata = await self._metadata_provider()
        stream = self._stub.StreamPricesByMarkets(request=request, metadata=metadata)

        try:
            async for price_update in stream:
                update = json_format.MessageToDict(
                    message=price_update,
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
