import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    market_status = "active"
    quote_denom = "peggy0x69efCB62D98f4a6ff5a0b0CFaa4AAbB122e85e08"
    market = await client.get_derivative_markets(
        market_status=market_status,
        quote_denom=quote_denom
    )
    print(market)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
