from collections import deque

from pyinjective.proto.ibc.applications.transfer.v1 import (
    query_pb2 as ibc_transfer_query,
    query_pb2_grpc as ibc_transfer_query_grpc,
)


class ConfigurableIBCTransferQueryServicer(ibc_transfer_query_grpc.QueryServicer):
    def __init__(self):
        super().__init__()
        self.denom_trace_responses = deque()
        self.denom_traces_responses = deque()
        self.params_responses = deque()
        self.denom_hash_responses = deque()
        self.escrow_address_responses = deque()
        self.total_escrow_for_denom_responses = deque()

    async def DenomTrace(self, request: ibc_transfer_query.QueryDenomTraceRequest, context=None, metadata=None):
        return self.denom_trace_responses.pop()

    async def DenomTraces(self, request: ibc_transfer_query.QueryDenomTracesRequest, context=None, metadata=None):
        return self.denom_traces_responses.pop()

    async def Params(self, request: ibc_transfer_query.QueryParamsRequest, context=None, metadata=None):
        return self.params_responses.pop()

    async def DenomHash(self, request: ibc_transfer_query.QueryDenomHashRequest, context=None, metadata=None):
        return self.denom_hash_responses.pop()

    async def EscrowAddress(self, request: ibc_transfer_query.QueryEscrowAddressRequest, context=None, metadata=None):
        return self.escrow_address_responses.pop()

    async def TotalEscrowForDenom(
        self, request: ibc_transfer_query.QueryTotalEscrowForDenomRequest, context=None, metadata=None
    ):
        return self.total_escrow_for_denom_responses.pop()
