import asyncio

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    metadata = await client.fetch_denom_authority_metadata(
        creator="inj1uv6psuupldve0c9n3uezqlecadszqexv5vxx04",
        sub_denom="position",
    )
    print(metadata)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
