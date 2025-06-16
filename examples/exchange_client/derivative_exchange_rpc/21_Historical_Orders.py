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
    subaccount_id = "0x295639d56c987f0e24d21bb167872b3542a6e05a000000000000000000000000"
    is_conditional = "false"
    skip = 10
    limit = 3
    pagination = PaginationOption(skip=skip, limit=limit)
    orders = await client.fetch_derivative_orders_history(
        subaccount_id=subaccount_id,
        market_ids=market_ids,
        is_conditional=is_conditional,
        pagination=pagination,
    )
    print(json.dumps(orders, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
