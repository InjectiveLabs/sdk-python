from decimal import Decimal

import pytest

from pyinjective.composer import Composer
from pyinjective.core.gas_limit_estimator import (
    DERIVATIVE_ORDER_CANCELATION_GAS_LIMIT,
    DERIVATIVE_ORDER_CREATION_GAS_LIMIT,
    SPOT_ORDER_CANCELATION_GAS_LIMIT,
    SPOT_ORDER_CREATION_GAS_LIMIT,
    BatchCancelDerivativeOrdersGasLimitEstimator,
    BatchCancelSpotOrdersGasLimitEstimator,
    BatchCreateDerivativeLimitOrdersGasLimitEstimator,
    BatchCreateSpotLimitOrdersGasLimitEstimator,
    BatchUpdateOrdersGasLimitEstimator,
    ExecGasLimitEstimator,
    GasLimitEstimator,
)
from pyinjective.core.market import BinaryOptionMarket
from pyinjective.core.network import Network
from pyinjective.proto.cosmos.gov.v1beta1 import tx_pb2 as gov_tx_pb
from pyinjective.proto.cosmwasm.wasm.v1 import tx_pb2 as wasm_tx_pb
from pyinjective.proto.injective.exchange.v1beta1 import tx_pb2 as injective_exchange_tx_pb
from tests.model_fixtures.markets_fixtures import btc_usdt_perp_market  # noqa: F401
from tests.model_fixtures.markets_fixtures import first_match_bet_market  # noqa: F401
from tests.model_fixtures.markets_fixtures import inj_token  # noqa: F401
from tests.model_fixtures.markets_fixtures import inj_usdt_spot_market  # noqa: F401
from tests.model_fixtures.markets_fixtures import usdt_perp_token  # noqa: F401
from tests.model_fixtures.markets_fixtures import usdt_token  # noqa: F401


class TestGasLimitEstimator:
    def test_estimation_for_message_without_applying_rule(self):
        composer = Composer(network="testnet")
        message = composer.msg_send(from_address="from_address", to_address="to_address", amount=1, denom="inj")

        estimator = GasLimitEstimator.for_message(message=message)

        expected_message_gas_limit = 150_000

        assert expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_privileged_execute_contract_message(self):
        message = injective_exchange_tx_pb.MsgPrivilegedExecuteContract()
        estimator = GasLimitEstimator.for_message(message=message)

        expected_gas_limit = 900_000

        assert expected_gas_limit == estimator.gas_limit()

    def test_estimation_for_execute_contract_message(self):
        composer = Composer(network="testnet")
        message = composer.MsgExecuteContract(
            sender="",
            contract="",
            msg="",
        )
        estimator = GasLimitEstimator.for_message(message=message)

        expected_gas_limit = 375_000

        assert expected_gas_limit == estimator.gas_limit()

    def test_estimation_for_wasm_message(self):
        message = wasm_tx_pb.MsgInstantiateContract2()
        estimator = GasLimitEstimator.for_message(message=message)

        expected_gas_limit = 225_000

        assert expected_gas_limit == estimator.gas_limit()

    def test_estimation_for_governance_message(self):
        message = gov_tx_pb.MsgDeposit()
        estimator = GasLimitEstimator.for_message(message=message)

        expected_gas_limit = 2_250_000

        assert expected_gas_limit == estimator.gas_limit()


