import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    market = (await client.all_derivative_markets())[
        "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
    ]

    base_symbol = market.oracle_base
    quote_symbol = market.oracle_quote
    oracle_type = market.oracle_type

    oracle_prices = await client.fetch_oracle_price(
        base_symbol=base_symbol,
        quote_symbol=quote_symbol,
        oracle_type=oracle_type,
    )
    print(oracle_prices)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
