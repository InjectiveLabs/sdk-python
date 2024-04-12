import asyncio

from google.protobuf import symbol_database

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)

    port_id = "transfer"
    channel_id = "channel-126"
    sequences = [1, 2]

    packets = await client.fetch_ibc_unreceived_packets(
        port_id=port_id, channel_id=channel_id, packet_commitment_sequences=sequences
    )
    print(packets)


if __name__ == "__main__":
    symbol_db = symbol_database.Default()
    asyncio.get_event_loop().run_until_complete(main())
