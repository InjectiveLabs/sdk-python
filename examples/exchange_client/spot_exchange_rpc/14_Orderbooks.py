import asyncio
import json

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    network = Network.testnet()
    client = IndexerClient(network)
    market_ids = [
        "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
        "0x7a57e705bb4e09c88aecfc295569481dbf2fe1d5efe364651fbe72385938e9b0",
    ]
    depth = 1
    orderbooks = await client.fetch_spot_orderbooks_v2(market_ids=market_ids, depth=depth)
    print(json.dumps(orderbooks, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
