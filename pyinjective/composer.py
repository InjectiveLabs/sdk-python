from time import time
import json
import logging

from google.protobuf import any_pb2, message, timestamp_pb2

from .proto.cosmos.authz.v1beta1 import authz_pb2 as cosmos_authz_pb
from .proto.cosmos.authz.v1beta1 import tx_pb2 as cosmos_authz_tx_pb

from .proto.injective.exchange.v1beta1 import authz_pb2 as injective_authz_pb

from .proto.cosmos.bank.v1beta1 import tx_pb2 as cosmos_bank_tx_pb
from .proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_base_coin_pb

from .proto.injective.exchange.v1beta1 import tx_pb2 as injective_exchange_tx_pb
from .proto.injective.exchange.v1beta1 import exchange_pb2 as injective_exchange_pb
from .proto.injective.types.v1beta1 import tx_response_pb2 as tx_response_pb

from .proto.injective.auction.v1beta1 import tx_pb2 as injective_auction_tx_pb

from .proto.injective.peggy.v1 import msgs_pb2 as injective_peggy_tx_pb

from .proto.injective.oracle.v1beta1 import tx_pb2 as injective_oracle_tx_pb

from .proto.cosmos.staking.v1beta1 import tx_pb2 as cosmos_staking_tx_pb

from .proto.cosmos.distribution.v1beta1 import tx_pb2 as cosmos_distribution_tx_pb

from .proto.cosmos.gov.v1beta1 import tx_pb2 as cosmos_gov_tx_pb

from .constant import Denom
from .utils import *
from typing import List

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)


