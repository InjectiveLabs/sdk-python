import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main():
    # Select network: choose between testnet, mainnet, or local
    network = Network.testnet()

    # Initialize AsyncClient
    client = AsyncClient(network)

    try:
        # Fetch relayers
        validators = await client.fetch_relayers()

        # Print relayers
        print("Relayers:")
        print(validators)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
