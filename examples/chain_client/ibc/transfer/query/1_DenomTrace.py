import asyncio
from hashlib import sha256

from google.protobuf import symbol_database

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)

    path = "transfer/channel-126"
    base_denom = "uluna"
    full_path = f"{path}/{base_denom}"
    path_hash = sha256(full_path.encode()).hexdigest()
    trace_hash = f"ibc/{path_hash}"

    denom_trace = await client.fetch_denom_trace(hash=trace_hash)
    print(denom_trace)


if __name__ == "__main__":
    symbol_db = symbol_database.Default()
    asyncio.get_event_loop().run_until_complete(main())
