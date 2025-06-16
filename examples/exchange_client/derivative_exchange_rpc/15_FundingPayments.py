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
    subaccount_id = "0xc6fe5d33615a1c52c08018c47e8bc53646a0e101000000000000000000000000"
    skip = 0
    limit = 3
    end_time = 1676426400125
    pagination = PaginationOption(skip=skip, limit=limit, end_time=end_time)
    funding_payments = await client.fetch_funding_payments(
        market_ids=market_ids, subaccount_id=subaccount_id, pagination=pagination
    )
    print(json.dumps(funding_payments, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
