# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from pyinjective.proto.ibc.applications.interchain_accounts.host.v1 import tx_pb2 as ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_tx__pb2


class MsgStub(object):
    """Msg defines the 27-interchain-accounts/host Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UpdateParams = channel.unary_unary(
                '/ibc.applications.interchain_accounts.host.v1.Msg/UpdateParams',
                request_serializer=ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_tx__pb2.MsgUpdateParams.SerializeToString,
                response_deserializer=ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_tx__pb2.MsgUpdateParamsResponse.FromString,
                _registered_method=True)
        self.ModuleQuerySafe = channel.unary_unary(
                '/ibc.applications.interchain_accounts.host.v1.Msg/ModuleQuerySafe',
                request_serializer=ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_tx__pb2.MsgModuleQuerySafe.SerializeToString,
                response_deserializer=ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_tx__pb2.MsgModuleQuerySafeResponse.FromString,
                _registered_method=True)


class MsgServicer(object):
    """Msg defines the 27-interchain-accounts/host Msg service.
    """

    def UpdateParams(self, request, context):
        """UpdateParams defines a rpc handler for MsgUpdateParams.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ModuleQuerySafe(self, request, context):
        """ModuleQuerySafe defines a rpc handler for MsgModuleQuerySafe.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UpdateParams': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateParams,
                    request_deserializer=ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_tx__pb2.MsgUpdateParams.FromString,
                    response_serializer=ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_tx__pb2.MsgUpdateParamsResponse.SerializeToString,
            ),
            'ModuleQuerySafe': grpc.unary_unary_rpc_method_handler(
                    servicer.ModuleQuerySafe,
                    request_deserializer=ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_tx__pb2.MsgModuleQuerySafe.FromString,
                    response_serializer=ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_tx__pb2.MsgModuleQuerySafeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ibc.applications.interchain_accounts.host.v1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ibc.applications.interchain_accounts.host.v1.Msg', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the 27-interchain-accounts/host Msg service.
    """

    @staticmethod
    def UpdateParams(request,
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
            '/ibc.applications.interchain_accounts.host.v1.Msg/UpdateParams',
            ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_tx__pb2.MsgUpdateParams.SerializeToString,
            ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_tx__pb2.MsgUpdateParamsResponse.FromString,
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
    def ModuleQuerySafe(request,
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
            '/ibc.applications.interchain_accounts.host.v1.Msg/ModuleQuerySafe',
            ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_tx__pb2.MsgModuleQuerySafe.SerializeToString,
            ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_tx__pb2.MsgModuleQuerySafeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
