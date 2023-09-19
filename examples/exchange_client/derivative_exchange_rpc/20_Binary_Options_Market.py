import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    market_id = "0x175513943b8677368d138e57bcd6bef53170a0da192e7eaa8c2cd4509b54f8db"
    market = await client.get_binary_options_market(market_id=market_id)
    print(market)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
