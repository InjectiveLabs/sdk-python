import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
    skip=0
    limit=3
    end_time=1675717201465
    funding_rates = await client.get_funding_rates(
        market_id=market_id,
        skip=skip,
        limit=limit,
        end_time=end_time
    )
    print(funding_rates)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
