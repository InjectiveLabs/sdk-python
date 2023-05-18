import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    market_id = "0x90e662193fa29a3a7e6c07be4407c94833e762d9ee82136a2cc712d6b87d7de3"
    markets = await client.stream_derivative_orderbook(market_id=market_id)
    async for market in markets:
        print(market)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
