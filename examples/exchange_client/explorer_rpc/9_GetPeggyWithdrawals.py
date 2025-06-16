import asyncio
import json

from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = IndexerClient(network=network)
    sender = "inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku"
    limit = 2
    pagination = PaginationOption(limit=limit)
    peggy_deposits = await client.fetch_peggy_withdrawal_txs(sender=sender, pagination=pagination)
    print(json.dumps(peggy_deposits, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
