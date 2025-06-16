from typing import Any, Callable, Dict, List, Optional
from warnings import warn

from pyinjective.client.indexer.grpc.indexer_grpc_account_api import IndexerGrpcAccountApi
from pyinjective.client.indexer.grpc.indexer_grpc_auction_api import IndexerGrpcAuctionApi
from pyinjective.client.indexer.grpc.indexer_grpc_derivative_api import IndexerGrpcDerivativeApi
from pyinjective.client.indexer.grpc.indexer_grpc_explorer_api import IndexerGrpcExplorerApi
from pyinjective.client.indexer.grpc.indexer_grpc_insurance_api import IndexerGrpcInsuranceApi
from pyinjective.client.indexer.grpc.indexer_grpc_meta_api import IndexerGrpcMetaApi
from pyinjective.client.indexer.grpc.indexer_grpc_oracle_api import IndexerGrpcOracleApi
from pyinjective.client.indexer.grpc.indexer_grpc_portfolio_api import IndexerGrpcPortfolioApi
from pyinjective.client.indexer.grpc.indexer_grpc_spot_api import IndexerGrpcSpotApi
from pyinjective.client.indexer.grpc_stream.indexer_grpc_account_stream import IndexerGrpcAccountStream
from pyinjective.client.indexer.grpc_stream.indexer_grpc_auction_stream import IndexerGrpcAuctionStream
from pyinjective.client.indexer.grpc_stream.indexer_grpc_derivative_stream import IndexerGrpcDerivativeStream
from pyinjective.client.indexer.grpc_stream.indexer_grpc_explorer_stream import IndexerGrpcExplorerStream
from pyinjective.client.indexer.grpc_stream.indexer_grpc_meta_stream import IndexerGrpcMetaStream
from pyinjective.client.indexer.grpc_stream.indexer_grpc_oracle_stream import IndexerGrpcOracleStream
from pyinjective.client.indexer.grpc_stream.indexer_grpc_portfolio_stream import IndexerGrpcPortfolioStream
from pyinjective.client.indexer.grpc_stream.indexer_grpc_spot_stream import IndexerGrpcSpotStream
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network
from pyinjective.proto.exchange import injective_oracle_rpc_pb2 as exchange_oracle_pb


