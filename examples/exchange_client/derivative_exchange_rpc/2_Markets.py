import asyncio
import json

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = IndexerClient(network)
    market_statuses = ["active"]
    quote_denom = "peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5"
    market = await client.fetch_derivative_markets(market_statuses=market_statuses, quote_denom=quote_denom)
    print(json.dumps(market, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
