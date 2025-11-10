import asyncio
import json

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    """
    Demonstrate fetching denom min notionals using AsyncClient.
    """
    # Select network: choose between Network.mainnet(), Network.testnet(), or Network.devnet()
    network = Network.testnet()

    # Initialize the Async Client
    client = AsyncClient(network)

    market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
    open_interest = await client.fetch_open_interest(market_id=market_id)
    print(json.dumps(open_interest, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
