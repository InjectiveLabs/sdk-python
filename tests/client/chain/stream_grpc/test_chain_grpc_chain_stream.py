import asyncio
import base64

import grpc
import pytest

from pyinjective.client.chain.grpc_stream.chain_grpc_chain_stream import ChainGrpcChainStream
from pyinjective.composer import Composer
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as coin_pb
from pyinjective.proto.injective.exchange.v1beta1 import exchange_pb2 as exchange_pb
from pyinjective.proto.injective.exchange.v2 import exchange_pb2 as exchange_v2_pb, order_pb2 as order_v2_pb
from pyinjective.proto.injective.stream.v1beta1 import query_pb2 as chain_stream_pb
from pyinjective.proto.injective.stream.v2 import query_pb2 as chain_stream_v2_pb
from tests.client.chain.stream_grpc.configurable_chain_stream_query_servicer import (
    ConfigurableChainStreamQueryServicer,
    ConfigurableChainStreamV2QueryServicer,
)


@pytest.fixture
def chain_stream_servicer():
    return ConfigurableChainStreamQueryServicer()


@pytest.fixture
def chain_stream_v2_servicer():
    return ConfigurableChainStreamV2QueryServicer()


class TestChainGrpcChainStream:
    @pytest.mark.asyncio
    async def test_stream(
        self,
        chain_stream_servicer,
        chain_stream_v2_servicer,
    ):
        block_height = 19114391
        block_time = 1701457189786
        balance_coin = coin_pb.Coin(
            denom="inj",
            amount="6941221373191000000000",
        )
        bank_balance = chain_stream_pb.BankBalance(
            account="inj1qaq7mkvuc474k2nyjm2suwyes06fdm4kt26ks4",
            balances=[balance_coin],
        )
        deposit = exchange_pb.Deposit(
            available_balance="112292968420000000000000",
            total_balance="73684013968420000000000000",
        )
        subaccount_deposit = chain_stream_pb.SubaccountDeposit(
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            deposit=deposit,
        )
        subaccount_deposits = chain_stream_pb.SubaccountDeposits(
            subaccount_id="0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000007",
            deposits=[subaccount_deposit],
        )
        spot_trade = chain_stream_pb.SpotTrade(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            is_buy=False,
            executionType="LimitMatchNewOrder",
            quantity="7000000000000000000000000000000000",
            price="18215000",
            subaccount_id="0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000001",
            fee="76503000000000000000",
            order_hash=b"\xaa\xb0Ju\xa3)@\xfe\xd58N\xba\xdfG\xfd\xd8}\xe4\r\xf4\xf8a\xd9\n\xa9\xd6x+V\x9b\x02&",
            fee_recipient_address="inj13ylj40uqx338u5xtccujxystzy39q08q2gz3dx",
            cid="HBOTSIJUT60b77b9c56f0456af96c5c6c0d8",
            trade_id=f"{block_height}_0",
        )
        position_delta = exchange_pb.PositionDelta(
            is_long=True,
            execution_quantity="5000000",
            execution_price="13945600",
            execution_margin="69728000",
        )
        derivative_trade = chain_stream_pb.DerivativeTrade(
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            is_buy=False,
            executionType="LimitMatchNewOrder",
            subaccount_id="0xc7dca7c15c364865f77a4fb67ab11dc95502e6fe000000000000000000000001",
            position_delta=position_delta,
            payout="0",
            fee="76503000000000000000",
            order_hash="0xe549e4750287c93fcc8dec24f319c15025e07e89a8d0937be2b3865ed79d9da7",
            fee_recipient_address="inj1clw20s2uxeyxtam6f7m84vgae92s9eh7vygagt",
            cid="cid1",
            trade_id=f"{block_height}_1",
        )
        spot_order_info = exchange_pb.OrderInfo(
            subaccount_id="0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000004",
            fee_recipient="inj1tcjf7r5vksr0g80pdcdada44teauwkkahelyfy",
            price="18775000",
            quantity="54606542000000000000000000000000000000000",
            cid="cid2",
        )
        spot_limit_order = exchange_pb.SpotLimitOrder(
            order_info=spot_order_info,
            order_type=exchange_pb.OrderType.SELL_PO,
            fillable="54606542000000000000000000000000000000000",
            trigger_price="",
            order_hash=(
                b"\xf9\xc7\xd8v8\x84-\x9b\x99s\xf5\xdfX\xc9\xf9V\x9a\xf7\xf9\xc3\xa1\x00h\t\xc17<\xd1k\x9d\x12\xed"
            ),
        )
        spot_order = chain_stream_pb.SpotOrder(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            order=spot_limit_order,
        )
        spot_order_update = chain_stream_pb.SpotOrderUpdate(
            status="Booked",
            order_hash=(
                b"\xf9\xc7\xd8v8\x84-\x9b\x99s\xf5\xdfX\xc9\xf9V\x9a\xf7\xf9\xc3\xa1\x00h\t\xc17<\xd1k\x9d\x12\xed"
            ),
            cid="cid2",
            order=spot_order,
        )
        derivative_order_info = exchange_pb.OrderInfo(
            subaccount_id="0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000004",
            fee_recipient="inj1tcjf7r5vksr0g80pdcdada44teauwkkahelyfy",
            price="18775000",
            quantity="54606542000000000000000000000000000000000",
            cid="cid2",
        )
        derivative_limit_order = exchange_pb.DerivativeLimitOrder(
            order_info=derivative_order_info,
            order_type=exchange_pb.OrderType.SELL_PO,
            margin="54606542000000000000000000000000000000000",
            fillable="54606542000000000000000000000000000000000",
            trigger_price="",
            order_hash=b"\x03\xc9\xf8G*Q-G%\xf1\xbcF3\xe89g\xbe\xeag\xd8Y\x7f\x87\x8a\xa5\xac\x8ew\x8a\x91\xa2F",
        )
        derivative_order = chain_stream_pb.DerivativeOrder(
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            order=derivative_limit_order,
            is_market=False,
        )
        derivative_order_update = chain_stream_pb.DerivativeOrderUpdate(
            status="Booked",
            order_hash=b"\x03\xc9\xf8G*Q-G%\xf1\xbcF3\xe89g\xbe\xeag\xd8Y\x7f\x87\x8a\xa5\xac\x8ew\x8a\x91\xa2F",
            cid="cid3",
            order=derivative_order,
        )
        spot_buy_level = exchange_pb.Level(p="17280000", q="44557734000000000000000000000000000000000")
        spot_sell_level = exchange_pb.Level(
            p="18207000",
            q="22196395000000000000000000000000000000000",
        )
        spot_orderbook = chain_stream_pb.Orderbook(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            buy_levels=[spot_buy_level],
            sell_levels=[spot_sell_level],
        )
        spot_orderbook_update = chain_stream_pb.OrderbookUpdate(
            seq=6645013,
            orderbook=spot_orderbook,
        )
        derivative_buy_level = exchange_pb.Level(p="17280000", q="44557734000000000000000000000000000000000")
        derivative_sell_level = exchange_pb.Level(
            p="18207000",
            q="22196395000000000000000000000000000000000",
        )
        derivative_orderbook = chain_stream_pb.Orderbook(
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            buy_levels=[derivative_buy_level],
            sell_levels=[derivative_sell_level],
        )
        derivative_orderbook_update = chain_stream_pb.OrderbookUpdate(
            seq=6645013,
            orderbook=derivative_orderbook,
        )
        position = chain_stream_pb.Position(
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            subaccount_id="0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000004",
            isLong=True,
            quantity="22196395000000000000000000000000000000000",
            entry_price="18207000",
            margin="22196395000000000000000000000000000000000",
            cumulative_funding_entry="0",
        )
        oracle_price = chain_stream_pb.OraclePrice(
            symbol="0x41f3625971ca2ed2263e78573fe5ce23e13d2558ed3f2e47ab0f84fb9e7ae722",
            price="999910860000000000",
            type="pyth",
        )

        chain_stream_servicer.stream_responses.append(
            chain_stream_pb.StreamResponse(
                block_height=block_height,
                block_time=block_time,
                bank_balances=[bank_balance],
                subaccount_deposits=[subaccount_deposits],
                spot_trades=[spot_trade],
                derivative_trades=[derivative_trade],
                spot_orders=[spot_order_update],
                derivative_orders=[derivative_order_update],
                spot_orderbook_updates=[spot_orderbook_update],
                derivative_orderbook_updates=[derivative_orderbook_update],
                positions=[position],
                oracle_prices=[oracle_price],
            )
        )

        network = Network.devnet()
        composer = Composer(network=network.string())
        api = self._api_instance(servicer=chain_stream_servicer, servicer_v2=chain_stream_v2_servicer)

        events = asyncio.Queue()
        end_event = asyncio.Event()

        callback = lambda update: events.put_nowait(update)
        error_callback = lambda exception: pytest.fail(str(exception))
        end_callback = lambda: end_event.set()

        bank_balances_filter = composer.chain_stream_bank_balances_filter()
        subaccount_deposits_filter = composer.chain_stream_subaccount_deposits_filter()
        spot_trades_filter = composer.chain_stream_trades_filter()
        derivative_trades_filter = composer.chain_stream_trades_filter()
        spot_orders_filter = composer.chain_stream_orders_filter()
        derivative_orders_filter = composer.chain_stream_orders_filter()
        spot_orderbooks_filter = composer.chain_stream_orderbooks_filter()
        derivative_orderbooks_filter = composer.chain_stream_orderbooks_filter()
        positions_filter = composer.chain_stream_positions_filter()
        oracle_price_filter = composer.chain_stream_oracle_price_filter()

        expected_update = {
            "blockHeight": str(block_height),
            "blockTime": str(block_time),
            "bankBalances": [
                {
                    "account": bank_balance.account,
                    "balances": [
                        {
                            "denom": balance_coin.denom,
                            "amount": balance_coin.amount,
                        }
                    ],
                },
            ],
            "subaccountDeposits": [
                {
                    "subaccountId": subaccount_deposits.subaccount_id,
                    "deposits": [
                        {
                            "denom": subaccount_deposit.denom,
                            "deposit": {
                                "availableBalance": deposit.available_balance,
                                "totalBalance": deposit.total_balance,
                            },
                        }
                    ],
                }
            ],
            "spotTrades": [
                {
                    "marketId": spot_trade.market_id,
                    "isBuy": spot_trade.is_buy,
                    "executionType": spot_trade.executionType,
                    "quantity": spot_trade.quantity,
                    "price": spot_trade.price,
                    "subaccountId": spot_trade.subaccount_id,
                    "fee": spot_trade.fee,
                    "orderHash": base64.b64encode(spot_trade.order_hash).decode(),
                    "feeRecipientAddress": spot_trade.fee_recipient_address,
                    "cid": spot_trade.cid,
                    "tradeId": spot_trade.trade_id,
                },
            ],
            "derivativeTrades": [
                {
                    "marketId": derivative_trade.market_id,
                    "isBuy": derivative_trade.is_buy,
                    "executionType": derivative_trade.executionType,
                    "subaccountId": derivative_trade.subaccount_id,
                    "positionDelta": {
                        "isLong": position_delta.is_long,
                        "executionMargin": position_delta.execution_margin,
                        "executionQuantity": position_delta.execution_quantity,
                        "executionPrice": position_delta.execution_price,
                    },
                    "payout": derivative_trade.payout,
                    "fee": derivative_trade.fee,
                    "orderHash": derivative_trade.order_hash,
                    "feeRecipientAddress": derivative_trade.fee_recipient_address,
                    "cid": derivative_trade.cid,
                    "tradeId": derivative_trade.trade_id,
                }
            ],
            "spotOrders": [
                {
                    "status": "Booked",
                    "orderHash": base64.b64encode(spot_order_update.order_hash).decode(),
                    "cid": spot_order_update.cid,
                    "order": {
                        "marketId": spot_order.market_id,
                        "order": {
                            "orderInfo": {
                                "subaccountId": spot_order_info.subaccount_id,
                                "feeRecipient": spot_order_info.fee_recipient,
                                "price": spot_order_info.price,
                                "quantity": spot_order_info.quantity,
                                "cid": spot_order_info.cid,
                            },
                            "orderType": "SELL_PO",
                            "fillable": spot_limit_order.fillable,
                            "triggerPrice": spot_limit_order.trigger_price,
                            "orderHash": base64.b64encode(spot_limit_order.order_hash).decode(),
                        },
                    },
                },
            ],
            "derivativeOrders": [
                {
                    "status": "Booked",
                    "orderHash": base64.b64encode(derivative_order_update.order_hash).decode(),
                    "cid": derivative_order_update.cid,
                    "order": {
                        "marketId": derivative_order.market_id,
                        "order": {
                            "orderInfo": {
                                "subaccountId": derivative_order_info.subaccount_id,
                                "feeRecipient": derivative_order_info.fee_recipient,
                                "price": derivative_order_info.price,
                                "quantity": derivative_order_info.quantity,
                                "cid": derivative_order_info.cid,
                            },
                            "orderType": "SELL_PO",
                            "margin": derivative_limit_order.margin,
                            "fillable": derivative_limit_order.fillable,
                            "triggerPrice": derivative_limit_order.trigger_price,
                            "orderHash": base64.b64encode(derivative_limit_order.order_hash).decode(),
                        },
                        "isMarket": derivative_order.is_market,
                    },
                },
            ],
            "spotOrderbookUpdates": [
                {
                    "seq": str(spot_orderbook_update.seq),
                    "orderbook": {
                        "marketId": spot_orderbook.market_id,
                        "buyLevels": [
                            {
                                "p": spot_buy_level.p,
                                "q": spot_buy_level.q,
                            },
                        ],
                        "sellLevels": [
                            {"p": spot_sell_level.p, "q": spot_sell_level.q},
                        ],
                    },
                },
            ],
            "derivativeOrderbookUpdates": [
                {
                    "seq": str(derivative_orderbook_update.seq),
                    "orderbook": {
                        "marketId": derivative_orderbook.market_id,
                        "buyLevels": [
                            {
                                "p": derivative_buy_level.p,
                                "q": derivative_buy_level.q,
                            },
                        ],
                        "sellLevels": [
                            {
                                "p": derivative_sell_level.p,
                                "q": derivative_sell_level.q,
                            },
                        ],
                    },
                },
            ],
            "positions": [
                {
                    "marketId": position.market_id,
                    "subaccountId": position.subaccount_id,
                    "isLong": position.isLong,
                    "quantity": position.quantity,
                    "entryPrice": position.entry_price,
                    "margin": position.margin,
                    "cumulativeFundingEntry": position.cumulative_funding_entry,
                }
            ],
            "oraclePrices": [
                {
                    "symbol": oracle_price.symbol,
                    "price": oracle_price.price,
                    "type": oracle_price.type,
                },
            ],
        }

        asyncio.get_event_loop().create_task(
            api.stream(
                callback=callback,
                on_end_callback=end_callback,
                on_status_callback=error_callback,
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
        )

        first_update = await asyncio.wait_for(events.get(), timeout=1)

        assert first_update == expected_update
        assert end_event.is_set()

    @pytest.mark.asyncio
    async def test_stream_v2(
        self,
        chain_stream_servicer,
        chain_stream_v2_servicer,
    ):
        block_height = 19114391
        block_time = 1701457189786
        balance_coin = coin_pb.Coin(
            denom="inj",
            amount="6941221373191000000000",
        )
        bank_balance = chain_stream_v2_pb.BankBalance(
            account="inj1qaq7mkvuc474k2nyjm2suwyes06fdm4kt26ks4",
            balances=[balance_coin],
        )
        deposit = exchange_v2_pb.Deposit(
            available_balance="112292968420000000000000",
            total_balance="73684013968420000000000000",
        )
        subaccount_deposit = chain_stream_v2_pb.SubaccountDeposit(
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            deposit=deposit,
        )
        subaccount_deposits = chain_stream_v2_pb.SubaccountDeposits(
            subaccount_id="0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000007",
            deposits=[subaccount_deposit],
        )
        spot_trade = chain_stream_v2_pb.SpotTrade(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            is_buy=False,
            executionType="LimitMatchNewOrder",
            quantity="70",
            price="18.215",
            subaccount_id="0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000001",
            fee="7.6503",
            order_hash=b"\xaa\xb0Ju\xa3)@\xfe\xd58N\xba\xdfG\xfd\xd8}\xe4\r\xf4\xf8a\xd9\n\xa9\xd6x+V\x9b\x02&",
            fee_recipient_address="inj13ylj40uqx338u5xtccujxystzy39q08q2gz3dx",
            cid="HBOTSIJUT60b77b9c56f0456af96c5c6c0d8",
            trade_id=f"{block_height}_0",
        )
        position_delta = exchange_v2_pb.PositionDelta(
            is_long=True,
            execution_quantity="5",
            execution_price="13.9456",
            execution_margin="69.728",
        )
        derivative_trade = chain_stream_v2_pb.DerivativeTrade(
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            is_buy=False,
            executionType="LimitMatchNewOrder",
            subaccount_id="0xc7dca7c15c364865f77a4fb67ab11dc95502e6fe000000000000000000000001",
            position_delta=position_delta,
            payout="0",
            fee="7.6503",
            order_hash="0xe549e4750287c93fcc8dec24f319c15025e07e89a8d0937be2b3865ed79d9da7",
            fee_recipient_address="inj1clw20s2uxeyxtam6f7m84vgae92s9eh7vygagt",
            cid="cid1",
            trade_id=f"{block_height}_1",
        )
        spot_order_info = order_v2_pb.OrderInfo(
            subaccount_id="0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000004",
            fee_recipient="inj1tcjf7r5vksr0g80pdcdada44teauwkkahelyfy",
            price="18.775",
            quantity="54.606542",
            cid="cid2",
        )
        spot_limit_order = order_v2_pb.SpotLimitOrder(
            order_info=spot_order_info,
            order_type=order_v2_pb.OrderType.SELL_PO,
            fillable="54.606542",
            trigger_price="",
            order_hash=(
                b"\xf9\xc7\xd8v8\x84-\x9b\x99s\xf5\xdfX\xc9\xf9V\x9a\xf7\xf9\xc3\xa1\x00h\t\xc17<\xd1k\x9d\x12\xed"
            ),
        )
        spot_order = chain_stream_v2_pb.SpotOrder(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            order=spot_limit_order,
        )
        spot_order_update = chain_stream_v2_pb.SpotOrderUpdate(
            status="Booked",
            order_hash=(
                b"\xf9\xc7\xd8v8\x84-\x9b\x99s\xf5\xdfX\xc9\xf9V\x9a\xf7\xf9\xc3\xa1\x00h\t\xc17<\xd1k\x9d\x12\xed"
            ),
            cid="cid2",
            order=spot_order,
        )
        derivative_order_info = order_v2_pb.OrderInfo(
            subaccount_id="0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000004",
            fee_recipient="inj1tcjf7r5vksr0g80pdcdada44teauwkkahelyfy",
            price="18.775",
            quantity="54.606542",
            cid="cid2",
        )
        derivative_limit_order = order_v2_pb.DerivativeLimitOrder(
            order_info=derivative_order_info,
            order_type=order_v2_pb.OrderType.SELL_PO,
            margin="546.06542",
            fillable="54.606542",
            trigger_price="",
            order_hash=b"\x03\xc9\xf8G*Q-G%\xf1\xbcF3\xe89g\xbe\xeag\xd8Y\x7f\x87\x8a\xa5\xac\x8ew\x8a\x91\xa2F",
        )
        derivative_order = chain_stream_v2_pb.DerivativeOrder(
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            order=derivative_limit_order,
            is_market=False,
        )
        derivative_order_update = chain_stream_v2_pb.DerivativeOrderUpdate(
            status="Booked",
            order_hash=b"\x03\xc9\xf8G*Q-G%\xf1\xbcF3\xe89g\xbe\xeag\xd8Y\x7f\x87\x8a\xa5\xac\x8ew\x8a\x91\xa2F",
            cid="cid3",
            order=derivative_order,
        )
        spot_buy_level = exchange_v2_pb.Level(p="17.28", q="445577.34")
        spot_sell_level = exchange_v2_pb.Level(
            p="18.207",
            q="221963.95",
        )
        spot_orderbook = chain_stream_v2_pb.Orderbook(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            buy_levels=[spot_buy_level],
            sell_levels=[spot_sell_level],
        )
        spot_orderbook_update = chain_stream_v2_pb.OrderbookUpdate(
            seq=6645013,
            orderbook=spot_orderbook,
        )
        derivative_buy_level = exchange_v2_pb.Level(p="17.28", q="445577.34")
        derivative_sell_level = exchange_v2_pb.Level(
            p="18.207",
            q="221963.95",
        )
        derivative_orderbook = chain_stream_v2_pb.Orderbook(
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            buy_levels=[derivative_buy_level],
            sell_levels=[derivative_sell_level],
        )
        derivative_orderbook_update = chain_stream_v2_pb.OrderbookUpdate(
            seq=6645013,
            orderbook=derivative_orderbook,
        )
        position = chain_stream_v2_pb.Position(
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            subaccount_id="0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000004",
            isLong=True,
            quantity="221.96395",
            entry_price="18.207",
            margin="2219.6395",
            cumulative_funding_entry="0",
        )
        oracle_price = chain_stream_v2_pb.OraclePrice(
            symbol="0x41f3625971ca2ed2263e78573fe5ce23e13d2558ed3f2e47ab0f84fb9e7ae722",
            price="99.991086",
            type="pyth",
        )

        chain_stream_v2_servicer.stream_responses.append(
            chain_stream_v2_pb.StreamResponse(
                block_height=block_height,
                block_time=block_time,
                bank_balances=[bank_balance],
                subaccount_deposits=[subaccount_deposits],
                spot_trades=[spot_trade],
                derivative_trades=[derivative_trade],
                spot_orders=[spot_order_update],
                derivative_orders=[derivative_order_update],
                spot_orderbook_updates=[spot_orderbook_update],
                derivative_orderbook_updates=[derivative_orderbook_update],
                positions=[position],
                oracle_prices=[oracle_price],
            )
        )

        network = Network.devnet()
        composer = Composer(network=network.string())
        api = self._api_instance(servicer=chain_stream_servicer, servicer_v2=chain_stream_v2_servicer)

        events = asyncio.Queue()
        end_event = asyncio.Event()

        callback = lambda update: events.put_nowait(update)
        error_callback = lambda exception: pytest.fail(str(exception))
        end_callback = lambda: end_event.set()

        bank_balances_filter = composer.chain_stream_bank_balances_v2_filter()
        subaccount_deposits_filter = composer.chain_stream_subaccount_deposits_v2_filter()
        spot_trades_filter = composer.chain_stream_trades_v2_filter()
        derivative_trades_filter = composer.chain_stream_trades_v2_filter()
        spot_orders_filter = composer.chain_stream_orders_v2_filter()
        derivative_orders_filter = composer.chain_stream_orders_v2_filter()
        spot_orderbooks_filter = composer.chain_stream_orderbooks_v2_filter()
        derivative_orderbooks_filter = composer.chain_stream_orderbooks_v2_filter()
        positions_filter = composer.chain_stream_positions_v2_filter()
        oracle_price_filter = composer.chain_stream_oracle_price_v2_filter()

        expected_update = {
            "blockHeight": str(block_height),
            "blockTime": str(block_time),
            "bankBalances": [
                {
                    "account": bank_balance.account,
                    "balances": [
                        {
                            "denom": balance_coin.denom,
                            "amount": balance_coin.amount,
                        }
                    ],
                },
            ],
            "subaccountDeposits": [
                {
                    "subaccountId": subaccount_deposits.subaccount_id,
                    "deposits": [
                        {
                            "denom": subaccount_deposit.denom,
                            "deposit": {
                                "availableBalance": deposit.available_balance,
                                "totalBalance": deposit.total_balance,
                            },
                        }
                    ],
                }
            ],
            "spotTrades": [
                {
                    "marketId": spot_trade.market_id,
                    "isBuy": spot_trade.is_buy,
                    "executionType": spot_trade.executionType,
                    "quantity": spot_trade.quantity,
                    "price": spot_trade.price,
                    "subaccountId": spot_trade.subaccount_id,
                    "fee": spot_trade.fee,
                    "orderHash": base64.b64encode(spot_trade.order_hash).decode(),
                    "feeRecipientAddress": spot_trade.fee_recipient_address,
                    "cid": spot_trade.cid,
                    "tradeId": spot_trade.trade_id,
                },
            ],
            "derivativeTrades": [
                {
                    "marketId": derivative_trade.market_id,
                    "isBuy": derivative_trade.is_buy,
                    "executionType": derivative_trade.executionType,
                    "subaccountId": derivative_trade.subaccount_id,
                    "positionDelta": {
                        "isLong": position_delta.is_long,
                        "executionMargin": position_delta.execution_margin,
                        "executionQuantity": position_delta.execution_quantity,
                        "executionPrice": position_delta.execution_price,
                    },
                    "payout": derivative_trade.payout,
                    "fee": derivative_trade.fee,
                    "orderHash": derivative_trade.order_hash,
                    "feeRecipientAddress": derivative_trade.fee_recipient_address,
                    "cid": derivative_trade.cid,
                    "tradeId": derivative_trade.trade_id,
                }
            ],
            "spotOrders": [
                {
                    "status": "Booked",
                    "orderHash": base64.b64encode(spot_order_update.order_hash).decode(),
                    "cid": spot_order_update.cid,
                    "order": {
                        "marketId": spot_order.market_id,
                        "order": {
                            "orderInfo": {
                                "subaccountId": spot_order_info.subaccount_id,
                                "feeRecipient": spot_order_info.fee_recipient,
                                "price": spot_order_info.price,
                                "quantity": spot_order_info.quantity,
                                "cid": spot_order_info.cid,
                            },
                            "orderType": "SELL_PO",
                            "fillable": spot_limit_order.fillable,
                            "triggerPrice": spot_limit_order.trigger_price,
                            "orderHash": base64.b64encode(spot_limit_order.order_hash).decode(),
                        },
                    },
                },
            ],
            "derivativeOrders": [
                {
                    "status": "Booked",
                    "orderHash": base64.b64encode(derivative_order_update.order_hash).decode(),
                    "cid": derivative_order_update.cid,
                    "order": {
                        "marketId": derivative_order.market_id,
                        "order": {
                            "orderInfo": {
                                "subaccountId": derivative_order_info.subaccount_id,
                                "feeRecipient": derivative_order_info.fee_recipient,
                                "price": derivative_order_info.price,
                                "quantity": derivative_order_info.quantity,
                                "cid": derivative_order_info.cid,
                            },
                            "orderType": "SELL_PO",
                            "margin": derivative_limit_order.margin,
                            "fillable": derivative_limit_order.fillable,
                            "triggerPrice": derivative_limit_order.trigger_price,
                            "orderHash": base64.b64encode(derivative_limit_order.order_hash).decode(),
                        },
                        "isMarket": derivative_order.is_market,
                    },
                },
            ],
            "spotOrderbookUpdates": [
                {
                    "seq": str(spot_orderbook_update.seq),
                    "orderbook": {
                        "marketId": spot_orderbook.market_id,
                        "buyLevels": [
                            {
                                "p": spot_buy_level.p,
                                "q": spot_buy_level.q,
                            },
                        ],
                        "sellLevels": [
                            {"p": spot_sell_level.p, "q": spot_sell_level.q},
                        ],
                    },
                },
            ],
            "derivativeOrderbookUpdates": [
                {
                    "seq": str(derivative_orderbook_update.seq),
                    "orderbook": {
                        "marketId": derivative_orderbook.market_id,
                        "buyLevels": [
                            {
                                "p": derivative_buy_level.p,
                                "q": derivative_buy_level.q,
                            },
                        ],
                        "sellLevels": [
                            {
                                "p": derivative_sell_level.p,
                                "q": derivative_sell_level.q,
                            },
                        ],
                    },
                },
            ],
            "positions": [
                {
                    "marketId": position.market_id,
                    "subaccountId": position.subaccount_id,
                    "isLong": position.isLong,
                    "quantity": position.quantity,
                    "entryPrice": position.entry_price,
                    "margin": position.margin,
                    "cumulativeFundingEntry": position.cumulative_funding_entry,
                }
            ],
            "oraclePrices": [
                {
                    "symbol": oracle_price.symbol,
                    "price": oracle_price.price,
                    "type": oracle_price.type,
                },
            ],
        }

        asyncio.get_event_loop().create_task(
            api.stream_v2(
                callback=callback,
                on_end_callback=end_callback,
                on_status_callback=error_callback,
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
        )

        first_update = await asyncio.wait_for(events.get(), timeout=1)

        assert first_update == expected_update
        assert end_event.is_set()

    def _api_instance(self, servicer, servicer_v2):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = ChainGrpcChainStream(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer
        api._stub_v2 = servicer_v2

        return api
