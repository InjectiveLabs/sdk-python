import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    market_id = "0x90e662193fa29a3a7e6c07be4407c94833e762d9ee82136a2cc712d6b87d7de3"
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
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
