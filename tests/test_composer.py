import json
from decimal import Decimal

import pytest
from google.protobuf import json_format

from pyinjective.composer import Composer
from pyinjective.constant import ADDITIONAL_CHAIN_FORMAT_DECIMALS
from pyinjective.core.network import Network
from tests.model_fixtures.markets_fixtures import btc_usdt_perp_market  # noqa: F401
from tests.model_fixtures.markets_fixtures import first_match_bet_market  # noqa: F401
from tests.model_fixtures.markets_fixtures import inj_token  # noqa: F401
from tests.model_fixtures.markets_fixtures import inj_usdt_spot_market  # noqa: F401
from tests.model_fixtures.markets_fixtures import usdt_perp_token  # noqa: F401
from tests.model_fixtures.markets_fixtures import usdt_token  # noqa: F401


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

    def test_composer_initialization_from_ini_files(self):
        composer = Composer(network=Network.devnet().string())

        inj_token = composer.tokens["INJ"]
        inj_usdt_spot_market = next(
            (market for market in composer.spot_markets.values() if market.ticker == "'Devnet Spot INJ/USDT'")
        )
        inj_usdt_perp_market = next(
            (
                market
                for market in composer.derivative_markets.values()
                if market.ticker == "'Devnet Derivative INJ/USDT PERP'"
            )
        )

        assert 18 == inj_token.decimals
        assert 18 == inj_usdt_spot_market.base_token.decimals
        assert 6 == inj_usdt_spot_market.quote_token.decimals
        assert 6 == inj_usdt_perp_market.quote_token.decimals

    def test_msg_create_denom(self, basic_composer: Composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        subdenom = "inj-test"
        name = "Injective Test"
        symbol = "INJTEST"

        message = basic_composer.msg_create_denom(
            sender=sender,
            subdenom=subdenom,
            name=name,
            symbol=symbol,
        )

        assert message.sender == sender
        assert message.subdenom == subdenom
        assert message.name == name
        assert message.symbol == symbol

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

        assert message.sender == sender
        assert message.amount == amount

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

        assert message.sender == sender
        assert message.amount == amount

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

        assert message.sender == sender
        assert message.metadata.description == description
        assert message.metadata.denom_units[0].denom == denom
        assert message.metadata.denom_units[0].exponent == 0
        assert message.metadata.denom_units[0].aliases == [f"micro{subdenom}"]
        assert message.metadata.denom_units[1].denom == subdenom
        assert message.metadata.denom_units[1].exponent == token_decimals
        assert message.metadata.denom_units[1].aliases == [subdenom]
        assert message.metadata.base == denom
        assert message.metadata.display == subdenom
        assert message.metadata.name == name
        assert message.metadata.symbol == symbol
        assert message.metadata.uri == uri
        assert message.metadata.uri_hash == uri_hash

    def test_msg_change_admin(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        denom = "factory/inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r/inj_test"
        new_admin = "inj1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqe2hm49"

        message = basic_composer.msg_change_admin(
            sender=sender,
            denom=denom,
            new_admin=new_admin,
        )

        assert message.sender == sender
        assert message.denom == denom
        assert message.new_admin == new_admin

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

        assert message.sender == sender
        assert message.contract == contract
        assert message.msg == msg
        assert message.funds == funds

    def test_msg_deposit(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        subaccount_id = "0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000001"
        amount = Decimal(100)
        denom = "INJ"

        token = basic_composer.tokens[denom]

        expected_amount = token.chain_formatted_value(human_readable_value=Decimal(amount))

        message = basic_composer.msg_deposit(
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
                "denom": token.denom,
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
        amount = Decimal(100)
        denom = "INJ"

        token = basic_composer.tokens[denom]

        expected_amount = token.chain_formatted_value(human_readable_value=Decimal(amount))

        message = basic_composer.msg_withdraw(
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
                "denom": token.denom,
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
        base_denom = "INJ"
        quote_denom = "USDT"
        min_price_tick_size = Decimal("0.01")
        min_quantity_tick_size = Decimal("1")

        base_token = basic_composer.tokens[base_denom]
        quote_token = basic_composer.tokens[quote_denom]

        expected_min_price_tick_size = min_price_tick_size * Decimal(
            f"1e{quote_token.decimals - base_token.decimals + ADDITIONAL_CHAIN_FORMAT_DECIMALS}"
        )
        expected_min_quantity_tick_size = min_quantity_tick_size * Decimal(
            f"1e{base_token.decimals + ADDITIONAL_CHAIN_FORMAT_DECIMALS}"
        )

        message = basic_composer.msg_instant_spot_market_launch(
            sender=sender,
            ticker=ticker,
            base_denom=base_denom,
            quote_denom=quote_denom,
            min_price_tick_size=min_price_tick_size,
            min_quantity_tick_size=min_quantity_tick_size,
        )

        expected_message = {
            "sender": sender,
            "ticker": ticker,
            "baseDenom": base_token.denom,
            "quoteDenom": quote_token.denom,
            "minPriceTickSize": f"{expected_min_price_tick_size.normalize():f}",
            "minQuantityTickSize": f"{expected_min_quantity_tick_size.normalize():f}",
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_instant_perpetual_market_launch(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        ticker = "BTC/INJ PERP"
        quote_denom = "INJ"
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

        quote_token = basic_composer.tokens[quote_denom]

        expected_min_price_tick_size = min_price_tick_size * Decimal(
            f"1e{quote_token.decimals + ADDITIONAL_CHAIN_FORMAT_DECIMALS}"
        )
        expected_min_quantity_tick_size = min_quantity_tick_size * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        expected_maker_fee_rate = maker_fee_rate * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        expected_taker_fee_rate = taker_fee_rate * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        expected_initial_margin_ratio = initial_margin_ratio * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        expected_maintenance_margin_ratio = maintenance_margin_ratio * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        message = basic_composer.msg_instant_perpetual_market_launch(
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
        )

        expected_message = {
            "sender": sender,
            "ticker": ticker,
            "quoteDenom": quote_token.denom,
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
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_instant_expiry_futures_market_launch(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        ticker = "BTC/INJ PERP"
        quote_denom = "INJ"
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

        quote_token = basic_composer.tokens[quote_denom]

        expected_min_price_tick_size = min_price_tick_size * Decimal(
            f"1e{quote_token.decimals + ADDITIONAL_CHAIN_FORMAT_DECIMALS}"
        )
        expected_min_quantity_tick_size = min_quantity_tick_size * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        expected_maker_fee_rate = maker_fee_rate * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        expected_taker_fee_rate = taker_fee_rate * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        expected_initial_margin_ratio = initial_margin_ratio * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        expected_maintenance_margin_ratio = maintenance_margin_ratio * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        message = basic_composer.msg_instant_expiry_futures_market_launch(
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
        )

        expected_message = {
            "sender": sender,
            "ticker": ticker,
            "quoteDenom": quote_token.denom,
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

        message = basic_composer.msg_create_spot_limit_order(
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

        expected_price = spot_market.price_to_chain_format(human_readable_value=price)
        expected_quantity = spot_market.quantity_to_chain_format(human_readable_value=quantity)
        expected_trigger_price = spot_market.price_to_chain_format(human_readable_value=trigger_price)

        assert "injective.exchange.v1beta1.MsgCreateSpotLimitOrder" == message.DESCRIPTOR.full_name
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

        message = basic_composer.msg_batch_create_spot_limit_orders(
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

        message = basic_composer.msg_create_spot_market_order(
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

        expected_price = spot_market.price_to_chain_format(human_readable_value=price)
        expected_quantity = spot_market.quantity_to_chain_format(human_readable_value=quantity)
        expected_trigger_price = spot_market.price_to_chain_format(human_readable_value=trigger_price)

        assert "injective.exchange.v1beta1.MsgCreateSpotMarketOrder" == message.DESCRIPTOR.full_name
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

    def test_msg_cancel_spot_order(self, basic_composer):
        spot_market = list(basic_composer.spot_markets.values())[0]
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        order_hash = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        cid = "test_cid"

        message = basic_composer.msg_cancel_spot_order(
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

        order_data = basic_composer.order_data(
            market_id=spot_market.id,
            subaccount_id=subaccount_id,
            order_hash="0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000",
        )

        message = basic_composer.msg_batch_cancel_spot_orders(
            sender=sender,
            orders_data=[order_data],
        )

        assert "injective.exchange.v1beta1.MsgBatchCancelSpotOrders" == message.DESCRIPTOR.full_name
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
        spot_order_to_cancel = basic_composer.order_data(
            market_id=spot_market_id,
            subaccount_id=subaccount_id,
            order_hash="0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000",
        )
        derivative_order_to_cancel = basic_composer.order_data(
            market_id=derivative_market_id,
            subaccount_id=subaccount_id,
            order_hash="0x222daa22f60fe9f075ed0ca583459e121c23e64431c3fbffdedda04598ede0d2",
        )
        binary_options_order_to_cancel = basic_composer.order_data(
            market_id=binary_options_market_id,
            subaccount_id=subaccount_id,
            order_hash="0x7ee76255d7ca763c56b0eab9828fca89fdd3739645501c8a80f58b62b4f76da5",
        )
        spot_order_to_create = basic_composer.spot_order(
            market_id=spot_market_id,
            subaccount_id=subaccount_id,
            fee_recipient="inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r",
            price=Decimal("36.1"),
            quantity=Decimal("100"),
            order_type="BUY",
            cid="test_cid",
            trigger_price=Decimal("43.5"),
        )
        derivative_order_to_create = basic_composer.derivative_order(
            market_id=derivative_market_id,
            subaccount_id=subaccount_id,
            fee_recipient="inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r",
            price=Decimal("36.1"),
            quantity=Decimal("100"),
            margin=Decimal("36.1") * Decimal("100"),
            order_type="BUY",
        )
        binary_options_order_to_create = basic_composer.binary_options_order(
            market_id=binary_options_market_id,
            subaccount_id=subaccount_id,
            fee_recipient="inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r",
            price=Decimal("36.1"),
            quantity=Decimal("100"),
            margin=Decimal("36.1") * Decimal("100"),
            order_type="BUY",
        )

        message = basic_composer.msg_batch_update_orders(
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

        message = basic_composer.msg_create_derivative_limit_order(
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

        expected_price = derivative_market.price_to_chain_format(human_readable_value=price)
        expected_quantity = derivative_market.quantity_to_chain_format(human_readable_value=quantity)
        expected_margin = derivative_market.margin_to_chain_format(human_readable_value=margin)
        expected_trigger_price = derivative_market.price_to_chain_format(human_readable_value=trigger_price)

        expected_message = {
            "sender": sender,
            "order": {
                "marketId": derivative_market.id,
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

        order = basic_composer.derivative_order(
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

        message = basic_composer.msg_batch_create_derivative_limit_orders(
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

        message = basic_composer.msg_create_derivative_market_order(
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

        expected_price = derivative_market.price_to_chain_format(human_readable_value=price)
        expected_quantity = derivative_market.quantity_to_chain_format(human_readable_value=quantity)
        expected_margin = derivative_market.margin_to_chain_format(human_readable_value=margin)
        expected_trigger_price = derivative_market.price_to_chain_format(human_readable_value=trigger_price)

        expected_message = {
            "sender": sender,
            "order": {
                "marketId": derivative_market.id,
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

        message = basic_composer.msg_cancel_derivative_order(
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

        order_data = basic_composer.order_data(
            market_id=derivative_market.id,
            subaccount_id=subaccount_id,
            order_hash="0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000",
        )

        message = basic_composer.msg_batch_cancel_derivative_orders(
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
        quote_denom = "INJ"
        min_price_tick_size = Decimal("0.01")
        min_quantity_tick_size = Decimal("1")
        maker_fee_rate = Decimal("0.001")
        taker_fee_rate = Decimal("-0.002")
        expiration_timestamp = 1630000000
        settlement_timestamp = 1660000000
        admin = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"

        quote_token = basic_composer.tokens[quote_denom]

        expected_min_price_tick_size = min_price_tick_size * Decimal(
            f"1e{quote_token.decimals + ADDITIONAL_CHAIN_FORMAT_DECIMALS}"
        )
        expected_min_quantity_tick_size = min_quantity_tick_size * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        expected_maker_fee_rate = maker_fee_rate * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        expected_taker_fee_rate = taker_fee_rate * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        message = basic_composer.msg_instant_binary_options_market_launch(
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
        )

        expected_message = {
            "sender": sender,
            "ticker": ticker,
            "oracleSymbol": oracle_symbol,
            "oracleProvider": oracle_provider,
            "oracleType": oracle_type,
            "oracleScaleFactor": oracle_scale_factor,
            "makerFeeRate": f"{expected_maker_fee_rate.normalize():f}",
            "takerFeeRate": f"{expected_taker_fee_rate.normalize():f}",
            "expirationTimestamp": str(expiration_timestamp),
            "settlementTimestamp": str(settlement_timestamp),
            "admin": admin,
            "quoteDenom": quote_token.denom,
            "minPriceTickSize": f"{expected_min_price_tick_size.normalize():f}",
            "minQuantityTickSize": f"{expected_min_quantity_tick_size.normalize():f}",
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

        message = basic_composer.msg_create_binary_options_limit_order(
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

        expected_price = market.price_to_chain_format(human_readable_value=price)
        expected_quantity = market.quantity_to_chain_format(human_readable_value=quantity)
        expected_margin = market.margin_to_chain_format(human_readable_value=margin)
        expected_trigger_price = market.price_to_chain_format(human_readable_value=trigger_price)

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

        message = basic_composer.msg_create_binary_options_market_order(
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

        expected_price = market.price_to_chain_format(human_readable_value=price)
        expected_quantity = market.quantity_to_chain_format(human_readable_value=quantity)
        expected_margin = market.margin_to_chain_format(human_readable_value=margin)
        expected_trigger_price = market.price_to_chain_format(human_readable_value=trigger_price)

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

        message = basic_composer.msg_cancel_derivative_order(
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
        amount = Decimal(100)
        denom = "INJ"

        token = basic_composer.tokens[denom]

        expected_amount = token.chain_formatted_value(human_readable_value=amount)

        message = basic_composer.msg_subaccount_transfer(
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
                "amount": f"{expected_amount.normalize():f}",
                "denom": token.denom,
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
        amount = Decimal(100)
        denom = "INJ"

        token = basic_composer.tokens[denom]

        expected_amount = token.chain_formatted_value(human_readable_value=amount)

        message = basic_composer.msg_subaccount_transfer(
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
                "amount": f"{expected_amount.normalize():f}",
                "denom": token.denom,
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
        order = basic_composer.derivative_order(
            market_id=market.id,
            subaccount_id=subaccount_id,
            fee_recipient="inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r",
            price=Decimal("36.1"),
            quantity=Decimal("100"),
            margin=Decimal("36.1") * Decimal("100"),
            order_type="BUY",
        )

        message = basic_composer.msg_liquidate_position(
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

        message = basic_composer.msg_emergency_settle_market(
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

    def test_msg_external_transfer(self, basic_composer):
        market = list(basic_composer.derivative_markets.values())[0]
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        source_subaccount_id = "0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000001"
        destination_subaccount_id = "0xc6fe5d33615a1c52c08018c47e8bc53646a0e101000000000000000000000000"
        amount = Decimal(100)

        expected_amount = market.margin_to_chain_format(human_readable_value=amount)

        message = basic_composer.msg_increase_position_margin(
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

        expected_settlement_price = market.price_to_chain_format(human_readable_value=settlement_price)

        message = basic_composer.msg_admin_update_binary_options_market(
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
