import asyncio

from google.protobuf import symbol_database

from pyinjective.async_client import AsyncClient
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)

    connection = "connection-182"
    pagination = PaginationOption(skip=2, limit=4)

    channels = await client.fetch_ibc_connection_channels(connection=connection, pagination=pagination)
    print(channels)


if __name__ == "__main__":
    symbol_db = symbol_database.Default()
    asyncio.get_event_loop().run_until_complete(main())
