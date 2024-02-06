import asyncio
import os

import dotenv
from grpc import RpcError

from pyinjective.async_client import AsyncClient
from pyinjective.constant import GAS_FEE_BUFFER_AMOUNT, GAS_PRICE
from pyinjective.core.network import Network
from pyinjective.transaction import Transaction
from pyinjective.wallet import PrivateKey


async def main() -> None:
    dotenv.load_dotenv()
    configured_private_key = os.getenv("INJECTIVE_PRIVATE_KEY")

    # select network: local, testnet, mainnet
    network = Network.testnet()

    # initialize grpc client
    # set custom cookie location (optional) - defaults to current dir
    client = AsyncClient(network)
    composer = await client.composer()
    await client.sync_timeout_height()

    # load account
    priv_key = PrivateKey.from_hex(configured_private_key)
    pub_key = priv_key.to_public_key()
    address = pub_key.to_address()
    await client.fetch_account(address.to_acc_bech32())

    # prepare tx msg
    # NOTE: COIN MUST BE SORTED IN ALPHABETICAL ORDER BY DENOMS
    funds = [
        composer.Coin(
            amount=69,
            denom="factory/inj1hdvy6tl89llqy3ze8lv6mz5qh66sx9enn0jxg6/inj12ngevx045zpvacus9s6anr258gkwpmthnz80e9",
        ),
        composer.Coin(amount=420, denom="peggy0x44C21afAaF20c270EBbF5914Cfc3b5022173FEB7"),
        composer.Coin(amount=1, denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5"),
    ]
    msg = composer.MsgExecuteContract(
        sender=address.to_acc_bech32(),
        contract="inj1ady3s7whq30l4fx8sj3x6muv5mx4dfdlcpv8n7",
        msg='{"increment":{}}',
        funds=funds,
    )

    # build sim tx
    tx = (
        Transaction()
        .with_messages(msg)
        .with_sequence(client.get_sequence())
        .with_account_num(client.get_number())
        .with_chain_id(network.chain_id)
    )
    sim_sign_doc = tx.get_sign_doc(pub_key)
    sim_sig = priv_key.sign(sim_sign_doc.SerializeToString())
    sim_tx_raw_bytes = tx.get_tx_data(sim_sig, pub_key)

    # simulate tx
    try:
        sim_res = await client.simulate(sim_tx_raw_bytes)
    except RpcError as ex:
        print(ex)
        return

    # build tx
    gas_price = GAS_PRICE
    gas_limit = int(sim_res["gasInfo"]["gasUsed"]) + GAS_FEE_BUFFER_AMOUNT  # add buffer for gas fee computation
    gas_fee = "{:.18f}".format((gas_price * gas_limit) / pow(10, 18)).rstrip("0")
    fee = [
        composer.Coin(
            amount=gas_price * gas_limit,
            denom=network.fee_denom,
        )
    ]
    tx = tx.with_gas(gas_limit).with_fee(fee).with_memo("").with_timeout_height(client.timeout_height)
    sign_doc = tx.get_sign_doc(pub_key)
    sig = priv_key.sign(sign_doc.SerializeToString())
    tx_raw_bytes = tx.get_tx_data(sig, pub_key)

    # broadcast tx: send_tx_async_mode, send_tx_sync_mode, send_tx_block_mode
    res = await client.broadcast_tx_sync_mode(tx_raw_bytes)
    print(res)
    print("gas wanted: {}".format(gas_limit))
    print("gas fee: {} INJ".format(gas_fee))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
