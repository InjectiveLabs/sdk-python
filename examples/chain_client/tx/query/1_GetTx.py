import asyncio

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.devnet()
    client = AsyncClient(network)
    tx_hash = "EA598BB5297341636DD62D378DEB87ECE6F95AFB4F45966AA6A53D36EF022DA5"
    tx_logs = await client.fetch_tx(hash=tx_hash)
    print(tx_logs)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
