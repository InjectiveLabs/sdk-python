import math
from abc import ABC, abstractmethod
from decimal import Decimal
from typing import Union

from google.protobuf import any_pb2

from pyinjective.core.gas_limit_estimator import GasLimitEstimator
from pyinjective.proto.cosmos.authz.v1beta1 import tx_pb2 as cosmos_authz_tx_pb
from pyinjective.proto.injective.exchange.v2 import (
    order_pb2 as injective_order_v2_pb,
    tx_pb2 as injective_exchange_tx_pb,
)

SPOT_ORDER_CREATION_GAS_LIMIT = 100_000
SPOT_MARKET_ORDER_CREATION_GAS_LIMIT = 50_000
POST_ONLY_SPOT_ORDER_CREATION_GAS_LIMIT = 120_000
DERIVATIVE_ORDER_CREATION_GAS_LIMIT = 120_000
DERIVATIVE_MARKET_ORDER_CREATION_GAS_LIMIT = 105_000
POST_ONLY_DERIVATIVE_ORDER_CREATION_GAS_LIMIT = 140_000
BINARY_OPTIONS_ORDER_CREATION_GAS_LIMIT = DERIVATIVE_ORDER_CREATION_GAS_LIMIT
BINARY_OPTIONS_MARKET_ORDER_CREATION_GAS_LIMIT = DERIVATIVE_MARKET_ORDER_CREATION_GAS_LIMIT
POST_ONLY_BINARY_OPTIONS_ORDER_CREATION_GAS_LIMIT = POST_ONLY_DERIVATIVE_ORDER_CREATION_GAS_LIMIT
SPOT_ORDER_CANCELATION_GAS_LIMIT = 65_000
DERIVATIVE_ORDER_CANCELATION_GAS_LIMIT = 70_000
BINARY_OPTIONS_ORDER_CANCELATION_GAS_LIMIT = DERIVATIVE_ORDER_CANCELATION_GAS_LIMIT

GTB_ORDERS_GAS_MULTIPLIER = "1.1"

DEPOSIT_GAS_LIMIT = 38_000
WITHDRAW_GAS_LIMIT = 35_000
SUBACCOUNT_TRANSFER_GAS_LIMIT = 15_000
EXTERNAL_TRANSFER_GAS_LIMIT = 40_000
INCREASE_POSITION_MARGIN_TRANSFER_GAS_LIMIT = 51_000
DECREASE_POSITION_MARGIN_TRANSFER_GAS_LIMIT = 60_000


class GasHeuristicsGasLimitEstimator(ABC):
    GENERAL_MESSAGE_GAS_LIMIT = 25_000
    BASIC_REFERENCE_GAS_LIMIT = 150_000

    @classmethod
    @abstractmethod
    def applies_to(cls, message: any_pb2.Any) -> bool:
        ...

    @classmethod
    def for_message(cls, message: any_pb2.Any):
        estimator_class = next(
            (
                estimator_subclass
                for estimator_subclass in cls.__subclasses__()
                if estimator_subclass.applies_to(message=message)
            ),
            None,
        )
        if estimator_class is None:
            estimator = GasLimitEstimator.for_message(message=message)
        else:
            estimator = estimator_class(message=message)

        return estimator

    @abstractmethod
    def gas_limit(self) -> int:
        ...

    @staticmethod
    def message_type(message: any_pb2.Any) -> str:
        if isinstance(message, any_pb2.Any):
            message_type = message.type_url
        else:
            message_type = message.DESCRIPTOR.full_name
        return message_type

    @abstractmethod
    def _message_class(self, message: any_pb2.Any):
        ...

    def _parsed_message(self, message: any_pb2.Any) -> any_pb2.Any:
        if isinstance(message, any_pb2.Any):
            parsed_message = self._message_class(message=message).FromString(message.value)
        else:
            parsed_message = message
        return parsed_message

    @staticmethod
    def is_post_only_order(
        order: Union[injective_order_v2_pb.SpotOrder, injective_order_v2_pb.DerivativeOrder],
    ) -> bool:
        return order.order_type in [injective_order_v2_pb.OrderType.BUY_PO, injective_order_v2_pb.OrderType.SELL_PO]


