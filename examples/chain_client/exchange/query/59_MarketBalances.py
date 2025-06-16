import asyncio

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    """
    Demonstrate fetching market balances using AsyncClient.
    """
    # Select network: choose between Network.mainnet(), Network.testnet(), or Network.devnet()
    network = Network.testnet()

    # Initialize the Async Client
    client = AsyncClient(network)

    try:
        # Fetch market balances
        market_balances = await client.fetch_market_balances()
        print("Market Balances:")
        print(market_balances)

    except Exception as ex:
        print(f"Error occurred: {ex}")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
