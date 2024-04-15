import asyncio

from google.protobuf import symbol_database

from pyinjective.async_client import AsyncClient
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)

    pagination = PaginationOption(skip=2, limit=4)

    channels = await client.fetch_ibc_channels(pagination=pagination)
    print(channels)


if __name__ == "__main__":
    symbol_db = symbol_database.Default()
    asyncio.get_event_loop().run_until_complete(main())
