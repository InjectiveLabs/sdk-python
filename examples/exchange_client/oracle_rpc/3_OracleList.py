import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    oracle_list = await client.get_oracle_list()
    print(oracle_list)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
