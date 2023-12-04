from typing import Callable, Optional

from grpc.aio import Channel

from pyinjective.proto.injective.stream.v1beta1 import query_pb2 as chain_stream_pb, query_pb2_grpc as chain_stream_grpc
from pyinjective.utils.grpc_api_stream_assistant import GrpcApiStreamAssistant


class ChainGrpcChainStream:
    def __init__(self, channel: Channel, metadata_provider: Callable):
        self._stub = self._stub = chain_stream_grpc.StreamStub(channel)
        self._assistant = GrpcApiStreamAssistant(metadata_provider=metadata_provider)

    async def stream(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        bank_balances_filter: Optional[chain_stream_pb.BankBalancesFilter] = None,
        subaccount_deposits_filter: Optional[chain_stream_pb.SubaccountDepositsFilter] = None,
        spot_trades_filter: Optional[chain_stream_pb.TradesFilter] = None,
        derivative_trades_filter: Optional[chain_stream_pb.TradesFilter] = None,
        spot_orders_filter: Optional[chain_stream_pb.OrdersFilter] = None,
        derivative_orders_filter: Optional[chain_stream_pb.OrdersFilter] = None,
        spot_orderbooks_filter: Optional[chain_stream_pb.OrderbookFilter] = None,
        derivative_orderbooks_filter: Optional[chain_stream_pb.OrderbookFilter] = None,
        positions_filter: Optional[chain_stream_pb.PositionsFilter] = None,
        oracle_price_filter: Optional[chain_stream_pb.OraclePriceFilter] = None,
    ):
        request = chain_stream_pb.StreamRequest(
            bank_balances_filter=bank_balances_filter,
            subaccount_deposits_filter=subaccount_deposits_filter,
            spot_trades_filter=spot_trades_filter,
            derivative_trades_filter=derivative_trades_filter,
            spot_orders_filter=spot_orders_filter,
            derivative_orders_filter=derivative_orders_filter,
            spot_orderbooks_filter=spot_orderbooks_filter,
            derivative_orderbooks_filter=derivative_orderbooks_filter,
            positions_filter=positions_filter,
            oracle_price_filter=oracle_price_filter,
        )

        await self._assistant.listen_stream(
            call=self._stub.Stream,
            request=request,
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
        )
