# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from pyinjective.proto.injective.permissions.v1beta1 import query_pb2 as injective_dot_permissions_dot_v1beta1_dot_query__pb2


class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Params = channel.unary_unary(
                '/injective.permissions.v1beta1.Query/Params',
                request_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString,
                response_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString,
                _registered_method=True)
        self.NamespaceDenoms = channel.unary_unary(
                '/injective.permissions.v1beta1.Query/NamespaceDenoms',
                request_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryNamespaceDenomsRequest.SerializeToString,
                response_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryNamespaceDenomsResponse.FromString,
                _registered_method=True)
        self.Namespaces = channel.unary_unary(
                '/injective.permissions.v1beta1.Query/Namespaces',
                request_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryNamespacesRequest.SerializeToString,
                response_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryNamespacesResponse.FromString,
                _registered_method=True)
        self.Namespace = channel.unary_unary(
                '/injective.permissions.v1beta1.Query/Namespace',
                request_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryNamespaceRequest.SerializeToString,
                response_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryNamespaceResponse.FromString,
                _registered_method=True)
        self.RolesByActor = channel.unary_unary(
                '/injective.permissions.v1beta1.Query/RolesByActor',
                request_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryRolesByActorRequest.SerializeToString,
                response_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryRolesByActorResponse.FromString,
                _registered_method=True)
        self.ActorsByRole = channel.unary_unary(
                '/injective.permissions.v1beta1.Query/ActorsByRole',
                request_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryActorsByRoleRequest.SerializeToString,
                response_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryActorsByRoleResponse.FromString,
                _registered_method=True)
        self.RoleManagers = channel.unary_unary(
                '/injective.permissions.v1beta1.Query/RoleManagers',
                request_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryRoleManagersRequest.SerializeToString,
                response_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryRoleManagersResponse.FromString,
                _registered_method=True)
        self.RoleManager = channel.unary_unary(
                '/injective.permissions.v1beta1.Query/RoleManager',
                request_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryRoleManagerRequest.SerializeToString,
                response_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryRoleManagerResponse.FromString,
                _registered_method=True)
        self.PolicyStatuses = channel.unary_unary(
                '/injective.permissions.v1beta1.Query/PolicyStatuses',
                request_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryPolicyStatusesRequest.SerializeToString,
                response_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryPolicyStatusesResponse.FromString,
                _registered_method=True)
        self.PolicyManagerCapabilities = channel.unary_unary(
                '/injective.permissions.v1beta1.Query/PolicyManagerCapabilities',
                request_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryPolicyManagerCapabilitiesRequest.SerializeToString,
                response_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryPolicyManagerCapabilitiesResponse.FromString,
                _registered_method=True)
        self.Vouchers = channel.unary_unary(
                '/injective.permissions.v1beta1.Query/Vouchers',
                request_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryVouchersRequest.SerializeToString,
                response_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryVouchersResponse.FromString,
                _registered_method=True)
        self.Voucher = channel.unary_unary(
                '/injective.permissions.v1beta1.Query/Voucher',
                request_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryVoucherRequest.SerializeToString,
                response_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryVoucherResponse.FromString,
                _registered_method=True)
        self.PermissionsModuleState = channel.unary_unary(
                '/injective.permissions.v1beta1.Query/PermissionsModuleState',
                request_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryModuleStateRequest.SerializeToString,
                response_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryModuleStateResponse.FromString,
                _registered_method=True)


