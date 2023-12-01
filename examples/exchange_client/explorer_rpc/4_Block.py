import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    block_height = "5825046"
    block = await client.fetch_block(block_id=block_height)
    print(block)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
