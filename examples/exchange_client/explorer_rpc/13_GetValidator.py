import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main():
    # Select network: choose between testnet, mainnet, or local
    network = Network.testnet()

    # Initialize AsyncClient
    client = AsyncClient(network)
    address = "injvaloper1kk523rsm9pey740cx4plalp40009ncs0wrchfe"

    try:
        # Fetch validator
        validator = await client.fetch_validator(address=address)

        # Print validators
        print("Validator:")
        print(validator)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
