import asyncio
import json

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main():
    # Select network: choose between testnet, mainnet, or local
    network = Network.testnet()
    client = IndexerClient(network=network)

    address = "injvaloper1kk523rsm9pey740cx4plalp40009ncs0wrchfe"

    try:
        # Fetch validator
        validator = await client.fetch_validator(address=address)

        # Print validators
        print("Validator:")
        print(json.dumps(validator, indent=2))

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
