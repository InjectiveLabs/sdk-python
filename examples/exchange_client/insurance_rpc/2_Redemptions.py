import asyncio
import json

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = IndexerClient(network)
    redeemer = "inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku"
    redemption_denom = "share4"
    status = "disbursed"
    insurance_redemptions = await client.fetch_redemptions(address=redeemer, denom=redemption_denom, status=status)
    print(json.dumps(insurance_redemptions, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
