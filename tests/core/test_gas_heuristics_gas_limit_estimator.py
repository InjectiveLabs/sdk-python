import math
from decimal import Decimal

import pytest

from pyinjective.composer_v2 import Composer
from pyinjective.core.gas_heuristics_gas_limit_estimator import (
    BINARY_OPTIONS_MARKET_ORDER_CREATION_GAS_LIMIT,
    BINARY_OPTIONS_ORDER_CANCELATION_GAS_LIMIT,
    BINARY_OPTIONS_ORDER_CREATION_GAS_LIMIT,
    DECREASE_POSITION_MARGIN_TRANSFER_GAS_LIMIT,
    DEPOSIT_GAS_LIMIT,
    DERIVATIVE_MARKET_ORDER_CREATION_GAS_LIMIT,
    DERIVATIVE_ORDER_CANCELATION_GAS_LIMIT,
    DERIVATIVE_ORDER_CREATION_GAS_LIMIT,
    EXTERNAL_TRANSFER_GAS_LIMIT,
    GTB_ORDERS_GAS_MULTIPLIER,
    INCREASE_POSITION_MARGIN_TRANSFER_GAS_LIMIT,
    POST_ONLY_BINARY_OPTIONS_ORDER_CREATION_GAS_LIMIT,
    POST_ONLY_DERIVATIVE_ORDER_CREATION_GAS_LIMIT,
    POST_ONLY_SPOT_ORDER_CREATION_GAS_LIMIT,
    SPOT_MARKET_ORDER_CREATION_GAS_LIMIT,
    SPOT_ORDER_CANCELATION_GAS_LIMIT,
    SPOT_ORDER_CREATION_GAS_LIMIT,
    SUBACCOUNT_TRANSFER_GAS_LIMIT,
    WITHDRAW_GAS_LIMIT,
    BatchUpdateOrdersGasLimitEstimator,
    GasHeuristicsGasLimitEstimator,
)
from pyinjective.core.gas_limit_estimator import ExecGasLimitEstimator
from pyinjective.core.network import Network
from pyinjective.proto.cosmos.gov.v1beta1 import tx_pb2 as gov_tx_pb
from pyinjective.proto.cosmwasm.wasm.v1 import tx_pb2 as wasm_tx_pb
from pyinjective.proto.injective.exchange.v1beta1 import tx_pb2 as injective_exchange_tx_pb
from tests.model_fixtures.markets_v2_fixtures import (  # noqa: F401
    btc_usdt_perp_market,
    first_match_bet_market,
    inj_token,
    inj_usdt_spot_market,
    usdt_perp_token,
    usdt_token,
)


