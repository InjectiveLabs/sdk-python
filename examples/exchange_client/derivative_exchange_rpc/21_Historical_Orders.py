import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    market_id = "0x90e662193fa29a3a7e6c07be4407c94833e762d9ee82136a2cc712d6b87d7de3"
    subaccount_id = "0x295639d56c987f0e24d21bb167872b3542a6e05a000000000000000000000000"
    is_conditional = "false"
    skip = 10
    limit = 3
    orders = await client.get_historical_derivative_orders(
        market_id=market_id,
        subaccount_id=subaccount_id,
        skip=skip,
        limit=limit,
        is_conditional=is_conditional,
    )
    print(orders)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
