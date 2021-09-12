# import sys
# sys.path.insert(0, '/Users/nam/desktop/injective/sdk-python/')

import asyncio
import logging

from pyinjective.client import Client
from pyinjective.transaction import Transaction
from pyinjective.constant import Network
from pyinjective.wallet import PrivateKey, PublicKey, Address

import pyinjective.proto.injective.exchange.v1beta1.tx_pb2 as injective_exchange_tx_pb
import pyinjective.proto.cosmos.base.v1beta1.coin_pb2 as cosmos_base_coin_pb

async def main() -> None:
    # select network: localhost, testnet, mainnet
    network = Network.local()

    # initialize grpc client
    client = Client(network.grpc_endpoint, insecure=True)

    # load account
    priv_key = PrivateKey.from_mnemonic("copper push brief egg scan entry inform record adjust fossil boss egg comic alien upon aspect dry avoid interest fury window hint race symptom")
    pub_key =  priv_key.to_public_key()
    address = pub_key.to_address()
    subaccount_id = address.get_subaccount_id(index=7)

    # prepare tx msg
    msg = injective_exchange_tx_pb.MsgDeposit(
        sender=address.to_acc_bech32(),
        subaccount_id=subaccount_id,
        amount=cosmos_base_coin_pb.Coin(denom=network.fee_denom,amount=str(700))
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
