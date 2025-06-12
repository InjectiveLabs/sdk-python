import asyncio
import json
import os

import dotenv

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.broadcaster import MsgBroadcasterWithPk
from pyinjective.core.network import Network
from pyinjective.wallet import PrivateKey


async def main() -> None:
    dotenv.load_dotenv()
    private_key_in_hexa = os.getenv("INJECTIVE_PRIVATE_KEY")

    # select network: local, testnet, mainnet
    network = Network.devnet()

    client = AsyncClient(network)
    composer = await client.composer()

    gas_price = await client.current_chain_gas_price()
    # adjust gas price to make it valid even if it changes between the time it is requested and the TX is broadcasted
    gas_price = int(gas_price * 1.1)

    message_broadcaster = MsgBroadcasterWithPk.new_using_simulation(
        network=network,
        private_key=private_key_in_hexa,
        gas_price=gas_price,
        client=client,
        composer=composer,
    )

    priv_key = PrivateKey.from_hex(private_key_in_hexa)
    pub_key = priv_key.to_public_key()
    address = pub_key.to_address()

    denom = "factory/inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r/inj_test"

    role_actors1 = composer.permissions_role_actors(
        role="admin",
        actors=["inj1actoraddress1", "inj1actoraddress2"],
    )
    role_actors2 = composer.permissions_role_actors(
        role="user",
        actors=["inj1actoraddress3"],
    )
    role_actors3 = composer.permissions_role_actors(
        role="user",
        actors=["inj1actoraddress4"],
    )
    role_actors4 = composer.permissions_role_actors(
        role="admin",
        actors=["inj1actoraddress5"],
    )

    message = composer.msg_update_actor_roles(
        sender=address.to_acc_bech32(),
        denom=denom,
        role_actors_to_add=[role_actors1, role_actors2],
        role_actors_to_revoke=[role_actors3, role_actors4],
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
