import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    account_address = "inj1clw20s2uxeyxtam6f7m84vgae92s9eh7vygagt"
    updates = await client.stream_account_portfolio(account_address=account_address)
    async for update in updates:
        print("Account portfolio Update:\n")
        print(update)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
