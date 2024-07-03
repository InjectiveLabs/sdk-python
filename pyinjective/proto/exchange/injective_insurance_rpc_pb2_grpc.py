# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from pyinjective.proto.exchange import injective_insurance_rpc_pb2 as exchange_dot_injective__insurance__rpc__pb2


class InjectiveInsuranceRPCStub(object):
    """InjectiveInsuranceRPC defines gRPC API of Insurance provider.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Funds = channel.unary_unary(
                '/injective_insurance_rpc.InjectiveInsuranceRPC/Funds',
                request_serializer=exchange_dot_injective__insurance__rpc__pb2.FundsRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__insurance__rpc__pb2.FundsResponse.FromString,
                )
        self.Redemptions = channel.unary_unary(
                '/injective_insurance_rpc.InjectiveInsuranceRPC/Redemptions',
                request_serializer=exchange_dot_injective__insurance__rpc__pb2.RedemptionsRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__insurance__rpc__pb2.RedemptionsResponse.FromString,
                )


class InjectiveInsuranceRPCServicer(object):
    """InjectiveInsuranceRPC defines gRPC API of Insurance provider.
    """

    def Funds(self, request, context):
        """Funds lists all insurance funds.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Redemptions(self, request, context):
        """PendingRedemptions lists all pending redemptions according to a filter
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InjectiveInsuranceRPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Funds': grpc.unary_unary_rpc_method_handler(
                    servicer.Funds,
                    request_deserializer=exchange_dot_injective__insurance__rpc__pb2.FundsRequest.FromString,
                    response_serializer=exchange_dot_injective__insurance__rpc__pb2.FundsResponse.SerializeToString,
            ),
            'Redemptions': grpc.unary_unary_rpc_method_handler(
                    servicer.Redemptions,
                    request_deserializer=exchange_dot_injective__insurance__rpc__pb2.RedemptionsRequest.FromString,
                    response_serializer=exchange_dot_injective__insurance__rpc__pb2.RedemptionsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective_insurance_rpc.InjectiveInsuranceRPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InjectiveInsuranceRPC(object):
    """InjectiveInsuranceRPC defines gRPC API of Insurance provider.
    """

    @staticmethod
    def Funds(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_insurance_rpc.InjectiveInsuranceRPC/Funds',
            exchange_dot_injective__insurance__rpc__pb2.FundsRequest.SerializeToString,
            exchange_dot_injective__insurance__rpc__pb2.FundsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Redemptions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_insurance_rpc.InjectiveInsuranceRPC/Redemptions',
            exchange_dot_injective__insurance__rpc__pb2.RedemptionsRequest.SerializeToString,
            exchange_dot_injective__insurance__rpc__pb2.RedemptionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
