import asyncio
import json

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main():
    # Select network: testnet, mainnet, or local
    network = Network.testnet()
    client = IndexerClient(network)

    try:
        # Fetch INJ burnt amount
        inj_burnt_response = await client.fetch_inj_burnt()
        print("INJ Burnt Endpoint Response:")
        print(json.dumps(inj_burnt_response, indent=2))

    except Exception as e:
        print(f"Error fetching INJ burnt amount: {e}")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
