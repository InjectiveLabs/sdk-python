import asyncio

from google.protobuf import symbol_database

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)

    connection_id = "connection-0"

    state = await client.fetch_ibc_connection_client_state(connection_id=connection_id)
    print(state)


if __name__ == "__main__":
    symbol_db = symbol_database.Default()
    asyncio.get_event_loop().run_until_complete(main())
