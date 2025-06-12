import asyncio
import json

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    network = Network.testnet()
    client = IndexerClient(network)
    account_address = "inj1clw20s2uxeyxtam6f7m84vgae92s9eh7vygagt"
    subacc_list = await client.fetch_subaccounts_list(account_address)
    print(json.dumps(subacc_list, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
