import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    market_ids = ["0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"]
    subaccount_ids = ["0xc6fe5d33615a1c52c08018c47e8bc53646a0e101000000000000000000000000"]
    skip = 0
    limit = 4
    pagination = PaginationOption(skip=skip, limit=limit)
    trades = await client.fetch_derivative_trades(
        market_ids=market_ids, subaccount_ids=subaccount_ids, pagination=pagination
    )
    print(trades)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
