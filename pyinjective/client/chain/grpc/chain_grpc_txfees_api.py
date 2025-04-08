from typing import Any, Callable, Dict

from grpc.aio import Channel

from pyinjective.core.network import CookieAssistant
from pyinjective.proto.injective.txfees.v1beta1 import query_pb2 as txfees_query_pb, query_pb2_grpc as txfees_query_grpc
from pyinjective.utils.grpc_api_request_assistant import GrpcApiRequestAssistant


class ChainGrpcTxfeesApi:
    def __init__(self, channel: Channel, cookie_assistant: CookieAssistant):
        self._query_stub = txfees_query_grpc.QueryStub(channel)
        self._assistant = GrpcApiRequestAssistant(cookie_assistant=cookie_assistant)

    async def fetch_module_params(self) -> Dict[str, Any]:
        request = txfees_query_pb.QueryParamsRequest()
        response = await self._execute_call(call=self._query_stub.Params, request=request)

        return response

    async def fetch_eip_base_fee(self) -> Dict[str, Any]:
        request = txfees_query_pb.QueryEipBaseFeeRequest()
        response = await self._execute_call(call=self._query_stub.GetEipBaseFee, request=request)

        return response

    async def _execute_call(self, call: Callable, request) -> Dict[str, Any]:
        return await self._assistant.execute_call(call=call, request=request)
