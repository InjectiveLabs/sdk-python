import asyncio

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    denom = "inj"
    owners = await client.fetch_denom_owners(
        denom=denom,
        pagination=PaginationOption(limit=10),
    )
    print(owners)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