class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def Params(self, request, context):
        """Params defines a gRPC query method that returns the permissions module's
        parameters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NamespaceDenoms(self, request, context):
        """NamespaceDenoms defines a gRPC query method that returns the denoms for which a namespace exists
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Namespaces(self, request, context):
        """Namespaces defines a gRPC query method that returns the permissions
        module's created namespaces.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Namespace(self, request, context):
        """Namespace defines a gRPC query method that returns the permissions
        module's namespace associated with the provided denom.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RolesByActor(self, request, context):
        """RolesByActor defines a gRPC query method that returns roles for the actor in the namespace
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ActorsByRole(self, request, context):
        """ActorsByRole defines a gRPC query method that returns a namespace's roles associated with the provided actor.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RoleManagers(self, request, context):
        """RoleManagers defines a gRPC query method that returns a namespace's role managers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RoleManager(self, request, context):
        """RoleManager defines a gRPC query method that returns the roles a given role manager manages for a given namespace
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PolicyStatuses(self, request, context):
        """PolicyStatuses defines a gRPC query method that returns a namespace's policy statuses
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PolicyManagerCapabilities(self, request, context):
        """PolicyManagerCapabilities defines a gRPC query method that returns a namespace's policy manager capabilities
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Vouchers(self, request, context):
        """Vouchers defines a gRPC query method for the vouchers for a given denom
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Voucher(self, request, context):
        """Voucher defines a gRPC query method for the vouchers for a given denom and address
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PermissionsModuleState(self, request, context):
        """Retrieves the entire permissions module's state
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Params': grpc.unary_unary_rpc_method_handler(
                    servicer.Params,
                    request_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryParamsRequest.FromString,
                    response_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryParamsResponse.SerializeToString,
            ),
            'NamespaceDenoms': grpc.unary_unary_rpc_method_handler(
                    servicer.NamespaceDenoms,
                    request_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryNamespaceDenomsRequest.FromString,
                    response_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryNamespaceDenomsResponse.SerializeToString,
            ),
            'Namespaces': grpc.unary_unary_rpc_method_handler(
                    servicer.Namespaces,
                    request_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryNamespacesRequest.FromString,
                    response_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryNamespacesResponse.SerializeToString,
            ),
            'Namespace': grpc.unary_unary_rpc_method_handler(
                    servicer.Namespace,
                    request_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryNamespaceRequest.FromString,
                    response_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryNamespaceResponse.SerializeToString,
            ),
            'RolesByActor': grpc.unary_unary_rpc_method_handler(
                    servicer.RolesByActor,
                    request_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryRolesByActorRequest.FromString,
                    response_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryRolesByActorResponse.SerializeToString,
            ),
            'ActorsByRole': grpc.unary_unary_rpc_method_handler(
                    servicer.ActorsByRole,
                    request_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryActorsByRoleRequest.FromString,
                    response_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryActorsByRoleResponse.SerializeToString,
            ),
            'RoleManagers': grpc.unary_unary_rpc_method_handler(
                    servicer.RoleManagers,
                    request_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryRoleManagersRequest.FromString,
                    response_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryRoleManagersResponse.SerializeToString,
            ),
            'RoleManager': grpc.unary_unary_rpc_method_handler(
                    servicer.RoleManager,
                    request_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryRoleManagerRequest.FromString,
                    response_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryRoleManagerResponse.SerializeToString,
            ),
            'PolicyStatuses': grpc.unary_unary_rpc_method_handler(
                    servicer.PolicyStatuses,
                    request_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryPolicyStatusesRequest.FromString,
                    response_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryPolicyStatusesResponse.SerializeToString,
            ),
            'PolicyManagerCapabilities': grpc.unary_unary_rpc_method_handler(
                    servicer.PolicyManagerCapabilities,
                    request_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryPolicyManagerCapabilitiesRequest.FromString,
                    response_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryPolicyManagerCapabilitiesResponse.SerializeToString,
            ),
            'Vouchers': grpc.unary_unary_rpc_method_handler(
                    servicer.Vouchers,
                    request_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryVouchersRequest.FromString,
                    response_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryVouchersResponse.SerializeToString,
            ),
            'Voucher': grpc.unary_unary_rpc_method_handler(
                    servicer.Voucher,
                    request_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryVoucherRequest.FromString,
                    response_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryVoucherResponse.SerializeToString,
            ),
            'PermissionsModuleState': grpc.unary_unary_rpc_method_handler(
                    servicer.PermissionsModuleState,
                    request_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryModuleStateRequest.FromString,
                    response_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryModuleStateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective.permissions.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('injective.permissions.v1beta1.Query', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def Params(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective.permissions.v1beta1.Query/Params',
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString,
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def NamespaceDenoms(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective.permissions.v1beta1.Query/NamespaceDenoms',
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryNamespaceDenomsRequest.SerializeToString,
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryNamespaceDenomsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Namespaces(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective.permissions.v1beta1.Query/Namespaces',
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryNamespacesRequest.SerializeToString,
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryNamespacesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Namespace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective.permissions.v1beta1.Query/Namespace',
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryNamespaceRequest.SerializeToString,
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryNamespaceResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RolesByActor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective.permissions.v1beta1.Query/RolesByActor',
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryRolesByActorRequest.SerializeToString,
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryRolesByActorResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ActorsByRole(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective.permissions.v1beta1.Query/ActorsByRole',
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryActorsByRoleRequest.SerializeToString,
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryActorsByRoleResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RoleManagers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective.permissions.v1beta1.Query/RoleManagers',
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryRoleManagersRequest.SerializeToString,
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryRoleManagersResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RoleManager(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective.permissions.v1beta1.Query/RoleManager',
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryRoleManagerRequest.SerializeToString,
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryRoleManagerResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PolicyStatuses(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective.permissions.v1beta1.Query/PolicyStatuses',
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryPolicyStatusesRequest.SerializeToString,
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryPolicyStatusesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PolicyManagerCapabilities(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective.permissions.v1beta1.Query/PolicyManagerCapabilities',
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryPolicyManagerCapabilitiesRequest.SerializeToString,
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryPolicyManagerCapabilitiesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Vouchers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective.permissions.v1beta1.Query/Vouchers',
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryVouchersRequest.SerializeToString,
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryVouchersResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Voucher(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective.permissions.v1beta1.Query/Voucher',
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryVoucherRequest.SerializeToString,
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryVoucherResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PermissionsModuleState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective.permissions.v1beta1.Query/PermissionsModuleState',
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryModuleStateRequest.SerializeToString,
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryModuleStateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
