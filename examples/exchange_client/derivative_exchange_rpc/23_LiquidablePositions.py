import asyncio
import json

from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    network = Network.testnet()
    client = IndexerClient(network)
    market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
    skip = 10
    limit = 3
    pagination = PaginationOption(skip=skip, limit=limit)
    positions = await client.fetch_derivative_liquidable_positions(
        market_id=market_id,
        pagination=pagination,
    )
    print(json.dumps(positions, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
