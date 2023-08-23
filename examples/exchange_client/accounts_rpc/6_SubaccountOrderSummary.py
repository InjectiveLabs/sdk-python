import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    subaccount = "0xaf79152ac5df276d9a8e1e2e22822f9713474902000000000000000000000000"
    order_direction = "buy"
    market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
    subacc_order_summary = await client.get_subaccount_order_summary(
        subaccount_id=subaccount,
        # order_direction=order_direction,
        # market_id=market_id
        )
    print(subacc_order_summary)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