class CreateSpotLimitOrdersGasLimitEstimator(GasHeuristicsGasLimitEstimator):
    def __init__(self, message: any_pb2.Any):
        self._message = self._parsed_message(message=message)

    @classmethod
    def applies_to(cls, message: any_pb2.Any):
        return cls.message_type(message=message).endswith("MsgCreateSpotLimitOrder")

    @staticmethod
    def gas_cost_for_order(order: injective_order_v2_pb.SpotOrder) -> int:
        if GasHeuristicsGasLimitEstimator.is_post_only_order(order):
            gas_cost = POST_ONLY_SPOT_ORDER_CREATION_GAS_LIMIT
        else:
            gas_cost = SPOT_ORDER_CREATION_GAS_LIMIT

        if order.expiration_block > 0:
            gas_cost = math.ceil(Decimal(gas_cost) * Decimal(GTB_ORDERS_GAS_MULTIPLIER))

        return gas_cost

    def gas_limit(self) -> int:
        return self.gas_cost_for_order(self._message.order)

    def _message_class(self, message: any_pb2.Any):
        return injective_exchange_tx_pb.MsgCreateSpotLimitOrder


class CreateSpotMarketOrdersGasLimitEstimator(GasHeuristicsGasLimitEstimator):
    def __init__(self, message: any_pb2.Any):
        self._message = self._parsed_message(message=message)

    @classmethod
    def applies_to(cls, message: any_pb2.Any):
        return cls.message_type(message=message).endswith("MsgCreateSpotMarketOrder")

    def gas_limit(self) -> int:
        return SPOT_MARKET_ORDER_CREATION_GAS_LIMIT

    def _message_class(self, message: any_pb2.Any):
        return injective_exchange_tx_pb.MsgCreateSpotMarketOrder


class CancelSpotOrderGasLimitEstimator(GasHeuristicsGasLimitEstimator):
    def __init__(self, message: any_pb2.Any):
        self._message = self._parsed_message(message=message)

    @classmethod
    def applies_to(cls, message: any_pb2.Any):
        return cls.message_type(message=message).endswith("MsgCancelSpotOrder")

    def gas_limit(self) -> int:
        return SPOT_ORDER_CANCELATION_GAS_LIMIT

    def _message_class(self, message: any_pb2.Any):
        return injective_exchange_tx_pb.MsgCancelSpotOrder


class CreateDerivativeLimitOrdersGasLimitEstimator(GasHeuristicsGasLimitEstimator):
    def __init__(self, message: any_pb2.Any):
        self._message = self._parsed_message(message=message)

    @classmethod
    def applies_to(cls, message: any_pb2.Any):
        return cls.message_type(message=message).endswith("MsgCreateDerivativeLimitOrder")

    @staticmethod
    def gas_cost_for_order(order: injective_order_v2_pb.DerivativeOrder) -> int:
        if GasHeuristicsGasLimitEstimator.is_post_only_order(order=order):
            gas_cost = POST_ONLY_DERIVATIVE_ORDER_CREATION_GAS_LIMIT
        else:
            gas_cost = DERIVATIVE_ORDER_CREATION_GAS_LIMIT

        if order.expiration_block > 0:
            gas_cost = math.ceil(Decimal(gas_cost) * Decimal(GTB_ORDERS_GAS_MULTIPLIER))

        return gas_cost

    def gas_limit(self) -> int:
        return self.gas_cost_for_order(self._message.order)

    def _message_class(self, message: any_pb2.Any):
        return injective_exchange_tx_pb.MsgCreateDerivativeLimitOrder


class CreateDerivativeMarketOrdersGasLimitEstimator(GasHeuristicsGasLimitEstimator):
    def __init__(self, message: any_pb2.Any):
        self._message = self._parsed_message(message=message)

    @classmethod
    def applies_to(cls, message: any_pb2.Any):
        return cls.message_type(message=message).endswith("MsgCreateDerivativeMarketOrder")

    def gas_limit(self) -> int:
        return DERIVATIVE_MARKET_ORDER_CREATION_GAS_LIMIT

    def _message_class(self, message: any_pb2.Any):
        return injective_exchange_tx_pb.MsgCreateDerivativeMarketOrder


