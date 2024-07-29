import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)

    address = "inj1knhahceyp57j5x7xh69p7utegnnnfgxavmahjr"
    addresses = await client.fetch_permissions_vouchers_for_address(address=address)
    print(addresses)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
