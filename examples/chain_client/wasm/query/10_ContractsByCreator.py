import asyncio

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    creator = "inj1h3gepa4tszh66ee67he53jzmprsqc2l9npq3ty"
    limit = 2
    pagination = PaginationOption(limit=limit)
    response = await client.fetch_contracts_by_creator(creator_address=creator, pagination=pagination)
    print(response)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