class CancelDerivativeOrderGasLimitEstimator(GasHeuristicsGasLimitEstimator):
    def __init__(self, message: any_pb2.Any):
        self._message = self._parsed_message(message=message)

    @classmethod
    def applies_to(cls, message: any_pb2.Any):
        return cls.message_type(message=message).endswith("MsgCancelDerivativeOrder")

    def gas_limit(self) -> int:
        return DERIVATIVE_ORDER_CANCELATION_GAS_LIMIT

    def _message_class(self, message: any_pb2.Any):
        return injective_exchange_tx_pb.MsgCancelDerivativeOrder


class CreateBinaryOptionsLimitOrdersGasLimitEstimator(GasHeuristicsGasLimitEstimator):
    def __init__(self, message: any_pb2.Any):
        self._message = self._parsed_message(message=message)

    @classmethod
    def applies_to(cls, message: any_pb2.Any):
        return cls.message_type(message=message).endswith("MsgCreateBinaryOptionsLimitOrder")

    @staticmethod
    def gas_cost_for_order(order: injective_order_v2_pb.DerivativeOrder) -> int:
        if GasHeuristicsGasLimitEstimator.is_post_only_order(order=order):
            gas_cost = POST_ONLY_BINARY_OPTIONS_ORDER_CREATION_GAS_LIMIT
        else:
            gas_cost = BINARY_OPTIONS_ORDER_CREATION_GAS_LIMIT

        if order.expiration_block > 0:
            gas_cost = math.ceil(Decimal(gas_cost) * Decimal(GTB_ORDERS_GAS_MULTIPLIER))

        return gas_cost

    def gas_limit(self) -> int:
        return self.gas_cost_for_order(self._message.order)

    def _message_class(self, message: any_pb2.Any):
        return injective_exchange_tx_pb.MsgCreateBinaryOptionsLimitOrder


class CreateBinaryOptionsMarketOrdersGasLimitEstimator(GasHeuristicsGasLimitEstimator):
    def __init__(self, message: any_pb2.Any):
        self._message = self._parsed_message(message=message)

    @classmethod
    def applies_to(cls, message: any_pb2.Any):
        return cls.message_type(message=message).endswith("MsgCreateBinaryOptionsMarketOrder")

    def gas_limit(self) -> int:
        return BINARY_OPTIONS_MARKET_ORDER_CREATION_GAS_LIMIT

    def _message_class(self, message: any_pb2.Any):
        return injective_exchange_tx_pb.MsgCreateBinaryOptionsMarketOrder


class CancelBinaryOptionsOrderGasLimitEstimator(GasHeuristicsGasLimitEstimator):
    def __init__(self, message: any_pb2.Any):
        self._message = self._parsed_message(message=message)

    @classmethod
    def applies_to(cls, message: any_pb2.Any):
        return cls.message_type(message=message).endswith("MsgCancelBinaryOptionsOrder")

    def gas_limit(self) -> int:
        return BINARY_OPTIONS_ORDER_CANCELATION_GAS_LIMIT

    def _message_class(self, message: any_pb2.Any):
        return injective_exchange_tx_pb.MsgCancelBinaryOptionsOrder


class BatchCreateSpotLimitOrdersGasLimitEstimator(GasHeuristicsGasLimitEstimator):
    def __init__(self, message: any_pb2.Any):
        self._message = self._parsed_message(message=message)

    @classmethod
    def applies_to(cls, message: any_pb2.Any):
        return cls.message_type(message=message).endswith("MsgBatchCreateSpotLimitOrders")

    def gas_limit(self) -> int:
        total = 0

        for order in self._message.orders:
            total += CreateSpotLimitOrdersGasLimitEstimator.gas_cost_for_order(order)

        return total

    def _message_class(self, message: any_pb2.Any):
        return injective_exchange_tx_pb.MsgBatchCreateSpotLimitOrders


class BatchCancelSpotOrdersGasLimitEstimator(GasHeuristicsGasLimitEstimator):
    def __init__(self, message: any_pb2.Any):
        self._message = self._parsed_message(message=message)

    @classmethod
    def applies_to(cls, message: any_pb2.Any):
        return cls.message_type(message=message).endswith("MsgBatchCancelSpotOrders")

    def gas_limit(self) -> int:
        total = 0
        total += len(self._message.data) * SPOT_ORDER_CANCELATION_GAS_LIMIT

        return total

    def _message_class(self, message: any_pb2.Any):
        return injective_exchange_tx_pb.MsgBatchCancelSpotOrders


