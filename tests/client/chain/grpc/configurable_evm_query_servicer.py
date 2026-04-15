from collections import deque

from pyinjective.proto.injective.evm.v1 import query_pb2 as evm_query_pb, query_pb2_grpc as evm_query_grpc


class ConfigurableEVMQueryServicer(evm_query_grpc.QueryServicer):
    def __init__(self):
        super().__init__()
        self.params_responses = deque()
        self.account_responses = deque()
        self.cosmos_account_responses = deque()
        self.validator_account_responses = deque()
        self.balance_responses = deque()
        self.storage_responses = deque()
        self.code_responses = deque()
        self.base_fee_responses = deque()

    async def Params(self, request: evm_query_pb.QueryParamsRequest, context=None, metadata=None):
        return self.params_responses.pop()

    async def Account(self, request: evm_query_pb.QueryAccountRequest, context=None, metadata=None):
        return self.account_responses.pop()

    async def CosmosAccount(self, request: evm_query_pb.QueryCosmosAccountRequest, context=None, metadata=None):
        return self.cosmos_account_responses.pop()

    async def ValidatorAccount(self, request: evm_query_pb.QueryValidatorAccountRequest, context=None, metadata=None):
        return self.validator_account_responses.pop()

    async def Balance(self, request: evm_query_pb.QueryBalanceRequest, context=None, metadata=None):
        return self.balance_responses.pop()

    async def Storage(self, request: evm_query_pb.QueryStorageRequest, context=None, metadata=None):
        return self.storage_responses.pop()

    async def Code(self, request: evm_query_pb.QueryCodeRequest, context=None, metadata=None):
        return self.code_responses.pop()

    async def BaseFee(self, request: evm_query_pb.QueryBaseFeeRequest, context=None, metadata=None):
        return self.base_fee_responses.pop()
