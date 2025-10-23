import asyncio

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()

    # initialize grpc client
    client = AsyncClient(network)

    deposits = await client.fetch_auction_exchange_transfer_denom_decimal(denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5")
    print(deposits)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
