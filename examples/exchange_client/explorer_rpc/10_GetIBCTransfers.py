import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    receiver = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
    ibc_transfers = await client.get_ibc_transfers(receiver=receiver)
    print(ibc_transfers)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
