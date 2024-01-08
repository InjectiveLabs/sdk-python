import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    market_ids = ["0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"]
    execution_side = "taker"
    direction = "buy"
    subaccount_ids = ["0xc7dca7c15c364865f77a4fb67ab11dc95502e6fe000000000000000000000001"]
    execution_types = ["limitMatchNewOrder", "market"]
    orders = await client.fetch_spot_trades(
        market_ids=market_ids,
        subaccount_ids=subaccount_ids,
        execution_side=execution_side,
        direction=direction,
        execution_types=execution_types,
    )
    print(orders)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
