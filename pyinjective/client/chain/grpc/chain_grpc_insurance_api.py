from typing import Any, Callable, Dict

from grpc.aio import Channel

from pyinjective.core.network import CookieAssistant
from pyinjective.proto.injective.insurance.v1beta1 import (
    query_pb2 as insurance_query_pb,
    query_pb2_grpc as insurance_query_grpc,
)
from pyinjective.utils.grpc_api_request_assistant import GrpcApiRequestAssistant


class ChainGrpcInsuranceApi:
    def __init__(self, channel: Channel, cookie_assistant: CookieAssistant):
        self._stub = insurance_query_grpc.QueryStub(channel)
        self._assistant = GrpcApiRequestAssistant(cookie_assistant=cookie_assistant)

    async def fetch_module_params(self) -> Dict[str, Any]:
        request = insurance_query_pb.QueryInsuranceParamsRequest()
        response = await self._execute_call(call=self._stub.InsuranceParams, request=request)

        return response

    async def fetch_insurance_fund(self, market_id: str) -> Dict[str, Any]:
        request = insurance_query_pb.QueryInsuranceFundRequest(market_id=market_id)
        response = await self._execute_call(call=self._stub.InsuranceFund, request=request)

        return response

    async def fetch_insurance_funds(self) -> Dict[str, Any]:
        request = insurance_query_pb.QueryInsuranceFundsRequest()
        response = await self._execute_call(call=self._stub.InsuranceFunds, request=request)

        return response

    async def fetch_estimated_redemptions(self, market_id: str, address: str) -> Dict[str, Any]:
        request = insurance_query_pb.QueryEstimatedRedemptionsRequest(marketId=market_id, address=address)
        response = await self._execute_call(call=self._stub.EstimatedRedemptions, request=request)

        return response

    async def fetch_pending_redemptions(self, market_id: str, address: str) -> Dict[str, Any]:
        request = insurance_query_pb.QueryPendingRedemptionsRequest(marketId=market_id, address=address)
        response = await self._execute_call(call=self._stub.PendingRedemptions, request=request)

        return response

    async def fetch_module_state(self) -> Dict[str, Any]:
        request = insurance_query_pb.QueryModuleStateRequest()
        response = await self._execute_call(call=self._stub.InsuranceModuleState, request=request)

        return response

    async def fetch_failed_redemptions(self) -> Dict[str, Any]:
        request = insurance_query_pb.QueryFailedRedemptionsRequest()
        response = await self._execute_call(call=self._stub.FailedRedemptions, request=request)

        return response

    async def fetch_vouchers(self, denom: str) -> Dict[str, Any]:
        request = insurance_query_pb.QueryVouchersRequest(denom=denom)
        response = await self._execute_call(call=self._stub.Vouchers, request=request)

        return response

    async def fetch_voucher(self, denom: str, address: str) -> Dict[str, Any]:
        request = insurance_query_pb.QueryVoucherRequest(denom=denom, address=address)
        response = await self._execute_call(call=self._stub.Voucher, request=request)

        return response

    async def _execute_call(self, call: Callable, request) -> Dict[str, Any]:
        return await self._assistant.execute_call(call=call, request=request)
