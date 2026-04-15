from collections import deque

from pyinjective.proto.injective.permissions.v1beta1 import (
    query_pb2 as permissions_query_pb,
    query_pb2_grpc as permissions_query_grpc,
)


class ConfigurablePermissionsQueryServicer(permissions_query_grpc.QueryServicer):
    def __init__(self):
        super().__init__()
        self.permissions_params = deque()
        self.namespace_denoms_responses = deque()
        self.namespaces_responses = deque()
        self.namespace_responses = deque()
        self.roles_by_actor_responses = deque()
        self.actors_by_role_responses = deque()
        self.role_managers_responses = deque()
        self.role_manager_responses = deque()
        self.policy_statuses_responses = deque()
        self.policy_manager_capabilities_responses = deque()
        self.vouchers_responses = deque()
        self.voucher_responses = deque()
        self.module_state_responses = deque()

    async def Params(self, request: permissions_query_pb.QueryParamsRequest, context=None, metadata=None):
        return self.permissions_params.pop()

    async def NamespaceDenoms(
        self, request: permissions_query_pb.QueryNamespaceDenomsRequest, context=None, metadata=None
    ):
        return self.namespace_denoms_responses.pop()

    async def Namespaces(self, request: permissions_query_pb.QueryNamespaceDenomsRequest, context=None, metadata=None):
        return self.namespaces_responses.pop()

    async def Namespace(self, request: permissions_query_pb.QueryNamespaceRequest, context=None, metadata=None):
        return self.namespace_responses.pop()

    async def RolesByActor(self, request: permissions_query_pb.QueryRolesByActorRequest, context=None, metadata=None):
        return self.roles_by_actor_responses.pop()

    async def ActorsByRole(self, request: permissions_query_pb.QueryActorsByRoleRequest, context=None, metadata=None):
        return self.actors_by_role_responses.pop()

    async def RoleManagers(self, request: permissions_query_pb.QueryRoleManagersRequest, context=None, metadata=None):
        return self.role_managers_responses.pop()

    async def RoleManager(self, request: permissions_query_pb.QueryRoleManagerRequest, context=None, metadata=None):
        return self.role_manager_responses.pop()

    async def PolicyStatuses(
        self, request: permissions_query_pb.QueryPolicyStatusesRequest, context=None, metadata=None
    ):
        return self.policy_statuses_responses.pop()

    async def PolicyManagerCapabilities(
        self, request: permissions_query_pb.QueryPolicyManagerCapabilitiesRequest, context=None, metadata=None
    ):
        return self.policy_manager_capabilities_responses.pop()

    async def Vouchers(self, request: permissions_query_pb.QueryVouchersRequest, context=None, metadata=None):
        return self.vouchers_responses.pop()

    async def Voucher(self, request: permissions_query_pb.QueryVoucherRequest, context=None, metadata=None):
        return self.voucher_responses.pop()

    async def PermissionsModuleState(
        self, request: permissions_query_pb.QueryModuleStateRequest, context=None, metadata=None
    ):
        return self.module_state_responses.pop()
