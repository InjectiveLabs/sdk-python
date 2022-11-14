import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    subaccount = "0xaf79152ac5df276d9a8e1e2e22822f9713474902000000000000000000000000"
    denom = "inj"
    transfer_types = ["withdraw", "deposit"]
    skip = 10
    limit = 10
    subacc_history = await client.get_subaccount_history(
        subaccount_id=subaccount,
        denom=denom,
        transfer_types=transfer_types,
        skip=skip,
        limit=limit
    )
    print(subacc_history)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
