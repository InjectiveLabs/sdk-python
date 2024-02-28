import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    tx_hash = "D265527E3171C47D01D7EC9B839A95F8F794D4E683F26F5564025961C96EFDDA"
    tx_logs = await client.fetch_tx(hash=tx_hash)
    print(tx_logs)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
