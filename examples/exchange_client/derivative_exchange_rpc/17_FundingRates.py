import asyncio
import json

from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = IndexerClient(network)
    market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
    skip = 0
    limit = 3
    end_time = 1675717201465
    pagination = PaginationOption(skip=skip, limit=limit, end_time=end_time)
    funding_rates = await client.fetch_funding_rates(market_id=market_id, pagination=pagination)
    print(json.dumps(funding_rates, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
