import json
from decimal import Decimal

import pytest
from google.protobuf import json_format

from pyinjective.composer_v2 import Composer
from pyinjective.constant import ADDITIONAL_CHAIN_FORMAT_DECIMALS, INJ_DECIMALS
from pyinjective.core.network import Network
from pyinjective.core.token import Token
from pyinjective.proto.injective.permissions.v1beta1 import permissions_pb2 as permissions_pb


class TestComposer:
    @pytest.fixture
    def inj_usdt_market_id(self):
        return "0xa508cb32923323679f29a032c70342c147c17d0145625922b0ef22e955c844c0"

    @pytest.fixture
    def basic_composer(self):
        composer = Composer(
            network=Network.devnet().string(),
        )

        return composer

    def test_msg_create_denom(self, basic_composer: Composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        subdenom = "inj-test"
        name = "Injective Test"
        symbol = "INJTEST"
        decimals = 18
        allow_admin_burn = True

        message = basic_composer.msg_create_denom(
            sender=sender,
            subdenom=subdenom,
            name=name,
            symbol=symbol,
            decimals=decimals,
            allow_admin_burn=allow_admin_burn,
        )

        expected_message = {
            "sender": sender,
            "subdenom": subdenom,
            "name": name,
            "symbol": symbol,
            "decimals": decimals,
            "allowAdminBurn": allow_admin_burn,
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
        receiver = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"

        message = basic_composer.msg_mint(
            sender=sender,
            amount=amount,
            receiver=receiver,
        )

        expected_message = {
            "sender": sender,
            "amount": {
                "amount": str(amount.amount),
                "denom": amount.denom,
            },
            "receiver": receiver,
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
        burn_from_address = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"

        message = basic_composer.msg_burn(
            sender=sender,
            amount=amount,
            burn_from_address=burn_from_address,
        )

        expected_message = {
            "sender": sender,
            "amount": {
                "amount": str(amount.amount),
                "denom": amount.denom,
            },
            "burnFromAddress": burn_from_address,
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

        expected_amount = Decimal(str(amount))

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
                "amount": f"{Decimal(str(amount)):f}",
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

        message = basic_composer.msg_instant_spot_market_launch(
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
        reduce_margin_ratio = Decimal("3")
        cap_value = Decimal("1000")
        open_notional_cap = basic_composer.open_notional_cap(value=cap_value)

        expected_min_price_tick_size = Token.convert_value_to_extended_decimal_format(value=min_price_tick_size)
        expected_min_quantity_tick_size = Token.convert_value_to_extended_decimal_format(value=min_quantity_tick_size)
        expected_maker_fee_rate = Token.convert_value_to_extended_decimal_format(value=maker_fee_rate)
        expected_taker_fee_rate = Token.convert_value_to_extended_decimal_format(value=taker_fee_rate)
        expected_initial_margin_ratio = Token.convert_value_to_extended_decimal_format(value=initial_margin_ratio)
        expected_maintenance_margin_ratio = Token.convert_value_to_extended_decimal_format(value=maintenance_margin_ratio)
        expected_reduce_margin_ratio = Token.convert_value_to_extended_decimal_format(value=reduce_margin_ratio)
        expected_min_notional = Token.convert_value_to_extended_decimal_format(value=min_notional)
        expected_open_notional_cap_value = Token.convert_value_to_extended_decimal_format(value=cap_value)

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
            reduce_margin_ratio=reduce_margin_ratio,
            min_price_tick_size=min_price_tick_size,
            min_quantity_tick_size=min_quantity_tick_size,
            min_notional=min_notional,
            open_notional_cap=open_notional_cap,
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
            "reduceMarginRatio": f"{expected_reduce_margin_ratio.normalize():f}",
            "minPriceTickSize": f"{expected_min_price_tick_size.normalize():f}",
            "minQuantityTickSize": f"{expected_min_quantity_tick_size.normalize():f}",
            "minNotional": f"{expected_min_notional.normalize():f}",
            "openNotionalCap": {
                "capped": {
                    "value": f"{expected_open_notional_cap_value.normalize():f}",
                },
            },
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
        reduce_margin_ratio = Decimal("3")
        min_notional = Decimal("2")
        cap_value = Decimal("1000")
        open_notional_cap = basic_composer.open_notional_cap(value=cap_value)

        expected_min_price_tick_size = Token.convert_value_to_extended_decimal_format(value=min_price_tick_size)
        expected_min_quantity_tick_size = Token.convert_value_to_extended_decimal_format(value=min_quantity_tick_size)
        expected_maker_fee_rate = Token.convert_value_to_extended_decimal_format(value=maker_fee_rate)
        expected_taker_fee_rate = Token.convert_value_to_extended_decimal_format(value=taker_fee_rate)
        expected_initial_margin_ratio = Token.convert_value_to_extended_decimal_format(value=initial_margin_ratio)
        expected_maintenance_margin_ratio = Token.convert_value_to_extended_decimal_format(
            value=maintenance_margin_ratio
        )
        expected_reduce_margin_ratio = Token.convert_value_to_extended_decimal_format(value=reduce_margin_ratio)
        expected_min_notional = Token.convert_value_to_extended_decimal_format(value=min_notional)
        expected_open_notional_cap_value = Token.convert_value_to_extended_decimal_format(value=cap_value)

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
            reduce_margin_ratio=reduce_margin_ratio,
            min_price_tick_size=min_price_tick_size,
            min_quantity_tick_size=min_quantity_tick_size,
            min_notional=min_notional,
            open_notional_cap=open_notional_cap,
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
            "reduceMarginRatio": f"{expected_reduce_margin_ratio.normalize():f}",
            "minPriceTickSize": f"{expected_min_price_tick_size.normalize():f}",
            "minQuantityTickSize": f"{expected_min_quantity_tick_size.normalize():f}",
            "minNotional": f"{expected_min_notional.normalize():f}",
            "openNotionalCap": {
                "capped": {
                    "value": f"{expected_open_notional_cap_value.normalize():f}",
                },
            },
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_spot_order(self, basic_composer):
        market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
        price = Decimal("36.1")
        quantity = Decimal("100")
        order_type = "BUY"
        cid = "test_cid"
        trigger_price = Decimal("43.5")

        order = basic_composer.spot_order(
            market_id=market_id,
            subaccount_id=subaccount_id,
            fee_recipient=fee_recipient,
            price=price,
            quantity=quantity,
            order_type=order_type,
            cid=cid,
            trigger_price=trigger_price,
            expiration_block=1234567,
        )

        expected_price = Token.convert_value_to_extended_decimal_format(value=price)
        expected_quantity = Token.convert_value_to_extended_decimal_format(value=quantity)
        expected_trigger_price = Token.convert_value_to_extended_decimal_format(value=trigger_price)

        expected_order = {
            "marketId": market_id,
            "orderInfo": {
                "subaccountId": subaccount_id,
                "feeRecipient": fee_recipient,
                "price": f"{expected_price.normalize():f}",
                "quantity": f"{expected_quantity.normalize():f}",
                "cid": cid,
            },
            "orderType": order_type,
            "triggerPrice": f"{expected_trigger_price.normalize():f}",
            "expirationBlock": "1234567",
        }
        dict_message = json_format.MessageToDict(
            message=order,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_order

    def test_derivative_order(self, basic_composer):
        market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
        price = Decimal("36.1")
        quantity = Decimal("100")
        margin = price * quantity
        order_type = "BUY"
        cid = "test_cid"
        trigger_price = Decimal("43.5")

        order = basic_composer.derivative_order(
            market_id=market_id,
            subaccount_id=subaccount_id,
            fee_recipient=fee_recipient,
            price=price,
            quantity=quantity,
            margin=margin,
            order_type=order_type,
            cid=cid,
            trigger_price=trigger_price,
            expiration_block=1234567,
        )

        expected_price = Token.convert_value_to_extended_decimal_format(value=price)
        expected_quantity = Token.convert_value_to_extended_decimal_format(value=quantity)
        expected_margin = Token.convert_value_to_extended_decimal_format(value=margin)
        expected_trigger_price = Token.convert_value_to_extended_decimal_format(value=trigger_price)

        expected_order = {
            "marketId": market_id,
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
            "expirationBlock": "1234567",
        }
        dict_message = json_format.MessageToDict(
            message=order,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_order

    def test_msg_create_spot_limit_order(self, basic_composer):
        market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        price = Decimal("36.1")
        quantity = Decimal("100")
        order_type = "BUY"
        cid = "test_cid"
        trigger_price = Decimal("43.5")
        expiration_block = 123456789

        message = basic_composer.msg_create_spot_limit_order(
            market_id=market_id,
            sender=sender,
            subaccount_id=subaccount_id,
            fee_recipient=fee_recipient,
            price=price,
            quantity=quantity,
            order_type=order_type,
            cid=cid,
            trigger_price=trigger_price,
            expiration_block=expiration_block,
        )

        expected_price = Token.convert_value_to_extended_decimal_format(value=price)
        expected_quantity = Token.convert_value_to_extended_decimal_format(value=quantity)
        expected_trigger_price = Token.convert_value_to_extended_decimal_format(value=trigger_price)

        assert "injective.exchange.v2.MsgCreateSpotLimitOrder" == message.DESCRIPTOR.full_name
        expected_message = {
            "sender": sender,
            "order": {
                "marketId": market_id,
                "orderInfo": {
                    "subaccountId": subaccount_id,
                    "feeRecipient": fee_recipient,
                    "price": f"{expected_price.normalize():f}",
                    "quantity": f"{expected_quantity.normalize():f}",
                    "cid": cid,
                },
                "orderType": order_type,
                "triggerPrice": f"{expected_trigger_price.normalize():f}",
                "expirationBlock": str(expiration_block),
            },
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_batch_create_spot_limit_orders(self, basic_composer):
        market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        price = Decimal("36.1")
        quantity = Decimal("100")
        order_type = "BUY"
        cid = "test_cid"
        trigger_price = Decimal("43.5")

        order = basic_composer.spot_order(
            market_id=market_id,
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
        market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        price = Decimal("36.1")
        quantity = Decimal("100")
        order_type = "BUY"
        cid = "test_cid"
        trigger_price = Decimal("43.5")

        message = basic_composer.msg_create_spot_market_order(
            market_id=market_id,
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
                "marketId": market_id,
                "orderInfo": {
                    "subaccountId": subaccount_id,
                    "feeRecipient": fee_recipient,
                    "price": f"{Token.convert_value_to_extended_decimal_format(value=price).normalize():f}",
                    "quantity": f"{Token.convert_value_to_extended_decimal_format(value=quantity).normalize():f}",
                    "cid": cid,
                },
                "orderType": order_type,
                "triggerPrice": f"{Token.convert_value_to_extended_decimal_format(value=trigger_price).normalize():f}",
                "expirationBlock": "0",
            },
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_cancel_spot_order(self, basic_composer):
        market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        order_hash = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        cid = "test_cid"

        message = basic_composer.msg_cancel_spot_order(
            market_id=market_id,
            sender=sender,
            subaccount_id=subaccount_id,
            order_hash=order_hash,
            cid=cid,
        )

        expected_message = {
            "sender": sender,
            "marketId": market_id,
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
        market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"

        order_data = basic_composer.order_data_without_mask(
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hash="0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000",
        )

        message = basic_composer.msg_batch_cancel_spot_orders(
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
        spot_market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        derivative_market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
        binary_options_market_id = "0x00617e128fdc0c0423dd18a1ff454511af14c4db6bdd98005a99cdf8fdbf74e9"

        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"

        spot_order_to_cancel = basic_composer.order_data_without_mask(
            market_id=spot_market_id,
            subaccount_id=subaccount_id,
            order_hash="0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000",
        )
        derivative_order_to_cancel = basic_composer.order_data_without_mask(
            market_id=derivative_market_id,
            subaccount_id=subaccount_id,
            order_hash="0x222daa22f60fe9f075ed0ca583459e121c23e64431c3fbffdedda04598ede0d2",
        )
        binary_options_order_to_cancel = basic_composer.order_data_without_mask(
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
        spot_market_order_to_create = basic_composer.spot_order(
            market_id=spot_market_id,
            subaccount_id=subaccount_id,
            fee_recipient="inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q4r",
            price=Decimal("37"),
            quantity=Decimal("1"),
            order_type="BUY",
            cid="test_cid_spot_market",
        )
        derivative_market_order_to_create = basic_composer.derivative_order(
            market_id=derivative_market_id,
            subaccount_id=subaccount_id,
            fee_recipient="inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q5r",
            price=Decimal("38"),
            quantity=Decimal("1"),
            margin=Decimal("38") * Decimal("1"),
            order_type="BUY",
        )
        binary_options_market_order_to_create = basic_composer.binary_options_order(
            market_id=binary_options_market_id,
            subaccount_id=subaccount_id,
            fee_recipient="inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q6r",
            price=Decimal("39"),
            quantity=Decimal("1"),
            margin=Decimal("39") * Decimal("1"),
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
            spot_market_orders_to_create=[spot_market_order_to_create],
            derivative_market_orders_to_create=[derivative_market_order_to_create],
            binary_options_market_orders_to_create=[binary_options_market_order_to_create],
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
            "spotMarketOrdersToCreate": [
                json_format.MessageToDict(message=spot_market_order_to_create, always_print_fields_with_no_presence=True)
            ],
            "derivativeMarketOrdersToCreate": [
                json_format.MessageToDict(message=derivative_market_order_to_create, always_print_fields_with_no_presence=True)
            ],
            "binaryOptionsMarketOrdersToCreate": [
                json_format.MessageToDict(message=binary_options_market_order_to_create, always_print_fields_with_no_presence=True)
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
        market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        price = Decimal("36.1")
        quantity = Decimal("100")
        margin = price * quantity
        order_type = "BUY"
        cid = "test_cid"
        trigger_price = Decimal("43.5")
        expiration_block = 123456789

        message = basic_composer.msg_create_derivative_limit_order(
            market_id=market_id,
            sender=sender,
            subaccount_id=subaccount_id,
            fee_recipient=fee_recipient,
            price=price,
            quantity=quantity,
            margin=margin,
            order_type=order_type,
            cid=cid,
            trigger_price=trigger_price,
            expiration_block=expiration_block,
        )

        expected_message = {
            "sender": sender,
            "order": {
                "marketId": market_id,
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
                "expirationBlock": str(expiration_block),
            },
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_batch_create_derivative_limit_orders(self, basic_composer):
        market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        price = Decimal("36.1")
        quantity = Decimal("100")
        order_type = "BUY"
        cid = "test_cid"
        trigger_price = Decimal("43.5")

        order = basic_composer.derivative_order(
            market_id=market_id,
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
        market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"

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
            market_id=market_id,
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
                "marketId": market_id,
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
                "expirationBlock": "0",
            },
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_cancel_derivative_order(self, basic_composer):
        market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"

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
            market_id=market_id,
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
            "marketId": market_id,
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
        market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"

        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"

        order_data = basic_composer.order_data_without_mask(
            market_id=market_id,
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
        quote_denom = "inj"
        min_price_tick_size = Decimal("0.01")
        min_quantity_tick_size = Decimal("1")
        maker_fee_rate = Decimal("0.001")
        taker_fee_rate = Decimal("-0.002")
        expiration_timestamp = 1630000000
        settlement_timestamp = 1660000000
        admin = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
        min_notional = Decimal("2")
        cap_value = Decimal("1000")
        open_notional_cap = basic_composer.open_notional_cap(value=cap_value)

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
            min_notional=min_notional,
            open_notional_cap=open_notional_cap,
        )

        chain_min_price_tick_size = Token.convert_value_to_extended_decimal_format(value=min_price_tick_size)
        chain_min_quantity_tick_size = Token.convert_value_to_extended_decimal_format(value=min_quantity_tick_size)
        chain_min_notional = Token.convert_value_to_extended_decimal_format(value=min_notional)
        expected_open_notional_cap_value = Token.convert_value_to_extended_decimal_format(value=cap_value)

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
            "openNotionalCap": {
                "capped": {
                    "value": f"{expected_open_notional_cap_value.normalize():f}",
                },
            },
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_create_binary_options_limit_order(self, basic_composer):
        market_id = "0x767e1542fbc111e88901e223e625a4a8eb6d630c96884bbde672e8bc874075bb"

        subaccount_id = "0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000"
        fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        price = Decimal("36.1")
        quantity = Decimal("100")
        margin = price * quantity
        order_type = "BUY"
        cid = "test_cid"
        trigger_price = Decimal("43.5")
        expiration_block = 123456789

        message = basic_composer.msg_create_binary_options_limit_order(
            market_id=market_id,
            sender=sender,
            subaccount_id=subaccount_id,
            fee_recipient=fee_recipient,
            price=price,
            quantity=quantity,
            margin=margin,
            order_type=order_type,
            cid=cid,
            trigger_price=trigger_price,
            expiration_block=expiration_block,
        )

        expected_price = Token.convert_value_to_extended_decimal_format(value=price)
        expected_quantity = Token.convert_value_to_extended_decimal_format(value=quantity)
        expected_margin = Token.convert_value_to_extended_decimal_format(value=margin)
        expected_trigger_price = Token.convert_value_to_extended_decimal_format(value=trigger_price)

        expected_message = {
            "sender": sender,
            "order": {
                "marketId": market_id,
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
                "expirationBlock": str(expiration_block),
            },
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_create_binary_options_market_order(self, basic_composer):
        market_id = "0x767e1542fbc111e88901e223e625a4a8eb6d630c96884bbde672e8bc874075bb"

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
            market_id=market_id,
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
                "marketId": market_id,
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
                "expirationBlock": "0",
            },
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_cancel_derivative_order(self, basic_composer):
        market_id = "0x767e1542fbc111e88901e223e625a4a8eb6d630c96884bbde672e8bc874075bb"

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
            market_id=market_id,
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
            "marketId": market_id,
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
                "amount": f"{Decimal(str(amount)).normalize():f}",
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

        message = basic_composer.msg_external_transfer(
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
                "amount": f"{Decimal(str(amount)).normalize():f}",
                "denom": denom,
            },
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_liquidate_position(self, basic_composer):
        market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"

        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        subaccount_id = "0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000001"
        order = basic_composer.derivative_order(
            market_id=market_id,
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
            market_id=market_id,
            order=order,
        )

        expected_message = {
            "sender": sender,
            "subaccountId": subaccount_id,
            "marketId": market_id,
            "order": json_format.MessageToDict(message=order, always_print_fields_with_no_presence=True),
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_emergency_settle_market(self, basic_composer):
        market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"

        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        subaccount_id = "0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000001"

        message = basic_composer.msg_emergency_settle_market(
            sender=sender,
            subaccount_id=subaccount_id,
            market_id=market_id,
        )

        expected_message = {
            "sender": sender,
            "subaccountId": subaccount_id,
            "marketId": market_id,
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_increase_position_margin(self, basic_composer):
        market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"

        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        source_subaccount_id = "0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000001"
        destination_subaccount_id = "0xc6fe5d33615a1c52c08018c47e8bc53646a0e101000000000000000000000000"
        amount = Decimal(100)

        expected_amount = Token.convert_value_to_extended_decimal_format(value=amount)

        message = basic_composer.msg_increase_position_margin(
            sender=sender,
            source_subaccount_id=source_subaccount_id,
            destination_subaccount_id=destination_subaccount_id,
            market_id=market_id,
            amount=amount,
        )

        expected_message = {
            "sender": sender,
            "sourceSubaccountId": source_subaccount_id,
            "destinationSubaccountId": destination_subaccount_id,
            "marketId": market_id,
            "amount": f"{expected_amount.normalize():f}",
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_decrease_position_margin(self, basic_composer):
        market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"

        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        source_subaccount_id = "0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000001"
        destination_subaccount_id = "0xc6fe5d33615a1c52c08018c47e8bc53646a0e101000000000000000000000000"
        amount = Decimal(100)

        expected_amount = Token.convert_value_to_extended_decimal_format(value=amount)

        message = basic_composer.msg_decrease_position_margin(
            sender=sender,
            source_subaccount_id=source_subaccount_id,
            destination_subaccount_id=destination_subaccount_id,
            market_id=market_id,
            amount=amount,
        )

        expected_message = {
            "sender": sender,
            "sourceSubaccountId": source_subaccount_id,
            "destinationSubaccountId": destination_subaccount_id,
            "marketId": market_id,
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
        market_id = "0x767e1542fbc111e88901e223e625a4a8eb6d630c96884bbde672e8bc874075bb"

        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        status = "Paused"
        settlement_price = Decimal("100.5")
        expiration_timestamp = 1630000000
        settlement_timestamp = 1660000000

        expected_settlement_price = Token.convert_value_to_extended_decimal_format(value=settlement_price)

        message = basic_composer.msg_admin_update_binary_options_market(
            sender=sender,
            market_id=market_id,
            status=status,
            settlement_price=settlement_price,
            expiration_timestamp=expiration_timestamp,
            settlement_timestamp=settlement_timestamp,
        )

        expected_message = {
            "sender": sender,
            "marketId": market_id,
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
        market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        new_ticker = "NEW/TICKER"
        min_price_tick_size = Decimal("0.0009")
        min_quantity_tick_size = Decimal("10")
        min_notional = Decimal("5")

        expected_min_price_tick_size = Token.convert_value_to_extended_decimal_format(value=min_price_tick_size)
        expected_min_quantity_tick_size = Token.convert_value_to_extended_decimal_format(value=min_quantity_tick_size)
        expected_min_notional = Token.convert_value_to_extended_decimal_format(value=min_notional)

        message = basic_composer.msg_update_spot_market(
            admin=sender,
            market_id=market_id,
            new_ticker=new_ticker,
            new_min_price_tick_size=min_price_tick_size,
            new_min_quantity_tick_size=min_quantity_tick_size,
            new_min_notional=min_notional,
        )

        expected_message = {
            "admin": sender,
            "marketId": market_id,
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
        market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"

        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        new_ticker = "NEW/TICKER"
        min_price_tick_size = Decimal("0.0009")
        min_quantity_tick_size = Decimal("10")
        min_notional = Decimal("5")
        initial_margin_ratio = Decimal("0.05")
        maintenance_margin_ratio = Decimal("0.009")
        reduce_margin_ration = Decimal("3")

        expected_min_price_tick_size = Token.convert_value_to_extended_decimal_format(value=min_price_tick_size)
        expected_min_quantity_tick_size = Token.convert_value_to_extended_decimal_format(value=min_quantity_tick_size)
        expected_min_notional = Token.convert_value_to_extended_decimal_format(value=min_notional)
        expected_initial_margin_ratio = Token.convert_value_to_extended_decimal_format(value=initial_margin_ratio)
        expected_maintenance_margin_ratio = Token.convert_value_to_extended_decimal_format(
            value=maintenance_margin_ratio
        )
        expected_reduce_margin_ratio = Token.convert_value_to_extended_decimal_format(value=reduce_margin_ration)
        open_notional_cap_value = Decimal("100000")
        expected_open_notional_cap_value = Token.convert_value_to_extended_decimal_format(value=open_notional_cap_value)
        open_notional_cap = basic_composer.open_notional_cap(value=open_notional_cap_value)

        message = basic_composer.msg_update_derivative_market(
            admin=sender,
            market_id=market_id,
            new_ticker=new_ticker,
            new_min_price_tick_size=min_price_tick_size,
            new_min_quantity_tick_size=min_quantity_tick_size,
            new_min_notional=min_notional,
            new_initial_margin_ratio=initial_margin_ratio,
            new_maintenance_margin_ratio=maintenance_margin_ratio,
            new_reduce_margin_ratio=reduce_margin_ration,
            new_open_notional_cap=open_notional_cap,
        )

        expected_message = {
            "admin": sender,
            "marketId": market_id,
            "newTicker": new_ticker,
            "newMinPriceTickSize": f"{expected_min_price_tick_size.normalize():f}",
            "newMinQuantityTickSize": f"{expected_min_quantity_tick_size.normalize():f}",
            "newMinNotional": f"{expected_min_notional.normalize():f}",
            "newInitialMarginRatio": f"{expected_initial_margin_ratio.normalize():f}",
            "newMaintenanceMarginRatio": f"{expected_maintenance_margin_ratio.normalize():f}",
            "newReduceMarginRatio": f"{expected_reduce_margin_ratio.normalize():f}",
            "newOpenNotionalCap": {
                "capped": {
                    "value": f"{expected_open_notional_cap_value.normalize():f}",
                },
            },
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
        contract_hook = "contrachook"
        permissions_role1 = basic_composer.permissions_role(
            name="role1",
            role_id=1,
            permissions=5,
        )
        permissions_role2 = basic_composer.permissions_role(
            name="role2",
            role_id=2,
            permissions=6,
        )
        actor_roles1 = basic_composer.permissions_actor_roles(
            actor="actor1",
            roles=["role1"],
        )
        actor_roles2 = basic_composer.permissions_actor_roles(
            actor="actor2",
            roles=["role2"],
        )
        role_manager1 = basic_composer.permissions_role_manager(
            manager="manager1",
            roles=["role1"],
        )
        role_manager2 = basic_composer.permissions_role_manager(
            manager="manager2",
            roles=["role2"],
        )
        policy_status1 = basic_composer.permissions_policy_status(
            action=basic_composer.PERMISSIONS_ACTION["MINT"],
            is_disabled=False,
            is_sealed=True,
        )
        policy_status2 = basic_composer.permissions_policy_status(
            action=basic_composer.PERMISSIONS_ACTION["SEND"] | basic_composer.PERMISSIONS_ACTION["BURN"],
            is_disabled=True,
            is_sealed=False,
        )
        policy_manager_capability1 = basic_composer.permissions_policy_manager_capability(
            manager="manager1",
            action=basic_composer.PERMISSIONS_ACTION["MINT"],
            can_disable=False,
            can_seal=True,
        )
        policy_manager_capability2 = basic_composer.permissions_policy_manager_capability(
            manager="manager2",
            action=basic_composer.PERMISSIONS_ACTION["SEND"] | basic_composer.PERMISSIONS_ACTION["BURN"],
            can_disable=True,
            can_seal=False,
        )

        message = basic_composer.msg_create_namespace(
            sender=sender,
            denom=denom,
            contract_hook=contract_hook,
            role_permissions=[permissions_role1, permissions_role2],
            actor_roles=[actor_roles1, actor_roles2],
            role_managers=[role_manager1, role_manager2],
            policy_statuses=[policy_status1, policy_status2],
            policy_manager_capabilities=[policy_manager_capability1, policy_manager_capability2],
        )

        expected_message = {
            "sender": sender,
            "namespace": {
                "denom": denom,
                "contractHook": contract_hook,
                "rolePermissions": [
                    {
                        "name": permissions_role1.name,
                        "roleId": permissions_role1.role_id,
                        "permissions": permissions_role1.permissions,
                    },
                    {
                        "name": permissions_role2.name,
                        "roleId": permissions_role2.role_id,
                        "permissions": permissions_role2.permissions,
                    },
                ],
                "actorRoles": [
                    {
                        "actor": actor_roles1.actor,
                        "roles": actor_roles1.roles,
                    },
                    {
                        "actor": actor_roles2.actor,
                        "roles": actor_roles2.roles,
                    },
                ],
                "roleManagers": [
                    {
                        "manager": role_manager1.manager,
                        "roles": role_manager1.roles,
                    },
                    {
                        "manager": role_manager2.manager,
                        "roles": role_manager2.roles,
                    },
                ],
                "policyStatuses": [
                    {
                        "action": permissions_pb.Action.Name(policy_status1.action),
                        "isDisabled": policy_status1.is_disabled,
                        "isSealed": policy_status1.is_sealed,
                    },
                    {
                        "action": policy_status2.action,
                        "isDisabled": policy_status2.is_disabled,
                        "isSealed": policy_status2.is_sealed,
                    },
                ],
                "policyManagerCapabilities": [
                    {
                        "manager": policy_manager_capability1.manager,
                        "action": permissions_pb.Action.Name(policy_manager_capability1.action),
                        "canDisable": policy_manager_capability1.can_disable,
                        "canSeal": policy_manager_capability1.can_seal,
                    },
                    {
                        "manager": policy_manager_capability2.manager,
                        "action": policy_manager_capability2.action,
                        "canDisable": policy_manager_capability2.can_disable,
                        "canSeal": policy_manager_capability2.can_seal,
                    },
                ],
            },
        }

        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_update_namespace(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        denom = "inj"
        contract_hook = "contracthook"
        permissions_role1 = basic_composer.permissions_role(
            name="role1",
            role_id=1,
            permissions=5,
        )
        permissions_role2 = basic_composer.permissions_role(
            name="role2",
            role_id=2,
            permissions=6,
        )
        role_manager1 = basic_composer.permissions_role_manager(
            manager="manager1",
            roles=["role1"],
        )
        role_manager2 = basic_composer.permissions_role_manager(
            manager="manager2",
            roles=["role2"],
        )
        policy_status1 = basic_composer.permissions_policy_status(
            action=basic_composer.PERMISSIONS_ACTION["MINT"],
            is_disabled=False,
            is_sealed=True,
        )
        policy_status2 = basic_composer.permissions_policy_status(
            action=basic_composer.PERMISSIONS_ACTION["SEND"] | basic_composer.PERMISSIONS_ACTION["BURN"],
            is_disabled=True,
            is_sealed=False,
        )
        policy_manager_capability1 = basic_composer.permissions_policy_manager_capability(
            manager="manager1",
            action=basic_composer.PERMISSIONS_ACTION["MINT"],
            can_disable=False,
            can_seal=True,
        )
        policy_manager_capability2 = basic_composer.permissions_policy_manager_capability(
            manager="manager2",
            action=basic_composer.PERMISSIONS_ACTION["SEND"] | basic_composer.PERMISSIONS_ACTION["BURN"],
            can_disable=True,
            can_seal=False,
        )

        message = basic_composer.msg_update_namespace(
            sender=sender,
            denom=denom,
            contract_hook=contract_hook,
            role_permissions=[permissions_role1, permissions_role2],
            role_managers=[role_manager1, role_manager2],
            policy_statuses=[policy_status1, policy_status2],
            policy_manager_capabilities=[policy_manager_capability1, policy_manager_capability2],
        )

        expected_message = {
            "sender": sender,
            "denom": denom,
            "contractHook": {
                "newValue": contract_hook,
            },
            "rolePermissions": [
                {
                    "name": permissions_role1.name,
                    "roleId": permissions_role1.role_id,
                    "permissions": permissions_role1.permissions,
                },
                {
                    "name": permissions_role2.name,
                    "roleId": permissions_role2.role_id,
                    "permissions": permissions_role2.permissions,
                },
            ],
            "roleManagers": [
                {
                    "manager": role_manager1.manager,
                    "roles": role_manager1.roles,
                },
                {
                    "manager": role_manager2.manager,
                    "roles": role_manager2.roles,
                },
            ],
            "policyStatuses": [
                {
                    "action": permissions_pb.Action.Name(policy_status1.action),
                    "isDisabled": policy_status1.is_disabled,
                    "isSealed": policy_status1.is_sealed,
                },
                {
                    "action": policy_status2.action,
                    "isDisabled": policy_status2.is_disabled,
                    "isSealed": policy_status2.is_sealed,
                },
            ],
            "policyManagerCapabilities": [
                {
                    "manager": policy_manager_capability1.manager,
                    "action": permissions_pb.Action.Name(policy_manager_capability1.action),
                    "canDisable": policy_manager_capability1.can_disable,
                    "canSeal": policy_manager_capability1.can_seal,
                },
                {
                    "manager": policy_manager_capability2.manager,
                    "action": policy_manager_capability2.action,
                    "canDisable": policy_manager_capability2.can_disable,
                    "canSeal": policy_manager_capability2.can_seal,
                },
            ],
        }

        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_update_actor_roles(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        denom = "inj"
        role_actors1 = basic_composer.permissions_role_actors(
            role="role1",
            actors=["actor1"],
        )
        role_actors2 = basic_composer.permissions_role_actors(
            role="role2",
            actors=["actor2"],
        )
        role_actors3 = basic_composer.permissions_role_actors(
            role="role3",
            actors=["actor3"],
        )
        role_actors4 = basic_composer.permissions_role_actors(
            role="role4",
            actors=["actor4"],
        )

        message = basic_composer.msg_update_actor_roles(
            sender=sender,
            denom=denom,
            role_actors_to_add=[role_actors1, role_actors2],
            role_actors_to_revoke=[role_actors3, role_actors4],
        )

        expected_message = {
            "sender": sender,
            "denom": denom,
            "roleActorsToAdd": [
                {
                    "role": role_actors1.role,
                    "actors": role_actors1.actors,
                },
                {
                    "role": role_actors2.role,
                    "actors": role_actors2.actors,
                },
            ],
            "roleActorsToRevoke": [
                {
                    "role": role_actors3.role,
                    "actors": role_actors3.actors,
                },
                {
                    "role": role_actors4.role,
                    "actors": role_actors4.actors,
                },
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

    def test_order_data_without_mask(self, basic_composer):
        market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"

        order_data = basic_composer.order_data_without_mask(
            market_id=market_id,
            subaccount_id="subaccount_id",
            order_hash="0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000",
        )

        expected_message = {
            "marketId": market_id,
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
                "amount": f"{Decimal('1').normalize():f}",
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
                "amount": f"{Decimal(1).normalize():f}",
                "denom": "peggy0x44C21afAaF20c270EBbF5914Cfc3b5022173FEB7",
            },
            "bridgeFee": {
                "amount": f"{Decimal(2).normalize():f}",
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
                "amount": f"{Decimal('1').normalize():f}",
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
                    "amount": f"{Decimal('1').normalize():f}",
                    "denom": "peggy0x44C21afAaF20c270EBbF5914Cfc3b5022173FEB7",
                },
            ],
        }
        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_create_token_pair(self, basic_composer):
        message = basic_composer.msg_create_token_pair(
            sender="sender",
            bank_denom="denom",
            erc20_address="erc20_address",
        )

        expected_message = {
            "sender": "sender",
            "tokenPair": {
                "bankDenom": "denom",
                "erc20Address": "erc20_address",
            },
        }

        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_delete_token_pair(self, basic_composer):
        message = basic_composer.msg_delete_token_pair(
            sender="sender",
            bank_denom="denom",
        )

        expected_message = {
            "sender": "sender",
            "bankDenom": "denom",
        }

        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_msg_cancel_post_only_mode(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"

        message = basic_composer.msg_cancel_post_only_mode(
            sender=sender,
        )

        assert "injective.exchange.v2.MsgCancelPostOnlyMode" == message.DESCRIPTOR.full_name
        expected_message = {
            "sender": sender,
        }

        dict_message = json_format.MessageToDict(
            message=message,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_open_notional_cap(self, basic_composer):
        cap_value = Decimal("100000")
        expected_cap_value = Token.convert_value_to_extended_decimal_format(value=cap_value)

        open_notional_cap = basic_composer.open_notional_cap(value=cap_value)

        expected_message = {
            "capped": {
                "value": f"{expected_cap_value.normalize():f}",
            },
        }

        dict_message = json_format.MessageToDict(
            message=open_notional_cap,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_uncapped_open_notional_cap(self, basic_composer):
        open_notional_cap = basic_composer.uncapped_open_notional_cap()

        expected_message = {
            "uncapped": {},
        }

        dict_message = json_format.MessageToDict(
            message=open_notional_cap,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_chain_stream_bank_balances_filter(self, basic_composer):
        accounts = ["inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0", "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"]

        filter_result = basic_composer.chain_stream_bank_balances_filter(accounts=accounts)

        expected_message = {
            "accounts": accounts,
        }

        dict_message = json_format.MessageToDict(
            message=filter_result,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_chain_stream_bank_balances_filter_default(self, basic_composer):
        filter_result = basic_composer.chain_stream_bank_balances_filter()

        expected_message = {
            "accounts": ["*"],
        }

        dict_message = json_format.MessageToDict(
            message=filter_result,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_chain_stream_subaccount_deposits_filter(self, basic_composer):
        subaccount_ids = [
            "0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000001",
            "0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000002",
        ]

        filter_result = basic_composer.chain_stream_subaccount_deposits_filter(subaccount_ids=subaccount_ids)

        expected_message = {
            "subaccountIds": subaccount_ids,
        }

        dict_message = json_format.MessageToDict(
            message=filter_result,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_chain_stream_subaccount_deposits_filter_default(self, basic_composer):
        filter_result = basic_composer.chain_stream_subaccount_deposits_filter()

        expected_message = {
            "subaccountIds": ["*"],
        }

        dict_message = json_format.MessageToDict(
            message=filter_result,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_chain_stream_trades_filter(self, basic_composer):
        subaccount_ids = [
            "0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000001",
            "0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000002",
        ]
        market_ids = [
            "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
        ]

        filter_result = basic_composer.chain_stream_trades_filter(
            subaccount_ids=subaccount_ids, market_ids=market_ids
        )

        expected_message = {
            "subaccountIds": subaccount_ids,
            "marketIds": market_ids,
        }

        dict_message = json_format.MessageToDict(
            message=filter_result,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_chain_stream_trades_filter_default(self, basic_composer):
        filter_result = basic_composer.chain_stream_trades_filter()

        expected_message = {
            "subaccountIds": ["*"],
            "marketIds": ["*"],
        }

        dict_message = json_format.MessageToDict(
            message=filter_result,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_chain_stream_orders_filter(self, basic_composer):
        subaccount_ids = [
            "0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000001",
            "0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000002",
        ]
        market_ids = [
            "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
        ]

        filter_result = basic_composer.chain_stream_orders_filter(
            subaccount_ids=subaccount_ids, market_ids=market_ids
        )

        expected_message = {
            "subaccountIds": subaccount_ids,
            "marketIds": market_ids,
        }

        dict_message = json_format.MessageToDict(
            message=filter_result,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_chain_stream_orders_filter_default(self, basic_composer):
        filter_result = basic_composer.chain_stream_orders_filter()

        expected_message = {
            "subaccountIds": ["*"],
            "marketIds": ["*"],
        }

        dict_message = json_format.MessageToDict(
            message=filter_result,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_chain_stream_orderbooks_filter(self, basic_composer):
        market_ids = [
            "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
        ]

        filter_result = basic_composer.chain_stream_orderbooks_filter(market_ids=market_ids)

        expected_message = {
            "marketIds": market_ids,
        }

        dict_message = json_format.MessageToDict(
            message=filter_result,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_chain_stream_orderbooks_filter_default(self, basic_composer):
        filter_result = basic_composer.chain_stream_orderbooks_filter()

        expected_message = {
            "marketIds": ["*"],
        }

        dict_message = json_format.MessageToDict(
            message=filter_result,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_chain_stream_positions_filter(self, basic_composer):
        subaccount_ids = [
            "0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000001",
            "0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000002",
        ]
        market_ids = [
            "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
        ]

        filter_result = basic_composer.chain_stream_positions_filter(
            subaccount_ids=subaccount_ids, market_ids=market_ids
        )

        expected_message = {
            "subaccountIds": subaccount_ids,
            "marketIds": market_ids,
        }

        dict_message = json_format.MessageToDict(
            message=filter_result,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_chain_stream_positions_filter_default(self, basic_composer):
        filter_result = basic_composer.chain_stream_positions_filter()

        expected_message = {
            "subaccountIds": ["*"],
            "marketIds": ["*"],
        }

        dict_message = json_format.MessageToDict(
            message=filter_result,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_chain_stream_oracle_price_filter(self, basic_composer):
        symbols = ["BTC/USD", "ETH/USD", "INJ/USD"]

        filter_result = basic_composer.chain_stream_oracle_price_filter(symbols=symbols)

        expected_message = {
            "symbol": symbols,
        }

        dict_message = json_format.MessageToDict(
            message=filter_result,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_chain_stream_oracle_price_filter_default(self, basic_composer):
        filter_result = basic_composer.chain_stream_oracle_price_filter()

        expected_message = {
            "symbol": ["*"],
        }

        dict_message = json_format.MessageToDict(
            message=filter_result,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_chain_stream_order_failures_filter(self, basic_composer):
        accounts = ["inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0", "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"]

        filter_result = basic_composer.chain_stream_order_failures_filter(accounts=accounts)

        expected_message = {
            "accounts": accounts,
        }

        dict_message = json_format.MessageToDict(
            message=filter_result,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_chain_stream_order_failures_filter_default(self, basic_composer):
        filter_result = basic_composer.chain_stream_order_failures_filter()

        expected_message = {
            "accounts": ["*"],
        }

        dict_message = json_format.MessageToDict(
            message=filter_result,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_chain_stream_conditional_order_trigger_failures_filter(self, basic_composer):
        subaccount_ids = [
            "0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000001",
            "0x893f2abf8034627e50cbc63923120b1122503ce0000000000000000000000002",
        ]
        market_ids = [
            "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
        ]

        filter_result = basic_composer.chain_stream_conditional_order_trigger_failures_filter(
            subaccount_ids=subaccount_ids, market_ids=market_ids
        )

        expected_message = {
            "subaccountIds": subaccount_ids,
            "marketIds": market_ids,
        }

        dict_message = json_format.MessageToDict(
            message=filter_result,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message

    def test_chain_stream_conditional_order_trigger_failures_filter_default(self, basic_composer):
        filter_result = basic_composer.chain_stream_conditional_order_trigger_failures_filter()

        expected_message = {
            "subaccountIds": ["*"],
            "marketIds": ["*"],
        }

        dict_message = json_format.MessageToDict(
            message=filter_result,
            always_print_fields_with_no_presence=True,
        )
        assert dict_message == expected_message
