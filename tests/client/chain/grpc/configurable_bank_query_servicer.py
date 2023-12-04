from collections import deque

from pyinjective.proto.cosmos.bank.v1beta1 import query_pb2 as bank_query_pb, query_pb2_grpc as bank_query_grpc


class ConfigurableBankQueryServicer(bank_query_grpc.QueryServicer):
    def __init__(self):
        super().__init__()
        self.bank_params = deque()
        self.balance_responses = deque()
        self.balances_responses = deque()
        self.total_supply_responses = deque()

    async def Params(self, request: bank_query_pb.QueryParamsRequest, context=None, metadata=None):
        return self.bank_params.pop()

    async def Balance(self, request: bank_query_pb.QueryBalanceRequest, context=None, metadata=None):
        return self.balance_responses.pop()

    async def AllBalances(self, request: bank_query_pb.QueryAllBalancesRequest, context=None, metadata=None):
        return self.balances_responses.pop()

    async def TotalSupply(self, request: bank_query_pb.QueryTotalSupplyRequest, context=None, metadata=None):
        return self.total_supply_responses.pop()
