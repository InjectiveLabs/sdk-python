# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from pyinjective.proto.testpb import test_schema_query_pb2 as testpb_dot_test__schema__query__pb2


class TestSchemaQueryServiceStub(object):
    """TestSchemaQueryService queries the state of the tables specified by testpb/test_schema.proto.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetExampleTable = channel.unary_unary(
                '/testpb.TestSchemaQueryService/GetExampleTable',
                request_serializer=testpb_dot_test__schema__query__pb2.GetExampleTableRequest.SerializeToString,
                response_deserializer=testpb_dot_test__schema__query__pb2.GetExampleTableResponse.FromString,
                )
        self.GetExampleTableByU64Str = channel.unary_unary(
                '/testpb.TestSchemaQueryService/GetExampleTableByU64Str',
                request_serializer=testpb_dot_test__schema__query__pb2.GetExampleTableByU64StrRequest.SerializeToString,
                response_deserializer=testpb_dot_test__schema__query__pb2.GetExampleTableByU64StrResponse.FromString,
                )
        self.ListExampleTable = channel.unary_unary(
                '/testpb.TestSchemaQueryService/ListExampleTable',
                request_serializer=testpb_dot_test__schema__query__pb2.ListExampleTableRequest.SerializeToString,
                response_deserializer=testpb_dot_test__schema__query__pb2.ListExampleTableResponse.FromString,
                )
        self.GetExampleAutoIncrementTable = channel.unary_unary(
                '/testpb.TestSchemaQueryService/GetExampleAutoIncrementTable',
                request_serializer=testpb_dot_test__schema__query__pb2.GetExampleAutoIncrementTableRequest.SerializeToString,
                response_deserializer=testpb_dot_test__schema__query__pb2.GetExampleAutoIncrementTableResponse.FromString,
                )
        self.GetExampleAutoIncrementTableByX = channel.unary_unary(
                '/testpb.TestSchemaQueryService/GetExampleAutoIncrementTableByX',
                request_serializer=testpb_dot_test__schema__query__pb2.GetExampleAutoIncrementTableByXRequest.SerializeToString,
                response_deserializer=testpb_dot_test__schema__query__pb2.GetExampleAutoIncrementTableByXResponse.FromString,
                )
        self.ListExampleAutoIncrementTable = channel.unary_unary(
                '/testpb.TestSchemaQueryService/ListExampleAutoIncrementTable',
                request_serializer=testpb_dot_test__schema__query__pb2.ListExampleAutoIncrementTableRequest.SerializeToString,
                response_deserializer=testpb_dot_test__schema__query__pb2.ListExampleAutoIncrementTableResponse.FromString,
                )
        self.GetExampleSingleton = channel.unary_unary(
                '/testpb.TestSchemaQueryService/GetExampleSingleton',
                request_serializer=testpb_dot_test__schema__query__pb2.GetExampleSingletonRequest.SerializeToString,
                response_deserializer=testpb_dot_test__schema__query__pb2.GetExampleSingletonResponse.FromString,
                )
        self.GetExampleTimestamp = channel.unary_unary(
                '/testpb.TestSchemaQueryService/GetExampleTimestamp',
                request_serializer=testpb_dot_test__schema__query__pb2.GetExampleTimestampRequest.SerializeToString,
                response_deserializer=testpb_dot_test__schema__query__pb2.GetExampleTimestampResponse.FromString,
                )
        self.ListExampleTimestamp = channel.unary_unary(
                '/testpb.TestSchemaQueryService/ListExampleTimestamp',
                request_serializer=testpb_dot_test__schema__query__pb2.ListExampleTimestampRequest.SerializeToString,
                response_deserializer=testpb_dot_test__schema__query__pb2.ListExampleTimestampResponse.FromString,
                )
        self.GetSimpleExample = channel.unary_unary(
                '/testpb.TestSchemaQueryService/GetSimpleExample',
                request_serializer=testpb_dot_test__schema__query__pb2.GetSimpleExampleRequest.SerializeToString,
                response_deserializer=testpb_dot_test__schema__query__pb2.GetSimpleExampleResponse.FromString,
                )
        self.GetSimpleExampleByUnique = channel.unary_unary(
                '/testpb.TestSchemaQueryService/GetSimpleExampleByUnique',
                request_serializer=testpb_dot_test__schema__query__pb2.GetSimpleExampleByUniqueRequest.SerializeToString,
                response_deserializer=testpb_dot_test__schema__query__pb2.GetSimpleExampleByUniqueResponse.FromString,
                )
        self.ListSimpleExample = channel.unary_unary(
                '/testpb.TestSchemaQueryService/ListSimpleExample',
                request_serializer=testpb_dot_test__schema__query__pb2.ListSimpleExampleRequest.SerializeToString,
                response_deserializer=testpb_dot_test__schema__query__pb2.ListSimpleExampleResponse.FromString,
                )
        self.GetExampleAutoIncFieldName = channel.unary_unary(
                '/testpb.TestSchemaQueryService/GetExampleAutoIncFieldName',
                request_serializer=testpb_dot_test__schema__query__pb2.GetExampleAutoIncFieldNameRequest.SerializeToString,
                response_deserializer=testpb_dot_test__schema__query__pb2.GetExampleAutoIncFieldNameResponse.FromString,
                )
        self.ListExampleAutoIncFieldName = channel.unary_unary(
                '/testpb.TestSchemaQueryService/ListExampleAutoIncFieldName',
                request_serializer=testpb_dot_test__schema__query__pb2.ListExampleAutoIncFieldNameRequest.SerializeToString,
                response_deserializer=testpb_dot_test__schema__query__pb2.ListExampleAutoIncFieldNameResponse.FromString,
                )


class TestSchemaQueryServiceServicer(object):
    """TestSchemaQueryService queries the state of the tables specified by testpb/test_schema.proto.
    """

    def GetExampleTable(self, request, context):
        """Get queries the ExampleTable table by its primary key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetExampleTableByU64Str(self, request, context):
        """GetExampleTableByU64Str queries the ExampleTable table by its U64Str index
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListExampleTable(self, request, context):
        """ListExampleTable queries the ExampleTable table using prefix and range queries against defined indexes.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetExampleAutoIncrementTable(self, request, context):
        """Get queries the ExampleAutoIncrementTable table by its primary key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetExampleAutoIncrementTableByX(self, request, context):
        """GetExampleAutoIncrementTableByX queries the ExampleAutoIncrementTable table by its X index
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListExampleAutoIncrementTable(self, request, context):
        """ListExampleAutoIncrementTable queries the ExampleAutoIncrementTable table using prefix and range queries against
        defined indexes.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetExampleSingleton(self, request, context):
        """GetExampleSingleton queries the ExampleSingleton singleton.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetExampleTimestamp(self, request, context):
        """Get queries the ExampleTimestamp table by its primary key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListExampleTimestamp(self, request, context):
        """ListExampleTimestamp queries the ExampleTimestamp table using prefix and range queries against defined indexes.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSimpleExample(self, request, context):
        """Get queries the SimpleExample table by its primary key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSimpleExampleByUnique(self, request, context):
        """GetSimpleExampleByUnique queries the SimpleExample table by its Unique index
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSimpleExample(self, request, context):
        """ListSimpleExample queries the SimpleExample table using prefix and range queries against defined indexes.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetExampleAutoIncFieldName(self, request, context):
        """Get queries the ExampleAutoIncFieldName table by its primary key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListExampleAutoIncFieldName(self, request, context):
        """ListExampleAutoIncFieldName queries the ExampleAutoIncFieldName table using prefix and range queries against
        defined indexes.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TestSchemaQueryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetExampleTable': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExampleTable,
                    request_deserializer=testpb_dot_test__schema__query__pb2.GetExampleTableRequest.FromString,
                    response_serializer=testpb_dot_test__schema__query__pb2.GetExampleTableResponse.SerializeToString,
            ),
            'GetExampleTableByU64Str': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExampleTableByU64Str,
                    request_deserializer=testpb_dot_test__schema__query__pb2.GetExampleTableByU64StrRequest.FromString,
                    response_serializer=testpb_dot_test__schema__query__pb2.GetExampleTableByU64StrResponse.SerializeToString,
            ),
            'ListExampleTable': grpc.unary_unary_rpc_method_handler(
                    servicer.ListExampleTable,
                    request_deserializer=testpb_dot_test__schema__query__pb2.ListExampleTableRequest.FromString,
                    response_serializer=testpb_dot_test__schema__query__pb2.ListExampleTableResponse.SerializeToString,
            ),
            'GetExampleAutoIncrementTable': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExampleAutoIncrementTable,
                    request_deserializer=testpb_dot_test__schema__query__pb2.GetExampleAutoIncrementTableRequest.FromString,
                    response_serializer=testpb_dot_test__schema__query__pb2.GetExampleAutoIncrementTableResponse.SerializeToString,
            ),
            'GetExampleAutoIncrementTableByX': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExampleAutoIncrementTableByX,
                    request_deserializer=testpb_dot_test__schema__query__pb2.GetExampleAutoIncrementTableByXRequest.FromString,
                    response_serializer=testpb_dot_test__schema__query__pb2.GetExampleAutoIncrementTableByXResponse.SerializeToString,
            ),
            'ListExampleAutoIncrementTable': grpc.unary_unary_rpc_method_handler(
                    servicer.ListExampleAutoIncrementTable,
                    request_deserializer=testpb_dot_test__schema__query__pb2.ListExampleAutoIncrementTableRequest.FromString,
                    response_serializer=testpb_dot_test__schema__query__pb2.ListExampleAutoIncrementTableResponse.SerializeToString,
            ),
            'GetExampleSingleton': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExampleSingleton,
                    request_deserializer=testpb_dot_test__schema__query__pb2.GetExampleSingletonRequest.FromString,
                    response_serializer=testpb_dot_test__schema__query__pb2.GetExampleSingletonResponse.SerializeToString,
            ),
            'GetExampleTimestamp': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExampleTimestamp,
                    request_deserializer=testpb_dot_test__schema__query__pb2.GetExampleTimestampRequest.FromString,
                    response_serializer=testpb_dot_test__schema__query__pb2.GetExampleTimestampResponse.SerializeToString,
            ),
            'ListExampleTimestamp': grpc.unary_unary_rpc_method_handler(
                    servicer.ListExampleTimestamp,
                    request_deserializer=testpb_dot_test__schema__query__pb2.ListExampleTimestampRequest.FromString,
                    response_serializer=testpb_dot_test__schema__query__pb2.ListExampleTimestampResponse.SerializeToString,
            ),
            'GetSimpleExample': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSimpleExample,
                    request_deserializer=testpb_dot_test__schema__query__pb2.GetSimpleExampleRequest.FromString,
                    response_serializer=testpb_dot_test__schema__query__pb2.GetSimpleExampleResponse.SerializeToString,
            ),
            'GetSimpleExampleByUnique': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSimpleExampleByUnique,
                    request_deserializer=testpb_dot_test__schema__query__pb2.GetSimpleExampleByUniqueRequest.FromString,
                    response_serializer=testpb_dot_test__schema__query__pb2.GetSimpleExampleByUniqueResponse.SerializeToString,
            ),
            'ListSimpleExample': grpc.unary_unary_rpc_method_handler(
                    servicer.ListSimpleExample,
                    request_deserializer=testpb_dot_test__schema__query__pb2.ListSimpleExampleRequest.FromString,
                    response_serializer=testpb_dot_test__schema__query__pb2.ListSimpleExampleResponse.SerializeToString,
            ),
            'GetExampleAutoIncFieldName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExampleAutoIncFieldName,
                    request_deserializer=testpb_dot_test__schema__query__pb2.GetExampleAutoIncFieldNameRequest.FromString,
                    response_serializer=testpb_dot_test__schema__query__pb2.GetExampleAutoIncFieldNameResponse.SerializeToString,
            ),
            'ListExampleAutoIncFieldName': grpc.unary_unary_rpc_method_handler(
                    servicer.ListExampleAutoIncFieldName,
                    request_deserializer=testpb_dot_test__schema__query__pb2.ListExampleAutoIncFieldNameRequest.FromString,
                    response_serializer=testpb_dot_test__schema__query__pb2.ListExampleAutoIncFieldNameResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'testpb.TestSchemaQueryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TestSchemaQueryService(object):
    """TestSchemaQueryService queries the state of the tables specified by testpb/test_schema.proto.
    """

    @staticmethod
    def GetExampleTable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testpb.TestSchemaQueryService/GetExampleTable',
            testpb_dot_test__schema__query__pb2.GetExampleTableRequest.SerializeToString,
            testpb_dot_test__schema__query__pb2.GetExampleTableResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetExampleTableByU64Str(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testpb.TestSchemaQueryService/GetExampleTableByU64Str',
            testpb_dot_test__schema__query__pb2.GetExampleTableByU64StrRequest.SerializeToString,
            testpb_dot_test__schema__query__pb2.GetExampleTableByU64StrResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListExampleTable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testpb.TestSchemaQueryService/ListExampleTable',
            testpb_dot_test__schema__query__pb2.ListExampleTableRequest.SerializeToString,
            testpb_dot_test__schema__query__pb2.ListExampleTableResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetExampleAutoIncrementTable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testpb.TestSchemaQueryService/GetExampleAutoIncrementTable',
            testpb_dot_test__schema__query__pb2.GetExampleAutoIncrementTableRequest.SerializeToString,
            testpb_dot_test__schema__query__pb2.GetExampleAutoIncrementTableResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetExampleAutoIncrementTableByX(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testpb.TestSchemaQueryService/GetExampleAutoIncrementTableByX',
            testpb_dot_test__schema__query__pb2.GetExampleAutoIncrementTableByXRequest.SerializeToString,
            testpb_dot_test__schema__query__pb2.GetExampleAutoIncrementTableByXResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListExampleAutoIncrementTable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testpb.TestSchemaQueryService/ListExampleAutoIncrementTable',
            testpb_dot_test__schema__query__pb2.ListExampleAutoIncrementTableRequest.SerializeToString,
            testpb_dot_test__schema__query__pb2.ListExampleAutoIncrementTableResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetExampleSingleton(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testpb.TestSchemaQueryService/GetExampleSingleton',
            testpb_dot_test__schema__query__pb2.GetExampleSingletonRequest.SerializeToString,
            testpb_dot_test__schema__query__pb2.GetExampleSingletonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetExampleTimestamp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testpb.TestSchemaQueryService/GetExampleTimestamp',
            testpb_dot_test__schema__query__pb2.GetExampleTimestampRequest.SerializeToString,
            testpb_dot_test__schema__query__pb2.GetExampleTimestampResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListExampleTimestamp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testpb.TestSchemaQueryService/ListExampleTimestamp',
            testpb_dot_test__schema__query__pb2.ListExampleTimestampRequest.SerializeToString,
            testpb_dot_test__schema__query__pb2.ListExampleTimestampResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSimpleExample(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testpb.TestSchemaQueryService/GetSimpleExample',
            testpb_dot_test__schema__query__pb2.GetSimpleExampleRequest.SerializeToString,
            testpb_dot_test__schema__query__pb2.GetSimpleExampleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSimpleExampleByUnique(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testpb.TestSchemaQueryService/GetSimpleExampleByUnique',
            testpb_dot_test__schema__query__pb2.GetSimpleExampleByUniqueRequest.SerializeToString,
            testpb_dot_test__schema__query__pb2.GetSimpleExampleByUniqueResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListSimpleExample(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testpb.TestSchemaQueryService/ListSimpleExample',
            testpb_dot_test__schema__query__pb2.ListSimpleExampleRequest.SerializeToString,
            testpb_dot_test__schema__query__pb2.ListSimpleExampleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetExampleAutoIncFieldName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testpb.TestSchemaQueryService/GetExampleAutoIncFieldName',
            testpb_dot_test__schema__query__pb2.GetExampleAutoIncFieldNameRequest.SerializeToString,
            testpb_dot_test__schema__query__pb2.GetExampleAutoIncFieldNameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListExampleAutoIncFieldName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testpb.TestSchemaQueryService/ListExampleAutoIncFieldName',
            testpb_dot_test__schema__query__pb2.ListExampleAutoIncFieldNameRequest.SerializeToString,
            testpb_dot_test__schema__query__pb2.ListExampleAutoIncFieldNameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
