import json
from configparser import ConfigParser
from decimal import Decimal
from time import time
from typing import Dict, List, Optional

from google.protobuf import any_pb2, json_format, timestamp_pb2

from pyinjective import constant
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from pyinjective.proto.injective.exchange.v1beta1 import (
    exchange_pb2 as injective_dot_exchange_dot_v1beta1_dot_exchange__pb2,
)

from .constant import ADDITIONAL_CHAIN_FORMAT_DECIMALS, INJ_DENOM
from .core.market import BinaryOptionMarket, DerivativeMarket, SpotMarket
from .core.token import Token
from .proto.cosmos.authz.v1beta1 import authz_pb2 as cosmos_authz_pb
from .proto.cosmos.authz.v1beta1 import tx_pb2 as cosmos_authz_tx_pb
from .proto.cosmos.bank.v1beta1 import tx_pb2 as cosmos_bank_tx_pb
from .proto.cosmos.distribution.v1beta1 import tx_pb2 as cosmos_distribution_tx_pb
from .proto.cosmos.gov.v1beta1 import tx_pb2 as cosmos_gov_tx_pb
from .proto.cosmos.staking.v1beta1 import tx_pb2 as cosmos_staking_tx_pb
from .proto.cosmwasm.wasm.v1 import tx_pb2 as wasm_tx_pb
from .proto.injective.auction.v1beta1 import tx_pb2 as injective_auction_tx_pb
from .proto.injective.exchange.v1beta1 import authz_pb2 as injective_authz_pb
from .proto.injective.exchange.v1beta1 import tx_pb2 as injective_exchange_tx_pb
from .proto.injective.insurance.v1beta1 import tx_pb2 as injective_insurance_tx_pb
from .proto.injective.oracle.v1beta1 import tx_pb2 as injective_oracle_tx_pb
from .proto.injective.peggy.v1 import msgs_pb2 as injective_peggy_tx_pb


