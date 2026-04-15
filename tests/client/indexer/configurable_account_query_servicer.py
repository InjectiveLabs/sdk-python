from collections import deque

from pyinjective.proto.exchange import (
    injective_accounts_rpc_pb2 as exchange_accounts_pb,
    injective_accounts_rpc_pb2_grpc as exchange_accounts_grpc,
)


class ConfigurableAccountQueryServicer(exchange_accounts_grpc.InjectiveAccountsRPCServicer):
    def __init__(self):
        super().__init__()
        self.portfolio_responses = deque()
        self.order_states_responses = deque()
        self.subaccounts_list_responses = deque()
        self.subaccount_balances_list_responses = deque()
        self.subaccount_balance_responses = deque()
        self.subaccount_history_responses = deque()
        self.subaccount_order_summary_responses = deque()
        self.rewards_responses = deque()
        self.stream_subaccount_balance_responses = deque()

    async def Portfolio(self, request: exchange_accounts_pb.PortfolioRequest, context=None, metadata=None):
        return self.portfolio_responses.pop()

    async def OrderStates(self, request: exchange_accounts_pb.OrderStatesRequest, context=None, metadata=None):
        return self.order_states_responses.pop()

    async def SubaccountsList(self, request: exchange_accounts_pb.SubaccountsListRequest, context=None, metadata=None):
        return self.subaccounts_list_responses.pop()

    async def SubaccountBalancesList(
        self, request: exchange_accounts_pb.SubaccountBalancesListRequest, context=None, metadata=None
    ):
        return self.subaccount_balances_list_responses.pop()

    async def SubaccountBalanceEndpoint(
        self, request: exchange_accounts_pb.SubaccountBalanceEndpointRequest, context=None, metadata=None
    ):
        return self.subaccount_balance_responses.pop()

    async def SubaccountHistory(
        self, request: exchange_accounts_pb.SubaccountHistoryRequest, context=None, metadata=None
    ):
        return self.subaccount_history_responses.pop()

    async def SubaccountOrderSummary(
        self, request: exchange_accounts_pb.SubaccountOrderSummaryRequest, context=None, metadata=None
    ):
        return self.subaccount_order_summary_responses.pop()

    async def Rewards(self, request: exchange_accounts_pb.RewardsRequest, context=None, metadata=None):
        return self.rewards_responses.pop()

    async def StreamSubaccountBalance(
        self, request: exchange_accounts_pb.SubaccountOrderSummaryRequest, context=None, metadata=None
    ):
        for event in self.stream_subaccount_balance_responses:
            yield event
