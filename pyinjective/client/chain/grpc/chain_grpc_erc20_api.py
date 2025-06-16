from typing import Any, Callable, Dict, Optional

from grpc.aio import Channel

from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import CookieAssistant
from pyinjective.proto.injective.erc20.v1beta1 import query_pb2 as erc20_query_pb, query_pb2_grpc as erc20_query_grpc
from pyinjective.utils.grpc_api_request_assistant import GrpcApiRequestAssistant


class ChainGrpcERC20Api:
    def __init__(self, channel: Channel, cookie_assistant: CookieAssistant):
        self._stub = erc20_query_grpc.QueryStub(channel)
        self._assistant = GrpcApiRequestAssistant(cookie_assistant=cookie_assistant)

    async def fetch_erc20_params(self) -> Dict[str, Any]:
        request = erc20_query_pb.QueryParamsRequest()
        response = await self._execute_call(call=self._stub.Params, request=request)

        return response

    async def fetch_all_token_pairs(
        self,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        pagination_request = None
        if pagination is not None:
            pagination_request = pagination.create_pagination_request()
        request = erc20_query_pb.QueryAllTokenPairsRequest(
            pagination=pagination_request,
        )
        response = await self._execute_call(call=self._stub.AllTokenPairs, request=request)

        return response

    async def fetch_token_pair_by_denom(self, bank_denom: str) -> Dict[str, Any]:
        request = erc20_query_pb.QueryTokenPairByDenomRequest(bank_denom=bank_denom)
        response = await self._execute_call(call=self._stub.TokenPairByDenom, request=request)

        return response

    async def fetch_token_pair_by_erc20_address(self, erc20_address: str) -> Dict[str, Any]:
        request = erc20_query_pb.QueryTokenPairByERC20AddressRequest(erc20_address=erc20_address)
        response = await self._execute_call(call=self._stub.TokenPairByERC20Address, request=request)

        return response

    async def _execute_call(self, call: Callable, request) -> Dict[str, Any]:
        return await self._assistant.execute_call(call=call, request=request)
