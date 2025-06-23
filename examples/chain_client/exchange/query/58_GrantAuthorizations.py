import asyncio
import json
import os

import dotenv

from pyinjective import PrivateKey
from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    dotenv.load_dotenv()
    configured_private_key = os.getenv("INJECTIVE_PRIVATE_KEY")

    # select network: local, testnet, mainnet
    network = Network.testnet()

    # initialize grpc client
    client = AsyncClient(network)

    priv_key = PrivateKey.from_hex(configured_private_key)
    pub_key = priv_key.to_public_key()
    address = pub_key.to_address()

    active_grant = await client.fetch_grant_authorizations(
        granter=address.to_acc_bech32(),
    )
    print(json.dumps(active_grant, indent=4))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
