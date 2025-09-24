import asyncio

import grpc
import pytest

from pyinjective.client.indexer.grpc_stream.indexer_grpc_derivative_stream import IndexerGrpcDerivativeStream
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.exchange import injective_derivative_exchange_rpc_pb2 as exchange_derivative_pb
from tests.client.indexer.configurable_derivative_query_servicer import ConfigurableDerivativeQueryServicer


@pytest.fixture
def derivative_servicer():
    return ConfigurableDerivativeQueryServicer()


class TestIndexerGrpcDerivativeStream:
    @pytest.mark.asyncio
    async def test_stream_market(
        self,
        derivative_servicer,
    ):
        operation_type = "update"
        timestamp = 1672218001897

        quote_token_meta = exchange_derivative_pb.TokenMeta(
            name="Testnet Tether USDT",
            address="0x0000000000000000000000000000000000000000",
            symbol="USDT",
            logo="https://static.alchemyapi.io/images/assets/825.png",
            decimals=6,
            updated_at=1683119359320,
        )
        perpetual_market_info = exchange_derivative_pb.PerpetualMarketInfo(
            hourly_funding_rate_cap="0.000625",
            hourly_interest_rate="0.00000416666",
            next_funding_timestamp=1700064000,
            funding_interval=3600,
        )
        perpetual_market_funding = exchange_derivative_pb.PerpetualMarketFunding(
            cumulative_funding="-82680.076492986572881307",
            cumulative_price="-78.41752505919454668",
            last_timestamp=1700004260,
            last_funding_rate="0.12345",
        )

        market = exchange_derivative_pb.DerivativeMarketInfo(
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            market_status="active",
            ticker="INJ/USDT PERP",
            oracle_base="0x2d9315a88f3019f8efa88dfe9c0f0843712da0bac814461e27733f6b83eb51b3",
            oracle_quote="0x1fc18861232290221461220bd4e2acd1dcdfbc89c84092c93c18bdc7756c1588",
            oracle_type="pyth",
            oracle_scale_factor=6,
            initial_margin_ratio="0.05",
            maintenance_margin_ratio="0.02",
            reduce_margin_ratio="0.3",
            quote_denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            quote_token_meta=quote_token_meta,
            maker_fee_rate="-0.0001",
            taker_fee_rate="0.001",
            service_provider_fee="0.4",
            is_perpetual=True,
            min_price_tick_size="100",
            min_quantity_tick_size="0.0001",
            perpetual_market_info=perpetual_market_info,
            perpetual_market_funding=perpetual_market_funding,
            min_notional="1000000",
        )

        derivative_servicer.stream_market_responses.append(
            exchange_derivative_pb.StreamMarketResponse(
                market=market,
                operation_type=operation_type,
                timestamp=timestamp,
            )
        )

        api = self._api_instance(servicer=derivative_servicer)

        market_updates = asyncio.Queue()
        end_event = asyncio.Event()

        callback = lambda update: market_updates.put_nowait(update)
        error_callback = lambda exception: pytest.fail(str(exception))
        end_callback = lambda: end_event.set()

        asyncio.get_event_loop().create_task(
            api.stream_market(
                callback=callback,
                on_end_callback=end_callback,
                on_status_callback=error_callback,
                market_ids=[market.market_id],
            )
        )
        expected_update = {
            "market": {
                "marketId": market.market_id,
                "marketStatus": market.market_status,
                "ticker": market.ticker,
                "oracleBase": market.oracle_base,
                "oracleQuote": market.oracle_quote,
                "oracleType": market.oracle_type,
                "oracleScaleFactor": market.oracle_scale_factor,
                "initialMarginRatio": market.initial_margin_ratio,
                "maintenanceMarginRatio": market.maintenance_margin_ratio,
                "reduceMarginRatio": market.reduce_margin_ratio,
                "quoteDenom": market.quote_denom,
                "quoteTokenMeta": {
                    "name": market.quote_token_meta.name,
                    "address": market.quote_token_meta.address,
                    "symbol": market.quote_token_meta.symbol,
                    "logo": market.quote_token_meta.logo,
                    "decimals": market.quote_token_meta.decimals,
                    "updatedAt": str(market.quote_token_meta.updated_at),
                },
                "makerFeeRate": market.maker_fee_rate,
                "takerFeeRate": market.taker_fee_rate,
                "serviceProviderFee": market.service_provider_fee,
                "isPerpetual": market.is_perpetual,
                "minPriceTickSize": market.min_price_tick_size,
                "minQuantityTickSize": market.min_quantity_tick_size,
                "minNotional": market.min_notional,
                "perpetualMarketInfo": {
                    "hourlyFundingRateCap": perpetual_market_info.hourly_funding_rate_cap,
                    "hourlyInterestRate": str(perpetual_market_info.hourly_interest_rate),
                    "nextFundingTimestamp": str(perpetual_market_info.next_funding_timestamp),
                    "fundingInterval": str(perpetual_market_info.funding_interval),
                },
                "perpetualMarketFunding": {
                    "cumulativeFunding": perpetual_market_funding.cumulative_funding,
                    "cumulativePrice": perpetual_market_funding.cumulative_price,
                    "lastTimestamp": str(perpetual_market_funding.last_timestamp),
                    "lastFundingRate": perpetual_market_funding.last_funding_rate,
                },
            },
            "operationType": operation_type,
            "timestamp": str(timestamp),
        }

        first_update = await asyncio.wait_for(market_updates.get(), timeout=1)

        assert first_update == expected_update
        assert end_event.is_set()

    @pytest.mark.asyncio
    async def test_stream_orderbook_v2(
        self,
        derivative_servicer,
    ):
        operation_type = "update"
        timestamp = 1672218001897
        market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"

        buy = exchange_derivative_pb.PriceLevel(
            price="0.000000000014198",
            quantity="142000000000000000000",
            timestamp=1698982052141,
        )
        sell = exchange_derivative_pb.PriceLevel(
            price="0.00000000095699",
            quantity="189000000000000000",
            timestamp=1698920369246,
        )

        orderbook = exchange_derivative_pb.DerivativeLimitOrderbookV2(
            buys=[buy],
            sells=[sell],
            sequence=5506752,
            timestamp=1698982083606,
            height=1000,
        )

        derivative_servicer.stream_orderbook_v2_responses.append(
            exchange_derivative_pb.StreamOrderbookV2Response(
                orderbook=orderbook,
                operation_type=operation_type,
                timestamp=timestamp,
                market_id=market_id,
            )
        )

        api = self._api_instance(servicer=derivative_servicer)

        orderbook_updates = asyncio.Queue()
        end_event = asyncio.Event()

        callback = lambda update: orderbook_updates.put_nowait(update)
        error_callback = lambda exception: pytest.fail(str(exception))
        end_callback = lambda: end_event.set()

        asyncio.get_event_loop().create_task(
            api.stream_orderbook_v2(
                callback=callback,
                on_end_callback=end_callback,
                on_status_callback=error_callback,
                market_ids=[market_id],
            )
        )
        expected_update = {
            "orderbook": {
                "buys": [
                    {
                        "price": buy.price,
                        "quantity": buy.quantity,
                        "timestamp": str(buy.timestamp),
                    }
                ],
                "sells": [
                    {
                        "price": sell.price,
                        "quantity": sell.quantity,
                        "timestamp": str(sell.timestamp),
                    }
                ],
                "sequence": str(orderbook.sequence),
                "timestamp": str(orderbook.timestamp),
                "height": str(orderbook.height),
            },
            "operationType": operation_type,
            "timestamp": str(timestamp),
            "marketId": market_id,
        }

        first_update = await asyncio.wait_for(orderbook_updates.get(), timeout=1)

        assert first_update == expected_update
        assert end_event.is_set()

    @pytest.mark.asyncio
    async def test_stream_orderbook_update(
        self,
        derivative_servicer,
    ):
        operation_type = "update"
        timestamp = 1672218001897

        buy = exchange_derivative_pb.PriceLevelUpdate(
            price="0.000000000014198",
            quantity="142000000000000000000",
            is_active=True,
            timestamp=1698982052141,
        )
        sell = exchange_derivative_pb.PriceLevelUpdate(
            price="0.00000000095699",
            quantity="189000000000000000",
            is_active=True,
            timestamp=1698920369246,
        )

        level_updates = exchange_derivative_pb.OrderbookLevelUpdates(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            sequence=5506752,
            buys=[buy],
            sells=[sell],
            updated_at=1698982083606,
        )

        derivative_servicer.stream_orderbook_update_responses.append(
            exchange_derivative_pb.StreamOrderbookUpdateResponse(
                orderbook_level_updates=level_updates,
                operation_type=operation_type,
                timestamp=timestamp,
                market_id=level_updates.market_id,
            )
        )

        api = self._api_instance(servicer=derivative_servicer)

        orderbook_updates = asyncio.Queue()
        end_event = asyncio.Event()

        callback = lambda update: orderbook_updates.put_nowait(update)
        error_callback = lambda exception: pytest.fail(str(exception))
        end_callback = lambda: end_event.set()

        asyncio.get_event_loop().create_task(
            api.stream_orderbook_update(
                market_ids=[level_updates.market_id],
                callback=callback,
                on_end_callback=end_callback,
                on_status_callback=error_callback,
            )
        )
        expected_update = {
            "orderbookLevelUpdates": {
                "marketId": level_updates.market_id,
                "sequence": str(level_updates.sequence),
                "buys": [
                    {
                        "price": buy.price,
                        "quantity": buy.quantity,
                        "isActive": buy.is_active,
                        "timestamp": str(buy.timestamp),
                    }
                ],
                "sells": [
                    {
                        "price": sell.price,
                        "quantity": sell.quantity,
                        "isActive": sell.is_active,
                        "timestamp": str(sell.timestamp),
                    }
                ],
                "updatedAt": str(level_updates.updated_at),
            },
            "operationType": operation_type,
            "timestamp": str(timestamp),
            "marketId": level_updates.market_id,
        }

        first_update = await asyncio.wait_for(orderbook_updates.get(), timeout=1)

        assert first_update == expected_update
        assert end_event.is_set()

    @pytest.mark.asyncio
    async def test_stream_positions(
        self,
        derivative_servicer,
    ):
        timestamp = 1672218001897

        position = exchange_derivative_pb.DerivativePosition(
            ticker="INJ/USDT PERP",
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            subaccount_id="0x1383dabde57e5aed55960ee43e158ae7118057d3000000000000000000000000",
            direction="short",
            quantity="0.070294765766186502",
            entry_price="15980281.340438795311756847",
            margin="561065.540974",
            liquidation_price="23492052.224777",
            mark_price="16197000",
            aggregate_reduce_only_quantity="0",
            updated_at=1700161202147,
            created_at=-62135596800000,
        )

        derivative_servicer.stream_positions_responses.append(
            exchange_derivative_pb.StreamPositionsResponse(
                position=position,
                timestamp=timestamp,
            )
        )

        api = self._api_instance(servicer=derivative_servicer)

        positions = asyncio.Queue()
        end_event = asyncio.Event()

        callback = lambda update: positions.put_nowait(update)
        error_callback = lambda exception: pytest.fail(str(exception))
        end_callback = lambda: end_event.set()

        asyncio.get_event_loop().create_task(
            api.stream_positions(
                callback=callback,
                on_end_callback=end_callback,
                on_status_callback=error_callback,
                market_ids=[position.market_id],
                subaccount_ids=[position.subaccount_id],
            )
        )
        expected_update = {
            "position": {
                "ticker": position.ticker,
                "marketId": position.market_id,
                "subaccountId": position.subaccount_id,
                "direction": position.direction,
                "quantity": position.quantity,
                "entryPrice": position.entry_price,
                "margin": position.margin,
                "liquidationPrice": position.liquidation_price,
                "markPrice": position.mark_price,
                "aggregateReduceOnlyQuantity": position.aggregate_reduce_only_quantity,
                "createdAt": str(position.created_at),
                "updatedAt": str(position.updated_at),
            },
            "timestamp": str(timestamp),
        }

        first_update = await asyncio.wait_for(positions.get(), timeout=1)

        assert first_update == expected_update
        assert end_event.is_set()

    @pytest.mark.asyncio
    async def test_stream_orders(
        self,
        derivative_servicer,
    ):
        operation_type = "update"
        timestamp = 1672218001897

        order = exchange_derivative_pb.DerivativeLimitOrder(
            order_hash="0x14e43adbb3302db28bcd0619068227ebca880cdd66cdfc8b4a662bcac0777849",
            order_side="buy",
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            subaccount_id="0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000004",
            is_reduce_only=False,
            margin="2280000000",
            price="0.000000000017541",
            quantity="50955000000000000000",
            unfilled_quantity="50955000000000000000",
            trigger_price="0",
            fee_recipient="inj1tcjf7r5vksr0g80pdcdada44teauwkkahelyfy",
            state="booked",
            created_at=1699644939364,
            updated_at=1699644939364,
            order_number=0,
            order_type="",
            is_conditional=False,
            trigger_at=0,
            placed_order_hash="",
            execution_type="",
            tx_hash="0x0000000000000000000000000000000000000000000000000000000000000000",
            cid="cid1",
        )

        derivative_servicer.stream_orders_responses.append(
            exchange_derivative_pb.StreamOrdersResponse(
                order=order,
                operation_type=operation_type,
                timestamp=timestamp,
            )
        )

        api = self._api_instance(servicer=derivative_servicer)

        orders_updates = asyncio.Queue()
        end_event = asyncio.Event()

        callback = lambda update: orders_updates.put_nowait(update)
        error_callback = lambda exception: pytest.fail(str(exception))
        end_callback = lambda: end_event.set()

        asyncio.get_event_loop().create_task(
            api.stream_orders(
                market_ids=[order.market_id],
                order_side=order.order_side,
                subaccount_id=order.subaccount_id,
                is_conditional="true",
                order_type="",
                include_inactive=True,
                subaccount_total_orders=True,
                trade_id="7959737_3_0",
                cid=order.cid,
                pagination=PaginationOption(
                    skip=0,
                    limit=100,
                    start_time=1699544939364,
                    end_time=1699744939364,
                ),
                callback=callback,
                on_end_callback=end_callback,
                on_status_callback=error_callback,
            )
        )
        expected_update = {
            "order": {
                "orderHash": order.order_hash,
                "orderSide": order.order_side,
                "marketId": order.market_id,
                "subaccountId": order.subaccount_id,
                "isReduceOnly": order.is_reduce_only,
                "margin": order.margin,
                "price": order.price,
                "quantity": order.quantity,
                "unfilledQuantity": order.unfilled_quantity,
                "triggerPrice": order.trigger_price,
                "feeRecipient": order.fee_recipient,
                "state": order.state,
                "createdAt": str(order.created_at),
                "updatedAt": str(order.updated_at),
                "orderNumber": str(order.order_number),
                "orderType": order.order_type,
                "isConditional": order.is_conditional,
                "triggerAt": str(order.trigger_at),
                "placedOrderHash": order.placed_order_hash,
                "executionType": order.execution_type,
                "txHash": order.tx_hash,
                "cid": order.cid,
            },
            "operationType": operation_type,
            "timestamp": str(timestamp),
        }

        first_update = await asyncio.wait_for(orders_updates.get(), timeout=1)

        assert first_update == expected_update
        assert end_event.is_set()

    @pytest.mark.asyncio
    async def test_stream_trades(
        self,
        derivative_servicer,
    ):
        operation_type = "update"
        timestamp = 1672218001897

        position_delta = exchange_derivative_pb.PositionDelta(
            trade_direction="buy",
            execution_price="13945600",
            execution_quantity="5",
            execution_margin="69728000",
        )

        trade = exchange_derivative_pb.DerivativeTrade(
            order_hash="0xe549e4750287c93fcc8dec24f319c15025e07e89a8d0937be2b3865ed79d9da7",
            subaccount_id="0xc7dca7c15c364865f77a4fb67ab11dc95502e6fe000000000000000000000001",
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            trade_execution_type="limitMatchNewOrder",
            is_liquidation=False,
            position_delta=position_delta,
            payout="0",
            fee="36.144",
            executed_at=1677563766350,
            fee_recipient="inj1clw20s2uxeyxtam6f7m84vgae92s9eh7vygagt",
            trade_id="8662464_1_0",
            execution_side="taker",
            cid="cid1",
            pnl="1000.123456789",
        )

        derivative_servicer.stream_trades_responses.append(
            exchange_derivative_pb.StreamTradesResponse(
                trade=trade,
                operation_type=operation_type,
                timestamp=timestamp,
            )
        )

        api = self._api_instance(servicer=derivative_servicer)

        trade_updates = asyncio.Queue()
        end_event = asyncio.Event()

        callback = lambda update: trade_updates.put_nowait(update)
        error_callback = lambda exception: pytest.fail(str(exception))
        end_callback = lambda: end_event.set()

        task = asyncio.get_event_loop().create_task(
            api.stream_trades(
                callback=callback,
                on_end_callback=end_callback,
                on_status_callback=error_callback,
                market_ids=[trade.market_id],
                subaccount_ids=[trade.subaccount_id],
                execution_side=trade.execution_side,
                direction=position_delta.trade_direction,
                execution_types=[trade.trade_execution_type],
                trade_id="7959737_3_0",
                account_address="inj1clw20s2uxeyxtam6f7m84vgae92s9eh7vygagt",
                cid=trade.cid,
                fee_recipient=trade.fee_recipient,
                pagination=PaginationOption(
                    skip=0,
                    limit=100,
                    start_time=1699544939364,
                    end_time=1699744939364,
                ),
            )
        )
        expected_update = {
            "trade": {
                "orderHash": trade.order_hash,
                "subaccountId": trade.subaccount_id,
                "marketId": trade.market_id,
                "tradeExecutionType": trade.trade_execution_type,
                "isLiquidation": trade.is_liquidation,
                "positionDelta": {
                    "tradeDirection": position_delta.trade_direction,
                    "executionPrice": position_delta.execution_price,
                    "executionQuantity": position_delta.execution_quantity,
                    "executionMargin": position_delta.execution_margin,
                },
                "payout": trade.payout,
                "fee": trade.fee,
                "executedAt": str(trade.executed_at),
                "feeRecipient": trade.fee_recipient,
                "tradeId": trade.trade_id,
                "executionSide": trade.execution_side,
                "cid": trade.cid,
                "pnl": trade.pnl,
            },
            "operationType": operation_type,
            "timestamp": str(timestamp),
        }

        first_update = await asyncio.wait_for(trade_updates.get(), timeout=1)

        task.cancel("Test finishing")
        assert first_update == expected_update
        assert end_event.is_set()

    @pytest.mark.asyncio
    async def test_stream_orders_history(
        self,
        derivative_servicer,
    ):
        operation_type = "update"
        timestamp = 1672218001897

        order = exchange_derivative_pb.DerivativeOrderHistory(
            order_hash="0x14e43adbb3302db28bcd0619068227ebca880cdd66cdfc8b4a662bcac0777849",
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            is_active=True,
            subaccount_id="0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000004",
            execution_type="limit",
            order_type="buy_po",
            price="0.000000000017541",
            trigger_price="0",
            quantity="50955000000000000000",
            filled_quantity="1000000000000000",
            state="booked",
            created_at=1699644939364,
            updated_at=1699644939364,
            is_reduce_only=False,
            direction="buy",
            is_conditional=False,
            trigger_at=0,
            placed_order_hash="",
            margin="2280000000",
            tx_hash="0x0000000000000000000000000000000000000000000000000000000000000000",
            cid="cid1",
        )

        derivative_servicer.stream_orders_history_responses.append(
            exchange_derivative_pb.StreamOrdersHistoryResponse(
                order=order,
                operation_type=operation_type,
                timestamp=timestamp,
            )
        )

        api = self._api_instance(servicer=derivative_servicer)

        orders_history_updates = asyncio.Queue()
        end_event = asyncio.Event()

        callback = lambda update: orders_history_updates.put_nowait(update)
        error_callback = lambda exception: pytest.fail(str(exception))
        end_callback = lambda: end_event.set()

        asyncio.get_event_loop().create_task(
            api.stream_orders_history(
                callback=callback,
                on_end_callback=end_callback,
                on_status_callback=error_callback,
                subaccount_id=order.subaccount_id,
                market_id=order.market_id,
                order_types=[order.order_type],
                direction=order.direction,
                state=order.state,
                execution_types=[order.execution_type],
            )
        )
        expected_update = {
            "order": {
                "orderHash": order.order_hash,
                "marketId": order.market_id,
                "isActive": order.is_active,
                "subaccountId": order.subaccount_id,
                "executionType": order.execution_type,
                "orderType": order.order_type,
                "price": order.price,
                "triggerPrice": order.trigger_price,
                "quantity": order.quantity,
                "filledQuantity": order.filled_quantity,
                "state": order.state,
                "createdAt": str(order.created_at),
                "updatedAt": str(order.updated_at),
                "isReduceOnly": order.is_reduce_only,
                "direction": order.direction,
                "isConditional": order.is_conditional,
                "triggerAt": str(order.trigger_at),
                "placedOrderHash": order.placed_order_hash,
                "margin": order.margin,
                "txHash": order.tx_hash,
                "cid": order.cid,
            },
            "operationType": operation_type,
            "timestamp": str(timestamp),
        }

        first_update = await asyncio.wait_for(orders_history_updates.get(), timeout=1)

        assert first_update == expected_update
        assert end_event.is_set()

    @pytest.mark.asyncio
    async def test_stream_trades_v2(
        self,
        derivative_servicer,
    ):
        operation_type = "update"
        timestamp = 1672218001897

        position_delta = exchange_derivative_pb.PositionDelta(
            trade_direction="buy",
            execution_price="13945600",
            execution_quantity="5",
            execution_margin="69728000",
        )

        trade = exchange_derivative_pb.DerivativeTrade(
            order_hash="0xe549e4750287c93fcc8dec24f319c15025e07e89a8d0937be2b3865ed79d9da7",
            subaccount_id="0xc7dca7c15c364865f77a4fb67ab11dc95502e6fe000000000000000000000001",
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            trade_execution_type="limitMatchNewOrder",
            is_liquidation=False,
            position_delta=position_delta,
            payout="0",
            fee="36.144",
            executed_at=1677563766350,
            fee_recipient="inj1clw20s2uxeyxtam6f7m84vgae92s9eh7vygagt",
            trade_id="8662464_1_0",
            execution_side="taker",
            cid="cid1",
            pnl="1000.123456789",
        )

        derivative_servicer.stream_trades_v2_responses.append(
            exchange_derivative_pb.StreamTradesV2Response(
                trade=trade,
                operation_type=operation_type,
                timestamp=timestamp,
            )
        )

        api = self._api_instance(servicer=derivative_servicer)

        trade_updates = asyncio.Queue()
        end_event = asyncio.Event()

        callback = lambda update: trade_updates.put_nowait(update)
        error_callback = lambda exception: pytest.fail(str(exception))
        end_callback = lambda: end_event.set()

        task = asyncio.get_event_loop().create_task(
            api.stream_trades_v2(
                callback=callback,
                on_end_callback=end_callback,
                on_status_callback=error_callback,
                market_ids=[trade.market_id],
                subaccount_ids=[trade.subaccount_id],
                execution_side=trade.execution_side,
                direction=position_delta.trade_direction,
                execution_types=[trade.trade_execution_type],
                trade_id="7959737_3_0",
                account_address="inj1clw20s2uxeyxtam6f7m84vgae92s9eh7vygagt",
                cid=trade.cid,
                fee_recipient=trade.fee_recipient,
                pagination=PaginationOption(
                    skip=0,
                    limit=100,
                    start_time=1699544939364,
                    end_time=1699744939364,
                ),
            )
        )
        expected_update = {
            "trade": {
                "orderHash": trade.order_hash,
                "subaccountId": trade.subaccount_id,
                "marketId": trade.market_id,
                "tradeExecutionType": trade.trade_execution_type,
                "isLiquidation": trade.is_liquidation,
                "positionDelta": {
                    "tradeDirection": position_delta.trade_direction,
                    "executionPrice": position_delta.execution_price,
                    "executionQuantity": position_delta.execution_quantity,
                    "executionMargin": position_delta.execution_margin,
                },
                "payout": trade.payout,
                "fee": trade.fee,
                "executedAt": str(trade.executed_at),
                "feeRecipient": trade.fee_recipient,
                "tradeId": trade.trade_id,
                "executionSide": trade.execution_side,
                "cid": trade.cid,
                "pnl": trade.pnl,
            },
            "operationType": operation_type,
            "timestamp": str(timestamp),
        }

        first_update = await asyncio.wait_for(trade_updates.get(), timeout=1)

        task.cancel("Test finishing")
        assert first_update == expected_update
        assert end_event.is_set()

    @pytest.mark.asyncio
    async def test_stream_positions_v2(
        self,
        derivative_servicer,
    ):
        timestamp = 1672218001897

        position = exchange_derivative_pb.DerivativePositionV2(
            ticker="INJ/USDT PERP",
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            subaccount_id="0x1383dabde57e5aed55960ee43e158ae7118057d3000000000000000000000000",
            direction="short",
            quantity="0.070294765766186502",
            entry_price="15980281.340438795311756847",
            margin="561065.540974",
            liquidation_price="23492052.224777",
            mark_price="16197000",
            updated_at=1700161202147,
            denom="inj",
        )

        derivative_servicer.stream_positions_v2_responses.append(
            exchange_derivative_pb.StreamPositionsV2Response(
                position=position,
                timestamp=timestamp,
            )
        )

        api = self._api_instance(servicer=derivative_servicer)

        positions = asyncio.Queue()
        end_event = asyncio.Event()

        callback = lambda update: positions.put_nowait(update)
        error_callback = lambda exception: pytest.fail(str(exception))
        end_callback = lambda: end_event.set()

        stream_task = asyncio.get_event_loop().create_task(
            api.stream_positions_v2(
                callback=callback,
                on_end_callback=end_callback,
                on_status_callback=error_callback,
                market_ids=[position.market_id],
                subaccount_ids=[position.subaccount_id],
                subaccount_id=position.subaccount_id,
                market_id=position.market_id,
                account_address="inj1address",
            )
        )
        expected_update = {
            "position": {
                "ticker": position.ticker,
                "marketId": position.market_id,
                "subaccountId": position.subaccount_id,
                "direction": position.direction,
                "quantity": position.quantity,
                "entryPrice": position.entry_price,
                "margin": position.margin,
                "liquidationPrice": position.liquidation_price,
                "markPrice": position.mark_price,
                "updatedAt": str(position.updated_at),
                "denom": position.denom,
            },
            "timestamp": str(timestamp),
        }

        first_update = await asyncio.wait_for(positions.get(), timeout=1)

        # Optional: cancel the task if needed
        stream_task.cancel()

        assert first_update == expected_update
        assert end_event.is_set()

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = IndexerGrpcDerivativeStream(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer

        return api
