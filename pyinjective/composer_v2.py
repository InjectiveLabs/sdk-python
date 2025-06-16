import json
from decimal import Decimal
from enum import IntFlag
from time import time
from typing import Any, Dict, List, Optional

from google.protobuf import any_pb2, json_format, timestamp_pb2

from pyinjective.constant import INJ_DECIMALS, INJ_DENOM
from pyinjective.core.token import Token
from pyinjective.ofac import OfacChecker
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
from pyinjective.proto.ibc.applications.transfer.v1 import tx_pb2 as ibc_transfer_tx_pb
from pyinjective.proto.ibc.core.client.v1 import client_pb2 as ibc_core_client_pb
from pyinjective.proto.injective.auction.v1beta1 import tx_pb2 as injective_auction_tx_pb
from pyinjective.proto.injective.erc20.v1beta1 import erc20_pb2 as injective_erc20_pb2, tx_pb2 as injective_erc20_tx_pb
from pyinjective.proto.injective.exchange.v1beta1 import tx_pb2 as injective_exchange_tx_pb
from pyinjective.proto.injective.exchange.v2 import (
    authz_pb2 as injective_authz_v2_pb,
    exchange_pb2 as injective_exchange_v2_pb,
    order_pb2 as injective_order_v2_pb,
    tx_pb2 as injective_exchange_tx_v2_pb,
)
from pyinjective.proto.injective.insurance.v1beta1 import tx_pb2 as injective_insurance_tx_pb
from pyinjective.proto.injective.oracle.v1beta1 import (
    oracle_pb2 as injective_oracle_pb,
    tx_pb2 as injective_oracle_tx_pb,
)
from pyinjective.proto.injective.peggy.v1 import msgs_pb2 as injective_peggy_tx_pb
from pyinjective.proto.injective.permissions.v1beta1 import (
    permissions_pb2 as injective_permissions_pb,
    tx_pb2 as injective_permissions_tx_pb,
)
from pyinjective.proto.injective.stream.v2 import query_pb2 as chain_stream_v2_query
from pyinjective.proto.injective.tokenfactory.v1beta1 import tx_pb2 as token_factory_tx_pb
from pyinjective.proto.injective.wasmx.v1 import tx_pb2 as wasmx_tx_pb

# fmt: off
REQUEST_TO_RESPONSE_TYPE_MAP = {
    "MsgCreateSpotLimitOrder":
        injective_exchange_tx_v2_pb.MsgCreateSpotLimitOrderResponse,
    "MsgCreateSpotMarketOrder":
        injective_exchange_tx_v2_pb.MsgCreateSpotMarketOrderResponse,
    "MsgCreateDerivativeLimitOrder":
        injective_exchange_tx_v2_pb.MsgCreateDerivativeLimitOrderResponse,
    "MsgCreateDerivativeMarketOrder":
        injective_exchange_tx_v2_pb.MsgCreateDerivativeMarketOrderResponse,
    "MsgCancelSpotOrder":
        injective_exchange_tx_v2_pb.MsgCancelSpotOrderResponse,
    "MsgCancelDerivativeOrder":
        injective_exchange_tx_v2_pb.MsgCancelDerivativeOrderResponse,
    "MsgBatchCancelSpotOrders":
        injective_exchange_tx_v2_pb.MsgBatchCancelSpotOrdersResponse,
    "MsgBatchCancelDerivativeOrders":
        injective_exchange_tx_v2_pb.MsgBatchCancelDerivativeOrdersResponse,
    "MsgBatchCreateSpotLimitOrders":
        injective_exchange_tx_v2_pb.MsgBatchCreateSpotLimitOrdersResponse,
    "MsgBatchCreateDerivativeLimitOrders":
        injective_exchange_tx_v2_pb.MsgBatchCreateDerivativeLimitOrdersResponse,
    "MsgBatchUpdateOrders":
        injective_exchange_tx_v2_pb.MsgBatchUpdateOrdersResponse,
    "MsgDeposit":
        injective_exchange_tx_v2_pb.MsgDepositResponse,
    "MsgWithdraw":
        injective_exchange_tx_v2_pb.MsgWithdrawResponse,
    "MsgSubaccountTransfer":
        injective_exchange_tx_v2_pb.MsgSubaccountTransferResponse,
    "MsgLiquidatePosition":
        injective_exchange_tx_v2_pb.MsgLiquidatePositionResponse,
    "MsgIncreasePositionMargin":
        injective_exchange_tx_v2_pb.MsgIncreasePositionMarginResponse,
    "MsgCreateBinaryOptionsLimitOrder":
        injective_exchange_tx_v2_pb.MsgCreateBinaryOptionsLimitOrderResponse,
    "MsgCreateBinaryOptionsMarketOrder":
        injective_exchange_tx_v2_pb.MsgCreateBinaryOptionsMarketOrderResponse,
    "MsgCancelBinaryOptionsOrder":
        injective_exchange_tx_v2_pb.MsgCancelBinaryOptionsOrderResponse,
    "MsgAdminUpdateBinaryOptionsMarket":
        injective_exchange_tx_v2_pb.MsgAdminUpdateBinaryOptionsMarketResponse,
    "MsgInstantBinaryOptionsMarketLaunch":
        injective_exchange_tx_v2_pb.MsgInstantBinaryOptionsMarketLaunchResponse,
}

GRPC_MESSAGE_TYPE_TO_CLASS_MAP = {
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
        injective_exchange_tx_pb.MsgBatchCreateDerivativeLimitOrders,  # noqa: 121
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
    "/injective.exchange.v2.MsgCreateSpotLimitOrder":
        injective_exchange_tx_v2_pb.MsgCreateSpotLimitOrder,
    "/injective.exchange.v2.MsgCreateSpotMarketOrder":
        injective_exchange_tx_v2_pb.MsgCreateSpotMarketOrder,
    "/injective.exchange.v2.MsgCreateDerivativeLimitOrder":
        injective_exchange_tx_v2_pb.MsgCreateDerivativeLimitOrder,
    "/injective.exchange.v2.MsgCreateDerivativeMarketOrder":
        injective_exchange_tx_v2_pb.MsgCreateDerivativeMarketOrder,
    "/injective.exchange.v2.MsgCancelSpotOrder":
        injective_exchange_tx_v2_pb.MsgCancelSpotOrder,
    "/injective.exchange.v2.MsgCancelDerivativeOrder":
        injective_exchange_tx_v2_pb.MsgCancelDerivativeOrder,
    "/injective.exchange.v2.MsgBatchCancelSpotOrders":
        injective_exchange_tx_v2_pb.MsgBatchCancelSpotOrders,
    "/injective.exchange.v2.MsgBatchCancelDerivativeOrders":
        injective_exchange_tx_v2_pb.MsgBatchCancelDerivativeOrders,
    "/injective.exchange.v2.MsgBatchCreateSpotLimitOrders":
        injective_exchange_tx_v2_pb.MsgBatchCreateSpotLimitOrders,
    "/injective.exchange.v2.MsgBatchCreateDerivativeLimitOrders":
        injective_exchange_tx_v2_pb.MsgBatchCreateDerivativeLimitOrders,
    "/injective.exchange.v2.MsgBatchUpdateOrders":
        injective_exchange_tx_v2_pb.MsgBatchUpdateOrders,
    "/injective.exchange.v2.MsgDeposit":
        injective_exchange_tx_v2_pb.MsgDeposit,
    "/injective.exchange.v2.MsgWithdraw":
        injective_exchange_tx_v2_pb.MsgWithdraw,
    "/injective.exchange.v2.MsgSubaccountTransfer":
        injective_exchange_tx_v2_pb.MsgSubaccountTransfer,
    "/injective.exchange.v2.MsgLiquidatePosition":
        injective_exchange_tx_v2_pb.MsgLiquidatePosition,
    "/injective.exchange.v2.MsgIncreasePositionMargin":
        injective_exchange_tx_v2_pb.MsgIncreasePositionMargin,
    "/injective.exchange.v2.MsgCreateBinaryOptionsLimitOrder":
        injective_exchange_tx_v2_pb.MsgCreateBinaryOptionsLimitOrder,
    "/injective.exchange.v2.MsgCreateBinaryOptionsMarketOrder":
        injective_exchange_tx_v2_pb.MsgCreateBinaryOptionsMarketOrder,
    "/injective.exchange.v2.MsgCancelBinaryOptionsOrder":
        injective_exchange_tx_v2_pb.MsgCancelBinaryOptionsOrder,
    "/injective.exchange.v2.MsgAdminUpdateBinaryOptionsMarket":
        injective_exchange_tx_v2_pb.MsgAdminUpdateBinaryOptionsMarket,
    "/injective.exchange.v2.MsgInstantBinaryOptionsMarketLaunch":
        injective_exchange_tx_v2_pb.MsgInstantBinaryOptionsMarketLaunch,
}

