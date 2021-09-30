from .proto.cosmos.bank.v1beta1 import tx_pb2 as cosmos_bank_tx_pb
from .proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_base_coin_pb

from .proto.injective.exchange.v1beta1 import tx_pb2 as injective_exchange_tx_pb
from .proto.injective.exchange.v1beta1 import exchange_pb2 as injective_exchange_pb

from .constant import Denom
from .utils import *

class Composer:
    def __init__(self, network: str):
        self.network =  network

    def Coin(self, amount: int, denom: str):
        return cosmos_base_coin_pb.Coin(
            amount=amount,
            denom=denom
        )

    def OrderData(self, market_id: str, subaccount_id: str, order_hash: str):
        return injective_exchange_tx_pb.OrderData(
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hash=order_hash
        )

    def SpotOrder(
        self,
        market_id: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        isBuy: bool
    ):
        # load denom metadata
        denom =  Denom.load_market(self.network, market_id)
        print('Loaded market metadata for', denom.description)

        # prepare values
        quantity = spot_quantity_to_backend(quantity, denom)
        price = spot_price_to_backend(price, denom)
        trigger_price = spot_price_to_backend(0, denom)
        order_type = injective_exchange_pb.OrderType.BUY if isBuy else injective_exchange_pb.OrderType.SELL

        return injective_exchange_pb.SpotOrder(
            market_id=market_id,
            order_info=injective_exchange_pb.OrderInfo(
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=price,
                quantity=quantity
            ),
            order_type=order_type,
            trigger_price=trigger_price
        )

    def DerivativeOrder(
        self,
        market_id: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        leverage: float,
        isBuy: bool
    ):
        # load denom metadata
        denom =  Denom.load_market(self.network, market_id)
        print('Loaded market metadata for', denom.description)

        # prepare values
        margin = derivative_margin_to_backend(price, quantity, leverage, denom)
        price = derivative_price_to_backend(price, denom)
        trigger_price = derivative_price_to_backend(0, denom)
        quantity = derivative_quantity_to_backend(quantity, denom)
        order_type = injective_exchange_pb.OrderType.BUY if isBuy else injective_exchange_pb.OrderType.SELL

        return injective_exchange_pb.DerivativeOrder(
            market_id=market_id,
            order_info=injective_exchange_pb.OrderInfo(
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=price,
                quantity=quantity
            ),
            margin=margin,
            order_type=order_type,
            trigger_price=trigger_price
        )

    def MsgSend(self, from_address: str, to_address: str, amount: int, denom: str):
        peggy_denom, decimals = Denom.load_peggy_denom(self.network, denom)
        be_amount = amount_to_backend(amount, decimals)
        print("Loaded send symbol {} ({}) with decimals = {}".format(denom, peggy_denom, decimals))

        return cosmos_bank_tx_pb.MsgSend(
            from_address=from_address,
            to_address=to_address,
            amount=[self.Coin(amount=be_amount,denom=peggy_denom)]
        )

    def MsgDeposit(self, sender: str, subaccount_id: str, amount: int, denom: str):
        peggy_denom, decimals = Denom.load_peggy_denom(self.network, denom)
        be_amount = amount_to_backend(amount, decimals)
        print("Loaded deposit symbol {} ({}) with decimals = {}".format(denom, peggy_denom, decimals))

        return injective_exchange_tx_pb.MsgDeposit(
            sender=sender,
            subaccount_id=subaccount_id,
            amount=self.Coin(amount=be_amount,denom=peggy_denom)
        )

    def MsgCreateSpotLimitOrder(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        isBuy: bool
    ):
        return injective_exchange_tx_pb.MsgCreateSpotLimitOrder(
            sender=sender,
            order=self.SpotOrder(
                market_id=market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=price,
                quantity=quantity,
                isBuy=isBuy
            )
        )

    def MsgCreateSpotMarketOrder(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        isBuy: bool
    ):
        return injective_exchange_tx_pb.MsgCreateSpotMarketOrder(
            sender=sender,
            order=self.SpotOrder(
                market_id=market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=price,
                quantity=quantity,
                isBuy=isBuy
            )
        )

    def MsgCancelSpotOrder(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        order_hash: str
    ):
        return injective_exchange_tx_pb.MsgCancelSpotOrder(
            sender=sender,
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hash=order_hash
        )

    def MsgBatchCreateSpotLimitOrders(
        self,
        sender: str,
        orders: list
    ):
        return injective_exchange_tx_pb.MsgBatchCreateSpotLimitOrders(
            sender=sender,
            orders=orders
        )

    def MsgBatchCancelSpotOrders(
        self,
        sender: str,
        data: list
    ):
        return injective_exchange_tx_pb.MsgBatchCancelSpotOrders(
            sender=sender,
            data=data
        )

    def MsgCreateDerivativeLimitOrder(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        leverage: float,
        isBuy: bool
    ):
        return injective_exchange_tx_pb.MsgCreateDerivativeLimitOrder(
            sender=sender,
            order=self.DerivativeOrder(
                market_id=market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=price,
                quantity=quantity,
                leverage=leverage,
                isBuy=isBuy
            )
        )

    def MsgCreateDerivativeMarketOrder(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        leverage: float,
        isBuy: bool
    ):
        return injective_exchange_tx_pb.MsgCreateDerivativeMarketOrder(
            sender=sender,
            order=self.DerivativeOrder(
                market_id=market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=price,
                quantity=quantity,
                leverage=leverage,
                isBuy=isBuy
            )
        )

    def MsgCancelDerivativeOrder(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        order_hash: str
    ):
        return injective_exchange_tx_pb.MsgCancelDerivativeOrder(
            sender=sender,
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hash=order_hash
        )

    def MsgBatchCreateDerivativeLimitOrders(
        self,
        sender: str,
        orders: list
    ):
        return injective_exchange_tx_pb.MsgBatchCreateDerivativeLimitOrders(
            sender=sender,
            orders=orders
        )

    def MsgBatchCancelDerivativeOrders(
        self,
        sender: str,
        data: list
    ):
        return injective_exchange_tx_pb.MsgBatchCancelDerivativeOrders(
            sender=sender,
            data=data
        )

    def MsgLiquidatePosition(
        self,
        sender: str,
        subaccount_id: str,
        market_id: str
    ):
        return injective_exchange_tx_pb.MsgLiquidatePosition(
            sender=sender,
            subaccount_id=subaccount_id,
            market_id=market_id
        )

    def MsgIncreasePositionMargin (
        self,
        sender: str,
        source_subaccount_id: str,
        destination_subaccount_id: str,
        market_id: str,
        amount: str
    ):
        denom =  Denom.load_market(self.network, market_id)
        additional_margin = derivative_additional_margin_to_backend(amount, denom)
        return injective_exchange_tx_pb.MsgIncreasePositionMargin(
            sender=sender,
            source_subaccount_id=source_subaccount_id,
            destination_subaccount_id=destination_subaccount_id,
            market_id=market_id,
            amount=additional_margin
        )

    def MsgSubaccountTransfer (
        self,
        sender: str,
        source_subaccount_id: str,
        destination_subaccount_id: str,
        amount: int,
        denom: str
    ):

        return injective_exchange_tx_pb.MsgSubaccountTransfer(
            sender=sender,
            source_subaccount_id=source_subaccount_id,
            destination_subaccount_id=destination_subaccount_id,
            amount=self.Coin(amount=str(amount),denom=denom)
        )

    def MsgWithdraw(
        self,
        sender: str,
        subaccount_id: str,
        amount: float,
        denom: str
    ):
        peggy_denom, decimals = Denom.load_peggy_denom(self.network, denom)
        be_amount = amount_to_backend(amount, decimals)
        print("Loaded withdrawal symbol {} ({}) with decimals = {}".format(denom, peggy_denom, decimals))

        return injective_exchange_tx_pb.MsgWithdraw(
            sender=sender,
            subaccount_id=subaccount_id,
            amount=self.Coin(amount=be_amount,denom=peggy_denom)
        )

