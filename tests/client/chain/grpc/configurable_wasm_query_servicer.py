from collections import deque

from pyinjective.proto.cosmwasm.wasm.v1 import query_pb2 as wasm_query_pb, query_pb2_grpc as wasm_query_grpc


class ConfigurableWasmQueryServicer(wasm_query_grpc.QueryServicer):
    def __init__(self):
        super().__init__()
        self.params_responses = deque()
        self.contract_info_responses = deque()
        self.contract_history_responses = deque()
        self.contracts_by_code_responses = deque()
        self.all_contracts_state_responses = deque()
        self.raw_contract_state_responses = deque()
        self.smart_contract_state_responses = deque()
        self.code_responses = deque()
        self.codes_responses = deque()
        self.pinned_codes_responses = deque()
        self.contracts_by_creator_responses = deque()

    async def Params(self, request: wasm_query_pb.QueryParamsRequest, context=None, metadata=None):
        return self.params_responses.pop()

    async def ContractInfo(self, request: wasm_query_pb.QueryContractInfoRequest, context=None, metadata=None):
        return self.contract_info_responses.pop()

    async def ContractHistory(self, request: wasm_query_pb.QueryContractHistoryRequest, context=None, metadata=None):
        return self.contract_history_responses.pop()

    async def ContractsByCode(self, request: wasm_query_pb.QueryContractsByCodeRequest, context=None, metadata=None):
        return self.contracts_by_code_responses.pop()

    async def AllContractState(self, request: wasm_query_pb.QueryAllContractStateRequest, context=None, metadata=None):
        return self.all_contracts_state_responses.pop()

    async def RawContractState(self, request: wasm_query_pb.QueryRawContractStateRequest, context=None, metadata=None):
        return self.raw_contract_state_responses.pop()

    async def SmartContractState(
        self, request: wasm_query_pb.QuerySmartContractStateRequest, context=None, metadata=None
    ):
        return self.smart_contract_state_responses.pop()

    async def Code(self, request: wasm_query_pb.QueryCodeRequest, context=None, metadata=None):
        return self.code_responses.pop()

    async def Codes(self, request: wasm_query_pb.QueryCodesRequest, context=None, metadata=None):
        return self.codes_responses.pop()

    async def PinnedCodes(self, request: wasm_query_pb.QueryPinnedCodesRequest, context=None, metadata=None):
        return self.pinned_codes_responses.pop()

    async def ContractsByCreator(
        self, request: wasm_query_pb.QueryContractsByCreatorRequest, context=None, metadata=None
    ):
        return self.contracts_by_creator_responses.pop()
