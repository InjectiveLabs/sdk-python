import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    tx_hash = "0F3EBEC1882E1EEAC5B7BDD836E976250F1CD072B79485877CEACCB92ACDDF52"
    account = await client.get_tx_by_hash(tx_hash=tx_hash)
    print(account)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