class Parser:
    # data field format: [request-msg-header][raw-byte-msg-response]
    # you need to figure out this magic prefix number to trim request-msg-header off the data
    # then parse the rest into corresponding response type

    # Spot
    @staticmethod
    def MsgCreateSpotLimitOrderResponse(data, simulation=False):
        if not simulation:
            data = bytes.fromhex(data)
        prefix = 57
        return injective_exchange_tx_pb.MsgCreateSpotLimitOrderResponse.FromString(data[prefix:])

    @staticmethod
    def MsgCreateSpotMarketOrderResponse(data, simulation=False):
        if not simulation:
            data = bytes.fromhex(data)
        prefix = 58
        return injective_exchange_tx_pb.MsgCreateSpotMarketOrderResponse.FromString(data[prefix:])

    @staticmethod
    def MsgBatchCreateSpotLimitOrdersResponse(data, simulation=False):
        if not simulation:
            data = bytes.fromhex(data)
        prefix = 65
        return injective_exchange_tx_pb.MsgBatchCreateSpotLimitOrdersResponse.FromString(data[prefix:])

    @staticmethod
    def MsgBatchCancelSpotOrdersResponse(data, simulation=False):
        if not simulation:
            data = bytes.fromhex(data)
        prefix = 58
        return injective_exchange_tx_pb.MsgBatchCancelSpotOrdersResponse.FromString(data[prefix:])

    # derivative
    @staticmethod
    def MsgCreateDerivativeLimitOrderResponse(data, simulation=False):
        if not simulation:
            data = bytes.fromhex(data)
        prefix = 64
        return injective_exchange_tx_pb.MsgCreateDerivativeLimitOrderResponse.FromString(data[prefix:])

    @staticmethod
    def MsgCreateDerivativeMarketOrderResponse(data, simulation=False):
        if not simulation:
            data = bytes.fromhex(data)
        prefix = 64
        return injective_exchange_tx_pb.MsgCreateDerivativeMarketOrderResponse.FromString(data[prefix:])

    @staticmethod
    def MsgBatchCreateDerivativeLimitOrdersResponse(data, simulation=False):
        if not simulation:
            data = bytes.fromhex(data)
        prefix = 71
        return injective_exchange_tx_pb.MsgBatchCreateDerivativeLimitOrdersResponse.FromString(data[prefix:])

    @staticmethod
    def MsgBatchCancelDerivativeOrdersResponse(data, simulation=False):
        if not simulation:
            data = bytes.fromhex(data)
        prefix = 64
        return injective_exchange_tx_pb.MsgBatchCancelDerivativeOrdersResponse.FromString(data[prefix:])
