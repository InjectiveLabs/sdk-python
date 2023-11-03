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
    mresp = await client.fetch_spot_markets(market_status=status)
    for market in mresp["markets"]:
        # append symbols to dict
        if market["baseTokenMeta"] != "":
            symbols[market["baseTokenMeta"]["symbol"]] = (market["baseDenom"], market["baseTokenMeta"]["decimals"])

        if market["quoteTokenMeta"] != "":
            symbols[market["quoteTokenMeta"]["symbol"]] = (market["baseDenom"], market["quoteTokenMeta"]["decimals"])

        # format into ini entry
        min_display_price_tick_size = float(market["minPriceTickSize"]) / pow(
            10, market["quoteTokenMeta"]["decimals"] - market["baseTokenMeta"]["decimals"]
        )
        min_display_quantity_tick_size = float(market["minQuantityTickSize"]) / pow(
            10, market["baseTokenMeta"]["decimals"]
        )
        config = metadata_template.format(
            market["marketId"],
            network.string().capitalize(),
            "Spot",
            market["ticker"],
            market["baseTokenMeta"]["decimals"],
            market["quoteTokenMeta"]["decimals"],
            market["minPriceTickSize"],
            min_display_price_tick_size,
            market["minQuantityTickSize"],
            min_display_quantity_tick_size,
        )
        denom_output += config

    # fetch meta data for derivative markets
    client = AsyncClient(network)
    status = "active"
    mresp = await client.get_derivative_markets(market_status=status)
    for market in mresp.markets:
        # append symbols to dict
        if market["quoteTokenMeta"] != "":
            symbols[market["quoteTokenMeta"]["symbol"]] = (market["quoteDenom"], market["quoteTokenMeta"]["decimals"])

            # format into ini entry
        min_display_price_tick_size = float(market["minPriceTickSize"]) / pow(10, market["quoteTokenMeta"]["decimals"])
        config = metadata_template.format(
            market["marketId"],
            network.string().capitalize(),
            "Derivative",
            market["ticker"],
            0,
            market["quoteTokenMeta"]["decimals"],
            market["minPriceTickSize"],
            min_display_price_tick_size,
            market["minQuantityTickSize"],
            market["minQuantityTickSize"],
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
