import asyncio
import json

from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = IndexerClient(network)
    subaccount_id = "0xaf79152ac5df276d9a8e1e2e22822f9713474902000000000000000000000000"
    market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
    execution_type = "market"
    direction = "sell"
    skip = 10
    limit = 2
    pagination = PaginationOption(skip=skip, limit=limit)
    trades = await client.fetch_derivative_subaccount_trades_list(
        subaccount_id=subaccount_id,
        market_id=market_id,
        execution_type=execution_type,
        direction=direction,
        pagination=pagination,
    )
    print(json.dumps(trades, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
