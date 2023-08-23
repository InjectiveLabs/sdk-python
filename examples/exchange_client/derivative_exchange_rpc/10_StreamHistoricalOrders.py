import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
    order_side = "sell"
    subaccount_id = "0xc6fe5d33615a1c52c08018c47e8bc53646a0e101000000000000000000000000"
    orders = await client.stream_historical_derivative_orders(
        market_id=market_id
    )
    async for order in orders:
        print(order)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
