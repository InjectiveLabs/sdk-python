import asyncio
import json

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main():
    # Select network: choose between testnet, mainnet, or local
    network = Network.testnet()
    client = IndexerClient(network=network)

    try:
        # Fetch relayers
        relayers = await client.fetch_relayers()

        # Print relayers
        print("Relayers:")
        print(json.dumps(relayers, indent=2))

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
