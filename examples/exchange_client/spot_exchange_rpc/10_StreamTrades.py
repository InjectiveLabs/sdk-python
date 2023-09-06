import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    market_ids = [
        "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
        "0x7a57e705bb4e09c88aecfc295569481dbf2fe1d5efe364651fbe72385938e9b0"
    ]
    execution_side = "maker"
    direction = "sell"
    subaccount_id = "0xc7dca7c15c364865f77a4fb67ab11dc95502e6fe000000000000000000000001"
    execution_types = ["limitMatchRestingOrder"]
    trades = await client.stream_spot_trades(
        market_ids=market_ids,
        execution_side=execution_side,
        direction=direction,
        subaccount_id=subaccount_id,
        execution_types=execution_types
    )
    async for trade in trades:
        print(trade)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
