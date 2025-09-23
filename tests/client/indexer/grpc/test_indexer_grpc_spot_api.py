import grpc
import pytest

from pyinjective.client.indexer.grpc.indexer_grpc_spot_api import IndexerGrpcSpotApi
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.exchange import injective_spot_exchange_rpc_pb2 as exchange_spot_pb
from tests.client.indexer.configurable_spot_query_servicer import ConfigurableSpotQueryServicer


@pytest.fixture
def spot_servicer():
    return ConfigurableSpotQueryServicer()


class TestIndexerGrpcSpotApi:
    @pytest.mark.asyncio
    async def test_fetch_markets(
        self,
        spot_servicer,
    ):
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
            min_notional="1000000",
        )

        spot_servicer.markets_responses.append(
            exchange_spot_pb.MarketsResponse(
                markets=[market],
            )
        )

        api = self._api_instance(servicer=spot_servicer)

        result_markets = await api.fetch_markets(
            market_statuses=[market.market_status],
            base_denom=market.base_denom,
            quote_denom=market.quote_denom,
        )
        expected_markets = {
            "markets": [
                {
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
                    "minNotional": market.min_notional,
                }
            ]
        }

        assert result_markets == expected_markets

    @pytest.mark.asyncio
    async def test_fetch_market(
        self,
        spot_servicer,
    ):
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
            min_notional="1000000",
        )

        spot_servicer.market_responses.append(
            exchange_spot_pb.MarketResponse(
                market=market,
            )
        )

        api = self._api_instance(servicer=spot_servicer)

        result_market = await api.fetch_market(market_id=market.market_id)
        expected_market = {
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
                "minNotional": market.min_notional,
            }
        }

        assert result_market == expected_market

    @pytest.mark.asyncio
    async def test_fetch_orderbook_v2(
        self,
        spot_servicer,
    ):
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
            height=1000,
        )

        spot_servicer.orderbook_v2_responses.append(
            exchange_spot_pb.OrderbookV2Response(
                orderbook=orderbook,
            )
        )

        api = self._api_instance(servicer=spot_servicer)

        result_orderbook = await api.fetch_orderbook_v2(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            depth=1,
        )
        expected_orderbook = {
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
            }
        }

        assert result_orderbook == expected_orderbook

    @pytest.mark.asyncio
    async def test_fetch_orderbooks_v2(
        self,
        spot_servicer,
    ):
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
            height=1000,
        )

        single_orderbook = exchange_spot_pb.SingleSpotLimitOrderbookV2(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            orderbook=orderbook,
        )

        spot_servicer.orderbooks_v2_responses.append(
            exchange_spot_pb.OrderbooksV2Response(
                orderbooks=[single_orderbook],
            )
        )

        api = self._api_instance(servicer=spot_servicer)

        result_orderbook = await api.fetch_orderbooks_v2(market_ids=[single_orderbook.market_id], depth=1)
        expected_orderbook = {
            "orderbooks": [
                {
                    "marketId": single_orderbook.market_id,
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
                }
            ]
        }

        assert result_orderbook == expected_orderbook

    @pytest.mark.asyncio
    async def test_fetch_orders(
        self,
        spot_servicer,
    ):
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

        paging = exchange_spot_pb.Paging(total=5, to=5, count_by_subaccount=10, next=["next1", "next2"])
        setattr(paging, "from", 1)

        spot_servicer.orders_responses.append(
            exchange_spot_pb.OrdersResponse(
                orders=[order],
                paging=paging,
            )
        )

        api = self._api_instance(servicer=spot_servicer)

        result_orders = await api.fetch_orders(
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
        )
        expected_orders = {
            "orders": [
                {
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
            ],
            "paging": {
                "total": str(paging.total),
                "from": getattr(paging, "from"),
                "to": paging.to,
                "countBySubaccount": str(paging.count_by_subaccount),
                "next": paging.next,
            },
        }

        assert result_orders == expected_orders

    @pytest.mark.asyncio
    async def test_fetch_trades(
        self,
        spot_servicer,
    ):
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

        paging = exchange_spot_pb.Paging(total=5, to=5, count_by_subaccount=10, next=["next1", "next2"])
        setattr(paging, "from", 1)

        spot_servicer.trades_responses.append(
            exchange_spot_pb.TradesResponse(
                trades=[trade],
                paging=paging,
            )
        )

        api = self._api_instance(servicer=spot_servicer)

        result_trades = await api.fetch_trades(
            market_ids=[trade.market_id],
            subaccount_ids=[trade.subaccount_id],
            execution_side=trade.execution_side,
            direction=trade.trade_direction,
            execution_types=[trade.trade_execution_type],
            trade_id=trade.trade_id,
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
        expected_trades = {
            "trades": [
                {
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
            ],
            "paging": {
                "total": str(paging.total),
                "from": getattr(paging, "from"),
                "to": paging.to,
                "countBySubaccount": str(paging.count_by_subaccount),
                "next": paging.next,
            },
        }

        assert result_trades == expected_trades

    @pytest.mark.asyncio
    async def test_fetch_subaccount_orders_list(
        self,
        spot_servicer,
    ):
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

        paging = exchange_spot_pb.Paging(total=5, to=5, count_by_subaccount=10, next=["next1", "next2"])
        setattr(paging, "from", 1)

        spot_servicer.subaccount_orders_list_responses.append(
            exchange_spot_pb.SubaccountOrdersListResponse(
                orders=[order],
                paging=paging,
            )
        )

        api = self._api_instance(servicer=spot_servicer)

        result_orders = await api.fetch_subaccount_orders_list(
            subaccount_id=order.subaccount_id,
            market_id=order.market_id,
            pagination=PaginationOption(
                skip=0,
                limit=100,
            ),
        )
        expected_orders = {
            "orders": [
                {
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
            ],
            "paging": {
                "total": str(paging.total),
                "from": getattr(paging, "from"),
                "to": paging.to,
                "countBySubaccount": str(paging.count_by_subaccount),
                "next": paging.next,
            },
        }

        assert result_orders == expected_orders

    @pytest.mark.asyncio
    async def test_fetch_subaccount_trades_list(
        self,
        spot_servicer,
    ):
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

        spot_servicer.subaccount_trades_list_responses.append(
            exchange_spot_pb.SubaccountTradesListResponse(
                trades=[trade],
            )
        )

        api = self._api_instance(servicer=spot_servicer)

        result_trades = await api.fetch_subaccount_trades_list(
            subaccount_id=trade.subaccount_id,
            market_id=trade.market_id,
            execution_type=trade.trade_execution_type,
            direction=trade.trade_direction,
            pagination=PaginationOption(
                skip=0,
                limit=100,
            ),
        )
        expected_trades = {
            "trades": [
                {
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
            ],
        }

        assert result_trades == expected_trades

    @pytest.mark.asyncio
    async def test_fetch_orders_history(
        self,
        spot_servicer,
    ):
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

        paging = exchange_spot_pb.Paging(total=5, to=5, count_by_subaccount=10, next=["next1", "next2"])
        setattr(paging, "from", 1)

        spot_servicer.orders_history_responses.append(
            exchange_spot_pb.OrdersHistoryResponse(
                orders=[order],
                paging=paging,
            )
        )

        api = self._api_instance(servicer=spot_servicer)

        result_orders = await api.fetch_orders_history(
            subaccount_id=order.subaccount_id,
            market_ids=[order.market_id],
            order_types=[order.order_type],
            direction=order.direction,
            state=order.state,
            execution_types=[order.execution_type],
            trade_id="8662464_1_0",
            active_markets_only=True,
            cid=order.cid,
            pagination=PaginationOption(
                skip=0,
                limit=100,
                start_time=1699544939364,
                end_time=1699744939364,
            ),
        )
        expected_orders = {
            "orders": [
                {
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
            ],
            "paging": {
                "total": str(paging.total),
                "from": getattr(paging, "from"),
                "to": paging.to,
                "countBySubaccount": str(paging.count_by_subaccount),
                "next": paging.next,
            },
        }

        assert result_orders == expected_orders

    @pytest.mark.asyncio
    async def test_fetch_atomic_swap_history(
        self,
        spot_servicer,
    ):
        source_coin = exchange_spot_pb.Coin(
            denom="inj",
            amount="988987297011197594664",
            usd_value="1000000000000000000000",
        )
        dest_coin = exchange_spot_pb.Coin(
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            amount="54497408",
            usd_value="200000000000000000",
        )
        fee = exchange_spot_pb.Coin(denom="inj", amount="100000")

        atomic_swap = exchange_spot_pb.AtomicSwap(
            sender="sender",
            route="route",
            source_coin=source_coin,
            dest_coin=dest_coin,
            fees=[fee],
            contract_address="contract address",
            index_by_sender=1,
            index_by_sender_contract=2,
            tx_hash="0x0000000000000000000000000000000000000000000000000000000000000000",
            executed_at=1699644939364,
            refund_amount="0",
        )
        paging = exchange_spot_pb.Paging(total=5, to=5, count_by_subaccount=10, next=["next1", "next2"])
        setattr(paging, "from", 1)

        spot_servicer.atomic_swap_history_responses.append(
            exchange_spot_pb.AtomicSwapHistoryResponse(
                data=[atomic_swap],
                paging=paging,
            )
        )

        api = self._api_instance(servicer=spot_servicer)

        result_history = await api.fetch_atomic_swap_history(
            address=atomic_swap.sender,
            contract_address=atomic_swap.contract_address,
            pagination=PaginationOption(
                skip=0,
                limit=100,
                from_number=1,
                to_number=100,
            ),
        )
        expected_history = {
            "data": [
                {
                    "contractAddress": atomic_swap.contract_address,
                    "destCoin": {"amount": dest_coin.amount, "denom": dest_coin.denom, "usdValue": dest_coin.usd_value},
                    "executedAt": str(atomic_swap.executed_at),
                    "fees": [{"amount": fee.amount, "denom": fee.denom, "usdValue": fee.usd_value}],
                    "indexBySender": atomic_swap.index_by_sender,
                    "indexBySenderContract": atomic_swap.index_by_sender_contract,
                    "refundAmount": atomic_swap.refund_amount,
                    "route": atomic_swap.route,
                    "sender": atomic_swap.sender,
                    "sourceCoin": {
                        "amount": source_coin.amount,
                        "denom": source_coin.denom,
                        "usdValue": source_coin.usd_value,
                    },
                    "txHash": atomic_swap.tx_hash,
                }
            ],
            "paging": {
                "total": str(paging.total),
                "from": getattr(paging, "from"),
                "to": paging.to,
                "countBySubaccount": str(paging.count_by_subaccount),
                "next": paging.next,
            },
        }

        assert result_history == expected_history

    @pytest.mark.asyncio
    async def test_fetch_trades_v2(
        self,
        spot_servicer,
    ):
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

        paging = exchange_spot_pb.Paging(total=5, to=5, count_by_subaccount=10, next=["next1", "next2"])
        setattr(paging, "from", 1)

        spot_servicer.trades_v2_responses.append(
            exchange_spot_pb.TradesV2Response(
                trades=[trade],
                paging=paging,
            )
        )

        api = self._api_instance(servicer=spot_servicer)

        result_trades = await api.fetch_trades_v2(
            market_ids=[trade.market_id],
            subaccount_ids=[trade.subaccount_id],
            execution_side=trade.execution_side,
            direction=trade.trade_direction,
            execution_types=[trade.trade_execution_type],
            trade_id=trade.trade_id,
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
        expected_trades = {
            "trades": [
                {
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
            ],
            "paging": {
                "total": str(paging.total),
                "from": getattr(paging, "from"),
                "to": paging.to,
                "countBySubaccount": str(paging.count_by_subaccount),
                "next": paging.next,
            },
        }

        assert result_trades == expected_trades

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = IndexerGrpcSpotApi(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer

        return api
