import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)

    denom = "inj"
    role = "roleName"
    addresses = await client.fetch_permissions_actors_by_role(denom=denom, role=role)
    print(addresses)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
