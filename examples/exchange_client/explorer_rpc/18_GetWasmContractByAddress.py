import asyncio
import json
import logging

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    network = Network.testnet()
    client = IndexerClient(network=network)

    address = "inj1yhz4e7df95908jhs9erl87vdzjkdsc24q7afjf"

    wasm_contract = await client.fetch_wasm_contract_by_address(address=address)
    print("Wasm contract:")
    print(json.dumps(wasm_contract, indent=2))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
