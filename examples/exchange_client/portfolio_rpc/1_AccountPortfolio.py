import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    account_address = "inj1clw20s2uxeyxtam6f7m84vgae92s9eh7vygagt"
    portfolio = await client.fetch_account_portfolio_balances(account_address=account_address, usd=False)
    print(portfolio)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
