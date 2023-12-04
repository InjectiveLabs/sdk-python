import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    limit = 2
    pagination = PaginationOption(limit=limit)
    txs = await client.fetch_txs(pagination=pagination)
    print(txs)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
