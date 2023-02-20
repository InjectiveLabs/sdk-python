import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    market_ids = ["0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"]
    orderbooks = await client.stream_spot_orderbook_snapshot(market_ids=market_ids)
    async for orderbook in orderbooks:
        print(orderbook)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