GRPC_RESPONSE_TYPE_TO_CLASS_MAP = {
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
    "/injective.exchange.v2.MsgCreateSpotLimitOrderResponse":
        injective_exchange_tx_v2_pb.MsgCreateSpotLimitOrderResponse,
    "/injective.exchange.v2.MsgCreateSpotMarketOrderResponse":
        injective_exchange_tx_v2_pb.MsgCreateSpotMarketOrderResponse,
    "/injective.exchange.v2.MsgCreateDerivativeLimitOrderResponse":
        injective_exchange_tx_v2_pb.MsgCreateDerivativeLimitOrderResponse,
    "/injective.exchange.v2.MsgCreateDerivativeMarketOrderResponse":
        injective_exchange_tx_v2_pb.MsgCreateDerivativeMarketOrderResponse,
    "/injective.exchange.v2.MsgCancelSpotOrderResponse":
        injective_exchange_tx_v2_pb.MsgCancelSpotOrderResponse,
    "/injective.exchange.v2.MsgCancelDerivativeOrderResponse":
        injective_exchange_tx_v2_pb.MsgCancelDerivativeOrderResponse,
    "/injective.exchange.v2.MsgBatchCancelSpotOrdersResponse":
        injective_exchange_tx_v2_pb.MsgBatchCancelSpotOrdersResponse,
    "/injective.exchange.v2.MsgBatchCancelDerivativeOrdersResponse":
        injective_exchange_tx_v2_pb.MsgBatchCancelDerivativeOrdersResponse,
    "/injective.exchange.v2.MsgBatchCreateSpotLimitOrdersResponse":
        injective_exchange_tx_v2_pb.MsgBatchCreateSpotLimitOrdersResponse,
    "/injective.exchange.v2.MsgBatchCreateDerivativeLimitOrdersResponse":
        injective_exchange_tx_v2_pb.MsgBatchCreateDerivativeLimitOrdersResponse,
    "/injective.exchange.v2.MsgBatchUpdateOrdersResponse":
        injective_exchange_tx_v2_pb.MsgBatchUpdateOrdersResponse,
    "/injective.exchange.v2.MsgDepositResponse":
        injective_exchange_tx_v2_pb.MsgDepositResponse,
    "/injective.exchange.v2.MsgWithdrawResponse":
        injective_exchange_tx_v2_pb.MsgWithdrawResponse,
    "/injective.exchange.v2.MsgSubaccountTransferResponse":
        injective_exchange_tx_v2_pb.MsgSubaccountTransferResponse,
    "/injective.exchange.v2.MsgLiquidatePositionResponse":
        injective_exchange_tx_v2_pb.MsgLiquidatePositionResponse,
    "/injective.exchange.v2.MsgIncreasePositionMarginResponse":
        injective_exchange_tx_v2_pb.MsgIncreasePositionMarginResponse,
    "/injective.exchange.v2.MsgCreateBinaryOptionsLimitOrderResponse":
        injective_exchange_tx_v2_pb.MsgCreateBinaryOptionsLimitOrderResponse,
    "/injective.exchange.v2.MsgCreateBinaryOptionsMarketOrderResponse":
        injective_exchange_tx_v2_pb.MsgCreateBinaryOptionsMarketOrderResponse,
    "/injective.exchange.v2.MsgCancelBinaryOptionsOrderResponse":
        injective_exchange_tx_v2_pb.MsgCancelBinaryOptionsOrderResponse,
    "/injective.exchange.v2.MsgAdminUpdateBinaryOptionsMarketResponse":
        injective_exchange_tx_v2_pb.MsgAdminUpdateBinaryOptionsMarketResponse,
    "/injective.exchange.v2.MsgInstantBinaryOptionsMarketLaunchResponse":
        injective_exchange_tx_v2_pb.MsgInstantBinaryOptionsMarketLaunchResponse,
}

# fmt: on


