from collections import deque

from pyinjective.proto.cosmos.authz.v1beta1 import query_pb2 as authz_query, query_pb2_grpc as authz_query_grpc


class ConfigurableAuthZQueryServicer(authz_query_grpc.QueryServicer):
    def __init__(self):
        super().__init__()
        self.grants_responses = deque()
        self.granter_grants_responses = deque()
        self.grantee_grants_responses = deque()

    async def Grants(self, request: authz_query.QueryGrantsRequest, context=None, metadata=None):
        return self.grants_responses.pop()

    async def GranterGrants(self, request: authz_query.QueryGranterGrantsRequest, context=None, metadata=None):
        return self.granter_grants_responses.pop()

    async def GranteeGrants(self, request: authz_query.QueryGranteeGrantsRequest, context=None, metadata=None):
        return self.grantee_grants_responses.pop()
