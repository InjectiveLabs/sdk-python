import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    base_symbol = "BTC"
    quote_symbol = "USDT"
    oracle_type = "bandibc"
    oracle_prices = await client.stream_oracle_prices(
        base_symbol=base_symbol, quote_symbol=quote_symbol, oracle_type=oracle_type
    )
    async for oracle in oracle_prices:
        print(oracle)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
