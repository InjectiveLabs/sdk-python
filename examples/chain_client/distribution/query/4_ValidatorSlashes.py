import asyncio

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    limit = 2
    pagination = PaginationOption(limit=limit)
    validator_address = "injvaloper1jue5dpr9lerjn6wlwtrywxrsenrf28ru89z99z"
    contracts = await client.fetch_validator_slashes(validator_address=validator_address, pagination=pagination)
    print(contracts)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
