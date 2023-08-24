import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
    order_side = "buy"
    subaccount_id = "0xc6fe5d33615a1c52c08018c47e8bc53646a0e101000000000000000000000000"
    orders = await client.stream_historical_spot_orders(
        market_id=market_id,
        order_side=order_side
    )
    async for order in orders:
        print(order)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
