# import sys
# sys.path.insert(0, '/Users/nam/desktop/injective/sdk-python/')

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
    priv_key = PrivateKey.from_hex("5d386fbdbf11f1141010f81a46b40f94887367562bd33b452bbaa6ce1cd1381e")
    pub_key =  priv_key.to_public_key()
    address = pub_key.to_address()
    subaccount_id = address.get_subaccount_id(index=0)

    # prepare trade info
    denom =  Denom.pair('INJ/USDT')
    quantity = quantity_to_backend(0.001, denom)
    price = price_to_backend(7.523, denom)
    trigger_price = price_to_backend(0, denom)
    market_id = "0xa508cb32923323679f29a032c70342c147c17d0145625922b0ef22e955c844c0"
    fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"

    # prepare tx msg
    msg = injective_exchange_tx_pb.MsgCreateSpotLimitOrder(
        sender=address.to_acc_bech32(),
        order=injective_exchange_pb.SpotOrder(
            market_id=market_id,
            order_info=injective_exchange_pb.OrderInfo(
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=price,
                quantity=quantity
            ),
            order_type=injective_exchange_pb.OrderType.BUY,
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

#
# import asyncio
# import aiohttp
# import logging
# import base64
# import json
# import ecdsa
# import sha3
# import grpc
#
# from typing import Any, Dict, List
# from injective.utils import *
# from injective.constant import *
# from injective.chain_client._wallet import (
#     generate_wallet,
#     privkey_to_address,
#     privkey_hex_to_bytes,
#     privkey_to_pubkey,
#     pubkey_to_address,
#     seed_to_privkey,
#     DEFAULT_BECH32_HRP,
# )
# from injective.chain_client._typings import SyncMode
#
# MIN_GAS_PRICE = 500000000
#
# class Transaction:
#
#     def __init__(
#         self,
#         *,
#         privkey: bytes,
#         account_num: int,
#         sequence: int,
#         fee: int,
#         gas: int,
#         fee_denom: str = "inj",
#         memo: str = "",
#         chain_id: str = "injective-888",
#         hrp: str = DEFAULT_BECH32_HRP,
#         sync_mode: SyncMode = "block",
#     ) -> None:
#         self._privkey = privkey
#         self._account_num = account_num
#         self._sequence = sequence
#         self._fee = fee
#         self._fee_denom = fee_denom
#         self._gas = gas
#         self._memo = memo
#         self._chain_id = chain_id
#         self._hrp = hrp
#         self._sync_mode = sync_mode
#         self._msgs: List[dict] = []
#
#     def msg_create_spot_limit_order(self, subaccount_id: str,  market_id: str, fee_recipient: str, price, quantity, order_type, trigger_price) -> None:
#         msg = {
#             "type": "exchange/MsgCreateSpotLimitOrder",
#             "value": {
#                 "sender": privkey_to_address(self._privkey, hrp=self._hrp),
#                 "order": {
#                     'market_id': market_id,
#                     'order_info': {
#                         'subaccount_id': subaccount_id,
#                         'fee_recipient': fee_recipient,
#                         'price': price,
#                         'quantity': quantity,
#                     },
#                     'order_type': order_type,
#                     "trigger_price": trigger_price,
#                 },
#             }
#         }
#         self._msgs.append(msg)
#
#     def get_signed(self) -> str:
#         pubkey = privkey_to_pubkey(self._privkey)
#         base64_pubkey = base64.b64encode(pubkey).decode("utf-8")
#         signed_tx = {
#             "tx": {
#                 "msg": self._msgs,
#                 "fee": {
#                     "gas": str(self._gas),
#                     "amount": [{"denom": self._fee_denom, "amount": str(self._fee)}],
#                 },
#                 "memo": self._memo,
#                 "signatures": [
#                     {
#                         "signature": self._sign(),
#                         "pub_key": {"type": "injective/PubKeyEthSecp256k1", "value": base64_pubkey},
#                         "account_number": str(self._account_num),
#                         "sequence": str(self._sequence),
#                     }
#                 ],
#             },
#             "mode": self._sync_mode,
#         }
#         return json.dumps(signed_tx, separators=(",", ":"))
#
#     def _sign(self) -> str:
#         message_str = json.dumps(
#             self._get_sign_message(), separators=(",", ":"), sort_keys=True)
#         message_bytes = message_str.encode("utf-8")
#
#         privkey = ecdsa.SigningKey.from_string(
#             self._privkey, curve=ecdsa.SECP256k1)
#         signature_compact_keccak = privkey.sign_deterministic(
#             message_bytes, hashfunc=sha3.keccak_256, sigencode=ecdsa.util.sigencode_string_canonize
#         )
#         signature_base64_str = base64.b64encode(
#             signature_compact_keccak).decode("utf-8")
#         return signature_base64_str
#
#     def _get_sign_message(self) -> Dict[str, Any]:
#         return {
#             "chain_id": self._chain_id,
#             "account_number": str(self._account_num),
#             "fee": {
#                 "gas": str(self._gas),
#                 "amount": [{"amount": str(self._fee), "denom": self._fee_denom}],
#             },
#             "memo": self._memo,
#             "sequence": str(self._sequence),
#             "msgs": self._msgs,
#         }
#
# async def main() -> None:
#     sender_pk = seed_to_privkey(
#         "physical page glare junk return scale subject river token door mirror title"
#     )
#     sender_acc_addr = privkey_to_address(sender_pk)
#     print("Sender Account:", sender_acc_addr)
#
#     acc_num, acc_seq = await get_account_num_seq(sender_acc_addr)
#
#     price = float(7.523)
#     quantity = float(12.22)
#     trigger_price = float(0)
#     base_decimals = int(18)
#     quote_decimals = int(6)
#     market = "0xa508cb32923323679f29a032c70342c147c17d0145625922b0ef22e955c844c0"
#     endpoint = "testnet-sentry0.injective.network:9910" #testnet endpoint
#     #endpoint = "145.40.67.91:9910" #mainnet endpoint
#
#     tx = Transaction(
#         privkey=sender_pk,
#         account_num=acc_num,
#         sequence=acc_seq,
#         gas=200000,
#         fee=200000 * MIN_GAS_PRICE,
#         sync_mode="block",
#     )
#
#     tx.msg_create_spot_limit_order(
#         market_id = market,
#         subaccount_id = "0xbdaedec95d563fb05240d6e01821008454c24c36000000000000000000000000",
#         fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r",
#         price = await spot_price_to_backend(endpoint, market, price, base_decimals, quote_decimals),
#         quantity = await spot_quantity_to_backend(endpoint, market, quantity, base_decimals),
#         order_type = ORDERTYPE_DICT["BUY"],
#         trigger_price = await spot_price_to_backend(endpoint, market, trigger_price, base_decimals, quote_decimals),
#     )
#
#     tx_json = tx.get_signed()
#
#     print("Signed Tx:", tx_json)
#     print("Sent Tx:", await post_tx(tx_json))
#
# async def get_account_num_seq(address: str) -> (int, int):
#     async with aiohttp.ClientSession() as session:
#         async with session.request(
#             'GET', 'http://staking-lcd-testnet.injective.network/cosmos/auth/v1beta1/accounts/' + address,
#             headers={'Accept-Encoding': 'application/json'},
#         ) as response:
#             if response.status != 200:
#                 print(await response.text())
#                 raise ValueError("HTTP response status", response.status)
#
#             resp = json.loads(await response.text())
#             acc = resp['account']['base_account']
#             return acc['account_number'], acc['sequence']
#
# async def post_tx(tx_json: str):
#     async with aiohttp.ClientSession() as session:
#         async with session.request(
#             'POST', 'http://staking-lcd-testnet.injective.network/txs', data=tx_json,
#             headers={'Content-Type': 'application/json'},
#         ) as response:
#             if response.status != 200:
#                 print(await response.text())
#                 raise ValueError("HTTP response status", response.status)
#
#             resp = json.loads(await response.text())
#             if 'code' in resp:
#                 print("Response:", resp)
#                 raise ValueError('sdk error %d: %s' % (resp['code'], resp['raw_log']))
#
#             return resp['txhash']
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO)
#     asyncio.get_event_loop().run_until_complete(main())
