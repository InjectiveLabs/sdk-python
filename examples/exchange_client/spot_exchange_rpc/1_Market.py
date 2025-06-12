import asyncio
import json

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    network = Network.testnet()
    client = IndexerClient(network)
    market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
    market = await client.fetch_spot_market(market_id=market_id)
    print(json.dumps(market, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
