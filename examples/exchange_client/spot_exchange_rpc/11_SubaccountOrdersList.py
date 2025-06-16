import asyncio
import json

from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = IndexerClient(network)
    subaccount_id = "0xc7dca7c15c364865f77a4fb67ab11dc95502e6fe000000000000000000000001"
    market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
    skip = 10
    limit = 10
    pagination = PaginationOption(skip=skip, limit=limit)
    orders = await client.fetch_spot_subaccount_orders_list(
        subaccount_id=subaccount_id, market_id=market_id, pagination=pagination
    )
    print(json.dumps(orders, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
