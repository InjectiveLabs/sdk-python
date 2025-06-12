import asyncio
import json

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)

    latest_block = await client.fetch_latest_block()
    print(json.dumps(latest_block, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
