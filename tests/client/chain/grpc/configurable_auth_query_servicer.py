from collections import deque

from pyinjective.proto.cosmos.auth.v1beta1 import query_pb2 as auth_query_pb, query_pb2_grpc as auth_query_grpc


class ConfigurableAuthQueryServicer(auth_query_grpc.QueryServicer):
    def __init__(self):
        super().__init__()
        self.auth_params = deque()
        self.account_responses = deque()
        self.accounts_responses = deque()

    async def Params(self, request: auth_query_pb.QueryParamsRequest, context=None, metadata=None):
        return self.auth_params.pop()

    async def Account(self, request: auth_query_pb.QueryAccountRequest, context=None, metadata=None):
        return self.account_responses.pop()

    async def Accounts(self, request: auth_query_pb.QueryAccountsRequest, context=None, metadata=None):
        return self.accounts_responses.pop()
