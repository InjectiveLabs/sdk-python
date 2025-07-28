import asyncio
import json

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = IndexerClient(network)
    bid_round = 31
    auction = await client.fetch_auction(round=bid_round)
    print(json.dumps(auction, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