class Composer:
    def __init__(
        self,
        network: str,
        spot_markets: Optional[Dict[str, SpotMarket]] = None,
        derivative_markets: Optional[Dict[str, DerivativeMarket]] = None,
        binary_option_markets: Optional[Dict[str, BinaryOptionMarket]] = None,
        tokens: Optional[Dict[str, Token]] = None,
    ):
        """Composer is used to create the requests to send to the nodes using the Client

        :param network: the name of the network to use (mainnet, testnet, devnet)
        :type network: str

        :param spot_markets: a dictionary containing all spot markets
        :type spot_markets: Dictionary

        :param derivative_markets: a dictionary containing all derivative markets
        :type derivative_markets: Dictionary

        :param binary_option_markets: a dictionary containing all derivative markets
        :type binary_option_markets: Dictionary

        :param tokens: a dictionary with all the possible tokens
        :type tokens: Dictionary


        """
        self.network = network
        self.spot_markets = dict()
        self.derivative_markets = dict()
        self.binary_option_markets = dict()
        self.tokens = dict()
        if spot_markets is None or derivative_markets is None or binary_option_markets is None or tokens is None:
            self._initialize_markets_and_tokens_from_files()
        else:
            self.spot_markets = spot_markets
            self.derivative_markets = derivative_markets
            self.binary_option_markets = binary_option_markets
            self.tokens = tokens

    def Coin(self, amount: int, denom: str):
        return cosmos_dot_base_dot_v1beta1_dot_coin__pb2.Coin(amount=str(amount), denom=denom)

    def get_order_mask(self, **kwargs):
        order_mask = 0

        if kwargs.get("is_conditional"):
            order_mask += injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.OrderMask.CONDITIONAL
        else:
            order_mask += injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.OrderMask.REGULAR

        if kwargs.get("order_direction") == "buy":
            order_mask += injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.OrderMask.DIRECTION_BUY_OR_HIGHER

        elif kwargs.get("order_direction") == "sell":
            order_mask += injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.OrderMask.DIRECTION_SELL_OR_LOWER

        if kwargs.get("order_type") == "market":
            order_mask += injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.OrderMask.TYPE_MARKET

        elif kwargs.get("order_type") == "limit":
            order_mask += injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.OrderMask.TYPE_LIMIT

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
        market = self.spot_markets[market_id]

        # prepare values
        quantity = market.quantity_to_chain_format(human_readable_value=Decimal(str(quantity)))
        price = market.price_to_chain_format(human_readable_value=Decimal(str(price)))
        trigger_price = market.price_to_chain_format(human_readable_value=Decimal(0))

        if kwargs.get("is_buy") and not kwargs.get("is_po"):
            order_type = injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.OrderType.BUY

        elif not kwargs.get("is_buy") and not kwargs.get("is_po"):
            order_type = injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.OrderType.SELL

        elif kwargs.get("is_buy") and kwargs.get("is_po"):
            order_type = injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.OrderType.BUY_PO

        elif not kwargs.get("is_buy") and kwargs.get("is_po"):
            order_type = injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.OrderType.SELL_PO

        return injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.SpotOrder(
            market_id=market_id,
            order_info=injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.OrderInfo(
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=str(int(price)),
                quantity=str(int(quantity)),
            ),
            order_type=order_type,
            trigger_price=str(int(trigger_price)),
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
        market = self.derivative_markets[market_id]

        if kwargs.get("is_reduce_only", False):
            margin = 0
        else:
            margin = market.calculate_margin_in_chain_format(
                human_readable_quantity=Decimal(str(quantity)),
                human_readable_price=Decimal(str(price)),
                leverage=Decimal(str(kwargs["leverage"])),
            )

        # prepare values
        quantity = market.quantity_to_chain_format(human_readable_value=Decimal(str(quantity)))
        price = market.price_to_chain_format(human_readable_value=Decimal(str(price)))
        trigger_price = market.price_to_chain_format(human_readable_value=Decimal(str(trigger_price)))

        if kwargs.get("is_buy") and not kwargs.get("is_po"):
            order_type = injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.OrderType.BUY

        elif not kwargs.get("is_buy") and not kwargs.get("is_po"):
            order_type = injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.OrderType.SELL

        elif kwargs.get("is_buy") and kwargs.get("is_po"):
            order_type = injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.OrderType.BUY_PO

        elif not kwargs.get("is_buy") and kwargs.get("is_po"):
            order_type = injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.OrderType.SELL_PO

        elif kwargs.get("stop_buy"):
            order_type = injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.OrderType.STOP_BUY

        elif kwargs.get("stop_sell"):
            order_type = injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.OrderType.STOP_SEll

        elif kwargs.get("take_buy"):
            order_type = injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.OrderType.TAKE_BUY

        elif kwargs.get("take_sell"):
            order_type = injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.OrderType.TAKE_SELL

        return injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.DerivativeOrder(
            market_id=market_id,
            order_info=injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.OrderInfo(
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=str(int(price)),
                quantity=str(int(quantity)),
            ),
            margin=str(int(margin)),
            order_type=order_type,
            trigger_price=str(int(trigger_price)),
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
        market = self.binary_option_markets[market_id]
        denom = kwargs.get("denom", None)

        if kwargs.get("is_reduce_only", False):
            margin = 0
        else:
            margin = market.calculate_margin_in_chain_format(
                human_readable_quantity=Decimal(str(quantity)),
                human_readable_price=Decimal(str(price)),
                is_buy=kwargs["is_buy"],
                special_denom=denom,
            )

        # prepare values
        price = market.price_to_chain_format(human_readable_value=Decimal(str(price)), special_denom=denom)
        trigger_price = market.price_to_chain_format(human_readable_value=Decimal(str(0)), special_denom=denom)
        quantity = market.quantity_to_chain_format(human_readable_value=Decimal(str(quantity)), special_denom=denom)

        if kwargs.get("is_buy") and not kwargs.get("is_po"):
            order_type = injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.OrderType.BUY

        elif not kwargs.get("is_buy") and not kwargs.get("is_po"):
            order_type = injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.OrderType.SELL

        elif kwargs.get("is_buy") and kwargs.get("is_po"):
            order_type = injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.OrderType.BUY_PO

        elif not kwargs.get("is_buy") and kwargs.get("is_po"):
            order_type = injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.OrderType.SELL_PO

        return injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.DerivativeOrder(
            market_id=market_id,
            order_info=injective_dot_exchange_dot_v1beta1_dot_exchange__pb2.OrderInfo(
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=str(int(price)),
                quantity=str(int(quantity)),
            ),
            margin=str(int(margin)),
            order_type=order_type,
            trigger_price=str(int(trigger_price)),
        )

    def MsgSend(self, from_address: str, to_address: str, amount: float, denom: str):
        token = self.tokens[denom]
        be_amount = token.chain_formatted_value(human_readable_value=Decimal(str(amount)))

        return cosmos_bank_tx_pb.MsgSend(
            from_address=from_address,
            to_address=to_address,
            amount=[self.Coin(amount=int(be_amount), denom=token.denom)],
        )

    def MsgExecuteContract(self, sender: str, contract: str, msg: str, **kwargs):
        return wasm_tx_pb.MsgExecuteContract(
            sender=sender,
            contract=contract,
            msg=bytes(msg, "utf-8"),
            funds=kwargs.get("funds")  # funds is a list of cosmos_dot_base_dot_v1beta1_dot_coin__pb2.Coin.
            # The coins in the list must be sorted in alphabetical order by denoms.
        )

    def MsgDeposit(self, sender: str, subaccount_id: str, amount: float, denom: str):
        token = self.tokens[denom]
        be_amount = token.chain_formatted_value(human_readable_value=Decimal(str(amount)))

        return injective_exchange_tx_pb.MsgDeposit(
            sender=sender,
            subaccount_id=subaccount_id,
            amount=self.Coin(amount=int(be_amount), denom=token.denom),
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

    def MsgCancelSpotOrder(self, market_id: str, sender: str, subaccount_id: str, order_hash: str):
        return injective_exchange_tx_pb.MsgCancelSpotOrder(
            sender=sender,
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hash=order_hash,
        )

    def MsgBatchCreateSpotLimitOrders(self, sender: str, orders: List):
        return injective_exchange_tx_pb.MsgBatchCreateSpotLimitOrders(sender=sender, orders=orders)

    def MsgBatchCancelSpotOrders(self, sender: str, data: List):
        return injective_exchange_tx_pb.MsgBatchCancelSpotOrders(sender=sender, data=data)

    def MsgRewardsOptOut(self, sender: str):
        return injective_exchange_tx_pb.MsgRewardsOptOut(sender=sender)

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

    def MsgCancelBinaryOptionsOrder(self, sender: str, market_id: str, subaccount_id: str, order_hash: str):
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

    def MsgRelayProviderPrices(self, sender: str, provider: str, symbols: list, prices: list):
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

        scaled_min_price_tick_size = Decimal((min_price_tick_size * pow(10, quote_decimals + 18)))
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

    def MsgCancelDerivativeOrder(self, market_id: str, sender: str, subaccount_id: str, order_hash: str, **kwargs):
        order_mask = self.get_order_mask(**kwargs)

        return injective_exchange_tx_pb.MsgCancelDerivativeOrder(
            sender=sender,
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hash=order_hash,
            order_mask=order_mask,
        )

    def MsgBatchCreateDerivativeLimitOrders(self, sender: str, orders: List):
        return injective_exchange_tx_pb.MsgBatchCreateDerivativeLimitOrders(sender=sender, orders=orders)

    def MsgBatchCancelDerivativeOrders(self, sender: str, data: List):
        return injective_exchange_tx_pb.MsgBatchCancelDerivativeOrders(sender=sender, data=data)

    def MsgBatchUpdateOrders(self, sender: str, **kwargs):
        return injective_exchange_tx_pb.MsgBatchUpdateOrders(
            sender=sender,
            subaccount_id=kwargs.get("subaccount_id"),
            spot_market_ids_to_cancel_all=kwargs.get("spot_market_ids_to_cancel_all"),
            derivative_market_ids_to_cancel_all=kwargs.get("derivative_market_ids_to_cancel_all"),
            spot_orders_to_cancel=kwargs.get("spot_orders_to_cancel"),
            derivative_orders_to_cancel=kwargs.get("derivative_orders_to_cancel"),
            spot_orders_to_create=kwargs.get("spot_orders_to_create"),
            derivative_orders_to_create=kwargs.get("derivative_orders_to_create"),
            binary_options_orders_to_cancel=kwargs.get("binary_options_orders_to_cancel"),
            binary_options_market_ids_to_cancel_all=kwargs.get("binary_options_market_ids_to_cancel_all"),
            binary_options_orders_to_create=kwargs.get("binary_options_orders_to_create"),
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
        market = self.derivative_markets[market_id]

        additional_margin = market.margin_to_chain_format(human_readable_value=Decimal(str(amount)))
        return injective_exchange_tx_pb.MsgIncreasePositionMargin(
            sender=sender,
            source_subaccount_id=source_subaccount_id,
            destination_subaccount_id=destination_subaccount_id,
            market_id=market_id,
            amount=str(int(additional_margin)),
        )

    def MsgSubaccountTransfer(
        self,
        sender: str,
        source_subaccount_id: str,
        destination_subaccount_id: str,
        amount: int,
        denom: str,
    ):
        token = self.tokens[denom]
        be_amount = token.chain_formatted_value(human_readable_value=Decimal(str(amount)))

        return injective_exchange_tx_pb.MsgSubaccountTransfer(
            sender=sender,
            source_subaccount_id=source_subaccount_id,
            destination_subaccount_id=destination_subaccount_id,
            amount=self.Coin(amount=int(be_amount), denom=token.denom),
        )

    def MsgWithdraw(self, sender: str, subaccount_id: str, amount: float, denom: str):
        token = self.tokens[denom]
        be_amount = token.chain_formatted_value(human_readable_value=Decimal(str(amount)))

        return injective_exchange_tx_pb.MsgWithdraw(
            sender=sender,
            subaccount_id=subaccount_id,
            amount=self.Coin(amount=int(be_amount), denom=token.denom),
        )

    def MsgExternalTransfer(
        self,
        sender: str,
        source_subaccount_id: str,
        destination_subaccount_id: str,
        amount: int,
        denom: str,
    ):
        token = self.tokens[denom]
        be_amount = token.chain_formatted_value(human_readable_value=Decimal(str(amount)))

        return injective_exchange_tx_pb.MsgExternalTransfer(
            sender=sender,
            source_subaccount_id=source_subaccount_id,
            destination_subaccount_id=destination_subaccount_id,
            amount=self.Coin(amount=int(be_amount), denom=token.denom),
        )

    def MsgBid(self, sender: str, bid_amount: float, round: float):
        be_amount = Decimal(str(bid_amount)) * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        return injective_auction_tx_pb.MsgBid(
            sender=sender,
            round=round,
            bid_amount=self.Coin(amount=int(be_amount), denom=INJ_DENOM),
        )

    def MsgGrantGeneric(self, granter: str, grantee: str, msg_type: str, expire_in: int):
        auth = cosmos_authz_pb.GenericAuthorization(msg=msg_type)
        any_auth = any_pb2.Any()
        any_auth.Pack(auth, type_url_prefix="")

        grant = cosmos_authz_pb.Grant(
            authorization=any_auth,
            expiration=timestamp_pb2.Timestamp(seconds=(int(time()) + expire_in)),
        )

        return cosmos_authz_tx_pb.MsgGrant(granter=granter, grantee=grantee, grant=grant)

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

        return cosmos_authz_tx_pb.MsgGrant(granter=granter, grantee=grantee, grant=grant)

    def MsgExec(self, grantee: str, msgs: List):
        any_msgs: List[any_pb2.Any] = []
        for msg in msgs:
            any_msg = any_pb2.Any()
            any_msg.Pack(msg, type_url_prefix="")
            any_msgs.append(any_msg)

        return cosmos_authz_tx_pb.MsgExec(grantee=grantee, msgs=any_msgs)

    def MsgRevoke(self, granter: str, grantee: str, msg_type: str):
        return cosmos_authz_tx_pb.MsgRevoke(granter=granter, grantee=grantee, msg_type_url=msg_type)

    def MsgRelayPriceFeedPrice(self, sender: list, base: list, quote: list, price: list):
        return injective_oracle_tx_pb.MsgRelayPriceFeedPrice(sender=sender, base=base, quote=quote, price=price)

    def MsgSendToEth(self, denom: str, sender: str, eth_dest: str, amount: float, bridge_fee: float):
        token = self.tokens[denom]
        be_amount = token.chain_formatted_value(human_readable_value=Decimal(str(amount)))
        be_bridge_fee = token.chain_formatted_value(human_readable_value=Decimal(str(bridge_fee)))

        return injective_peggy_tx_pb.MsgSendToEth(
            sender=sender,
            eth_dest=eth_dest,
            amount=self.Coin(amount=int(be_amount), denom=token.denom),
            bridge_fee=self.Coin(amount=int(be_bridge_fee), denom=token.denom),
        )

    def MsgDelegate(self, delegator_address: str, validator_address: str, amount: float):
        be_amount = Decimal(str(amount)) * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        return cosmos_staking_tx_pb.MsgDelegate(
            delegator_address=delegator_address,
            validator_address=validator_address,
            amount=self.Coin(amount=int(be_amount), denom=INJ_DENOM),
        )

    def MsgCreateInsuranceFund(
        self,
        sender: str,
        ticker: str,
        quote_denom: str,
        oracle_base: str,
        oracle_quote: str,
        oracle_type: int,
        expiry: int,
        initial_deposit: int,
    ):
        token = self.tokens[quote_denom]
        be_amount = token.chain_formatted_value(human_readable_value=Decimal(str(initial_deposit)))

        return injective_insurance_tx_pb.MsgCreateInsuranceFund(
            sender=sender,
            ticker=ticker,
            quote_denom=token.denom,
            oracle_base=oracle_base,
            oracle_quote=oracle_quote,
            oracle_type=oracle_type,
            expiry=expiry,
            initial_deposit=self.Coin(amount=int(be_amount), denom=token.denom),
        )

    def MsgUnderwrite(
        self,
        sender: str,
        market_id: str,
        quote_denom: str,
        amount: int,
    ):
        token = self.tokens[quote_denom]
        be_amount = token.chain_formatted_value(human_readable_value=Decimal(str(amount)))

        return injective_insurance_tx_pb.MsgUnderwrite(
            sender=sender,
            market_id=market_id,
            deposit=self.Coin(amount=int(be_amount), denom=token.denom),
        )

    def MsgRequestRedemption(
        self,
        sender: str,
        market_id: str,
        share_denom: str,
        amount: int,
    ):
        return injective_insurance_tx_pb.MsgRequestRedemption(
            sender=sender,
            market_id=market_id,
            amount=self.Coin(amount=amount, denom=share_denom),
        )

    def MsgWithdrawDelegatorReward(self, delegator_address: str, validator_address: str):
        return cosmos_distribution_tx_pb.MsgWithdrawDelegatorReward(
            delegator_address=delegator_address, validator_address=validator_address
        )

    def MsgWithdrawValidatorCommission(self, validator_address: str):
        return cosmos_distribution_tx_pb.MsgWithdrawValidatorCommission(validator_address=validator_address)

    def MsgVote(
        self,
        proposal_id: str,
        voter: str,
        option: int,
    ):
        return cosmos_gov_tx_pb.MsgVote(proposal_id=proposal_id, voter=voter, option=option)

    def MsgPrivilegedExecuteContract(
        self, sender: str, contract: str, msg: str, **kwargs
    ) -> injective_exchange_tx_pb.MsgPrivilegedExecuteContract:
        return injective_exchange_tx_pb.MsgPrivilegedExecuteContract(
            sender=sender,
            contract_address=contract,
            data=msg,
            funds=kwargs.get("funds")  # funds is a string of Coin strings, comma separated,
            # e.g. 100000inj,20000000000usdt
        )

    def MsgInstantiateContract(
        self, sender: str, admin: str, code_id: int, label: str, message: bytes, **kwargs
    ) -> wasm_tx_pb.MsgInstantiateContract:
        return wasm_tx_pb.MsgInstantiateContract(
            sender=sender,
            admin=admin,
            code_id=code_id,
            label=label,
            msg=message,
            funds=kwargs.get("funds"),  # funds is a list of cosmos_dot_base_dot_v1beta1_dot_coin__pb2.Coin.
            # The coins in the list must be sorted in alphabetical order by denoms.
        )

    # data field format: [request-msg-header][raw-byte-msg-response]
    # you need to figure out this magic prefix number to trim request-msg-header off the data
    # this method handles only exchange responses
    @staticmethod
    def MsgResponses(response, simulation=False):
        data = response.result
        if not simulation:
            data = bytes.fromhex(data)
        # fmt: off
        header_map = {
            "/injective.exchange.v1beta1.MsgCreateSpotLimitOrderResponse":
                injective_exchange_tx_pb.MsgCreateSpotLimitOrderResponse,
            "/injective.exchange.v1beta1.MsgCreateSpotMarketOrderResponse":
                injective_exchange_tx_pb.MsgCreateSpotMarketOrderResponse,
            "/injective.exchange.v1beta1.MsgCreateDerivativeLimitOrderResponse":
                injective_exchange_tx_pb.MsgCreateDerivativeLimitOrderResponse,
            "/injective.exchange.v1beta1.MsgCreateDerivativeMarketOrderResponse":
                injective_exchange_tx_pb.MsgCreateDerivativeMarketOrderResponse,
            "/injective.exchange.v1beta1.MsgCancelSpotOrderResponse":
                injective_exchange_tx_pb.MsgCancelSpotOrderResponse,
            "/injective.exchange.v1beta1.MsgCancelDerivativeOrderResponse":
                injective_exchange_tx_pb.MsgCancelDerivativeOrderResponse,
            "/injective.exchange.v1beta1.MsgBatchCancelSpotOrdersResponse":
                injective_exchange_tx_pb.MsgBatchCancelSpotOrdersResponse,
            "/injective.exchange.v1beta1.MsgBatchCancelDerivativeOrdersResponse":
                injective_exchange_tx_pb.MsgBatchCancelDerivativeOrdersResponse,
            "/injective.exchange.v1beta1.MsgBatchCreateSpotLimitOrdersResponse":
                injective_exchange_tx_pb.MsgBatchCreateSpotLimitOrdersResponse,
            "/injective.exchange.v1beta1.MsgBatchCreateDerivativeLimitOrdersResponse":
                injective_exchange_tx_pb.MsgBatchCreateDerivativeLimitOrdersResponse,
            "/injective.exchange.v1beta1.MsgBatchUpdateOrdersResponse":
                injective_exchange_tx_pb.MsgBatchUpdateOrdersResponse,
            "/injective.exchange.v1beta1.MsgDepositResponse":
                injective_exchange_tx_pb.MsgDepositResponse,
            "/injective.exchange.v1beta1.MsgWithdrawResponse":
                injective_exchange_tx_pb.MsgWithdrawResponse,
            "/injective.exchange.v1beta1.MsgSubaccountTransferResponse":
                injective_exchange_tx_pb.MsgSubaccountTransferResponse,
            "/injective.exchange.v1beta1.MsgLiquidatePositionResponse":
                injective_exchange_tx_pb.MsgLiquidatePositionResponse,
            "/injective.exchange.v1beta1.MsgIncreasePositionMarginResponse":
                injective_exchange_tx_pb.MsgIncreasePositionMarginResponse,
            "/injective.auction.v1beta1.MsgBidResponse":
                injective_auction_tx_pb.MsgBidResponse,
            "/injective.exchange.v1beta1.MsgCreateBinaryOptionsLimitOrderResponse":
                injective_exchange_tx_pb.MsgCreateBinaryOptionsLimitOrderResponse,
            "/injective.exchange.v1beta1.MsgCreateBinaryOptionsMarketOrderResponse":
                injective_exchange_tx_pb.MsgCreateBinaryOptionsMarketOrderResponse,
            "/injective.exchange.v1beta1.MsgCancelBinaryOptionsOrderResponse":
                injective_exchange_tx_pb.MsgCancelBinaryOptionsOrderResponse,
            "/injective.exchange.v1beta1.MsgAdminUpdateBinaryOptionsMarketResponse":
                injective_exchange_tx_pb.MsgAdminUpdateBinaryOptionsMarketResponse,
            "/injective.exchange.v1beta1.MsgInstantBinaryOptionsMarketLaunchResponse":
                injective_exchange_tx_pb.MsgInstantBinaryOptionsMarketLaunchResponse,
            "/cosmos.bank.v1beta1.MsgSendResponse":
                cosmos_bank_tx_pb.MsgSendResponse,
            "/cosmos.authz.v1beta1.MsgGrantResponse":
                cosmos_authz_tx_pb.MsgGrantResponse,
            "/cosmos.authz.v1beta1.MsgExecResponse":
                cosmos_authz_tx_pb.MsgExecResponse,
            "/cosmos.authz.v1beta1.MsgRevokeResponse":
                cosmos_authz_tx_pb.MsgRevokeResponse,
            "/injective.oracle.v1beta1.MsgRelayPriceFeedPriceResponse":
                injective_oracle_tx_pb.MsgRelayPriceFeedPriceResponse,
            "/injective.oracle.v1beta1.MsgRelayProviderPricesResponse":
                injective_oracle_tx_pb.MsgRelayProviderPrices,
        }
        # fmt: on
        msgs = []
        for msg in data.msg_responses:
            msgs.append(header_map[msg.type_url].FromString(msg.value))

        return msgs

    @staticmethod
    def UnpackMsgExecResponse(msg_type, data):
        # fmt: off
        header_map = {
            "MsgCreateSpotLimitOrder":
                injective_exchange_tx_pb.MsgCreateSpotLimitOrderResponse,
            "MsgCreateSpotMarketOrder":
                injective_exchange_tx_pb.MsgCreateSpotMarketOrderResponse,
            "MsgCreateDerivativeLimitOrder":
                injective_exchange_tx_pb.MsgCreateDerivativeLimitOrderResponse,
            "MsgCreateDerivativeMarketOrder":
                injective_exchange_tx_pb.MsgCreateDerivativeMarketOrderResponse,
            "MsgCancelSpotOrder":
                injective_exchange_tx_pb.MsgCancelSpotOrderResponse,
            "MsgCancelDerivativeOrder":
                injective_exchange_tx_pb.MsgCancelDerivativeOrderResponse,
            "MsgBatchCancelSpotOrders":
                injective_exchange_tx_pb.MsgBatchCancelSpotOrdersResponse,
            "MsgBatchCancelDerivativeOrders":
                injective_exchange_tx_pb.MsgBatchCancelDerivativeOrdersResponse,
            "MsgBatchCreateSpotLimitOrders":
                injective_exchange_tx_pb.MsgBatchCreateSpotLimitOrdersResponse,
            "MsgBatchCreateDerivativeLimitOrders":
                injective_exchange_tx_pb.MsgBatchCreateDerivativeLimitOrdersResponse,
            "MsgBatchUpdateOrders":
                injective_exchange_tx_pb.MsgBatchUpdateOrdersResponse,
            "MsgDeposit":
                injective_exchange_tx_pb.MsgDepositResponse,
            "MsgWithdraw":
                injective_exchange_tx_pb.MsgWithdrawResponse,
            "MsgSubaccountTransfer":
                injective_exchange_tx_pb.MsgSubaccountTransferResponse,
            "MsgLiquidatePosition":
                injective_exchange_tx_pb.MsgLiquidatePositionResponse,
            "MsgIncreasePositionMargin":
                injective_exchange_tx_pb.MsgIncreasePositionMarginResponse,
            "MsgCreateBinaryOptionsLimitOrder":
                injective_exchange_tx_pb.MsgCreateBinaryOptionsLimitOrderResponse,
            "MsgCreateBinaryOptionsMarketOrder":
                injective_exchange_tx_pb.MsgCreateBinaryOptionsMarketOrderResponse,
            "MsgCancelBinaryOptionsOrder":
                injective_exchange_tx_pb.MsgCancelBinaryOptionsOrderResponse,
            "MsgAdminUpdateBinaryOptionsMarket":
                injective_exchange_tx_pb.MsgAdminUpdateBinaryOptionsMarketResponse,
            "MsgInstantBinaryOptionsMarketLaunch":
                injective_exchange_tx_pb.MsgInstantBinaryOptionsMarketLaunchResponse,
        }
        # fmt: on

        responses = [header_map[msg_type].FromString(result) for result in data.results]
        return responses

    @staticmethod
    def UnpackTransactionMessages(transaction):
        meta_messages = json.loads(transaction.messages.decode())
        # fmt: off
        header_map = {
            "/injective.exchange.v1beta1.MsgCreateSpotLimitOrder":
                injective_exchange_tx_pb.MsgCreateSpotLimitOrder,
            "/injective.exchange.v1beta1.MsgCreateSpotMarketOrder":
                injective_exchange_tx_pb.MsgCreateSpotMarketOrder,
            "/injective.exchange.v1beta1.MsgCreateDerivativeLimitOrder":
                injective_exchange_tx_pb.MsgCreateDerivativeLimitOrder,
            "/injective.exchange.v1beta1.MsgCreateDerivativeMarketOrder":
                injective_exchange_tx_pb.MsgCreateDerivativeMarketOrder,
            "/injective.exchange.v1beta1.MsgCancelSpotOrder":
                injective_exchange_tx_pb.MsgCancelSpotOrder,
            "/injective.exchange.v1beta1.MsgCancelDerivativeOrder":
                injective_exchange_tx_pb.MsgCancelDerivativeOrder,
            "/injective.exchange.v1beta1.MsgBatchCancelSpotOrders":
                injective_exchange_tx_pb.MsgBatchCancelSpotOrders,
            "/injective.exchange.v1beta1.MsgBatchCancelDerivativeOrders":
                injective_exchange_tx_pb.MsgBatchCancelDerivativeOrders,
            "/injective.exchange.v1beta1.MsgBatchCreateSpotLimitOrders":
                injective_exchange_tx_pb.MsgBatchCreateSpotLimitOrders,
            "/injective.exchange.v1beta1.MsgBatchCreateDerivativeLimitOrders":
                injective_exchange_tx_pb.MsgBatchCreateDerivativeLimitOrders,
            "/injective.exchange.v1beta1.MsgBatchUpdateOrders":
                injective_exchange_tx_pb.MsgBatchUpdateOrders,
            "/injective.exchange.v1beta1.MsgDeposit":
                injective_exchange_tx_pb.MsgDeposit,
            "/injective.exchange.v1beta1.MsgWithdraw":
                injective_exchange_tx_pb.MsgWithdraw,
            "/injective.exchange.v1beta1.MsgSubaccountTransfer":
                injective_exchange_tx_pb.MsgSubaccountTransfer,
            "/injective.exchange.v1beta1.MsgLiquidatePosition":
                injective_exchange_tx_pb.MsgLiquidatePosition,
            "/injective.exchange.v1beta1.MsgIncreasePositionMargin":
                injective_exchange_tx_pb.MsgIncreasePositionMargin,
            "/injective.auction.v1beta1.MsgBid":
                injective_auction_tx_pb.MsgBid,
            "/injective.exchange.v1beta1.MsgCreateBinaryOptionsLimitOrder":
                injective_exchange_tx_pb.MsgCreateBinaryOptionsLimitOrder,
            "/injective.exchange.v1beta1.MsgCreateBinaryOptionsMarketOrder":
                injective_exchange_tx_pb.MsgCreateBinaryOptionsMarketOrder,
            "/injective.exchange.v1beta1.MsgCancelBinaryOptionsOrder":
                injective_exchange_tx_pb.MsgCancelBinaryOptionsOrder,
            "/injective.exchange.v1beta1.MsgAdminUpdateBinaryOptionsMarket":
                injective_exchange_tx_pb.MsgAdminUpdateBinaryOptionsMarket,
            "/injective.exchange.v1beta1.MsgInstantBinaryOptionsMarketLaunch":
                injective_exchange_tx_pb.MsgInstantBinaryOptionsMarketLaunch,
            "/cosmos.bank.v1beta1.MsgSend":
                cosmos_bank_tx_pb.MsgSend,
            "/cosmos.authz.v1beta1.MsgGrant":
                cosmos_authz_tx_pb.MsgGrant,
            "/cosmos.authz.v1beta1.MsgExec":
                cosmos_authz_tx_pb.MsgExec,
            "/cosmos.authz.v1beta1.MsgRevoke":
                cosmos_authz_tx_pb.MsgRevoke,
            "/injective.oracle.v1beta1.MsgRelayPriceFeedPrice":
                injective_oracle_tx_pb.MsgRelayPriceFeedPrice,
            "/injective.oracle.v1beta1.MsgRelayProviderPrices":
                injective_oracle_tx_pb.MsgRelayProviderPrices,
        }
        # fmt: on
        msgs = []
        for msg in meta_messages:
            msg_as_string_dict = json.dumps(msg["value"])
            msgs.append(json_format.Parse(msg_as_string_dict, header_map[msg["type"]]()))

        return msgs

    def _initialize_markets_and_tokens_from_files(self):
        config: ConfigParser = constant.CONFIGS[self.network]
        spot_markets = dict()
        derivative_markets = dict()
        tokens = dict()

        for section_name, configuration_section in config.items():
            if section_name.startswith("0x"):
                description = configuration_section["description"]

                quote_token = Token(
                    name="",
                    symbol="",
                    denom="",
                    address="",
                    decimals=int(configuration_section["quote"]),
                    logo="",
                    updated=-1,
                )

                if "Spot" in description:
                    base_token = Token(
                        name="",
                        symbol="",
                        denom="",
                        address="",
                        decimals=int(configuration_section["base"]),
                        logo="",
                        updated=-1,
                    )

                    market = SpotMarket(
                        id=section_name,
                        status="",
                        ticker=description,
                        base_token=base_token,
                        quote_token=quote_token,
                        maker_fee_rate=None,
                        taker_fee_rate=None,
                        service_provider_fee=None,
                        min_price_tick_size=Decimal(str(configuration_section["min_price_tick_size"])),
                        min_quantity_tick_size=Decimal(str(configuration_section["min_quantity_tick_size"])),
                    )
                    spot_markets[market.id] = market
                else:
                    market = DerivativeMarket(
                        id=section_name,
                        status="",
                        ticker=description,
                        oracle_base="",
                        oracle_quote="",
                        oracle_type="",
                        oracle_scale_factor=1,
                        initial_margin_ratio=None,
                        maintenance_margin_ratio=None,
                        quote_token=quote_token,
                        maker_fee_rate=None,
                        taker_fee_rate=None,
                        service_provider_fee=None,
                        min_price_tick_size=Decimal(str(configuration_section["min_price_tick_size"])),
                        min_quantity_tick_size=Decimal(str(configuration_section["min_quantity_tick_size"])),
                    )

                    derivative_markets[market.id] = market

            elif section_name != "DEFAULT":
                token = Token(
                    name=section_name,
                    symbol=section_name,
                    denom=configuration_section["peggy_denom"],
                    address="",
                    decimals=int(configuration_section["decimals"]),
                    logo="",
                    updated=-1,
                )

                tokens[token.symbol] = token

        self.tokens = tokens
        self.spot_markets = spot_markets
        self.derivative_markets = derivative_markets
        self.binary_option_markets = dict()
