import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    market_ids = [
        "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
        "0xd5e4b12b19ecf176e4e14b42944731c27677819d2ed93be4104ad7025529c7ff"
    ]
    markets = await client.get_derivative_orderbooks(market_ids=market_ids)
    print(markets)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
