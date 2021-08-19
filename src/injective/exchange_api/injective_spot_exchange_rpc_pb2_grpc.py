# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from injective.exchange_api import (
    injective_spot_exchange_rpc_pb2 as injective__spot__exchange__rpc__pb2,
)


class InjectiveSpotExchangeRPCStub(object):
    """InjectiveSpotExchangeRPC defines gRPC API of Spot Exchange provider."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Markets = channel.unary_unary(
            "/injective_spot_exchange_rpc.InjectiveSpotExchangeRPC/Markets",
            request_serializer=injective__spot__exchange__rpc__pb2.MarketsRequest.SerializeToString,
            response_deserializer=injective__spot__exchange__rpc__pb2.MarketsResponse.FromString,
        )
        self.Market = channel.unary_unary(
            "/injective_spot_exchange_rpc.InjectiveSpotExchangeRPC/Market",
            request_serializer=injective__spot__exchange__rpc__pb2.MarketRequest.SerializeToString,
            response_deserializer=injective__spot__exchange__rpc__pb2.MarketResponse.FromString,
        )
        self.StreamMarkets = channel.unary_stream(
            "/injective_spot_exchange_rpc.InjectiveSpotExchangeRPC/StreamMarkets",
            request_serializer=injective__spot__exchange__rpc__pb2.StreamMarketsRequest.SerializeToString,
            response_deserializer=injective__spot__exchange__rpc__pb2.StreamMarketsResponse.FromString,
        )
        self.Orderbook = channel.unary_unary(
            "/injective_spot_exchange_rpc.InjectiveSpotExchangeRPC/Orderbook",
            request_serializer=injective__spot__exchange__rpc__pb2.OrderbookRequest.SerializeToString,
            response_deserializer=injective__spot__exchange__rpc__pb2.OrderbookResponse.FromString,
        )
        self.StreamOrderbook = channel.unary_stream(
            "/injective_spot_exchange_rpc.InjectiveSpotExchangeRPC/StreamOrderbook",
            request_serializer=injective__spot__exchange__rpc__pb2.StreamOrderbookRequest.SerializeToString,
            response_deserializer=injective__spot__exchange__rpc__pb2.StreamOrderbookResponse.FromString,
        )
        self.Orders = channel.unary_unary(
            "/injective_spot_exchange_rpc.InjectiveSpotExchangeRPC/Orders",
            request_serializer=injective__spot__exchange__rpc__pb2.OrdersRequest.SerializeToString,
            response_deserializer=injective__spot__exchange__rpc__pb2.OrdersResponse.FromString,
        )
        self.StreamOrders = channel.unary_stream(
            "/injective_spot_exchange_rpc.InjectiveSpotExchangeRPC/StreamOrders",
            request_serializer=injective__spot__exchange__rpc__pb2.StreamOrdersRequest.SerializeToString,
            response_deserializer=injective__spot__exchange__rpc__pb2.StreamOrdersResponse.FromString,
        )
        self.Trades = channel.unary_unary(
            "/injective_spot_exchange_rpc.InjectiveSpotExchangeRPC/Trades",
            request_serializer=injective__spot__exchange__rpc__pb2.TradesRequest.SerializeToString,
            response_deserializer=injective__spot__exchange__rpc__pb2.TradesResponse.FromString,
        )
        self.StreamTrades = channel.unary_stream(
            "/injective_spot_exchange_rpc.InjectiveSpotExchangeRPC/StreamTrades",
            request_serializer=injective__spot__exchange__rpc__pb2.StreamTradesRequest.SerializeToString,
            response_deserializer=injective__spot__exchange__rpc__pb2.StreamTradesResponse.FromString,
        )
        self.SubaccountOrdersList = channel.unary_unary(
            "/injective_spot_exchange_rpc.InjectiveSpotExchangeRPC/SubaccountOrdersList",
            request_serializer=injective__spot__exchange__rpc__pb2.SubaccountOrdersListRequest.SerializeToString,
            response_deserializer=injective__spot__exchange__rpc__pb2.SubaccountOrdersListResponse.FromString,
        )
        self.SubaccountTradesList = channel.unary_unary(
            "/injective_spot_exchange_rpc.InjectiveSpotExchangeRPC/SubaccountTradesList",
            request_serializer=injective__spot__exchange__rpc__pb2.SubaccountTradesListRequest.SerializeToString,
            response_deserializer=injective__spot__exchange__rpc__pb2.SubaccountTradesListResponse.FromString,
        )


class InjectiveSpotExchangeRPCServicer(object):
    """InjectiveSpotExchangeRPC defines gRPC API of Spot Exchange provider."""

    def Markets(self, request, context):
        """Get a list of Spot Markets"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Market(self, request, context):
        """Get details of a single spot market"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def StreamMarkets(self, request, context):
        """Stream live updates of selected spot markets"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Orderbook(self, request, context):
        """Orderbook of a Spot Market"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def StreamOrderbook(self, request, context):
        """Stream live updates of selected spot market orderbook"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Orders(self, request, context):
        """Orders of a Spot Market"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def StreamOrders(self, request, context):
        """Stream updates to individual orders of a Spot Market"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Trades(self, request, context):
        """Trades of a Spot Market"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def StreamTrades(self, request, context):
        """Stream newly executed trades from Spot Market"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SubaccountOrdersList(self, request, context):
        """List orders posted from this subaccount"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SubaccountTradesList(self, request, context):
        """List trades executed by this subaccount"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_InjectiveSpotExchangeRPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Markets": grpc.unary_unary_rpc_method_handler(
            servicer.Markets,
            request_deserializer=injective__spot__exchange__rpc__pb2.MarketsRequest.FromString,
            response_serializer=injective__spot__exchange__rpc__pb2.MarketsResponse.SerializeToString,
        ),
        "Market": grpc.unary_unary_rpc_method_handler(
            servicer.Market,
            request_deserializer=injective__spot__exchange__rpc__pb2.MarketRequest.FromString,
            response_serializer=injective__spot__exchange__rpc__pb2.MarketResponse.SerializeToString,
        ),
        "StreamMarkets": grpc.unary_stream_rpc_method_handler(
            servicer.StreamMarkets,
            request_deserializer=injective__spot__exchange__rpc__pb2.StreamMarketsRequest.FromString,
            response_serializer=injective__spot__exchange__rpc__pb2.StreamMarketsResponse.SerializeToString,
        ),
        "Orderbook": grpc.unary_unary_rpc_method_handler(
            servicer.Orderbook,
            request_deserializer=injective__spot__exchange__rpc__pb2.OrderbookRequest.FromString,
            response_serializer=injective__spot__exchange__rpc__pb2.OrderbookResponse.SerializeToString,
        ),
        "StreamOrderbook": grpc.unary_stream_rpc_method_handler(
            servicer.StreamOrderbook,
            request_deserializer=injective__spot__exchange__rpc__pb2.StreamOrderbookRequest.FromString,
            response_serializer=injective__spot__exchange__rpc__pb2.StreamOrderbookResponse.SerializeToString,
        ),
        "Orders": grpc.unary_unary_rpc_method_handler(
            servicer.Orders,
            request_deserializer=injective__spot__exchange__rpc__pb2.OrdersRequest.FromString,
            response_serializer=injective__spot__exchange__rpc__pb2.OrdersResponse.SerializeToString,
        ),
        "StreamOrders": grpc.unary_stream_rpc_method_handler(
            servicer.StreamOrders,
            request_deserializer=injective__spot__exchange__rpc__pb2.StreamOrdersRequest.FromString,
            response_serializer=injective__spot__exchange__rpc__pb2.StreamOrdersResponse.SerializeToString,
        ),
        "Trades": grpc.unary_unary_rpc_method_handler(
            servicer.Trades,
            request_deserializer=injective__spot__exchange__rpc__pb2.TradesRequest.FromString,
            response_serializer=injective__spot__exchange__rpc__pb2.TradesResponse.SerializeToString,
        ),
        "StreamTrades": grpc.unary_stream_rpc_method_handler(
            servicer.StreamTrades,
            request_deserializer=injective__spot__exchange__rpc__pb2.StreamTradesRequest.FromString,
            response_serializer=injective__spot__exchange__rpc__pb2.StreamTradesResponse.SerializeToString,
        ),
        "SubaccountOrdersList": grpc.unary_unary_rpc_method_handler(
            servicer.SubaccountOrdersList,
            request_deserializer=injective__spot__exchange__rpc__pb2.SubaccountOrdersListRequest.FromString,
            response_serializer=injective__spot__exchange__rpc__pb2.SubaccountOrdersListResponse.SerializeToString,
        ),
        "SubaccountTradesList": grpc.unary_unary_rpc_method_handler(
            servicer.SubaccountTradesList,
            request_deserializer=injective__spot__exchange__rpc__pb2.SubaccountTradesListRequest.FromString,
            response_serializer=injective__spot__exchange__rpc__pb2.SubaccountTradesListResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "injective_spot_exchange_rpc.InjectiveSpotExchangeRPC", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class InjectiveSpotExchangeRPC(object):
    """InjectiveSpotExchangeRPC defines gRPC API of Spot Exchange provider."""

    @staticmethod
    def Markets(
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
            "/injective_spot_exchange_rpc.InjectiveSpotExchangeRPC/Markets",
            injective__spot__exchange__rpc__pb2.MarketsRequest.SerializeToString,
            injective__spot__exchange__rpc__pb2.MarketsResponse.FromString,
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
    def Market(
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
            "/injective_spot_exchange_rpc.InjectiveSpotExchangeRPC/Market",
            injective__spot__exchange__rpc__pb2.MarketRequest.SerializeToString,
            injective__spot__exchange__rpc__pb2.MarketResponse.FromString,
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
    def StreamMarkets(
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
            "/injective_spot_exchange_rpc.InjectiveSpotExchangeRPC/StreamMarkets",
            injective__spot__exchange__rpc__pb2.StreamMarketsRequest.SerializeToString,
            injective__spot__exchange__rpc__pb2.StreamMarketsResponse.FromString,
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
    def Orderbook(
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
            "/injective_spot_exchange_rpc.InjectiveSpotExchangeRPC/Orderbook",
            injective__spot__exchange__rpc__pb2.OrderbookRequest.SerializeToString,
            injective__spot__exchange__rpc__pb2.OrderbookResponse.FromString,
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
    def StreamOrderbook(
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
            "/injective_spot_exchange_rpc.InjectiveSpotExchangeRPC/StreamOrderbook",
            injective__spot__exchange__rpc__pb2.StreamOrderbookRequest.SerializeToString,
            injective__spot__exchange__rpc__pb2.StreamOrderbookResponse.FromString,
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
    def Orders(
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
            "/injective_spot_exchange_rpc.InjectiveSpotExchangeRPC/Orders",
            injective__spot__exchange__rpc__pb2.OrdersRequest.SerializeToString,
            injective__spot__exchange__rpc__pb2.OrdersResponse.FromString,
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
    def StreamOrders(
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
            "/injective_spot_exchange_rpc.InjectiveSpotExchangeRPC/StreamOrders",
            injective__spot__exchange__rpc__pb2.StreamOrdersRequest.SerializeToString,
            injective__spot__exchange__rpc__pb2.StreamOrdersResponse.FromString,
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
    def Trades(
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
            "/injective_spot_exchange_rpc.InjectiveSpotExchangeRPC/Trades",
            injective__spot__exchange__rpc__pb2.TradesRequest.SerializeToString,
            injective__spot__exchange__rpc__pb2.TradesResponse.FromString,
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
    def StreamTrades(
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
            "/injective_spot_exchange_rpc.InjectiveSpotExchangeRPC/StreamTrades",
            injective__spot__exchange__rpc__pb2.StreamTradesRequest.SerializeToString,
            injective__spot__exchange__rpc__pb2.StreamTradesResponse.FromString,
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
    def SubaccountOrdersList(
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
            "/injective_spot_exchange_rpc.InjectiveSpotExchangeRPC/SubaccountOrdersList",
            injective__spot__exchange__rpc__pb2.SubaccountOrdersListRequest.SerializeToString,
            injective__spot__exchange__rpc__pb2.SubaccountOrdersListResponse.FromString,
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
    def SubaccountTradesList(
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
            "/injective_spot_exchange_rpc.InjectiveSpotExchangeRPC/SubaccountTradesList",
            injective__spot__exchange__rpc__pb2.SubaccountTradesListRequest.SerializeToString,
            injective__spot__exchange__rpc__pb2.SubaccountTradesListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
