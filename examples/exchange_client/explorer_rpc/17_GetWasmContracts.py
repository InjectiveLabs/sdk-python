import asyncio
import json
import logging

from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    network = Network.testnet()
    client = IndexerClient(network=network)

    pagination = PaginationOption(
        limit=10,
        from_number=1000,
        to_number=2000,
    )

    wasm_contracts = await client.fetch_wasm_contracts(
        assets_only=True,
        pagination=pagination,
    )
    print("Wasm contracts:")
    print(json.dumps(wasm_contracts, indent=2))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
