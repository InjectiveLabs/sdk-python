import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    address = "inj1ady3s7whq30l4fx8sj3x6muv5mx4dfdlcpv8n7"
    contract_info = await client.fetch_contract_info(address=address)
    print(contract_info)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
