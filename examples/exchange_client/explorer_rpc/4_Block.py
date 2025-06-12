import asyncio
import json

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = IndexerClient(network=network)
    block_height = "5825046"
    block = await client.fetch_block(block_id=block_height)
    print(json.dumps(block, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
