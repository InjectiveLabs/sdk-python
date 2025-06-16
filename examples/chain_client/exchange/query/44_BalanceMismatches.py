import asyncio

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()

    # initialize grpc client
    client = AsyncClient(network)

    mismatches = await client.fetch_balance_mismatches(dust_factor=1)
    print(mismatches)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
