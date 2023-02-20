import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    subaccount_id = "0xaf79152ac5df276d9a8e1e2e22822f9713474902000000000000000000000000"
    market_id = "0xe112199d9ee44ceb2697ea0edd1cd422223c105f3ed2bdf85223d3ca59f5909a"
    skip = 1
    limit = 2
    orders = await client.get_derivative_subaccount_orders(
        subaccount_id=subaccount_id,
        market_id=market_id,
        skip=skip,
        limit=limit
    )
    print(orders)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
