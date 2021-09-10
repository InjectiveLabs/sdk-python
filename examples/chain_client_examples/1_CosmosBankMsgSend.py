import asyncio
import aiohttp
import logging
import json
import base64
import ecdsa
import sha3
import grpc
import mnemonic
import ecdsa
import hdwallets
import bech32
import sys
from google.protobuf.any_pb2 import Any
from google.protobuf.json_format import MessageToJson


sys.path.insert(0, '/Users/nam/Desktop/injective/sdk-python/src/proto')
sys.path.insert(0, '/Users/nam/Desktop/injective/sdk-python/src/proto/injective')

import crypto.v1beta1.ethsecp256k1.keys_pb2 as eth_key_pb

import cosmos.base.v1beta1.coin_pb2 as cosmos_base_coin_pb
import cosmos.bank.v1beta1.tx_pb2 as cosmos_bank_tx_pb
import cosmos.bank.v1beta1.tx_pb2_grpc as cosmos_bank_tx_grpc
import cosmos.bank.v1beta1.query_pb2 as cosmos_bank_query_pb
import cosmos.bank.v1beta1.query_pb2_grpc as cosmos_bank_query_grpc

import cosmos.auth.v1beta1.query_pb2 as cosmos_auth_query_pb
import cosmos.auth.v1beta1.query_pb2_grpc as cosmos_auth_query_grpc

import cosmos.tx.v1beta1.tx_pb2 as cosmos_tx_pb
import cosmos.tx.v1beta1.service_pb2 as cosmos_tx_service_pb
import cosmos.tx.v1beta1.service_pb2_grpc as cosmos_tx_service_grpc
import cosmos.tx.signing.v1beta1.signing_pb2 as cosmos_tx_signing_pb

DEFAULT_DERIVATION_PATH = "m/44'/60'/0'/0/0"
DEFAULT_BECH32_HRP = "inj"

def seed2Privkey(seed: str, path: str = DEFAULT_DERIVATION_PATH) -> bytes:
    """Get a private key from a mnemonic seed and a derivation path.

    Assumes a BIP39 mnemonic seed with no passphrase. Raises
    `BIP32DerivationError` if the resulting private key is
    invalid.
    """
    seed_bytes = mnemonic.Mnemonic.to_seed(seed, passphrase="")
    hd_wallet = hdwallets.BIP32.from_seed(seed_bytes)
    # This can raise a `hdwallets.BIP32DerivationError` (which we alias so
    # that the same exception type is also in the `chainclient` namespace).
    derived_privkey = hd_wallet.get_privkey_from_path(path)

    return derived_privkey

def pubkey2Address(pubkey: bytes, *, hrp: str = DEFAULT_BECH32_HRP) -> str:
    if len(pubkey) != 65:
        raise ValueError("wrong pubkey length (must be uncompressed, len = 65)")

    # This is for vanilla Cosmos SDK folks
    #   s = hashlib.new("sha256", pubkey).digest()
    #   r = hashlib.new("ripemd160", s).digest()

    # --
    # This is for EVM compatible chads
    k = sha3.keccak_256()
    k.update(pubkey[1:])
    addr = k.digest()[12:]

    five_bit_r = bech32.convertbits(addr, 8, 5)
    assert five_bit_r is not None, "Unsuccessful bech32.convertbits call"
    return bech32.bech32_encode(hrp, five_bit_r)

def privkey2Pubkey(privkey: bytes) -> bytes:
    privkey_obj = ecdsa.SigningKey.from_string(privkey, curve=ecdsa.SECP256k1)
    pubkey_obj = privkey_obj.get_verifying_key()
    return pubkey_obj.to_string("compressed")

def privkey2UncompressedPubkey(privkey: bytes) -> bytes:
    privkey_obj = ecdsa.SigningKey.from_string(privkey, curve=ecdsa.SECP256k1)
    pubkey_obj = privkey_obj.get_verifying_key()
    return pubkey_obj.to_string("uncompressed")

def privkey2Address(privkey: bytes, *, hrp: str = DEFAULT_BECH32_HRP) -> str:
    pubkey = privkey2UncompressedPubkey(privkey)
    return pubkey2Address(pubkey, hrp=hrp)

