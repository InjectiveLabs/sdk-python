import asyncio
import os

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
    client = AsyncClient(network)
    composer = await client.composer()

    message_broadcaster = MsgBroadcasterWithPk.new_without_simulation(
        network=network,
        private_key=configured_private_key,
        client=client,
        composer=composer,
    )

    priv_key = PrivateKey.from_hex(configured_private_key)
    pub_key = priv_key.to_public_key()
    address = pub_key.to_address()
    await client.fetch_account(address.to_acc_bech32())

    # prepare tx msg
    validator_address = "injvaloper1ultw9r29l8nxy5u6thcgusjn95vsy2caw722q5"

    message = composer.msg_withdraw_validator_commission(validator_address=validator_address)

    # broadcast the transaction
    result = await message_broadcaster.broadcast([message])
    print("---Transaction Response---")
    print(result)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
