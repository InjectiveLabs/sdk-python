import asyncio
import json

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = IndexerClient(network)
    oracle_list = await client.fetch_oracle_list()
    print(json.dumps(oracle_list, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
