import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    receiver = "inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex"
    peggy_deposits = await client.get_peggy_deposits(receiver=receiver)
    print(peggy_deposits)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
