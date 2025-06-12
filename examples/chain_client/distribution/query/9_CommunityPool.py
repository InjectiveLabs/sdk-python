import asyncio

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    community_pool = await client.fetch_community_pool()
    print(community_pool)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
