import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # network: Network = Network.testnet()
    network: Network = Network.testnet()
    client: AsyncClient = AsyncClient(network)

    address = "inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex"

    balance = await client.fetch_cw20_balance(address=address)
    print("Cw20 balance:")
    print(balance)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
