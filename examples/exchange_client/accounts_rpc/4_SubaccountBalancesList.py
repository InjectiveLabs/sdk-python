import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    subaccount = "0xaf79152ac5df276d9a8e1e2e22822f9713474902000000000000000000000000"
    denoms = ["inj", "peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5"]
    subacc_balances_list = await client.get_subaccount_balances_list(
        subaccount_id=subaccount,
        denoms=denoms
    )
    print(subacc_balances_list)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
