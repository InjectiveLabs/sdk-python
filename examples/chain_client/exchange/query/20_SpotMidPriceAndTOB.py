import asyncio

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()

    # initialize grpc client
    client = AsyncClient(network)

    prices = await client.fetch_spot_mid_price_and_tob(
        market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
    )
    print(prices)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
