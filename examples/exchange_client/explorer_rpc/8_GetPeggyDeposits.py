import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    receiver = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
    peggy_deposits = await client.get_peggy_deposits(receiver=receiver)
    print(peggy_deposits)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
