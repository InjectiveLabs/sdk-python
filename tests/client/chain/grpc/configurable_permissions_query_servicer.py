from collections import deque

from pyinjective.proto.injective.permissions.v1beta1 import (
    query_pb2 as permissions_query_pb,
    query_pb2_grpc as permissions_query_grpc,
)


class ConfigurablePermissionsQueryServicer(permissions_query_grpc.QueryServicer):
    def __init__(self):
        super().__init__()
        self.permissions_params = deque()
        self.all_namespaces_responses = deque()
        self.namespace_by_denom_responses = deque()
        self.address_roles_responses = deque()
        self.addresses_by_role_responses = deque()
        self.vouchers_for_address_responses = deque()

    async def Params(self, request: permissions_query_pb.QueryParamsRequest, context=None, metadata=None):
        return self.permissions_params.pop()

    async def AllNamespaces(self, request: permissions_query_pb.QueryAllNamespacesRequest, context=None, metadata=None):
        return self.all_namespaces_responses.pop()

    async def NamespaceByDenom(
        self, request: permissions_query_pb.QueryNamespaceByDenomRequest, context=None, metadata=None
    ):
        return self.namespace_by_denom_responses.pop()

    async def AddressRoles(self, request: permissions_query_pb.QueryAddressRolesRequest, context=None, metadata=None):
        return self.address_roles_responses.pop()

    async def AddressesByRole(
        self, request: permissions_query_pb.QueryAddressesByRoleRequest, context=None, metadata=None
    ):
        return self.addresses_by_role_responses.pop()

    async def VouchersForAddress(
        self, request: permissions_query_pb.QueryVouchersForAddressRequest, context=None, metadata=None
    ):
        return self.vouchers_for_address_responses.pop()
