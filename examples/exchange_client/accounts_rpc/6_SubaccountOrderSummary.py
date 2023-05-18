import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    subaccount = "0xaf79152ac5df276d9a8e1e2e22822f9713474902000000000000000000000000"
    order_direction = "buy"
    market_id = "0xe112199d9ee44ceb2697ea0edd1cd422223c105f3ed2bdf85223d3ca59f5909a"
    subacc_order_summary = await client.get_subaccount_order_summary(
        subaccount_id=subaccount,
        # order_direction=order_direction,
        # market_id=market_id
        )
    print(subacc_order_summary)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
