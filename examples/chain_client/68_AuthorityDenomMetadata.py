import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    metadata = await client.fetch_denom_authority_metadata(creator="inj1zvy8xrlhe7ex9scer868clfstdv7j6vz790kwa")
    print(metadata)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
