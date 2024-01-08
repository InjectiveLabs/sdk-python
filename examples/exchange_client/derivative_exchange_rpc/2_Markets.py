import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    market_statuses = ["active"]
    quote_denom = "peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5"
    market = await client.fetch_derivative_markets(market_statuses=market_statuses, quote_denom=quote_denom)
    print(market)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