def sign(bodyBytes, authInfoBytes, accNum, privkey) -> str:
    payload = cosmos_tx_pb.SignDoc(
        body_bytes=bodyBytes,
        auth_info_bytes=authInfoBytes,
        chain_id="injective-1",
        account_number=accNum
    )

    pk = ecdsa.SigningKey.from_string(privkey, curve=ecdsa.SECP256k1)
    sig = pk.sign_deterministic(
        payload.SerializeToString(),
        hashfunc=sha3.keccak_256,
        sigencode=ecdsa.util.sigencode_string_canonize
    )

    return sig

async def getAccNumSeq(address: str) -> (int, int):
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
            return int(acc['account_number']), int(acc['sequence'])


async def main() -> None:
    async with grpc.aio.insecure_channel('localhost:9900') as channel:
        txServiceStub = cosmos_tx_service_grpc.ServiceStub(channel)
        # bankMsgStub = cosmos_bank_tx_grpc.MsgStub(channel)
        # bankQueryStub = cosmos_bank_query_grpc.QueryStub(channel)
        # authQueryStub = cosmos_auth_query_grpc.QueryStub(channel)

        senderPk = seed2Privkey("copper push brief egg scan entry inform record adjust fossil boss egg comic alien upon aspect dry avoid interest fury window hint race symptom")
        sender = privkey2Address(senderPk)
        print("Sender",sender)
        receiver = "inj1jcltmuhplrdcwp7stlr4hlhlhgd4htqhe4c0cs"

        sendMsg = cosmos_bank_tx_pb.MsgSend(
            from_address=sender,
            to_address=receiver,
            amount=[cosmos_base_coin_pb.Coin(denom="inj",amount=str(700))]
        )
        packedSendMsg = Any()
        packedSendMsg.Pack(sendMsg, type_url_prefix="")

        publicKey = eth_key_pb.PubKey(key=privkey2Pubkey(senderPk))
        packedPublicKey = Any()
        packedPublicKey.Pack(publicKey,type_url_prefix="")

        accNumSeq = await getAccNumSeq(sender)
        gasPrice = 500000000
        gasLimit = 200000
        # req = cosmos_auth_query_pb.QueryAccountRequest(address=sender)
        # res = await authQueryStub.Account(req)
        # print(res)

        signerInfo = cosmos_tx_pb.SignerInfo(
            public_key=packedPublicKey,
            mode_info=cosmos_tx_pb.ModeInfo(
                single=cosmos_tx_pb.ModeInfo.Single(
                    mode=cosmos_tx_signing_pb.SignMode.SIGN_MODE_DIRECT
                )
            ),
            sequence=accNumSeq[1],
        )

        txAuthInfo = cosmos_tx_pb.AuthInfo(
            signer_infos=[signerInfo],
            fee=cosmos_tx_pb.Fee(
                amount=[cosmos_base_coin_pb.Coin(denom="inj",amount=str(gasPrice * gasLimit))],
                gas_limit=gasLimit
            )
        )

        txBody = cosmos_tx_pb.TxBody(
            messages=[packedSendMsg],
            memo="",
        )

        txBodyBytes = txBody.SerializeToString()
        txAuthInfoBytes = txAuthInfo.SerializeToString()
        sig = sign(txBodyBytes, txAuthInfoBytes, accNumSeq[0], senderPk)

        txRaw = cosmos_tx_pb.TxRaw(
            body_bytes=txBodyBytes,
            auth_info_bytes=txAuthInfoBytes,
            signatures=[sig]
        )

        tx = cosmos_tx_pb.Tx(
            body=txBody,
            auth_info=txAuthInfo,
            signatures=[sig]
        )

        txJson = MessageToJson(tx)
        print(txJson)

        broadcastReq = cosmos_tx_service_pb.BroadcastTxRequest(
            tx_bytes=txRaw.SerializeToString(),
            mode=cosmos_tx_service_pb.BROADCAST_MODE_BLOCK
        )

        res = await txServiceStub.BroadcastTx(broadcastReq)
        print(res)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
