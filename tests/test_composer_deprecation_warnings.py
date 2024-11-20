import warnings
from decimal import Decimal

import pytest

from pyinjective.composer import Composer
from pyinjective.core.network import Network
from pyinjective.proto.injective.oracle.v1beta1 import oracle_pb2 as oracle_pb
from tests.model_fixtures.markets_fixtures import (  # noqa: F401
    btc_usdt_perp_market,
    first_match_bet_market,
    inj_token,
    inj_usdt_spot_market,
    usdt_perp_token,
    usdt_token,
)


class TestComposerDeprecationWarnings:
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

    def test_chain_stream_bank_balances_filter_deprecation_warning(self):
        composer = Composer(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.chain_stream_bank_balances_filter(accounts=["account"])

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use chain_stream_bank_balances_v2_filter instead"
        )

    def test_chain_stream_subaccount_deposits_filter_deprecation_warning(self):
        composer = Composer(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.chain_stream_subaccount_deposits_filter()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use chain_stream_subaccount_deposits_v2_filter instead"
        )

    def test_chain_stream_trades_filter_deprecation_warning(self):
        composer = Composer(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.chain_stream_trades_filter()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use chain_stream_trades_v2_filter instead"
        )

    def test_chain_stream_orders_filter_deprecation_warning(self):
        composer = Composer(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.chain_stream_orders_filter()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use chain_stream_orders_v2_filter instead"
        )

    def test_chain_stream_orderbooks_filter_deprecation_warning(self):
        composer = Composer(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.chain_stream_orderbooks_filter()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use chain_stream_orderbooks_v2_filter instead"
        )

    def test_chain_stream_positions_filter_deprecation_warning(self):
        composer = Composer(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.chain_stream_positions_filter()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use chain_stream_positions_v2_filter instead"
        )

    def test_chain_stream_oracle_price_filter_deprecation_warning(self):
        composer = Composer(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.chain_stream_oracle_price_filter()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use chain_stream_oracle_price_v2_filter instead"
        )

    def test_msg_grant_typed_deprecation_warning(self):
        composer = Composer(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgGrantTyped(
                granter="granter",
                grantee="grantee",
                msg_type="CreateSpotLimitOrderAuthz",
                expire_in=100,
                subaccount_id="subaccount_id",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use create_typed_msg_grant instead"

    def test_spot_order_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.spot_order(
                market_id=list(basic_composer.spot_markets.keys())[0],
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal("1"),
                quantity=Decimal("1"),
                order_type="BUY",
                cid="cid",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use create_spot_order_v2 instead"

    def test_basic_derivative_order_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer._basic_derivative_order(
                market_id=list(basic_composer.spot_markets.keys())[0],
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                chain_price=Decimal("1"),
                chain_quantity=Decimal("1"),
                chain_margin=Decimal("1"),
                order_type="BUY",
                cid="cid",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message) == "This method is deprecated. Use _basic_derivative_order_v2 instead"
        )

    def test_derivative_order_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.derivative_order(
                market_id=list(basic_composer.derivative_markets.keys())[0],
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal("1"),
                quantity=Decimal("1"),
                margin=Decimal("1"),
                order_type="BUY",
                cid="cid",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 2
        assert (
            str(deprecation_warnings[0].message) == "This method is deprecated. Use create_derivative_order_v2 instead"
        )

    def test_binary_options_order_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.binary_options_order(
                market_id=list(basic_composer.binary_option_markets.keys())[0],
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal("1"),
                quantity=Decimal("1"),
                margin=Decimal("1"),
                order_type="BUY",
                cid="cid",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 2
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use create_binary_options_order_v2 instead"
        )

    def test_msg_batch_create_spot_limit_orders_deprecation_warning(self, basic_composer):
        order = basic_composer.spot_order(
            market_id=list(basic_composer.spot_markets.keys())[0],
            subaccount_id="subaccount_id",
            fee_recipient="fee_recipient",
            price=Decimal("1"),
            quantity=Decimal("1"),
            order_type="BUY",
            cid="cid",
        )
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_batch_create_spot_limit_orders(sender="sender", orders=[order])

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_batch_create_spot_limit_orders_v2 instead"
        )

    def test_msg_create_spot_market_order_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_create_spot_market_order(
                market_id=list(basic_composer.spot_markets.keys())[0],
                sender="sender",
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal("1"),
                quantity=Decimal("1"),
                order_type="BUY",
                cid="cid",
                trigger_price=Decimal("1"),
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 2
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_create_spot_market_order_v2 instead"
        )

    def test_msg_cancel_spot_order_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_cancel_spot_order(
                market_id=list(basic_composer.spot_markets.keys())[0],
                sender="sender",
                subaccount_id="subaccount_id",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_cancel_spot_order_v2 instead"

    def test_msg_batch_cancel_spot_orders_deprecation_warning(self, basic_composer):
        order_data = basic_composer.order_data(
            market_id=list(basic_composer.spot_markets.keys())[0],
            subaccount_id="subaccount_id",
            order_hash="0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000",
        )

        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_batch_cancel_spot_orders(
                sender="sender",
                orders_data=[order_data],
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_batch_cancel_spot_orders_v2 instead"
        )

    def test_order_data_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.order_data(
                market_id=list(basic_composer.spot_markets.keys())[0],
                subaccount_id="subaccount_id",
                order_hash="0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use create_order_data_v2 instead"

    def test_order_data_without_mask_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.order_data_without_mask(
                market_id=list(basic_composer.spot_markets.keys())[0],
                subaccount_id="subaccount_id",
                order_hash="0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use create_order_data_without_mask_v2 instead"
        )

    def test_msg_batch_update_orders_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_batch_update_orders(
                sender="sender",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_batch_update_orders_v2 instead"
        )

    def test_msg_privileged_execute_contract_deprecation_warning(self, basic_composer):
        sender = "inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0"
        contract_address = "inj1ady3s7whq30l4fx8sj3x6muv5mx4dfdlcpv8n7"
        data = "test_data"
        funds = "100inj,420peggy0x44C21afAaF20c270EBbF5914Cfc3b5022173FEB7"

        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_privileged_execute_contract(
                sender=sender,
                contract_address=contract_address,
                data=data,
                funds=funds,
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_privileged_execute_contract_v2 instead"
        )

    def test_msg_create_derivative_limit_order_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_create_derivative_limit_order(
                market_id=list(basic_composer.derivative_markets.keys())[0],
                sender="sender",
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal("1"),
                quantity=Decimal("1"),
                margin=Decimal("1"),
                order_type="BUY",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 3
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_create_derivative_limit_order_v2 instead"
        )

    def test_msg_batch_create_derivative_limit_orders_deprecation_warning(self, basic_composer):
        order = basic_composer.derivative_order(
            market_id=list(basic_composer.derivative_markets.keys())[0],
            subaccount_id="subaccount_id",
            fee_recipient="fee_recipient",
            price=Decimal("1"),
            quantity=Decimal("1"),
            margin=Decimal("1"),
            order_type="BUY",
            cid="cid",
        )

        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_batch_create_derivative_limit_orders(
                sender="sender",
                orders=[order],
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_batch_create_derivative_limit_orders_v2 instead"
        )

    def test_msg_create_derivative_market_order_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_create_derivative_market_order(
                market_id=list(basic_composer.derivative_markets.keys())[0],
                sender="sender",
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal("1"),
                quantity=Decimal("1"),
                margin=Decimal("1"),
                order_type="BUY",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 3
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_create_derivative_market_order_v2 instead"
        )

    def test_msg_cancel_derivative_order_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_cancel_derivative_order(
                market_id=list(basic_composer.derivative_markets.keys())[0],
                sender="sender",
                subaccount_id="subaccount_id",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_cancel_derivative_order_v2 instead"
        )

    def test_msg_batch_cancel_derivative_orders_deprecation_warning(self, basic_composer):
        order_data = basic_composer.order_data_without_mask(
            market_id=list(basic_composer.derivative_markets.keys())[0],
            subaccount_id="subaccount_id",
            order_hash="0x5e249f0e8cb406f41de16e1bd6f6b55e7bc75add000000000000000000000000",
        )

        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_batch_cancel_derivative_orders(
                sender="sender",
                orders_data=[order_data],
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_batch_cancel_derivative_orders_v2 instead"
        )

    def test_msg_instant_binary_options_market_launch_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_instant_binary_options_market_launch(
                sender="sender",
                ticker="ticker",
                oracle_symbol="oracle_symbol",
                oracle_provider="oracle_provider",
                oracle_type="Band",
                oracle_scale_factor=6,
                maker_fee_rate=Decimal("0.1"),
                taker_fee_rate=Decimal("0.1"),
                expiration_timestamp=1707800399,
                settlement_timestamp=1707843599,
                admin="admin",
                quote_denom=list(basic_composer.binary_option_markets.values())[0].quote_token.symbol,
                min_price_tick_size=Decimal("1"),
                min_quantity_tick_size=Decimal("1"),
                min_notional=Decimal("1"),
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_instant_binary_options_market_launch_v2 instead"
        )

    def test_msg_create_binary_options_market_order_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_create_binary_options_market_order(
                market_id=list(basic_composer.binary_option_markets.keys())[0],
                sender="sender",
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal("1"),
                quantity=Decimal("1"),
                margin=Decimal("1"),
                order_type="BUY",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 3
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_create_binary_options_market_order_v2 instead"
        )

    def test_msg_cancel_binary_options_order_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_cancel_binary_options_order(
                market_id=list(basic_composer.derivative_markets.keys())[0],
                sender="sender",
                subaccount_id="subaccount_id",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_cancel_binary_options_order_v2 instead"
        )

    def test_msg_subaccount_transfer_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_subaccount_transfer(
                sender="sender",
                source_subaccount_id="source_subaccount_id",
                destination_subaccount_id="destination_subaccount_id",
                amount=Decimal("1"),
                denom="INJ",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_subaccount_transfer_v2 instead"
        )

    def test_msg_deposit_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_deposit(
                sender="sender",
                subaccount_id="source_subaccount_id",
                amount=Decimal("1"),
                denom="INJ",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_deposit_v2 instead"

    def test_msg_external_transfer_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_external_transfer(
                sender="sender",
                source_subaccount_id="source_subaccount_id",
                destination_subaccount_id="destination_subaccount_id",
                amount=Decimal("1"),
                denom="INJ",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_external_transfer_v2 instead"

    def test_msg_withdraw_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_withdraw(
                sender="sender",
                subaccount_id="subaccount_id",
                amount=Decimal("1"),
                denom="INJ",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_withdraw_v2 instead"

    def test_msg_create_insurance_fund_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.MsgCreateInsuranceFund(
                sender="sender",
                ticker="ticker",
                quote_denom="INJ",
                oracle_base="oracle_base",
                oracle_quote="oracle_quote",
                oracle_type=oracle_pb.OracleType.Band,
                expiry=-1,
                initial_deposit=1,
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_create_insurance_fund instead"
        )

    def test_msg_send_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.MsgSend(
                from_address="from_address",
                to_address="to_address",
                amount=1,
                denom="INJ",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_send instead"

    def test_msg_send_to_eth_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.MsgSendToEth(
                denom="INJ",
                sender="sender",
                eth_dest="eth_dest",
                amount=1,
                bridge_fee=1,
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_send_to_eth instead"

    def test_msg_underwrite_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.MsgUnderwrite(
                sender="sender",
                market_id="market_id",
                quote_denom="INJ",
                amount=1,
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_underwrite instead"

    def test_msg_instant_spot_market_launch_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_instant_spot_market_launch(
                sender="sender",
                ticker="ticker",
                base_denom=list(basic_composer.spot_markets.values())[0].base_token.symbol,
                quote_denom=list(basic_composer.spot_markets.values())[0].quote_token.symbol,
                min_price_tick_size=Decimal("1"),
                min_quantity_tick_size=Decimal("1"),
                min_notional=Decimal("1"),
                base_decimals=6,
                quote_decimals=6,
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_instant_spot_market_launch_v2 instead"
        )

    def test_msg_instant_perpetual_market_launch_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_instant_perpetual_market_launch(
                sender="sender",
                ticker="ticker",
                quote_denom=list(basic_composer.spot_markets.values())[0].quote_token.symbol,
                oracle_base="oracle_base",
                oracle_quote="oracle_quote",
                oracle_scale_factor=6,
                oracle_type="Band",
                maker_fee_rate=Decimal("0.1"),
                taker_fee_rate=Decimal("0.1"),
                initial_margin_ratio=Decimal("0.1"),
                maintenance_margin_ratio=Decimal("0.1"),
                min_price_tick_size=Decimal("1"),
                min_quantity_tick_size=Decimal("1"),
                min_notional=Decimal("1"),
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_instant_perpetual_market_launch_v2 instead"
        )

    def test_msg_liquidate_position_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_liquidate_position(
                sender="sender",
                subaccount_id="subaccount_id",
                market_id="market_id",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_liquidate_position_v2 instead"
        )

    def test_msg_instant_expiry_futures_market_launch_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_instant_expiry_futures_market_launch(
                sender="sender",
                ticker="ticker",
                quote_denom=list(basic_composer.spot_markets.values())[0].quote_token.symbol,
                oracle_base="oracle_base",
                oracle_quote="oracle_quote",
                oracle_scale_factor=6,
                oracle_type="Band",
                expiry=1707800399,
                maker_fee_rate=Decimal("0.1"),
                taker_fee_rate=Decimal("0.1"),
                initial_margin_ratio=Decimal("0.1"),
                maintenance_margin_ratio=Decimal("0.1"),
                min_price_tick_size=Decimal("1"),
                min_quantity_tick_size=Decimal("1"),
                min_notional=Decimal("1"),
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_instant_expiry_futures_market_launch_v2 instead"
        )

    def test_msg_create_spot_limit_order_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_create_spot_limit_order(
                market_id=list(basic_composer.spot_markets.keys())[0],
                sender="sender",
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal("1"),
                quantity=Decimal("1"),
                order_type="BUY",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 2
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_create_spot_limit_order_v2 instead"
        )

    def test_msg_create_binary_options_limit_order_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_create_binary_options_limit_order(
                market_id=list(basic_composer.binary_option_markets.keys())[0],
                sender="sender",
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal("1"),
                quantity=Decimal("1"),
                margin=Decimal("1"),
                order_type="BUY",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 3
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_create_binary_options_limit_order_v2 instead"
        )

    def test_msg_emergency_settle_market_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_emergency_settle_market(
                sender="sender",
                subaccount_id="subaccount_id",
                market_id="market_id",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_emergency_settle_market_v2 instead"
        )

    def test_msg_increase_position_margin_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_increase_position_margin(
                sender="sender",
                source_subaccount_id="source_subaccount_id",
                destination_subaccount_id="destination_subaccount_id",
                market_id=list(basic_composer.derivative_markets.keys())[0],
                amount=Decimal("1"),
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_increase_position_margin_v2 instead"
        )

    def test_msg_decrease_position_margin_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_decrease_position_margin(
                sender="sender",
                source_subaccount_id="source_subaccount_id",
                destination_subaccount_id="destination_subaccount_id",
                market_id=list(basic_composer.derivative_markets.keys())[0],
                amount=Decimal("1"),
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_decrease_position_margin_v2 instead"
        )

    def test_msg_admin_update_binary_options_market_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_admin_update_binary_options_market(
                sender="sender",
                market_id=list(basic_composer.binary_option_markets.keys())[0],
                status="Expired",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_admin_update_binary_options_market_v2 instead"
        )

    def test_msg_update_spot_market_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_update_spot_market(
                admin="admin",
                market_id=list(basic_composer.spot_markets.keys())[0],
                new_ticker="new_ticker",
                new_min_price_tick_size=Decimal("1"),
                new_min_quantity_tick_size=Decimal("2"),
                new_min_notional=Decimal("3"),
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_update_spot_market_v2 instead"
        )

    def test_msg_update_derivative_market_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.msg_update_derivative_market(
                admin="admin",
                market_id=list(basic_composer.derivative_markets.keys())[0],
                new_ticker="new_ticker",
                new_min_price_tick_size=Decimal("1"),
                new_min_quantity_tick_size=Decimal("2"),
                new_min_notional=Decimal("3"),
                new_initial_margin_ratio=Decimal("0.1"),
                new_maintenance_margin_ratio=Decimal("0.05"),
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_update_derivative_market_v2 instead"
        )
