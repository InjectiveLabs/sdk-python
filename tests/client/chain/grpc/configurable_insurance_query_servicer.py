from collections import deque

from pyinjective.proto.injective.insurance.v1beta1 import (
    query_pb2 as insurance_query_pb,
    query_pb2_grpc as insurance_query_grpc,
)


class ConfigurableInsuranceQueryServicer(insurance_query_grpc.QueryServicer):
    def __init__(self):
        super().__init__()
        self.insurance_params = deque()
        self.insurance_fund_responses = deque()
        self.insurance_funds_responses = deque()
        self.estimated_redemptions_responses = deque()
        self.pending_redemptions_responses = deque()
        self.module_states = deque()
        self.failed_redemptions_responses = deque()
        self.vouchers_responses = deque()
        self.voucher_responses = deque()

    async def InsuranceParams(
        self, request: insurance_query_pb.QueryInsuranceParamsRequest, context=None, metadata=None
    ):
        return self.insurance_params.pop()

    async def InsuranceFund(
        self, request: insurance_query_pb.QueryInsuranceFundRequest, context=None, metadata=None
    ):
        return self.insurance_fund_responses.pop()

    async def InsuranceFunds(
        self, request: insurance_query_pb.QueryInsuranceFundsRequest, context=None, metadata=None
    ):
        return self.insurance_funds_responses.pop()

    async def EstimatedRedemptions(
        self, request: insurance_query_pb.QueryEstimatedRedemptionsRequest, context=None, metadata=None
    ):
        return self.estimated_redemptions_responses.pop()

    async def PendingRedemptions(
        self, request: insurance_query_pb.QueryPendingRedemptionsRequest, context=None, metadata=None
    ):
        return self.pending_redemptions_responses.pop()

    async def InsuranceModuleState(
        self, request: insurance_query_pb.QueryModuleStateRequest, context=None, metadata=None
    ):
        return self.module_states.pop()

    async def FailedRedemptions(
        self, request: insurance_query_pb.QueryFailedRedemptionsRequest, context=None, metadata=None
    ):
        return self.failed_redemptions_responses.pop()

    async def Vouchers(self, request: insurance_query_pb.QueryVouchersRequest, context=None, metadata=None):
        return self.vouchers_responses.pop()

    async def Voucher(self, request: insurance_query_pb.QueryVoucherRequest, context=None, metadata=None):
        return self.voucher_responses.pop()
