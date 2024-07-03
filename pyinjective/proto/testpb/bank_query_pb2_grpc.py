# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from pyinjective.proto.testpb import bank_query_pb2 as testpb_dot_bank__query__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in testpb/bank_query_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class BankQueryServiceStub(object):
    """BankQueryService queries the state of the tables specified by testpb/bank.proto.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetBalance = channel.unary_unary(
                '/testpb.BankQueryService/GetBalance',
                request_serializer=testpb_dot_bank__query__pb2.GetBalanceRequest.SerializeToString,
                response_deserializer=testpb_dot_bank__query__pb2.GetBalanceResponse.FromString,
                _registered_method=True)
        self.ListBalance = channel.unary_unary(
                '/testpb.BankQueryService/ListBalance',
                request_serializer=testpb_dot_bank__query__pb2.ListBalanceRequest.SerializeToString,
                response_deserializer=testpb_dot_bank__query__pb2.ListBalanceResponse.FromString,
                _registered_method=True)
        self.GetSupply = channel.unary_unary(
                '/testpb.BankQueryService/GetSupply',
                request_serializer=testpb_dot_bank__query__pb2.GetSupplyRequest.SerializeToString,
                response_deserializer=testpb_dot_bank__query__pb2.GetSupplyResponse.FromString,
                _registered_method=True)
        self.ListSupply = channel.unary_unary(
                '/testpb.BankQueryService/ListSupply',
                request_serializer=testpb_dot_bank__query__pb2.ListSupplyRequest.SerializeToString,
                response_deserializer=testpb_dot_bank__query__pb2.ListSupplyResponse.FromString,
                _registered_method=True)


class BankQueryServiceServicer(object):
    """BankQueryService queries the state of the tables specified by testpb/bank.proto.
    """

    def GetBalance(self, request, context):
        """Get queries the Balance table by its primary key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListBalance(self, request, context):
        """ListBalance queries the Balance table using prefix and range queries against defined indexes.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSupply(self, request, context):
        """Get queries the Supply table by its primary key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSupply(self, request, context):
        """ListSupply queries the Supply table using prefix and range queries against defined indexes.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BankQueryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetBalance': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBalance,
                    request_deserializer=testpb_dot_bank__query__pb2.GetBalanceRequest.FromString,
                    response_serializer=testpb_dot_bank__query__pb2.GetBalanceResponse.SerializeToString,
            ),
            'ListBalance': grpc.unary_unary_rpc_method_handler(
                    servicer.ListBalance,
                    request_deserializer=testpb_dot_bank__query__pb2.ListBalanceRequest.FromString,
                    response_serializer=testpb_dot_bank__query__pb2.ListBalanceResponse.SerializeToString,
            ),
            'GetSupply': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSupply,
                    request_deserializer=testpb_dot_bank__query__pb2.GetSupplyRequest.FromString,
                    response_serializer=testpb_dot_bank__query__pb2.GetSupplyResponse.SerializeToString,
            ),
            'ListSupply': grpc.unary_unary_rpc_method_handler(
                    servicer.ListSupply,
                    request_deserializer=testpb_dot_bank__query__pb2.ListSupplyRequest.FromString,
                    response_serializer=testpb_dot_bank__query__pb2.ListSupplyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'testpb.BankQueryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('testpb.BankQueryService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class BankQueryService(object):
    """BankQueryService queries the state of the tables specified by testpb/bank.proto.
    """

    @staticmethod
    def GetBalance(request,
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
            '/testpb.BankQueryService/GetBalance',
            testpb_dot_bank__query__pb2.GetBalanceRequest.SerializeToString,
            testpb_dot_bank__query__pb2.GetBalanceResponse.FromString,
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
    def ListBalance(request,
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
            '/testpb.BankQueryService/ListBalance',
            testpb_dot_bank__query__pb2.ListBalanceRequest.SerializeToString,
            testpb_dot_bank__query__pb2.ListBalanceResponse.FromString,
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
    def GetSupply(request,
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
            '/testpb.BankQueryService/GetSupply',
            testpb_dot_bank__query__pb2.GetSupplyRequest.SerializeToString,
            testpb_dot_bank__query__pb2.GetSupplyResponse.FromString,
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
    def ListSupply(request,
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
            '/testpb.BankQueryService/ListSupply',
            testpb_dot_bank__query__pb2.ListSupplyRequest.SerializeToString,
            testpb_dot_bank__query__pb2.ListSupplyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
