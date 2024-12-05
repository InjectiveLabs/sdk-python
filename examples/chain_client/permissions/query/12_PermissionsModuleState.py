import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)

    state = await client.fetch_permissions_module_state()
    print(state)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
