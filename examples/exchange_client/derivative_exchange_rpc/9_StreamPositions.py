import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
    subaccount_id = "0xea98e3aa091a6676194df40ac089e40ab4604bf9000000000000000000000000"
    positions = await client.stream_derivative_positions(market_id=market_id, subaccount_id=subaccount_id)
    async for position in positions:
        print(position)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
