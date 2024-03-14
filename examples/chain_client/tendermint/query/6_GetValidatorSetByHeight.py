import asyncio

from google.protobuf import symbol_database

from pyinjective.async_client import AsyncClient
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)

    pagination = PaginationOption(skip=2, limit=4)

    validator_set = await client.fetch_validator_set_by_height(height=23040174, pagination=pagination)
    print(validator_set)


if __name__ == "__main__":
    symbol_db = symbol_database.Default()
    asyncio.get_event_loop().run_until_complete(main())
