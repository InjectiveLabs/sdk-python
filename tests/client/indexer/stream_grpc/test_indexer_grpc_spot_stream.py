import asyncio

import grpc
import pytest

from pyinjective.client.indexer.grpc_stream.indexer_grpc_spot_stream import IndexerGrpcSpotStream
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network
from pyinjective.proto.exchange import injective_spot_exchange_rpc_pb2 as exchange_spot_pb
from tests.client.indexer.configurable_spot_query_servicer import ConfigurableSpotQueryServicer


@pytest.fixture
def spot_servicer():
    return ConfigurableSpotQueryServicer()


class TestIndexerGrpcSpotStream:
    @pytest.mark.asyncio
    async def test_stream_markets(
        self,
        spot_servicer,
    ):
        operation_type = "update"
        timestamp = 1672218001897

        base_token_meta = exchange_spot_pb.TokenMeta(
            name="Injective Protocol",
            address="0xe28b3B32B6c345A34Ff64674606124Dd5Aceca30",
            symbol="INJ",
            logo="https://static.alchemyapi.io/images/assets/7226.png",
            decimals=18,
            updated_at=1683119359318,
        )
        quote_token_meta = exchange_spot_pb.TokenMeta(
            name="Testnet Tether USDT",
            address="0x0000000000000000000000000000000000000000",
            symbol="USDT",
            logo="https://static.alchemyapi.io/images/assets/825.png",
            decimals=6,
            updated_at=1683119359320,
        )

        market = exchange_spot_pb.SpotMarketInfo(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            market_status="active",
            ticker="INJ/USDT",
            base_denom="inj",
            base_token_meta=base_token_meta,
            quote_denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            quote_token_meta=quote_token_meta,
            maker_fee_rate="-0.0001",
            taker_fee_rate="0.001",
            service_provider_fee="0.4",
            min_price_tick_size="0.000000000000001",
            min_quantity_tick_size="1000000000000000",
        )

        spot_servicer.stream_markets_responses.append(
            exchange_spot_pb.StreamMarketsResponse(
                market=market,
                operation_type=operation_type,
                timestamp=timestamp,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcSpotStream(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = spot_servicer

        market_updates = asyncio.Queue()
        end_event = asyncio.Event()

        callback = lambda update: market_updates.put_nowait(update)
        error_callback = lambda exception: pytest.fail(str(exception))
        end_callback = lambda: end_event.set()

        asyncio.get_event_loop().create_task(
            api.stream_markets(
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
                "baseDenom": market.base_denom,
                "baseTokenMeta": {
                    "name": market.base_token_meta.name,
                    "address": market.base_token_meta.address,
                    "symbol": market.base_token_meta.symbol,
                    "logo": market.base_token_meta.logo,
                    "decimals": market.base_token_meta.decimals,
                    "updatedAt": str(market.base_token_meta.updated_at),
                },
                "quoteDenom": market.quote_denom,
                "quoteTokenMeta": {
                    "name": market.quote_token_meta.name,
                    "address": market.quote_token_meta.address,
                    "symbol": market.quote_token_meta.symbol,
                    "logo": market.quote_token_meta.logo,
                    "decimals": market.quote_token_meta.decimals,
                    "updatedAt": str(market.quote_token_meta.updated_at),
                },
                "takerFeeRate": market.taker_fee_rate,
                "makerFeeRate": market.maker_fee_rate,
                "serviceProviderFee": market.service_provider_fee,
                "minPriceTickSize": market.min_price_tick_size,
                "minQuantityTickSize": market.min_quantity_tick_size,
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
        spot_servicer,
    ):
        operation_type = "update"
        timestamp = 1672218001897
        market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"

        buy = exchange_spot_pb.PriceLevel(
            price="0.000000000014198",
            quantity="142000000000000000000",
            timestamp=1698982052141,
        )
        sell = exchange_spot_pb.PriceLevel(
            price="0.00000000095699",
            quantity="189000000000000000",
            timestamp=1698920369246,
        )

        orderbook = exchange_spot_pb.SpotLimitOrderbookV2(
            buys=[buy],
            sells=[sell],
            sequence=5506752,
            timestamp=1698982083606,
        )

        spot_servicer.stream_orderbook_v2_responses.append(
            exchange_spot_pb.StreamOrderbookV2Response(
                orderbook=orderbook,
                operation_type=operation_type,
                timestamp=timestamp,
                market_id=market_id,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcSpotStream(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = spot_servicer

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
        spot_servicer,
    ):
        operation_type = "update"
        timestamp = 1672218001897

        buy = exchange_spot_pb.PriceLevelUpdate(
            price="0.000000000014198",
            quantity="142000000000000000000",
            is_active=True,
            timestamp=1698982052141,
        )
        sell = exchange_spot_pb.PriceLevelUpdate(
            price="0.00000000095699",
            quantity="189000000000000000",
            is_active=True,
            timestamp=1698920369246,
        )

        level_updates = exchange_spot_pb.OrderbookLevelUpdates(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            sequence=5506752,
            buys=[buy],
            sells=[sell],
            updated_at=1698982083606,
        )

        spot_servicer.stream_orderbook_update_responses.append(
            exchange_spot_pb.StreamOrderbookUpdateResponse(
                orderbook_level_updates=level_updates,
                operation_type=operation_type,
                timestamp=timestamp,
                market_id=level_updates.market_id,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcSpotStream(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = spot_servicer

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
    async def test_stream_orders(
        self,
        spot_servicer,
    ):
        operation_type = "update"
        timestamp = 1672218001897

        order = exchange_spot_pb.SpotLimitOrder(
            order_hash="0x14e43adbb3302db28bcd0619068227ebca880cdd66cdfc8b4a662bcac0777849",
            order_side="buy",
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            subaccount_id="0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000004",
            price="0.000000000017541",
            quantity="50955000000000000000",
            unfilled_quantity="50955000000000000000",
            trigger_price="0",
            fee_recipient="inj1tcjf7r5vksr0g80pdcdada44teauwkkahelyfy",
            state="booked",
            created_at=1699644939364,
            updated_at=1699644939364,
            tx_hash="0x0000000000000000000000000000000000000000000000000000000000000000",
            cid="cid1",
        )

        spot_servicer.stream_orders_responses.append(
            exchange_spot_pb.StreamOrdersResponse(
                order=order,
                operation_type=operation_type,
                timestamp=timestamp,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcSpotStream(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = spot_servicer

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
                "price": order.price,
                "quantity": order.quantity,
                "unfilledQuantity": order.unfilled_quantity,
                "triggerPrice": order.trigger_price,
                "feeRecipient": order.fee_recipient,
                "state": order.state,
                "createdAt": str(order.created_at),
                "updatedAt": str(order.updated_at),
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
        spot_servicer,
    ):
        operation_type = "update"
        timestamp = 1672218001897

        price = exchange_spot_pb.PriceLevel(
            price="0.000000000006024",
            quantity="10000000000000000",
            timestamp=1677563766350,
        )

        trade = exchange_spot_pb.SpotTrade(
            order_hash="0xe549e4750287c93fcc8dec24f319c15025e07e89a8d0937be2b3865ed79d9da7",
            subaccount_id="0xc7dca7c15c364865f77a4fb67ab11dc95502e6fe000000000000000000000001",
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            trade_execution_type="limitMatchNewOrder",
            trade_direction="buy",
            price=price,
            fee="36.144",
            executed_at=1677563766350,
            fee_recipient="inj1clw20s2uxeyxtam6f7m84vgae92s9eh7vygagt",
            trade_id="8662464_1_0",
            execution_side="taker",
            cid="cid1",
        )

        spot_servicer.stream_trades_responses.append(
            exchange_spot_pb.StreamTradesResponse(
                trade=trade,
                operation_type=operation_type,
                timestamp=timestamp,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcSpotStream(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = spot_servicer

        trade_updates = asyncio.Queue()
        end_event = asyncio.Event()

        callback = lambda update: trade_updates.put_nowait(update)
        error_callback = lambda exception: pytest.fail(str(exception))
        end_callback = lambda: end_event.set()

        asyncio.get_event_loop().create_task(
            api.stream_trades(
                callback=callback,
                on_end_callback=end_callback,
                on_status_callback=error_callback,
                market_ids=[trade.market_id],
                subaccount_ids=[trade.subaccount_id],
                execution_side=trade.execution_side,
                direction=trade.trade_direction,
                execution_types=[trade.trade_execution_type],
                trade_id="7959737_3_0",
                account_address="inj1clw20s2uxeyxtam6f7m84vgae92s9eh7vygagt",
                cid=trade.cid,
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
                "tradeDirection": trade.trade_direction,
                "price": {
                    "price": price.price,
                    "quantity": price.quantity,
                    "timestamp": str(price.timestamp),
                },
                "fee": trade.fee,
                "executedAt": str(trade.executed_at),
                "feeRecipient": trade.fee_recipient,
                "tradeId": trade.trade_id,
                "executionSide": trade.execution_side,
                "cid": trade.cid,
            },
            "operationType": operation_type,
            "timestamp": str(timestamp),
        }

        first_update = await asyncio.wait_for(trade_updates.get(), timeout=1)

        assert first_update == expected_update
        assert end_event.is_set()

    @pytest.mark.asyncio
    async def test_stream_orders_history(
        self,
        spot_servicer,
    ):
        operation_type = "update"
        timestamp = 1672218001897

        order = exchange_spot_pb.SpotOrderHistory(
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
            direction="buy",
            tx_hash="0x0000000000000000000000000000000000000000000000000000000000000000",
            cid="cid1",
        )

        spot_servicer.stream_orders_history_responses.append(
            exchange_spot_pb.StreamOrdersHistoryResponse(
                order=order,
                operation_type=operation_type,
                timestamp=timestamp,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcSpotStream(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = spot_servicer

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
                "direction": order.direction,
                "txHash": order.tx_hash,
                "isActive": order.is_active,
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
        spot_servicer,
    ):
        operation_type = "update"
        timestamp = 1672218001897

        price = exchange_spot_pb.PriceLevel(
            price="0.000000000006024",
            quantity="10000000000000000",
            timestamp=1677563766350,
        )

        trade = exchange_spot_pb.SpotTrade(
            order_hash="0xe549e4750287c93fcc8dec24f319c15025e07e89a8d0937be2b3865ed79d9da7",
            subaccount_id="0xc7dca7c15c364865f77a4fb67ab11dc95502e6fe000000000000000000000001",
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            trade_execution_type="limitMatchNewOrder",
            trade_direction="buy",
            price=price,
            fee="36.144",
            executed_at=1677563766350,
            fee_recipient="inj1clw20s2uxeyxtam6f7m84vgae92s9eh7vygagt",
            trade_id="8662464_1_0",
            execution_side="taker",
            cid="cid1",
        )

        spot_servicer.stream_trades_v2_responses.append(
            exchange_spot_pb.StreamTradesV2Response(
                trade=trade,
                operation_type=operation_type,
                timestamp=timestamp,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcSpotStream(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = spot_servicer

        trade_updates = asyncio.Queue()
        end_event = asyncio.Event()

        callback = lambda update: trade_updates.put_nowait(update)
        error_callback = lambda exception: pytest.fail(str(exception))
        end_callback = lambda: end_event.set()

        asyncio.get_event_loop().create_task(
            api.stream_trades_v2(
                callback=callback,
                on_end_callback=end_callback,
                on_status_callback=error_callback,
                market_ids=[trade.market_id],
                subaccount_ids=[trade.subaccount_id],
                execution_side=trade.execution_side,
                direction=trade.trade_direction,
                execution_types=[trade.trade_execution_type],
                trade_id="7959737_3_0",
                account_address="inj1clw20s2uxeyxtam6f7m84vgae92s9eh7vygagt",
                cid=trade.cid,
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
                "tradeDirection": trade.trade_direction,
                "price": {
                    "price": price.price,
                    "quantity": price.quantity,
                    "timestamp": str(price.timestamp),
                },
                "fee": trade.fee,
                "executedAt": str(trade.executed_at),
                "feeRecipient": trade.fee_recipient,
                "tradeId": trade.trade_id,
                "executionSide": trade.execution_side,
                "cid": trade.cid,
            },
            "operationType": operation_type,
            "timestamp": str(timestamp),
        }

        first_update = await asyncio.wait_for(trade_updates.get(), timeout=1)

        assert first_update == expected_update
        assert end_event.is_set()

    async def _dummy_metadata_provider(self):
        return None
