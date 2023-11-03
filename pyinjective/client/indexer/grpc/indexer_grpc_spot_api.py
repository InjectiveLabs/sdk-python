from typing import Any, Callable, Dict, Optional

from grpc.aio import Channel

from pyinjective.proto.exchange import (
    injective_spot_exchange_rpc_pb2 as exchange_spot_pb,
    injective_spot_exchange_rpc_pb2_grpc as exchange_spot_grpc,
)
from pyinjective.utils.grpc_api_request_assistant import GrpcApiRequestAssistant


class IndexerGrpcSpotApi:
    def __init__(self, channel: Channel, metadata_provider: Callable):
        self._stub = self._stub = exchange_spot_grpc.InjectiveSpotExchangeRPCStub(channel)
        self._assistant = GrpcApiRequestAssistant(metadata_provider=metadata_provider)

    async def fetch_markets(
        self,
        market_status: Optional[str] = None,
        base_denom: Optional[str] = None,
        quote_denom: Optional[str] = None,
    ) -> Dict[str, Any]:
        request = exchange_spot_pb.MarketsRequest(
            market_status=market_status,
            base_denom=base_denom,
            quote_denom=quote_denom,
        )
        response = await self._execute_call(call=self._stub.Markets, request=request)

        return response

    async def fetch_market(self, market_id: str) -> Dict[str, Any]:
        request = exchange_spot_pb.MarketRequest(market_id=market_id)
        response = await self._execute_call(call=self._stub.Market, request=request)

        return response

    async def fetch_orderbook_v2(self, market_id: str) -> Dict[str, Any]:
        request = exchange_spot_pb.OrderbookV2Request(market_id=market_id)
        response = await self._execute_call(call=self._stub.OrderbookV2, request=request)

        return response

    async def _execute_call(self, call: Callable, request) -> Dict[str, Any]:
        return await self._assistant.execute_call(call=call, request=request)
