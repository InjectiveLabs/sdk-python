import asyncio
import logging
import time

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    resp = await client.info()
    print('[!] Info:')
    print(resp)
    latency = int(round(time.time() * 1000)) - resp.timestamp
    print(f'Server Latency: {latency}ms')


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
