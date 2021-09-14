import sys
sys.path.insert(0, '/Users/nam/desktop/injective/sdk-python/')

import asyncio
import logging
from decimal import *

from pyinjective.client import Client
from pyinjective.transaction import Transaction
from pyinjective.constant import Network, Denom
from pyinjective.wallet import PrivateKey, PublicKey, Address
from pyinjective.utils import *

import pyinjective.proto.injective.exchange.v1beta1.tx_pb2 as injective_exchange_tx_pb
import pyinjective.proto.injective.exchange.v1beta1.exchange_pb2 as injective_exchange_pb
import pyinjective.proto.cosmos.base.v1beta1.coin_pb2 as cosmos_base_coin_pb

async def main() -> None:
    # select network: localhost, testnet, mainnet
    network = Network.testnet()

    # initialize grpc client
    client = Client(network.grpc_endpoint, insecure=True)

    # load account
    priv_key = PrivateKey.from_hex("f9db9bf330e23cb7839039e944adef6e9df447b90b503d5b4464c90bea9022f3")
    pub_key =  priv_key.to_public_key()
    address = pub_key.to_address()
    subaccount_id = address.get_subaccount_id(index=0)

    # prepare trade info
    denom =  Denom.pair('BTC/USDT')
    market_id = "0xd0f46edfba58827fe692aab7c8d46395d1696239fdf6aeddfa668b73ca82ea30"
    fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
    price = 60000
    quantity = 30
    trigger_price = 0
    leverage = 3

    margin = derivative_margin_to_backend(price, quantity, leverage, denom)
    price = derivative_price_to_backend(price, denom)
    trigger_price = derivative_price_to_backend(trigger_price, denom)
    quantity = derivative_quantity_to_backend(quantity, denom)

    # prepare tx msg
    msg = injective_exchange_tx_pb.MsgCreateDerivativeMarketOrder(
        sender=address.to_acc_bech32(),
        order=injective_exchange_pb.DerivativeOrder(
            market_id=market_id,
            order_info=injective_exchange_pb.OrderInfo(
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=price,
                quantity=quantity,
            ),
            order_type=injective_exchange_pb.OrderType.BUY,
            margin=margin,
            trigger_price=trigger_price
        )
    )

    acc_num, acc_seq = await address.get_num_seq(network.lcd_endpoint)
    gas_price = 500000000
    gas_limit = 200000
    fee = [cosmos_base_coin_pb.Coin(denom=network.fee_denom,amount=str(gas_price * gas_limit))]

    # build tx
    tx = (
        Transaction()
        .with_messages(msg)
        .with_sequence(acc_seq)
        .with_account_num(acc_num)
        .with_chain_id(network.chain_id)
        .with_gas(gas_limit)
        .with_fee(fee)
        .with_memo("")
        .with_timeout_height(0)
    )

    # build signed tx
    sign_doc = tx.get_sign_doc(pub_key)
    sig = priv_key.sign(sign_doc.SerializeToString())
    tx_raw_bytes = tx.get_tx_data(sig, pub_key)

    # broadcast tx: send_tx_async_mode, send_tx_sync_mode, send_tx_block_mode
    res = client.send_tx_block_mode(tx_raw_bytes)

    # print tx response
    print(res)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
