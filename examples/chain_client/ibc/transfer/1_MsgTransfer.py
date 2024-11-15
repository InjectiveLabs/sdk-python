import asyncio
import os
from decimal import Decimal

import dotenv

from pyinjective.async_client import AsyncClient
from pyinjective.core.broadcaster import MsgBroadcasterWithPk
from pyinjective.core.network import Network
from pyinjective.wallet import PrivateKey


async def main() -> None:
    dotenv.load_dotenv()
    configured_private_key = os.getenv("INJECTIVE_PRIVATE_KEY")

    # select network: local, testnet, mainnet
    network = Network.testnet()

    # initialize grpc client
    client = AsyncClient(network)
    await client.initialize_tokens_from_chain_denoms()
    composer = await client.composer()
    await client.sync_timeout_height()

    message_broadcaster = MsgBroadcasterWithPk.new_using_simulation(
        network=network,
        private_key=configured_private_key,
    )

    # load account
    priv_key = PrivateKey.from_hex(configured_private_key)
    pub_key = priv_key.to_public_key()
    address = pub_key.to_address()
    await client.fetch_account(address.to_acc_bech32())

    source_port = "transfer"
    source_channel = "channel-126"
    token_decimals = 18
    transfer_amount = Decimal("0.1") * Decimal(f"1e{token_decimals}")
    inj_chain_denom = "inj"
    token_amount = composer.coin(amount=int(transfer_amount), denom=inj_chain_denom)
    sender = address.to_acc_bech32()
    receiver = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
    timeout_height = 10

    # prepare tx msg
    message = composer.msg_ibc_transfer(
        source_port=source_port,
        source_channel=source_channel,
        token_amount=token_amount,
        sender=sender,
        receiver=receiver,
        timeout_height=timeout_height,
    )

    # broadcast the transaction
    result = await message_broadcaster.broadcast([message])
    print("---Transaction Response---")
    print(result)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
