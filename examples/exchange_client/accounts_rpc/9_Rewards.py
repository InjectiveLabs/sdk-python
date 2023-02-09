import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    # account_address = "inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku"
    epoch = -1
    rewards = await client.get_rewards(
        # account_address=account_address,
        epoch=epoch)
    print(rewards)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
