import asyncio
import json

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    network = Network.testnet()
    client = IndexerClient(network)
    market_id = "0x175513943b8677368d138e57bcd6bef53170a0da192e7eaa8c2cd4509b54f8db"
    market = await client.fetch_binary_options_market(market_id=market_id)
    print(json.dumps(market, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
