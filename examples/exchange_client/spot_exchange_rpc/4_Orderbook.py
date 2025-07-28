import asyncio
import json

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    network = Network.testnet()
    client = IndexerClient(network)
    market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
    depth = 1
    orderbook = await client.fetch_spot_orderbook_v2(market_id=market_id, depth=depth)
    print(json.dumps(orderbook, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
