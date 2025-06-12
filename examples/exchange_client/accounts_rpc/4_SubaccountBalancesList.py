import asyncio
import json

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    network = Network.testnet()
    client = IndexerClient(network)
    subaccount = "0xaf79152ac5df276d9a8e1e2e22822f9713474902000000000000000000000000"
    denoms = ["inj", "peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5"]
    subacc_balances_list = await client.fetch_subaccount_balances_list(subaccount_id=subaccount, denoms=denoms)
    print(json.dumps(subacc_balances_list, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
