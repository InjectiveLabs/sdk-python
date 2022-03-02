from time import time
import json

from google.protobuf import any_pb2, message, timestamp_pb2

from .proto.cosmos.authz.v1beta1 import authz_pb2 as cosmos_authz_pb
from .proto.cosmos.authz.v1beta1 import tx_pb2 as cosmos_authz_tx_pb

from .proto.cosmos.bank.v1beta1 import tx_pb2 as cosmos_bank_tx_pb
from .proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_base_coin_pb

from .proto.injective.exchange.v1beta1 import tx_pb2 as injective_exchange_tx_pb
from .proto.injective.exchange.v1beta1 import exchange_pb2 as injective_exchange_pb
from .proto.injective.types.v1beta1 import tx_response_pb2 as tx_response_pb

from .proto.injective.auction.v1beta1 import tx_pb2 as injective_auction_tx_pb

from .proto.injective.peggy.v1 import msgs_pb2 as injective_peggy_tx_pb

from .proto.injective.oracle.v1beta1 import tx_pb2 as injective_oracle_tx_pb

from .constant import Denom
from .utils import *
from typing import List

from .wallet import Address

from web3 import Web3, HTTPProvider

class Composer:
    def __init__(self, network: str):
        self.network = network

    def Coin(self, amount: int, denom: str):
        return cosmos_base_coin_pb.Coin(amount=str(amount), denom=denom)

    def OrderData(self, market_id: str, subaccount_id: str, order_hash: str):
        return injective_exchange_tx_pb.OrderData(
            market_id=market_id, subaccount_id=subaccount_id, order_hash=order_hash
        )

    def SpotOrder(
        self,
        market_id: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
        **kwargs
    ):
        # load denom metadata
        denom = Denom.load_market(self.network, market_id)
        print("Loaded market metadata for", denom.description)

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
        **kwargs
    ):
        # load denom metadata
        denom = Denom.load_market(self.network, market_id)
        print("Loaded market metadata for", denom.description)

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
        trigger_price = derivative_price_to_backend(0, denom)
        quantity = derivative_quantity_to_backend(quantity, denom)

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
        print(
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
        print(
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
        **kwargs
    ):
        return injective_exchange_tx_pb.MsgCreateSpotLimitOrder(
            sender=sender,
            order=self.SpotOrder(
                market_id=market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=price,
                quantity=quantity,
                is_buy=kwargs.get("is_buy"),
                is_po=kwargs.get("is_po")
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

    def MsgCreateDerivativeLimitOrder(
        self,
        market_id: str,
        sender: str,
        subaccount_id: str,
        fee_recipient: str,
        price: float,
        quantity: float,
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
                is_buy=kwargs.get("is_buy"),
                is_po=kwargs.get("is_po"),
                leverage=kwargs.get("leverage"),
                is_reduce_only=kwargs.get("is_reduce_only"),
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
        **kwargs
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
                leverage=kwargs.get("leverage"),
                is_reduce_only=kwargs.get("is_reduce_only"),
            ),
        )

    def MsgCancelDerivativeOrder(
        self, market_id: str, sender: str, subaccount_id: str, order_hash: str
    ):
        return injective_exchange_tx_pb.MsgCancelDerivativeOrder(
            sender=sender,
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hash=order_hash,
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
        print(
            "Loaded withdrawal symbol {} ({}) with decimals = {}".format(
                denom, peggy_denom, decimals
            )
        )

        return injective_exchange_tx_pb.MsgWithdraw(
            sender=sender,
            subaccount_id=subaccount_id,
            amount=self.Coin(amount=be_amount, denom=peggy_denom),
        )

    def MsgBid(self, sender: str, bid_amount: float, round: float):

        be_amount = amount_to_backend(bid_amount, 18)

        return injective_auction_tx_pb.MsgBid(
            sender=sender,
            round=round,
            bid_amount=self.Coin(amount=be_amount, denom="inj"),
        )

    def MsgGrant(self, granter: str, grantee: str, msg_type: str, expire_in: int):
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
        self,
        sender: list,
        base: list,
        quote: list,
        price: list
    ):

        return injective_oracle_tx_pb.MsgRelayPriceFeedPrice(
            sender=sender,
            base=base,
            quote=quote,
            price=price
        )

    def MsgSendToEth(
        self,
        denom: str,
        sender: str,
        eth_dest: str,
        amount: float,
        bridge_fee: float
    ):

        peggy_denom, decimals = Denom.load_peggy_denom(self.network, denom)
        be_amount = amount_to_backend(amount, decimals)
        be_bridge_fee = amount_to_backend(bridge_fee, decimals)
        print("Loaded withdrawal symbol {} ({}) with decimals = {}".format(denom, peggy_denom, decimals))

        return injective_peggy_tx_pb.MsgSendToEth(
            sender=sender,
            eth_dest=eth_dest,
            amount=self.Coin(amount=be_amount, denom=peggy_denom),
            bridge_fee=self.Coin(amount=be_bridge_fee, denom=peggy_denom)
        )

    def SendToCosmos(self, ethereum_endpoint: str, private_key: str, token_contract: str, receiver: str, amount: int, maxFeePerGas: int,  maxPriorityFeePerGas: int, peggo_abi: str, decimals=18):
        if self.network == 'testnet':
            peggy_proxy_address = "0xd6Da9dA014806Fdb64bF39b48fcA386AE3420d21"
        elif self.network == 'mainnet':
            peggy_proxy_address = "0xF955C57f9EA9Dc8781965FEaE0b6A2acE2BAD6f3"
        else:
            print("SendToCosmos is only supported on Mainnet & Testnet")
        web3 = Web3(Web3.HTTPProvider(ethereum_endpoint))
        contract = web3.eth.contract(address=peggy_proxy_address, abi=peggo_abi)

        token_contract_address = web3.toChecksumAddress(token_contract)

        receiver_address = Address.from_acc_bech32(receiver)
        receiver_ethereum_address = Address.get_ethereum_address(receiver_address)
        receiver_address_checksum = web3.toChecksumAddress(receiver_ethereum_address)
        receiver_slice = receiver_address_checksum[2:]
        receiver_padded_address = '0x' + receiver_slice.zfill(64)

        destination = web3.toBytes(hexstr=receiver_padded_address)

        sender_ethereum_address = web3.eth.account.privateKeyToAccount(private_key).address
        sender_address_checksum = web3.toChecksumAddress(sender_ethereum_address)
        nonce = web3.eth.get_transaction_count(sender_address_checksum)

        amount_to_send = int(amount * pow(10, decimals))

        gas = contract.functions.sendToCosmos(
            token_contract_address,
            destination,
            amount_to_send,
        ).estimateGas({'from': sender_address_checksum})

        transaction_body = {
            'nonce': nonce,
            'gas': gas,
            'maxFeePerGas': web3.toWei(maxFeePerGas, 'gwei'),
            'maxPriorityFeePerGas': web3.toWei(maxPriorityFeePerGas, 'gwei'),
        }

        tx = contract.functions.sendToCosmos(
            token_contract_address,
            destination,
            amount_to_send,
        ).buildTransaction(transaction_body)

        signed_tx = web3.eth.account.signTransaction(tx, private_key=private_key)

        try:
            tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            print("Transferred {} {} from {} to {}".format(amount, token_contract, sender_ethereum_address, receiver))
            print("Transaction hash:", web3.toHex(tx_hash))
        except Exception as e:
            print("Transaction failed", e)

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
            "/cosmos.bank.v1beta1.MsgSend": cosmos_bank_tx_pb.MsgSendResponse,
            "/cosmos.authz.v1beta1.MsgGrant": cosmos_authz_tx_pb.MsgGrantResponse,
            "/cosmos.authz.v1beta1.MsgExec": cosmos_authz_tx_pb.MsgExecResponse,
            "/cosmos.authz.v1beta1.MsgRevoke": cosmos_authz_tx_pb.MsgRevokeResponse,
            "/injective.oracle.v1beta1.MsgRelayPriceFeedPrice": injective_oracle_tx_pb.MsgRelayPriceFeedPriceResponse
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
            "MsgBid": injective_auction_tx_pb.MsgBidResponse,
        }

        return header_map[msg_type].FromString(data)
