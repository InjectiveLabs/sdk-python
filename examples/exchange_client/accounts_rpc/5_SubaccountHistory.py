import asyncio
import json

from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    network = Network.testnet()
    client = IndexerClient(network)
    subaccount = "0xaf79152ac5df276d9a8e1e2e22822f9713474902000000000000000000000000"
    denom = "inj"
    transfer_types = ["withdraw", "deposit"]
    skip = 1
    limit = 15
    end_time = 1665118340224
    pagination = PaginationOption(skip=skip, limit=limit, end_time=end_time)
    subacc_history = await client.fetch_subaccount_history(
        subaccount_id=subaccount,
        denom=denom,
        transfer_types=transfer_types,
        pagination=pagination,
    )
    print(json.dumps(subacc_history, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
