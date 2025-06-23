import asyncio
import json

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
        market_balance = await client.fetch_market_balance(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        )
        print("Market Balance:")
        print(json.dumps(market_balance, indent=4))

    except Exception as ex:
        print(f"Error occurred: {ex}")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