class BatchCreateDerivativeLimitOrdersGasLimitEstimator(GasHeuristicsGasLimitEstimator):
    def __init__(self, message: any_pb2.Any):
        self._message = self._parsed_message(message=message)

    @classmethod
    def applies_to(cls, message: any_pb2.Any):
        return cls.message_type(message=message).endswith("MsgBatchCreateDerivativeLimitOrders")

    def gas_limit(self) -> int:
        total = 0

        for order in self._message.orders:
            total += CreateDerivativeLimitOrdersGasLimitEstimator.gas_cost_for_order(order)

        return total

    def _message_class(self, message: any_pb2.Any):
        return injective_exchange_tx_pb.MsgBatchCreateDerivativeLimitOrders


class BatchCancelDerivativeOrdersGasLimitEstimator(GasHeuristicsGasLimitEstimator):
    def __init__(self, message: any_pb2.Any):
        self._message = self._parsed_message(message=message)

    @classmethod
    def applies_to(cls, message: any_pb2.Any):
        return cls.message_type(message=message).endswith("MsgBatchCancelDerivativeOrders")

    def gas_limit(self) -> int:
        total = 0
        total += len(self._message.data) * DERIVATIVE_ORDER_CANCELATION_GAS_LIMIT

        return total

    def _message_class(self, message: any_pb2.Any):
        return injective_exchange_tx_pb.MsgBatchCancelDerivativeOrders


class BatchUpdateOrdersGasLimitEstimator(GasHeuristicsGasLimitEstimator):
    AVERAGE_CANCEL_ALL_AFFECTED_ORDERS = 20

    def __init__(self, message: any_pb2.Any):
        self._message = self._parsed_message(message=message)

    @classmethod
    def applies_to(cls, message: any_pb2.Any):
        return cls.message_type(message=message).endswith("MsgBatchUpdateOrders")

    def gas_limit(self) -> int:
        total = 0

        for order in self._message.spot_orders_to_create:
            total += CreateSpotLimitOrdersGasLimitEstimator.gas_cost_for_order(order)
        for order in self._message.derivative_orders_to_create:
            total += CreateDerivativeLimitOrdersGasLimitEstimator.gas_cost_for_order(order)
        for order in self._message.binary_options_orders_to_create:
            total += CreateBinaryOptionsLimitOrdersGasLimitEstimator.gas_cost_for_order(order)

        total += len(self._message.spot_orders_to_cancel) * SPOT_ORDER_CANCELATION_GAS_LIMIT
        total += len(self._message.derivative_orders_to_cancel) * DERIVATIVE_ORDER_CANCELATION_GAS_LIMIT
        total += len(self._message.binary_options_orders_to_cancel) * BINARY_OPTIONS_ORDER_CANCELATION_GAS_LIMIT

        total += (
            len(self._message.spot_market_ids_to_cancel_all)
            * SPOT_ORDER_CANCELATION_GAS_LIMIT
            * self.AVERAGE_CANCEL_ALL_AFFECTED_ORDERS
        )
        total += (
            len(self._message.derivative_market_ids_to_cancel_all)
            * DERIVATIVE_ORDER_CANCELATION_GAS_LIMIT
            * self.AVERAGE_CANCEL_ALL_AFFECTED_ORDERS
        )
        total += (
            len(self._message.binary_options_market_ids_to_cancel_all)
            * BINARY_OPTIONS_ORDER_CANCELATION_GAS_LIMIT
            * self.AVERAGE_CANCEL_ALL_AFFECTED_ORDERS
        )

        return total

    def _message_class(self, message: any_pb2.Any):
        return injective_exchange_tx_pb.MsgBatchUpdateOrders


