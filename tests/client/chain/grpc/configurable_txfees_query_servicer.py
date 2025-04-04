from collections import deque

from pyinjective.proto.injective.txfees.v1beta1 import query_pb2 as txfees_query_pb, query_pb2_grpc as txfees_query_grpc


class ConfigurableTxfeesQueryServicer(txfees_query_grpc.QueryServicer):
    def __init__(self):
        super().__init__()
        self.params_responses = deque()
        self.eip_base_fee_responses = deque()

    async def Params(self, request: txfees_query_pb.QueryParamsRequest, context=None, metadata=None):
        return self.params_responses.pop()

    async def GetEipBaseFee(self, request: txfees_query_pb.QueryEipBaseFeeRequest, context=None, metadata=None):
        return self.eip_base_fee_responses.pop()
