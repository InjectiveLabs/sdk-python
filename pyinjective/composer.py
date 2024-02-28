import json
from configparser import ConfigParser
from decimal import Decimal
from time import time
from typing import Any, Dict, List, Optional
from warnings import warn

from google.protobuf import any_pb2, json_format, timestamp_pb2

from pyinjective import constant
from pyinjective.constant import ADDITIONAL_CHAIN_FORMAT_DECIMALS, INJ_DENOM
from pyinjective.core.market import BinaryOptionMarket, DerivativeMarket, SpotMarket
from pyinjective.core.token import Token
from pyinjective.proto.cosmos.authz.v1beta1 import authz_pb2 as cosmos_authz_pb, tx_pb2 as cosmos_authz_tx_pb
from pyinjective.proto.cosmos.bank.v1beta1 import bank_pb2 as bank_pb, tx_pb2 as cosmos_bank_tx_pb
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as base_coin_pb
from pyinjective.proto.cosmos.distribution.v1beta1 import (
    distribution_pb2 as cosmos_distribution_pb2,
    tx_pb2 as cosmos_distribution_tx_pb,
)
from pyinjective.proto.cosmos.gov.v1beta1 import tx_pb2 as cosmos_gov_tx_pb
from pyinjective.proto.cosmos.staking.v1beta1 import tx_pb2 as cosmos_staking_tx_pb
from pyinjective.proto.cosmwasm.wasm.v1 import tx_pb2 as wasm_tx_pb
from pyinjective.proto.exchange import injective_explorer_rpc_pb2 as explorer_pb2
from pyinjective.proto.injective.auction.v1beta1 import tx_pb2 as injective_auction_tx_pb
from pyinjective.proto.injective.exchange.v1beta1 import (
    authz_pb2 as injective_authz_pb,
    exchange_pb2 as injective_exchange_pb,
    tx_pb2 as injective_exchange_tx_pb,
)
from pyinjective.proto.injective.insurance.v1beta1 import tx_pb2 as injective_insurance_tx_pb
from pyinjective.proto.injective.oracle.v1beta1 import (
    oracle_pb2 as injective_oracle_pb,
    tx_pb2 as injective_oracle_tx_pb,
)
from pyinjective.proto.injective.peggy.v1 import msgs_pb2 as injective_peggy_tx_pb
from pyinjective.proto.injective.stream.v1beta1 import query_pb2 as chain_stream_query
from pyinjective.proto.injective.tokenfactory.v1beta1 import tx_pb2 as token_factory_tx_pb
from pyinjective.proto.injective.wasmx.v1 import tx_pb2 as wasmx_tx_pb
from pyinjective.utils.denom import Denom

