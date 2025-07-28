import asyncio
import json

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = IndexerClient(network=network)
    receiver = "inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex"
    peggy_deposits = await client.fetch_peggy_deposit_txs(receiver=receiver)
    print(json.dumps(peggy_deposits, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
