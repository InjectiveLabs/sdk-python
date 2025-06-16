import asyncio

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    address = "inj18pp4vjwucpgg4nw3rr4wh4zyjg9ct5t8v9wqgj"
    limit = 2
    pagination = PaginationOption(limit=limit)
    contract_history = await client.fetch_contract_history(address=address, pagination=pagination)
    print(contract_history)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
