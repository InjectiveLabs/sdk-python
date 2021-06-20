

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
"""Injective Chain Tx Send Example."""

import asyncio
import aiohttp
import logging
import json

from _transaction import Transaction as Transaction
from _wallet import generate_wallet as generate_wallet
from _wallet import privkey_to_address as privkey_to_address
from _wallet import privkey_to_pubkey as privkey_to_pubkey
from _wallet import pubkey_to_address as pubkey_to_address
from _wallet import seed_to_privkey as seed_to_privkey


MIN_GAS_PRICE = 500000000


async def main() -> None:
    # user1 @ e2e-multinode
    sender_pk = seed_to_privkey("physical page glare junk return scale subject river token door mirror title")
    sender_acc_addr = privkey_to_address(sender_pk)
    print("Sender Account:", sender_acc_addr)

    # To Check:
    #   $ injectived --home ./var/data/injective-888/n0 --keyring-backend test keys show user1
    #   address: inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r

    acc_num, acc_seq = await get_account_num_seq(sender_acc_addr)

    tx = Transaction(
        privkey=sender_pk,
        account_num=acc_num,
        sequence=acc_seq,
        gas=100000,
        fee=100000 * MIN_GAS_PRICE,
        sync_mode="block"
    )
    tx.add_cosmos_bank_msg_send(
        recipient="inj1qy69k458ppmj45c3vqwcd6wvlcuvk23x0hsz58",  # maxim @ e2e-multinode
        amount=100000000000000000,  # 0.1 INJ
        denom="inj",
    )

    tx_json = tx.get_signed()

    print('Signed Tx:', tx_json)
    print('Sent Tx:', await post_tx(tx_json))


async def get_account_num_seq(address: str) -> (int, int):
    async with aiohttp.ClientSession() as session:
        async with session.request(
            'GET', 'http://localhost:10337/cosmos/auth/v1beta1/accounts/' + address,
            headers={'Accept-Encoding': 'application/json'},
        ) as response:
            if response.status != 200:
                print(await response.text())
                raise ValueError("HTTP response status", response.status)

            resp = json.loads(await response.text())
            acc = resp['account']['base_account']
            return acc['account_number'], acc['sequence']


async def post_tx(tx_json: str):
    async with aiohttp.ClientSession() as session:
        async with session.request(
            'POST', 'http://localhost:10337/txs', data=tx_json,
            headers={'Content-Type': 'application/json'},
        ) as response:
            if response.status != 200:
                print(await response.text())
                raise ValueError("HTTP response status", response.status)

            resp = json.loads(await response.text())
            if 'code' in resp:
                print("Response:", resp)
                raise ValueError('sdk error %d: %s' % (resp['code'], resp['raw_log']))

            return resp['txhash']

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())