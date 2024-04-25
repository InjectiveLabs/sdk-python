import asyncio

from google.protobuf import symbol_database

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)

    connection_id = "connection-0"

    connection = await client.fetch_ibc_connection(connection_id=connection_id)
    print(connection)


if __name__ == "__main__":
    symbol_db = symbol_database.Default()
    asyncio.get_event_loop().run_until_complete(main())
