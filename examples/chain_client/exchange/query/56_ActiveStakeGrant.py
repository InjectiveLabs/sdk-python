import asyncio
import os

import dotenv

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    dotenv.load_dotenv()
    grantee_public_address = os.getenv("INJECTIVE_GRANTEE_PUBLIC_ADDRESS")

    # select network: local, testnet, mainnet
    network = Network.testnet()

    # initialize grpc client
    client = AsyncClient(network)

    active_grant = await client.fetch_active_stake_grant(
        grantee=grantee_public_address,
    )
    print(active_grant)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
