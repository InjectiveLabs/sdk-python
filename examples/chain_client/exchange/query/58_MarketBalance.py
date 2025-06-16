import asyncio

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    """
    Demonstrate fetching market balance using AsyncClient.
    """
    # Select network: choose between Network.mainnet(), Network.testnet(), or Network.devnet()
    network = Network.testnet()

    # Initialize the Async Client
    client = AsyncClient(network)

    try:
        # Example market ID (replace with an actual market ID from the network)
        market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"

        # Fetch market balance
        market_balance = await client.fetch_market_balance(market_id=market_id)
        print("Market Balance:")
        print(market_balance)

    except Exception as ex:
        print(f"Error occurred: {ex}")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