class Composer:
    PERMISSIONS_ACTION = IntFlag(
        "PERMISSIONS_ACTION",
        [
            (permission_name, injective_permissions_pb.Action.Value(permission_name))
            for permission_name in injective_permissions_pb.Action.keys()
        ],
    )

    def __init__(self, network: str):
        """Composer is used to create the requests to send to the nodes using the Client

        :param network: the name of the network to use (mainnet, testnet, devnet)
        :type network: str
        """
        self.network = network
        self._ofac_checker = OfacChecker()

    def coin(self, amount: int, denom: str) -> base_coin_pb.Coin:
        """
        This method create an instance of Coin gRPC type, considering the amount is already expressed in chain format
        """
        formatted_amount_string = str(int(amount))
        return base_coin_pb.Coin(amount=formatted_amount_string, denom=denom)

    def order_data(
        self,
        market_id: str,
        subaccount_id: str,
        is_buy: bool,
        is_market_order: bool,
        is_conditional: bool,
        order_hash: Optional[str] = None,
        cid: Optional[str] = None,
    ) -> injective_exchange_tx_v2_pb.OrderData:
        order_mask = self._order_mask(is_conditional=is_conditional, is_buy=is_buy, is_market_order=is_market_order)

        return injective_exchange_tx_v2_pb.OrderData(
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hash=order_hash,
            order_mask=order_mask,
            cid=cid,
        )

    def order_data_without_mask(
        self,
        market_id: str,
        subaccount_id: str,
        order_hash: Optional[str] = None,
        cid: Optional[str] = None,
    ) -> injective_exchange_tx_v2_pb.OrderData:
        return injective_exchange_tx_v2_pb.OrderData(
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hash=order_hash,
            order_mask=1,
            cid=cid,
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
        expiration_block: Optional[int] = None,
    ) -> injective_order_v2_pb.SpotOrder:
        trigger_price = trigger_price or Decimal(0)
        expiration_block = expiration_block or 0
        chain_order_type = injective_order_v2_pb.OrderType.Value(order_type)
        chain_quantity = f"{Token.convert_value_to_extended_decimal_format(value=quantity).normalize():f}"
        chain_price = f"{Token.convert_value_to_extended_decimal_format(value=price).normalize():f}"
        chain_trigger_price = f"{Token.convert_value_to_extended_decimal_format(value=trigger_price).normalize():f}"

        return injective_order_v2_pb.SpotOrder(
            market_id=market_id,
            order_info=injective_order_v2_pb.OrderInfo(
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=chain_price,
                quantity=chain_quantity,
                cid=cid,
            ),
            order_type=chain_order_type,
            trigger_price=chain_trigger_price,
            expiration_block=expiration_block,
        )

    def calculate_margin(
        self, quantity: Decimal, price: Decimal, leverage: Decimal, is_reduce_only: bool = False
    ) -> Decimal:
        if is_reduce_only:
            margin = Decimal(0)
        else:
            margin = quantity * price / leverage

        return margin

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
        expiration_block: Optional[int] = None,
    ) -> injective_order_v2_pb.DerivativeOrder:
        return self._basic_derivative_order(
            market_id=market_id,
            subaccount_id=subaccount_id,
            fee_recipient=fee_recipient,
            price=price,
            quantity=quantity,
            margin=margin,
            order_type=order_type,
            cid=cid,
            trigger_price=trigger_price,
            expiration_block=expiration_block,
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
        expiration_block: Optional[int] = None,
    ) -> injective_order_v2_pb.DerivativeOrder:
        return self._basic_derivative_order(
            market_id=market_id,
            subaccount_id=subaccount_id,
            fee_recipient=fee_recipient,
            price=price,
            quantity=quantity,
            margin=margin,
            order_type=order_type,
            cid=cid,
            trigger_price=trigger_price,
            expiration_block=expiration_block,
        )

    def create_grant_authorization(self, grantee: str, amount: Decimal) -> injective_exchange_v2_pb.GrantAuthorization:
        chain_formatted_amount = int(amount * Decimal(f"1e{INJ_DECIMALS}"))
        return injective_exchange_v2_pb.GrantAuthorization(grantee=grantee, amount=str(chain_formatted_amount))

    # region Auction module
    def msg_bid(self, sender: str, bid_amount: float, round: float) -> injective_auction_tx_pb.MsgBid:
        be_amount = Token.convert_value_to_extended_decimal_format(value=Decimal(str(bid_amount)))

        return injective_auction_tx_pb.MsgBid(
            sender=sender,
            round=round,
            bid_amount=self.coin(amount=int(be_amount), denom=INJ_DENOM),
        )

    # endregion

    # region Authz module
    def msg_grant_generic(
        self, granter: str, grantee: str, msg_type: str, expire_in: int
    ) -> cosmos_authz_tx_pb.MsgGrant:
        if self._ofac_checker.is_blacklisted(granter):
            raise Exception(f"Address {granter} is in the OFAC list")
        auth = cosmos_authz_pb.GenericAuthorization(msg=msg_type)
        any_auth = any_pb2.Any()
        any_auth.Pack(auth, type_url_prefix="")

        grant = cosmos_authz_pb.Grant(
            authorization=any_auth,
            expiration=timestamp_pb2.Timestamp(seconds=(int(time()) + expire_in)),
        )

        return cosmos_authz_tx_pb.MsgGrant(granter=granter, grantee=grantee, grant=grant)

    def msg_exec(self, grantee: str, msgs: List):
        any_msgs: List[any_pb2.Any] = []
        for msg in msgs:
            any_msg = any_pb2.Any()
            any_msg.Pack(msg, type_url_prefix="")
            any_msgs.append(any_msg)

        return cosmos_authz_tx_pb.MsgExec(grantee=grantee, msgs=any_msgs)

    def msg_revoke(self, granter: str, grantee: str, msg_type: str) -> cosmos_authz_tx_pb.MsgRevoke:
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
    def msg_send(self, from_address: str, to_address: str, amount: int, denom: str):
        coin = self.coin(amount=int(amount), denom=denom)

        return cosmos_bank_tx_pb.MsgSend(
            from_address=from_address,
            to_address=to_address,
            amount=[coin],
        )

    # endregion

    # region Chain Exchange module
    def msg_deposit(
        self, sender: str, subaccount_id: str, amount: int, denom: str
    ) -> injective_exchange_tx_v2_pb.MsgDeposit:
        coin = self.coin(amount=int(amount), denom=denom)

        return injective_exchange_tx_v2_pb.MsgDeposit(
            sender=sender,
            subaccount_id=subaccount_id,
            amount=coin,
        )

    def msg_withdraw(
        self,
        sender: str,
        subaccount_id: str,
        amount: int,
        denom: str,
    ) -> injective_exchange_tx_v2_pb.MsgWithdraw:
        coin = self.coin(amount=int(amount), denom=denom)

        return injective_exchange_tx_v2_pb.MsgWithdraw(
            sender=sender,
            subaccount_id=subaccount_id,
            amount=coin,
        )

    def msg_instant_spot_market_launch(
        self,
        sender: str,
        ticker: str,
        base_denom: str,
        quote_denom: str,
        min_price_tick_size: Decimal,
        min_quantity_tick_size: Decimal,
        min_notional: Decimal,
        base_decimals: int,
        quote_decimals: int,
    ) -> injective_exchange_tx_v2_pb.MsgInstantSpotMarketLaunch:
        chain_min_price_tick_size = (
            f"{Token.convert_value_to_extended_decimal_format(value=min_price_tick_size).normalize():f}"
        )
        chain_min_quantity_tick_size = (
            f"{Token.convert_value_to_extended_decimal_format(value=min_quantity_tick_size).normalize():f}"
        )
        chain_min_notional = f"{Token.convert_value_to_extended_decimal_format(value=min_notional).normalize():f}"

        return injective_exchange_tx_v2_pb.MsgInstantSpotMarketLaunch(
            sender=sender,
            ticker=ticker,
            base_denom=base_denom,
            quote_denom=quote_denom,
            min_price_tick_size=chain_min_price_tick_size,
            min_quantity_tick_size=chain_min_quantity_tick_size,
            min_notional=chain_min_notional,
            base_decimals=base_decimals,
            quote_decimals=quote_decimals,
        )

    def msg_instant_perpetual_market_launch_v2(
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
        reduce_margin_ratio: Decimal,
        min_price_tick_size: Decimal,
        min_quantity_tick_size: Decimal,
        min_notional: Decimal,
    ) -> injective_exchange_tx_v2_pb.MsgInstantPerpetualMarketLaunch:
        chain_min_price_tick_size = Token.convert_value_to_extended_decimal_format(value=min_price_tick_size)
        chain_min_quantity_tick_size = Token.convert_value_to_extended_decimal_format(value=min_quantity_tick_size)
        chain_maker_fee_rate = Token.convert_value_to_extended_decimal_format(value=maker_fee_rate)
        chain_taker_fee_rate = Token.convert_value_to_extended_decimal_format(value=taker_fee_rate)
        chain_initial_margin_ratio = Token.convert_value_to_extended_decimal_format(value=initial_margin_ratio)
        chain_maintenance_margin_ratio = Token.convert_value_to_extended_decimal_format(value=maintenance_margin_ratio)
        chain_reduce_margin_ratio = Token.convert_value_to_extended_decimal_format(value=reduce_margin_ratio)
        chain_min_notional = Token.convert_value_to_extended_decimal_format(value=min_notional)

        return injective_exchange_tx_v2_pb.MsgInstantPerpetualMarketLaunch(
            sender=sender,
            ticker=ticker,
            quote_denom=quote_denom,
            oracle_base=oracle_base,
            oracle_quote=oracle_quote,
            oracle_scale_factor=oracle_scale_factor,
            oracle_type=injective_oracle_pb.OracleType.Value(oracle_type),
            maker_fee_rate=f"{chain_maker_fee_rate.normalize():f}",
            taker_fee_rate=f"{chain_taker_fee_rate.normalize():f}",
            initial_margin_ratio=f"{chain_initial_margin_ratio.normalize():f}",
            maintenance_margin_ratio=f"{chain_maintenance_margin_ratio.normalize():f}",
            reduce_margin_ratio=f"{chain_reduce_margin_ratio.normalize():f}",
            min_price_tick_size=f"{chain_min_price_tick_size.normalize():f}",
            min_quantity_tick_size=f"{chain_min_quantity_tick_size.normalize():f}",
            min_notional=f"{chain_min_notional.normalize():f}",
        )

    def msg_instant_expiry_futures_market_launch_v2(
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
        reduce_margin_ratio: Decimal,
        min_price_tick_size: Decimal,
        min_quantity_tick_size: Decimal,
        min_notional: Decimal,
    ) -> injective_exchange_tx_v2_pb.MsgInstantPerpetualMarketLaunch:
        chain_min_price_tick_size = Token.convert_value_to_extended_decimal_format(value=min_price_tick_size)
        chain_min_quantity_tick_size = Token.convert_value_to_extended_decimal_format(value=min_quantity_tick_size)
        chain_maker_fee_rate = Token.convert_value_to_extended_decimal_format(value=maker_fee_rate)
        chain_taker_fee_rate = Token.convert_value_to_extended_decimal_format(value=taker_fee_rate)
        chain_initial_margin_ratio = Token.convert_value_to_extended_decimal_format(value=initial_margin_ratio)
        chain_maintenance_margin_ratio = Token.convert_value_to_extended_decimal_format(value=maintenance_margin_ratio)
        chain_reduce_margin_ratio = Token.convert_value_to_extended_decimal_format(value=reduce_margin_ratio)
        chain_min_notional = Token.convert_value_to_extended_decimal_format(value=min_notional)

        return injective_exchange_tx_v2_pb.MsgInstantExpiryFuturesMarketLaunch(
            sender=sender,
            ticker=ticker,
            quote_denom=quote_denom,
            oracle_base=oracle_base,
            oracle_quote=oracle_quote,
            oracle_scale_factor=oracle_scale_factor,
            oracle_type=injective_oracle_pb.OracleType.Value(oracle_type),
            expiry=expiry,
            maker_fee_rate=f"{chain_maker_fee_rate.normalize():f}",
            taker_fee_rate=f"{chain_taker_fee_rate.normalize():f}",
            initial_margin_ratio=f"{chain_initial_margin_ratio.normalize():f}",
            maintenance_margin_ratio=f"{chain_maintenance_margin_ratio.normalize():f}",
            reduce_margin_ratio=f"{chain_reduce_margin_ratio.normalize():f}",
            min_price_tick_size=f"{chain_min_price_tick_size.normalize():f}",
            min_quantity_tick_size=f"{chain_min_quantity_tick_size.normalize():f}",
            min_notional=f"{chain_min_notional.normalize():f}",
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
        expiration_block: Optional[int] = None,
    ) -> injective_exchange_tx_v2_pb.MsgCreateSpotLimitOrder:
        return injective_exchange_tx_v2_pb.MsgCreateSpotLimitOrder(
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
                expiration_block=expiration_block,
            ),
        )

    def msg_batch_create_spot_limit_orders(
        self, sender: str, orders: List[injective_order_v2_pb.SpotOrder]
    ) -> injective_exchange_tx_v2_pb.MsgBatchCreateSpotLimitOrders:
        return injective_exchange_tx_v2_pb.MsgBatchCreateSpotLimitOrders(sender=sender, orders=orders)

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
    ) -> injective_exchange_tx_v2_pb.MsgCreateSpotMarketOrder:
        return injective_exchange_tx_v2_pb.MsgCreateSpotMarketOrder(
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

    def msg_cancel_spot_order(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        order_hash: Optional[str] = None,
        cid: Optional[str] = None,
    ) -> injective_exchange_tx_v2_pb.MsgCancelSpotOrder:
        return injective_exchange_tx_v2_pb.MsgCancelSpotOrder(
            sender=sender,
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hash=order_hash,
            cid=cid,
        )

    def msg_batch_cancel_spot_orders(
        self, sender: str, orders_data: List[injective_exchange_tx_v2_pb.OrderData]
    ) -> injective_exchange_tx_v2_pb.MsgBatchCancelSpotOrders:
        return injective_exchange_tx_v2_pb.MsgBatchCancelSpotOrders(sender=sender, data=orders_data)

    def msg_batch_update_orders(
        self,
        sender: str,
        subaccount_id: Optional[str] = None,
        spot_market_ids_to_cancel_all: Optional[List[str]] = None,
        derivative_market_ids_to_cancel_all: Optional[List[str]] = None,
        spot_orders_to_cancel: Optional[List[injective_exchange_tx_v2_pb.OrderData]] = None,
        derivative_orders_to_cancel: Optional[List[injective_exchange_tx_v2_pb.OrderData]] = None,
        spot_orders_to_create: Optional[List[injective_order_v2_pb.SpotOrder]] = None,
        derivative_orders_to_create: Optional[List[injective_order_v2_pb.DerivativeOrder]] = None,
        binary_options_orders_to_cancel: Optional[List[injective_exchange_tx_v2_pb.OrderData]] = None,
        binary_options_market_ids_to_cancel_all: Optional[List[str]] = None,
        binary_options_orders_to_create: Optional[List[injective_order_v2_pb.DerivativeOrder]] = None,
    ) -> injective_exchange_tx_v2_pb.MsgBatchUpdateOrders:
        return injective_exchange_tx_v2_pb.MsgBatchUpdateOrders(
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

    def msg_privileged_execute_contract(
        self,
        sender: str,
        contract_address: str,
        data: str,
        funds: Optional[str] = None,
    ) -> injective_exchange_tx_v2_pb.MsgPrivilegedExecuteContract:
        return injective_exchange_tx_v2_pb.MsgPrivilegedExecuteContract(
            sender=sender,
            contract_address=contract_address,
            data=data,
            funds=funds,
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
        expiration_block: Optional[int] = None,
    ) -> injective_exchange_tx_v2_pb.MsgCreateDerivativeLimitOrder:
        return injective_exchange_tx_v2_pb.MsgCreateDerivativeLimitOrder(
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
                expiration_block=expiration_block,
            ),
        )

    def msg_batch_create_derivative_limit_orders(
        self,
        sender: str,
        orders: List[injective_order_v2_pb.DerivativeOrder],
    ) -> injective_exchange_tx_v2_pb.MsgBatchCreateDerivativeLimitOrders:
        return injective_exchange_tx_v2_pb.MsgBatchCreateDerivativeLimitOrders(sender=sender, orders=orders)

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
    ) -> injective_exchange_tx_v2_pb.MsgCreateDerivativeMarketOrder:
        return injective_exchange_tx_v2_pb.MsgCreateDerivativeMarketOrder(
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

    def msg_cancel_derivative_order(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        is_buy: bool,
        is_market_order: bool,
        is_conditional: bool,
        order_hash: Optional[str] = None,
        cid: Optional[str] = None,
    ) -> injective_exchange_tx_v2_pb.MsgCancelDerivativeOrder:
        order_mask = self._order_mask(is_conditional=is_conditional, is_buy=is_buy, is_market_order=is_market_order)

        return injective_exchange_tx_v2_pb.MsgCancelDerivativeOrder(
            sender=sender,
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hash=order_hash,
            order_mask=order_mask,
            cid=cid,
        )

    def msg_batch_cancel_derivative_orders(
        self, sender: str, orders_data: List[injective_exchange_tx_v2_pb.OrderData]
    ) -> injective_exchange_tx_v2_pb.MsgBatchCancelDerivativeOrders:
        return injective_exchange_tx_v2_pb.MsgBatchCancelDerivativeOrders(sender=sender, data=orders_data)

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
        min_notional: Decimal,
    ) -> injective_exchange_tx_v2_pb.MsgInstantPerpetualMarketLaunch:
        chain_min_price_tick_size = Token.convert_value_to_extended_decimal_format(value=min_price_tick_size)
        chain_min_quantity_tick_size = Token.convert_value_to_extended_decimal_format(value=min_quantity_tick_size)
        chain_maker_fee_rate = Token.convert_value_to_extended_decimal_format(value=maker_fee_rate)
        chain_taker_fee_rate = Token.convert_value_to_extended_decimal_format(value=taker_fee_rate)
        chain_min_notional = Token.convert_value_to_extended_decimal_format(value=min_notional)

        return injective_exchange_tx_v2_pb.MsgInstantBinaryOptionsMarketLaunch(
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
            quote_denom=quote_denom,
            min_price_tick_size=f"{chain_min_price_tick_size.normalize():f}",
            min_quantity_tick_size=f"{chain_min_quantity_tick_size.normalize():f}",
            min_notional=f"{chain_min_notional.normalize():f}",
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
        expiration_block: Optional[int] = None,
    ) -> injective_exchange_tx_v2_pb.MsgCreateDerivativeLimitOrder:
        return injective_exchange_tx_v2_pb.MsgCreateDerivativeLimitOrder(
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
                expiration_block=expiration_block,
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
    ) -> injective_exchange_tx_v2_pb.MsgCreateBinaryOptionsMarketOrder:
        return injective_exchange_tx_v2_pb.MsgCreateBinaryOptionsMarketOrder(
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
            ),
        )

    def msg_cancel_binary_options_order(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        is_buy: bool,
        is_market_order: bool,
        is_conditional: bool,
        order_hash: Optional[str] = None,
        cid: Optional[str] = None,
    ) -> injective_exchange_tx_v2_pb.MsgCancelBinaryOptionsOrder:
        order_mask = self._order_mask(is_conditional=is_conditional, is_buy=is_buy, is_market_order=is_market_order)

        return injective_exchange_tx_v2_pb.MsgCancelBinaryOptionsOrder(
            sender=sender,
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hash=order_hash,
            order_mask=order_mask,
            cid=cid,
        )

    def msg_subaccount_transfer(
        self,
        sender: str,
        source_subaccount_id: str,
        destination_subaccount_id: str,
        amount: int,
        denom: str,
    ) -> injective_exchange_tx_v2_pb.MsgSubaccountTransfer:
        amount_coin = self.coin(amount=int(amount), denom=denom)

        return injective_exchange_tx_v2_pb.MsgSubaccountTransfer(
            sender=sender,
            source_subaccount_id=source_subaccount_id,
            destination_subaccount_id=destination_subaccount_id,
            amount=amount_coin,
        )

    def msg_external_transfer(
        self,
        sender: str,
        source_subaccount_id: str,
        destination_subaccount_id: str,
        amount: int,
        denom: str,
    ) -> injective_exchange_tx_v2_pb.MsgExternalTransfer:
        coin = self.coin(amount=int(amount), denom=denom)

        return injective_exchange_tx_v2_pb.MsgExternalTransfer(
            sender=sender,
            source_subaccount_id=source_subaccount_id,
            destination_subaccount_id=destination_subaccount_id,
            amount=coin,
        )

    def msg_liquidate_position(
        self,
        sender: str,
        subaccount_id: str,
        market_id: str,
        order: Optional[injective_order_v2_pb.DerivativeOrder] = None,
    ) -> injective_exchange_tx_v2_pb.MsgLiquidatePosition:
        return injective_exchange_tx_v2_pb.MsgLiquidatePosition(
            sender=sender, subaccount_id=subaccount_id, market_id=market_id, order=order
        )

    def msg_emergency_settle_market(
        self,
        sender: str,
        subaccount_id: str,
        market_id: str,
    ) -> injective_exchange_tx_v2_pb.MsgEmergencySettleMarket:
        return injective_exchange_tx_v2_pb.MsgEmergencySettleMarket(
            sender=sender, subaccount_id=subaccount_id, market_id=market_id
        )

    def msg_increase_position_margin(
        self,
        sender: str,
        source_subaccount_id: str,
        destination_subaccount_id: str,
        market_id: str,
        amount: Decimal,
    ) -> injective_exchange_tx_v2_pb.MsgIncreasePositionMargin:
        additional_margin = Token.convert_value_to_extended_decimal_format(value=amount)
        return injective_exchange_tx_v2_pb.MsgIncreasePositionMargin(
            sender=sender,
            source_subaccount_id=source_subaccount_id,
            destination_subaccount_id=destination_subaccount_id,
            market_id=market_id,
            amount=str(int(additional_margin)),
        )

    def msg_rewards_opt_out(self, sender: str) -> injective_exchange_tx_v2_pb.MsgRewardsOptOut:
        return injective_exchange_tx_v2_pb.MsgRewardsOptOut(sender=sender)

    def msg_admin_update_binary_options_market(
        self,
        sender: str,
        market_id: str,
        status: str,
        settlement_price: Optional[Decimal] = None,
        expiration_timestamp: Optional[int] = None,
        settlement_timestamp: Optional[int] = None,
    ) -> injective_exchange_tx_v2_pb.MsgAdminUpdateBinaryOptionsMarket:
        message = injective_exchange_tx_v2_pb.MsgAdminUpdateBinaryOptionsMarket(
            sender=sender,
            market_id=market_id,
            expiration_timestamp=expiration_timestamp,
            settlement_timestamp=settlement_timestamp,
            status=status,
        )

        if settlement_price is not None:
            chain_settlement_price = Token.convert_value_to_extended_decimal_format(value=settlement_price)
            message.settlement_price = f"{chain_settlement_price.normalize():f}"

        return message

    def msg_decrease_position_margin(
        self,
        sender: str,
        source_subaccount_id: str,
        destination_subaccount_id: str,
        market_id: str,
        amount: Decimal,
    ) -> injective_exchange_tx_v2_pb.MsgDecreasePositionMargin:
        margin_to_remove = Token.convert_value_to_extended_decimal_format(value=amount)
        return injective_exchange_tx_v2_pb.MsgDecreasePositionMargin(
            sender=sender,
            source_subaccount_id=source_subaccount_id,
            destination_subaccount_id=destination_subaccount_id,
            market_id=market_id,
            amount=f"{margin_to_remove.normalize():f}",
        )

    def msg_update_spot_market(
        self,
        admin: str,
        market_id: str,
        new_ticker: str,
        new_min_price_tick_size: Decimal,
        new_min_quantity_tick_size: Decimal,
        new_min_notional: Decimal,
    ) -> injective_exchange_tx_v2_pb.MsgUpdateSpotMarket:
        chain_min_price_tick_size = Token.convert_value_to_extended_decimal_format(value=new_min_price_tick_size)
        chain_min_quantity_tick_size = Token.convert_value_to_extended_decimal_format(value=new_min_quantity_tick_size)
        chain_min_notional = Token.convert_value_to_extended_decimal_format(value=new_min_notional)

        return injective_exchange_tx_v2_pb.MsgUpdateSpotMarket(
            admin=admin,
            market_id=market_id,
            new_ticker=new_ticker,
            new_min_price_tick_size=f"{chain_min_price_tick_size.normalize():f}",
            new_min_quantity_tick_size=f"{chain_min_quantity_tick_size.normalize():f}",
            new_min_notional=f"{chain_min_notional.normalize():f}",
        )

    def msg_update_derivative_market(
        self,
        admin: str,
        market_id: str,
        new_ticker: str,
        new_min_price_tick_size: Decimal,
        new_min_quantity_tick_size: Decimal,
        new_min_notional: Decimal,
        new_initial_margin_ratio: Decimal,
        new_maintenance_margin_ratio: Decimal,
        new_reduce_margin_ratio: Decimal,
    ) -> injective_exchange_tx_v2_pb.MsgUpdateDerivativeMarket:
        chain_min_price_tick_size = Token.convert_value_to_extended_decimal_format(value=new_min_price_tick_size)
        chain_min_quantity_tick_size = Token.convert_value_to_extended_decimal_format(value=new_min_quantity_tick_size)
        chain_min_notional = Token.convert_value_to_extended_decimal_format(value=new_min_notional)
        chain_initial_margin_ratio = Token.convert_value_to_extended_decimal_format(value=new_initial_margin_ratio)
        chain_maintenance_margin_ratio = Token.convert_value_to_extended_decimal_format(
            value=new_maintenance_margin_ratio
        )
        chain_reduce_margin_ratio = Token.convert_value_to_extended_decimal_format(value=new_reduce_margin_ratio)

        return injective_exchange_tx_v2_pb.MsgUpdateDerivativeMarket(
            admin=admin,
            market_id=market_id,
            new_ticker=new_ticker,
            new_min_price_tick_size=f"{chain_min_price_tick_size.normalize():f}",
            new_min_quantity_tick_size=f"{chain_min_quantity_tick_size.normalize():f}",
            new_min_notional=f"{chain_min_notional.normalize():f}",
            new_initial_margin_ratio=f"{chain_initial_margin_ratio.normalize():f}",
            new_maintenance_margin_ratio=f"{chain_maintenance_margin_ratio.normalize():f}",
            new_reduce_margin_ratio=f"{chain_reduce_margin_ratio.normalize():f}",
        )

    def msg_authorize_stake_grants(
        self, sender: str, grants: List[injective_exchange_v2_pb.GrantAuthorization]
    ) -> injective_exchange_tx_v2_pb.MsgAuthorizeStakeGrants:
        return injective_exchange_tx_v2_pb.MsgAuthorizeStakeGrants(
            sender=sender,
            grants=grants,
        )

    def msg_activate_stake_grant(self, sender: str, granter: str) -> injective_exchange_tx_v2_pb.MsgActivateStakeGrant:
        return injective_exchange_tx_v2_pb.MsgActivateStakeGrant(
            sender=sender,
            granter=granter,
        )

    # endregion

    # region Insurance module
    def msg_create_insurance_fund(
        self,
        sender: str,
        ticker: str,
        quote_denom: str,
        oracle_base: str,
        oracle_quote: str,
        oracle_type: str,
        expiry: int,
        initial_deposit: int,
    ) -> injective_insurance_tx_pb.MsgCreateInsuranceFund:
        deposit = self.coin(amount=int(initial_deposit), denom=quote_denom)

        return injective_insurance_tx_pb.MsgCreateInsuranceFund(
            sender=sender,
            ticker=ticker,
            quote_denom=quote_denom,
            oracle_base=oracle_base,
            oracle_quote=oracle_quote,
            oracle_type=injective_oracle_pb.OracleType.Value(oracle_type),
            expiry=expiry,
            initial_deposit=deposit,
        )

    def msg_underwrite(
        self,
        sender: str,
        market_id: str,
        quote_denom: str,
        amount: int,
    ):
        coin = self.coin(amount=int(amount), denom=quote_denom)

        return injective_insurance_tx_pb.MsgUnderwrite(
            sender=sender,
            market_id=market_id,
            deposit=coin,
        )

    def msg_request_redemption(
        self,
        sender: str,
        market_id: str,
        share_denom: str,
        amount: int,
    ) -> injective_insurance_tx_pb.MsgRequestRedemption:
        chain_amount = Token.convert_value_to_extended_decimal_format(value=Decimal(str(amount)))

        return injective_insurance_tx_pb.MsgRequestRedemption(
            sender=sender,
            market_id=market_id,
            amount=self.coin(amount=int(chain_amount), denom=share_denom),
        )

    # endregion

    # region Oracle module
    def msg_relay_provider_prices(
        self, sender: str, provider: str, symbols: list, prices: list
    ) -> injective_oracle_tx_pb.MsgRelayProviderPrices:
        oracle_prices = []

        for price in prices:
            scale_price = Decimal(price * pow(10, 18))
            price_to_bytes = bytes(str(scale_price), "utf-8")
            oracle_prices.append(price_to_bytes)

        return injective_oracle_tx_pb.MsgRelayProviderPrices(
            sender=sender, provider=provider, symbols=symbols, prices=oracle_prices
        )

    def msg_relay_price_feed_price(
        self, sender: list, base: list, quote: list, price: list
    ) -> injective_oracle_tx_pb.MsgRelayPriceFeedPrice:
        return injective_oracle_tx_pb.MsgRelayPriceFeedPrice(sender=sender, base=base, quote=quote, price=price)

    # endregion

    # region Peggy module
    def msg_send_to_eth(self, denom: str, sender: str, eth_dest: str, amount: int, bridge_fee: int):
        amount_coin = self.coin(amount=int(amount), denom=denom)
        bridge_fee_coin = self.coin(amount=int(bridge_fee), denom=denom)

        return injective_peggy_tx_pb.MsgSendToEth(
            sender=sender,
            eth_dest=eth_dest,
            amount=amount_coin,
            bridge_fee=bridge_fee_coin,
        )

    # endregion

    # region Staking module
    def msg_delegate(
        self, delegator_address: str, validator_address: str, amount: float
    ) -> cosmos_staking_tx_pb.MsgDelegate:
        be_amount = Token.convert_value_to_extended_decimal_format(Decimal(str(amount)))

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
        decimals: int,
        allow_admin_burn: bool,
    ) -> token_factory_tx_pb.MsgCreateDenom:
        return token_factory_tx_pb.MsgCreateDenom(
            sender=sender,
            subdenom=subdenom,
            name=name,
            symbol=symbol,
            decimals=decimals,
            allow_admin_burn=allow_admin_burn,
        )

    def msg_mint(
        self,
        sender: str,
        amount: base_coin_pb.Coin,
        receiver: str,
    ) -> token_factory_tx_pb.MsgMint:
        return token_factory_tx_pb.MsgMint(sender=sender, amount=amount, receiver=receiver)

    def msg_burn(
        self,
        sender: str,
        amount: base_coin_pb.Coin,
        burn_from_address: str,
    ) -> token_factory_tx_pb.MsgBurn:
        return token_factory_tx_pb.MsgBurn(sender=sender, amount=amount, burnFromAddress=burn_from_address)

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
            decimals=token_decimals,
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
    def msg_instantiate_contract(
        self,
        sender: str,
        admin: str,
        code_id: int,
        label: str,
        message: bytes,
        funds: Optional[List[base_coin_pb.Coin]] = None,
    ) -> wasm_tx_pb.MsgInstantiateContract:
        return wasm_tx_pb.MsgInstantiateContract(
            sender=sender,
            admin=admin,
            code_id=code_id,
            label=label,
            msg=message,
            funds=funds,  # The coins in the list must be sorted in alphabetical order by denoms.
        )

    def msg_execute_contract(
        self, sender: str, contract: str, msg: str, funds: Optional[List[base_coin_pb.Coin]] = None
    ):
        return wasm_tx_pb.MsgExecuteContract(
            sender=sender,
            contract=contract,
            msg=bytes(msg, "utf-8"),
            funds=funds,  # The coins in the list must be sorted in alphabetical order by denoms.
        )

    # endregion

    def msg_grant_typed(
        self,
        granter: str,
        grantee: str,
        msg_type: str,
        expiration_time_seconds: int,
        subaccount_id: str,
        market_ids: Optional[List[str]] = None,
        spot_markets: Optional[List[str]] = None,
        derivative_markets: Optional[List[str]] = None,
    ) -> cosmos_authz_tx_pb.MsgGrant:
        if self._ofac_checker.is_blacklisted(granter):
            raise Exception(f"Address {granter} is in the OFAC list")

        market_ids = market_ids or []
        auth = None
        if msg_type == "CreateSpotLimitOrderAuthz":
            auth = injective_authz_v2_pb.CreateSpotLimitOrderAuthz(subaccount_id=subaccount_id, market_ids=market_ids)
        elif msg_type == "CreateSpotMarketOrderAuthz":
            auth = injective_authz_v2_pb.CreateSpotMarketOrderAuthz(subaccount_id=subaccount_id, market_ids=market_ids)
        elif msg_type == "BatchCreateSpotLimitOrdersAuthz":
            auth = injective_authz_v2_pb.BatchCreateSpotLimitOrdersAuthz(
                subaccount_id=subaccount_id, market_ids=market_ids
            )
        elif msg_type == "CancelSpotOrderAuthz":
            auth = injective_authz_v2_pb.CancelSpotOrderAuthz(subaccount_id=subaccount_id, market_ids=market_ids)
        elif msg_type == "BatchCancelSpotOrdersAuthz":
            auth = injective_authz_v2_pb.BatchCancelSpotOrdersAuthz(subaccount_id=subaccount_id, market_ids=market_ids)
        elif msg_type == "CreateDerivativeLimitOrderAuthz":
            auth = injective_authz_v2_pb.CreateDerivativeLimitOrderAuthz(
                subaccount_id=subaccount_id, market_ids=market_ids
            )
        elif msg_type == "CreateDerivativeMarketOrderAuthz":
            auth = injective_authz_v2_pb.CreateDerivativeMarketOrderAuthz(
                subaccount_id=subaccount_id, market_ids=market_ids
            )
        elif msg_type == "BatchCreateDerivativeLimitOrdersAuthz":
            auth = injective_authz_v2_pb.BatchCreateDerivativeLimitOrdersAuthz(
                subaccount_id=subaccount_id, market_ids=market_ids
            )
        elif msg_type == "CancelDerivativeOrderAuthz":
            auth = injective_authz_v2_pb.CancelDerivativeOrderAuthz(subaccount_id=subaccount_id, market_ids=market_ids)
        elif msg_type == "BatchCancelDerivativeOrdersAuthz":
            auth = injective_authz_v2_pb.BatchCancelDerivativeOrdersAuthz(
                subaccount_id=subaccount_id, market_ids=market_ids
            )
        elif msg_type == "BatchUpdateOrdersAuthz":
            spot_markets_ids = spot_markets or []
            derivative_markets_ids = derivative_markets or []

            auth = injective_authz_v2_pb.BatchUpdateOrdersAuthz(
                subaccount_id=subaccount_id,
                spot_markets=spot_markets_ids,
                derivative_markets=derivative_markets_ids,
            )

        any_auth = any_pb2.Any()
        any_auth.Pack(auth, type_url_prefix="")

        grant = cosmos_authz_pb.Grant(
            authorization=any_auth,
            expiration=timestamp_pb2.Timestamp(seconds=(int(time()) + expiration_time_seconds)),
        )

        return cosmos_authz_tx_pb.MsgGrant(granter=granter, grantee=grantee, grant=grant)

    def msg_vote(
        self,
        proposal_id: int,
        voter: str,
        option: int,
    ) -> cosmos_gov_tx_pb.MsgVote:
        return cosmos_gov_tx_pb.MsgVote(proposal_id=proposal_id, voter=voter, option=option)

    # ------------------------------------------------
    # region Chain stream module's messages

    def chain_stream_bank_balances_filter(
        self, accounts: Optional[List[str]] = None
    ) -> chain_stream_v2_query.BankBalancesFilter:
        accounts = accounts or ["*"]
        return chain_stream_v2_query.BankBalancesFilter(accounts=accounts)

    def chain_stream_subaccount_deposits_filter(
        self,
        subaccount_ids: Optional[List[str]] = None,
    ) -> chain_stream_v2_query.SubaccountDepositsFilter:
        subaccount_ids = subaccount_ids or ["*"]
        return chain_stream_v2_query.SubaccountDepositsFilter(subaccount_ids=subaccount_ids)

    def chain_stream_trades_filter(
        self,
        subaccount_ids: Optional[List[str]] = None,
        market_ids: Optional[List[str]] = None,
    ) -> chain_stream_v2_query.TradesFilter:
        subaccount_ids = subaccount_ids or ["*"]
        market_ids = market_ids or ["*"]
        return chain_stream_v2_query.TradesFilter(subaccount_ids=subaccount_ids, market_ids=market_ids)

    def chain_stream_orders_filter(
        self,
        subaccount_ids: Optional[List[str]] = None,
        market_ids: Optional[List[str]] = None,
    ) -> chain_stream_v2_query.OrdersFilter:
        subaccount_ids = subaccount_ids or ["*"]
        market_ids = market_ids or ["*"]
        return chain_stream_v2_query.OrdersFilter(subaccount_ids=subaccount_ids, market_ids=market_ids)

    def chain_stream_orderbooks_filter(
        self,
        market_ids: Optional[List[str]] = None,
    ) -> chain_stream_v2_query.OrderbookFilter:
        market_ids = market_ids or ["*"]
        return chain_stream_v2_query.OrderbookFilter(market_ids=market_ids)

    def chain_stream_positions_filter(
        self,
        subaccount_ids: Optional[List[str]] = None,
        market_ids: Optional[List[str]] = None,
    ) -> chain_stream_v2_query.PositionsFilter:
        subaccount_ids = subaccount_ids or ["*"]
        market_ids = market_ids or ["*"]
        return chain_stream_v2_query.PositionsFilter(subaccount_ids=subaccount_ids, market_ids=market_ids)

    def chain_stream_oracle_price_filter(
        self,
        symbols: Optional[List[str]] = None,
    ) -> chain_stream_v2_query.PositionsFilter:
        symbols = symbols or ["*"]
        return chain_stream_v2_query.OraclePriceFilter(symbol=symbols)

    # endregion

    # ------------------------------------------------
    # region Distribution module's messages

    def msg_set_withdraw_address(self, delegator_address: str, withdraw_address: str):
        return cosmos_distribution_tx_pb.MsgSetWithdrawAddress(
            delegator_address=delegator_address, withdraw_address=withdraw_address
        )

    def msg_withdraw_delegator_reward(self, delegator_address: str, validator_address: str):
        return cosmos_distribution_tx_pb.MsgWithdrawDelegatorReward(
            delegator_address=delegator_address, validator_address=validator_address
        )

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

    # endregion

    # region IBC Transfer module
    def msg_ibc_transfer(
        self,
        source_port: str,
        source_channel: str,
        token_amount: base_coin_pb.Coin,
        sender: str,
        receiver: str,
        timeout_height: Optional[int] = None,
        timeout_timestamp: Optional[int] = None,
        memo: Optional[str] = None,
    ) -> ibc_transfer_tx_pb.MsgTransfer:
        if timeout_height is None and timeout_timestamp is None:
            raise ValueError("IBC Transfer error: Either timeout_height or timeout_timestamp must be provided")
        parsed_timeout_height = None
        if timeout_height:
            parsed_timeout_height = ibc_core_client_pb.Height(
                revision_number=timeout_height, revision_height=timeout_height
            )
        return ibc_transfer_tx_pb.MsgTransfer(
            source_port=source_port,
            source_channel=source_channel,
            token=token_amount,
            sender=sender,
            receiver=receiver,
            timeout_height=parsed_timeout_height,
            timeout_timestamp=timeout_timestamp,
            memo=memo,
        )

    # endregion

    # region Permissions module
    def permissions_role(self, name: str, role_id: int, permissions: int) -> injective_permissions_pb.Role:
        return injective_permissions_pb.Role(name=name, role_id=role_id, permissions=permissions)

    def permissions_actor_roles(self, actor: str, roles: List[str]) -> injective_permissions_pb.ActorRoles:
        return injective_permissions_pb.ActorRoles(actor=actor, roles=roles)

    def permissions_role_manager(self, manager: str, roles: List[str]) -> injective_permissions_pb.RoleManager:
        return injective_permissions_pb.RoleManager(manager=manager, roles=roles)

    def permissions_policy_status(
        self, action: int, is_disabled: bool, is_sealed: bool
    ) -> injective_permissions_pb.PolicyStatus:
        return injective_permissions_pb.PolicyStatus(action=action, is_disabled=is_disabled, is_sealed=is_sealed)

    def permissions_policy_manager_capability(
        self, manager: str, action: int, can_disable: bool, can_seal: bool
    ) -> injective_permissions_pb.PolicyManagerCapability:
        return injective_permissions_pb.PolicyManagerCapability(
            manager=manager, action=action, can_disable=can_disable, can_seal=can_seal
        )

    def permissions_role_actors(self, role: str, actors: List[str]) -> injective_permissions_pb.RoleActors:
        return injective_permissions_pb.RoleActors(role=role, actors=actors)

    def msg_create_namespace(
        self,
        sender: str,
        denom: str,
        contract_hook: str,
        role_permissions: List[injective_permissions_pb.Role],
        actor_roles: List[injective_permissions_pb.ActorRoles],
        role_managers: List[injective_permissions_pb.RoleManager],
        policy_statuses: List[injective_permissions_pb.PolicyStatus],
        policy_manager_capabilities: List[injective_permissions_pb.PolicyManagerCapability],
    ) -> injective_permissions_tx_pb.MsgCreateNamespace:
        namespace = injective_permissions_pb.Namespace(
            denom=denom,
            contract_hook=contract_hook,
            role_permissions=role_permissions,
            actor_roles=actor_roles,
            role_managers=role_managers,
            policy_statuses=policy_statuses,
            policy_manager_capabilities=policy_manager_capabilities,
        )
        return injective_permissions_tx_pb.MsgCreateNamespace(
            sender=sender,
            namespace=namespace,
        )

    def msg_update_namespace(
        self,
        sender: str,
        denom: str,
        contract_hook: str,
        role_permissions: List[injective_permissions_pb.Role],
        role_managers: List[injective_permissions_pb.RoleManager],
        policy_statuses: List[injective_permissions_pb.PolicyStatus],
        policy_manager_capabilities: List[injective_permissions_pb.PolicyManagerCapability],
    ) -> injective_permissions_tx_pb.MsgUpdateNamespace:
        contract_hook_update = injective_permissions_tx_pb.MsgUpdateNamespace.SetContractHook(new_value=contract_hook)

        return injective_permissions_tx_pb.MsgUpdateNamespace(
            sender=sender,
            denom=denom,
            contract_hook=contract_hook_update,
            role_permissions=role_permissions,
            role_managers=role_managers,
            policy_statuses=policy_statuses,
            policy_manager_capabilities=policy_manager_capabilities,
        )

    def msg_update_actor_roles(
        self,
        sender: str,
        denom: str,
        role_actors_to_add: List[injective_permissions_pb.RoleActors],
        role_actors_to_revoke: List[injective_permissions_pb.RoleActors],
    ) -> injective_permissions_tx_pb.MsgUpdateActorRoles:
        return injective_permissions_tx_pb.MsgUpdateActorRoles(
            sender=sender,
            denom=denom,
            role_actors_to_add=role_actors_to_add,
            role_actors_to_revoke=role_actors_to_revoke,
        )

    def msg_claim_voucher(
        self,
        sender: str,
        denom: str,
    ) -> injective_permissions_tx_pb.MsgClaimVoucher:
        return injective_permissions_tx_pb.MsgClaimVoucher(
            sender=sender,
            denom=denom,
        )

    # endregion

    # region ERC20 module
    def msg_create_token_pair(
        self, sender: str, bank_denom: str, erc20_address: str
    ) -> injective_erc20_tx_pb.MsgCreateTokenPair:
        token_pair = injective_erc20_pb2.TokenPair(
            bank_denom=bank_denom,
            erc20_address=erc20_address,
        )
        return injective_erc20_tx_pb.MsgCreateTokenPair(
            sender=sender,
            token_pair=token_pair,
        )

    def msg_delete_token_pair(self, sender: str, bank_denom: str) -> injective_erc20_tx_pb.MsgDeleteTokenPair:
        return injective_erc20_tx_pb.MsgDeleteTokenPair(
            sender=sender,
            bank_denom=bank_denom,
        )

    # endregion

    # data field format: [request-msg-header][raw-byte-msg-response]
    # you need to figure out this magic prefix number to trim request-msg-header off the data
    # this method handles only exchange responses
    @staticmethod
    def MsgResponses(response, simulation=False):
        data = response.result
        if not simulation:
            data = bytes.fromhex(data)

        msgs = []
        for msg in data.msg_responses:
            msgs.append(GRPC_RESPONSE_TYPE_TO_CLASS_MAP[msg.type_url].FromString(msg.value))

        return msgs

    @staticmethod
    def UnpackMsgExecResponse(msg_type, data):
        responses = []
        dict_message = json_format.MessageToDict(message=data, always_print_fields_with_no_presence=True)
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
                always_print_fields_with_no_presence=True,
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
                    "value": json_format.MessageToDict(message=grpc_message, always_print_fields_with_no_presence=True),
                }
            )

        return msgs

    def _order_mask(self, is_conditional: bool, is_buy: bool, is_market_order: bool) -> int:
        order_mask = 0

        if is_conditional:
            order_mask += injective_order_v2_pb.OrderMask.CONDITIONAL
        else:
            order_mask += injective_order_v2_pb.OrderMask.REGULAR

        if is_buy:
            order_mask += injective_order_v2_pb.OrderMask.DIRECTION_BUY_OR_HIGHER
        else:
            order_mask += injective_order_v2_pb.OrderMask.DIRECTION_SELL_OR_LOWER

        if is_market_order:
            order_mask += injective_order_v2_pb.OrderMask.TYPE_MARKET
        else:
            order_mask += injective_order_v2_pb.OrderMask.TYPE_LIMIT

        if order_mask == 0:
            order_mask = 1

        return order_mask

    def _basic_derivative_order(
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
        expiration_block: Optional[int] = None,
    ) -> injective_order_v2_pb.DerivativeOrder:
        trigger_price = trigger_price or Decimal(0)
        expiration_height = expiration_block or 0

        chain_quantity = f"{Token.convert_value_to_extended_decimal_format(value=quantity).normalize():f}"
        chain_price = f"{Token.convert_value_to_extended_decimal_format(value=price).normalize():f}"
        chain_margin = f"{Token.convert_value_to_extended_decimal_format(value=margin).normalize():f}"
        chain_trigger_price = f"{Token.convert_value_to_extended_decimal_format(value=trigger_price).normalize():f}"
        chain_order_type = injective_order_v2_pb.OrderType.Value(order_type)

        return injective_order_v2_pb.DerivativeOrder(
            market_id=market_id,
            order_info=injective_order_v2_pb.OrderInfo(
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=chain_price,
                quantity=chain_quantity,
                cid=cid,
            ),
            order_type=chain_order_type,
            margin=chain_margin,
            trigger_price=chain_trigger_price,
            expiration_block=expiration_height,
        )
