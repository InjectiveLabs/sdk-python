import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    subaccount_id = "0xc7dca7c15c364865f77a4fb67ab11dc95502e6fe000000000000000000000001"
    market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
    skip = 10
    limit = 10
    orders = await client.get_spot_subaccount_orders(
        subaccount_id=subaccount_id,
        market_id=market_id,
        skip=skip,
        limit=limit
    )
    print(orders)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
