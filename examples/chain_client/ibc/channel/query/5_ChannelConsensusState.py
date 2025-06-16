import asyncio

from google.protobuf import symbol_database

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)

    port_id = "transfer"
    channel_id = "channel-126"
    revision_number = 1
    revision_height = 7990906

    state = await client.fetch_ibc_channel_consensus_state(
        port_id=port_id, channel_id=channel_id, revision_number=revision_number, revision_height=revision_height
    )
    print(state)


if __name__ == "__main__":
    symbol_db = symbol_database.Default()
    asyncio.get_event_loop().run_until_complete(main())