class TestGasLimitEstimator:
    @pytest.fixture
    def basic_composer(self, inj_usdt_spot_market, btc_usdt_perp_market, first_match_bet_market):
        composer = Composer(
            network=Network.devnet().string(),
        )

        return composer

    def test_estimation_for_message_without_applying_rule(self, basic_composer):
        message = basic_composer.msg_send(from_address="from_address", to_address="to_address", amount=1, denom="INJ")

        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_message_gas_limit = 150_000

        assert expected_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_batch_create_spot_limit_orders(self, basic_composer):
        spot_market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
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
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = SPOT_ORDER_CREATION_GAS_LIMIT

        assert (expected_order_gas_limit * 2) == estimator.gas_limit()

    def test_estimation_for_batch_cancel_spot_orders(self):
        spot_market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        composer = Composer(network="testnet")
        orders = [
            composer.order_data_without_mask(
                market_id=spot_market_id,
                subaccount_id="subaccount_id",
                order_hash="0x3870fbdd91f07d54425147b1bb96404f4f043ba6335b422a6d494d285b387f2d",
            ),
            composer.order_data_without_mask(
                market_id=spot_market_id,
                subaccount_id="subaccount_id",
                order_hash="0x222daa22f60fe9f075ed0ca583459e121c23e64431c3fbffdedda04598ede0d2",
            ),
            composer.order_data_without_mask(
                market_id=spot_market_id,
                subaccount_id="subaccount_id",
                order_hash="0x7ee76255d7ca763c56b0eab9828fca89fdd3739645501c8a80f58b62b4f76da5",
            ),
        ]
        message = composer.msg_batch_cancel_spot_orders(sender="sender", orders_data=orders)
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = SPOT_ORDER_CANCELATION_GAS_LIMIT

        assert (expected_order_gas_limit * 3) == estimator.gas_limit()

    def test_estimation_for_batch_create_derivative_limit_orders(self, basic_composer):
        market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
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
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = DERIVATIVE_ORDER_CREATION_GAS_LIMIT

        assert (expected_order_gas_limit * 2) == estimator.gas_limit()

    def test_estimation_for_batch_cancel_derivative_orders(self):
        spot_market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        composer = Composer(network="testnet")
        orders = [
            composer.order_data_without_mask(
                market_id=spot_market_id,
                subaccount_id="subaccount_id",
                order_hash="0x3870fbdd91f07d54425147b1bb96404f4f043ba6335b422a6d494d285b387f2d",
            ),
            composer.order_data_without_mask(
                market_id=spot_market_id,
                subaccount_id="subaccount_id",
                order_hash="0x222daa22f60fe9f075ed0ca583459e121c23e64431c3fbffdedda04598ede0d2",
            ),
            composer.order_data_without_mask(
                market_id=spot_market_id,
                subaccount_id="subaccount_id",
                order_hash="0x7ee76255d7ca763c56b0eab9828fca89fdd3739645501c8a80f58b62b4f76da5",
            ),
        ]
        message = composer.msg_batch_cancel_derivative_orders(sender="sender", orders_data=orders)
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = DERIVATIVE_ORDER_CANCELATION_GAS_LIMIT

        assert (expected_order_gas_limit * 3) == estimator.gas_limit()

    def test_estimation_for_batch_update_orders_to_create_spot_orders(self, basic_composer):
        market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
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
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = SPOT_ORDER_CREATION_GAS_LIMIT

        assert (expected_order_gas_limit * 2) == estimator.gas_limit()

    def test_estimation_for_batch_update_orders_to_create_derivative_orders(self, basic_composer):
        market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
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
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = DERIVATIVE_ORDER_CREATION_GAS_LIMIT

        assert (expected_order_gas_limit * 2) == estimator.gas_limit()

    def test_estimation_for_batch_update_orders_to_create_binary_orders(self, usdt_token):
        market_id = "0x230dcce315364ff6360097838701b14713e2f4007d704df20ed3d81d09eec957"
        composer = Composer(network="testnet")
        orders = [
            composer.binary_options_order(
                market_id=market_id,
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal(3),
                quantity=Decimal(1),
                margin=Decimal(3),
                order_type="BUY",
            ),
            composer.binary_options_order(
                market_id=market_id,
                subaccount_id="subaccount_id",
                fee_recipient="fee_recipient",
                price=Decimal(20),
                quantity=Decimal(1),
                margin=Decimal(20),
                order_type="SELL",
            ),
        ]
        message = composer.msg_batch_update_orders(
            sender="senders",
            derivative_orders_to_create=[],
            spot_orders_to_create=[],
            binary_options_orders_to_create=orders,
            derivative_orders_to_cancel=[],
            spot_orders_to_cancel=[],
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = BINARY_OPTIONS_ORDER_CREATION_GAS_LIMIT

        assert (expected_order_gas_limit * 2) == estimator.gas_limit()

    def test_estimation_for_batch_update_orders_to_cancel_spot_orders(self):
        market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        composer = Composer(network="testnet")
        orders = [
            composer.order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x3870fbdd91f07d54425147b1bb96404f4f043ba6335b422a6d494d285b387f2d",
            ),
            composer.order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x222daa22f60fe9f075ed0ca583459e121c23e64431c3fbffdedda04598ede0d2",
            ),
            composer.order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x7ee76255d7ca763c56b0eab9828fca89fdd3739645501c8a80f58b62b4f76da5",
            ),
        ]
        message = composer.msg_batch_update_orders(
            sender="senders",
            derivative_orders_to_create=[],
            spot_orders_to_create=[],
            derivative_orders_to_cancel=[],
            spot_orders_to_cancel=orders,
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = SPOT_ORDER_CANCELATION_GAS_LIMIT

        assert (expected_order_gas_limit * 3) == estimator.gas_limit()

    def test_estimation_for_batch_update_orders_to_cancel_derivative_orders(self):
        market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
        composer = Composer(network="testnet")
        orders = [
            composer.order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x3870fbdd91f07d54425147b1bb96404f4f043ba6335b422a6d494d285b387f2d",
            ),
            composer.order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x222daa22f60fe9f075ed0ca583459e121c23e64431c3fbffdedda04598ede0d2",
            ),
            composer.order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x7ee76255d7ca763c56b0eab9828fca89fdd3739645501c8a80f58b62b4f76da5",
            ),
        ]
        message = composer.msg_batch_update_orders(
            sender="senders",
            derivative_orders_to_create=[],
            spot_orders_to_create=[],
            derivative_orders_to_cancel=orders,
            spot_orders_to_cancel=[],
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = DERIVATIVE_ORDER_CANCELATION_GAS_LIMIT

        assert (expected_order_gas_limit * 3) == estimator.gas_limit()

    def test_estimation_for_batch_update_orders_to_cancel_binary_orders(self):
        market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
        composer = Composer(network="testnet")
        orders = [
            composer.order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x3870fbdd91f07d54425147b1bb96404f4f043ba6335b422a6d494d285b387f2d",
            ),
            composer.order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x222daa22f60fe9f075ed0ca583459e121c23e64431c3fbffdedda04598ede0d2",
            ),
            composer.order_data_without_mask(
                market_id=market_id,
                subaccount_id="subaccount_id",
                order_hash="0x7ee76255d7ca763c56b0eab9828fca89fdd3739645501c8a80f58b62b4f76da5",
            ),
        ]
        message = composer.msg_batch_update_orders(
            sender="senders",
            derivative_orders_to_create=[],
            spot_orders_to_create=[],
            derivative_orders_to_cancel=[],
            spot_orders_to_cancel=[],
            binary_options_orders_to_cancel=orders,
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = BINARY_OPTIONS_ORDER_CANCELATION_GAS_LIMIT

        assert (expected_order_gas_limit * 3) == estimator.gas_limit()

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
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_gas_limit = (
            BatchUpdateOrdersGasLimitEstimator.AVERAGE_CANCEL_ALL_AFFECTED_ORDERS * SPOT_ORDER_CANCELATION_GAS_LIMIT
        )

        assert expected_gas_limit == estimator.gas_limit()

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
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_gas_limit = (
            BatchUpdateOrdersGasLimitEstimator.AVERAGE_CANCEL_ALL_AFFECTED_ORDERS
            * DERIVATIVE_ORDER_CANCELATION_GAS_LIMIT
        )

        assert expected_gas_limit == estimator.gas_limit()

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
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_gas_limit = (
            BatchUpdateOrdersGasLimitEstimator.AVERAGE_CANCEL_ALL_AFFECTED_ORDERS
            * BINARY_OPTIONS_ORDER_CANCELATION_GAS_LIMIT
        )

        assert expected_gas_limit == estimator.gas_limit()

    def test_estimation_for_create_spot_limit_order(self, basic_composer, inj_usdt_spot_market):
        composer = basic_composer
        market_id = inj_usdt_spot_market.id

        message = composer.msg_create_spot_limit_order(
            market_id=market_id,
            sender="senders",
            subaccount_id="subaccount_id",
            fee_recipient="fee_recipient",
            price=Decimal("7.523"),
            quantity=Decimal("0.01"),
            order_type="BUY",
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_gas_cost = SPOT_ORDER_CREATION_GAS_LIMIT

        assert expected_gas_cost == estimator.gas_limit()

        po_order_message = composer.msg_create_spot_limit_order(
            market_id=market_id,
            sender="senders",
            subaccount_id="subaccount_id",
            fee_recipient="fee_recipient",
            price=Decimal("7.523"),
            quantity=Decimal("0.01"),
            order_type="BUY_PO",
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=po_order_message)

        expected_gas_cost = POST_ONLY_SPOT_ORDER_CREATION_GAS_LIMIT

        assert expected_gas_cost == estimator.gas_limit()

    def test_estimation_for_create_gtb_spot_limit_order(self, basic_composer, inj_usdt_spot_market):
        composer = basic_composer
        market_id = inj_usdt_spot_market.id

        message = composer.msg_create_spot_limit_order(
            market_id=market_id,
            sender="senders",
            subaccount_id="subaccount_id",
            fee_recipient="fee_recipient",
            price=Decimal("7.523"),
            quantity=Decimal("0.01"),
            order_type="BUY",
            expiration_block=1234567,
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_gas_cost = math.ceil(Decimal(SPOT_ORDER_CREATION_GAS_LIMIT) * Decimal(GTB_ORDERS_GAS_MULTIPLIER))

        assert expected_gas_cost == estimator.gas_limit()

        po_order_message = composer.msg_create_spot_limit_order(
            market_id=market_id,
            sender="senders",
            subaccount_id="subaccount_id",
            fee_recipient="fee_recipient",
            price=Decimal("7.523"),
            quantity=Decimal("0.01"),
            order_type="BUY_PO",
            expiration_block=1234567,
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=po_order_message)

        expected_gas_cost = math.ceil(
            Decimal(POST_ONLY_SPOT_ORDER_CREATION_GAS_LIMIT) * Decimal(GTB_ORDERS_GAS_MULTIPLIER)
        )

        assert expected_gas_cost == estimator.gas_limit()

    def test_estimation_for_create_spot_market_order(self, basic_composer, inj_usdt_spot_market):
        composer = basic_composer
        market_id = inj_usdt_spot_market.id

        message = composer.msg_create_spot_market_order(
            market_id=market_id,
            sender="senders",
            subaccount_id="subaccount_id",
            fee_recipient="fee_recipient",
            price=Decimal("7.523"),
            quantity=Decimal("0.01"),
            order_type="BUY",
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_gas_cost = SPOT_MARKET_ORDER_CREATION_GAS_LIMIT

        assert expected_gas_cost == estimator.gas_limit()

    def test_estimation_for_cancel_spot_order(self, basic_composer, inj_usdt_spot_market):
        composer = basic_composer
        market_id = inj_usdt_spot_market.id

        message = composer.msg_cancel_spot_order(
            market_id=market_id,
            sender="senders",
            subaccount_id="subaccount_id",
            cid="cid",
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_gas_cost = SPOT_ORDER_CANCELATION_GAS_LIMIT

        assert expected_gas_cost == estimator.gas_limit()

    def test_estimation_for_create_derivative_limit_order(self, basic_composer, btc_usdt_perp_market):
        composer = basic_composer
        market_id = btc_usdt_perp_market.id

        message = composer.msg_create_derivative_limit_order(
            market_id=market_id,
            sender="senders",
            subaccount_id="subaccount_id",
            fee_recipient="fee_recipient",
            price=Decimal("7.523"),
            quantity=Decimal("0.01"),
            margin=Decimal("7.523") * Decimal("0.01"),
            order_type="BUY",
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_gas_cost = DERIVATIVE_ORDER_CREATION_GAS_LIMIT

        assert expected_gas_cost == estimator.gas_limit()

        po_order_message = composer.msg_create_derivative_limit_order(
            market_id=market_id,
            sender="senders",
            subaccount_id="subaccount_id",
            fee_recipient="fee_recipient",
            price=Decimal("7.523"),
            quantity=Decimal("0.01"),
            margin=Decimal("7.523") * Decimal("0.01"),
            order_type="BUY_PO",
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=po_order_message)

        expected_gas_cost = POST_ONLY_DERIVATIVE_ORDER_CREATION_GAS_LIMIT

        assert expected_gas_cost == estimator.gas_limit()

    def test_estimation_for_create_gtb_derivative_limit_order(self, basic_composer, btc_usdt_perp_market):
        composer = basic_composer
        market_id = btc_usdt_perp_market.id

        message = composer.msg_create_derivative_limit_order(
            market_id=market_id,
            sender="senders",
            subaccount_id="subaccount_id",
            fee_recipient="fee_recipient",
            price=Decimal("7.523"),
            quantity=Decimal("0.01"),
            margin=Decimal("7.523") * Decimal("0.01"),
            order_type="BUY",
            expiration_block=1234567,
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_gas_cost = math.ceil(Decimal(DERIVATIVE_ORDER_CREATION_GAS_LIMIT) * Decimal(GTB_ORDERS_GAS_MULTIPLIER))

        assert expected_gas_cost == estimator.gas_limit()

        po_order_message = composer.msg_create_derivative_limit_order(
            market_id=market_id,
            sender="senders",
            subaccount_id="subaccount_id",
            fee_recipient="fee_recipient",
            price=Decimal("7.523"),
            quantity=Decimal("0.01"),
            margin=Decimal("7.523") * Decimal("0.01"),
            order_type="BUY_PO",
            expiration_block=1234567,
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=po_order_message)

        expected_gas_cost = math.ceil(
            Decimal(POST_ONLY_DERIVATIVE_ORDER_CREATION_GAS_LIMIT) * Decimal(GTB_ORDERS_GAS_MULTIPLIER)
        )

        assert expected_gas_cost == estimator.gas_limit()

    def test_estimation_for_create_derivative_market_order(self, basic_composer, btc_usdt_perp_market):
        composer = basic_composer
        market_id = btc_usdt_perp_market.id

        message = composer.msg_create_derivative_market_order(
            market_id=market_id,
            sender="senders",
            subaccount_id="subaccount_id",
            fee_recipient="fee_recipient",
            price=Decimal("7.523"),
            quantity=Decimal("0.01"),
            margin=Decimal("7.523") * Decimal("0.01"),
            order_type="BUY",
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_gas_cost = DERIVATIVE_MARKET_ORDER_CREATION_GAS_LIMIT

        assert expected_gas_cost == estimator.gas_limit()

    def test_estimation_for_cancel_derivative_order(self, basic_composer, btc_usdt_perp_market):
        composer = basic_composer
        market_id = btc_usdt_perp_market.id

        message = composer.msg_cancel_derivative_order(
            market_id=market_id,
            sender="senders",
            subaccount_id="subaccount_id",
            is_buy=True,
            is_market_order=False,
            is_conditional=False,
            cid="cid",
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_gas_cost = DERIVATIVE_ORDER_CANCELATION_GAS_LIMIT

        assert expected_gas_cost == estimator.gas_limit()

    def test_estimation_for_create_binary_options_limit_order(self, basic_composer, first_match_bet_market):
        composer = basic_composer
        market_id = first_match_bet_market.id

        message = composer.msg_create_binary_options_limit_order(
            market_id=market_id,
            sender="senders",
            subaccount_id="subaccount_id",
            fee_recipient="fee_recipient",
            price=Decimal("0.5"),
            quantity=Decimal("10"),
            margin=Decimal("0.5") * Decimal("10"),
            order_type="BUY",
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_gas_cost = BINARY_OPTIONS_ORDER_CREATION_GAS_LIMIT

        assert expected_gas_cost == estimator.gas_limit()

        po_order_message = composer.msg_create_binary_options_limit_order(
            market_id=market_id,
            sender="senders",
            subaccount_id="subaccount_id",
            fee_recipient="fee_recipient",
            price=Decimal("0.5"),
            quantity=Decimal("10"),
            margin=Decimal("0.5") * Decimal("10"),
            order_type="BUY_PO",
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=po_order_message)

        expected_gas_cost = POST_ONLY_BINARY_OPTIONS_ORDER_CREATION_GAS_LIMIT

        assert expected_gas_cost == estimator.gas_limit()

    def test_estimation_for_create_gtb_binary_options_limit_order(self, basic_composer, first_match_bet_market):
        composer = basic_composer
        market_id = first_match_bet_market.id

        message = composer.msg_create_binary_options_limit_order(
            market_id=market_id,
            sender="senders",
            subaccount_id="subaccount_id",
            fee_recipient="fee_recipient",
            price=Decimal("0.5"),
            quantity=Decimal("10"),
            margin=Decimal("0.5") * Decimal("10"),
            order_type="BUY",
            expiration_block=1234567,
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_gas_cost = math.ceil(
            Decimal(BINARY_OPTIONS_ORDER_CREATION_GAS_LIMIT) * Decimal(GTB_ORDERS_GAS_MULTIPLIER)
        )

        assert expected_gas_cost == estimator.gas_limit()

        po_order_message = composer.msg_create_binary_options_limit_order(
            market_id=market_id,
            sender="senders",
            subaccount_id="subaccount_id",
            fee_recipient="fee_recipient",
            price=Decimal("0.5"),
            quantity=Decimal("10"),
            margin=Decimal("0.5") * Decimal("10"),
            order_type="BUY_PO",
            expiration_block=1234567,
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=po_order_message)

        expected_gas_cost = math.ceil(
            Decimal(POST_ONLY_BINARY_OPTIONS_ORDER_CREATION_GAS_LIMIT) * Decimal(GTB_ORDERS_GAS_MULTIPLIER)
        )

        assert expected_gas_cost == estimator.gas_limit()

    def test_estimation_for_create_binary_options_market_order(self, basic_composer, first_match_bet_market):
        composer = basic_composer
        market_id = first_match_bet_market.id

        message = composer.msg_create_binary_options_market_order(
            market_id=market_id,
            sender="senders",
            subaccount_id="subaccount_id",
            fee_recipient="fee_recipient",
            price=Decimal("0.5"),
            quantity=Decimal("10"),
            margin=Decimal("0.5") * Decimal("10"),
            order_type="BUY",
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_gas_cost = BINARY_OPTIONS_MARKET_ORDER_CREATION_GAS_LIMIT

        assert expected_gas_cost == estimator.gas_limit()

    def test_estimation_for_cancel_binary_options_order(self, basic_composer, first_match_bet_market):
        composer = basic_composer
        market_id = first_match_bet_market.id

        message = composer.msg_cancel_binary_options_order(
            market_id=market_id,
            sender="senders",
            subaccount_id="subaccount_id",
            is_buy=True,
            is_market_order=False,
            is_conditional=False,
            cid="cid",
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_gas_cost = BINARY_OPTIONS_ORDER_CANCELATION_GAS_LIMIT

        assert expected_gas_cost == estimator.gas_limit()

    def test_estimation_for_deposit(self, basic_composer):
        composer = basic_composer

        message = composer.msg_deposit(
            sender="senders",
            subaccount_id="subaccount_id",
            amount=Decimal("10"),
            denom="inj",
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_gas_cost = DEPOSIT_GAS_LIMIT

        assert expected_gas_cost == estimator.gas_limit()

    def test_estimation_for_withdraw(self, basic_composer):
        composer = basic_composer

        message = composer.msg_withdraw(
            sender="senders",
            subaccount_id="subaccount_id",
            amount=Decimal("10"),
            denom="inj",
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_gas_cost = WITHDRAW_GAS_LIMIT

        assert expected_gas_cost == estimator.gas_limit()

    def test_estimation_for_subaccount_transfer(self, basic_composer):
        composer = basic_composer

        message = composer.msg_subaccount_transfer(
            sender="senders",
            source_subaccount_id="subaccount_id",
            destination_subaccount_id="destination_subaccount_id",
            amount=Decimal("10"),
            denom="inj",
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_gas_cost = SUBACCOUNT_TRANSFER_GAS_LIMIT

        assert expected_gas_cost == estimator.gas_limit()

    def test_estimation_for_external_transfer(self, basic_composer):
        composer = basic_composer

        message = composer.msg_external_transfer(
            sender="senders",
            source_subaccount_id="subaccount_id",
            destination_subaccount_id="destination_subaccount_id",
            amount=Decimal("10"),
            denom="inj",
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_gas_cost = EXTERNAL_TRANSFER_GAS_LIMIT

        assert expected_gas_cost == estimator.gas_limit()

    def test_estimation_for_increase_position_margin(self, basic_composer, btc_usdt_perp_market):
        composer = basic_composer

        message = composer.msg_increase_position_margin(
            sender="senders",
            source_subaccount_id="subaccount_id",
            destination_subaccount_id="destination_subaccount_id",
            market_id=btc_usdt_perp_market.id,
            amount=Decimal("10"),
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_gas_cost = INCREASE_POSITION_MARGIN_TRANSFER_GAS_LIMIT

        assert expected_gas_cost == estimator.gas_limit()

    def test_estimation_for_decrease_position_margin(self, basic_composer, btc_usdt_perp_market):
        composer = basic_composer

        message = composer.msg_decrease_position_margin(
            sender="senders",
            source_subaccount_id="subaccount_id",
            destination_subaccount_id="destination_subaccount_id",
            market_id=btc_usdt_perp_market.id,
            amount=Decimal("10"),
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_gas_cost = DECREASE_POSITION_MARGIN_TRANSFER_GAS_LIMIT

        assert expected_gas_cost == estimator.gas_limit()

    def test_estimation_for_exec_message(self, basic_composer):
        market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
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
        message = basic_composer.msg_exec(grantee="grantee", msgs=[inner_message])

        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_order_gas_limit = SPOT_ORDER_CREATION_GAS_LIMIT
        expected_exec_message_gas_limit = ExecGasLimitEstimator.DEFAULT_GAS_LIMIT

        assert expected_order_gas_limit + expected_exec_message_gas_limit == estimator.gas_limit()

    def test_estimation_for_privileged_execute_contract_message(self):
        message = injective_exchange_tx_pb.MsgPrivilegedExecuteContract()
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_gas_limit = 900_000

        assert expected_gas_limit == estimator.gas_limit()

    def test_estimation_for_execute_contract_message(self):
        composer = Composer(network="testnet")
        message = composer.msg_execute_contract(
            sender="",
            contract="",
            msg="",
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_gas_limit = 375_000

        assert expected_gas_limit == estimator.gas_limit()

    def test_estimation_for_wasm_message(self):
        message = wasm_tx_pb.MsgInstantiateContract2()
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_gas_limit = 225_000

        assert expected_gas_limit == estimator.gas_limit()

    def test_estimation_for_governance_message(self):
        message = gov_tx_pb.MsgDeposit()
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_gas_limit = 2_250_000

        assert expected_gas_limit == estimator.gas_limit()

    def test_estimation_for_generic_exchange_message(self, basic_composer):
        market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        message = basic_composer.msg_liquidate_position(
            sender="sender",
            market_id=market_id,
            subaccount_id="subaccount_id",
        )
        estimator = GasHeuristicsGasLimitEstimator.for_message(message=message)

        expected_gas_limit = 120_000

        assert expected_gas_limit == estimator.gas_limit()
