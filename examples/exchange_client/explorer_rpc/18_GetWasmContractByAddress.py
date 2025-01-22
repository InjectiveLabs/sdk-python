import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # network: Network = Network.testnet()
    network: Network = Network.testnet()
    client: AsyncClient = AsyncClient(network)

    address = "inj1yhz4e7df95908jhs9erl87vdzjkdsc24q7afjf"

    wasm_contract = await client.fetch_wasm_contract_by_address(address=address)
    print("Wasm contract:")
    print(wasm_contract)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
