import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    account_address = "inj1cd0d4l9w9rpvugj8upwx0pt054v2fwtr563eh0"
    updates = await client.stream_account_portfolio(account_address=account_address)
    async for update in updates:
        print("Account portfolio Update:\n")
        print(update)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