class DepositGasLimitEstimator(GasHeuristicsGasLimitEstimator):
    def __init__(self, message: any_pb2.Any):
        self._message = self._parsed_message(message=message)

    @classmethod
    def applies_to(cls, message: any_pb2.Any):
        message_type = cls.message_type(message=message)
        return ".exchange." in message_type and message_type.endswith("MsgDeposit")

    def gas_limit(self) -> int:
        return DEPOSIT_GAS_LIMIT

    def _message_class(self, message: any_pb2.Any):
        return injective_exchange_tx_pb.MsgDeposit


class WithdrawGasLimitEstimator(GasHeuristicsGasLimitEstimator):
    def __init__(self, message: any_pb2.Any):
        self._message = self._parsed_message(message=message)

    @classmethod
    def applies_to(cls, message: any_pb2.Any):
        message_type = cls.message_type(message=message)
        return ".exchange." in message_type and message_type.endswith("MsgWithdraw")

    def gas_limit(self) -> int:
        return WITHDRAW_GAS_LIMIT

    def _message_class(self, message: any_pb2.Any):
        return injective_exchange_tx_pb.MsgWithdraw


class SubaccountTransferGasLimitEstimator(GasHeuristicsGasLimitEstimator):
    def __init__(self, message: any_pb2.Any):
        self._message = self._parsed_message(message=message)

    @classmethod
    def applies_to(cls, message: any_pb2.Any):
        message_type = cls.message_type(message=message)
        return ".exchange." in message_type and message_type.endswith("MsgSubaccountTransfer")

    def gas_limit(self) -> int:
        return SUBACCOUNT_TRANSFER_GAS_LIMIT

    def _message_class(self, message: any_pb2.Any):
        return injective_exchange_tx_pb.MsgSubaccountTransfer


class ExternalTransferGasLimitEstimator(GasHeuristicsGasLimitEstimator):
    def __init__(self, message: any_pb2.Any):
        self._message = self._parsed_message(message=message)

    @classmethod
    def applies_to(cls, message: any_pb2.Any):
        message_type = cls.message_type(message=message)
        return ".exchange." in message_type and message_type.endswith("MsgExternalTransfer")

    def gas_limit(self) -> int:
        return EXTERNAL_TRANSFER_GAS_LIMIT

    def _message_class(self, message: any_pb2.Any):
        return injective_exchange_tx_pb.MsgExternalTransfer


class IncreasePositionMarginGasLimitEstimator(GasHeuristicsGasLimitEstimator):
    def __init__(self, message: any_pb2.Any):
        self._message = self._parsed_message(message=message)

    @classmethod
    def applies_to(cls, message: any_pb2.Any):
        message_type = cls.message_type(message=message)
        return ".exchange." in message_type and message_type.endswith("MsgIncreasePositionMargin")

    def gas_limit(self) -> int:
        return INCREASE_POSITION_MARGIN_TRANSFER_GAS_LIMIT

    def _message_class(self, message: any_pb2.Any):
        return injective_exchange_tx_pb.MsgIncreasePositionMargin


class DecreasePositionMarginGasLimitEstimator(GasHeuristicsGasLimitEstimator):
    def __init__(self, message: any_pb2.Any):
        self._message = self._parsed_message(message=message)

    @classmethod
    def applies_to(cls, message: any_pb2.Any):
        message_type = cls.message_type(message=message)
        return ".exchange." in message_type and message_type.endswith("MsgDecreasePositionMargin")

    def gas_limit(self) -> int:
        return DECREASE_POSITION_MARGIN_TRANSFER_GAS_LIMIT

    def _message_class(self, message: any_pb2.Any):
        return injective_exchange_tx_pb.MsgDecreasePositionMargin


class ExecGasLimitEstimator(GasHeuristicsGasLimitEstimator):
    DEFAULT_GAS_LIMIT = 20_000

    def __init__(self, message: any_pb2.Any):
        self._message = self._parsed_message(message=message)

    @classmethod
    def applies_to(cls, message: any_pb2.Any) -> bool:
        return cls.message_type(message=message).endswith("MsgExec")

    def gas_limit(self) -> int:
        total = sum(
            [
                GasHeuristicsGasLimitEstimator.for_message(message=inner_message).gas_limit()
                for inner_message in self._message.msgs
            ]
        )
        total += self.DEFAULT_GAS_LIMIT

        return total

    def _message_class(self, message: any_pb2.Any):
        return cosmos_authz_tx_pb.MsgExec
