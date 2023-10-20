from typing import Any, Callable, Coroutine, Dict

from grpc.aio import Channel

from pyinjective.proto.cosmos.bank.v1beta1 import query_pb2 as bank_query_pb, query_pb2_grpc as bank_query_grpc
from pyinjective.utils.grpc_api_request_assistant import GrpcApiRequestAssistant


class ChainGrpcBankApi:
    def __init__(self, channel: Channel, metadata_provider: Coroutine):
        self._stub = bank_query_grpc.QueryStub(channel)
        self._assistant = GrpcApiRequestAssistant(metadata_provider=metadata_provider)

    async def fetch_module_params(self) -> Dict[str, Any]:
        request = bank_query_pb.QueryParamsRequest()
        response = await self._execute_call(call=self._stub.Params, request=request)

        return response

    async def fetch_balance(self, account_address: str, denom: str) -> Dict[str, Any]:
        request = bank_query_pb.QueryBalanceRequest(address=account_address, denom=denom)
        response = await self._execute_call(call=self._stub.Balance, request=request)

        return response

    async def fetch_balances(self, account_address: str) -> Dict[str, Any]:
        request = bank_query_pb.QueryAllBalancesRequest(address=account_address)
        response = await self._execute_call(call=self._stub.AllBalances, request=request)

        return response

    async def fetch_total_supply(self) -> Dict[str, Any]:
        request = bank_query_pb.QueryTotalSupplyRequest()
        response = await self._execute_call(call=self._stub.TotalSupply, request=request)

        return response

    async def _execute_call(self, call: Callable, request) -> Dict[str, Any]:
        return await self._assistant.execute_call(call=call, request=request)
