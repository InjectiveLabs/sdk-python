import asyncio
import json
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

    gas_price = await client.current_chain_gas_price()
    # adjust gas price to make it valid even if it changes between the time it is requested and the TX is broadcasted
    gas_price = int(gas_price * 1.1)

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
    token_amount = composer.create_coin_amount(amount=Decimal("0.1"), token_name="INJ")
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
    print(json.dumps(result, indent=2))

    gas_price = await client.current_chain_gas_price()
    # adjust gas price to make it valid even if it changes between the time it is requested and the TX is broadcasted
    gas_price = int(gas_price * 1.1)
    message_broadcaster.update_gas_price(gas_price=gas_price)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
