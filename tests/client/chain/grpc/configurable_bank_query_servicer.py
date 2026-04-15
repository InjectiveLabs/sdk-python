from collections import deque

from pyinjective.proto.cosmos.bank.v1beta1 import query_pb2 as bank_query_pb, query_pb2_grpc as bank_query_grpc


class ConfigurableBankQueryServicer(bank_query_grpc.QueryServicer):
    def __init__(self):
        super().__init__()
        self.bank_params = deque()
        self.balance_responses = deque()
        self.balances_responses = deque()
        self.spendable_balances_responses = deque()
        self.spendable_balances_by_denom_responses = deque()
        self.total_supply_responses = deque()
        self.supply_of_responses = deque()
        self.denom_metadata_responses = deque()
        self.denoms_metadata_responses = deque()
        self.denom_owners_responses = deque()
        self.send_enabled_responses = deque()

    async def Params(self, request: bank_query_pb.QueryParamsRequest, context=None, metadata=None):
        return self.bank_params.pop()

    async def Balance(self, request: bank_query_pb.QueryBalanceRequest, context=None, metadata=None):
        return self.balance_responses.pop()

    async def AllBalances(self, request: bank_query_pb.QueryAllBalancesRequest, context=None, metadata=None):
        return self.balances_responses.pop()

    async def SpendableBalances(
        self, request: bank_query_pb.QuerySpendableBalancesRequest, context=None, metadata=None
    ):
        return self.spendable_balances_responses.pop()

    async def SpendableBalanceByDenom(
        self, request: bank_query_pb.QuerySpendableBalanceByDenomRequest, context=None, metadata=None
    ):
        return self.spendable_balances_by_denom_responses.pop()

    async def TotalSupply(self, request: bank_query_pb.QueryTotalSupplyRequest, context=None, metadata=None):
        return self.total_supply_responses.pop()

    async def SupplyOf(self, request: bank_query_pb.QuerySupplyOfRequest, context=None, metadata=None):
        return self.supply_of_responses.pop()

    async def DenomMetadata(self, request: bank_query_pb.QueryDenomMetadataRequest, context=None, metadata=None):
        return self.denom_metadata_responses.pop()

    async def DenomsMetadata(self, request: bank_query_pb.QueryDenomsMetadataRequest, context=None, metadata=None):
        return self.denoms_metadata_responses.pop()

    async def DenomOwners(self, request: bank_query_pb.QueryDenomOwnersRequest, context=None, metadata=None):
        return self.denom_owners_responses.pop()

    async def SendEnabled(self, request: bank_query_pb.QuerySendEnabledRequest, context=None, metadata=None):
        return self.send_enabled_responses.pop()
