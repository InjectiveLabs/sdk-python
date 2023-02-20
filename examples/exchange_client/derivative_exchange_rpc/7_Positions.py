import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    market_ids = [
        "0x90e662193fa29a3a7e6c07be4407c94833e762d9ee82136a2cc712d6b87d7de3",
        "0xe112199d9ee44ceb2697ea0edd1cd422223c105f3ed2bdf85223d3ca59f5909a"
    ]
    subaccount_id = "0xc6fe5d33615a1c52c08018c47e8bc53646a0e101000000000000000000000000"
    direction = "short"
    subaccount_total_positions = False
    skip = 4
    limit = 4
    positions = await client.get_derivative_positions(
        market_ids=market_ids,
        # subaccount_id=subaccount_id,
        direction=direction,
        subaccount_total_positions=subaccount_total_positions,
        skip=skip,
        limit=limit
    )
    print(positions)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
