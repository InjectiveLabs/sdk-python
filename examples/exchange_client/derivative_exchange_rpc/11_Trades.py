import asyncio
import json

from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = IndexerClient(network)
    market_ids = ["0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"]
    subaccount_ids = ["0xc6fe5d33615a1c52c08018c47e8bc53646a0e101000000000000000000000000"]
    skip = 0
    limit = 4
    pagination = PaginationOption(skip=skip, limit=limit)
    trades = await client.fetch_derivative_trades(
        market_ids=market_ids, subaccount_ids=subaccount_ids, pagination=pagination
    )
    print(json.dumps(trades, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
