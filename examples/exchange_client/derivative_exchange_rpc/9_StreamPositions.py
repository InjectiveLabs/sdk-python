import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    market_id = "0x90e662193fa29a3a7e6c07be4407c94833e762d9ee82136a2cc712d6b87d7de3"
    subaccount_id = "0xea98e3aa091a6676194df40ac089e40ab4604bf9000000000000000000000000"
    positions = await client.stream_derivative_positions(
        market_id=market_id,
        subaccount_id=subaccount_id
    )
    async for position in positions:
        print(position)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
