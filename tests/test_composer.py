import json
from decimal import Decimal

import pytest
from google.protobuf import json_format

from pyinjective.composer import Composer
from pyinjective.constant import ADDITIONAL_CHAIN_FORMAT_DECIMALS, INJ_DECIMALS
from pyinjective.core.network import Network
from pyinjective.core.token import Token
from tests.model_fixtures.markets_fixtures import (  # noqa: F401
    btc_usdt_perp_market,
    first_match_bet_market,
    inj_token,
    inj_usdt_spot_market,
    usdt_perp_token,
    usdt_token,
)


class TestComposer:
    @pytest.fixture
    def inj_usdt_market_id(self):
        return "0xa508cb32923323679f29a032c70342c147c17d0145625922b0ef22e955c844c0"

    @pytest.fixture
    def basic_composer(self, inj_usdt_spot_market, btc_usdt_perp_market, first_match_bet_market):
        composer = Composer(
            network=Network.devnet().string(),
            spot_markets={inj_usdt_spot_market.id: inj_usdt_spot_market},
            derivative_markets={btc_usdt_perp_market.id: btc_usdt_perp_market},
            binary_option_markets={first_match_bet_market.id: first_match_bet_market},
            tokens={
                inj_usdt_spot_market.base_token.symbol: inj_usdt_spot_market.base_token,
                inj_usdt_spot_market.quote_token.symbol: inj_usdt_spot_market.quote_token,
                btc_usdt_perp_market.quote_token.symbol: btc_usdt_perp_market.quote_token,
            },
        )

        return composer

    def test_msg_create_denom(self, basic_composer: Composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        subdenom = "inj-test"
        name = "Injective Test"
        symbol = "INJTEST"
        decimals = 18

        message = basic_composer.msg_create_denom(
            sender=sender,
            subdenom=subdenom,
            name=name,
            symbol=symbol,
            decimals=decimals,
        )

        expected_message = {
            "sender": sender,
            "subdenom": subdenom,
            "name": name,
            "symbol": symbol,
            "decimals": decimals,
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )

        assert dict_message == expected_message

    def test_msg_mint(self, basic_composer: Composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        amount = basic_composer.coin(
            amount=1_000_000,
            denom="factory/inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r/inj_test",
        )

        message = basic_composer.msg_mint(
            sender=sender,
            amount=amount,
        )

        expected_message = {
            "sender": sender,
            "amount": {
                "amount": str(amount.amount),
                "denom": amount.denom,
            },
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )

        assert dict_message == expected_message

    def test_msg_burn(self, basic_composer: Composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        amount = basic_composer.coin(
            amount=100,
            denom="factory/inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r/inj_test",
        )

        message = basic_composer.msg_burn(
            sender=sender,
            amount=amount,
        )

        expected_message = {
            "sender": sender,
            "amount": {
                "amount": str(amount.amount),
                "denom": amount.denom,
            },
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )

        assert dict_message == expected_message

    def test_msg_set_denom_metadata(self, basic_composer: Composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        description = "Injective Test Token"
        subdenom = "inj_test"
        denom = "factory/inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r/inj_test"
        token_decimals = 6
        name = "Injective Test"
        symbol = "INJTEST"
        uri = "http://injective-test.com/icon.jpg"
        uri_hash = ""

        message = basic_composer.msg_set_denom_metadata(
            sender=sender,
            description=description,
            denom=denom,
            subdenom=subdenom,
            token_decimals=token_decimals,
            name=name,
            symbol=symbol,
            uri=uri,
            uri_hash=uri_hash,
        )

        expected_message = {
            "sender": sender,
            "metadata": {
                "base": denom,
                "denomUnits": [
                    {
                        "denom": denom,
                        "exponent": 0,
                        "aliases": [f"micro{subdenom}"],
                    },
                    {
                        "denom": subdenom,
                        "exponent": token_decimals,
                        "aliases": [subdenom],
                    },
                ],
                "description": description,
                "name": name,
                "symbol": symbol,
                "display": subdenom,
                "uri": uri,
                "uriHash": uri_hash,
                "decimals": token_decimals,
            },
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )

        assert dict_message == expected_message

    def test_msg_change_admin(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        denom = "factory/inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r/inj_test"
        new_admin = "inj1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqe2hm49"

        message = basic_composer.msg_change_admin(
            sender=sender,
            denom=denom,
            new_admin=new_admin,
        )

        expected_message = {
            "sender": sender,
            "denom": denom,
            "newAdmin": new_admin,
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )

        assert dict_message == expected_message

    def test_msg_execute_contract_compat(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        contract = "inj1ady3s7whq30l4fx8sj3x6muv5mx4dfdlcpv8n7"
        msg = json.dumps({"increment": {}})
        funds = "100inj,420peggy0x44C21afAaF20c270EBbF5914Cfc3b5022173FEB7"

        message = basic_composer.msg_execute_contract_compat(
            sender=sender,
            contract=contract,
            msg=msg,
            funds=funds,
        )

        expected_message = {
            "sender": sender,
            "contract": contract,
            "msg": msg,
            "funds": funds,
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )

        assert dict_message == expected_message

    def test_msg_deposit(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        subaccount_id = "0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000001"
        amount = 100
        denom = "inj"

        expected_amount = Token.convert_value_to_extended_decimal_format(value=Decimal(str(amount)))

        message = basic_composer.msg_deposit_v2(
            sender=sender,
            subaccount_id=subaccount_id,
            amount=amount,
            denom=denom,
        )

        expected_message = {
            "sender": sender,
            "subaccountId": subaccount_id,
            "amount": {
                "amount": f"{expected_amount.normalize():f}",
                "denom": denom,
            },
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_withdraw(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        subaccount_id = "0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000001"
        amount = 100
        denom = "inj"

        message = basic_composer.msg_withdraw_v2(
            sender=sender,
            subaccount_id=subaccount_id,
            amount=amount,
            denom=denom,
        )

        expected_message = {
            "sender": sender,
            "subaccountId": subaccount_id,
            "amount": {
                "amount": f"{Token.convert_value_to_extended_decimal_format(value=Decimal(str(amount))):f}",
                "denom": denom,
            },
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_instant_spot_market_launch(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        ticker = "INJ/USDT"
        base_denom = "inj"
        quote_denom = "peggy0xdAC17F958D2ee523a2206206994597C13D831ec7"
        min_price_tick_size = Decimal("0.01")
        min_quantity_tick_size = Decimal("1")
        min_notional = Decimal("2")
        base_decimals = 18
        quote_decimals = 6

        message = basic_composer.msg_instant_spot_market_launch_v2(
            sender=sender,
            ticker=ticker,
            base_denom=base_denom,
            quote_denom=quote_denom,
            min_price_tick_size=min_price_tick_size,
            min_quantity_tick_size=min_quantity_tick_size,
            min_notional=min_notional,
            base_decimals=base_decimals,
            quote_decimals=quote_decimals,
        )

        chain_min_price_tick_size = Token.convert_value_to_extended_decimal_format(value=min_price_tick_size)
        chain_min_quantity_tick_size = Token.convert_value_to_extended_decimal_format(value=min_quantity_tick_size)
        chain_min_notional = Token.convert_value_to_extended_decimal_format(value=min_notional)

        expected_message = {
            "sender": sender,
            "ticker": ticker,
            "baseDenom": base_denom,
            "quoteDenom": quote_denom,
            "minPriceTickSize": f"{chain_min_price_tick_size.normalize():f}",
            "minQuantityTickSize": f"{chain_min_quantity_tick_size.normalize():f}",
            "minNotional": f"{chain_min_notional.normalize():f}",
            "baseDecimals": base_decimals,
            "quoteDecimals": quote_decimals,
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_instant_perpetual_market_launch(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        ticker = "BTC/INJ PERP"
        quote_denom = "inj"
        oracle_base = "BTC"
        oracle_quote = "INJ"
        oracle_scale_factor = 6
        oracle_type = "Band"
        min_price_tick_size = Decimal("0.01")
        min_quantity_tick_size = Decimal("1")
        maker_fee_rate = Decimal("0.001")
        taker_fee_rate = Decimal("-0.002")
        initial_margin_ratio = Decimal("0.05")
        maintenance_margin_ratio = Decimal("0.03")
        min_notional = Decimal("2")

        expected_min_price_tick_size = min_price_tick_size * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        expected_min_quantity_tick_size = min_quantity_tick_size * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        expected_maker_fee_rate = maker_fee_rate * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        expected_taker_fee_rate = taker_fee_rate * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        expected_initial_margin_ratio = initial_margin_ratio * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        expected_maintenance_margin_ratio = maintenance_margin_ratio * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        expected_min_notional = min_notional * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        message = basic_composer.msg_instant_perpetual_market_launch_v2(
            sender=sender,
            ticker=ticker,
            quote_denom=quote_denom,
            oracle_base=oracle_base,
            oracle_quote=oracle_quote,
            oracle_scale_factor=oracle_scale_factor,
            oracle_type=oracle_type,
            maker_fee_rate=maker_fee_rate,
            taker_fee_rate=taker_fee_rate,
            initial_margin_ratio=initial_margin_ratio,
            maintenance_margin_ratio=maintenance_margin_ratio,
            min_price_tick_size=min_price_tick_size,
            min_quantity_tick_size=min_quantity_tick_size,
            min_notional=min_notional,
        )

        expected_message = {
            "sender": sender,
            "ticker": ticker,
            "quoteDenom": quote_denom,
            "oracleBase": oracle_base,
            "oracleQuote": oracle_quote,
            "oracleScaleFactor": oracle_scale_factor,
            "oracleType": oracle_type,
            "makerFeeRate": f"{expected_maker_fee_rate.normalize():f}",
            "takerFeeRate": f"{expected_taker_fee_rate.normalize():f}",
            "initialMarginRatio": f"{expected_initial_margin_ratio.normalize():f}",
            "maintenanceMarginRatio": f"{expected_maintenance_margin_ratio.normalize():f}",
            "minPriceTickSize": f"{expected_min_price_tick_size.normalize():f}",
            "minQuantityTickSize": f"{expected_min_quantity_tick_size.normalize():f}",
            "minNotional": f"{expected_min_notional.normalize():f}",
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_instant_expiry_futures_market_launch(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        ticker = "BTC/INJ PERP"
        quote_denom = "inj"
        oracle_base = "BTC"
        oracle_quote = "INJ"
        oracle_scale_factor = 6
        oracle_type = "Band"
        expiry = 1630000000
        min_price_tick_size = Decimal("0.01")
        min_quantity_tick_size = Decimal("1")
        maker_fee_rate = Decimal("0.001")
        taker_fee_rate = Decimal("-0.002")
        initial_margin_ratio = Decimal("0.05")
        maintenance_margin_ratio = Decimal("0.03")
        min_notional = Decimal("2")

        expected_min_price_tick_size = Token.convert_value_to_extended_decimal_format(value=min_price_tick_size)
        expected_min_quantity_tick_size = Token.convert_value_to_extended_decimal_format(value=min_quantity_tick_size)
        expected_maker_fee_rate = Token.convert_value_to_extended_decimal_format(value=maker_fee_rate)
        expected_taker_fee_rate = Token.convert_value_to_extended_decimal_format(value=taker_fee_rate)
        expected_initial_margin_ratio = Token.convert_value_to_extended_decimal_format(value=initial_margin_ratio)
        expected_maintenance_margin_ratio = Token.convert_value_to_extended_decimal_format(
            value=maintenance_margin_ratio
        )
        expected_min_notional = Token.convert_value_to_extended_decimal_format(value=min_notional)

        message = basic_composer.msg_instant_expiry_futures_market_launch_v2(
            sender=sender,
            ticker=ticker,
            quote_denom=quote_denom,
            oracle_base=oracle_base,
            oracle_quote=oracle_quote,
            oracle_scale_factor=oracle_scale_factor,
            oracle_type=oracle_type,
            expiry=expiry,
            maker_fee_rate=maker_fee_rate,
            taker_fee_rate=taker_fee_rate,
            initial_margin_ratio=initial_margin_ratio,
            maintenance_margin_ratio=maintenance_margin_ratio,
            min_price_tick_size=min_price_tick_size,
            min_quantity_tick_size=min_quantity_tick_size,
            min_notional=min_notional,
        )

        expected_message = {
            "sender": sender,
            "ticker": ticker,
            "quoteDenom": quote_denom,
            "oracleBase": oracle_base,
            "oracleQuote": oracle_quote,
            "oracleType": oracle_type,
            "oracleScaleFactor": oracle_scale_factor,
            "expiry": str(expiry),
            "makerFeeRate": f"{expected_maker_fee_rate.normalize():f}",
            "takerFeeRate": f"{expected_taker_fee_rate.normalize():f}",
            "initialMarginRatio": f"{expected_initial_margin_ratio.normalize():f}",
            "maintenanceMarginRatio": f"{expected_maintenance_margin_ratio.normalize():f}",
            "minPriceTickSize": f"{expected_min_price_tick_size.normalize():f}",
            "minQuantityTickSize": f"{expected_min_quantity_tick_size.normalize():f}",
            "minNotional": f"{expected_min_notional.normalize():f}",
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_spot_order(self, basic_composer):
        spot_market = list(basic_composer.spot_markets.values())[0]
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
        price = Decimal("36.1")
        quantity = Decimal("100")
        order_type = "BUY"
        cid = "test_cid"
        trigger_price = Decimal("43.5")

        order = basic_composer.spot_order(
            market_id=spot_market.id,
            subaccount_id=subaccount_id,
            fee_recipient=fee_recipient,
            price=price,
            quantity=quantity,
            order_type=order_type,
            cid=cid,
            trigger_price=trigger_price,
        )

        expected_price = spot_market.price_to_chain_format(human_readable_value=price)
        expected_quantity = spot_market.quantity_to_chain_format(human_readable_value=quantity)
        expected_trigger_price = spot_market.price_to_chain_format(human_readable_value=trigger_price)

        expected_order = {
            "marketId": spot_market.id,
            "orderInfo": {
                "subaccountId": subaccount_id,
                "feeRecipient": fee_recipient,
                "price": f"{expected_price.normalize():f}",
                "quantity": f"{expected_quantity.normalize():f}",
                "cid": cid,
            },
            "orderType": order_type,
            "triggerPrice": f"{expected_trigger_price.normalize():f}",
        }
        dict_message = json_format.MessageToDict(
            message=order,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_order

    def test_derivative_order(self, basic_composer):
        derivative_market = list(basic_composer.derivative_markets.values())[0]
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
        price = Decimal("36.1")
        quantity = Decimal("100")
        margin = price * quantity
        order_type = "BUY"
        cid = "test_cid"
        trigger_price = Decimal("43.5")

        order = basic_composer.derivative_order(
            market_id=derivative_market.id,
            subaccount_id=subaccount_id,
            fee_recipient=fee_recipient,
            price=price,
            quantity=quantity,
            margin=margin,
            order_type=order_type,
            cid=cid,
            trigger_price=trigger_price,
        )

        expected_price = derivative_market.price_to_chain_format(human_readable_value=price)
        expected_quantity = derivative_market.quantity_to_chain_format(human_readable_value=quantity)
        expected_margin = derivative_market.margin_to_chain_format(human_readable_value=margin)
        expected_trigger_price = derivative_market.price_to_chain_format(human_readable_value=trigger_price)

        expected_order = {
            "marketId": derivative_market.id,
            "orderInfo": {
                "subaccountId": subaccount_id,
                "feeRecipient": fee_recipient,
                "price": f"{expected_price.normalize():f}",
                "quantity": f"{expected_quantity.normalize():f}",
                "cid": cid,
            },
            "orderType": order_type,
            "margin": f"{expected_margin.normalize():f}",
            "triggerPrice": f"{expected_trigger_price.normalize():f}",
        }
        dict_message = json_format.MessageToDict(
            message=order,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_order

    def test_msg_create_spot_limit_order(self, basic_composer):
        spot_market = list(basic_composer.spot_markets.values())[0]
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        price = Decimal("36.1")
        quantity = Decimal("100")
        order_type = "BUY"
        cid = "test_cid"
        trigger_price = Decimal("43.5")

        message = basic_composer.msg_create_spot_limit_order_v2(
            market_id=spot_market.id,
            sender=sender,
            subaccount_id=subaccount_id,
            fee_recipient=fee_recipient,
            price=price,
            quantity=quantity,
            order_type=order_type,
            cid=cid,
            trigger_price=trigger_price,
        )

        expected_price = Token.convert_value_to_extended_decimal_format(value=price)
        expected_quantity = Token.convert_value_to_extended_decimal_format(value=quantity)
        expected_trigger_price = Token.convert_value_to_extended_decimal_format(value=trigger_price)

        assert "injective.exchange.v2.MsgCreateSpotLimitOrder" == message.DESCRIPTOR.full_name
        expected_message = {
            "sender": sender,
            "order": {
                "marketId": spot_market.id,
                "orderInfo": {
                    "subaccountId": subaccount_id,
                    "feeRecipient": fee_recipient,
                    "price": f"{expected_price.normalize():f}",
                    "quantity": f"{expected_quantity.normalize():f}",
                    "cid": cid,
                },
                "orderType": order_type,
                "triggerPrice": f"{expected_trigger_price.normalize():f}",
            },
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_batch_create_spot_limit_orders(self, basic_composer):
        spot_market = list(basic_composer.spot_markets.values())[0]
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        price = Decimal("36.1")
        quantity = Decimal("100")
        order_type = "BUY"
        cid = "test_cid"
        trigger_price = Decimal("43.5")

        order = basic_composer.create_spot_order_v2(
            market_id=spot_market.id,
            subaccount_id=subaccount_id,
            fee_recipient=fee_recipient,
            price=price,
            quantity=quantity,
            order_type=order_type,
            cid=cid,
            trigger_price=trigger_price,
        )

        message = basic_composer.msg_batch_create_spot_limit_orders_v2(
            sender=sender,
            orders=[order],
        )

        expected_message = {
            "sender": sender,
            "orders": [json_format.MessageToDict(message=order, always_print_fields_with_no_presence=True)],
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_create_spot_market_order(self, basic_composer):
        spot_market = list(basic_composer.spot_markets.values())[0]
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        price = Decimal("36.1")
        quantity = Decimal("100")
        order_type = "BUY"
        cid = "test_cid"
        trigger_price = Decimal("43.5")

        message = basic_composer.msg_create_spot_market_order_v2(
            market_id=spot_market.id,
            sender=sender,
            subaccount_id=subaccount_id,
            fee_recipient=fee_recipient,
            price=price,
            quantity=quantity,
            order_type=order_type,
            cid=cid,
            trigger_price=trigger_price,
        )

        assert "injective.exchange.v2.MsgCreateSpotMarketOrder" == message.DESCRIPTOR.full_name
        expected_message = {
            "sender": sender,
            "order": {
                "marketId": spot_market.id,
                "orderInfo": {
                    "subaccountId": subaccount_id,
                    "feeRecipient": fee_recipient,
                    "price": f"{Token.convert_value_to_extended_decimal_format(value=price).normalize():f}",
                    "quantity": f"{Token.convert_value_to_extended_decimal_format(value=quantity).normalize():f}",
                    "cid": cid,
                },
                "orderType": order_type,
                "triggerPrice": f"{Token.convert_value_to_extended_decimal_format(value=trigger_price).normalize():f}",
            },
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_cancel_spot_order(self, basic_composer):
        spot_market = list(basic_composer.spot_markets.values())[0]
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        order_hash = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        cid = "test_cid"

        message = basic_composer.msg_cancel_spot_order_v2(
            market_id=spot_market.id,
            sender=sender,
            subaccount_id=subaccount_id,
            order_hash=order_hash,
            cid=cid,
        )

        expected_message = {
            "sender": sender,
            "marketId": spot_market.id,
            "subaccountId": subaccount_id,
            "orderHash": order_hash,
            "cid": cid,
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_batch_cancel_spot_orders(self, basic_composer):
        spot_market = list(basic_composer.spot_markets.values())[0]
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"

        order_data = basic_composer.create_order_data_without_mask_v2(
            market_id=spot_market.id,
            subaccount_id=subaccount_id,
            order_hash="0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000",
        )

        message = basic_composer.msg_batch_cancel_spot_orders_v2(
            sender=sender,
            orders_data=[order_data],
        )

        assert "injective.exchange.v2.MsgBatchCancelSpotOrders" == message.DESCRIPTOR.full_name
        expected_message = {
            "sender": sender,
            "data": [json_format.MessageToDict(message=order_data, always_print_fields_with_no_presence=True)],
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_batch_update_orders(self, basic_composer):
        spot_market = list(basic_composer.spot_markets.values())[0]
        derivative_market = list(basic_composer.derivative_markets.values())[0]
        binary_options_market = list(basic_composer.binary_option_markets.values())[0]

        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        spot_market_id = spot_market.id
        derivative_market_id = derivative_market.id
        binary_options_market_id = binary_options_market.id
        spot_order_to_cancel = basic_composer.create_order_data_without_mask_v2(
            market_id=spot_market_id,
            subaccount_id=subaccount_id,
            order_hash="0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000",
        )
        derivative_order_to_cancel = basic_composer.create_order_data_without_mask_v2(
            market_id=derivative_market_id,
            subaccount_id=subaccount_id,
            order_hash="0x222daa22f60fe9f075ed0ca583459e121c23e64431c3fbffdedda04598ede0d2",
        )
        binary_options_order_to_cancel = basic_composer.create_order_data_without_mask_v2(
            market_id=binary_options_market_id,
            subaccount_id=subaccount_id,
            order_hash="0x7ee76255d7ca763c56b0eab9828fca89fdd3739645501c8a80f58b62b4f76da5",
        )
        spot_order_to_create = basic_composer.create_spot_order_v2(
            market_id=spot_market_id,
            subaccount_id=subaccount_id,
            fee_recipient="inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r",
            price=Decimal("36.1"),
            quantity=Decimal("100"),
            order_type="BUY",
            cid="test_cid",
            trigger_price=Decimal("43.5"),
        )
        derivative_order_to_create = basic_composer.create_derivative_order_v2(
            market_id=derivative_market_id,
            subaccount_id=subaccount_id,
            fee_recipient="inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r",
            price=Decimal("36.1"),
            quantity=Decimal("100"),
            margin=Decimal("36.1") * Decimal("100"),
            order_type="BUY",
        )
        binary_options_order_to_create = basic_composer.create_binary_options_order_v2(
            market_id=binary_options_market_id,
            subaccount_id=subaccount_id,
            fee_recipient="inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r",
            price=Decimal("36.1"),
            quantity=Decimal("100"),
            margin=Decimal("36.1") * Decimal("100"),
            order_type="BUY",
        )

        message = basic_composer.msg_batch_update_orders_v2(
            sender=sender,
            subaccount_id=subaccount_id,
            spot_market_ids_to_cancel_all=[spot_market_id],
            derivative_market_ids_to_cancel_all=[derivative_market_id],
            spot_orders_to_cancel=[spot_order_to_cancel],
            derivative_orders_to_cancel=[derivative_order_to_cancel],
            spot_orders_to_create=[spot_order_to_create],
            derivative_orders_to_create=[derivative_order_to_create],
            binary_options_orders_to_cancel=[binary_options_order_to_cancel],
            binary_options_market_ids_to_cancel_all=[binary_options_market_id],
            binary_options_orders_to_create=[binary_options_order_to_create],
        )

        expected_message = {
            "sender": sender,
            "subaccountId": subaccount_id,
            "spotMarketIdsToCancelAll": [spot_market_id],
            "derivativeMarketIdsToCancelAll": [derivative_market_id],
            "spotOrdersToCancel": [
                json_format.MessageToDict(message=spot_order_to_cancel, always_print_fields_with_no_presence=True)
            ],
            "derivativeOrdersToCancel": [
                json_format.MessageToDict(message=derivative_order_to_cancel, always_print_fields_with_no_presence=True)
            ],
            "spotOrdersToCreate": [
                json_format.MessageToDict(message=spot_order_to_create, always_print_fields_with_no_presence=True)
            ],
            "derivativeOrdersToCreate": [
                json_format.MessageToDict(message=derivative_order_to_create, always_print_fields_with_no_presence=True)
            ],
            "binaryOptionsOrdersToCancel": [
                json_format.MessageToDict(
                    message=binary_options_order_to_cancel, always_print_fields_with_no_presence=True
                )
            ],
            "binaryOptionsMarketIdsToCancelAll": [binary_options_market_id],
            "binaryOptionsOrdersToCreate": [
                json_format.MessageToDict(
                    message=binary_options_order_to_create, always_print_fields_with_no_presence=True
                )
            ],
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_privileged_execute_contract(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        contract_address = "inj1ady3s7whq30l4fx8sj3x6muv5mx4dfdlcpv8n7"
        data = "test_data"
        funds = "100inj,420peggy0x44C21afAaF20c270EBbF5914Cfc3b5022173FEB7"

        message = basic_composer.msg_privileged_execute_contract(
            sender=sender,
            contract_address=contract_address,
            data=data,
            funds=funds,
        )

        expected_message = {
            "sender": sender,
            "funds": funds,
            "contractAddress": contract_address,
            "data": data,
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_create_derivative_limit_order(self, basic_composer):
        derivative_market = list(basic_composer.derivative_markets.values())[0]
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        price = Decimal("36.1")
        quantity = Decimal("100")
        margin = price * quantity
        order_type = "BUY"
        cid = "test_cid"
        trigger_price = Decimal("43.5")

        message = basic_composer.msg_create_derivative_limit_order_v2(
            market_id=derivative_market.id,
            sender=sender,
            subaccount_id=subaccount_id,
            fee_recipient=fee_recipient,
            price=price,
            quantity=quantity,
            margin=margin,
            order_type=order_type,
            cid=cid,
            trigger_price=trigger_price,
        )

        expected_message = {
            "sender": sender,
            "order": {
                "marketId": derivative_market.id,
                "orderInfo": {
                    "subaccountId": subaccount_id,
                    "feeRecipient": fee_recipient,
                    "price": f"{Token.convert_value_to_extended_decimal_format(value=price).normalize():f}",
                    "quantity": f"{Token.convert_value_to_extended_decimal_format(value=quantity).normalize():f}",
                    "cid": cid,
                },
                "margin": f"{Token.convert_value_to_extended_decimal_format(value=margin).normalize():f}",
                "orderType": order_type,
                "triggerPrice": f"{Token.convert_value_to_extended_decimal_format(value=trigger_price).normalize():f}",
            },
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_batch_create_derivative_limit_orders(self, basic_composer):
        derivative_market = list(basic_composer.derivative_markets.values())[0]
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        price = Decimal("36.1")
        quantity = Decimal("100")
        order_type = "BUY"
        cid = "test_cid"
        trigger_price = Decimal("43.5")

        order = basic_composer.create_derivative_order_v2(
            market_id=derivative_market.id,
            subaccount_id=subaccount_id,
            fee_recipient=fee_recipient,
            price=price,
            quantity=quantity,
            margin=price * quantity,
            order_type=order_type,
            cid=cid,
            trigger_price=trigger_price,
        )

        message = basic_composer.msg_batch_create_derivative_limit_orders_v2(
            sender=sender,
            orders=[order],
        )

        expected_message = {
            "sender": sender,
            "orders": [json_format.MessageToDict(message=order, always_print_fields_with_no_presence=True)],
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_create_derivative_market_order(self, basic_composer):
        derivative_market = list(basic_composer.derivative_markets.values())[0]
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        price = Decimal("36.1")
        quantity = Decimal("100")
        margin = price * quantity
        order_type = "BUY"
        cid = "test_cid"
        trigger_price = Decimal("43.5")

        message = basic_composer.msg_create_derivative_market_order_v2(
            market_id=derivative_market.id,
            sender=sender,
            subaccount_id=subaccount_id,
            fee_recipient=fee_recipient,
            price=price,
            quantity=quantity,
            margin=margin,
            order_type=order_type,
            cid=cid,
            trigger_price=trigger_price,
        )

        expected_message = {
            "sender": sender,
            "order": {
                "marketId": derivative_market.id,
                "orderInfo": {
                    "subaccountId": subaccount_id,
                    "feeRecipient": fee_recipient,
                    "price": f"{Token.convert_value_to_extended_decimal_format(value=price).normalize():f}",
                    "quantity": f"{Token.convert_value_to_extended_decimal_format(value=quantity).normalize():f}",
                    "cid": cid,
                },
                "margin": f"{Token.convert_value_to_extended_decimal_format(value=margin).normalize():f}",
                "orderType": order_type,
                "triggerPrice": f"{Token.convert_value_to_extended_decimal_format(value=trigger_price).normalize():f}",
            },
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_cancel_derivative_order(self, basic_composer):
        derivative_market = list(basic_composer.derivative_markets.values())[0]
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        order_hash = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        cid = "test_cid"
        is_conditional = False
        is_buy = True
        is_market_order = False

        expected_order_mask = basic_composer._order_mask(
            is_conditional=is_conditional,
            is_buy=is_buy,
            is_market_order=is_market_order,
        )

        message = basic_composer.msg_cancel_derivative_order_v2(
            market_id=derivative_market.id,
            sender=sender,
            subaccount_id=subaccount_id,
            order_hash=order_hash,
            cid=cid,
            is_conditional=is_conditional,
            is_buy=is_buy,
            is_market_order=is_market_order,
        )

        expected_message = {
            "sender": sender,
            "marketId": derivative_market.id,
            "subaccountId": subaccount_id,
            "orderHash": order_hash,
            "orderMask": expected_order_mask,
            "cid": cid,
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_batch_cancel_derivative_orders(self, basic_composer):
        derivative_market = list(basic_composer.derivative_markets.values())[0]
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"

        order_data = basic_composer.create_order_data_without_mask_v2(
            market_id=derivative_market.id,
            subaccount_id=subaccount_id,
            order_hash="0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000",
        )

        message = basic_composer.msg_batch_cancel_derivative_orders_v2(
            sender=sender,
            orders_data=[order_data],
        )

        expected_message = {
            "sender": sender,
            "data": [json_format.MessageToDict(message=order_data, always_print_fields_with_no_presence=True)],
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_instant_binary_options_market_launch(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        ticker = "B2500/INJ"
        oracle_symbol = "B2500_1/INJ"
        oracle_provider = "Injective"
        oracle_scale_factor = 6
        oracle_type = "Band"
        quote_denom = "inj"
        min_price_tick_size = Decimal("0.01")
        min_quantity_tick_size = Decimal("1")
        maker_fee_rate = Decimal("0.001")
        taker_fee_rate = Decimal("-0.002")
        expiration_timestamp = 1630000000
        settlement_timestamp = 1660000000
        admin = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
        min_notional = Decimal("2")

        message = basic_composer.msg_instant_binary_options_market_launch_v2(
            sender=sender,
            ticker=ticker,
            oracle_symbol=oracle_symbol,
            oracle_provider=oracle_provider,
            oracle_type=oracle_type,
            oracle_scale_factor=oracle_scale_factor,
            maker_fee_rate=maker_fee_rate,
            taker_fee_rate=taker_fee_rate,
            expiration_timestamp=expiration_timestamp,
            settlement_timestamp=settlement_timestamp,
            admin=admin,
            quote_denom=quote_denom,
            min_price_tick_size=min_price_tick_size,
            min_quantity_tick_size=min_quantity_tick_size,
            min_notional=min_notional,
        )

        chain_min_price_tick_size = Token.convert_value_to_extended_decimal_format(value=min_price_tick_size)
        chain_min_quantity_tick_size = Token.convert_value_to_extended_decimal_format(value=min_quantity_tick_size)
        chain_min_notional = Token.convert_value_to_extended_decimal_format(value=min_notional)

        expected_message = {
            "sender": sender,
            "ticker": ticker,
            "oracleSymbol": oracle_symbol,
            "oracleProvider": oracle_provider,
            "oracleType": oracle_type,
            "oracleScaleFactor": oracle_scale_factor,
            "makerFeeRate": f"{Token.convert_value_to_extended_decimal_format(value=maker_fee_rate).normalize():f}",
            "takerFeeRate": f"{Token.convert_value_to_extended_decimal_format(value=taker_fee_rate).normalize():f}",
            "expirationTimestamp": str(expiration_timestamp),
            "settlementTimestamp": str(settlement_timestamp),
            "admin": admin,
            "quoteDenom": quote_denom,
            "minPriceTickSize": f"{chain_min_price_tick_size.normalize():f}",
            "minQuantityTickSize": f"{chain_min_quantity_tick_size.normalize():f}",
            "minNotional": f"{chain_min_notional.normalize():f}",
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_create_binary_options_limit_order(self, basic_composer):
        market = list(basic_composer.binary_option_markets.values())[0]
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        price = Decimal("36.1")
        quantity = Decimal("100")
        margin = price * quantity
        order_type = "BUY"
        cid = "test_cid"
        trigger_price = Decimal("43.5")

        message = basic_composer.msg_create_binary_options_limit_order_v2(
            market_id=market.id,
            sender=sender,
            subaccount_id=subaccount_id,
            fee_recipient=fee_recipient,
            price=price,
            quantity=quantity,
            margin=margin,
            order_type=order_type,
            cid=cid,
            trigger_price=trigger_price,
        )

        expected_price = Token.convert_value_to_extended_decimal_format(value=price)
        expected_quantity = Token.convert_value_to_extended_decimal_format(value=quantity)
        expected_margin = Token.convert_value_to_extended_decimal_format(value=margin)
        expected_trigger_price = Token.convert_value_to_extended_decimal_format(value=trigger_price)

        expected_message = {
            "sender": sender,
            "order": {
                "marketId": market.id,
                "orderInfo": {
                    "subaccountId": subaccount_id,
                    "feeRecipient": fee_recipient,
                    "price": f"{expected_price.normalize():f}",
                    "quantity": f"{expected_quantity.normalize():f}",
                    "cid": cid,
                },
                "margin": f"{expected_margin.normalize():f}",
                "orderType": order_type,
                "triggerPrice": f"{expected_trigger_price.normalize():f}",
            },
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_create_binary_options_market_order(self, basic_composer):
        market = list(basic_composer.binary_option_markets.values())[0]
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        price = Decimal("36.1")
        quantity = Decimal("100")
        margin = price * quantity
        order_type = "BUY"
        cid = "test_cid"
        trigger_price = Decimal("43.5")

        message = basic_composer.msg_create_binary_options_market_order_v2(
            market_id=market.id,
            sender=sender,
            subaccount_id=subaccount_id,
            fee_recipient=fee_recipient,
            price=price,
            quantity=quantity,
            margin=margin,
            order_type=order_type,
            cid=cid,
            trigger_price=trigger_price,
        )

        expected_message = {
            "sender": sender,
            "order": {
                "marketId": market.id,
                "orderInfo": {
                    "subaccountId": subaccount_id,
                    "feeRecipient": fee_recipient,
                    "price": f"{Token.convert_value_to_extended_decimal_format(value=price).normalize():f}",
                    "quantity": f"{Token.convert_value_to_extended_decimal_format(value=quantity).normalize():f}",
                    "cid": cid,
                },
                "margin": f"{Token.convert_value_to_extended_decimal_format(value=margin).normalize():f}",
                "orderType": order_type,
                "triggerPrice": f"{Token.convert_value_to_extended_decimal_format(value=trigger_price).normalize():f}",
            },
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_cancel_derivative_order(self, basic_composer):
        market = list(basic_composer.binary_option_markets.values())[0]
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        order_hash = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        cid = "test_cid"
        is_conditional = False
        is_buy = True
        is_market_order = False

        expected_order_mask = basic_composer._order_mask(
            is_conditional=is_conditional,
            is_buy=is_buy,
            is_market_order=is_market_order,
        )

        message = basic_composer.msg_cancel_derivative_order_v2(
            market_id=market.id,
            sender=sender,
            subaccount_id=subaccount_id,
            order_hash=order_hash,
            cid=cid,
            is_conditional=is_conditional,
            is_buy=is_buy,
            is_market_order=is_market_order,
        )

        expected_message = {
            "sender": sender,
            "marketId": market.id,
            "subaccountId": subaccount_id,
            "orderHash": order_hash,
            "orderMask": expected_order_mask,
            "cid": cid,
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_subaccount_transfer(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        source_subaccount_id = "0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000001"
        destination_subaccount_id = "0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000002"
        amount = 100
        denom = "inj"

        message = basic_composer.msg_subaccount_transfer_v2(
            sender=sender,
            source_subaccount_id=source_subaccount_id,
            destination_subaccount_id=destination_subaccount_id,
            amount=amount,
            denom=denom,
        )

        expected_message = {
            "sender": sender,
            "sourceSubaccountId": source_subaccount_id,
            "destinationSubaccountId": destination_subaccount_id,
            "amount": {
                "amount": f"{Token.convert_value_to_extended_decimal_format(value=Decimal(str(amount))).normalize():f}",
                "denom": denom,
            },
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_external_transfer(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        source_subaccount_id = "0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000001"
        destination_subaccount_id = "0xc6fe5d33615a1c52c08018c47e8bc53646a0e101000000000000000000000000"
        amount = 100
        denom = "inj"

        message = basic_composer.msg_external_transfer_v2(
            sender=sender,
            source_subaccount_id=source_subaccount_id,
            destination_subaccount_id=destination_subaccount_id,
            amount=100,
            denom=denom,
        )

        expected_message = {
            "sender": sender,
            "sourceSubaccountId": source_subaccount_id,
            "destinationSubaccountId": destination_subaccount_id,
            "amount": {
                "amount": f"{Token.convert_value_to_extended_decimal_format(value=Decimal(str(amount))).normalize():f}",
                "denom": denom,
            },
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_liquidate_position(self, basic_composer):
        market = list(basic_composer.derivative_markets.values())[0]
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        subaccount_id = "0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000001"
        order = basic_composer.create_derivative_order_v2(
            market_id=market.id,
            subaccount_id=subaccount_id,
            fee_recipient="inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r",
            price=Decimal("36.1"),
            quantity=Decimal("100"),
            margin=Decimal("36.1") * Decimal("100"),
            order_type="BUY",
        )

        message = basic_composer.msg_liquidate_position_v2(
            sender=sender,
            subaccount_id=subaccount_id,
            market_id=market.id,
            order=order,
        )

        expected_message = {
            "sender": sender,
            "subaccountId": subaccount_id,
            "marketId": market.id,
            "order": json_format.MessageToDict(message=order, always_print_fields_with_no_presence=True),
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_emergency_settle_market(self, basic_composer):
        market = list(basic_composer.derivative_markets.values())[0]
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        subaccount_id = "0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000001"

        message = basic_composer.msg_emergency_settle_market_v2(
            sender=sender,
            subaccount_id=subaccount_id,
            market_id=market.id,
        )

        expected_message = {
            "sender": sender,
            "subaccountId": subaccount_id,
            "marketId": market.id,
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_increase_position_margin(self, basic_composer):
        market = list(basic_composer.derivative_markets.values())[0]
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        source_subaccount_id = "0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000001"
        destination_subaccount_id = "0xc6fe5d33615a1c52c08018c47e8bc53646a0e101000000000000000000000000"
        amount = Decimal(100)

        expected_amount = Token.convert_value_to_extended_decimal_format(value=amount)

        message = basic_composer.msg_increase_position_margin_v2(
            sender=sender,
            source_subaccount_id=source_subaccount_id,
            destination_subaccount_id=destination_subaccount_id,
            market_id=market.id,
            amount=amount,
        )

        expected_message = {
            "sender": sender,
            "sourceSubaccountId": source_subaccount_id,
            "destinationSubaccountId": destination_subaccount_id,
            "marketId": market.id,
            "amount": f"{expected_amount.normalize():f}",
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_decrease_position_margin(self, basic_composer):
        market = list(basic_composer.derivative_markets.values())[0]
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        source_subaccount_id = "0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000001"
        destination_subaccount_id = "0xc6fe5d33615a1c52c08018c47e8bc53646a0e101000000000000000000000000"
        amount = Decimal(100)

        expected_amount = Token.convert_value_to_extended_decimal_format(value=amount)

        message = basic_composer.msg_decrease_position_margin_v2(
            sender=sender,
            source_subaccount_id=source_subaccount_id,
            destination_subaccount_id=destination_subaccount_id,
            market_id=market.id,
            amount=amount,
        )

        expected_message = {
            "sender": sender,
            "sourceSubaccountId": source_subaccount_id,
            "destinationSubaccountId": destination_subaccount_id,
            "marketId": market.id,
            "amount": f"{expected_amount.normalize():f}",
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_rewards_opt_out(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"

        message = basic_composer.msg_rewards_opt_out(
            sender=sender,
        )

        expected_message = {
            "sender": sender,
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_admin_update_binary_options_market(self, basic_composer):
        market = list(basic_composer.binary_option_markets.values())[0]
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        status = "Paused"
        settlement_price = Decimal("100.5")
        expiration_timestamp = 1630000000
        settlement_timestamp = 1660000000

        expected_settlement_price = Token.convert_value_to_extended_decimal_format(value=settlement_price)

        message = basic_composer.msg_admin_update_binary_options_market_v2(
            sender=sender,
            market_id=market.id,
            status=status,
            settlement_price=settlement_price,
            expiration_timestamp=expiration_timestamp,
            settlement_timestamp=settlement_timestamp,
        )

        expected_message = {
            "sender": sender,
            "marketId": market.id,
            "settlementPrice": f"{expected_settlement_price.normalize():f}",
            "expirationTimestamp": str(expiration_timestamp),
            "settlementTimestamp": str(settlement_timestamp),
            "status": status,
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_update_spot_market(self, basic_composer):
        market = list(basic_composer.spot_markets.values())[0]
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        new_ticker = "NEW/TICKER"
        min_price_tick_size = Decimal("0.0009")
        min_quantity_tick_size = Decimal("10")
        min_notional = Decimal("5")

        expected_min_price_tick_size = Token.convert_value_to_extended_decimal_format(value=min_price_tick_size)
        expected_min_quantity_tick_size = Token.convert_value_to_extended_decimal_format(value=min_quantity_tick_size)
        expected_min_notional = Token.convert_value_to_extended_decimal_format(value=min_notional)

        message = basic_composer.msg_update_spot_market_v2(
            admin=sender,
            market_id=market.id,
            new_ticker=new_ticker,
            new_min_price_tick_size=min_price_tick_size,
            new_min_quantity_tick_size=min_quantity_tick_size,
            new_min_notional=min_notional,
        )

        expected_message = {
            "admin": sender,
            "marketId": market.id,
            "newTicker": new_ticker,
            "newMinPriceTickSize": f"{expected_min_price_tick_size.normalize():f}",
            "newMinQuantityTickSize": f"{expected_min_quantity_tick_size.normalize():f}",
            "newMinNotional": f"{expected_min_notional.normalize():f}",
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_update_derivative_market(self, basic_composer):
        market = list(basic_composer.derivative_markets.values())[0]
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        new_ticker = "NEW/TICKER"
        min_price_tick_size = Decimal("0.0009")
        min_quantity_tick_size = Decimal("10")
        min_notional = Decimal("5")
        initial_margin_ratio = Decimal("0.05")
        maintenance_margin_ratio = Decimal("0.009")

        expected_min_price_tick_size = Token.convert_value_to_extended_decimal_format(value=min_price_tick_size)
        expected_min_quantity_tick_size = Token.convert_value_to_extended_decimal_format(value=min_quantity_tick_size)
        expected_min_notional = Token.convert_value_to_extended_decimal_format(value=min_notional)
        expected_initial_margin_ratio = Token.convert_value_to_extended_decimal_format(value=initial_margin_ratio)
        expected_maintenance_margin_ratio = Token.convert_value_to_extended_decimal_format(
            value=maintenance_margin_ratio
        )

        message = basic_composer.msg_update_derivative_market_v2(
            admin=sender,
            market_id=market.id,
            new_ticker=new_ticker,
            new_min_price_tick_size=min_price_tick_size,
            new_min_quantity_tick_size=min_quantity_tick_size,
            new_min_notional=min_notional,
            new_initial_margin_ratio=initial_margin_ratio,
            new_maintenance_margin_ratio=maintenance_margin_ratio,
        )

        expected_message = {
            "admin": sender,
            "marketId": market.id,
            "newTicker": new_ticker,
            "newMinPriceTickSize": f"{expected_min_price_tick_size.normalize():f}",
            "newMinQuantityTickSize": f"{expected_min_quantity_tick_size.normalize():f}",
            "newMinNotional": f"{expected_min_notional.normalize():f}",
            "newInitialMarginRatio": f"{expected_initial_margin_ratio.normalize():f}",
            "newMaintenanceMarginRatio": f"{expected_maintenance_margin_ratio.normalize():f}",
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_authorize_stake_grants(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        amount = Decimal("100")
        grant_authorization = basic_composer.create_grant_authorization(
            grantee="inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r",
            amount=amount,
        )

        message = basic_composer.msg_authorize_stake_grants(
            sender=sender,
            grants=[grant_authorization],
        )

        expected_amount = amount * Decimal(f"1e{INJ_DECIMALS}")
        expected_message = {
            "sender": sender,
            "grants": [
                {
                    "grantee": grant_authorization.grantee,
                    "amount": str(int(expected_amount)),
                }
            ],
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_activate_stake_grant(self, basic_composer):
        sender = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
        granter = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"

        message = basic_composer.msg_activate_stake_grant(
            sender=sender,
            granter=granter,
        )

        expected_message = {
            "sender": sender,
            "granter": granter,
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_ibc_transfer(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        source_port = "transfer"
        source_channel = "channel-126"
        token_decimals = 18
        transfer_amount = Decimal("0.1") * Decimal(f"1e{token_decimals}")
        inj_chain_denom = "inj"
        token_amount = basic_composer.coin(amount=int(transfer_amount), denom=inj_chain_denom)
        receiver = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
        timeout_height = 10
        timeout_timestamp = 1630000000
        memo = "memo"

        message = basic_composer.msg_ibc_transfer(
            source_port=source_port,
            source_channel=source_channel,
            token_amount=token_amount,
            sender=sender,
            receiver=receiver,
            timeout_height=timeout_height,
            timeout_timestamp=timeout_timestamp,
            memo=memo,
        )

        expected_message = {
            "sourcePort": source_port,
            "sourceChannel": source_channel,
            "token": {
                "amount": "100000000000000000",
                "denom": "inj",
            },
            "sender": sender,
            "receiver": receiver,
            "timeoutHeight": {"revisionNumber": str(timeout_height), "revisionHeight": str(timeout_height)},
            "timeoutTimestamp": str(timeout_timestamp),
            "memo": memo,
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_create_namespace(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        denom = "inj"
        wasmhook = "wasmhook"
        mints_paused = True
        sends_paused = False
        burns_paused = True
        permissions_role1 = basic_composer.permissions_role(
            role="role1",
            permissions=1,
        )
        permissions_role2 = basic_composer.permissions_role(
            role="role2",
            permissions=2,
        )
        permissions_address_roles1 = basic_composer.permissions_address_roles(
            address="inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0",
            roles=["role1"],
        )
        permissions_address_roles2 = basic_composer.permissions_address_roles(
            address="inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0",
            roles=["role2"],
        )

        message = basic_composer.msg_create_namespace(
            sender=sender,
            denom=denom,
            wasm_hook=wasmhook,
            mints_paused=mints_paused,
            sends_paused=sends_paused,
            burns_paused=burns_paused,
            role_permissions=[permissions_role1, permissions_role2],
            address_roles=[permissions_address_roles1, permissions_address_roles2],
        )

        expected_message = {
            "sender": sender,
            "namespace": {
                "denom": denom,
                "wasmHook": wasmhook,
                "mintsPaused": mints_paused,
                "sendsPaused": sends_paused,
                "burnsPaused": burns_paused,
                "rolePermissions": [
                    json_format.MessageToDict(message=permissions_role1, always_print_fields_with_no_presence=True),
                    json_format.MessageToDict(message=permissions_role2, always_print_fields_with_no_presence=True),
                ],
                "addressRoles": [
                    json_format.MessageToDict(
                        message=permissions_address_roles1, always_print_fields_with_no_presence=True
                    ),
                    json_format.MessageToDict(
                        message=permissions_address_roles2, always_print_fields_with_no_presence=True
                    ),
                ],
            },
        }

        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_delete_namespace(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        denom = "inj"

        message = basic_composer.msg_delete_namespace(
            sender=sender,
            namespace_denom=denom,
        )

        expected_message = {
            "sender": sender,
            "namespaceDenom": denom,
        }

        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_update_namespace(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        denom = "inj"
        wasmhook = "wasmhook"
        mints_paused = True
        sends_paused = False
        burns_paused = True

        message = basic_composer.msg_update_namespace(
            sender=sender,
            namespace_denom=denom,
            wasm_hook=wasmhook,
            mints_paused=mints_paused,
            sends_paused=sends_paused,
            burns_paused=burns_paused,
        )

        expected_message = {
            "sender": sender,
            "namespaceDenom": denom,
            "wasmHook": {"newValue": wasmhook},
            "mintsPaused": {"newValue": mints_paused},
            "sendsPaused": {"newValue": sends_paused},
            "burnsPaused": {"newValue": burns_paused},
        }

        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_update_namespace_roles(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        denom = "inj"
        permissions_role1 = basic_composer.permissions_role(
            role="role1",
            permissions=1,
        )
        permissions_role2 = basic_composer.permissions_role(
            role="role2",
            permissions=2,
        )
        permissions_address_roles1 = basic_composer.permissions_address_roles(
            address="inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0",
            roles=["role1"],
        )
        permissions_address_roles2 = basic_composer.permissions_address_roles(
            address="inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0",
            roles=["role2"],
        )

        message = basic_composer.msg_update_namespace_roles(
            sender=sender,
            namespace_denom=denom,
            role_permissions=[permissions_role1, permissions_role2],
            address_roles=[permissions_address_roles1, permissions_address_roles2],
        )

        expected_message = {
            "sender": sender,
            "namespaceDenom": denom,
            "rolePermissions": [
                json_format.MessageToDict(message=permissions_role1, always_print_fields_with_no_presence=True),
                json_format.MessageToDict(message=permissions_role2, always_print_fields_with_no_presence=True),
            ],
            "addressRoles": [
                json_format.MessageToDict(
                    message=permissions_address_roles1, always_print_fields_with_no_presence=True
                ),
                json_format.MessageToDict(
                    message=permissions_address_roles2, always_print_fields_with_no_presence=True
                ),
            ],
        }

        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_revoke_namespace_roles(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        denom = "inj"
        permissions_address_roles1 = basic_composer.permissions_address_roles(
            address="inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0",
            roles=["role1"],
        )
        permissions_address_roles2 = basic_composer.permissions_address_roles(
            address="inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0",
            roles=["role2"],
        )
        message = basic_composer.msg_revoke_namespace_roles(
            sender=sender,
            namespace_denom=denom,
            address_roles_to_revoke=[permissions_address_roles1, permissions_address_roles2],
        )

        expected_message = {
            "sender": sender,
            "namespaceDenom": denom,
            "addressRolesToRevoke": [
                json_format.MessageToDict(
                    message=permissions_address_roles1, always_print_fields_with_no_presence=True
                ),
                json_format.MessageToDict(
                    message=permissions_address_roles2, always_print_fields_with_no_presence=True
                ),
            ],
        }

        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_claim_voucher(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        denom = "inj"
        message = basic_composer.msg_claim_voucher(
            sender=sender,
            denom=denom,
        )

        expected_message = {
            "sender": sender,
            "denom": denom,
        }

        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_create_order_data_without_mask_v2(self, basic_composer):
        order_data = basic_composer.create_order_data_without_mask_v2(
            market_id=list(basic_composer.spot_markets.keys())[0],
            subaccount_id="subaccount_id",
            order_hash="0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000",
        )

        expected_message = {
            "marketId": list(basic_composer.spot_markets.keys())[0],
            "subaccountId": "subaccount_id",
            "orderHash": "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000",
            "orderMask": 1,
            "cid": "",
        }

        dict_message = json_format.MessageToDict(
            message=order_data,
            always_print_fields_with_no_presence=True,
        )

        assert dict_message == expected_message

    def test_msg_privileged_execute_contract_v2(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        contract_address = "inj1ady3s7whq30l4fx8sj3x6muv5mx4dfdlcpv8n7"
        data = "test_data"
        funds = "100inj,420peggy0x44C21afAaF20c270EBbF5914Cfc3b5022173FEB7"

        message = basic_composer.msg_privileged_execute_contract_v2(
            sender=sender,
            contract_address=contract_address,
            data=data,
            funds=funds,
        )

        expected_message = {
            "sender": sender,
            "funds": funds,
            "contractAddress": contract_address,
            "data": data,
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_create_insurance_fund(self, basic_composer):
        message = basic_composer.msg_create_insurance_fund(
            sender="sender",
            ticker="AAVE/USDT PERP",
            quote_denom="peggy0x44C21afAaF20c270EBbF5914Cfc3b5022173FEB7",
            oracle_base="0x2b9ab1e972a281585084148ba1389800799bd4be63b957507db1349314e47445",
            oracle_quote="0x2b89b9dc8fdf9f34709a5b106b472f0f39bb6ca9ce04b0fd7f2e971688e2e53b",
            oracle_type="Band",
            expiry=-1,
            initial_deposit=1,
        )

        expected_message = {
            "sender": "sender",
            "ticker": "AAVE/USDT PERP",
            "quoteDenom": "peggy0x44C21afAaF20c270EBbF5914Cfc3b5022173FEB7",
            "oracleBase": "0x2b9ab1e972a281585084148ba1389800799bd4be63b957507db1349314e47445",
            "oracleQuote": "0x2b89b9dc8fdf9f34709a5b106b472f0f39bb6ca9ce04b0fd7f2e971688e2e53b",
            "oracleType": "Band",
            "expiry": "-1",
            "initialDeposit": {
                "amount": f"{Token.convert_value_to_extended_decimal_format(value=Decimal('1')).normalize():f}",
                "denom": "peggy0x44C21afAaF20c270EBbF5914Cfc3b5022173FEB7",
            },
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_send_to_eth_fund(self, basic_composer):
        message = basic_composer.msg_send_to_eth(
            denom="peggy0x44C21afAaF20c270EBbF5914Cfc3b5022173FEB7",
            sender="sender",
            eth_dest="eth_dest",
            amount=1,
            bridge_fee=2,
        )

        expected_message = {
            "sender": "sender",
            "ethDest": "eth_dest",
            "amount": {
                "amount": f"{Token.convert_value_to_extended_decimal_format(value=Decimal(1)).normalize():f}",
                "denom": "peggy0x44C21afAaF20c270EBbF5914Cfc3b5022173FEB7",
            },
            "bridgeFee": {
                "amount": f"{Token.convert_value_to_extended_decimal_format(value=Decimal(2)).normalize():f}",
                "denom": "peggy0x44C21afAaF20c270EBbF5914Cfc3b5022173FEB7",
            },
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_underwrite(self, basic_composer):
        message = basic_composer.msg_underwrite(
            sender="sender",
            market_id="market_id",
            quote_denom="peggy0x44C21afAaF20c270EBbF5914Cfc3b5022173FEB7",
            amount=1,
        )

        expected_message = {
            "sender": "sender",
            "marketId": "market_id",
            "deposit": {
                "amount": f"{Token.convert_value_to_extended_decimal_format(Decimal('1')).normalize():f}",
                "denom": "peggy0x44C21afAaF20c270EBbF5914Cfc3b5022173FEB7",
            },
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_send(self, basic_composer):
        message = basic_composer.msg_send(
            from_address="from_address",
            to_address="to_address",
            amount=1,
            denom="peggy0x44C21afAaF20c270EBbF5914Cfc3b5022173FEB7",
        )

        expected_message = {
            "fromAddress": "from_address",
            "toAddress": "to_address",
            "amount": [
                {
                    "amount": f"{Token.convert_value_to_extended_decimal_format(Decimal('1')).normalize():f}",
                    "denom": "peggy0x44C21afAaF20c270EBbF5914Cfc3b5022173FEB7",
                },
            ],
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message
