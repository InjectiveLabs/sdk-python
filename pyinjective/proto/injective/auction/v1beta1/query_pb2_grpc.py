# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from pyinjective.proto.injective.auction.v1beta1 import query_pb2 as injective_dot_auction_dot_v1beta1_dot_query__pb2


class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AuctionParams = channel.unary_unary(
                '/injective.auction.v1beta1.Query/AuctionParams',
                request_serializer=injective_dot_auction_dot_v1beta1_dot_query__pb2.QueryAuctionParamsRequest.SerializeToString,
                response_deserializer=injective_dot_auction_dot_v1beta1_dot_query__pb2.QueryAuctionParamsResponse.FromString,
                )
        self.CurrentAuctionBasket = channel.unary_unary(
                '/injective.auction.v1beta1.Query/CurrentAuctionBasket',
                request_serializer=injective_dot_auction_dot_v1beta1_dot_query__pb2.QueryCurrentAuctionBasketRequest.SerializeToString,
                response_deserializer=injective_dot_auction_dot_v1beta1_dot_query__pb2.QueryCurrentAuctionBasketResponse.FromString,
                )
        self.AuctionModuleState = channel.unary_unary(
                '/injective.auction.v1beta1.Query/AuctionModuleState',
                request_serializer=injective_dot_auction_dot_v1beta1_dot_query__pb2.QueryModuleStateRequest.SerializeToString,
                response_deserializer=injective_dot_auction_dot_v1beta1_dot_query__pb2.QueryModuleStateResponse.FromString,
                )


class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def AuctionParams(self, request, context):
        """Retrieves auction params
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CurrentAuctionBasket(self, request, context):
        """Retrieves current auction basket with current highest bid and bidder
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AuctionModuleState(self, request, context):
        """Retrieves the entire auction module's state
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AuctionParams': grpc.unary_unary_rpc_method_handler(
                    servicer.AuctionParams,
                    request_deserializer=injective_dot_auction_dot_v1beta1_dot_query__pb2.QueryAuctionParamsRequest.FromString,
                    response_serializer=injective_dot_auction_dot_v1beta1_dot_query__pb2.QueryAuctionParamsResponse.SerializeToString,
            ),
            'CurrentAuctionBasket': grpc.unary_unary_rpc_method_handler(
                    servicer.CurrentAuctionBasket,
                    request_deserializer=injective_dot_auction_dot_v1beta1_dot_query__pb2.QueryCurrentAuctionBasketRequest.FromString,
                    response_serializer=injective_dot_auction_dot_v1beta1_dot_query__pb2.QueryCurrentAuctionBasketResponse.SerializeToString,
            ),
            'AuctionModuleState': grpc.unary_unary_rpc_method_handler(
                    servicer.AuctionModuleState,
                    request_deserializer=injective_dot_auction_dot_v1beta1_dot_query__pb2.QueryModuleStateRequest.FromString,
                    response_serializer=injective_dot_auction_dot_v1beta1_dot_query__pb2.QueryModuleStateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective.auction.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def AuctionParams(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.auction.v1beta1.Query/AuctionParams',
            injective_dot_auction_dot_v1beta1_dot_query__pb2.QueryAuctionParamsRequest.SerializeToString,
            injective_dot_auction_dot_v1beta1_dot_query__pb2.QueryAuctionParamsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CurrentAuctionBasket(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.auction.v1beta1.Query/CurrentAuctionBasket',
            injective_dot_auction_dot_v1beta1_dot_query__pb2.QueryCurrentAuctionBasketRequest.SerializeToString,
            injective_dot_auction_dot_v1beta1_dot_query__pb2.QueryCurrentAuctionBasketResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AuctionModuleState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.auction.v1beta1.Query/AuctionModuleState',
            injective_dot_auction_dot_v1beta1_dot_query__pb2.QueryModuleStateRequest.SerializeToString,
            injective_dot_auction_dot_v1beta1_dot_query__pb2.QueryModuleStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
