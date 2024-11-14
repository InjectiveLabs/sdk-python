import warnings
from decimal import Decimal

import pytest

from pyinjective.composer import Composer
from pyinjective.core.network import Network
from tests.model_fixtures.markets_fixtures import btc_usdt_perp_market  # noqa: F401
from tests.model_fixtures.markets_fixtures import first_match_bet_market  # noqa: F401
from tests.model_fixtures.markets_fixtures import inj_token  # noqa: F401
from tests.model_fixtures.markets_fixtures import inj_usdt_spot_market  # noqa: F401
from tests.model_fixtures.markets_fixtures import usdt_perp_token  # noqa: F401
from tests.model_fixtures.markets_fixtures import usdt_token  # noqa: F401


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

    def test_msg_deposit_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.MsgDeposit(sender="sender", subaccount_id="subaccount id", amount=1, denom="INJ")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_deposit instead"

    def test_msg_withdraw_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.MsgWithdraw(sender="sender", subaccount_id="subaccount id", amount=1, denom="USDT")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_withdraw instead"

    def test_coin_deprecation_warning(self):
        composer = Composer(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.Coin(
                amount=1,
                denom="INJ",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use coin instead"

    def test_order_data_deprecation_warning(self):
        composer = Composer(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.OrderData(
                market_id="market id",
                subaccount_id="subaccount id",
                order_hash="order hash",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use order_data instead"

    def test_spot_order_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            market_id = list(basic_composer.spot_markets.keys())[0]
            basic_composer.SpotOrder(
                market_id=market_id,
                subaccount_id="subaccount id",
                fee_recipient="fee recipient",
                price=1,
                quantity=1,
                is_buy=True,
                cid="cid",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use spot_order instead"

    def test_derivative_order_deprecation_warning(self, basic_composer):
        market_id = list(basic_composer.derivative_markets.keys())[0]
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.DerivativeOrder(
                market_id=market_id,
                subaccount_id="subaccount id",
                fee_recipient="fee recipient",
                price=1,
                quantity=1,
                is_buy=True,
                cid="cid",
                leverage=1,
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use derivative_order instead"

    def test_msg_create_spot_limit_order_deprecation_warning(self, basic_composer):
        market_id = list(basic_composer.spot_markets.keys())[0]
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.MsgCreateSpotLimitOrder(
                market_id=market_id,
                sender="sender",
                subaccount_id="subaccount id",
                fee_recipient="fee recipient",
                price=1,
                quantity=1,
                cid="cid",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_create_spot_limit_order instead"
        )

    def test_msg_batch_create_spot_limit_orders_deprecation_warning(self, basic_composer):
        market_id = list(basic_composer.spot_markets.keys())[0]
        order = basic_composer.spot_order(
            market_id=market_id,
            subaccount_id="subaccount id",
            fee_recipient="fee recipient",
            price=Decimal(1),
            quantity=Decimal(1),
            order_type="BUY",
        )

        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.MsgBatchCreateSpotLimitOrders(
                sender="sender",
                orders=[order],
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_batch_create_spot_limit_orders instead"
        )

    def test_msg_create_spot_market_order_deprecation_warning(self, basic_composer):
        market_id = list(basic_composer.spot_markets.keys())[0]
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.MsgCreateSpotMarketOrder(
                market_id=market_id,
                sender="sender",
                subaccount_id="subaccount id",
                fee_recipient="fee recipient",
                price=1,
                quantity=1,
                is_buy=True,
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_create_spot_market_order instead"
        )

    def test_msg_cancel_spot_order_deprecation_warning(self):
        composer = Composer(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgCancelSpotOrder(
                market_id="0xa508cb32923323679f29a032c70342c147c17d0145625922b0ef22e955c844c0",
                sender="sender",
                subaccount_id="subaccount id",
                order_hash="order hash",
                cid="cid",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_cancel_spot_order instead"

    def test_msg_batch_cancel_spot_orders_deprecation_warning(self):
        composer = Composer(network=Network.devnet().string())
        orders = [
            composer.order_data(
                market_id="0xa508cb32923323679f29a032c70342c147c17d0145625922b0ef22e955c844c0",
                subaccount_id="subaccount_id",
                order_hash="0x3870fbdd91f07d54425147b1bb96404f4f043ba6335b422a6d494d285b387f2d",
            ),
        ]

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgBatchCancelSpotOrders(sender="sender", data=orders)

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_batch_cancel_spot_orders instead"
        )

    def test_msg_batch_update_orders_deprecation_warning(self):
        composer = Composer(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgBatchUpdateOrders(sender="sender")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_batch_update_orders instead"

    def test_msg_privileged_execute_contract_deprecation_warning(self):
        composer = Composer(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgPrivilegedExecuteContract(
                sender="sender",
                contract="contract",
                msg="msg",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_privileged_execute_contract instead"
        )

    def test_msg_create_derivative_limit_order_deprecation_warning(self, basic_composer):
        market_id = list(basic_composer.derivative_markets.keys())[0]
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.MsgCreateDerivativeLimitOrder(
                market_id=market_id,
                sender="sender",
                subaccount_id="subaccount id",
                fee_recipient="fee recipient",
                price=1,
                quantity=1,
                cid="cid",
                leverage=1,
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_create_derivative_limit_order instead"
        )

    def test_msg_batch_create_derivative_limit_orders_deprecation_warning(self, basic_composer):
        market_id = list(basic_composer.derivative_markets.keys())[0]
        order = basic_composer.derivative_order(
            market_id=market_id,
            subaccount_id="subaccount id",
            fee_recipient="fee recipient",
            price=Decimal(1),
            quantity=Decimal(1),
            margin=Decimal(1),
            order_type="BUY",
        )

        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.MsgBatchCreateDerivativeLimitOrders(
                sender="sender",
                orders=[order],
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_batch_create_derivative_limit_orders instead"
        )

    def test_msg_create_derivative_market_order_deprecation_warning(self, basic_composer):
        market_id = list(basic_composer.derivative_markets.keys())[0]
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.MsgCreateDerivativeMarketOrder(
                market_id=market_id,
                sender="sender",
                subaccount_id="subaccount id",
                fee_recipient="fee recipient",
                price=1,
                quantity=1,
                cid="cid",
                leverage=1,
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_create_derivative_market_order instead"
        )

    def test_msg_cancel_derivative_order_deprecation_warning(self):
        composer = Composer(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgCancelDerivativeOrder(
                market_id="0x7cc8b10d7deb61e744ef83bdec2bbcf4a056867e89b062c6a453020ca82bd4e4",
                sender="sender",
                subaccount_id="subaccount id",
                order_hash="order hash",
                cid="cid",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_cancel_derivative_order instead"
        )

    def test_msg_batch_cancel_derivative_orders_deprecation_warning(self):
        composer = Composer(network=Network.devnet().string())
        orders = [
            composer.order_data(
                market_id="0x7cc8b10d7deb61e744ef83bdec2bbcf4a056867e89b062c6a453020ca82bd4e4",
                subaccount_id="subaccount_id",
                order_hash="0x3870fbdd91f07d54425147b1bb96404f4f043ba6335b422a6d494d285b387f2d",
            ),
        ]

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgBatchCancelDerivativeOrders(sender="sender", data=orders)

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_batch_cancel_derivative_orders instead"
        )

    def test_msg_instant_binary_options_market_launch_deprecation_warning(self):
        composer = Composer(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgInstantBinaryOptionsMarketLaunch(
                sender="sender",
                ticker="B2400/INJ",
                oracle_symbol="B2400/INJ",
                oracle_provider="injective",
                oracle_type="Band",
                oracle_scale_factor=6,
                maker_fee_rate=0.001,
                taker_fee_rate=0.001,
                expiration_timestamp=1630000000,
                settlement_timestamp=1630000000,
                quote_denom="inj",
                quote_decimals=18,
                min_price_tick_size=0.01,
                min_quantity_tick_size=0.01,
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_instant_binary_options_market_launch instead"
        )

    def test_msg_create_binary_options_limit_order_deprecation_warning(self, basic_composer):
        market = list(basic_composer.binary_option_markets.values())[0]

        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.MsgCreateBinaryOptionsLimitOrder(
                market_id=market.id,
                sender="sender",
                subaccount_id="subaccount id",
                fee_recipient="fee recipient",
                price=1,
                quantity=1,
                cid="cid",
                is_buy=True,
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_create_binary_options_limit_order instead"
        )

    def test_msg_create_binary_options_market_order_deprecation_warning(self, basic_composer):
        market = list(basic_composer.binary_option_markets.values())[0]

        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.MsgCreateBinaryOptionsMarketOrder(
                market_id=market.id,
                sender="sender",
                subaccount_id="subaccount id",
                fee_recipient="fee recipient",
                price=1,
                quantity=1,
                cid="cid",
                is_buy=True,
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_create_binary_options_market_order instead"
        )

    def test_msg_cancel_binary_options_order_deprecation_warning(self, basic_composer):
        market = list(basic_composer.binary_option_markets.values())[0]

        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.MsgCancelBinaryOptionsOrder(
                market_id=market.id,
                sender="sender",
                subaccount_id="subaccount id",
                order_hash="order hash",
                cid="cid",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_cancel_binary_options_order instead"
        )

    def test_msg_subaccount_transfer_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.MsgSubaccountTransfer(
                sender="sender",
                source_subaccount_id="source subaccount id",
                destination_subaccount_id="destination subaccount id",
                amount=1,
                denom="INJ",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_subaccount_transfer instead"

    def test_msg_external_transfer_deprecation_warning(self, basic_composer):
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.MsgExternalTransfer(
                sender="sender",
                source_subaccount_id="source subaccount id",
                destination_subaccount_id="destination subaccount id",
                amount=1,
                denom="INJ",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_external_transfer instead"

    def test_msg_liquidate_position_deprecation_warning(self):
        composer = Composer(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgLiquidatePosition(
                sender="sender",
                subaccount_id="subaccount id",
                market_id="0x7cc8b10d7deb61e744ef83bdec2bbcf4a056867e89b062c6a453020ca82bd4e4",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_liquidate_position instead"

    def test_msg_increase_position_margin_deprecation_warning(self, basic_composer):
        market_id = list(basic_composer.derivative_markets.keys())[0]
        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.MsgIncreasePositionMargin(
                sender="sender",
                source_subaccount_id="source_subaccount id",
                destination_subaccount_id="destination_subaccount id",
                market_id=market_id,
                amount=1,
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_increase_position_margin instead"
        )

    def test_msg_rewards_opt_out_deprecation_warning(self):
        composer = Composer(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgRewardsOptOut(
                sender="sender",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_rewards_opt_out instead"

    def test_msg_admin_update_binary_options_market_deprecation_warning(self, basic_composer):
        market = list(basic_composer.binary_option_markets.values())[0]

        with warnings.catch_warnings(record=True) as all_warnings:
            basic_composer.MsgAdminUpdateBinaryOptionsMarket(
                sender="sender",
                market_id=market.id,
                status="Paused",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_admin_update_binary_options_market instead"
        )

    def test_msg_withdraw_delegator_reward_deprecation_warning(self):
        composer = Composer(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgWithdrawDelegatorReward(
                delegator_address="delegator address",
                validator_address="validator address",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use msg_withdraw_delegator_reward instead"
        )
