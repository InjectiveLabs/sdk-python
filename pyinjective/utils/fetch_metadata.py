import asyncio
from decimal import Decimal

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network

metadata_template = """[{}]
description = '{} {} {}'
base = {}
quote = {}
min_price_tick_size = {}
min_display_price_tick_size = {}
min_quantity_tick_size = {}
min_display_quantity_tick_size = {}
min_notional = {}

"""

symbol_template = """[{}]
peggy_denom = {}
decimals = {}

"""

testnet_denom_output = ""
mainnet_denom_output = ""


async def fetch_denom(network) -> str:
    denom_output = ""

    # fetch meta data for spot markets
    client = AsyncClient(network)
    spot_markets = await client.all_spot_markets()
    for market in spot_markets.values():
        min_display_price_tick_size = market.min_price_tick_size / Decimal(
            f"1e{market.quote_token.decimals - market.base_token.decimals}"
        )
        min_display_quantity_tick_size = market.min_quantity_tick_size / Decimal(f"1e{market.base_token.decimals}")
        config = metadata_template.format(
            market.id,
            network.string().capitalize(),
            "Spot",
            market.ticker,
            market.base_token.decimals,
            market.quote_token.decimals,
            f"{market.min_price_tick_size.normalize():f}",
            f"{min_display_price_tick_size.normalize():f}",
            f"{market.min_quantity_tick_size.normalize():f}",
            f"{min_display_quantity_tick_size.normalize():f}",
            f"{market.min_notional.normalize():f}",
        )
        denom_output += config

    # fetch meta data for derivative markets
    client = AsyncClient(network)
    derivative_markets = await client.all_derivative_markets()
    for market in derivative_markets.values():
        min_display_price_tick_size = market.min_price_tick_size / Decimal(f"1e{market.quote_token.decimals}")
        config = metadata_template.format(
            market.id,
            network.string().capitalize(),
            "Derivative",
            market.ticker,
            0,
            market.quote_token.decimals,
            f"{market.min_price_tick_size.normalize():f}",
            f"{min_display_price_tick_size.normalize():f}",
            f"{market.min_quantity_tick_size.normalize():f}",
            f"{market.min_quantity_tick_size.normalize():f}",
            f"{market.min_notional.normalize():f}",
        )
        denom_output += config

    tokens = await client.all_tokens()
    for token_symbol, token in sorted(tokens.items(), key=lambda dict_item: dict_item[0]):
        symbol = symbol_template.format(token_symbol, token.denom, token.decimals)
        denom_output += symbol

    return denom_output


async def main() -> None:
    devnet = Network.devnet()
    data = await fetch_denom(devnet)
    with open("../denoms_devnet.ini", "w") as text_file:
        text_file.write(data)

    testnet = Network.testnet()
    data = await fetch_denom(testnet)
    with open("../denoms_testnet.ini", "w") as text_file:
        text_file.write(data)

    mainnet = Network.mainnet()
    data = await fetch_denom(mainnet)
    with open("../denoms_mainnet.ini", "w") as text_file:
        text_file.write(data)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
