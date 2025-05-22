import asyncio
import json

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    market_ids = [
        "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
        "0xd97d0da6f6c11710ef06315971250e4e9aed4b7d4cd02059c9477ec8cf243782",
    ]

    result = await client.fetch_open_interest(
        market_ids=market_ids,
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
