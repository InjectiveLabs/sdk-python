import asyncio

from google.protobuf import symbol_database

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)

    port_id = "transfer"
    channel_id = "channel-126"
    sequences = [1, 2]
    pagination = PaginationOption(skip=2, limit=4)

    acknowledgements = await client.fetch_ibc_packet_acknowledgements(
        port_id=port_id,
        channel_id=channel_id,
        packet_commitment_sequences=sequences,
        pagination=pagination,
    )
    print(acknowledgements)


if __name__ == "__main__":
    symbol_db = symbol_database.Default()
    asyncio.get_event_loop().run_until_complete(main())
