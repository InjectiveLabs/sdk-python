import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)

    denom = "inj"
    manager = "manager"
    managers = await client.fetch_permissions_role_manager(denom=denom, manager=manager)
    print(managers)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
