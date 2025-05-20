import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # network: Network = Network.testnet()
    network: Network = Network.testnet()
    client: AsyncClient = AsyncClient(network)

    code_id = 2008

    wasm_code = await client.fetch_wasm_code_by_id(
        code_id=code_id,
    )
    print("Wasm code:")
    print(wasm_code)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
