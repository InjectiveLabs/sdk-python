import asyncio
import json

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    # initialize grpc client
    client = AsyncClient(network)

    balances = await client.fetch_exchange_balances()
    print(json.dumps(balances, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
