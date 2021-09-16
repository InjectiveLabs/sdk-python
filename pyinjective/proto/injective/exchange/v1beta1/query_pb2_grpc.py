# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from injective.exchange.v1beta1 import query_pb2 as injective_dot_exchange_dot_v1beta1_dot_query__pb2


class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.QueryExchangeParams = channel.unary_unary(
                '/injective.exchange.v1beta1.Query/QueryExchangeParams',
                request_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryExchangeParamsRequest.SerializeToString,
                response_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryExchangeParamsResponse.FromString,
                )
        self.SubaccountDeposits = channel.unary_unary(
                '/injective.exchange.v1beta1.Query/SubaccountDeposits',
                request_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySubaccountDepositsRequest.SerializeToString,
                response_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySubaccountDepositsResponse.FromString,
                )
        self.SubaccountDeposit = channel.unary_unary(
                '/injective.exchange.v1beta1.Query/SubaccountDeposit',
                request_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySubaccountDepositRequest.SerializeToString,
                response_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySubaccountDepositResponse.FromString,
                )
        self.ExchangeBalances = channel.unary_unary(
                '/injective.exchange.v1beta1.Query/ExchangeBalances',
                request_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryExchangeBalancesRequest.SerializeToString,
                response_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryExchangeBalancesResponse.FromString,
                )
        self.SpotMarkets = channel.unary_unary(
                '/injective.exchange.v1beta1.Query/SpotMarkets',
                request_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySpotMarketsRequest.SerializeToString,
                response_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySpotMarketsResponse.FromString,
                )
        self.SpotMarket = channel.unary_unary(
                '/injective.exchange.v1beta1.Query/SpotMarket',
                request_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySpotMarketRequest.SerializeToString,
                response_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySpotMarketResponse.FromString,
                )
        self.SpotOrderbook = channel.unary_unary(
                '/injective.exchange.v1beta1.Query/SpotOrderbook',
                request_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySpotOrderbookRequest.SerializeToString,
                response_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySpotOrderbookResponse.FromString,
                )
        self.TraderSpotOrders = channel.unary_unary(
                '/injective.exchange.v1beta1.Query/TraderSpotOrders',
                request_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryTraderSpotOrdersRequest.SerializeToString,
                response_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryTraderSpotOrdersResponse.FromString,
                )
        self.DerivativeOrderbook = channel.unary_unary(
                '/injective.exchange.v1beta1.Query/DerivativeOrderbook',
                request_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryDerivativeOrderbookRequest.SerializeToString,
                response_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryDerivativeOrderbookResponse.FromString,
                )
        self.TraderDerivativeOrders = channel.unary_unary(
                '/injective.exchange.v1beta1.Query/TraderDerivativeOrders',
                request_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryTraderDerivativeOrdersRequest.SerializeToString,
                response_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryTraderDerivativeOrdersResponse.FromString,
                )
        self.DerivativeMarkets = channel.unary_unary(
                '/injective.exchange.v1beta1.Query/DerivativeMarkets',
                request_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryDerivativeMarketsRequest.SerializeToString,
                response_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryDerivativeMarketsResponse.FromString,
                )
        self.DerivativeMarket = channel.unary_unary(
                '/injective.exchange.v1beta1.Query/DerivativeMarket',
                request_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryDerivativeMarketRequest.SerializeToString,
                response_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryDerivativeMarketResponse.FromString,
                )
        self.SubaccountTradeNonce = channel.unary_unary(
                '/injective.exchange.v1beta1.Query/SubaccountTradeNonce',
                request_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySubaccountTradeNonceRequest.SerializeToString,
                response_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySubaccountTradeNonceResponse.FromString,
                )
        self.ExchangeModuleState = channel.unary_unary(
                '/injective.exchange.v1beta1.Query/ExchangeModuleState',
                request_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryModuleStateRequest.SerializeToString,
                response_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryModuleStateResponse.FromString,
                )
        self.Positions = channel.unary_unary(
                '/injective.exchange.v1beta1.Query/Positions',
                request_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryPositionsRequest.SerializeToString,
                response_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryPositionsResponse.FromString,
                )


