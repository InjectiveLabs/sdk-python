import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    market_status = "active"
    quote_denom = "peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5"
    market = await client.get_derivative_markets(
        market_status=market_status,
        quote_denom=quote_denom
    )
    print(market)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
