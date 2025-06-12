import asyncio

from google.protobuf import symbol_database

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)

    pagination = PaginationOption(skip=2, limit=4)

    states = await client.fetch_ibc_client_states(pagination=pagination)
    print(states)


if __name__ == "__main__":
    symbol_db = symbol_database.Default()
    asyncio.get_event_loop().run_until_complete(main())
