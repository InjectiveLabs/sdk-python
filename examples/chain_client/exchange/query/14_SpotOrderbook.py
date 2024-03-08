import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()

    # initialize grpc client
    client = AsyncClient(network)

    pagination = PaginationOption(limit=2)

    orderbook = await client.fetch_chain_spot_orderbook(
        market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
        order_side="Buy",
        pagination=pagination,
    )
    print(orderbook)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
