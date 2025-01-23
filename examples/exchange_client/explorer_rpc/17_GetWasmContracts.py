import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network


async def main() -> None:
    # network: Network = Network.testnet()
    network: Network = Network.testnet()
    client: AsyncClient = AsyncClient(network)

    pagination = PaginationOption(
        limit=10,
        from_number=1000,
        to_number=2000,
    )

    wasm_contracts = await client.fetch_wasm_contracts(
        assets_only=True,
        pagination=pagination,
    )
    print("Wasm contracts:")
    print(wasm_contracts)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
