import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    market_ids = [
        "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
        "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
    ]
    execution_side = "maker"
    direction = "sell"
    subaccount_id = "0xc6fe5d33615a1c52c08018c47e8bc53646a0e101000000000000000000000000"
    trades = await client.stream_spot_trades(
        market_id=market_ids[0],
        execution_side=execution_side,
        direction=direction,
        subaccount_id=subaccount_id
    )
    async for trade in trades:
        print(trade)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