class Composer:
    def __init__(self, network: str):
        self.network = network

    def Coin(self, amount: int, denom: str):
        return cosmos_base_coin_pb.Coin(amount=str(amount), denom=denom)

    def get_order_mask(self, **kwargs):
        order_mask = 0

        if kwargs.get("is_conditional"):
            order_mask += injective_exchange_pb.OrderMask.CONDITIONAL
        else:
            order_mask += injective_exchange_pb.OrderMask.REGULAR

        if kwargs.get("order_direction") == "buy":
            order_mask += injective_exchange_pb.OrderMask.DIRECTION_BUY_OR_HIGHER

        elif kwargs.get("order_direction") == "sell":
            order_mask += injective_exchange_pb.OrderMask.DIRECTION_SELL_OR_LOWER

        if kwargs.get("order_type") == "market":
            order_mask += injective_exchange_pb.OrderMask.TYPE_MARKET

        elif kwargs.get("order_type") == "limit":
            order_mask += injective_exchange_pb.OrderMask.TYPE_LIMIT

        if order_mask == 0:
            order_mask = 1

        return order_mask

    def OrderData(self, market_id: str, subaccount_id: str, order_hash: str, **kwargs):

        order_mask = self.get_order_mask(**kwargs)

        return injective_exchange_tx_pb.OrderData(
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hash=order_hash,
            order_mask=order_mask,
        )

    def SpotOrder(
        self,
        market_id: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        **kwargs,
    ):
        # load denom metadata
        denom = Denom.load_market(self.network, market_id)
        logging.info("Loaded market metadata for:{}".format(denom.description))

        # prepare values
        quantity = spot_quantity_to_backend(quantity, denom)
        price = spot_price_to_backend(price, denom)
        trigger_price = spot_price_to_backend(0, denom)

        if kwargs.get("is_buy") and not kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.BUY

        elif not kwargs.get("is_buy") and not kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.SELL

        elif kwargs.get("is_buy") and kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.BUY_PO

        elif not kwargs.get("is_buy") and kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.SELL_PO

        return injective_exchange_pb.SpotOrder(
            market_id=market_id,
            order_info=injective_exchange_pb.OrderInfo(
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=str(price),
                quantity=str(quantity),
            ),
            order_type=order_type,
            trigger_price=str(trigger_price),
        )

    def DerivativeOrder(
        self,
        market_id: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        trigger_price: float = 0,
        **kwargs,
    ):
        # load denom metadata
        denom = Denom.load_market(self.network, market_id)
        logging.info("Loaded market metadata for:{}".format(denom.description))

        if kwargs.get("is_reduce_only") is None:
            margin = derivative_margin_to_backend(
                price, quantity, kwargs.get("leverage"), denom
            )
        elif kwargs.get("is_reduce_only", True):
            margin = 0
        else:
            margin = derivative_margin_to_backend(
                price, quantity, kwargs.get("leverage"), denom
            )

        # prepare values
        price = derivative_price_to_backend(price, denom)
        trigger_price = derivative_price_to_backend(trigger_price, denom)
        quantity = derivative_quantity_to_backend(quantity, denom)

        if kwargs.get("is_buy") and not kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.BUY

        elif not kwargs.get("is_buy") and not kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.SELL

        elif kwargs.get("is_buy") and kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.BUY_PO

        elif not kwargs.get("is_buy") and kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.SELL_PO

        elif kwargs.get("stop_buy"):
            order_type = injective_exchange_pb.OrderType.STOP_BUY

        elif kwargs.get("stop_sell"):
            order_type = injective_exchange_pb.OrderType.STOP_SEll

        elif kwargs.get("take_buy"):
            order_type = injective_exchange_pb.OrderType.TAKE_BUY

        elif kwargs.get("take_sell"):
            order_type = injective_exchange_pb.OrderType.TAKE_SELL

        return injective_exchange_pb.DerivativeOrder(
            market_id=market_id,
            order_info=injective_exchange_pb.OrderInfo(
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=str(price),
                quantity=str(quantity),
            ),
            margin=str(margin),
            order_type=order_type,
            trigger_price=str(trigger_price),
        )

    def BinaryOptionsOrder(
        self,
        market_id: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        **kwargs,
    ):

        if "denom" in kwargs:
            denom = kwargs.get("denom")
        else:
            denom = Denom.load_market(self.network, market_id)

        # load denom metadata
        logging.info("Loaded market metadata for:{}".format(denom.description))

        if kwargs.get("is_reduce_only") is None and kwargs.get("is_buy"):
            margin = binary_options_buy_margin_to_backend(price, quantity, denom)
        elif kwargs.get("is_reduce_only") is None and not kwargs.get("is_buy"):
            margin = binary_options_sell_margin_to_backend(price, quantity, denom)
        elif kwargs.get("is_reduce_only") is False and kwargs.get("is_buy"):
            margin = binary_options_buy_margin_to_backend(price, quantity, denom)
        elif kwargs.get("is_reduce_only") is False and not kwargs.get("is_buy"):
            margin = binary_options_sell_margin_to_backend(price, quantity, denom)
        elif kwargs.get("is_reduce_only", True):
            margin = 0

        # prepare values
        price = binary_options_price_to_backend(price, denom)
        trigger_price = binary_options_price_to_backend(0, denom)
        quantity = binary_options_quantity_to_backend(quantity, denom)

        if kwargs.get("is_buy") and not kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.BUY

        elif not kwargs.get("is_buy") and not kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.SELL

        elif kwargs.get("is_buy") and kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.BUY_PO

        elif not kwargs.get("is_buy") and kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.SELL_PO

        return injective_exchange_pb.DerivativeOrder(
            market_id=market_id,
            order_info=injective_exchange_pb.OrderInfo(
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=str(price),
                quantity=str(quantity),
            ),
            margin=str(margin),
            order_type=order_type,
            trigger_price=str(trigger_price),
        )

    def MsgSend(self, from_address: str, to_address: str, amount: float, denom: str):
        peggy_denom, decimals = Denom.load_peggy_denom(self.network, denom)
        be_amount = amount_to_backend(amount, decimals)
        logging.info(
            "Loaded send symbol {} ({}) with decimals = {}".format(
                denom, peggy_denom, decimals
            )
        )

        return cosmos_bank_tx_pb.MsgSend(
            from_address=from_address,
            to_address=to_address,
            amount=[self.Coin(amount=be_amount, denom=peggy_denom)],
        )

    def MsgDeposit(self, sender: str, subaccount_id: str, amount: float, denom: str):
        peggy_denom, decimals = Denom.load_peggy_denom(self.network, denom)
        be_amount = amount_to_backend(amount, decimals)
        logging.info(
            "Loaded deposit symbol {} ({}) with decimals = {}".format(
                denom, peggy_denom, decimals
            )
        )

        return injective_exchange_tx_pb.MsgDeposit(
            sender=sender,
            subaccount_id=subaccount_id,
            amount=self.Coin(amount=be_amount, denom=peggy_denom),
        )

    def MsgCreateSpotLimitOrder(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        **kwargs,
    ):
        return injective_exchange_tx_pb.MsgCreateSpotLimitOrder(
            sender=sender,
            order=self.SpotOrder(
                market_id=market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=price,
                quantity=quantity,
                **kwargs,
            ),
        )

    def MsgCreateSpotMarketOrder(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        is_buy: bool,
    ):
        return injective_exchange_tx_pb.MsgCreateSpotMarketOrder(
            sender=sender,
            order=self.SpotOrder(
                market_id=market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=price,
                quantity=quantity,
                is_buy=is_buy,
            ),
        )

    def MsgCancelSpotOrder(
        self, market_id: str, sender: str, subaccount_id: str, order_hash: str
    ):
        return injective_exchange_tx_pb.MsgCancelSpotOrder(
            sender=sender,
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hash=order_hash,
        )

    def MsgBatchCreateSpotLimitOrders(self, sender: str, orders: List):
        return injective_exchange_tx_pb.MsgBatchCreateSpotLimitOrders(
            sender=sender, orders=orders
        )

    def MsgBatchCancelSpotOrders(self, sender: str, data: List):
        return injective_exchange_tx_pb.MsgBatchCancelSpotOrders(
            sender=sender, data=data
        )

    def MsgRewardsOptOut(self, sender: str):
        return injective_exchange_tx_pb.MsgRewardsOptOut(
            sender=sender
        )

    def MsgCreateDerivativeLimitOrder(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        **kwargs,
    ):
        return injective_exchange_tx_pb.MsgCreateDerivativeLimitOrder(
            sender=sender,
            order=self.DerivativeOrder(
                market_id=market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=price,
                quantity=quantity,
                **kwargs,
            ),
        )

    def MsgCreateDerivativeMarketOrder(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        is_buy: bool,
        **kwargs,
    ):
        return injective_exchange_tx_pb.MsgCreateDerivativeMarketOrder(
            sender=sender,
            order=self.DerivativeOrder(
                market_id=market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=price,
                quantity=quantity,
                is_buy=is_buy,
                **kwargs,
            ),
        )

    def MsgCreateBinaryOptionsLimitOrder(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        **kwargs,
    ):

        return injective_exchange_tx_pb.MsgCreateBinaryOptionsLimitOrder(
            sender=sender,
            order=self.BinaryOptionsOrder(
                market_id=market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=price,
                quantity=quantity,
                **kwargs,
            ),
        )

    def MsgCreateBinaryOptionsMarketOrder(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        **kwargs,
    ):
        return injective_exchange_tx_pb.MsgCreateBinaryOptionsMarketOrder(
            sender=sender,
            order=self.BinaryOptionsOrder(
                market_id=market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=price,
                quantity=quantity,
                **kwargs,
            ),
        )

    def MsgCancelBinaryOptionsOrder(
        self, sender: str, market_id: str, subaccount_id: str, order_hash: str
    ):

        return injective_exchange_tx_pb.MsgCancelBinaryOptionsOrder(
            sender=sender,
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hash=order_hash,
        )

    def MsgAdminUpdateBinaryOptionsMarket(
        self,
        sender: str,
        market_id: str,
        status: str,
        **kwargs,
    ):

        price_to_bytes = None

        if kwargs.get("settlement_price") is not None:
            scale_price = Decimal((kwargs.get("settlement_price") * pow(10, 18)))
            price_to_bytes = bytes(str(scale_price), "utf-8")

        else:
            price_to_bytes = ""

        return injective_exchange_tx_pb.MsgAdminUpdateBinaryOptionsMarket(
            sender=sender,
            market_id=market_id,
            settlement_price=price_to_bytes,
            expiration_timestamp=kwargs.get("expiration_timestamp"),
            settlement_timestamp=kwargs.get("settlement_timestamp"),
            status=status,
        )

    def MsgRelayProviderPrices(
        self, sender: str, provider: str, symbols: list, prices: list
    ):
        oracle_prices = []

        for price in prices:
            scale_price = Decimal((price) * pow(10, 18))
            price_to_bytes = bytes(str(scale_price), "utf-8")
            oracle_prices.append(price_to_bytes)

        return injective_oracle_tx_pb.MsgRelayProviderPrices(
            sender=sender, provider=provider, symbols=symbols, prices=oracle_prices
        )

    def MsgInstantBinaryOptionsMarketLaunch(
        self,
        sender: str,
        ticker: str,
        oracle_symbol: str,
        oracle_provider: str,
        oracle_type: str,
        oracle_scale_factor: int,
        maker_fee_rate: float,
        taker_fee_rate: float,
        expiration_timestamp: int,
        settlement_timestamp: int,
        quote_denom: str,
        quote_decimals: int,
        min_price_tick_size: float,
        min_quantity_tick_size: float,
        **kwargs,
    ):

        scaled_maker_fee_rate = Decimal((maker_fee_rate * pow(10, 18)))
        maker_fee_to_bytes = bytes(str(scaled_maker_fee_rate), "utf-8")

        scaled_taker_fee_rate = Decimal((taker_fee_rate * pow(10, 18)))
        taker_fee_to_bytes = bytes(str(scaled_taker_fee_rate), "utf-8")

        scaled_min_price_tick_size = Decimal(
            (min_price_tick_size * pow(10, quote_decimals + 18))
        )
        min_price_to_bytes = bytes(str(scaled_min_price_tick_size), "utf-8")

        scaled_min_quantity_tick_size = Decimal((min_quantity_tick_size * pow(10, 18)))
        min_quantity_to_bytes = bytes(str(scaled_min_quantity_tick_size), "utf-8")

        return injective_exchange_tx_pb.MsgInstantBinaryOptionsMarketLaunch(
            sender=sender,
            ticker=ticker,
            oracle_symbol=oracle_symbol,
            oracle_provider=oracle_provider,
            oracle_type=oracle_type,
            oracle_scale_factor=oracle_scale_factor,
            maker_fee_rate=maker_fee_to_bytes,
            taker_fee_rate=taker_fee_to_bytes,
            expiration_timestamp=expiration_timestamp,
            settlement_timestamp=settlement_timestamp,
            quote_denom=quote_denom,
            min_price_tick_size=min_price_to_bytes,
            min_quantity_tick_size=min_quantity_to_bytes,
            admin=kwargs.get("admin"),
        )

    def MsgCancelDerivativeOrder(
        self, market_id: str, sender: str, subaccount_id: str, order_hash: str, **kwargs
    ):
        order_mask = self.get_order_mask(**kwargs)

        return injective_exchange_tx_pb.MsgCancelDerivativeOrder(
            sender=sender,
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hash=order_hash,
            order_mask=order_mask,
        )

    def MsgBatchCreateDerivativeLimitOrders(self, sender: str, orders: List):
        return injective_exchange_tx_pb.MsgBatchCreateDerivativeLimitOrders(
            sender=sender, orders=orders
        )

    def MsgBatchCancelDerivativeOrders(self, sender: str, data: List):
        return injective_exchange_tx_pb.MsgBatchCancelDerivativeOrders(
            sender=sender, data=data
        )

    def MsgBatchUpdateOrders(self, sender: str, **kwargs):
        return injective_exchange_tx_pb.MsgBatchUpdateOrders(
            sender=sender,
            subaccount_id=kwargs.get("subaccount_id"),
            spot_market_ids_to_cancel_all=kwargs.get("spot_market_ids_to_cancel_all"),
            derivative_market_ids_to_cancel_all=kwargs.get(
                "derivative_market_ids_to_cancel_all"
            ),
            spot_orders_to_cancel=kwargs.get("spot_orders_to_cancel"),
            derivative_orders_to_cancel=kwargs.get("derivative_orders_to_cancel"),
            spot_orders_to_create=kwargs.get("spot_orders_to_create"),
            derivative_orders_to_create=kwargs.get("derivative_orders_to_create"),
            binary_options_orders_to_cancel=kwargs.get(
                "binary_options_orders_to_cancel"
            ),
            binary_options_market_ids_to_cancel_all=kwargs.get(
                "binary_options_market_ids_to_cancel_all"
            ),
            binary_options_orders_to_create=kwargs.get(
                "binary_options_orders_to_create"
            ),
        )

    def MsgLiquidatePosition(self, sender: str, subaccount_id: str, market_id: str):
        return injective_exchange_tx_pb.MsgLiquidatePosition(
            sender=sender, subaccount_id=subaccount_id, market_id=market_id
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
            amount=str(additional_margin),
        )

    def MsgSubaccountTransfer(
        self,
        sender: str,
        source_subaccount_id: str,
        destination_subaccount_id: str,
        amount: int,
        denom: str,
    ):

        return injective_exchange_tx_pb.MsgSubaccountTransfer(
            sender=sender,
            source_subaccount_id=source_subaccount_id,
            destination_subaccount_id=destination_subaccount_id,
            amount=self.Coin(amount=amount, denom=denom),
        )

    def MsgWithdraw(self, sender: str, subaccount_id: str, amount: float, denom: str):
        peggy_denom, decimals = Denom.load_peggy_denom(self.network, denom)
        be_amount = amount_to_backend(amount, decimals)
        logging.info(
            "Loaded withdrawal symbol {} ({}) with decimals = {}".format(
                denom, peggy_denom, decimals
            )
        )

        return injective_exchange_tx_pb.MsgWithdraw(
            sender=sender,
            subaccount_id=subaccount_id,
            amount=self.Coin(amount=be_amount, denom=peggy_denom),
        )

    def MsgExternalTransfer(
        self,
        sender: str,
        source_subaccount_id: str,
        destination_subaccount_id: str,
        amount: int,
        denom: str,
    ):
        peggy_denom, decimals = Denom.load_peggy_denom(self.network, denom)
        be_amount = amount_to_backend(amount, decimals)
        logging.debug(
            "Loaded send symbol {} ({}) with decimals = {}".format(
                denom, peggy_denom, decimals
            )
        )

        return injective_exchange_tx_pb.MsgExternalTransfer(
            sender=sender,
            source_subaccount_id=source_subaccount_id,
            destination_subaccount_id=destination_subaccount_id,
            amount=self.Coin(amount=be_amount, denom=peggy_denom),
        )

    def MsgBid(self, sender: str, bid_amount: float, round: float):

        be_amount = amount_to_backend(bid_amount, 18)

        return injective_auction_tx_pb.MsgBid(
            sender=sender,
            round=round,
            bid_amount=self.Coin(amount=be_amount, denom="inj"),
        )

    def MsgGrantGeneric(
        self, granter: str, grantee: str, msg_type: str, expire_in: int
    ):
        auth = cosmos_authz_pb.GenericAuthorization(msg=msg_type)
        any_auth = any_pb2.Any()
        any_auth.Pack(auth, type_url_prefix="")

        grant = cosmos_authz_pb.Grant(
            authorization=any_auth,
            expiration=timestamp_pb2.Timestamp(seconds=(int(time()) + expire_in)),
        )

        return cosmos_authz_tx_pb.MsgGrant(
            granter=granter, grantee=grantee, grant=grant
        )

    def MsgGrantTyped(
        self,
        granter: str,
        grantee: str,
        msg_type: str,
        expire_in: int,
        subaccount_id: str,
        **kwargs,
    ):
        auth = None
        if msg_type == "CreateSpotLimitOrderAuthz":
            auth = injective_authz_pb.CreateSpotLimitOrderAuthz(
                subaccount_id=subaccount_id, market_ids=kwargs.get("market_ids")
            )
        elif msg_type == "CreateSpotMarketOrderAuthz":
            auth = injective_authz_pb.CreateSpotMarketOrderAuthz(
                subaccount_id=subaccount_id, market_ids=kwargs.get("market_ids")
            )
        elif msg_type == "BatchCreateSpotLimitOrdersAuthz":
            auth = injective_authz_pb.BatchCreateSpotLimitOrdersAuthz(
                subaccount_id=subaccount_id, market_ids=kwargs.get("market_ids")
            )
        elif msg_type == "CancelSpotOrderAuthz":
            auth = injective_authz_pb.CancelSpotOrderAuthz(
                subaccount_id=subaccount_id, market_ids=kwargs.get("market_ids")
            )
        elif msg_type == "BatchCancelSpotOrdersAuthz":
            auth = injective_authz_pb.BatchCancelSpotOrdersAuthz(
                subaccount_id=subaccount_id, market_ids=kwargs.get("market_ids")
            )
        elif msg_type == "CreateDerivativeLimitOrderAuthz":
            auth = injective_authz_pb.CreateDerivativeLimitOrderAuthz(
                subaccount_id=subaccount_id, market_ids=kwargs.get("market_ids")
            )
        elif msg_type == "CreateDerivativeMarketOrderAuthz":
            auth = injective_authz_pb.CreateDerivativeMarketOrderAuthz(
                subaccount_id=subaccount_id, market_ids=kwargs.get("market_ids")
            )
        elif msg_type == "BatchCreateDerivativeLimitOrdersAuthz":
            auth = injective_authz_pb.BatchCreateDerivativeLimitOrdersAuthz(
                subaccount_id=subaccount_id, market_ids=kwargs.get("market_ids")
            )
        elif msg_type == "CancelDerivativeOrderAuthz":
            auth = injective_authz_pb.CancelDerivativeOrderAuthz(
                subaccount_id=subaccount_id, market_ids=kwargs.get("market_ids")
            )
        elif msg_type == "BatchCancelDerivativeOrdersAuthz":
            auth = injective_authz_pb.BatchCancelDerivativeOrdersAuthz(
                subaccount_id=subaccount_id, market_ids=kwargs.get("market_ids")
            )
        elif msg_type == "BatchUpdateOrdersAuthz":
            auth = injective_authz_pb.BatchUpdateOrdersAuthz(
                subaccount_id=subaccount_id,
                spot_markets=kwargs.get("spot_markets"),
                derivative_markets=kwargs.get("derivative_markets"),
            )

        any_auth = any_pb2.Any()
        any_auth.Pack(auth, type_url_prefix="")

        grant = cosmos_authz_pb.Grant(
            authorization=any_auth,
            expiration=timestamp_pb2.Timestamp(seconds=(int(time()) + expire_in)),
        )

        return cosmos_authz_tx_pb.MsgGrant(
            granter=granter, grantee=grantee, grant=grant
        )

    def MsgExec(self, grantee: str, msgs: List):
        any_msgs: List[any_pb2.Any] = []
        for msg in msgs:
            any_msg = any_pb2.Any()
            any_msg.Pack(msg, type_url_prefix="")
            any_msgs.append(any_msg)

        return cosmos_authz_tx_pb.MsgExec(grantee=grantee, msgs=any_msgs)

    def MsgRevoke(self, granter: str, grantee: str, msg_type: str):
        return cosmos_authz_tx_pb.MsgRevoke(
            granter=granter, grantee=grantee, msg_type_url=msg_type
        )

    def MsgRelayPriceFeedPrice(
        self, sender: list, base: list, quote: list, price: list
    ):

        return injective_oracle_tx_pb.MsgRelayPriceFeedPrice(
            sender=sender, base=base, quote=quote, price=price
        )

    def MsgSendToEth(
        self, denom: str, sender: str, eth_dest: str, amount: float, bridge_fee: float
    ):

        peggy_denom, decimals = Denom.load_peggy_denom(self.network, denom)
        be_amount = amount_to_backend(amount, decimals)
        be_bridge_fee = amount_to_backend(bridge_fee, decimals)
        logging.info(
            "Loaded withdrawal symbol {} ({}) with decimals = {}".format(
                denom, peggy_denom, decimals
            )
        )

        return injective_peggy_tx_pb.MsgSendToEth(
            sender=sender,
            eth_dest=eth_dest,
            amount=self.Coin(amount=be_amount, denom=peggy_denom),
            bridge_fee=self.Coin(amount=be_bridge_fee, denom=peggy_denom),
        )

    def MsgDelegate(
        self, delegator_address: str, validator_address: str, amount: float
    ):

        be_amount = amount_to_backend(amount, 18)

        return cosmos_staking_tx_pb.MsgDelegate(
            delegator_address=delegator_address,
            validator_address=validator_address,
            amount=self.Coin(amount=be_amount, denom="inj"),
        )

    def MsgWithdrawDelegatorReward(
        self, delegator_address: str, validator_address: str
    ):

        return cosmos_distribution_tx_pb.MsgWithdrawDelegatorReward(
            delegator_address=delegator_address, validator_address=validator_address
        )

    def MsgVote(
        self,
        proposal_id: str,
        voter: str,
        option: int,
    ):

        return cosmos_gov_tx_pb.MsgVote(
            proposal_id=proposal_id, voter=voter, option=option
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
            "/injective.exchange.v1beta1.MsgBatchUpdateOrders": injective_exchange_tx_pb.MsgBatchUpdateOrdersResponse,
            "/injective.exchange.v1beta1.MsgDeposit": injective_exchange_tx_pb.MsgDepositResponse,
            "/injective.exchange.v1beta1.MsgWithdraw": injective_exchange_tx_pb.MsgWithdrawResponse,
            "/injective.exchange.v1beta1.MsgSubaccountTransfer": injective_exchange_tx_pb.MsgSubaccountTransferResponse,
            "/injective.exchange.v1beta1.MsgLiquidatePosition": injective_exchange_tx_pb.MsgLiquidatePositionResponse,
            "/injective.exchange.v1beta1.MsgIncreasePositionMargin": injective_exchange_tx_pb.MsgIncreasePositionMarginResponse,
            "/injective.auction.v1beta1.MsgBid": injective_auction_tx_pb.MsgBidResponse,
            "/injective.exchange.v1beta1.MsgCreateBinaryOptionsLimitOrder": injective_exchange_tx_pb.MsgCreateBinaryOptionsLimitOrderResponse,
            "/injective.exchange.v1beta1.MsgCreateBinaryOptionsMarketOrder": injective_exchange_tx_pb.MsgCreateBinaryOptionsMarketOrderResponse,
            "/injective.exchange.v1beta1.MsgCancelBinaryOptionsOrder": injective_exchange_tx_pb.MsgCancelBinaryOptionsOrderResponse,
            "/injective.exchange.v1beta1.MsgAdminUpdateBinaryOptionsMarket": injective_exchange_tx_pb.MsgAdminUpdateBinaryOptionsMarketResponse,
            "/injective.exchange.v1beta1.MsgInstantBinaryOptionsMarketLaunch": injective_exchange_tx_pb.MsgInstantBinaryOptionsMarketLaunchResponse,
            "/cosmos.bank.v1beta1.MsgSend": cosmos_bank_tx_pb.MsgSendResponse,
            "/cosmos.authz.v1beta1.MsgGrant": cosmos_authz_tx_pb.MsgGrantResponse,
            "/cosmos.authz.v1beta1.MsgExec": cosmos_authz_tx_pb.MsgExecResponse,
            "/cosmos.authz.v1beta1.MsgRevoke": cosmos_authz_tx_pb.MsgRevokeResponse,
            "/injective.oracle.v1beta1.MsgRelayPriceFeedPrice": injective_oracle_tx_pb.MsgRelayPriceFeedPriceResponse,
            "/injective.oracle.v1beta1.MsgRelayProviderPrices": injective_oracle_tx_pb.MsgRelayProviderPrices,
        }

        response = tx_response_pb.TxResponseData.FromString(data)
        msgs = []
        for msg in response.messages:
            msgs.append(header_map[msg.header].FromString(msg.data))

        return msgs

    @staticmethod
    def UnpackMsgExecResponse(msg_type, data):
        header_map = {
            "MsgCreateSpotLimitOrder": injective_exchange_tx_pb.MsgCreateSpotLimitOrderResponse,
            "MsgCreateSpotMarketOrder": injective_exchange_tx_pb.MsgCreateSpotMarketOrderResponse,
            "MsgCreateDerivativeLimitOrder": injective_exchange_tx_pb.MsgCreateDerivativeLimitOrderResponse,
            "MsgCreateDerivativeMarketOrder": injective_exchange_tx_pb.MsgCreateDerivativeMarketOrderResponse,
            "MsgCancelSpotOrder": injective_exchange_tx_pb.MsgCancelSpotOrderResponse,
            "MsgCancelDerivativeOrder": injective_exchange_tx_pb.MsgCancelDerivativeOrderResponse,
            "MsgBatchCancelSpotOrders": injective_exchange_tx_pb.MsgBatchCancelSpotOrdersResponse,
            "MsgBatchCancelDerivativeOrders": injective_exchange_tx_pb.MsgBatchCancelDerivativeOrdersResponse,
            "MsgBatchCreateSpotLimitOrders": injective_exchange_tx_pb.MsgBatchCreateSpotLimitOrdersResponse,
            "MsgBatchCreateDerivativeLimitOrders": injective_exchange_tx_pb.MsgBatchCreateDerivativeLimitOrdersResponse,
            "MsgBatchUpdateOrders": injective_exchange_tx_pb.MsgBatchUpdateOrdersResponse,
            "MsgDeposit": injective_exchange_tx_pb.MsgDepositResponse,
            "MsgWithdraw": injective_exchange_tx_pb.MsgWithdrawResponse,
            "MsgSubaccountTransfer": injective_exchange_tx_pb.MsgSubaccountTransferResponse,
            "MsgLiquidatePosition": injective_exchange_tx_pb.MsgLiquidatePositionResponse,
            "MsgIncreasePositionMargin": injective_exchange_tx_pb.MsgIncreasePositionMarginResponse,
            "MsgCreateBinaryOptionsLimitOrder": injective_exchange_tx_pb.MsgCreateBinaryOptionsLimitOrderResponse,
            "MsgCreateBinaryOptionsMarketOrder": injective_exchange_tx_pb.MsgCreateBinaryOptionsMarketOrderResponse,
            "MsgCancelBinaryOptionsOrder": injective_exchange_tx_pb.MsgCancelBinaryOptionsOrderResponse,
            "MsgAdminUpdateBinaryOptionsMarket": injective_exchange_tx_pb.MsgAdminUpdateBinaryOptionsMarketResponse,
            "MsgInstantBinaryOptionsMarketLaunch": injective_exchange_tx_pb.MsgInstantBinaryOptionsMarketLaunchResponse,
        }

        return header_map[msg_type].FromString(bytes(data, "utf-8"))
