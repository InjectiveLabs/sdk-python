import asyncio

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()

    # initialize grpc client
    client = AsyncClient(network)

    market_id = await client.fetch_market_id_from_vault(vault_address="inj1qg5ega6dykkxc307y25pecuufrjkxkag6xhp6y")
    print(market_id)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
