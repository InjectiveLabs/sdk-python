import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)

    block = await client.fetch_block_by_height(height=15793860)
    print(block)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
