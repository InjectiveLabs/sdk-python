import asyncio

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)

    denom = "inj"
    actor = "actor"
    roles = await client.fetch_permissions_roles_by_actor(denom=denom, actor=actor)
    print(roles)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
