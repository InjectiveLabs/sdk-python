from .proto.cosmos.bank.v1beta1 import tx_pb2 as cosmos_bank_tx_pb
from .proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_base_coin_pb

from .proto.injective.exchange.v1beta1 import tx_pb2 as injective_exchange_tx_pb
from .proto.injective.exchange.v1beta1 import exchange_pb2 as injective_exchange_pb

from .constant import Denoms
from .utils import *

class Composer:
    @staticmethod
    def Coin(amount: int, denom: str):
        return cosmos_base_coin_pb.Coin(
            amount=amount,
            denom=denom
        )

    @staticmethod
    def MsgSend(from_address: str, to_address: str, amount: int, denom: str):
        return cosmos_bank_tx_pb.MsgSend(
            from_address=from_address,
            to_address=to_address,
            amount=[Composer.Coin(amount=str(amount),denom=denom)]
        )

    @staticmethod
    def MsgDeposit(sender: str, subaccount_id: str, amount: int, denom: str):
        return injective_exchange_tx_pb.MsgDeposit(
            sender=sender,
            subaccount_id=subaccount_id,
            amount=Composer.Coin(amount=str(amount),denom=denom)
        )

    @staticmethod
    def MsgCreateSpotLimitOrder(
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        isBuy: bool
    ):
        # load denom metadata
        denom =  Denoms.load_market(market_id)
        print('loaded market metadata for', denom.description)

        # prepare values
        quantity = spot_quantity_to_backend(quantity, denom)
        price = spot_price_to_backend(price, denom)
        trigger_price = spot_price_to_backend(0, denom)
        order_type = injective_exchange_pb.OrderType.BUY if isBuy else injective_exchange_pb.OrderType.SELL

        # compose proto msg
        return injective_exchange_tx_pb.MsgCreateSpotLimitOrder(
            sender=sender,
            order=injective_exchange_pb.SpotOrder(
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
        )

    @staticmethod
    def MsgCreateSpotMarketOrder(
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        isBuy: bool
    ):
        # load denom metadata
        denom =  Denoms.load_market(market_id)
        print('loaded market metadata for', denom.description)

        # prepare values
        quantity = spot_quantity_to_backend(quantity, denom)
        price = spot_price_to_backend(price, denom)
        trigger_price = spot_price_to_backend(0, denom)
        order_type = injective_exchange_pb.OrderType.BUY if isBuy else injective_exchange_pb.OrderType.SELL

        # compose proto msg
        return injective_exchange_tx_pb.MsgCreateSpotMarketOrder(
            sender=sender,
            order=injective_exchange_pb.SpotOrder(
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
        )

    @staticmethod
    def MsgCancelSpotOrder(
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

    @staticmethod
    def MsgCreateDerivativeLimitOrder(
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        leverage: float,
        isBuy: bool
    ):
        # load denom metadata
        denom =  Denoms.load_market(market_id)
        print('loaded market metadata for', denom.description)

        # prepare values
        margin = derivative_margin_to_backend(price, quantity, leverage, denom)
        price = derivative_price_to_backend(price, denom)
        trigger_price = derivative_price_to_backend(0, denom)
        quantity = derivative_quantity_to_backend(quantity, denom)
        order_type = injective_exchange_pb.OrderType.BUY if isBuy else injective_exchange_pb.OrderType.SELL

        # compose proto msg
        return injective_exchange_tx_pb.MsgCreateDerivativeLimitOrder(
            sender=sender,
            order=injective_exchange_pb.DerivativeOrder(
                market_id=market_id,
                order_info=injective_exchange_pb.OrderInfo(
                    subaccount_id=subaccount_id,
                    fee_recipient=fee_recipient,
                    price=price,
                    quantity=quantity,
                ),
                order_type=order_type,
                margin=margin,
                trigger_price=trigger_price
            )
        )

    @staticmethod
    def MsgCreateDerivativeMarketOrder(
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        leverage: float,
        isBuy: bool
    ):
        # load denom metadata
        denom =  Denoms.load_market(market_id)
        print('loaded market metadata for', denom.description)

        # prepare values
        margin = derivative_margin_to_backend(price, quantity, leverage, denom)
        price = derivative_price_to_backend(price, denom)
        trigger_price = derivative_price_to_backend(0, denom)
        quantity = derivative_quantity_to_backend(quantity, denom)
        order_type = injective_exchange_pb.OrderType.BUY if isBuy else injective_exchange_pb.OrderType.SELL

        # compose proto msg
        return injective_exchange_tx_pb.MsgCreateDerivativeMarketOrder(
            sender=sender,
            order=injective_exchange_pb.DerivativeOrder(
                market_id=market_id,
                order_info=injective_exchange_pb.OrderInfo(
                    subaccount_id=subaccount_id,
                    fee_recipient=fee_recipient,
                    price=price,
                    quantity=quantity,
                ),
                order_type=order_type,
                margin=margin,
                trigger_price=trigger_price
            )
        )

    @staticmethod
    def MsgCancelDerivativeOrder(
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
