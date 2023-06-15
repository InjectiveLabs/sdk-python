import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    market_status = "active"
    base_denom = "inj"
    quote_denom = "peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5"
    market = await client.get_spot_markets(
        market_status=market_status,
        base_denom=base_denom,
        quote_denom=quote_denom
    )
    print(market)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
