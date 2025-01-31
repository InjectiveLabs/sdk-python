# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from pyinjective.proto.injective.wasmx.v1 import query_pb2 as injective_dot_wasmx_dot_v1_dot_query__pb2


class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.WasmxParams = channel.unary_unary(
                '/injective.wasmx.v1.Query/WasmxParams',
                request_serializer=injective_dot_wasmx_dot_v1_dot_query__pb2.QueryWasmxParamsRequest.SerializeToString,
                response_deserializer=injective_dot_wasmx_dot_v1_dot_query__pb2.QueryWasmxParamsResponse.FromString,
                _registered_method=True)
        self.ContractRegistrationInfo = channel.unary_unary(
                '/injective.wasmx.v1.Query/ContractRegistrationInfo',
                request_serializer=injective_dot_wasmx_dot_v1_dot_query__pb2.QueryContractRegistrationInfoRequest.SerializeToString,
                response_deserializer=injective_dot_wasmx_dot_v1_dot_query__pb2.QueryContractRegistrationInfoResponse.FromString,
                _registered_method=True)
        self.WasmxModuleState = channel.unary_unary(
                '/injective.wasmx.v1.Query/WasmxModuleState',
                request_serializer=injective_dot_wasmx_dot_v1_dot_query__pb2.QueryModuleStateRequest.SerializeToString,
                response_deserializer=injective_dot_wasmx_dot_v1_dot_query__pb2.QueryModuleStateResponse.FromString,
                _registered_method=True)


class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def WasmxParams(self, request, context):
        """Retrieves wasmx params
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ContractRegistrationInfo(self, request, context):
        """Retrieves contract registration info
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WasmxModuleState(self, request, context):
        """Retrieves the entire wasmx module's state
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'WasmxParams': grpc.unary_unary_rpc_method_handler(
                    servicer.WasmxParams,
                    request_deserializer=injective_dot_wasmx_dot_v1_dot_query__pb2.QueryWasmxParamsRequest.FromString,
                    response_serializer=injective_dot_wasmx_dot_v1_dot_query__pb2.QueryWasmxParamsResponse.SerializeToString,
            ),
            'ContractRegistrationInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.ContractRegistrationInfo,
                    request_deserializer=injective_dot_wasmx_dot_v1_dot_query__pb2.QueryContractRegistrationInfoRequest.FromString,
                    response_serializer=injective_dot_wasmx_dot_v1_dot_query__pb2.QueryContractRegistrationInfoResponse.SerializeToString,
            ),
            'WasmxModuleState': grpc.unary_unary_rpc_method_handler(
                    servicer.WasmxModuleState,
                    request_deserializer=injective_dot_wasmx_dot_v1_dot_query__pb2.QueryModuleStateRequest.FromString,
                    response_serializer=injective_dot_wasmx_dot_v1_dot_query__pb2.QueryModuleStateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective.wasmx.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('injective.wasmx.v1.Query', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def WasmxParams(request,
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
            '/injective.wasmx.v1.Query/WasmxParams',
            injective_dot_wasmx_dot_v1_dot_query__pb2.QueryWasmxParamsRequest.SerializeToString,
            injective_dot_wasmx_dot_v1_dot_query__pb2.QueryWasmxParamsResponse.FromString,
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
    def ContractRegistrationInfo(request,
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
            '/injective.wasmx.v1.Query/ContractRegistrationInfo',
            injective_dot_wasmx_dot_v1_dot_query__pb2.QueryContractRegistrationInfoRequest.SerializeToString,
            injective_dot_wasmx_dot_v1_dot_query__pb2.QueryContractRegistrationInfoResponse.FromString,
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
    def WasmxModuleState(request,
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
            '/injective.wasmx.v1.Query/WasmxModuleState',
            injective_dot_wasmx_dot_v1_dot_query__pb2.QueryModuleStateRequest.SerializeToString,
            injective_dot_wasmx_dot_v1_dot_query__pb2.QueryModuleStateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
