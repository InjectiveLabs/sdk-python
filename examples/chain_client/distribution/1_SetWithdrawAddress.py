import asyncio
import json
import os

import dotenv

from pyinjective import AsyncClient, PrivateKey
from pyinjective.core.broadcaster import MsgBroadcasterWithPk
from pyinjective.core.network import Network


async def main() -> None:
    dotenv.load_dotenv()
    configured_private_key = os.getenv("INJECTIVE_PRIVATE_KEY")

    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    composer = await client.composer()

    gas_price = await client.current_chain_gas_price()
    # adjust gas price to make it valid even if it changes between the time it is requested and the TX is broadcasted
    gas_price = int(gas_price * 1.1)

    message_broadcaster = MsgBroadcasterWithPk.new_without_simulation(
        network=network,
        private_key=configured_private_key,
        gas_price=gas_price,
        client=client,
        composer=composer,
    )

    priv_key = PrivateKey.from_hex(configured_private_key)
    pub_key = priv_key.to_public_key()
    address = pub_key.to_address()
    await client.fetch_account(address.to_acc_bech32())

    withdraw_address = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"

    message = composer.msg_set_withdraw_address(
        delegator_address=address.to_acc_bech32(),
        withdraw_address=withdraw_address,
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
