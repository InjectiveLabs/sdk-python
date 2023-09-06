import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    subaccount_id = "0xc7dca7c15c364865f77a4fb67ab11dc95502e6fe000000000000000000000001"
    denoms = ["inj", "peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5"]
    subaccount = await client.stream_subaccount_balance(
        subaccount_id=subaccount_id,
        denoms=denoms
    )
    async for balance in subaccount:
        print("Subaccount balance Update:\n")
        print(balance)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
