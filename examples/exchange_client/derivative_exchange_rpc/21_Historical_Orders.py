import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
    subaccount_id = "0x295639d56c987f0e24d21bb167872b3542a6e05a000000000000000000000000"
    is_conditional = "false"
    skip = 10
    limit = 3
    orders = await client.get_historical_derivative_orders(
        market_id=market_id,
        subaccount_id=subaccount_id,
        skip=skip,
        limit=limit,
        is_conditional=is_conditional,
    )
    print(orders)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
