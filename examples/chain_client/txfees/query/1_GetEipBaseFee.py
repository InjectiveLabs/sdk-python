import asyncio
import json

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    metadata = await client.fetch_eip_base_fee()
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
