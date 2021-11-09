# Copyright 2021 Injective Labs
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Injective Chain Tx/Query client for Python. Example only."""

import asyncio
import logging

from pyinjective.composer import Composer as ProtoMsgComposer
from pyinjective.client import Client
from pyinjective.transaction import Transaction
from pyinjective.constant import Network
from pyinjective.wallet import PrivateKey, PublicKey, Address


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    composer = ProtoMsgComposer(network=network.string())

    # initialize grpc client
    client = Client(network, insecure=True)

    # load account
    priv_key = PrivateKey.from_hex("f9db9bf330e23cb7839039e944adef6e9df447b90b503d5b4464c90bea9022f3")
    pub_key = priv_key.to_public_key()
    address = await pub_key.to_address().init_num_seq(network.lcd_endpoint)
    subaccount_id = address.get_subaccount_id(index=0)

    # prepare trade info
    market_id1 = "0xa508cb32923323679f29a032c70342c147c17d0145625922b0ef22e955c844c0"
    market_id2 = "0xd0f46edfba58827fe692aab7c8d46395d1696239fdf6aeddfa668b73ca82ea30"
    fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"

    # prepare tx msg
    msg1 = composer.MsgCreateSpotLimitOrder(
        sender=address.to_acc_bech32(),
        market_id=market_id1,
        subaccount_id=subaccount_id,
        fee_recipient=fee_recipient,
        price=7.523,
        quantity=0.01,
        is_buy=True
    )

    msg2 = composer.MsgBatchCancelSpotOrders(
        sender=address.to_acc_bech32(),
        data=[
            composer.OrderData(
                market_id=market_id2,
                subaccount_id=subaccount_id,
                order_hash="0x098f2c92336bb1ec3591435df1e135052760310bc08fc16e3b9bc409885b863b"
            ),
            composer.OrderData(
                market_id=market_id2,
                subaccount_id=subaccount_id,
                order_hash="0x8d4e780927f91011bf77dea8b625948a14c1ae55d8c5d3f5af3dadbd6bec591d"
            ),
            composer.OrderData(
                market_id=market_id2,
                subaccount_id=subaccount_id,
                order_hash="0x8d4e111127f91011bf77dea8b625948a14c1ae55d8c5d3f5af3dadbd6bec591d"
            )
        ]
    )

    msg3 = composer.MsgCreateDerivativeLimitOrder(
        sender=address.to_acc_bech32(),
        market_id=market_id2,
        subaccount_id=subaccount_id,
        fee_recipient=fee_recipient,
        price=44054.48,
        quantity=0.01,
        leverage=0.7,
        is_buy=True
    )

    # build sim tx
    tx = (
        Transaction()
        .with_messages(msg1, msg2, msg3)
        .with_sequence(address.get_sequence())
        .with_account_num(address.get_number())
        .with_chain_id(network.chain_id)
    )
    sim_sign_doc = tx.get_sign_doc(pub_key)
    sim_sig = priv_key.sign(sim_sign_doc.SerializeToString())
    sim_tx_raw_bytes = tx.get_tx_data(sim_sig, pub_key)

    # simulate tx
    (simRes, success) = client.simulate_tx(sim_tx_raw_bytes)
    if not success:
        print(simRes)
        return

    sim_res_msg = ProtoMsgComposer.MsgResponses(simRes.result.data, simulation=True)
    print("simulation msg response")
    print(sim_res_msg)

    # build tx
    gas_price = 500000000
    gas_limit = simRes.gas_info.gas_used + 15000  # add 15k for gas, fee computation
    fee = [composer.Coin(
        amount=gas_price * gas_limit,
        denom=network.fee_denom,
    )]
    tx = tx.with_gas(gas_limit).with_fee(fee).with_memo("").with_timeout_height(0)
    sign_doc = tx.get_sign_doc(pub_key)
    sig = priv_key.sign(sign_doc.SerializeToString())
    tx_raw_bytes = tx.get_tx_data(sig, pub_key)

    # broadcast tx: send_tx_async_mode, send_tx_sync_mode, send_tx_block_mode
    res = client.send_tx_block_mode(tx_raw_bytes)
    res_msg = ProtoMsgComposer.MsgResponses(res.data)
    print("tx response")
    print(res)
    print("tx msg response")
    print(res_msg)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
