import asyncio
import json

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    denom = "factory/inj107aqkjc3t5r3l9j4n9lgrma5tm3jav8qgppz6m/position"
    metadata = await client.fetch_denom_metadata(denom=denom)
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
