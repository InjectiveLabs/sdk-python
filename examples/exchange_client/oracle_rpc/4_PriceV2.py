import asyncio
import json

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    market = (await client.all_derivative_markets())[
        "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
    ]

    filter = client.oracle_price_v2_filter(
        base_symbol=market.oracle_base,
        quote_symbol=market.oracle_quote,
        oracle_type=market.oracle_type,
    )
    oracle_prices = await client.fetch_oracle_price_v2(filters=[filter])
    print(json.dumps(oracle_prices, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
