import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    denom = "factory/inj107aqkjc3t5r3l9j4n9lgrma5tm3jav8qgppz6m/position"
    metadata = await client.fetch_denom_metadata(denom=denom)
    print(metadata)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
