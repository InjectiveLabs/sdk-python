import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    tx_hash = "7746BC12EB82B4D59D036FBFF2F67BDCA6F62A20B3DBC25661707DD61D4DC1B7"
    tx_logs = await client.get_tx(tx_hash=tx_hash)
    print(tx_logs)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())