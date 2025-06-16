import asyncio

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()

    # initialize grpc client
    client = AsyncClient(network)

    pagination = PaginationOption(limit=2)

    orderbook = await client.fetch_chain_derivative_orderbook(
        market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
        pagination=pagination,
    )
    print(orderbook)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
