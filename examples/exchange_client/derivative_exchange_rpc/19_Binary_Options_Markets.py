import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    market_status = "active"
    quote_denom = "peggy0xdAC17F958D2ee523a2206206994597C13D831ec7"
    market = await client.get_binary_options_markets(market_status=market_status, quote_denom=quote_denom)

    print(market)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
