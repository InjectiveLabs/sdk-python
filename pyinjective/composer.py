from .proto.cosmos.bank.v1beta1 import tx_pb2 as cosmos_bank_tx_pb
from .proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_base_coin_pb

from .proto.injective.exchange.v1beta1 import tx_pb2 as injective_exchange_tx_pb
from .proto.injective.exchange.v1beta1 import exchange_pb2 as injective_exchange_pb
from .proto.injective.types.v1beta1 import tx_response_pb2 as tx_response_pb

from .proto.injective.auction.v1beta1 import tx_pb2 as injective_auction_tx_pb

from .constant import Denom
from .utils import *

class Composer:
    def __init__(self, network: str):
        self.network = network

    def Coin(self, amount: int, denom: str):
        return cosmos_base_coin_pb.Coin(
            amount=str(amount),
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
        is_buy: bool
    ):
        # load denom metadata
        denom = Denom.load_market(self.network, market_id)
        print('Loaded market metadata for', denom.description)

        # prepare values
        quantity = spot_quantity_to_backend(quantity, denom)
        price = spot_price_to_backend(price, denom)
        trigger_price = spot_price_to_backend(0, denom)
        order_type = injective_exchange_pb.OrderType.BUY if is_buy else injective_exchange_pb.OrderType.SELL

        return injective_exchange_pb.SpotOrder(
            market_id=market_id,
            order_info=injective_exchange_pb.OrderInfo(
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=str(price),
                quantity=str(quantity)
            ),
            order_type=order_type,
            trigger_price=str(trigger_price)
        )

    def DerivativeOrder(
        self,
        market_id: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        is_buy: bool,
        **kwargs
    ):
        # load denom metadata
        denom = Denom.load_market(self.network, market_id)
        print('Loaded market metadata for', denom.description)

        if kwargs.get("is_reduce_only") is None:
            margin = derivative_margin_to_backend(price, quantity, kwargs.get("leverage"), denom)
        elif kwargs.get("is_reduce_only", True):
            margin = 0
        else:
            margin = derivative_margin_to_backend(price, quantity, kwargs.get("leverage"), denom)

        # prepare values
        price = derivative_price_to_backend(price, denom)
        trigger_price = derivative_price_to_backend(0, denom)
        quantity = derivative_quantity_to_backend(quantity, denom)
        order_type = injective_exchange_pb.OrderType.BUY if is_buy else injective_exchange_pb.OrderType.SELL

        return injective_exchange_pb.DerivativeOrder(
            market_id=market_id,
            order_info=injective_exchange_pb.OrderInfo(
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=str(price),
                quantity=str(quantity)
            ),
            margin=str(margin),
            order_type=order_type,
            trigger_price=str(trigger_price)
        )

    def MsgSend(self, from_address: str, to_address: str, amount: float, denom: str):
        peggy_denom, decimals = Denom.load_peggy_denom(self.network, denom)
        be_amount = amount_to_backend(amount, decimals)
        print("Loaded send symbol {} ({}) with decimals = {}".format(denom, peggy_denom, decimals))

        return cosmos_bank_tx_pb.MsgSend(
            from_address=from_address,
            to_address=to_address,
            amount=[self.Coin(amount=be_amount, denom=peggy_denom)]
        )

    def MsgDeposit(self, sender: str, subaccount_id: str, amount: float, denom: str):
        peggy_denom, decimals = Denom.load_peggy_denom(self.network, denom)
        be_amount = amount_to_backend(amount, decimals)
        print("Loaded deposit symbol {} ({}) with decimals = {}".format(denom, peggy_denom, decimals))

        return injective_exchange_tx_pb.MsgDeposit(
            sender=sender,
            subaccount_id=subaccount_id,
            amount=self.Coin(amount=be_amount, denom=peggy_denom)
        )

    def MsgCreateSpotLimitOrder(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        is_buy: bool
    ):
        return injective_exchange_tx_pb.MsgCreateSpotLimitOrder(
            sender=sender,
            order=self.SpotOrder(
                market_id=market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=price,
                quantity=quantity,
                is_buy=is_buy
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
        is_buy: bool
    ):
        return injective_exchange_tx_pb.MsgCreateSpotMarketOrder(
            sender=sender,
            order=self.SpotOrder(
                market_id=market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=price,
                quantity=quantity,
                is_buy=is_buy
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
        is_buy: bool,
        **kwargs
    ):
        return injective_exchange_tx_pb.MsgCreateDerivativeLimitOrder(
            sender=sender,
            order=self.DerivativeOrder(
                market_id=market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=price,
                quantity=quantity,
                is_buy=is_buy,
                leverage=kwargs.get("leverage"),
                is_reduce_only=kwargs.get("is_reduce_only")
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
        is_buy: bool
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
                is_buy=is_buy
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

    def MsgIncreasePositionMargin(
        self,
        sender: str,
        source_subaccount_id: str,
        destination_subaccount_id: str,
        market_id: str,
        amount: float,
    ):
        denom = Denom.load_market(self.network, market_id)
        additional_margin = derivative_additional_margin_to_backend(amount, denom)
        return injective_exchange_tx_pb.MsgIncreasePositionMargin(
            sender=sender,
            source_subaccount_id=source_subaccount_id,
            destination_subaccount_id=destination_subaccount_id,
            market_id=market_id,
            amount=str(additional_margin)
        )

    def MsgSubaccountTransfer(
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
            amount=self.Coin(amount=amount, denom=denom)
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
            amount=self.Coin(amount=be_amount, denom=peggy_denom)
        )

    def MsgBid(
        self,
        sender: str,
        bid_amount: float,
        round: float
    ):

        be_amount = amount_to_backend(bid_amount, 18)

        return injective_auction_tx_pb.MsgBid(
            sender=sender,
            round=round,
            bid_amount=self.Coin(amount=be_amount, denom="inj")
            )

    # data field format: [request-msg-header][raw-byte-msg-response]
    # you need to figure out this magic prefix number to trim request-msg-header off the data
    # this method handles only exchange responses
    @staticmethod
    def MsgResponses(data, simulation=False):
        if not simulation:
            data = bytes.fromhex(data)
        header_map = {
            "/injective.exchange.v1beta1.MsgCreateSpotLimitOrder": injective_exchange_tx_pb.MsgCreateSpotLimitOrderResponse,
            "/injective.exchange.v1beta1.MsgCreateSpotMarketOrder": injective_exchange_tx_pb.MsgCreateSpotMarketOrderResponse,
            "/injective.exchange.v1beta1.MsgCreateDerivativeLimitOrder": injective_exchange_tx_pb.MsgCreateDerivativeLimitOrderResponse,
            "/injective.exchange.v1beta1.MsgCreateDerivativeMarketOrder": injective_exchange_tx_pb.MsgCreateDerivativeMarketOrderResponse,
            "/injective.exchange.v1beta1.MsgCancelSpotOrder": injective_exchange_tx_pb.MsgCancelSpotOrderResponse,
            "/injective.exchange.v1beta1.MsgCancelDerivativeOrder": injective_exchange_tx_pb.MsgCancelDerivativeOrderResponse,
            "/injective.exchange.v1beta1.MsgBatchCancelSpotOrders": injective_exchange_tx_pb.MsgBatchCancelSpotOrdersResponse,
            "/injective.exchange.v1beta1.MsgBatchCancelDerivativeOrders": injective_exchange_tx_pb.MsgBatchCancelDerivativeOrdersResponse,
            "/injective.exchange.v1beta1.MsgBatchCreateSpotLimitOrders": injective_exchange_tx_pb.MsgBatchCreateSpotLimitOrdersResponse,
            "/injective.exchange.v1beta1.MsgBatchCreateDerivativeLimitOrders": injective_exchange_tx_pb.MsgBatchCreateDerivativeLimitOrdersResponse,
            "/injective.exchange.v1beta1.MsgWithdraw": injective_exchange_tx_pb.MsgWithdrawResponse,
            "/injective.exchange.v1beta1.MsgSubaccountTransfer": injective_exchange_tx_pb.MsgSubaccountTransferResponse,
            "/injective.exchange.v1beta1.MsgLiquidatePosition": injective_exchange_tx_pb.MsgLiquidatePosition,
            "/injective.exchange.v1beta1.MsgIncreasePositionMargin": injective_exchange_tx_pb.MsgIncreasePositionMargin,
            "/injective.auction.v1beta1.MsgBid": injective_auction_tx_pb.MsgBidResponse,
        }

        response = tx_response_pb.TxResponseData.FromString(data)
        msgs = []
        for msg in response.messages:
            msgs.append(header_map[msg.header].FromString(msg.data))

        return msgs
