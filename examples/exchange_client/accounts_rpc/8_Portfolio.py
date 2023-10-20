import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    account_address = "inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku"
    portfolio = await client.fetch_portfolio(account_address=account_address)
    print(portfolio)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
