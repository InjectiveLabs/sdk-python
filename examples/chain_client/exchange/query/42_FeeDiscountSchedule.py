import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()

    # initialize grpc client
    client = AsyncClient(network)

    schedule = await client.fetch_fee_discount_schedule()
    print(schedule)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
