import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    redeemer = "inj1gxqdj76ul07w4ujsl8403nhhzyvug2h66qk057"
    redemption_denom = "share2"
    status = "disbursed"
    insurance_redemptions = await client.get_redemptions(
        redeemer=redeemer,
        redemption_denom=redemption_denom,
        status=status
    )
    print(insurance_redemptions)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