class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def QueryExchangeParams(self, request, context):
        """Retrieves exchange params
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubaccountDeposits(self, request, context):
        """Retrieves a Subaccount's Deposits
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubaccountDeposit(self, request, context):
        """Retrieves a Subaccount's Deposits
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExchangeBalances(self, request, context):
        """Retrieves all of the balances of all users on the exchange.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SpotMarkets(self, request, context):
        """Retrieves a list of spot markets.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SpotMarket(self, request, context):
        """Retrieves a spot market by ticker
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SpotOrderbook(self, request, context):
        """Retrieves a spot market's orderbook by marketID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TraderSpotOrders(self, request, context):
        """Retrieves a trader's spot orders
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DerivativeOrderbook(self, request, context):
        """Retrieves a derivative market's orderbook by marketID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TraderDerivativeOrders(self, request, context):
        """Retrieves a trader's derivative orders
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DerivativeMarkets(self, request, context):
        """Retrieves a list of spot markets.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DerivativeMarket(self, request, context):
        """Retrieves a spot market by ticker
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubaccountTradeNonce(self, request, context):
        """Retrieves a subaccount's trade nonce
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExchangeModuleState(self, request, context):
        """Retrieves the entire exchange module's state
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Positions(self, request, context):
        """Retrieves the entire exchange module's positions
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'QueryExchangeParams': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryExchangeParams,
                    request_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryExchangeParamsRequest.FromString,
                    response_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryExchangeParamsResponse.SerializeToString,
            ),
            'SubaccountDeposits': grpc.unary_unary_rpc_method_handler(
                    servicer.SubaccountDeposits,
                    request_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySubaccountDepositsRequest.FromString,
                    response_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySubaccountDepositsResponse.SerializeToString,
            ),
            'SubaccountDeposit': grpc.unary_unary_rpc_method_handler(
                    servicer.SubaccountDeposit,
                    request_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySubaccountDepositRequest.FromString,
                    response_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySubaccountDepositResponse.SerializeToString,
            ),
            'ExchangeBalances': grpc.unary_unary_rpc_method_handler(
                    servicer.ExchangeBalances,
                    request_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryExchangeBalancesRequest.FromString,
                    response_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryExchangeBalancesResponse.SerializeToString,
            ),
            'SpotMarkets': grpc.unary_unary_rpc_method_handler(
                    servicer.SpotMarkets,
                    request_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySpotMarketsRequest.FromString,
                    response_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySpotMarketsResponse.SerializeToString,
            ),
            'SpotMarket': grpc.unary_unary_rpc_method_handler(
                    servicer.SpotMarket,
                    request_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySpotMarketRequest.FromString,
                    response_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySpotMarketResponse.SerializeToString,
            ),
            'SpotOrderbook': grpc.unary_unary_rpc_method_handler(
                    servicer.SpotOrderbook,
                    request_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySpotOrderbookRequest.FromString,
                    response_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySpotOrderbookResponse.SerializeToString,
            ),
            'TraderSpotOrders': grpc.unary_unary_rpc_method_handler(
                    servicer.TraderSpotOrders,
                    request_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryTraderSpotOrdersRequest.FromString,
                    response_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryTraderSpotOrdersResponse.SerializeToString,
            ),
            'DerivativeOrderbook': grpc.unary_unary_rpc_method_handler(
                    servicer.DerivativeOrderbook,
                    request_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryDerivativeOrderbookRequest.FromString,
                    response_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryDerivativeOrderbookResponse.SerializeToString,
            ),
            'TraderDerivativeOrders': grpc.unary_unary_rpc_method_handler(
                    servicer.TraderDerivativeOrders,
                    request_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryTraderDerivativeOrdersRequest.FromString,
                    response_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryTraderDerivativeOrdersResponse.SerializeToString,
            ),
            'DerivativeMarkets': grpc.unary_unary_rpc_method_handler(
                    servicer.DerivativeMarkets,
                    request_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryDerivativeMarketsRequest.FromString,
                    response_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryDerivativeMarketsResponse.SerializeToString,
            ),
            'DerivativeMarket': grpc.unary_unary_rpc_method_handler(
                    servicer.DerivativeMarket,
                    request_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryDerivativeMarketRequest.FromString,
                    response_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryDerivativeMarketResponse.SerializeToString,
            ),
            'SubaccountTradeNonce': grpc.unary_unary_rpc_method_handler(
                    servicer.SubaccountTradeNonce,
                    request_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySubaccountTradeNonceRequest.FromString,
                    response_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySubaccountTradeNonceResponse.SerializeToString,
            ),
            'ExchangeModuleState': grpc.unary_unary_rpc_method_handler(
                    servicer.ExchangeModuleState,
                    request_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryModuleStateRequest.FromString,
                    response_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryModuleStateResponse.SerializeToString,
            ),
            'Positions': grpc.unary_unary_rpc_method_handler(
                    servicer.Positions,
                    request_deserializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryPositionsRequest.FromString,
                    response_serializer=injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryPositionsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective.exchange.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def QueryExchangeParams(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.exchange.v1beta1.Query/QueryExchangeParams',
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryExchangeParamsRequest.SerializeToString,
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryExchangeParamsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubaccountDeposits(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.exchange.v1beta1.Query/SubaccountDeposits',
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySubaccountDepositsRequest.SerializeToString,
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySubaccountDepositsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubaccountDeposit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.exchange.v1beta1.Query/SubaccountDeposit',
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySubaccountDepositRequest.SerializeToString,
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySubaccountDepositResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExchangeBalances(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.exchange.v1beta1.Query/ExchangeBalances',
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryExchangeBalancesRequest.SerializeToString,
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryExchangeBalancesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SpotMarkets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.exchange.v1beta1.Query/SpotMarkets',
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySpotMarketsRequest.SerializeToString,
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySpotMarketsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SpotMarket(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.exchange.v1beta1.Query/SpotMarket',
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySpotMarketRequest.SerializeToString,
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySpotMarketResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SpotOrderbook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.exchange.v1beta1.Query/SpotOrderbook',
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySpotOrderbookRequest.SerializeToString,
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySpotOrderbookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TraderSpotOrders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.exchange.v1beta1.Query/TraderSpotOrders',
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryTraderSpotOrdersRequest.SerializeToString,
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryTraderSpotOrdersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DerivativeOrderbook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.exchange.v1beta1.Query/DerivativeOrderbook',
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryDerivativeOrderbookRequest.SerializeToString,
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryDerivativeOrderbookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TraderDerivativeOrders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.exchange.v1beta1.Query/TraderDerivativeOrders',
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryTraderDerivativeOrdersRequest.SerializeToString,
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryTraderDerivativeOrdersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DerivativeMarkets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.exchange.v1beta1.Query/DerivativeMarkets',
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryDerivativeMarketsRequest.SerializeToString,
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryDerivativeMarketsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DerivativeMarket(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.exchange.v1beta1.Query/DerivativeMarket',
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryDerivativeMarketRequest.SerializeToString,
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryDerivativeMarketResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubaccountTradeNonce(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.exchange.v1beta1.Query/SubaccountTradeNonce',
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySubaccountTradeNonceRequest.SerializeToString,
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QuerySubaccountTradeNonceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExchangeModuleState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.exchange.v1beta1.Query/ExchangeModuleState',
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryModuleStateRequest.SerializeToString,
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryModuleStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Positions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.exchange.v1beta1.Query/Positions',
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryPositionsRequest.SerializeToString,
            injective_dot_exchange_dot_v1beta1_dot_query__pb2.QueryPositionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
