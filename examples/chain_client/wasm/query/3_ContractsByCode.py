import asyncio

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    code_id = 3770
    limit = 2
    pagination = PaginationOption(limit=limit)
    contracts = await client.fetch_contracts_by_code(code_id=code_id, pagination=pagination)
    print(contracts)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
