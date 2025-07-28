import asyncio

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    denoms = await client.fetch_denoms_from_creator(creator="inj1maeyvxfamtn8lfyxpjca8kuvauuf2qeu6gtxm3")
    print(denoms)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