class IndexerClient:
    def __init__(
        self,
        network: Network,
    ):
        self.network = network

        # exchange stubs
        self.exchange_channel = self.network.create_exchange_grpc_channel()
        # explorer stubs
        self.explorer_channel = self.network.create_explorer_grpc_channel()

        self.account_api = IndexerGrpcAccountApi(
            channel=self.exchange_channel,
            cookie_assistant=network.exchange_cookie_assistant,
        )
        self.auction_api = IndexerGrpcAuctionApi(
            channel=self.exchange_channel,
            cookie_assistant=network.exchange_cookie_assistant,
        )
        self.derivative_api = IndexerGrpcDerivativeApi(
            channel=self.exchange_channel,
            cookie_assistant=network.exchange_cookie_assistant,
        )
        self.insurance_api = IndexerGrpcInsuranceApi(
            channel=self.exchange_channel,
            cookie_assistant=network.exchange_cookie_assistant,
        )
        self.meta_api = IndexerGrpcMetaApi(
            channel=self.exchange_channel,
            cookie_assistant=network.exchange_cookie_assistant,
        )
        self.oracle_api = IndexerGrpcOracleApi(
            channel=self.exchange_channel,
            cookie_assistant=network.exchange_cookie_assistant,
        )
        self.portfolio_api = IndexerGrpcPortfolioApi(
            channel=self.exchange_channel,
            cookie_assistant=network.exchange_cookie_assistant,
        )
        self.spot_api = IndexerGrpcSpotApi(
            channel=self.exchange_channel,
            cookie_assistant=network.exchange_cookie_assistant,
        )

        self.account_stream_api = IndexerGrpcAccountStream(
            channel=self.exchange_channel,
            cookie_assistant=network.exchange_cookie_assistant,
        )
        self.auction_stream_api = IndexerGrpcAuctionStream(
            channel=self.exchange_channel,
            cookie_assistant=network.exchange_cookie_assistant,
        )
        self.derivative_stream_api = IndexerGrpcDerivativeStream(
            channel=self.exchange_channel,
            cookie_assistant=network.exchange_cookie_assistant,
        )
        self.meta_stream_api = IndexerGrpcMetaStream(
            channel=self.exchange_channel,
            cookie_assistant=network.exchange_cookie_assistant,
        )
        self.oracle_stream_api = IndexerGrpcOracleStream(
            channel=self.exchange_channel,
            cookie_assistant=network.exchange_cookie_assistant,
        )
        self.portfolio_stream_api = IndexerGrpcPortfolioStream(
            channel=self.exchange_channel,
            cookie_assistant=network.exchange_cookie_assistant,
        )
        self.spot_stream_api = IndexerGrpcSpotStream(
            channel=self.exchange_channel,
            cookie_assistant=network.exchange_cookie_assistant,
        )

        self.explorer_api = IndexerGrpcExplorerApi(
            channel=self.explorer_channel,
            cookie_assistant=network.explorer_cookie_assistant,
        )
        self.explorer_stream_api = IndexerGrpcExplorerStream(
            channel=self.explorer_channel,
            cookie_assistant=network.explorer_cookie_assistant,
        )

    async def close_exchange_channel(self):
        await self.exchange_channel.close()

    async def close_explorer_channel(self):
        await self.explorer_channel.close()

    # region account
    async def fetch_subaccount_balance(self, subaccount_id: str, denom: str) -> Dict[str, Any]:
        return await self.account_api.fetch_subaccount_balance(subaccount_id=subaccount_id, denom=denom)

    async def fetch_subaccounts_list(self, address: str) -> Dict[str, Any]:
        return await self.account_api.fetch_subaccounts_list(address=address)

    async def fetch_subaccount_balances_list(
        self, subaccount_id: str, denoms: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        return await self.account_api.fetch_subaccount_balances_list(subaccount_id=subaccount_id, denoms=denoms)

    async def fetch_subaccount_history(
        self,
        subaccount_id: str,
        denom: Optional[str] = None,
        transfer_types: Optional[List[str]] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.account_api.fetch_subaccount_history(
            subaccount_id=subaccount_id,
            denom=denom,
            transfer_types=transfer_types,
            pagination=pagination,
        )

    async def fetch_subaccount_order_summary(
        self,
        subaccount_id: str,
        market_id: Optional[str] = None,
        order_direction: Optional[str] = None,
    ) -> Dict[str, Any]:
        return await self.account_api.fetch_subaccount_order_summary(
            subaccount_id=subaccount_id,
            market_id=market_id,
            order_direction=order_direction,
        )

    async def fetch_order_states(
        self,
        spot_order_hashes: Optional[List[str]] = None,
        derivative_order_hashes: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        return await self.account_api.fetch_order_states(
            spot_order_hashes=spot_order_hashes,
            derivative_order_hashes=derivative_order_hashes,
        )

    async def fetch_portfolio(self, account_address: str) -> Dict[str, Any]:
        return await self.account_api.fetch_portfolio(account_address=account_address)

    async def fetch_rewards(self, account_address: Optional[str] = None, epoch: Optional[int] = None) -> Dict[str, Any]:
        return await self.account_api.fetch_rewards(account_address=account_address, epoch=epoch)

    async def listen_subaccount_balance_updates(
        self,
        subaccount_id: str,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        denoms: Optional[List[str]] = None,
    ):
        await self.account_stream_api.stream_subaccount_balance(
            subaccount_id=subaccount_id,
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            denoms=denoms,
        )

    # endregion

    # region auction
    async def fetch_auction(self, round: int) -> Dict[str, Any]:
        return await self.auction_api.fetch_auction(round=round)

    async def fetch_auctions(self) -> Dict[str, Any]:
        return await self.auction_api.fetch_auctions()

    async def fetch_inj_burnt(self) -> Dict[str, Any]:
        return await self.auction_api.fetch_inj_burnt()

    async def listen_bids_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
    ):
        await self.auction_stream_api.stream_bids(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
        )

    # endregion

    # region derivative
    async def fetch_derivative_market(self, market_id: str) -> Dict[str, Any]:
        return await self.derivative_api.fetch_market(market_id=market_id)

    async def fetch_derivative_markets(
        self,
        market_statuses: Optional[List[str]] = None,
        quote_denom: Optional[str] = None,
    ) -> Dict[str, Any]:
        return await self.derivative_api.fetch_markets(
            market_statuses=market_statuses,
            quote_denom=quote_denom,
        )

    async def fetch_derivative_orderbook_v2(self, market_id: str, depth: int) -> Dict[str, Any]:
        return await self.derivative_api.fetch_orderbook_v2(market_id=market_id, depth=depth)

    async def fetch_derivative_orderbooks_v2(self, market_ids: List[str], depth: int) -> Dict[str, Any]:
        return await self.derivative_api.fetch_orderbooks_v2(market_ids=market_ids, depth=depth)

    async def fetch_derivative_orders(
        self,
        market_ids: Optional[List[str]] = None,
        order_side: Optional[str] = None,
        subaccount_id: Optional[str] = None,
        is_conditional: Optional[str] = None,
        order_type: Optional[str] = None,
        include_inactive: Optional[bool] = None,
        subaccount_total_orders: Optional[bool] = None,
        trade_id: Optional[str] = None,
        cid: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.derivative_api.fetch_orders(
            market_ids=market_ids,
            order_side=order_side,
            subaccount_id=subaccount_id,
            is_conditional=is_conditional,
            order_type=order_type,
            include_inactive=include_inactive,
            subaccount_total_orders=subaccount_total_orders,
            trade_id=trade_id,
            cid=cid,
            pagination=pagination,
        )

    async def fetch_derivative_orders_history(
        self,
        subaccount_id: Optional[str] = None,
        market_ids: Optional[List[str]] = None,
        order_types: Optional[List[str]] = None,
        direction: Optional[str] = None,
        is_conditional: Optional[str] = None,
        state: Optional[str] = None,
        execution_types: Optional[List[str]] = None,
        trade_id: Optional[str] = None,
        active_markets_only: Optional[bool] = None,
        cid: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.derivative_api.fetch_orders_history(
            subaccount_id=subaccount_id,
            market_ids=market_ids,
            order_types=order_types,
            direction=direction,
            is_conditional=is_conditional,
            state=state,
            execution_types=execution_types,
            trade_id=trade_id,
            active_markets_only=active_markets_only,
            cid=cid,
            pagination=pagination,
        )

    async def fetch_derivative_trades(
        self,
        market_ids: Optional[List[str]] = None,
        subaccount_ids: Optional[List[str]] = None,
        execution_side: Optional[str] = None,
        direction: Optional[str] = None,
        execution_types: Optional[List[str]] = None,
        trade_id: Optional[str] = None,
        account_address: Optional[str] = None,
        cid: Optional[str] = None,
        fee_recipient: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.derivative_api.fetch_trades_v2(
            market_ids=market_ids,
            subaccount_ids=subaccount_ids,
            execution_side=execution_side,
            direction=direction,
            execution_types=execution_types,
            trade_id=trade_id,
            account_address=account_address,
            cid=cid,
            fee_recipient=fee_recipient,
            pagination=pagination,
        )

    async def fetch_derivative_positions_v2(
        self,
        market_ids: Optional[List[str]] = None,
        subaccount_id: Optional[str] = None,
        direction: Optional[str] = None,
        subaccount_total_positions: Optional[bool] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.derivative_api.fetch_positions_v2(
            market_ids=market_ids,
            subaccount_id=subaccount_id,
            direction=direction,
            subaccount_total_positions=subaccount_total_positions,
            pagination=pagination,
        )

    async def fetch_derivative_liquidable_positions(
        self,
        market_id: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.derivative_api.fetch_liquidable_positions(
            market_id=market_id,
            pagination=pagination,
        )

    async def fetch_derivative_subaccount_orders_list(
        self,
        subaccount_id: str,
        market_id: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.derivative_api.fetch_subaccount_orders_list(
            subaccount_id=subaccount_id, market_id=market_id, pagination=pagination
        )

    async def fetch_derivative_subaccount_trades_list(
        self,
        subaccount_id: str,
        market_id: Optional[str] = None,
        execution_type: Optional[str] = None,
        direction: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.derivative_api.fetch_subaccount_trades_list(
            subaccount_id=subaccount_id,
            market_id=market_id,
            execution_type=execution_type,
            direction=direction,
            pagination=pagination,
        )

    async def fetch_funding_payments(
        self,
        market_ids: Optional[List[str]] = None,
        subaccount_id: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.derivative_api.fetch_funding_payments(
            market_ids=market_ids, subaccount_id=subaccount_id, pagination=pagination
        )

    async def fetch_funding_rates(
        self,
        market_id: str,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.derivative_api.fetch_funding_rates(market_id=market_id, pagination=pagination)

    async def fetch_binary_options_markets(
        self,
        market_status: Optional[str] = None,
        quote_denom: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.derivative_api.fetch_binary_options_markets(
            market_status=market_status,
            quote_denom=quote_denom,
            pagination=pagination,
        )

    async def fetch_binary_options_market(self, market_id: str) -> Dict[str, Any]:
        return await self.derivative_api.fetch_binary_options_market(market_id=market_id)

    async def fetch_open_interest(self, market_ids: List[str]) -> Dict[str, Any]:
        return await self.derivative_api.fetch_open_interest(market_ids=market_ids)

    async def listen_derivative_orders_history_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        subaccount_id: Optional[str] = None,
        market_id: Optional[str] = None,
        order_types: Optional[List[str]] = None,
        direction: Optional[str] = None,
        state: Optional[str] = None,
        execution_types: Optional[List[str]] = None,
    ):
        await self.derivative_stream_api.stream_orders_history(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            subaccount_id=subaccount_id,
            market_id=market_id,
            order_types=order_types,
            direction=direction,
            state=state,
            execution_types=execution_types,
        )

    async def listen_derivative_market_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        market_ids: Optional[List[str]] = None,
    ):
        await self.derivative_stream_api.stream_market(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            market_ids=market_ids,
        )

    async def listen_derivative_orderbook_snapshots(
        self,
        market_ids: List[str],
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
    ):
        await self.derivative_stream_api.stream_orderbook_v2(
            market_ids=market_ids,
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
        )

    async def listen_derivative_orderbook_updates(
        self,
        market_ids: List[str],
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
    ):
        await self.derivative_stream_api.stream_orderbook_update(
            market_ids=market_ids,
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
        )

    async def listen_derivative_orders_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        market_ids: Optional[List[str]] = None,
        order_side: Optional[str] = None,
        subaccount_id: Optional[PaginationOption] = None,
        is_conditional: Optional[str] = None,
        order_type: Optional[str] = None,
        include_inactive: Optional[bool] = None,
        subaccount_total_orders: Optional[bool] = None,
        trade_id: Optional[str] = None,
        cid: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ):
        await self.derivative_stream_api.stream_orders(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            market_ids=market_ids,
            order_side=order_side,
            subaccount_id=subaccount_id,
            is_conditional=is_conditional,
            order_type=order_type,
            include_inactive=include_inactive,
            subaccount_total_orders=subaccount_total_orders,
            trade_id=trade_id,
            cid=cid,
            pagination=pagination,
        )

    async def listen_derivative_trades_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        market_ids: Optional[List[str]] = None,
        execution_side: Optional[str] = None,
        direction: Optional[str] = None,
        subaccount_ids: Optional[List[str]] = None,
        execution_types: Optional[List[str]] = None,
        trade_id: Optional[str] = None,
        account_address: Optional[str] = None,
        cid: Optional[str] = None,
        fee_recipient: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ):
        return await self.derivative_stream_api.stream_trades_v2(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            market_ids=market_ids,
            subaccount_ids=subaccount_ids,
            execution_side=execution_side,
            direction=direction,
            execution_types=execution_types,
            trade_id=trade_id,
            account_address=account_address,
            cid=cid,
            fee_recipient=fee_recipient,
            pagination=pagination,
        )

    async def listen_derivative_positions_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        market_ids: Optional[List[str]] = None,
        subaccount_ids: Optional[List[str]] = None,
    ):
        """
        This method is deprecated and will be removed soon. Please use `listen_derivative_positions_v2_updates` instead.
        """
        warn(
            "This method is deprecated. Use listen_derivative_positions_v2_updates instead",
            DeprecationWarning,
            stacklevel=2,
        )
        await self.derivative_stream_api.stream_positions(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            market_ids=market_ids,
            subaccount_ids=subaccount_ids,
        )

    async def listen_derivative_positions_v2_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        subaccount_id: Optional[str] = None,
        market_id: Optional[str] = None,
        market_ids: Optional[List[str]] = None,
        subaccount_ids: Optional[List[str]] = None,
        account_address: Optional[str] = None,
    ):
        """
        Listen to derivative positions V2 updates.

        :param callback: Callback function to process each update
        :param on_end_callback: Optional callback when the stream ends
        :param on_status_callback: Optional callback for handling stream status
        :param subaccount_id: Optional subaccount ID to filter positions
        :param market_id: Optional market ID to filter positions
        :param market_ids: Optional list of market IDs to filter positions
        :param subaccount_ids: Optional list of subaccount IDs to filter positions
        :param account_address: Optional account address to filter positions
        """
        await self.derivative_stream_api.stream_positions_v2(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            subaccount_id=subaccount_id,
            market_id=market_id,
            market_ids=market_ids,
            subaccount_ids=subaccount_ids,
            account_address=account_address,
        )

    # endregion

    # region insurance
    async def fetch_insurance_funds(self) -> Dict[str, Any]:
        return await self.insurance_api.fetch_insurance_funds()

    async def fetch_redemptions(
        self,
        address: Optional[str] = None,
        denom: Optional[str] = None,
        status: Optional[str] = None,
    ) -> Dict[str, Any]:
        return await self.insurance_api.fetch_redemptions(
            address=address,
            denom=denom,
            status=status,
        )

    # endregion

    # region meta
    async def fetch_ping(self) -> Dict[str, Any]:
        return await self.meta_api.fetch_ping()

    async def fetch_version(self) -> Dict[str, Any]:
        return await self.meta_api.fetch_version()

    async def fetch_info(self) -> Dict[str, Any]:
        return await self.meta_api.fetch_info()

    async def listen_keepalive(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
    ):
        await self.meta_stream_api.stream_keepalive(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
        )

    # endregion

    # region oracle
    async def fetch_oracle_price(
        self,
        base_symbol: Optional[str] = None,
        quote_symbol: Optional[str] = None,
        oracle_type: Optional[str] = None,
        oracle_scale_factor: Optional[int] = None,
    ) -> Dict[str, Any]:
        return await self.oracle_api.fetch_oracle_price(
            base_symbol=base_symbol,
            quote_symbol=quote_symbol,
            oracle_type=oracle_type,
            oracle_scale_factor=oracle_scale_factor,
        )

    def oracle_price_v2_filter(
        self,
        base_symbol: Optional[str] = None,
        quote_symbol: Optional[str] = None,
        oracle_type: Optional[str] = None,
        oracle_scale_factor: Optional[int] = None,
    ) -> exchange_oracle_pb.PricePayloadV2:
        return exchange_oracle_pb.PricePayloadV2(
            base_symbol=base_symbol,
            quote_symbol=quote_symbol,
            oracle_type=oracle_type,
            oracle_scale_factor=oracle_scale_factor,
        )

    async def fetch_oracle_price_v2(self, filters: List[exchange_oracle_pb.PricePayloadV2]) -> Dict[str, Any]:
        return await self.oracle_api.fetch_oracle_price_v2(filters=filters)

    async def fetch_oracle_list(self) -> Dict[str, Any]:
        return await self.oracle_api.fetch_oracle_list()

    async def listen_oracle_prices_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        base_symbol: Optional[str] = None,
        quote_symbol: Optional[str] = None,
        oracle_type: Optional[str] = None,
    ):
        await self.oracle_stream_api.stream_oracle_prices(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            base_symbol=base_symbol,
            quote_symbol=quote_symbol,
            oracle_type=oracle_type,
        )

    # endregion

    # region portfolio
    async def fetch_account_portfolio_balances(
        self, account_address: str, usd: Optional[bool] = None
    ) -> Dict[str, Any]:
        return await self.portfolio_api.fetch_account_portfolio_balances(account_address=account_address, usd=usd)

    async def listen_account_portfolio_updates(
        self,
        account_address: str,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        subaccount_id: Optional[str] = None,
        update_type: Optional[str] = None,
    ):
        await self.portfolio_stream_api.stream_account_portfolio(
            account_address=account_address,
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            subaccount_id=subaccount_id,
            update_type=update_type,
        )

    # endregion

    # region spot
    async def fetch_spot_market(self, market_id: str) -> Dict[str, Any]:
        return await self.spot_api.fetch_market(market_id=market_id)

    async def fetch_spot_markets(
        self,
        market_statuses: Optional[List[str]] = None,
        base_denom: Optional[str] = None,
        quote_denom: Optional[str] = None,
    ) -> Dict[str, Any]:
        return await self.spot_api.fetch_markets(
            market_statuses=market_statuses, base_denom=base_denom, quote_denom=quote_denom
        )

    async def fetch_spot_orderbook_v2(self, market_id: str, depth: int) -> Dict[str, Any]:
        return await self.spot_api.fetch_orderbook_v2(market_id=market_id, depth=depth)

    async def fetch_spot_orderbooks_v2(self, market_ids: List[str], depth: int) -> Dict[str, Any]:
        return await self.spot_api.fetch_orderbooks_v2(market_ids=market_ids, depth=depth)

    async def fetch_spot_orders(
        self,
        market_ids: Optional[List[str]] = None,
        order_side: Optional[str] = None,
        subaccount_id: Optional[str] = None,
        include_inactive: Optional[bool] = None,
        subaccount_total_orders: Optional[bool] = None,
        trade_id: Optional[str] = None,
        cid: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.spot_api.fetch_orders(
            market_ids=market_ids,
            order_side=order_side,
            subaccount_id=subaccount_id,
            include_inactive=include_inactive,
            subaccount_total_orders=subaccount_total_orders,
            trade_id=trade_id,
            cid=cid,
            pagination=pagination,
        )

    async def fetch_spot_orders_history(
        self,
        subaccount_id: Optional[str] = None,
        market_ids: Optional[List[str]] = None,
        order_types: Optional[List[str]] = None,
        direction: Optional[str] = None,
        state: Optional[str] = None,
        execution_types: Optional[List[str]] = None,
        trade_id: Optional[str] = None,
        active_markets_only: Optional[bool] = None,
        cid: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.spot_api.fetch_orders_history(
            subaccount_id=subaccount_id,
            market_ids=market_ids,
            order_types=order_types,
            direction=direction,
            state=state,
            execution_types=execution_types,
            trade_id=trade_id,
            active_markets_only=active_markets_only,
            cid=cid,
            pagination=pagination,
        )

    async def fetch_spot_trades(
        self,
        market_ids: Optional[List[str]] = None,
        subaccount_ids: Optional[List[str]] = None,
        execution_side: Optional[str] = None,
        direction: Optional[str] = None,
        execution_types: Optional[List[str]] = None,
        trade_id: Optional[str] = None,
        account_address: Optional[str] = None,
        cid: Optional[str] = None,
        fee_recipient: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.spot_api.fetch_trades_v2(
            market_ids=market_ids,
            subaccount_ids=subaccount_ids,
            execution_side=execution_side,
            direction=direction,
            execution_types=execution_types,
            trade_id=trade_id,
            account_address=account_address,
            cid=cid,
            fee_recipient=fee_recipient,
            pagination=pagination,
        )

    async def fetch_spot_subaccount_orders_list(
        self,
        subaccount_id: str,
        market_id: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.spot_api.fetch_subaccount_orders_list(
            subaccount_id=subaccount_id, market_id=market_id, pagination=pagination
        )

    async def fetch_spot_subaccount_trades_list(
        self,
        subaccount_id: str,
        market_id: Optional[str] = None,
        execution_type: Optional[str] = None,
        direction: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.spot_api.fetch_subaccount_trades_list(
            subaccount_id=subaccount_id,
            market_id=market_id,
            execution_type=execution_type,
            direction=direction,
            pagination=pagination,
        )

    async def listen_spot_markets_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        market_ids: Optional[List[str]] = None,
    ):
        await self.spot_stream_api.stream_markets(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            market_ids=market_ids,
        )

    async def listen_spot_orderbook_snapshots(
        self,
        market_ids: List[str],
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
    ):
        await self.spot_stream_api.stream_orderbook_v2(
            market_ids=market_ids,
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
        )

    async def listen_spot_orderbook_updates(
        self,
        market_ids: List[str],
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
    ):
        await self.spot_stream_api.stream_orderbook_update(
            market_ids=market_ids,
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
        )

    async def listen_spot_orders_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        market_ids: Optional[List[str]] = None,
        order_side: Optional[str] = None,
        subaccount_id: Optional[PaginationOption] = None,
        include_inactive: Optional[bool] = None,
        subaccount_total_orders: Optional[bool] = None,
        trade_id: Optional[str] = None,
        cid: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ):
        await self.spot_stream_api.stream_orders(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            market_ids=market_ids,
            order_side=order_side,
            subaccount_id=subaccount_id,
            include_inactive=include_inactive,
            subaccount_total_orders=subaccount_total_orders,
            trade_id=trade_id,
            cid=cid,
            pagination=pagination,
        )

    async def listen_spot_orders_history_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        subaccount_id: Optional[str] = None,
        market_id: Optional[str] = None,
        order_types: Optional[List[str]] = None,
        direction: Optional[str] = None,
        state: Optional[str] = None,
        execution_types: Optional[List[str]] = None,
    ):
        await self.spot_stream_api.stream_orders_history(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            subaccount_id=subaccount_id,
            market_id=market_id,
            order_types=order_types,
            direction=direction,
            state=state,
            execution_types=execution_types,
        )

    async def listen_spot_trades_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        market_ids: Optional[List[str]] = None,
        subaccount_ids: Optional[List[str]] = None,
        execution_side: Optional[str] = None,
        direction: Optional[str] = None,
        execution_types: Optional[List[str]] = None,
        trade_id: Optional[str] = None,
        account_address: Optional[str] = None,
        cid: Optional[str] = None,
        fee_recipient: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ):
        await self.spot_stream_api.stream_trades_v2(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            market_ids=market_ids,
            subaccount_ids=subaccount_ids,
            execution_side=execution_side,
            direction=direction,
            execution_types=execution_types,
            trade_id=trade_id,
            account_address=account_address,
            cid=cid,
            fee_recipient=fee_recipient,
            pagination=pagination,
        )

    # endregion

    # region explorer
    async def fetch_tx_by_tx_hash(self, tx_hash: str) -> Dict[str, Any]:
        return await self.explorer_api.fetch_tx_by_tx_hash(tx_hash=tx_hash)

    async def fetch_account_txs(
        self,
        address: str,
        before: Optional[int] = None,
        after: Optional[int] = None,
        message_type: Optional[str] = None,
        module: Optional[str] = None,
        from_number: Optional[int] = None,
        to_number: Optional[int] = None,
        status: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.explorer_api.fetch_account_txs(
            address=address,
            before=before,
            after=after,
            message_type=message_type,
            module=module,
            from_number=from_number,
            to_number=to_number,
            status=status,
            pagination=pagination,
        )

    async def fetch_contract_txs_v2(
        self,
        address: str,
        height: Optional[int] = None,
        token: Optional[str] = None,
        status: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.explorer_api.fetch_contract_txs_v2(
            address=address,
            height=height,
            token=token,
            status=status,
            pagination=pagination,
        )

    async def fetch_blocks(
        self,
        before: Optional[int] = None,
        after: Optional[int] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.explorer_api.fetch_blocks(before=before, after=after, pagination=pagination)

    async def fetch_block(self, block_id: str) -> Dict[str, Any]:
        return await self.explorer_api.fetch_block(block_id=block_id)

    async def fetch_validators(self) -> Dict[str, Any]:
        return await self.explorer_api.fetch_validators()

    async def fetch_validator(self, address: str) -> Dict[str, Any]:
        return await self.explorer_api.fetch_validator(address)

    async def fetch_validator_uptime(self, address: str) -> Dict[str, Any]:
        return await self.explorer_api.fetch_validator_uptime(address=address)

    async def fetch_txs(
        self,
        before: Optional[int] = None,
        after: Optional[int] = None,
        message_type: Optional[str] = None,
        module: Optional[str] = None,
        from_number: Optional[int] = None,
        to_number: Optional[int] = None,
        status: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.explorer_api.fetch_txs(
            before=before,
            after=after,
            message_type=message_type,
            module=module,
            from_number=from_number,
            to_number=to_number,
            status=status,
            pagination=pagination,
        )

    async def fetch_peggy_deposit_txs(
        self,
        sender: Optional[str] = None,
        receiver: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.explorer_api.fetch_peggy_deposit_txs(
            sender=sender,
            receiver=receiver,
            pagination=pagination,
        )

    async def fetch_peggy_withdrawal_txs(
        self,
        sender: Optional[str] = None,
        receiver: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.explorer_api.fetch_peggy_withdrawal_txs(
            sender=sender,
            receiver=receiver,
            pagination=pagination,
        )

    async def fetch_ibc_transfer_txs(
        self,
        sender: Optional[str] = None,
        receiver: Optional[str] = None,
        src_channel: Optional[str] = None,
        src_port: Optional[str] = None,
        dest_channel: Optional[str] = None,
        dest_port: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.explorer_api.fetch_ibc_transfer_txs(
            sender=sender,
            receiver=receiver,
            src_channel=src_channel,
            src_port=src_port,
            dest_channel=dest_channel,
            dest_port=dest_port,
            pagination=pagination,
        )

    async def fetch_wasm_codes(
        self,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.explorer_api.fetch_wasm_codes(
            pagination=pagination,
        )

    async def fetch_wasm_code_by_id(
        self,
        code_id: int,
    ) -> Dict[str, Any]:
        return await self.explorer_api.fetch_wasm_code_by_id(code_id=code_id)

    async def fetch_wasm_contracts(
        self,
        code_id: Optional[int] = None,
        assets_only: Optional[bool] = None,
        label: Optional[str] = None,
        token: Optional[str] = None,
        lookup: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.explorer_api.fetch_wasm_contracts(
            code_id=code_id,
            assets_only=assets_only,
            label=label,
            token=token,
            lookup=lookup,
            pagination=pagination,
        )

    async def fetch_wasm_contract_by_address(
        self,
        address: str,
    ) -> Dict[str, Any]:
        return await self.explorer_api.fetch_wasm_contract_by_address(address=address)

    async def fetch_cw20_balance(
        self,
        address: str,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.explorer_api.fetch_cw20_balance(
            address=address,
            pagination=pagination,
        )

    async def fetch_relayers(
        self,
        market_ids: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        return await self.explorer_api.fetch_relayers(
            market_ids=market_ids,
        )

    async def fetch_bank_transfers(
        self,
        senders: Optional[List[str]] = None,
        recipients: Optional[List[str]] = None,
        is_community_pool_related: Optional[bool] = None,
        address: Optional[List[str]] = None,
        per_page: Optional[int] = None,
        token: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.explorer_api.fetch_bank_transfers(
            senders=senders,
            recipients=recipients,
            is_community_pool_related=is_community_pool_related,
            address=address,
            per_page=per_page,
            token=token,
            pagination=pagination,
        )

    async def listen_txs_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
    ):
        await self.explorer_stream_api.stream_txs(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
        )

    async def listen_blocks_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
    ):
        await self.explorer_stream_api.stream_blocks(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
        )

    # endregion
