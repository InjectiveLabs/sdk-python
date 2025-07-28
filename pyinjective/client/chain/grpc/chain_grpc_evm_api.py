from typing import Any, Callable, Dict, Optional

from grpc.aio import Channel

from pyinjective.core.network import CookieAssistant
from pyinjective.proto.injective.evm.v1 import query_pb2 as evm_query_pb, query_pb2_grpc as evm_query_grpc
from pyinjective.utils.grpc_api_request_assistant import GrpcApiRequestAssistant


class ChainGrpcEVMApi:
    def __init__(self, channel: Channel, cookie_assistant: CookieAssistant):
        self._stub = evm_query_grpc.QueryStub(channel)
        self._assistant = GrpcApiRequestAssistant(cookie_assistant=cookie_assistant)

    async def fetch_params(self) -> Dict[str, Any]:
        request = evm_query_pb.QueryParamsRequest()
        response = await self._execute_call(call=self._stub.Params, request=request)

        return response

    async def fetch_account(self, address: str) -> Dict[str, Any]:
        request = evm_query_pb.QueryAccountRequest(address=address)
        response = await self._execute_call(call=self._stub.Account, request=request)

        return response

    async def fetch_cosmos_account(self, address: str) -> Dict[str, Any]:
        request = evm_query_pb.QueryCosmosAccountRequest(address=address)
        response = await self._execute_call(call=self._stub.CosmosAccount, request=request)

        return response

    async def fetch_validator_account(self, cons_address: str) -> Dict[str, Any]:
        request = evm_query_pb.QueryValidatorAccountRequest(cons_address=cons_address)
        response = await self._execute_call(call=self._stub.ValidatorAccount, request=request)

        return response

    async def fetch_balance(self, address: str) -> Dict[str, Any]:
        request = evm_query_pb.QueryBalanceRequest(address=address)
        response = await self._execute_call(call=self._stub.Balance, request=request)

        return response

    async def fetch_storage(self, address: str, key: Optional[str] = None) -> Dict[str, Any]:
        request = evm_query_pb.QueryStorageRequest(address=address, key=key)
        response = await self._execute_call(call=self._stub.Storage, request=request)

        return response

    async def fetch_code(self, address: str) -> Dict[str, Any]:
        request = evm_query_pb.QueryCodeRequest(address=address)
        response = await self._execute_call(call=self._stub.Code, request=request)

        return response

    async def fetch_base_fee(self) -> Dict[str, Any]:
        request = evm_query_pb.QueryBaseFeeRequest()
        response = await self._execute_call(call=self._stub.BaseFee, request=request)

        return response

    async def _execute_call(self, call: Callable, request) -> Dict[str, Any]:
        return await self._assistant.execute_call(call=call, request=request)