REQUEST_TO_RESPONSE_TYPE_MAP = {
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

GRPC_MESSAGE_TYPE_TO_CLASS_MAP = {
    "/injective.exchange.v1beta1.MsgCreateSpotLimitOrder": injective_exchange_tx_pb.MsgCreateSpotLimitOrder,
    "/injective.exchange.v1beta1.MsgCreateSpotMarketOrder": injective_exchange_tx_pb.MsgCreateSpotMarketOrder,
    "/injective.exchange.v1beta1.MsgCreateDerivativeLimitOrder": injective_exchange_tx_pb.MsgCreateDerivativeLimitOrder,
    "/injective.exchange.v1beta1.MsgCreateDerivativeMarketOrder": injective_exchange_tx_pb.MsgCreateDerivativeMarketOrder,  # noqa: 121
    "/injective.exchange.v1beta1.MsgCancelSpotOrder": injective_exchange_tx_pb.MsgCancelSpotOrder,
    "/injective.exchange.v1beta1.MsgCancelDerivativeOrder": injective_exchange_tx_pb.MsgCancelDerivativeOrder,
    "/injective.exchange.v1beta1.MsgBatchCancelSpotOrders": injective_exchange_tx_pb.MsgBatchCancelSpotOrders,
    "/injective.exchange.v1beta1.MsgBatchCancelDerivativeOrders": injective_exchange_tx_pb.MsgBatchCancelDerivativeOrders,  # noqa: 121
    "/injective.exchange.v1beta1.MsgBatchCreateSpotLimitOrders": injective_exchange_tx_pb.MsgBatchCreateSpotLimitOrders,
    "/injective.exchange.v1beta1.MsgBatchCreateDerivativeLimitOrders": injective_exchange_tx_pb.MsgBatchCreateDerivativeLimitOrders,  # noqa: 121
    "/injective.exchange.v1beta1.MsgBatchUpdateOrders": injective_exchange_tx_pb.MsgBatchUpdateOrders,
    "/injective.exchange.v1beta1.MsgDeposit": injective_exchange_tx_pb.MsgDeposit,
    "/injective.exchange.v1beta1.MsgWithdraw": injective_exchange_tx_pb.MsgWithdraw,
    "/injective.exchange.v1beta1.MsgSubaccountTransfer": injective_exchange_tx_pb.MsgSubaccountTransfer,
    "/injective.exchange.v1beta1.MsgLiquidatePosition": injective_exchange_tx_pb.MsgLiquidatePosition,
    "/injective.exchange.v1beta1.MsgIncreasePositionMargin": injective_exchange_tx_pb.MsgIncreasePositionMargin,
    "/injective.auction.v1beta1.MsgBid": injective_auction_tx_pb.MsgBid,
    "/injective.exchange.v1beta1.MsgCreateBinaryOptionsLimitOrder": injective_exchange_tx_pb.MsgCreateBinaryOptionsLimitOrder,  # noqa: 121
    "/injective.exchange.v1beta1.MsgCreateBinaryOptionsMarketOrder": injective_exchange_tx_pb.MsgCreateBinaryOptionsMarketOrder,  # noqa: 121
    "/injective.exchange.v1beta1.MsgCancelBinaryOptionsOrder": injective_exchange_tx_pb.MsgCancelBinaryOptionsOrder,
    "/injective.exchange.v1beta1.MsgAdminUpdateBinaryOptionsMarket": injective_exchange_tx_pb.MsgAdminUpdateBinaryOptionsMarket,  # noqa: 121
    "/injective.exchange.v1beta1.MsgInstantBinaryOptionsMarketLaunch": injective_exchange_tx_pb.MsgInstantBinaryOptionsMarketLaunch,  # noqa: 121
    "/cosmos.bank.v1beta1.MsgSend": cosmos_bank_tx_pb.MsgSend,
    "/cosmos.authz.v1beta1.MsgGrant": cosmos_authz_tx_pb.MsgGrant,
    "/cosmos.authz.v1beta1.MsgExec": cosmos_authz_tx_pb.MsgExec,
    "/cosmos.authz.v1beta1.MsgRevoke": cosmos_authz_tx_pb.MsgRevoke,
    "/injective.oracle.v1beta1.MsgRelayPriceFeedPrice": injective_oracle_tx_pb.MsgRelayPriceFeedPrice,
    "/injective.oracle.v1beta1.MsgRelayProviderPrices": injective_oracle_tx_pb.MsgRelayProviderPrices,
}


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
        """
        This method is deprecated and will be removed soon. Please use `coin` instead
        """
        warn("This method is deprecated. Use coin instead", DeprecationWarning, stacklevel=2)
        return base_coin_pb.Coin(amount=str(amount), denom=denom)

    def coin(self, amount: int, denom: str):
        """
        This method create an instance of Coin gRPC type, considering the amount is already expressed in chain format
        """
        formatted_amount_string = str(int(amount))
        return base_coin_pb.Coin(amount=formatted_amount_string, denom=denom)

    def create_coin_amount(self, amount: Decimal, token_name: str):
        """
        This method create an instance of Coin gRPC type, considering the amount is already expressed in chain format
        """
        token = self.tokens[token_name]
        chain_amount = token.chain_formatted_value(human_readable_value=amount)
        return self.coin(amount=int(chain_amount), denom=token.denom)

    def OrderData(
        self, market_id: str, subaccount_id: str, order_hash: Optional[str] = None, cid: Optional[str] = None, **kwargs
    ):
        """
        This method is deprecated and will be removed soon. Please use `order_data` instead
        """
        warn("This method is deprecated. Use order_data instead", DeprecationWarning, stacklevel=2)

        is_conditional = kwargs.get("is_conditional", False)
        is_buy = kwargs.get("order_direction", "buy") == "buy"
        is_market_order = kwargs.get("order_type", "limit") == "market"
        order_mask = self._order_mask(is_conditional=is_conditional, is_buy=is_buy, is_market_order=is_market_order)

        return injective_exchange_tx_pb.OrderData(
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hash=order_hash,
            order_mask=order_mask,
            cid=cid,
        )

    def order_data(
        self,
        market_id: str,
        subaccount_id: str,
        order_hash: Optional[str] = None,
        cid: Optional[str] = None,
        is_conditional: Optional[bool] = False,
        is_buy: Optional[bool] = False,
        is_market_order: Optional[bool] = False,
    ) -> injective_exchange_tx_pb.OrderData:
        order_mask = self._order_mask(is_conditional=is_conditional, is_buy=is_buy, is_market_order=is_market_order)

        return injective_exchange_tx_pb.OrderData(
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hash=order_hash,
            order_mask=order_mask,
            cid=cid,
        )

    def SpotOrder(
        self,
        market_id: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        cid: Optional[str] = None,
        **kwargs,
    ):
        """
        This method is deprecated and will be removed soon. Please use `spot_order` instead
        """
        warn("This method is deprecated. Use spot_order instead", DeprecationWarning, stacklevel=2)

        market = self.spot_markets[market_id]

        # prepare values
        quantity = market.quantity_to_chain_format(human_readable_value=Decimal(str(quantity)))
        price = market.price_to_chain_format(human_readable_value=Decimal(str(price)))
        trigger_price = market.price_to_chain_format(human_readable_value=Decimal(0))

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
                price=str(int(price)),
                quantity=str(int(quantity)),
                cid=cid,
            ),
            order_type=order_type,
            trigger_price=str(int(trigger_price)),
        )

    def spot_order(
        self,
        market_id: str,
        subaccount_id: str,
        fee_recipient: str,
        price: Decimal,
        quantity: Decimal,
        order_type: str,
        cid: Optional[str] = None,
        trigger_price: Optional[Decimal] = None,
    ) -> injective_exchange_pb.SpotOrder:
        market = self.spot_markets[market_id]

        chain_quantity = f"{market.quantity_to_chain_format(human_readable_value=quantity).normalize():f}"
        chain_price = f"{market.price_to_chain_format(human_readable_value=price).normalize():f}"

        trigger_price = trigger_price or Decimal(0)
        chain_trigger_price = f"{market.price_to_chain_format(human_readable_value=trigger_price).normalize():f}"

        chain_order_type = injective_exchange_pb.OrderType.Value(order_type)

        return injective_exchange_pb.SpotOrder(
            market_id=market_id,
            order_info=injective_exchange_pb.OrderInfo(
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=chain_price,
                quantity=chain_quantity,
                cid=cid,
            ),
            order_type=chain_order_type,
            trigger_price=chain_trigger_price,
        )

    def calculate_margin(
        self, quantity: Decimal, price: Decimal, leverage: Decimal, is_reduce_only: bool = False
    ) -> Decimal:
        if is_reduce_only:
            margin = Decimal(0)
        else:
            margin = quantity * price / leverage

        return margin

    def DerivativeOrder(
        self,
        market_id: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        trigger_price: float = 0,
        cid: Optional[str] = None,
        **kwargs,
    ):
        """
        This method is deprecated and will be removed soon. Please use `derivative_order` instead
        """
        warn("This method is deprecated. Use derivative_order instead", DeprecationWarning, stacklevel=2)
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
                price=str(int(price)),
                quantity=str(int(quantity)),
                cid=cid,
            ),
            margin=str(int(margin)),
            order_type=order_type,
            trigger_price=str(int(trigger_price)),
        )

    def derivative_order(
        self,
        market_id: str,
        subaccount_id: str,
        fee_recipient: str,
        price: Decimal,
        quantity: Decimal,
        margin: Decimal,
        order_type: str,
        cid: Optional[str] = None,
        trigger_price: Optional[Decimal] = None,
    ) -> injective_exchange_pb.DerivativeOrder:
        market = self.derivative_markets[market_id]

        chain_quantity = market.quantity_to_chain_format(human_readable_value=quantity)
        chain_price = market.price_to_chain_format(human_readable_value=price)
        chain_margin = market.margin_to_chain_format(human_readable_value=margin)

        trigger_price = trigger_price or Decimal(0)
        chain_trigger_price = market.price_to_chain_format(human_readable_value=trigger_price)

        return self._basic_derivative_order(
            market_id=market.id,
            subaccount_id=subaccount_id,
            fee_recipient=fee_recipient,
            chain_price=chain_price,
            chain_quantity=chain_quantity,
            chain_margin=chain_margin,
            order_type=order_type,
            cid=cid,
            chain_trigger_price=chain_trigger_price,
        )

    def binary_options_order(
        self,
        market_id: str,
        subaccount_id: str,
        fee_recipient: str,
        price: Decimal,
        quantity: Decimal,
        margin: Decimal,
        order_type: str,
        cid: Optional[str] = None,
        trigger_price: Optional[Decimal] = None,
        denom: Optional[Denom] = None,
    ) -> injective_exchange_pb.DerivativeOrder:
        market = self.binary_option_markets[market_id]

        chain_quantity = market.quantity_to_chain_format(human_readable_value=quantity, special_denom=denom)
        chain_price = market.price_to_chain_format(human_readable_value=price, special_denom=denom)
        chain_margin = market.margin_to_chain_format(human_readable_value=margin, special_denom=denom)

        trigger_price = trigger_price or Decimal(0)
        chain_trigger_price = market.price_to_chain_format(human_readable_value=trigger_price, special_denom=denom)

        return self._basic_derivative_order(
            market_id=market.id,
            subaccount_id=subaccount_id,
            fee_recipient=fee_recipient,
            chain_price=chain_price,
            chain_quantity=chain_quantity,
            chain_margin=chain_margin,
            order_type=order_type,
            cid=cid,
            chain_trigger_price=chain_trigger_price,
        )

    # region Auction module
    def MsgBid(self, sender: str, bid_amount: float, round: float):
        be_amount = Decimal(str(bid_amount)) * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        return injective_auction_tx_pb.MsgBid(
            sender=sender,
            round=round,
            bid_amount=self.coin(amount=int(be_amount), denom=INJ_DENOM),
        )

    # endregion

    # region Authz module
    def MsgGrantGeneric(self, granter: str, grantee: str, msg_type: str, expire_in: int):
        auth = cosmos_authz_pb.GenericAuthorization(msg=msg_type)
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

    def msg_execute_contract_compat(self, sender: str, contract: str, msg: str, funds: str):
        return wasmx_tx_pb.MsgExecuteContractCompat(
            sender=sender,
            contract=contract,
            msg=msg,
            funds=funds,
        )

    # endregion

    # region Bank module
    def MsgSend(self, from_address: str, to_address: str, amount: float, denom: str):
        coin = self.create_coin_amount(amount=Decimal(str(amount)), token_name=denom)

        return cosmos_bank_tx_pb.MsgSend(
            from_address=from_address,
            to_address=to_address,
            amount=[coin],
        )

    # endregion

    # region Chain Exchange module
    def MsgDeposit(self, sender: str, subaccount_id: str, amount: float, denom: str):
        """
        This method is deprecated and will be removed soon. Please use `msg_deposit` instead
        """
        warn("This method is deprecated. Use msg_deposit instead", DeprecationWarning, stacklevel=2)
        coin = self.create_coin_amount(amount=Decimal(str(amount)), token_name=denom)

        return injective_exchange_tx_pb.MsgDeposit(
            sender=sender,
            subaccount_id=subaccount_id,
            amount=coin,
        )

    def msg_deposit(self, sender: str, subaccount_id: str, amount: Decimal, denom: str):
        coin = self.create_coin_amount(amount=amount, token_name=denom)

        return injective_exchange_tx_pb.MsgDeposit(
            sender=sender,
            subaccount_id=subaccount_id,
            amount=coin,
        )

    def MsgWithdraw(self, sender: str, subaccount_id: str, amount: float, denom: str):
        """
        This method is deprecated and will be removed soon. Please use `msg_withdraw` instead
        """
        warn("This method is deprecated. Use msg_withdraw instead", DeprecationWarning, stacklevel=2)
        be_amount = self.create_coin_amount(amount=Decimal(str(amount)), token_name=denom)

        return injective_exchange_tx_pb.MsgWithdraw(
            sender=sender,
            subaccount_id=subaccount_id,
            amount=be_amount,
        )

    def msg_withdraw(self, sender: str, subaccount_id: str, amount: Decimal, denom: str):
        be_amount = self.create_coin_amount(amount=amount, token_name=denom)

        return injective_exchange_tx_pb.MsgWithdraw(
            sender=sender,
            subaccount_id=subaccount_id,
            amount=be_amount,
        )

    def msg_instant_spot_market_launch(
        self,
        sender: str,
        ticker: str,
        base_denom: str,
        quote_denom: str,
        min_price_tick_size: Decimal,
        min_quantity_tick_size: Decimal,
    ) -> injective_exchange_tx_pb.MsgInstantSpotMarketLaunch:
        base_token = self.tokens[base_denom]
        quote_token = self.tokens[quote_denom]

        chain_min_price_tick_size = min_price_tick_size * Decimal(
            f"1e{quote_token.decimals - base_token.decimals + ADDITIONAL_CHAIN_FORMAT_DECIMALS}"
        )
        chain_min_quantity_tick_size = min_quantity_tick_size * Decimal(
            f"1e{base_token.decimals + ADDITIONAL_CHAIN_FORMAT_DECIMALS}"
        )

        return injective_exchange_tx_pb.MsgInstantSpotMarketLaunch(
            sender=sender,
            ticker=ticker,
            base_denom=base_token.denom,
            quote_denom=quote_token.denom,
            min_price_tick_size=f"{chain_min_price_tick_size.normalize():f}",
            min_quantity_tick_size=f"{chain_min_quantity_tick_size.normalize():f}",
        )

    def msg_instant_perpetual_market_launch(
        self,
        sender: str,
        ticker: str,
        quote_denom: str,
        oracle_base: str,
        oracle_quote: str,
        oracle_scale_factor: int,
        oracle_type: str,
        maker_fee_rate: Decimal,
        taker_fee_rate: Decimal,
        initial_margin_ratio: Decimal,
        maintenance_margin_ratio: Decimal,
        min_price_tick_size: Decimal,
        min_quantity_tick_size: Decimal,
    ) -> injective_exchange_tx_pb.MsgInstantPerpetualMarketLaunch:
        quote_token = self.tokens[quote_denom]

        chain_min_price_tick_size = min_price_tick_size * Decimal(
            f"1e{quote_token.decimals + ADDITIONAL_CHAIN_FORMAT_DECIMALS}"
        )
        chain_min_quantity_tick_size = min_quantity_tick_size * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        chain_maker_fee_rate = maker_fee_rate * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        chain_taker_fee_rate = taker_fee_rate * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        chain_initial_margin_ratio = initial_margin_ratio * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        chain_maintenance_margin_ratio = maintenance_margin_ratio * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        return injective_exchange_tx_pb.MsgInstantPerpetualMarketLaunch(
            sender=sender,
            ticker=ticker,
            quote_denom=quote_token.denom,
            oracle_base=oracle_base,
            oracle_quote=oracle_quote,
            oracle_scale_factor=oracle_scale_factor,
            oracle_type=injective_oracle_pb.OracleType.Value(oracle_type),
            maker_fee_rate=f"{chain_maker_fee_rate.normalize():f}",
            taker_fee_rate=f"{chain_taker_fee_rate.normalize():f}",
            initial_margin_ratio=f"{chain_initial_margin_ratio.normalize():f}",
            maintenance_margin_ratio=f"{chain_maintenance_margin_ratio.normalize():f}",
            min_price_tick_size=f"{chain_min_price_tick_size.normalize():f}",
            min_quantity_tick_size=f"{chain_min_quantity_tick_size.normalize():f}",
        )

    def msg_instant_expiry_futures_market_launch(
        self,
        sender: str,
        ticker: str,
        quote_denom: str,
        oracle_base: str,
        oracle_quote: str,
        oracle_scale_factor: int,
        oracle_type: str,
        expiry: int,
        maker_fee_rate: Decimal,
        taker_fee_rate: Decimal,
        initial_margin_ratio: Decimal,
        maintenance_margin_ratio: Decimal,
        min_price_tick_size: Decimal,
        min_quantity_tick_size: Decimal,
    ) -> injective_exchange_tx_pb.MsgInstantPerpetualMarketLaunch:
        quote_token = self.tokens[quote_denom]

        chain_min_price_tick_size = min_price_tick_size * Decimal(
            f"1e{quote_token.decimals + ADDITIONAL_CHAIN_FORMAT_DECIMALS}"
        )
        chain_min_quantity_tick_size = min_quantity_tick_size * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        chain_maker_fee_rate = maker_fee_rate * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        chain_taker_fee_rate = taker_fee_rate * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        chain_initial_margin_ratio = initial_margin_ratio * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        chain_maintenance_margin_ratio = maintenance_margin_ratio * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        return injective_exchange_tx_pb.MsgInstantExpiryFuturesMarketLaunch(
            sender=sender,
            ticker=ticker,
            quote_denom=quote_token.denom,
            oracle_base=oracle_base,
            oracle_quote=oracle_quote,
            oracle_scale_factor=oracle_scale_factor,
            oracle_type=injective_oracle_pb.OracleType.Value(oracle_type),
            expiry=expiry,
            maker_fee_rate=f"{chain_maker_fee_rate.normalize():f}",
            taker_fee_rate=f"{chain_taker_fee_rate.normalize():f}",
            initial_margin_ratio=f"{chain_initial_margin_ratio.normalize():f}",
            maintenance_margin_ratio=f"{chain_maintenance_margin_ratio.normalize():f}",
            min_price_tick_size=f"{chain_min_price_tick_size.normalize():f}",
            min_quantity_tick_size=f"{chain_min_quantity_tick_size.normalize():f}",
        )

    def MsgCreateSpotLimitOrder(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        cid: Optional[str] = None,
        **kwargs,
    ):
        """
        This method is deprecated and will be removed soon. Please use `msg_create_spot_limit_order` instead
        """
        warn("This method is deprecated. Use msg_create_spot_limit_order instead", DeprecationWarning, stacklevel=2)

        order_type_name = "BUY"
        if kwargs.get("is_buy") and not kwargs.get("is_po"):
            order_type_name = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.BUY)

        elif not kwargs.get("is_buy") and not kwargs.get("is_po"):
            order_type_name = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.SELL)

        elif kwargs.get("is_buy") and kwargs.get("is_po"):
            order_type_name = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.BUY_PO)

        elif not kwargs.get("is_buy") and kwargs.get("is_po"):
            order_type_name = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.SELL_PO)

        return injective_exchange_tx_pb.MsgCreateSpotLimitOrder(
            sender=sender,
            order=self.spot_order(
                market_id=market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=Decimal(str(price)),
                quantity=Decimal(str(quantity)),
                order_type=order_type_name,
                cid=cid,
            ),
        )

    def msg_create_spot_limit_order(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: Decimal,
        quantity: Decimal,
        order_type: str,
        cid: Optional[str] = None,
        trigger_price: Optional[Decimal] = None,
    ) -> injective_exchange_tx_pb.MsgCreateSpotLimitOrder:
        return injective_exchange_tx_pb.MsgCreateSpotLimitOrder(
            sender=sender,
            order=self.spot_order(
                market_id=market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=price,
                quantity=quantity,
                order_type=order_type,
                cid=cid,
                trigger_price=trigger_price,
            ),
        )

    def MsgBatchCreateSpotLimitOrders(self, sender: str, orders: List):
        """
        This method is deprecated and will be removed soon. Please use `msg_batch_create_spot_limit_orders` instead
        """
        warn(
            "This method is deprecated. Use msg_batch_create_spot_limit_orders instead",
            DeprecationWarning,
            stacklevel=2,
        )
        return injective_exchange_tx_pb.MsgBatchCreateSpotLimitOrders(sender=sender, orders=orders)

    def msg_batch_create_spot_limit_orders(
        self, sender: str, orders: List[injective_exchange_pb.SpotOrder]
    ) -> injective_exchange_tx_pb.MsgBatchCreateSpotLimitOrders:
        return injective_exchange_tx_pb.MsgBatchCreateSpotLimitOrders(sender=sender, orders=orders)

    def MsgCreateSpotMarketOrder(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        is_buy: bool,
        cid: Optional[str] = None,
    ):
        """
        This method is deprecated and will be removed soon. Please use `msg_create_spot_market_order` instead
        """
        warn("This method is deprecated. Use msg_create_spot_market_order instead", DeprecationWarning, stacklevel=2)

        order_type_name = "BUY"
        if not is_buy:
            order_type_name = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.SELL)

        return injective_exchange_tx_pb.MsgCreateSpotMarketOrder(
            sender=sender,
            order=self.spot_order(
                market_id=market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=Decimal(str(price)),
                quantity=Decimal(str(quantity)),
                order_type=order_type_name,
                cid=cid,
            ),
        )

    def msg_create_spot_market_order(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: Decimal,
        quantity: Decimal,
        order_type: str,
        cid: Optional[str] = None,
        trigger_price: Optional[Decimal] = None,
    ) -> injective_exchange_tx_pb.MsgCreateSpotMarketOrder:
        return injective_exchange_tx_pb.MsgCreateSpotMarketOrder(
            sender=sender,
            order=self.spot_order(
                market_id=market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=price,
                quantity=quantity,
                order_type=order_type,
                cid=cid,
                trigger_price=trigger_price,
            ),
        )

    def MsgCancelSpotOrder(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        order_hash: Optional[str] = None,
        cid: Optional[str] = None,
    ):
        """
        This method is deprecated and will be removed soon. Please use `msg_cancel_spot_order` instead
        """
        warn("This method is deprecated. Use msg_cancel_spot_order instead", DeprecationWarning, stacklevel=2)
        return injective_exchange_tx_pb.MsgCancelSpotOrder(
            sender=sender,
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hash=order_hash,
            cid=cid,
        )

    def msg_cancel_spot_order(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        order_hash: Optional[str] = None,
        cid: Optional[str] = None,
    ) -> injective_exchange_tx_pb.MsgCancelSpotOrder:
        return injective_exchange_tx_pb.MsgCancelSpotOrder(
            sender=sender,
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hash=order_hash,
            cid=cid,
        )

    def MsgBatchCancelSpotOrders(self, sender: str, data: List):
        """
        This method is deprecated and will be removed soon. Please use `msg_batch_cancel_spot_orders` instead
        """
        warn("This method is deprecated. Use msg_batch_cancel_spot_orders instead", DeprecationWarning, stacklevel=2)
        return injective_exchange_tx_pb.MsgBatchCancelSpotOrders(sender=sender, data=data)

    def msg_batch_cancel_spot_orders(
        self, sender: str, orders_data: List[injective_exchange_tx_pb.OrderData]
    ) -> injective_exchange_tx_pb.MsgBatchCancelSpotOrders:
        return injective_exchange_tx_pb.MsgBatchCancelSpotOrders(sender=sender, data=orders_data)

    def MsgBatchUpdateOrders(self, sender: str, **kwargs):
        """
        This method is deprecated and will be removed soon. Please use `msg_batch_update_orders` instead
        """
        warn("This method is deprecated. Use msg_batch_update_orders instead", DeprecationWarning, stacklevel=2)
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

    def msg_batch_update_orders(
        self,
        sender: str,
        subaccount_id: Optional[str] = None,
        spot_market_ids_to_cancel_all: Optional[List[str]] = None,
        derivative_market_ids_to_cancel_all: Optional[List[str]] = None,
        spot_orders_to_cancel: Optional[List[injective_exchange_tx_pb.OrderData]] = None,
        derivative_orders_to_cancel: Optional[List[injective_exchange_tx_pb.OrderData]] = None,
        spot_orders_to_create: Optional[List[injective_exchange_pb.SpotOrder]] = None,
        derivative_orders_to_create: Optional[List[injective_exchange_pb.DerivativeOrder]] = None,
        binary_options_orders_to_cancel: Optional[List[injective_exchange_tx_pb.OrderData]] = None,
        binary_options_market_ids_to_cancel_all: Optional[List[str]] = None,
        binary_options_orders_to_create: Optional[List[injective_exchange_pb.DerivativeOrder]] = None,
    ) -> injective_exchange_tx_pb.MsgBatchUpdateOrders:
        return injective_exchange_tx_pb.MsgBatchUpdateOrders(
            sender=sender,
            subaccount_id=subaccount_id,
            spot_market_ids_to_cancel_all=spot_market_ids_to_cancel_all,
            derivative_market_ids_to_cancel_all=derivative_market_ids_to_cancel_all,
            spot_orders_to_cancel=spot_orders_to_cancel,
            derivative_orders_to_cancel=derivative_orders_to_cancel,
            spot_orders_to_create=spot_orders_to_create,
            derivative_orders_to_create=derivative_orders_to_create,
            binary_options_orders_to_cancel=binary_options_orders_to_cancel,
            binary_options_market_ids_to_cancel_all=binary_options_market_ids_to_cancel_all,
            binary_options_orders_to_create=binary_options_orders_to_create,
        )

    def MsgPrivilegedExecuteContract(
        self, sender: str, contract: str, msg: str, **kwargs
    ) -> injective_exchange_tx_pb.MsgPrivilegedExecuteContract:
        """
        This method is deprecated and will be removed soon. Please use `msg_privileged_execute_contract` instead
        """
        warn("This method is deprecated. Use msg_privileged_execute_contract instead", DeprecationWarning, stacklevel=2)

        return injective_exchange_tx_pb.MsgPrivilegedExecuteContract(
            sender=sender,
            contract_address=contract,
            data=msg,
            funds=kwargs.get("funds")  # funds is a string of Coin strings, comma separated,
            # e.g. 100000inj,20000000000usdt
        )

    def msg_privileged_execute_contract(
        self,
        sender: str,
        contract_address: str,
        data: str,
        funds: Optional[str] = None,
    ) -> injective_exchange_tx_pb.MsgPrivilegedExecuteContract:
        # funds is a string of Coin strings, comma separated,  e.g. 100000inj,20000000000usdt
        return injective_exchange_tx_pb.MsgPrivilegedExecuteContract(
            sender=sender,
            contract_address=contract_address,
            data=data,
            funds=funds,
        )

    def MsgCreateDerivativeLimitOrder(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        cid: Optional[str] = None,
        **kwargs,
    ):
        """
        This method is deprecated and will be removed soon. Please use `msg_create_derivative_limit_order` instead
        """
        warn(
            "This method is deprecated. Use msg_create_derivative_limit_order instead", DeprecationWarning, stacklevel=2
        )

        if kwargs.get("is_reduce_only", False):
            margin = Decimal(0)
        else:
            margin = Decimal(str(price)) * Decimal(str(quantity)) / Decimal(str(kwargs["leverage"]))

        if kwargs.get("is_buy") and not kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.BUY)

        elif not kwargs.get("is_buy") and not kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.SELL)

        elif kwargs.get("is_buy") and kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.BUY_PO)

        elif not kwargs.get("is_buy") and kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.SELL_PO)

        elif kwargs.get("stop_buy"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.STOP_BUY)

        elif kwargs.get("stop_sell"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.STOP_SEll)

        elif kwargs.get("take_buy"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.TAKE_BUY)

        elif kwargs.get("take_sell"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.TAKE_SELL)

        return injective_exchange_tx_pb.MsgCreateDerivativeLimitOrder(
            sender=sender,
            order=self.derivative_order(
                market_id=market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=Decimal(str(price)),
                quantity=Decimal(str(quantity)),
                margin=margin,
                order_type=order_type,
                cid=cid,
                trigger_price=Decimal(str(kwargs["trigger_price"])) if "trigger_price" in kwargs else None,
            ),
        )

    def msg_create_derivative_limit_order(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: Decimal,
        quantity: Decimal,
        margin: Decimal,
        order_type: str,
        cid: Optional[str] = None,
        trigger_price: Optional[Decimal] = None,
    ) -> injective_exchange_tx_pb.MsgCreateDerivativeLimitOrder:
        return injective_exchange_tx_pb.MsgCreateDerivativeLimitOrder(
            sender=sender,
            order=self.derivative_order(
                market_id=market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=price,
                quantity=quantity,
                margin=margin,
                order_type=order_type,
                cid=cid,
                trigger_price=trigger_price,
            ),
        )

    def MsgBatchCreateDerivativeLimitOrders(self, sender: str, orders: List):
        """
        This method is deprecated and will be removed soon.
        Please use `msg_batch_create_derivative_limit_orders` instead
        """
        warn(
            "This method is deprecated. Use msg_batch_create_derivative_limit_orders instead",
            DeprecationWarning,
            stacklevel=2,
        )
        return injective_exchange_tx_pb.MsgBatchCreateDerivativeLimitOrders(sender=sender, orders=orders)

    def msg_batch_create_derivative_limit_orders(
        self,
        sender: str,
        orders: List[injective_exchange_pb.DerivativeOrder],
    ) -> injective_exchange_tx_pb.MsgBatchCreateDerivativeLimitOrders:
        return injective_exchange_tx_pb.MsgBatchCreateDerivativeLimitOrders(sender=sender, orders=orders)

    def MsgCreateDerivativeMarketOrder(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        cid: Optional[str] = None,
        **kwargs,
    ):
        """
        This method is deprecated and will be removed soon. Please use `msg_create_derivative_market_order` instead
        """
        warn(
            "This method is deprecated. Use msg_create_derivative_market_order instead",
            DeprecationWarning,
            stacklevel=2,
        )

        if kwargs.get("is_reduce_only", False):
            margin = Decimal(0)
        else:
            margin = Decimal(str(price)) * Decimal(str(quantity)) / Decimal(str(kwargs["leverage"]))

        if kwargs.get("is_buy") and not kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.BUY)

        elif not kwargs.get("is_buy") and not kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.SELL)

        elif kwargs.get("is_buy") and kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.BUY_PO)

        elif not kwargs.get("is_buy") and kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.SELL_PO)

        elif kwargs.get("stop_buy"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.STOP_BUY)

        elif kwargs.get("stop_sell"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.STOP_SEll)

        elif kwargs.get("take_buy"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.TAKE_BUY)

        elif kwargs.get("take_sell"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.TAKE_SELL)

        return injective_exchange_tx_pb.MsgCreateDerivativeMarketOrder(
            sender=sender,
            order=self.derivative_order(
                market_id=market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=Decimal(str(price)),
                quantity=Decimal(str(quantity)),
                margin=margin,
                order_type=order_type,
                cid=cid,
                trigger_price=Decimal(str(kwargs["trigger_price"])) if "trigger_price" in kwargs else None,
            ),
        )

    def msg_create_derivative_market_order(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: Decimal,
        quantity: Decimal,
        margin: Decimal,
        order_type: str,
        cid: Optional[str] = None,
        trigger_price: Optional[Decimal] = None,
    ) -> injective_exchange_tx_pb.MsgCreateDerivativeMarketOrder:
        return injective_exchange_tx_pb.MsgCreateDerivativeMarketOrder(
            sender=sender,
            order=self.derivative_order(
                market_id=market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=price,
                quantity=quantity,
                margin=margin,
                order_type=order_type,
                cid=cid,
                trigger_price=trigger_price,
            ),
        )

    def MsgCancelDerivativeOrder(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        order_hash: Optional[str] = None,
        cid: Optional[str] = None,
        **kwargs,
    ):
        """
        This method is deprecated and will be removed soon. Please use `msg_cancel_derivative_order` instead
        """
        warn(
            "This method is deprecated. Use msg_cancel_derivative_order instead",
            DeprecationWarning,
            stacklevel=2,
        )

        is_conditional = kwargs.get("is_conditional", False)
        is_buy = kwargs.get("order_direction", "buy") == "buy"
        is_market_order = kwargs.get("order_type", "limit") == "market"
        order_mask = self._order_mask(is_conditional=is_conditional, is_buy=is_buy, is_market_order=is_market_order)

        return injective_exchange_tx_pb.MsgCancelDerivativeOrder(
            sender=sender,
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hash=order_hash,
            order_mask=order_mask,
            cid=cid,
        )

    def msg_cancel_derivative_order(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        order_hash: Optional[str] = None,
        cid: Optional[str] = None,
        is_conditional: Optional[bool] = False,
        is_buy: Optional[bool] = False,
        is_market_order: Optional[bool] = False,
    ) -> injective_exchange_tx_pb.MsgCancelDerivativeOrder:
        order_mask = self._order_mask(is_conditional=is_conditional, is_buy=is_buy, is_market_order=is_market_order)

        return injective_exchange_tx_pb.MsgCancelDerivativeOrder(
            sender=sender,
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hash=order_hash,
            order_mask=order_mask,
            cid=cid,
        )

    def MsgBatchCancelDerivativeOrders(self, sender: str, data: List):
        """
        This method is deprecated and will be removed soon. Please use `msg_batch_cancel_derivative_orders` instead
        """
        warn(
            "This method is deprecated. Use msg_batch_cancel_derivative_orders instead",
            DeprecationWarning,
            stacklevel=2,
        )
        return injective_exchange_tx_pb.MsgBatchCancelDerivativeOrders(sender=sender, data=data)

    def msg_batch_cancel_derivative_orders(
        self, sender: str, orders_data: List[injective_exchange_tx_pb.OrderData]
    ) -> injective_exchange_tx_pb.MsgBatchCancelDerivativeOrders:
        return injective_exchange_tx_pb.MsgBatchCancelDerivativeOrders(sender=sender, data=orders_data)

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
        """
        This method is deprecated and will be removed soon.
        Please use `msg_instant_binary_options_market_launch` instead
        """
        warn(
            "This method is deprecated. Use msg_instant_binary_options_market_launch instead",
            DeprecationWarning,
            stacklevel=2,
        )
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

    def msg_instant_binary_options_market_launch(
        self,
        sender: str,
        ticker: str,
        oracle_symbol: str,
        oracle_provider: str,
        oracle_type: str,
        oracle_scale_factor: int,
        maker_fee_rate: Decimal,
        taker_fee_rate: Decimal,
        expiration_timestamp: int,
        settlement_timestamp: int,
        admin: str,
        quote_denom: str,
        min_price_tick_size: Decimal,
        min_quantity_tick_size: Decimal,
    ) -> injective_exchange_tx_pb.MsgInstantPerpetualMarketLaunch:
        quote_token = self.tokens[quote_denom]

        chain_min_price_tick_size = min_price_tick_size * Decimal(
            f"1e{quote_token.decimals + ADDITIONAL_CHAIN_FORMAT_DECIMALS}"
        )
        chain_min_quantity_tick_size = min_quantity_tick_size * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        chain_maker_fee_rate = maker_fee_rate * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        chain_taker_fee_rate = taker_fee_rate * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        return injective_exchange_tx_pb.MsgInstantBinaryOptionsMarketLaunch(
            sender=sender,
            ticker=ticker,
            oracle_symbol=oracle_symbol,
            oracle_provider=oracle_provider,
            oracle_type=injective_oracle_pb.OracleType.Value(oracle_type),
            oracle_scale_factor=oracle_scale_factor,
            maker_fee_rate=f"{chain_maker_fee_rate.normalize():f}",
            taker_fee_rate=f"{chain_taker_fee_rate.normalize():f}",
            expiration_timestamp=expiration_timestamp,
            settlement_timestamp=settlement_timestamp,
            admin=admin,
            quote_denom=quote_token.denom,
            min_price_tick_size=f"{chain_min_price_tick_size.normalize():f}",
            min_quantity_tick_size=f"{chain_min_quantity_tick_size.normalize():f}",
        )

    def MsgCreateBinaryOptionsLimitOrder(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        cid: Optional[str] = None,
        **kwargs,
    ):
        """
        This method is deprecated and will be removed soon. Please use `msg_create_binary_options_limit_order` instead
        """
        warn(
            "This method is deprecated. Use msg_create_binary_options_limit_order instead",
            DeprecationWarning,
            stacklevel=2,
        )
        if kwargs.get("is_reduce_only", False):
            margin = Decimal(0)
        else:
            margin = Decimal(str(price)) * Decimal(str(quantity))

        if kwargs.get("is_buy") and not kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.BUY)

        elif not kwargs.get("is_buy") and not kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.SELL)

        elif kwargs.get("is_buy") and kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.BUY_PO)

        elif not kwargs.get("is_buy") and kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.SELL_PO)

        elif kwargs.get("stop_buy"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.STOP_BUY)

        elif kwargs.get("stop_sell"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.STOP_SEll)

        elif kwargs.get("take_buy"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.TAKE_BUY)

        elif kwargs.get("take_sell"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.TAKE_SELL)

        return injective_exchange_tx_pb.MsgCreateBinaryOptionsLimitOrder(
            sender=sender,
            order=self.binary_options_order(
                market_id=market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=Decimal(str(price)),
                quantity=Decimal(str(quantity)),
                margin=margin,
                order_type=order_type,
                cid=cid,
                trigger_price=Decimal(str(kwargs["trigger_price"])) if "trigger_price" in kwargs else None,
                denom=kwargs.get("denom"),
            ),
        )

    def msg_create_binary_options_limit_order(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: Decimal,
        quantity: Decimal,
        margin: Decimal,
        order_type: str,
        cid: Optional[str] = None,
        trigger_price: Optional[Decimal] = None,
        denom: Optional[Denom] = None,
    ) -> injective_exchange_tx_pb.MsgCreateDerivativeLimitOrder:
        return injective_exchange_tx_pb.MsgCreateDerivativeLimitOrder(
            sender=sender,
            order=self.binary_options_order(
                market_id=market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=price,
                quantity=quantity,
                margin=margin,
                order_type=order_type,
                cid=cid,
                trigger_price=trigger_price,
                denom=denom,
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
        cid: Optional[str] = None,
        **kwargs,
    ):
        """
        This method is deprecated and will be removed soon. Please use `msg_create_binary_options_market_order` instead
        """
        warn(
            "This method is deprecated. Use msg_create_binary_options_market_order instead",
            DeprecationWarning,
            stacklevel=2,
        )
        if kwargs.get("is_reduce_only", False):
            margin = Decimal(0)
        else:
            margin = Decimal(str(price)) * Decimal(str(quantity))

        if kwargs.get("is_buy") and not kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.BUY)

        elif not kwargs.get("is_buy") and not kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.SELL)

        elif kwargs.get("is_buy") and kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.BUY_PO)

        elif not kwargs.get("is_buy") and kwargs.get("is_po"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.SELL_PO)

        elif kwargs.get("stop_buy"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.STOP_BUY)

        elif kwargs.get("stop_sell"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.STOP_SEll)

        elif kwargs.get("take_buy"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.TAKE_BUY)

        elif kwargs.get("take_sell"):
            order_type = injective_exchange_pb.OrderType.Name(injective_exchange_pb.OrderType.TAKE_SELL)

        return injective_exchange_tx_pb.MsgCreateBinaryOptionsMarketOrder(
            sender=sender,
            order=self.binary_options_order(
                market_id=market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=Decimal(str(price)),
                quantity=Decimal(str(quantity)),
                margin=margin,
                order_type=order_type,
                cid=cid,
                trigger_price=Decimal(str(kwargs["trigger_price"])) if "trigger_price" in kwargs else None,
                denom=kwargs.get("denom"),
            ),
        )

    def msg_create_binary_options_market_order(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: Decimal,
        quantity: Decimal,
        margin: Decimal,
        order_type: str,
        cid: Optional[str] = None,
        trigger_price: Optional[Decimal] = None,
        denom: Optional[Denom] = None,
    ):
        return injective_exchange_tx_pb.MsgCreateBinaryOptionsMarketOrder(
            sender=sender,
            order=self.binary_options_order(
                market_id=market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=price,
                quantity=quantity,
                margin=margin,
                order_type=order_type,
                cid=cid,
                trigger_price=trigger_price,
                denom=denom,
            ),
        )

    def MsgCancelBinaryOptionsOrder(
        self,
        sender: str,
        market_id: str,
        subaccount_id: str,
        order_hash: Optional[str] = None,
        cid: Optional[str] = None,
    ):
        """
        This method is deprecated and will be removed soon. Please use `msg_cancel_binary_options_order` instead
        """
        warn(
            "This method is deprecated. Use msg_cancel_binary_options_order instead",
            DeprecationWarning,
            stacklevel=2,
        )
        return injective_exchange_tx_pb.MsgCancelBinaryOptionsOrder(
            sender=sender,
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hash=order_hash,
            cid=cid,
        )

    def msg_cancel_binary_options_order(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        order_hash: Optional[str] = None,
        cid: Optional[str] = None,
        is_conditional: Optional[bool] = False,
        is_buy: Optional[bool] = False,
        is_market_order: Optional[bool] = False,
    ) -> injective_exchange_tx_pb.MsgCancelBinaryOptionsOrder:
        order_mask = self._order_mask(is_conditional=is_conditional, is_buy=is_buy, is_market_order=is_market_order)

        return injective_exchange_tx_pb.MsgCancelBinaryOptionsOrder(
            sender=sender,
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hash=order_hash,
            order_mask=order_mask,
            cid=cid,
        )

    def MsgSubaccountTransfer(
        self,
        sender: str,
        source_subaccount_id: str,
        destination_subaccount_id: str,
        amount: int,
        denom: str,
    ):
        """
        This method is deprecated and will be removed soon. Please use `msg_subaccount_transfer` instead
        """
        warn(
            "This method is deprecated. Use msg_subaccount_transfer instead",
            DeprecationWarning,
            stacklevel=2,
        )
        be_amount = self.create_coin_amount(amount=Decimal(str(amount)), token_name=denom)

        return injective_exchange_tx_pb.MsgSubaccountTransfer(
            sender=sender,
            source_subaccount_id=source_subaccount_id,
            destination_subaccount_id=destination_subaccount_id,
            amount=be_amount,
        )

    def msg_subaccount_transfer(
        self,
        sender: str,
        source_subaccount_id: str,
        destination_subaccount_id: str,
        amount: Decimal,
        denom: str,
    ) -> injective_exchange_tx_pb.MsgSubaccountTransfer:
        be_amount = self.create_coin_amount(amount=amount, token_name=denom)

        return injective_exchange_tx_pb.MsgSubaccountTransfer(
            sender=sender,
            source_subaccount_id=source_subaccount_id,
            destination_subaccount_id=destination_subaccount_id,
            amount=be_amount,
        )

    def MsgExternalTransfer(
        self,
        sender: str,
        source_subaccount_id: str,
        destination_subaccount_id: str,
        amount: int,
        denom: str,
    ):
        """
        This method is deprecated and will be removed soon. Please use `msg_external_transfer` instead
        """
        warn(
            "This method is deprecated. Use msg_external_transfer instead",
            DeprecationWarning,
            stacklevel=2,
        )
        coin = self.create_coin_amount(amount=Decimal(str(amount)), token_name=denom)

        return injective_exchange_tx_pb.MsgExternalTransfer(
            sender=sender,
            source_subaccount_id=source_subaccount_id,
            destination_subaccount_id=destination_subaccount_id,
            amount=coin,
        )

    def msg_external_transfer(
        self,
        sender: str,
        source_subaccount_id: str,
        destination_subaccount_id: str,
        amount: Decimal,
        denom: str,
    ) -> injective_exchange_tx_pb.MsgExternalTransfer:
        coin = self.create_coin_amount(amount=amount, token_name=denom)

        return injective_exchange_tx_pb.MsgExternalTransfer(
            sender=sender,
            source_subaccount_id=source_subaccount_id,
            destination_subaccount_id=destination_subaccount_id,
            amount=coin,
        )

    def MsgLiquidatePosition(
        self,
        sender: str,
        subaccount_id: str,
        market_id: str,
        order: Optional[injective_exchange_pb.DerivativeOrder] = None,
    ):
        """
        This method is deprecated and will be removed soon. Please use `msg_liquidate_position` instead
        """
        warn(
            "This method is deprecated. Use msg_liquidate_position instead",
            DeprecationWarning,
            stacklevel=2,
        )
        return injective_exchange_tx_pb.MsgLiquidatePosition(
            sender=sender, subaccount_id=subaccount_id, market_id=market_id, order=order
        )

    def msg_liquidate_position(
        self,
        sender: str,
        subaccount_id: str,
        market_id: str,
        order: Optional[injective_exchange_pb.DerivativeOrder] = None,
    ) -> injective_exchange_tx_pb.MsgLiquidatePosition:
        return injective_exchange_tx_pb.MsgLiquidatePosition(
            sender=sender, subaccount_id=subaccount_id, market_id=market_id, order=order
        )

    def msg_emergency_settle_market(
        self,
        sender: str,
        subaccount_id: str,
        market_id: str,
    ) -> injective_exchange_tx_pb.MsgEmergencySettleMarket:
        return injective_exchange_tx_pb.MsgEmergencySettleMarket(
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
        """
        This method is deprecated and will be removed soon. Please use `msg_increase_position_margin` instead
        """
        warn(
            "This method is deprecated. Use msg_increase_position_margin instead",
            DeprecationWarning,
            stacklevel=2,
        )
        market = self.derivative_markets[market_id]

        additional_margin = market.margin_to_chain_format(human_readable_value=Decimal(str(amount)))
        return injective_exchange_tx_pb.MsgIncreasePositionMargin(
            sender=sender,
            source_subaccount_id=source_subaccount_id,
            destination_subaccount_id=destination_subaccount_id,
            market_id=market_id,
            amount=str(int(additional_margin)),
        )

    def msg_increase_position_margin(
        self,
        sender: str,
        source_subaccount_id: str,
        destination_subaccount_id: str,
        market_id: str,
        amount: Decimal,
    ):
        market = self.derivative_markets[market_id]

        additional_margin = market.margin_to_chain_format(human_readable_value=amount)
        return injective_exchange_tx_pb.MsgIncreasePositionMargin(
            sender=sender,
            source_subaccount_id=source_subaccount_id,
            destination_subaccount_id=destination_subaccount_id,
            market_id=market_id,
            amount=str(int(additional_margin)),
        )

    def MsgRewardsOptOut(self, sender: str):
        """
        This method is deprecated and will be removed soon. Please use `msg_rewards_opt_out` instead
        """
        warn(
            "This method is deprecated. Use msg_rewards_opt_out instead",
            DeprecationWarning,
            stacklevel=2,
        )
        return injective_exchange_tx_pb.MsgRewardsOptOut(sender=sender)

    def msg_rewards_opt_out(self, sender: str) -> injective_exchange_tx_pb.MsgRewardsOptOut:
        return injective_exchange_tx_pb.MsgRewardsOptOut(sender=sender)

    def MsgAdminUpdateBinaryOptionsMarket(
        self,
        sender: str,
        market_id: str,
        status: str,
        **kwargs,
    ):
        """
        This method is deprecated and will be removed soon. Please use `msg_admin_update_binary_options_market` instead
        """
        warn(
            "This method is deprecated. Use msg_admin_update_binary_options_market instead",
            DeprecationWarning,
            stacklevel=2,
        )

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

    def msg_admin_update_binary_options_market(
        self,
        sender: str,
        market_id: str,
        status: str,
        settlement_price: Optional[Decimal] = None,
        expiration_timestamp: Optional[int] = None,
        settlement_timestamp: Optional[int] = None,
    ) -> injective_exchange_tx_pb.MsgAdminUpdateBinaryOptionsMarket:
        market = self.binary_option_markets[market_id]

        if settlement_price is not None:
            chain_settlement_price = market.price_to_chain_format(human_readable_value=settlement_price)
            price_parameter = f"{chain_settlement_price.normalize():f}"
        else:
            price_parameter = None

        return injective_exchange_tx_pb.MsgAdminUpdateBinaryOptionsMarket(
            sender=sender,
            market_id=market_id,
            settlement_price=price_parameter,
            expiration_timestamp=expiration_timestamp,
            settlement_timestamp=settlement_timestamp,
            status=status,
        )

    # endregion

    # region Insurance module
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
        deposit = self.create_coin_amount(Decimal(str(initial_deposit)), quote_denom)

        return injective_insurance_tx_pb.MsgCreateInsuranceFund(
            sender=sender,
            ticker=ticker,
            quote_denom=token.denom,
            oracle_base=oracle_base,
            oracle_quote=oracle_quote,
            oracle_type=oracle_type,
            expiry=expiry,
            initial_deposit=deposit,
        )

    def MsgUnderwrite(
        self,
        sender: str,
        market_id: str,
        quote_denom: str,
        amount: int,
    ):
        be_amount = self.create_coin_amount(amount=Decimal(str(amount)), token_name=quote_denom)

        return injective_insurance_tx_pb.MsgUnderwrite(
            sender=sender,
            market_id=market_id,
            deposit=be_amount,
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
            amount=self.coin(amount=amount, denom=share_denom),
        )

    # endregion

    # region Oracle module
    def MsgRelayProviderPrices(self, sender: str, provider: str, symbols: list, prices: list):
        oracle_prices = []

        for price in prices:
            scale_price = Decimal((price) * pow(10, 18))
            price_to_bytes = bytes(str(scale_price), "utf-8")
            oracle_prices.append(price_to_bytes)

        return injective_oracle_tx_pb.MsgRelayProviderPrices(
            sender=sender, provider=provider, symbols=symbols, prices=oracle_prices
        )

    def MsgRelayPriceFeedPrice(self, sender: list, base: list, quote: list, price: list):
        return injective_oracle_tx_pb.MsgRelayPriceFeedPrice(sender=sender, base=base, quote=quote, price=price)

    # endregion

    # region Peggy module
    def MsgSendToEth(self, denom: str, sender: str, eth_dest: str, amount: float, bridge_fee: float):
        be_amount = self.create_coin_amount(amount=Decimal(str(amount)), token_name=denom)
        be_bridge_fee = self.create_coin_amount(amount=Decimal(str(bridge_fee)), token_name=denom)

        return injective_peggy_tx_pb.MsgSendToEth(
            sender=sender,
            eth_dest=eth_dest,
            amount=be_amount,
            bridge_fee=be_bridge_fee,
        )

    # endregion

    # region Staking module
    def MsgDelegate(self, delegator_address: str, validator_address: str, amount: float):
        be_amount = Decimal(str(amount)) * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        return cosmos_staking_tx_pb.MsgDelegate(
            delegator_address=delegator_address,
            validator_address=validator_address,
            amount=self.coin(amount=int(be_amount), denom=INJ_DENOM),
        )

    # endregion

    # region Tokenfactory module
    def msg_create_denom(
        self,
        sender: str,
        subdenom: str,
        name: str,
        symbol: str,
    ) -> token_factory_tx_pb.MsgCreateDenom:
        return token_factory_tx_pb.MsgCreateDenom(
            sender=sender,
            subdenom=subdenom,
            name=name,
            symbol=symbol,
        )

    def msg_mint(
        self,
        sender: str,
        amount: base_coin_pb.Coin,
    ) -> token_factory_tx_pb.MsgMint:
        return token_factory_tx_pb.MsgMint(sender=sender, amount=amount)

    def msg_burn(
        self,
        sender: str,
        amount: base_coin_pb.Coin,
    ) -> token_factory_tx_pb.MsgBurn:
        return token_factory_tx_pb.MsgBurn(sender=sender, amount=amount)

    def msg_set_denom_metadata(
        self,
        sender: str,
        description: str,
        denom: str,
        subdenom: str,
        token_decimals: int,
        name: str,
        symbol: str,
        uri: str,
        uri_hash: str,
    ) -> token_factory_tx_pb.MsgSetDenomMetadata:
        micro_denom_unit = bank_pb.DenomUnit(
            denom=denom,
            exponent=0,
            aliases=[f"micro{subdenom}"],
        )
        denom_unit = bank_pb.DenomUnit(
            denom=subdenom,
            exponent=token_decimals,
            aliases=[subdenom],
        )
        metadata = bank_pb.Metadata(
            description=description,
            denom_units=[micro_denom_unit, denom_unit],
            base=denom,
            display=subdenom,
            name=name,
            symbol=symbol,
            uri=uri,
            uri_hash=uri_hash,
        )
        return token_factory_tx_pb.MsgSetDenomMetadata(sender=sender, metadata=metadata)

    def msg_change_admin(
        self,
        sender: str,
        denom: str,
        new_admin: str,
    ) -> token_factory_tx_pb.MsgChangeAdmin:
        return token_factory_tx_pb.MsgChangeAdmin(
            sender=sender,
            denom=denom,
            new_admin=new_admin,
        )

    # endregion

    # region Wasm module
    def MsgInstantiateContract(
        self, sender: str, admin: str, code_id: int, label: str, message: bytes, **kwargs
    ) -> wasm_tx_pb.MsgInstantiateContract:
        return wasm_tx_pb.MsgInstantiateContract(
            sender=sender,
            admin=admin,
            code_id=code_id,
            label=label,
            msg=message,
            funds=kwargs.get("funds"),  # funds is a list of base_coin_pb.Coin.
            # The coins in the list must be sorted in alphabetical order by denoms.
        )

    def MsgExecuteContract(self, sender: str, contract: str, msg: str, **kwargs):
        return wasm_tx_pb.MsgExecuteContract(
            sender=sender,
            contract=contract,
            msg=bytes(msg, "utf-8"),
            funds=kwargs.get("funds")  # funds is a list of base_coin_pb.Coin.
            # The coins in the list must be sorted in alphabetical order by denoms.
        )

    # endregion

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

    def MsgVote(
        self,
        proposal_id: str,
        voter: str,
        option: int,
    ):
        return cosmos_gov_tx_pb.MsgVote(proposal_id=proposal_id, voter=voter, option=option)

    def chain_stream_bank_balances_filter(
        self, accounts: Optional[List[str]] = None
    ) -> chain_stream_query.BankBalancesFilter:
        accounts = accounts or ["*"]
        return chain_stream_query.BankBalancesFilter(accounts=accounts)

    def chain_stream_subaccount_deposits_filter(
        self,
        subaccount_ids: Optional[List[str]] = None,
    ) -> chain_stream_query.SubaccountDepositsFilter:
        subaccount_ids = subaccount_ids or ["*"]
        return chain_stream_query.SubaccountDepositsFilter(subaccount_ids=subaccount_ids)

    def chain_stream_trades_filter(
        self,
        subaccount_ids: Optional[List[str]] = None,
        market_ids: Optional[List[str]] = None,
    ) -> chain_stream_query.TradesFilter:
        subaccount_ids = subaccount_ids or ["*"]
        market_ids = market_ids or ["*"]
        return chain_stream_query.TradesFilter(subaccount_ids=subaccount_ids, market_ids=market_ids)

    def chain_stream_orders_filter(
        self,
        subaccount_ids: Optional[List[str]] = None,
        market_ids: Optional[List[str]] = None,
    ) -> chain_stream_query.OrdersFilter:
        subaccount_ids = subaccount_ids or ["*"]
        market_ids = market_ids or ["*"]
        return chain_stream_query.OrdersFilter(subaccount_ids=subaccount_ids, market_ids=market_ids)

    def chain_stream_orderbooks_filter(
        self,
        market_ids: Optional[List[str]] = None,
    ) -> chain_stream_query.OrderbookFilter:
        market_ids = market_ids or ["*"]
        return chain_stream_query.OrderbookFilter(market_ids=market_ids)

    def chain_stream_positions_filter(
        self,
        subaccount_ids: Optional[List[str]] = None,
        market_ids: Optional[List[str]] = None,
    ) -> chain_stream_query.PositionsFilter:
        subaccount_ids = subaccount_ids or ["*"]
        market_ids = market_ids or ["*"]
        return chain_stream_query.PositionsFilter(subaccount_ids=subaccount_ids, market_ids=market_ids)

    def chain_stream_oracle_price_filter(
        self,
        symbols: Optional[List[str]] = None,
    ) -> chain_stream_query.PositionsFilter:
        symbols = symbols or ["*"]
        return chain_stream_query.OraclePriceFilter(symbol=symbols)

    # ------------------------------------------------
    # Distribution module's messages

    def msg_set_withdraw_address(self, delegator_address: str, withdraw_address: str):
        return cosmos_distribution_tx_pb.MsgSetWithdrawAddress(
            delegator_address=delegator_address, withdraw_address=withdraw_address
        )

    # Deprecated
    def MsgWithdrawDelegatorReward(self, delegator_address: str, validator_address: str):
        """
        This method is deprecated and will be removed soon. Please use `msg_withdraw_delegator_reward` instead
        """
        warn("This method is deprecated. Use msg_withdraw_delegator_reward instead", DeprecationWarning, stacklevel=2)
        return cosmos_distribution_tx_pb.MsgWithdrawDelegatorReward(
            delegator_address=delegator_address, validator_address=validator_address
        )

    def msg_withdraw_delegator_reward(self, delegator_address: str, validator_address: str):
        return cosmos_distribution_tx_pb.MsgWithdrawDelegatorReward(
            delegator_address=delegator_address, validator_address=validator_address
        )

    def MsgWithdrawValidatorCommission(self, validator_address: str):
        """
        This method is deprecated and will be removed soon. Please use `msg_withdraw_validator_commission` instead
        """
        warn(
            "This method is deprecated. Use msg_withdraw_validator_commission instead", DeprecationWarning, stacklevel=2
        )
        return cosmos_distribution_tx_pb.MsgWithdrawValidatorCommission(validator_address=validator_address)

    def msg_withdraw_validator_commission(self, validator_address: str):
        return cosmos_distribution_tx_pb.MsgWithdrawValidatorCommission(validator_address=validator_address)

    def msg_fund_community_pool(self, amounts: List[base_coin_pb.Coin], depositor: str):
        return cosmos_distribution_tx_pb.MsgFundCommunityPool(amount=amounts, depositor=depositor)

    def msg_update_distribution_params(self, authority: str, community_tax: str, withdraw_address_enabled: bool):
        params = cosmos_distribution_pb2.Params(
            community_tax=community_tax,
            withdraw_addr_enabled=withdraw_address_enabled,
        )
        return cosmos_distribution_tx_pb.MsgUpdateParams(authority=authority, params=params)

    def msg_community_pool_spend(self, authority: str, recipient: str, amount: List[base_coin_pb.Coin]):
        return cosmos_distribution_tx_pb.MsgCommunityPoolSpend(authority=authority, recipient=recipient, amount=amount)

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
        responses = []
        dict_message = json_format.MessageToDict(message=data, including_default_value_fields=True)
        json_responses = Composer.unpack_msg_exec_response(underlying_msg_type=msg_type, msg_exec_response=dict_message)
        for json_response in json_responses:
            response = REQUEST_TO_RESPONSE_TYPE_MAP[msg_type]()
            json_format.ParseDict(js_dict=json_response, message=response, ignore_unknown_fields=True)
            responses.append(response)
        return responses

    @staticmethod
    def unpack_msg_exec_response(underlying_msg_type: str, msg_exec_response: Dict[str, Any]) -> List[Dict[str, Any]]:
        grpc_response = cosmos_authz_tx_pb.MsgExecResponse()
        json_format.ParseDict(js_dict=msg_exec_response, message=grpc_response, ignore_unknown_fields=True)
        responses = [
            json_format.MessageToDict(
                message=REQUEST_TO_RESPONSE_TYPE_MAP[underlying_msg_type].FromString(result),
                including_default_value_fields=True,
            )
            for result in grpc_response.results
        ]

        return responses

    @staticmethod
    def UnpackTransactionMessages(transaction):
        meta_messages = json.loads(transaction.messages.decode())
        header_map = GRPC_MESSAGE_TYPE_TO_CLASS_MAP
        msgs = []
        for msg in meta_messages:
            msg_as_string_dict = json.dumps(msg["value"])
            msgs.append(json_format.Parse(msg_as_string_dict, header_map[msg["type"]]()))

        return msgs

    @staticmethod
    def unpack_transaction_messages(transaction_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        grpc_tx = explorer_pb2.TxDetailData()
        json_format.ParseDict(js_dict=transaction_data, message=grpc_tx, ignore_unknown_fields=True)
        meta_messages = json.loads(grpc_tx.messages.decode())
        msgs = []
        for msg in meta_messages:
            msg_as_string_dict = json.dumps(msg["value"])
            grpc_message = json_format.Parse(msg_as_string_dict, GRPC_MESSAGE_TYPE_TO_CLASS_MAP[msg["type"]]())
            msgs.append(
                {
                    "type": msg["type"],
                    "value": json_format.MessageToDict(message=grpc_message, including_default_value_fields=True),
                }
            )

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

    def _order_mask(self, is_conditional: bool, is_buy: bool, is_market_order: bool) -> int:
        order_mask = 0

        if is_conditional:
            order_mask += injective_exchange_pb.OrderMask.CONDITIONAL
        else:
            order_mask += injective_exchange_pb.OrderMask.REGULAR

        if is_buy:
            order_mask += injective_exchange_pb.OrderMask.DIRECTION_BUY_OR_HIGHER
        else:
            order_mask += injective_exchange_pb.OrderMask.DIRECTION_SELL_OR_LOWER

        if is_market_order:
            order_mask += injective_exchange_pb.OrderMask.TYPE_MARKET
        else:
            order_mask += injective_exchange_pb.OrderMask.TYPE_LIMIT

        if order_mask == 0:
            order_mask = 1

        return order_mask

    def _basic_derivative_order(
        self,
        market_id: str,
        subaccount_id: str,
        fee_recipient: str,
        chain_price: Decimal,
        chain_quantity: Decimal,
        chain_margin: Decimal,
        order_type: str,
        cid: Optional[str] = None,
        chain_trigger_price: Optional[Decimal] = None,
    ) -> injective_exchange_pb.DerivativeOrder:
        formatted_quantity = f"{chain_quantity.normalize():f}"
        formatted_price = f"{chain_price.normalize():f}"
        formatted_margin = f"{chain_margin.normalize():f}"

        trigger_price = chain_trigger_price or Decimal(0)
        formatted_trigger_price = f"{trigger_price.normalize():f}"

        chain_order_type = injective_exchange_pb.OrderType.Value(order_type)

        return injective_exchange_pb.DerivativeOrder(
            market_id=market_id,
            order_info=injective_exchange_pb.OrderInfo(
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=formatted_price,
                quantity=formatted_quantity,
                cid=cid,
            ),
            order_type=chain_order_type,
            margin=formatted_margin,
            trigger_price=formatted_trigger_price,
        )
