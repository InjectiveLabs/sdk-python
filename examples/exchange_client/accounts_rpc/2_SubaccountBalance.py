import asyncio
import json

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    network = Network.testnet()
    client = IndexerClient(network)
    subaccount_id = "0xaf79152ac5df276d9a8e1e2e22822f9713474902000000000000000000000000"
    denom = "inj"
    balance = await client.fetch_subaccount_balance(subaccount_id=subaccount_id, denom=denom)
    print(json.dumps(balance, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
