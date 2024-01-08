from collections import deque

from pyinjective.proto.exchange import (
    injective_insurance_rpc_pb2 as exchange_insurance_pb,
    injective_insurance_rpc_pb2_grpc as exchange_insurance_grpc,
)


class ConfigurableInsuranceQueryServicer(exchange_insurance_grpc.InjectiveInsuranceRPCServicer):
    def __init__(self):
        super().__init__()
        self.funds_responses = deque()
        self.redemptions_responses = deque()

    async def Funds(self, request: exchange_insurance_pb.FundsRequest, context=None, metadata=None):
        return self.funds_responses.pop()

    async def Redemptions(self, request: exchange_insurance_pb.RedemptionsRequest, context=None, metadata=None):
        return self.redemptions_responses.pop()