class TestGasLimitEstimatorForV1ExchangeMessages:
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

    def test_estimation_for_batch_create_spot_limit_orders(self, basic_composer):
        spot_market_id = list(basic_composer.spot_markets.keys())[0]
        orders = [
            basic_composer.spot_order(
                market_id=spot_market_id,
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal("5"),
                quantity=Decimal("1"),
                order_type="BUY",
            ),
            basic_composer.spot_order(
                market_id=spot_market_id,
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal("4"),
                quantity=Decimal("1"),
                order_type="BUY",
            ),
        ]
        message = basic_composer.msg_batch_create_spot_limit_orders(sender="sender", orders=orders)
        estimator = GasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = SPOT_ORDER_CREATION_GAS_LIMIT
        expected_message_gas_limit = BatchCreateSpotLimitOrdersGasLimitEstimator.GENERAL_MESSAGE_GAS_LIMIT

        assert (expected_order_gas_limit * 2) + expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_batch_cancel_spot_orders(self, basic_composer):
        spot_market_id = list(basic_composer.spot_markets.keys())[0]
        orders = [
            basic_composer.order_data_without_mask(
                market_id=spot_market_id,
                subaccount_id="subaccount_id",
                order_hash="0x3870fbdd91f07d54425147b1bb96404f4f043ba6335b422a6d494d285b387f2d",
            ),
            basic_composer.order_data_without_mask(
                market_id=spot_market_id,
                subaccount_id="subaccount_id",
                order_hash="0x222daa22f60fe9f075ed0ca583459e121c23e64431c3fbffdedda04598ede0d2",
            ),
            basic_composer.order_data_without_mask(
                market_id=spot_market_id,
                subaccount_id="subaccount_id",
                order_hash="0x7ee76255d7ca763c56b0eab9828fca89fdd3739645501c8a80f58b62b4f76da5",
            ),
        ]
        message = basic_composer.msg_batch_cancel_spot_orders(sender="sender", orders_data=orders)
        estimator = GasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = SPOT_ORDER_CANCELATION_GAS_LIMIT
        expected_message_gas_limit = BatchCancelSpotOrdersGasLimitEstimator.GENERAL_MESSAGE_GAS_LIMIT

        assert (expected_order_gas_limit * 3) + expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_batch_create_derivative_limit_orders(self, basic_composer):
        market_id = list(basic_composer.derivative_markets.keys())[0]
        orders = [
            basic_composer.derivative_order(
                market_id=market_id,
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal(3),
                quantity=Decimal(1),
                margin=Decimal(3),
                order_type="BUY",
            ),
            basic_composer.derivative_order(
                market_id=market_id,
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal(20),
                quantity=Decimal(1),
                margin=Decimal(20),
                order_type="SELL",
            ),
        ]
        message = basic_composer.msg_batch_create_derivative_limit_orders(sender="sender", orders=orders)
        estimator = GasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = DERIVATIVE_ORDER_CREATION_GAS_LIMIT
        expected_message_gas_limit = BatchCreateDerivativeLimitOrdersGasLimitEstimator.GENERAL_MESSAGE_GAS_LIMIT

        assert (expected_order_gas_limit * 2) + expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_batch_cancel_derivative_orders(self, basic_composer):
        spot_market_id = list(basic_composer.spot_markets.keys())[0]
        orders = [
            basic_composer.order_data_without_mask(
                market_id=spot_market_id,
                subaccount_id="subaccount_id",
                order_hash="0x3870fbdd91f07d54425147b1bb96404f4f043ba6335b422a6d494d285b387f2d",
            ),
            basic_composer.order_data_without_mask(
                market_id=spot_market_id,
                subaccount_id="subaccount_id",
                order_hash="0x222daa22f60fe9f075ed0ca583459e121c23e64431c3fbffdedda04598ede0d2",
            ),
            basic_composer.order_data_without_mask(
                market_id=spot_market_id,
                subaccount_id="subaccount_id",
                order_hash="0x7ee76255d7ca763c56b0eab9828fca89fdd3739645501c8a80f58b62b4f76da5",
            ),
        ]
        message = basic_composer.msg_batch_cancel_derivative_orders(sender="sender", orders_data=orders)
        estimator = GasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = DERIVATIVE_ORDER_CANCELATION_GAS_LIMIT
        expected_message_gas_limit = BatchCancelDerivativeOrdersGasLimitEstimator.GENERAL_MESSAGE_GAS_LIMIT

        assert (expected_order_gas_limit * 3) + expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_batch_update_orders_to_create_spot_orders(self, basic_composer):
        market_id = list(basic_composer.spot_markets.keys())[0]
        orders = [
            basic_composer.spot_order(
                market_id=market_id,
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal("5"),
                quantity=Decimal("1"),
                order_type="BUY",
            ),
            basic_composer.spot_order(
                market_id=market_id,
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal("4"),
                quantity=Decimal("1"),
                order_type="BUY",
            ),
        ]
        message = basic_composer.msg_batch_update_orders(
            sender="senders",
            derivative_orders_to_create=[],
            spot_orders_to_create=orders,
            derivative_orders_to_cancel=[],
            spot_orders_to_cancel=[],
        )
        estimator = GasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = SPOT_ORDER_CREATION_GAS_LIMIT
        expected_message_gas_limit = BatchUpdateOrdersGasLimitEstimator.MESSAGE_GAS_LIMIT

        assert (expected_order_gas_limit * 2) + expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_batch_update_orders_to_create_derivative_orders(self, basic_composer):
        market_id = list(basic_composer.derivative_markets.keys())[0]
        orders = [
            basic_composer.derivative_order(
                market_id=market_id,
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal(3),
                quantity=Decimal(1),
                margin=Decimal(3),
                order_type="BUY",
            ),
            basic_composer.derivative_order(
                market_id=market_id,
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal(20),
                quantity=Decimal(1),
                margin=Decimal(20),
                order_type="SELL",
            ),
        ]
        message = basic_composer.msg_batch_update_orders(
            sender="senders",
            derivative_orders_to_create=orders,
            spot_orders_to_create=[],
            derivative_orders_to_cancel=[],
            spot_orders_to_cancel=[],
        )
        estimator = GasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = DERIVATIVE_ORDER_CREATION_GAS_LIMIT
        expected_message_gas_limit = BatchUpdateOrdersGasLimitEstimator.MESSAGE_GAS_LIMIT

        assert (expected_order_gas_limit * 2) + expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_batch_update_orders_to_create_binary_orders(self, basic_composer, usdt_token):
        market_id = list(basic_composer.binary_option_markets.keys())[0]
        market = BinaryOptionMarket(
            id=market_id,
            status="active",
            ticker="5fdbe0b1-1707800399-WAS",
            oracle_symbol="Frontrunner",
            oracle_provider="Frontrunner",
            oracle_type="provider",
            oracle_scale_factor=6,
            expiration_timestamp=1707800399,
            settlement_timestamp=1707843599,
            quote_token=usdt_token,
            maker_fee_rate=Decimal("0"),
            taker_fee_rate=Decimal("0"),
            service_provider_fee=Decimal("0.4"),
            min_price_tick_size=Decimal("10000"),
            min_quantity_tick_size=Decimal("1"),
            min_notional=Decimal(0),
        )
        basic_composer.binary_option_markets[market.id] = market
        orders = [
            basic_composer.binary_options_order(
                market_id=market_id,
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal(3),
                quantity=Decimal(1),
                margin=Decimal(3),
                order_type="BUY",
            ),
            basic_composer.binary_options_order(
                market_id=market_id,
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal(20),
                quantity=Decimal(1),
                margin=Decimal(20),
                order_type="SELL",
            ),
        ]
        message = basic_composer.msg_batch_update_orders(
            sender="senders",
            derivative_orders_to_create=[],
            spot_orders_to_create=[],
            binary_options_orders_to_create=orders,
            derivative_orders_to_cancel=[],
            spot_orders_to_cancel=[],
        )
        estimator = GasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = DERIVATIVE_ORDER_CREATION_GAS_LIMIT
        expected_message_gas_limit = BatchUpdateOrdersGasLimitEstimator.MESSAGE_GAS_LIMIT

        assert (expected_order_gas_limit * 2) + expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_batch_update_orders_to_cancel_spot_orders(self, basic_composer):
        market_id = list(basic_composer.spot_markets.keys())[0]
        orders = [
            basic_composer.order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x3870fbdd91f07d54425147b1bb96404f4f043ba6335b422a6d494d285b387f2d",
            ),
            basic_composer.order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x222daa22f60fe9f075ed0ca583459e121c23e64431c3fbffdedda04598ede0d2",
            ),
            basic_composer.order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x7ee76255d7ca763c56b0eab9828fca89fdd3739645501c8a80f58b62b4f76da5",
            ),
        ]
        message = basic_composer.msg_batch_update_orders(
            sender="senders",
            derivative_orders_to_create=[],
            spot_orders_to_create=[],
            derivative_orders_to_cancel=[],
            spot_orders_to_cancel=orders,
        )
        estimator = GasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = SPOT_ORDER_CANCELATION_GAS_LIMIT
        expected_message_gas_limit = BatchUpdateOrdersGasLimitEstimator.MESSAGE_GAS_LIMIT

        assert (expected_order_gas_limit * 3) + expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_batch_update_orders_to_cancel_derivative_orders(self, basic_composer):
        market_id = list(basic_composer.derivative_markets.keys())[0]
        orders = [
            basic_composer.order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x3870fbdd91f07d54425147b1bb96404f4f043ba6335b422a6d494d285b387f2d",
            ),
            basic_composer.order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x222daa22f60fe9f075ed0ca583459e121c23e64431c3fbffdedda04598ede0d2",
            ),
            basic_composer.order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x7ee76255d7ca763c56b0eab9828fca89fdd3739645501c8a80f58b62b4f76da5",
            ),
        ]
        message = basic_composer.msg_batch_update_orders(
            sender="senders",
            derivative_orders_to_create=[],
            spot_orders_to_create=[],
            derivative_orders_to_cancel=orders,
            spot_orders_to_cancel=[],
        )
        estimator = GasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = DERIVATIVE_ORDER_CANCELATION_GAS_LIMIT
        expected_message_gas_limit = BatchUpdateOrdersGasLimitEstimator.MESSAGE_GAS_LIMIT

        assert (expected_order_gas_limit * 3) + expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_batch_update_orders_to_cancel_binary_orders(self, basic_composer):
        market_id = list(basic_composer.binary_option_markets.keys())[0]
        orders = [
            basic_composer.order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x3870fbdd91f07d54425147b1bb96404f4f043ba6335b422a6d494d285b387f2d",
            ),
            basic_composer.order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x222daa22f60fe9f075ed0ca583459e121c23e64431c3fbffdedda04598ede0d2",
            ),
            basic_composer.order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x7ee76255d7ca763c56b0eab9828fca89fdd3739645501c8a80f58b62b4f76da5",
            ),
        ]
        message = basic_composer.msg_batch_update_orders(
            sender="senders",
            derivative_orders_to_create=[],
            spot_orders_to_create=[],
            derivative_orders_to_cancel=[],
            spot_orders_to_cancel=[],
            binary_options_orders_to_cancel=orders,
        )
        estimator = GasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = DERIVATIVE_ORDER_CANCELATION_GAS_LIMIT
        expected_message_gas_limit = BatchUpdateOrdersGasLimitEstimator.MESSAGE_GAS_LIMIT

        assert (expected_order_gas_limit * 3) + expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_batch_update_orders_to_cancel_all_for_spot_market(self):
        market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        composer = Composer(network="testnet")

        message = composer.msg_batch_update_orders(
            sender="senders",
            subaccount_id="subaccount_id",
            spot_market_ids_to_cancel_all=[market_id],
            derivative_orders_to_create=[],
            spot_orders_to_create=[],
            derivative_orders_to_cancel=[],
            spot_orders_to_cancel=[],
        )
        estimator = GasLimitEstimator.for_message(message=message)

        expected_gas_limit = BatchUpdateOrdersGasLimitEstimator.CANCEL_ALL_SPOT_MARKET_GAS_LIMIT * 20
        expected_message_gas_limit = BatchUpdateOrdersGasLimitEstimator.MESSAGE_GAS_LIMIT

        assert expected_gas_limit + expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_batch_update_orders_to_cancel_all_for_derivative_market(self):
        market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        composer = Composer(network="testnet")

        message = composer.msg_batch_update_orders(
            sender="senders",
            subaccount_id="subaccount_id",
            derivative_market_ids_to_cancel_all=[market_id],
            derivative_orders_to_create=[],
            spot_orders_to_create=[],
            derivative_orders_to_cancel=[],
            spot_orders_to_cancel=[],
        )
        estimator = GasLimitEstimator.for_message(message=message)

        expected_gas_limit = BatchUpdateOrdersGasLimitEstimator.CANCEL_ALL_DERIVATIVE_MARKET_GAS_LIMIT * 20
        expected_message_gas_limit = BatchUpdateOrdersGasLimitEstimator.MESSAGE_GAS_LIMIT

        assert expected_gas_limit + expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_batch_update_orders_to_cancel_all_for_binary_options_market(self):
        market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        composer = Composer(network="testnet")

        message = composer.msg_batch_update_orders(
            sender="senders",
            subaccount_id="subaccount_id",
            binary_options_market_ids_to_cancel_all=[market_id],
            derivative_orders_to_create=[],
            spot_orders_to_create=[],
            derivative_orders_to_cancel=[],
            spot_orders_to_cancel=[],
        )
        estimator = GasLimitEstimator.for_message(message=message)

        expected_gas_limit = BatchUpdateOrdersGasLimitEstimator.CANCEL_ALL_DERIVATIVE_MARKET_GAS_LIMIT * 20
        expected_message_gas_limit = BatchUpdateOrdersGasLimitEstimator.MESSAGE_GAS_LIMIT

        assert expected_gas_limit + expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_exec_message(self, basic_composer):
        market_id = list(basic_composer.spot_markets.keys())[0]
        orders = [
            basic_composer.spot_order(
                market_id=market_id,
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal("5"),
                quantity=Decimal("1"),
                order_type="BUY",
            ),
        ]
        inner_message = basic_composer.msg_batch_update_orders(
            sender="senders",
            derivative_orders_to_create=[],
            spot_orders_to_create=orders,
            derivative_orders_to_cancel=[],
            spot_orders_to_cancel=[],
        )
        message = basic_composer.MsgExec(grantee="grantee", msgs=[inner_message])

        estimator = GasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = SPOT_ORDER_CREATION_GAS_LIMIT
        expected_inner_message_gas_limit = BatchUpdateOrdersGasLimitEstimator.MESSAGE_GAS_LIMIT
        expected_exec_message_gas_limit = ExecGasLimitEstimator.DEFAULT_GAS_LIMIT

        assert (
            expected_order_gas_limit + expected_inner_message_gas_limit + expected_exec_message_gas_limit
            == estimator.gas_limit()
        )

    def test_estimation_for_generic_exchange_message(self, basic_composer):
        market_id = list(basic_composer.spot_markets.keys())[0]
        message = basic_composer.msg_create_spot_limit_order(
            sender="sender",
            market_id=market_id,
            subaccount_id="subaccount_id",
            fee_recipient="fee_recipient",
            price=Decimal("7.523"),
            quantity=Decimal("0.01"),
            order_type="BUY",
        )
        estimator = GasLimitEstimator.for_message(message=message)

        expected_gas_limit = 120_000

        assert expected_gas_limit == estimator.gas_limit()


