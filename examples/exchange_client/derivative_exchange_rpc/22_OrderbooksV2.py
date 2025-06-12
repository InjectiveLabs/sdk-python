import asyncio
import json

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = IndexerClient(network=network)
    market_ids = [
        "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
        "0xd5e4b12b19ecf176e4e14b42944731c27677819d2ed93be4104ad7025529c7ff",
    ]
    depth = 1
    orderbooks = await client.fetch_derivative_orderbooks_v2(market_ids=market_ids, depth=depth)
    print(json.dumps(orderbooks, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
