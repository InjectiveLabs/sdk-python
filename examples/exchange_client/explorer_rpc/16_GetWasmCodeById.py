import asyncio
import json
import logging

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    network = Network.testnet()
    client = IndexerClient(network=network)

    code_id = 2008

    wasm_code = await client.fetch_wasm_code_by_id(
        code_id=code_id,
    )
    print("Wasm code:")
    print(json.dumps(wasm_code, indent=2))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
