# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from injective.exchange_api import (
    injective_accounts_rpc_pb2 as injective__accounts__rpc__pb2,
)


class InjectiveAccountsRPCStub(object):
    """InjectiveAccountsRPC defines gRPC API of Exchange Accounts provider."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubaccountsList = channel.unary_unary(
            "/injective_accounts_rpc.InjectiveAccountsRPC/SubaccountsList",
            request_serializer=injective__accounts__rpc__pb2.SubaccountsListRequest.SerializeToString,
            response_deserializer=injective__accounts__rpc__pb2.SubaccountsListResponse.FromString,
        )
        self.SubaccountBalancesList = channel.unary_unary(
            "/injective_accounts_rpc.InjectiveAccountsRPC/SubaccountBalancesList",
            request_serializer=injective__accounts__rpc__pb2.SubaccountBalancesListRequest.SerializeToString,
            response_deserializer=injective__accounts__rpc__pb2.SubaccountBalancesListResponse.FromString,
        )
        self.SubaccountBalanceEndpoint = channel.unary_unary(
            "/injective_accounts_rpc.InjectiveAccountsRPC/SubaccountBalanceEndpoint",
            request_serializer=injective__accounts__rpc__pb2.SubaccountBalanceRequest.SerializeToString,
            response_deserializer=injective__accounts__rpc__pb2.SubaccountBalanceResponse.FromString,
        )
        self.StreamSubaccountBalance = channel.unary_stream(
            "/injective_accounts_rpc.InjectiveAccountsRPC/StreamSubaccountBalance",
            request_serializer=injective__accounts__rpc__pb2.StreamSubaccountBalanceRequest.SerializeToString,
            response_deserializer=injective__accounts__rpc__pb2.StreamSubaccountBalanceResponse.FromString,
        )
        self.SubaccountHistory = channel.unary_unary(
            "/injective_accounts_rpc.InjectiveAccountsRPC/SubaccountHistory",
            request_serializer=injective__accounts__rpc__pb2.SubaccountHistoryRequest.SerializeToString,
            response_deserializer=injective__accounts__rpc__pb2.SubaccountHistoryResponse.FromString,
        )
        self.SubaccountOrderSummary = channel.unary_unary(
            "/injective_accounts_rpc.InjectiveAccountsRPC/SubaccountOrderSummary",
            request_serializer=injective__accounts__rpc__pb2.SubaccountOrderSummaryRequest.SerializeToString,
            response_deserializer=injective__accounts__rpc__pb2.SubaccountOrderSummaryResponse.FromString,
        )


class InjectiveAccountsRPCServicer(object):
    """InjectiveAccountsRPC defines gRPC API of Exchange Accounts provider."""

    def SubaccountsList(self, request, context):
        """List all subaccounts IDs of an account address"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SubaccountBalancesList(self, request, context):
        """List subaccount balances for the provided denoms."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SubaccountBalanceEndpoint(self, request, context):
        """Gets a balance for specific coin denom"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def StreamSubaccountBalance(self, request, context):
        """StreamSubaccountBalance streams new balance changes for a specified
        subaccount and denoms. If no denoms are provided, all denom changes are
        streamed.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SubaccountHistory(self, request, context):
        """Get subaccount's deposits and withdrawals history"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SubaccountOrderSummary(self, request, context):
        """Get subaccount's orders summary"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_InjectiveAccountsRPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "SubaccountsList": grpc.unary_unary_rpc_method_handler(
            servicer.SubaccountsList,
            request_deserializer=injective__accounts__rpc__pb2.SubaccountsListRequest.FromString,
            response_serializer=injective__accounts__rpc__pb2.SubaccountsListResponse.SerializeToString,
        ),
        "SubaccountBalancesList": grpc.unary_unary_rpc_method_handler(
            servicer.SubaccountBalancesList,
            request_deserializer=injective__accounts__rpc__pb2.SubaccountBalancesListRequest.FromString,
            response_serializer=injective__accounts__rpc__pb2.SubaccountBalancesListResponse.SerializeToString,
        ),
        "SubaccountBalanceEndpoint": grpc.unary_unary_rpc_method_handler(
            servicer.SubaccountBalanceEndpoint,
            request_deserializer=injective__accounts__rpc__pb2.SubaccountBalanceRequest.FromString,
            response_serializer=injective__accounts__rpc__pb2.SubaccountBalanceResponse.SerializeToString,
        ),
        "StreamSubaccountBalance": grpc.unary_stream_rpc_method_handler(
            servicer.StreamSubaccountBalance,
            request_deserializer=injective__accounts__rpc__pb2.StreamSubaccountBalanceRequest.FromString,
            response_serializer=injective__accounts__rpc__pb2.StreamSubaccountBalanceResponse.SerializeToString,
        ),
        "SubaccountHistory": grpc.unary_unary_rpc_method_handler(
            servicer.SubaccountHistory,
            request_deserializer=injective__accounts__rpc__pb2.SubaccountHistoryRequest.FromString,
            response_serializer=injective__accounts__rpc__pb2.SubaccountHistoryResponse.SerializeToString,
        ),
        "SubaccountOrderSummary": grpc.unary_unary_rpc_method_handler(
            servicer.SubaccountOrderSummary,
            request_deserializer=injective__accounts__rpc__pb2.SubaccountOrderSummaryRequest.FromString,
            response_serializer=injective__accounts__rpc__pb2.SubaccountOrderSummaryResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "injective_accounts_rpc.InjectiveAccountsRPC", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class InjectiveAccountsRPC(object):
    """InjectiveAccountsRPC defines gRPC API of Exchange Accounts provider."""

    @staticmethod
    def SubaccountsList(
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
            "/injective_accounts_rpc.InjectiveAccountsRPC/SubaccountsList",
            injective__accounts__rpc__pb2.SubaccountsListRequest.SerializeToString,
            injective__accounts__rpc__pb2.SubaccountsListResponse.FromString,
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
    def SubaccountBalancesList(
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
            "/injective_accounts_rpc.InjectiveAccountsRPC/SubaccountBalancesList",
            injective__accounts__rpc__pb2.SubaccountBalancesListRequest.SerializeToString,
            injective__accounts__rpc__pb2.SubaccountBalancesListResponse.FromString,
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
    def SubaccountBalanceEndpoint(
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
            "/injective_accounts_rpc.InjectiveAccountsRPC/SubaccountBalanceEndpoint",
            injective__accounts__rpc__pb2.SubaccountBalanceRequest.SerializeToString,
            injective__accounts__rpc__pb2.SubaccountBalanceResponse.FromString,
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
    def StreamSubaccountBalance(
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
        return grpc.experimental.unary_stream(
            request,
            target,
            "/injective_accounts_rpc.InjectiveAccountsRPC/StreamSubaccountBalance",
            injective__accounts__rpc__pb2.StreamSubaccountBalanceRequest.SerializeToString,
            injective__accounts__rpc__pb2.StreamSubaccountBalanceResponse.FromString,
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
    def SubaccountHistory(
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
            "/injective_accounts_rpc.InjectiveAccountsRPC/SubaccountHistory",
            injective__accounts__rpc__pb2.SubaccountHistoryRequest.SerializeToString,
            injective__accounts__rpc__pb2.SubaccountHistoryResponse.FromString,
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
    def SubaccountOrderSummary(
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
            "/injective_accounts_rpc.InjectiveAccountsRPC/SubaccountOrderSummary",
            injective__accounts__rpc__pb2.SubaccountOrderSummaryRequest.SerializeToString,
            injective__accounts__rpc__pb2.SubaccountOrderSummaryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
