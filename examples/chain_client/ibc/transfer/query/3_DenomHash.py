import asyncio

from google.protobuf import symbol_database

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)

    path = "transfer/channel-126"
    base_denom = "uluna"
    full_path = f"{path}/{base_denom}"

    denom_hash = await client.fetch_denom_hash(trace=full_path)
    print(denom_hash)


if __name__ == "__main__":
    symbol_db = symbol_database.Default()
    asyncio.get_event_loop().run_until_complete(main())
