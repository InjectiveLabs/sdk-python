# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from injective.exchange_api import (
    injective_exchange_rpc_pb2 as injective__exchange__rpc__pb2,
)


class InjectiveExchangeRPCStub(object):
    """InjectiveExchangeRPC defines gRPC API of an Injective Exchange service."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ping = channel.unary_unary(
            "/injective_exchange_rpc.InjectiveExchangeRPC/Ping",
            request_serializer=injective__exchange__rpc__pb2.PingRequest.SerializeToString,
            response_deserializer=injective__exchange__rpc__pb2.PingResponse.FromString,
        )
        self.Version = channel.unary_unary(
            "/injective_exchange_rpc.InjectiveExchangeRPC/Version",
            request_serializer=injective__exchange__rpc__pb2.VersionRequest.SerializeToString,
            response_deserializer=injective__exchange__rpc__pb2.VersionResponse.FromString,
        )
        self.GetTx = channel.unary_unary(
            "/injective_exchange_rpc.InjectiveExchangeRPC/GetTx",
            request_serializer=injective__exchange__rpc__pb2.GetTxRequest.SerializeToString,
            response_deserializer=injective__exchange__rpc__pb2.GetTxResponse.FromString,
        )
        self.PrepareTx = channel.unary_unary(
            "/injective_exchange_rpc.InjectiveExchangeRPC/PrepareTx",
            request_serializer=injective__exchange__rpc__pb2.PrepareTxRequest.SerializeToString,
            response_deserializer=injective__exchange__rpc__pb2.PrepareTxResponse.FromString,
        )
        self.BroadcastTx = channel.unary_unary(
            "/injective_exchange_rpc.InjectiveExchangeRPC/BroadcastTx",
            request_serializer=injective__exchange__rpc__pb2.BroadcastTxRequest.SerializeToString,
            response_deserializer=injective__exchange__rpc__pb2.BroadcastTxResponse.FromString,
        )


class InjectiveExchangeRPCServicer(object):
    """InjectiveExchangeRPC defines gRPC API of an Injective Exchange service."""

    def Ping(self, request, context):
        """Endpoint for checking server health."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Version(self, request, context):
        """Returns injective-exchange version."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetTx(self, request, context):
        """GetTx gets transaction details by hash."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def PrepareTx(self, request, context):
        """PrepareTx generates a Web3-signable body for a Cosmos transaction"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def BroadcastTx(self, request, context):
        """BroadcastTx broadcasts a signed Web3 transaction"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_InjectiveExchangeRPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Ping": grpc.unary_unary_rpc_method_handler(
            servicer.Ping,
            request_deserializer=injective__exchange__rpc__pb2.PingRequest.FromString,
            response_serializer=injective__exchange__rpc__pb2.PingResponse.SerializeToString,
        ),
        "Version": grpc.unary_unary_rpc_method_handler(
            servicer.Version,
            request_deserializer=injective__exchange__rpc__pb2.VersionRequest.FromString,
            response_serializer=injective__exchange__rpc__pb2.VersionResponse.SerializeToString,
        ),
        "GetTx": grpc.unary_unary_rpc_method_handler(
            servicer.GetTx,
            request_deserializer=injective__exchange__rpc__pb2.GetTxRequest.FromString,
            response_serializer=injective__exchange__rpc__pb2.GetTxResponse.SerializeToString,
        ),
        "PrepareTx": grpc.unary_unary_rpc_method_handler(
            servicer.PrepareTx,
            request_deserializer=injective__exchange__rpc__pb2.PrepareTxRequest.FromString,
            response_serializer=injective__exchange__rpc__pb2.PrepareTxResponse.SerializeToString,
        ),
        "BroadcastTx": grpc.unary_unary_rpc_method_handler(
            servicer.BroadcastTx,
            request_deserializer=injective__exchange__rpc__pb2.BroadcastTxRequest.FromString,
            response_serializer=injective__exchange__rpc__pb2.BroadcastTxResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "injective_exchange_rpc.InjectiveExchangeRPC", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class InjectiveExchangeRPC(object):
    """InjectiveExchangeRPC defines gRPC API of an Injective Exchange service."""

    @staticmethod
    def Ping(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/injective_exchange_rpc.InjectiveExchangeRPC/Ping",
            injective__exchange__rpc__pb2.PingRequest.SerializeToString,
            injective__exchange__rpc__pb2.PingResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Version(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/injective_exchange_rpc.InjectiveExchangeRPC/Version",
            injective__exchange__rpc__pb2.VersionRequest.SerializeToString,
            injective__exchange__rpc__pb2.VersionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetTx(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/injective_exchange_rpc.InjectiveExchangeRPC/GetTx",
            injective__exchange__rpc__pb2.GetTxRequest.SerializeToString,
            injective__exchange__rpc__pb2.GetTxResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def PrepareTx(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/injective_exchange_rpc.InjectiveExchangeRPC/PrepareTx",
            injective__exchange__rpc__pb2.PrepareTxRequest.SerializeToString,
            injective__exchange__rpc__pb2.PrepareTxResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def BroadcastTx(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/injective_exchange_rpc.InjectiveExchangeRPC/BroadcastTx",
            injective__exchange__rpc__pb2.BroadcastTxRequest.SerializeToString,
            injective__exchange__rpc__pb2.BroadcastTxResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
