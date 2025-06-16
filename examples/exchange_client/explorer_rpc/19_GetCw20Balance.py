import asyncio
import json
import logging

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    network = Network.testnet()
    client = IndexerClient(network=network)

    address = "inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex"

    balance = await client.fetch_cw20_balance(address=address)
    print("Cw20 balance:")
    print(json.dumps(balance, indent=2))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
