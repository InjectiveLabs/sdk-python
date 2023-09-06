import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    market_ids = [
        "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
        "0xd97d0da6f6c11710ef06315971250e4e9aed4b7d4cd02059c9477ec8cf243782"
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
    asyncio.get_event_loop().run_until_complete(main())
