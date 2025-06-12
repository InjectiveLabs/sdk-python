import asyncio
import json

from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = IndexerClient(network=network)
    limit = 2
    pagination = PaginationOption(limit=limit)
    blocks = await client.fetch_blocks(pagination=pagination)
    print(json.dumps(blocks, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
