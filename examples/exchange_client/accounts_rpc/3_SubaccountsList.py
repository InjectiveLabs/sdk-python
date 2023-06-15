import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    account_address = "inj1clw20s2uxeyxtam6f7m84vgae92s9eh7vygagt"
    subacc_list = await client.get_subaccount_list(account_address)
    print(subacc_list)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
