import asyncio
import json

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
    depth = 1
    orderbook = await client.fetch_spot_orderbook_v2(market_id=market_id, depth=depth)
    print(json.dumps(orderbook, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
