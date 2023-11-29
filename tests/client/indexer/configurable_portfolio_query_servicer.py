from collections import deque

from pyinjective.proto.exchange import (
    injective_portfolio_rpc_pb2 as exchange_portfolio_pb,
    injective_portfolio_rpc_pb2_grpc as exchange_portfolio_grpc,
)


class ConfigurablePortfolioQueryServicer(exchange_portfolio_grpc.InjectivePortfolioRPCServicer):
    def __init__(self):
        super().__init__()
        self.account_portfolio_responses = deque()
        self.stream_account_portfolio_responses = deque()

    async def AccountPortfolio(
        self, request: exchange_portfolio_pb.AccountPortfolioRequest, context=None, metadata=None
    ):
        return self.account_portfolio_responses.pop()

    async def StreamAccountPortfolio(
        self, request: exchange_portfolio_pb.StreamAccountPortfolioRequest, context=None, metadata=None
    ):
        for event in self.stream_account_portfolio_responses:
            yield event
