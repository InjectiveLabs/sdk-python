import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main():
    # Select network: testnet, mainnet, or local
    network = Network.testnet()

    # Initialize AsyncClient
    client = AsyncClient(network)

    try:
        # Fetch INJ burnt amount
        inj_burnt_response = await client.fetch_inj_burnt()
        print("INJ Burnt Endpoint Response:")
        print(inj_burnt_response)

    except Exception as e:
        print(f"Error fetching INJ burnt amount: {e}")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