class TestGasLimitEstimatorForV2ExchangeMessages:
    def test_estimation_for_batch_create_spot_limit_orders(self):
        spot_market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        composer = Composer(network="testnet")
        orders = [
            composer.create_v2_spot_order(
                market_id=spot_market_id,
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal("5"),
                quantity=Decimal("1"),
                order_type="BUY",
            ),
            composer.create_v2_spot_order(
                market_id=spot_market_id,
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal("4"),
                quantity=Decimal("1"),
                order_type="BUY",
            ),
        ]
        message = composer.msg_batch_create_spot_limit_orders_v2(sender="sender", orders=orders)
        estimator = GasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = SPOT_ORDER_CREATION_GAS_LIMIT
        expected_message_gas_limit = BatchCreateSpotLimitOrdersGasLimitEstimator.GENERAL_MESSAGE_GAS_LIMIT

        assert (expected_order_gas_limit * 2) + expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_batch_cancel_spot_orders(self):
        spot_market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        composer = Composer(network="testnet")
        orders = [
            composer.create_v2_order_data_without_mask(
                market_id=spot_market_id,
                subaccount_id="subaccount_id",
                order_hash="0x3870fbdd91f07d54425147b1bb96404f4f043ba6335b422a6d494d285b387f2d",
            ),
            composer.create_v2_order_data_without_mask(
                market_id=spot_market_id,
                subaccount_id="subaccount_id",
                order_hash="0x222daa22f60fe9f075ed0ca583459e121c23e64431c3fbffdedda04598ede0d2",
            ),
            composer.create_v2_order_data_without_mask(
                market_id=spot_market_id,
                subaccount_id="subaccount_id",
                order_hash="0x7ee76255d7ca763c56b0eab9828fca89fdd3739645501c8a80f58b62b4f76da5",
            ),
        ]
        message = composer.msg_batch_cancel_spot_orders_v2(sender="sender", orders_data=orders)
        estimator = GasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = SPOT_ORDER_CANCELATION_GAS_LIMIT
        expected_message_gas_limit = BatchCancelSpotOrdersGasLimitEstimator.GENERAL_MESSAGE_GAS_LIMIT

        assert (expected_order_gas_limit * 3) + expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_batch_create_derivative_limit_orders(self):
        market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
        composer = Composer(network="testnet")
        orders = [
            composer.create_v2_derivative_order(
                market_id=market_id,
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal(3),
                quantity=Decimal(1),
                margin=Decimal(3),
                order_type="BUY",
            ),
            composer.create_v2_derivative_order(
                market_id=market_id,
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal(20),
                quantity=Decimal(1),
                margin=Decimal(20),
                order_type="SELL",
            ),
        ]
        message = composer.msg_batch_create_derivative_limit_orders_v2(sender="sender", orders=orders)
        estimator = GasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = DERIVATIVE_ORDER_CREATION_GAS_LIMIT
        expected_message_gas_limit = BatchCreateDerivativeLimitOrdersGasLimitEstimator.GENERAL_MESSAGE_GAS_LIMIT

        assert (expected_order_gas_limit * 2) + expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_batch_cancel_derivative_orders(self):
        spot_market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        composer = Composer(network="testnet")
        orders = [
            composer.create_v2_order_data_without_mask(
                market_id=spot_market_id,
                subaccount_id="subaccount_id",
                order_hash="0x3870fbdd91f07d54425147b1bb96404f4f043ba6335b422a6d494d285b387f2d",
            ),
            composer.create_v2_order_data_without_mask(
                market_id=spot_market_id,
                subaccount_id="subaccount_id",
                order_hash="0x222daa22f60fe9f075ed0ca583459e121c23e64431c3fbffdedda04598ede0d2",
            ),
            composer.create_v2_order_data_without_mask(
                market_id=spot_market_id,
                subaccount_id="subaccount_id",
                order_hash="0x7ee76255d7ca763c56b0eab9828fca89fdd3739645501c8a80f58b62b4f76da5",
            ),
        ]
        message = composer.msg_batch_cancel_derivative_orders_v2(sender="sender", orders_data=orders)
        estimator = GasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = DERIVATIVE_ORDER_CANCELATION_GAS_LIMIT
        expected_message_gas_limit = BatchCancelDerivativeOrdersGasLimitEstimator.GENERAL_MESSAGE_GAS_LIMIT

        assert (expected_order_gas_limit * 3) + expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_batch_update_orders_to_create_spot_orders(self):
        market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        composer = Composer(network="testnet")
        orders = [
            composer.create_v2_spot_order(
                market_id=market_id,
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal("5"),
                quantity=Decimal("1"),
                order_type="BUY",
            ),
            composer.create_v2_spot_order(
                market_id=market_id,
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal("4"),
                quantity=Decimal("1"),
                order_type="BUY",
            ),
        ]
        message = composer.msg_batch_update_orders_v2(
            sender="senders",
            derivative_orders_to_create=[],
            spot_orders_to_create=orders,
            derivative_orders_to_cancel=[],
            spot_orders_to_cancel=[],
        )
        estimator = GasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = SPOT_ORDER_CREATION_GAS_LIMIT
        expected_message_gas_limit = BatchUpdateOrdersGasLimitEstimator.MESSAGE_GAS_LIMIT

        assert (expected_order_gas_limit * 2) + expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_batch_update_orders_to_create_derivative_orders(self):
        market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
        composer = Composer(network="testnet")
        orders = [
            composer.create_v2_derivative_order(
                market_id=market_id,
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal(3),
                quantity=Decimal(1),
                margin=Decimal(3),
                order_type="BUY",
            ),
            composer.create_v2_derivative_order(
                market_id=market_id,
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal(20),
                quantity=Decimal(1),
                margin=Decimal(20),
                order_type="SELL",
            ),
        ]
        message = composer.msg_batch_update_orders_v2(
            sender="senders",
            derivative_orders_to_create=orders,
            spot_orders_to_create=[],
            derivative_orders_to_cancel=[],
            spot_orders_to_cancel=[],
        )
        estimator = GasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = DERIVATIVE_ORDER_CREATION_GAS_LIMIT
        expected_message_gas_limit = BatchUpdateOrdersGasLimitEstimator.MESSAGE_GAS_LIMIT

        assert (expected_order_gas_limit * 2) + expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_batch_update_orders_to_create_binary_orders(self, usdt_token):
        market_id = "0x230dcce315364ff6360097838701b14713e2f4007d704df20ed3d81d09eec957"
        composer = Composer(network="testnet")
        market = BinaryOptionMarket(
            id=market_id,
            status="active",
            ticker="5fdbe0b1-1707800399-WAS",
            oracle_symbol="Frontrunner",
            oracle_provider="Frontrunner",
            oracle_type="provider",
            oracle_scale_factor=6,
            expiration_timestamp=1707800399,
            settlement_timestamp=1707843599,
            quote_token=usdt_token,
            maker_fee_rate=Decimal("0"),
            taker_fee_rate=Decimal("0"),
            service_provider_fee=Decimal("0.4"),
            min_price_tick_size=Decimal("10000"),
            min_quantity_tick_size=Decimal("1"),
            min_notional=Decimal(0),
        )
        composer.binary_option_markets[market.id] = market
        orders = [
            composer.create_v2_binary_options_order(
                market_id=market_id,
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal(3),
                quantity=Decimal(1),
                margin=Decimal(3),
                order_type="BUY",
            ),
            composer.create_v2_binary_options_order(
                market_id=market_id,
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal(20),
                quantity=Decimal(1),
                margin=Decimal(20),
                order_type="SELL",
            ),
        ]
        message = composer.msg_batch_update_orders_v2(
            sender="senders",
            derivative_orders_to_create=[],
            spot_orders_to_create=[],
            binary_options_orders_to_create=orders,
            derivative_orders_to_cancel=[],
            spot_orders_to_cancel=[],
        )
        estimator = GasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = DERIVATIVE_ORDER_CREATION_GAS_LIMIT
        expected_message_gas_limit = BatchUpdateOrdersGasLimitEstimator.MESSAGE_GAS_LIMIT

        assert (expected_order_gas_limit * 2) + expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_batch_update_orders_to_cancel_spot_orders(self):
        market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        composer = Composer(network="testnet")
        orders = [
            composer.create_v2_order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x3870fbdd91f07d54425147b1bb96404f4f043ba6335b422a6d494d285b387f2d",
            ),
            composer.create_v2_order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x222daa22f60fe9f075ed0ca583459e121c23e64431c3fbffdedda04598ede0d2",
            ),
            composer.create_v2_order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x7ee76255d7ca763c56b0eab9828fca89fdd3739645501c8a80f58b62b4f76da5",
            ),
        ]
        message = composer.msg_batch_update_orders_v2(
            sender="senders",
            derivative_orders_to_create=[],
            spot_orders_to_create=[],
            derivative_orders_to_cancel=[],
            spot_orders_to_cancel=orders,
        )
        estimator = GasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = SPOT_ORDER_CANCELATION_GAS_LIMIT
        expected_message_gas_limit = BatchUpdateOrdersGasLimitEstimator.MESSAGE_GAS_LIMIT

        assert (expected_order_gas_limit * 3) + expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_batch_update_orders_to_cancel_derivative_orders(self):
        market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
        composer = Composer(network="testnet")
        orders = [
            composer.create_v2_order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x3870fbdd91f07d54425147b1bb96404f4f043ba6335b422a6d494d285b387f2d",
            ),
            composer.create_v2_order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x222daa22f60fe9f075ed0ca583459e121c23e64431c3fbffdedda04598ede0d2",
            ),
            composer.create_v2_order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x7ee76255d7ca763c56b0eab9828fca89fdd3739645501c8a80f58b62b4f76da5",
            ),
        ]
        message = composer.msg_batch_update_orders_v2(
            sender="senders",
            derivative_orders_to_create=[],
            spot_orders_to_create=[],
            derivative_orders_to_cancel=orders,
            spot_orders_to_cancel=[],
        )
        estimator = GasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = DERIVATIVE_ORDER_CANCELATION_GAS_LIMIT
        expected_message_gas_limit = BatchUpdateOrdersGasLimitEstimator.MESSAGE_GAS_LIMIT

        assert (expected_order_gas_limit * 3) + expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_batch_update_orders_to_cancel_binary_orders(self):
        market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
        composer = Composer(network="testnet")
        orders = [
            composer.create_v2_order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x3870fbdd91f07d54425147b1bb96404f4f043ba6335b422a6d494d285b387f2d",
            ),
            composer.create_v2_order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x222daa22f60fe9f075ed0ca583459e121c23e64431c3fbffdedda04598ede0d2",
            ),
            composer.create_v2_order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x7ee76255d7ca763c56b0eab9828fca89fdd3739645501c8a80f58b62b4f76da5",
            ),
        ]
        message = composer.msg_batch_update_orders_v2(
            sender="senders",
            derivative_orders_to_create=[],
            spot_orders_to_create=[],
            derivative_orders_to_cancel=[],
            spot_orders_to_cancel=[],
            binary_options_orders_to_cancel=orders,
        )
        estimator = GasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = DERIVATIVE_ORDER_CANCELATION_GAS_LIMIT
        expected_message_gas_limit = BatchUpdateOrdersGasLimitEstimator.MESSAGE_GAS_LIMIT

        assert (expected_order_gas_limit * 3) + expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_batch_update_orders_to_cancel_all_for_spot_market(self):
        market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        composer = Composer(network="testnet")

        message = composer.msg_batch_update_orders_v2(
            sender="senders",
            subaccount_id="subaccount_id",
            spot_market_ids_to_cancel_all=[market_id],
            derivative_orders_to_create=[],
            spot_orders_to_create=[],
            derivative_orders_to_cancel=[],
            spot_orders_to_cancel=[],
        )
        estimator = GasLimitEstimator.for_message(message=message)

        expected_gas_limit = BatchUpdateOrdersGasLimitEstimator.CANCEL_ALL_SPOT_MARKET_GAS_LIMIT * 20
        expected_message_gas_limit = BatchUpdateOrdersGasLimitEstimator.MESSAGE_GAS_LIMIT

        assert expected_gas_limit + expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_batch_update_orders_to_cancel_all_for_derivative_market(self):
        market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        composer = Composer(network="testnet")

        message = composer.msg_batch_update_orders_v2(
            sender="senders",
            subaccount_id="subaccount_id",
            derivative_market_ids_to_cancel_all=[market_id],
            derivative_orders_to_create=[],
            spot_orders_to_create=[],
            derivative_orders_to_cancel=[],
            spot_orders_to_cancel=[],
        )
        estimator = GasLimitEstimator.for_message(message=message)

        expected_gas_limit = BatchUpdateOrdersGasLimitEstimator.CANCEL_ALL_DERIVATIVE_MARKET_GAS_LIMIT * 20
        expected_message_gas_limit = BatchUpdateOrdersGasLimitEstimator.MESSAGE_GAS_LIMIT

        assert expected_gas_limit + expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_batch_update_orders_to_cancel_all_for_binary_options_market(self):
        market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        composer = Composer(network="testnet")

        message = composer.msg_batch_update_orders_v2(
            sender="senders",
            subaccount_id="subaccount_id",
            binary_options_market_ids_to_cancel_all=[market_id],
            derivative_orders_to_create=[],
            spot_orders_to_create=[],
            derivative_orders_to_cancel=[],
            spot_orders_to_cancel=[],
        )
        estimator = GasLimitEstimator.for_message(message=message)

        expected_gas_limit = BatchUpdateOrdersGasLimitEstimator.CANCEL_ALL_DERIVATIVE_MARKET_GAS_LIMIT * 20
        expected_message_gas_limit = BatchUpdateOrdersGasLimitEstimator.MESSAGE_GAS_LIMIT

        assert expected_gas_limit + expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_exec_message(self):
        market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        composer = Composer(network="testnet")
        orders = [
            composer.create_v2_spot_order(
                market_id=market_id,
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal("5"),
                quantity=Decimal("1"),
                order_type="BUY",
            ),
        ]
        inner_message = composer.msg_batch_update_orders_v2(
            sender="senders",
            derivative_orders_to_create=[],
            spot_orders_to_create=orders,
            derivative_orders_to_cancel=[],
            spot_orders_to_cancel=[],
        )
        message = composer.MsgExec(grantee="grantee", msgs=[inner_message])

        estimator = GasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = SPOT_ORDER_CREATION_GAS_LIMIT
        expected_inner_message_gas_limit = BatchUpdateOrdersGasLimitEstimator.MESSAGE_GAS_LIMIT
        expected_exec_message_gas_limit = ExecGasLimitEstimator.DEFAULT_GAS_LIMIT

        assert (
            expected_order_gas_limit + expected_inner_message_gas_limit + expected_exec_message_gas_limit
            == estimator.gas_limit()
        )

    def test_estimation_for_generic_exchange_message(self):
        composer = Composer(network="testnet")
        message = composer.msg_create_spot_limit_order_v2(
            sender="sender",
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            subaccount_id="subaccount_id",
            fee_recipient="fee_recipient",
            price=Decimal("7.523"),
            quantity=Decimal("0.01"),
            order_type="BUY",
        )
        estimator = GasLimitEstimator.for_message(message=message)

        expected_gas_limit = 120_000

        assert expected_gas_limit == estimator.gas_limit()
