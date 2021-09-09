# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from cosmos.feegrant.v1beta1 import tx_pb2 as cosmos_dot_feegrant_dot_v1beta1_dot_tx__pb2


class MsgStub(object):
    """Msg defines the feegrant msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GrantAllowance = channel.unary_unary(
                '/cosmos.feegrant.v1beta1.Msg/GrantAllowance',
                request_serializer=cosmos_dot_feegrant_dot_v1beta1_dot_tx__pb2.MsgGrantAllowance.SerializeToString,
                response_deserializer=cosmos_dot_feegrant_dot_v1beta1_dot_tx__pb2.MsgGrantAllowanceResponse.FromString,
                )
        self.RevokeAllowance = channel.unary_unary(
                '/cosmos.feegrant.v1beta1.Msg/RevokeAllowance',
                request_serializer=cosmos_dot_feegrant_dot_v1beta1_dot_tx__pb2.MsgRevokeAllowance.SerializeToString,
                response_deserializer=cosmos_dot_feegrant_dot_v1beta1_dot_tx__pb2.MsgRevokeAllowanceResponse.FromString,
                )


class MsgServicer(object):
    """Msg defines the feegrant msg service.
    """

    def GrantAllowance(self, request, context):
        """GrantAllowance grants fee allowance to the grantee on the granter's
        account with the provided expiration time.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RevokeAllowance(self, request, context):
        """RevokeAllowance revokes any fee allowance of granter's account that
        has been granted to the grantee.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GrantAllowance': grpc.unary_unary_rpc_method_handler(
                    servicer.GrantAllowance,
                    request_deserializer=cosmos_dot_feegrant_dot_v1beta1_dot_tx__pb2.MsgGrantAllowance.FromString,
                    response_serializer=cosmos_dot_feegrant_dot_v1beta1_dot_tx__pb2.MsgGrantAllowanceResponse.SerializeToString,
            ),
            'RevokeAllowance': grpc.unary_unary_rpc_method_handler(
                    servicer.RevokeAllowance,
                    request_deserializer=cosmos_dot_feegrant_dot_v1beta1_dot_tx__pb2.MsgRevokeAllowance.FromString,
                    response_serializer=cosmos_dot_feegrant_dot_v1beta1_dot_tx__pb2.MsgRevokeAllowanceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cosmos.feegrant.v1beta1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the feegrant msg service.
    """

    @staticmethod
    def GrantAllowance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.feegrant.v1beta1.Msg/GrantAllowance',
            cosmos_dot_feegrant_dot_v1beta1_dot_tx__pb2.MsgGrantAllowance.SerializeToString,
            cosmos_dot_feegrant_dot_v1beta1_dot_tx__pb2.MsgGrantAllowanceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RevokeAllowance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.feegrant.v1beta1.Msg/RevokeAllowance',
            cosmos_dot_feegrant_dot_v1beta1_dot_tx__pb2.MsgRevokeAllowance.SerializeToString,
            cosmos_dot_feegrant_dot_v1beta1_dot_tx__pb2.MsgRevokeAllowanceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
