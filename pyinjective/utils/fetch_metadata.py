import asyncio

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

"""

symbol_template = """[{}]
peggy_denom = {}
decimals = {}

"""

testnet_denom_output = ""
mainnet_denom_output = ""


async def fetch_denom(network) -> str:
    denom_output = ""
    symbols = {}

    # fetch meta data for spot markets
    client = AsyncClient(network)
    status = "active"
    mresp = await client.get_spot_markets(market_status=status)
    for market in mresp.markets:
        # append symbols to dict
        if market.base_token_meta.SerializeToString() != "":
            symbols[market.base_token_meta.symbol] = (market.base_denom, market.base_token_meta.decimals)

        if market.quote_token_meta.SerializeToString() != "":
            symbols[market.quote_token_meta.symbol] = (market.base_denom, market.quote_token_meta.decimals)

        # format into ini entry
        min_display_price_tick_size = float(market.min_price_tick_size) / pow(
            10, market.quote_token_meta.decimals - market.base_token_meta.decimals
        )
        min_display_quantity_tick_size = float(market.min_quantity_tick_size) / pow(10, market.base_token_meta.decimals)
        config = metadata_template.format(
            market.market_id,
            network.string().capitalize(),
            "Spot",
            market.ticker,
            market.base_token_meta.decimals,
            market.quote_token_meta.decimals,
            market.min_price_tick_size,
            min_display_price_tick_size,
            market.min_quantity_tick_size,
            min_display_quantity_tick_size,
        )
        denom_output += config

    # fetch meta data for derivative markets
    client = AsyncClient(network)
    status = "active"
    mresp = await client.get_derivative_markets(market_status=status)
    for market in mresp.markets:
        # append symbols to dict
        if market.quote_token_meta.SerializeToString() != "":
            symbols[market.quote_token_meta.symbol] = (market.quote_denom, market.quote_token_meta.decimals)

            # format into ini entry
        min_display_price_tick_size = float(market.min_price_tick_size) / pow(10, market.quote_token_meta.decimals)
        config = metadata_template.format(
            market.market_id,
            network.string().capitalize(),
            "Derivative",
            market.ticker,
            0,
            market.quote_token_meta.decimals,
            market.min_price_tick_size,
            min_display_price_tick_size,
            market.min_quantity_tick_size,
            market.min_quantity_tick_size,
        )
        denom_output += config

    # format into ini entry
    for key in symbols:
        peggy_id, decimals = symbols[key]
        symbol = symbol_template.format(key, peggy_id, decimals)
        denom_output += symbol

    return denom_output


async def main() -> None:
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
