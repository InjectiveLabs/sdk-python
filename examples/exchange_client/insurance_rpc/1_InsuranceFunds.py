import asyncio
import json

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = IndexerClient(network)
    insurance_funds = await client.fetch_insurance_funds()
    print(json.dumps(insurance_funds, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
