import asyncio
import json

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = IndexerClient(network)
    market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
    market = await client.fetch_derivative_market(market_id=market_id)
    print(json.dumps(market, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
