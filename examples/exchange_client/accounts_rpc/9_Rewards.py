import asyncio
import json

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    network = Network.testnet()
    client = IndexerClient(network)
    account_address = "inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku"
    epoch = -1
    rewards = await client.fetch_rewards(account_address=account_address, epoch=epoch)
    print(json.dumps(rewards, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
