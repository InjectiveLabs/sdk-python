import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    """
    Demonstrate fetching denom min notional using AsyncClient.
    """
    # Select network: choose between Network.mainnet(), Network.testnet(), or Network.devnet()
    network = Network.testnet()

    # Initialize the Async Client
    client = AsyncClient(network)

    try:
        # Example denom
        denom = "factory/inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r/inj_test"

        # Fetch market balance
        min_notional = await client.fetch_denom_min_notional(denom=denom)
        print("Min Notional:")
        print(min_notional)

    except Exception as ex:
        print(f"Error occurred: {ex}")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
