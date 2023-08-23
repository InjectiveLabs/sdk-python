import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    insurance_funds = await client.get_insurance_funds()
    print(insurance_funds)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
