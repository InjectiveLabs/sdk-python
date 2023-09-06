import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    redeemer = "inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku"
    redemption_denom = "share4"
    status = "disbursed"
    insurance_redemptions = await client.get_redemptions(
        redeemer=redeemer,
        redemption_denom=redemption_denom,
        status=status
    )
    print(insurance_redemptions)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
