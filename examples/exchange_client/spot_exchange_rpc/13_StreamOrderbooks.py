import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    market_ids = [
        "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
        "0x7a57e705bb4e09c88aecfc295569481dbf2fe1d5efe364651fbe72385938e9b0"
    ]
    orderbook = await client.stream_spot_orderbook_snapshot(market_ids=market_ids)
    async for orders in orderbook:
        print(orders)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
