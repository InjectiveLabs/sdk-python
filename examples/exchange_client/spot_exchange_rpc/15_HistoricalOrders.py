import asyncio
import json

from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    network = Network.testnet()
    client = IndexerClient(network)
    market_ids = ["0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"]
    subaccount_id = "0xbdaedec95d563fb05240d6e01821008454c24c36000000000000000000000000"
    skip = 10
    limit = 3
    order_types = ["buy_po"]
    pagination = PaginationOption(skip=skip, limit=limit)
    orders = await client.fetch_spot_orders_history(
        subaccount_id=subaccount_id,
        market_ids=market_ids,
        order_types=order_types,
        pagination=pagination,
    )
    print(json.dumps(orders, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
