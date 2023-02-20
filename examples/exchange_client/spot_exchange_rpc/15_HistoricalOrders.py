import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
    subaccount_id = "0xbdaedec95d563fb05240d6e01821008454c24c36000000000000000000000000"
    skip = 10
    limit = 3
    order_types = ["buy_po"]
    orders = await client.get_historical_spot_orders(
        market_id=market_id,
        subaccount_id=subaccount_id,
        skip=skip,
        limit=limit,
        order_types=order_types
    )
    print(orders)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
