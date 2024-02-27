import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    total_supply = await client.fetch_total_supply(
        pagination=PaginationOption(limit=10),
    )
    print(total_supply)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
