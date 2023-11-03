import asyncio
from decimal import Decimal
from typing import Any, List, Tuple

import pyinjective.constant as constant
import pyinjective.utils.denom
from pyinjective.async_client import AsyncClient
from pyinjective.core.market import BinaryOptionMarket, DerivativeMarket, SpotMarket
from pyinjective.core.network import Network


def find_metadata_inconsistencies(network: Network) -> Tuple[List[Any]]:
    client = AsyncClient(network)
    ini_config = constant.CONFIGS[network.string()]

    spot_markets = asyncio.get_event_loop().run_until_complete(client.all_spot_markets())
    derivative_markets = asyncio.get_event_loop().run_until_complete(client.all_derivative_markets())
    binary_option_markets = asyncio.get_event_loop().run_until_complete(client.all_binary_option_markets())
    all_tokens = asyncio.get_event_loop().run_until_complete(client.all_tokens())

    markets_not_found = []
    markets_with_diffs = []
    peggy_denoms_not_found = []
    peggy_denoms_with_diffs = []

    for config_key in ini_config:
        if config_key.startswith("0x"):
            denom = pyinjective.utils.denom.Denom.load_market(network=network.string(), market_id=config_key)
            if config_key in spot_markets:
                market: SpotMarket = spot_markets[config_key]
                if (
                    market.base_token.decimals != denom.base
                    or market.quote_token.decimals != denom.quote
                    or market.min_price_tick_size != Decimal(str(denom.min_price_tick_size))
                    or market.min_quantity_tick_size != Decimal(str(denom.min_quantity_tick_size))
                ):
                    markets_with_diffs.append(
                        [
                            {
                                "denom-market": config_key,
                                "base_decimals": denom.base,
                                "quote_decimals": denom.quote,
                                "min_quantity_tick_size": denom.min_quantity_tick_size,
                                "min_price_tick_size": denom.min_price_tick_size,
                            },
                            {
                                "newer-market": market.id,
                                "base_decimals": market.base_token.decimals,
                                "quote_decimals": market.quote_token.decimals,
                                "min_quantity_tick_size": float(market.min_quantity_tick_size),
                                "min_price_tick_size": float(market.min_price_tick_size),
                                "ticker": market.ticker,
                            },
                        ]
                    )
            elif config_key in derivative_markets:
                market: DerivativeMarket = derivative_markets[config_key]
                if (
                    market.quote_token.decimals != denom.quote
                    or market.min_price_tick_size != Decimal(str(denom.min_price_tick_size))
                    or market.min_quantity_tick_size != Decimal(str(denom.min_quantity_tick_size))
                ):
                    markets_with_diffs.append(
                        [
                            {
                                "denom-market": config_key,
                                "quote_decimals": denom.quote,
                                "min_quantity_tick_size": denom.min_quantity_tick_size,
                                "min_price_tick_size": denom.min_price_tick_size,
                            },
                            {
                                "newer-market": market.id,
                                "quote_decimals": market.quote_token.decimals,
                                "min_quantity_tick_size": float(market.min_quantity_tick_size),
                                "min_price_tick_size": float(market.min_price_tick_size),
                                "ticker": market.ticker,
                            },
                        ]
                    )
            elif config_key in binary_option_markets:
                market: BinaryOptionMarket = binary_option_markets[config_key]
                if (
                    market.quote_token.decimals != denom.quote
                    or market.min_price_tick_size != Decimal(str(denom.min_price_tick_size))
                    or market.min_quantity_tick_size != Decimal(str(denom.min_quantity_tick_size))
                ):
                    markets_with_diffs.append(
                        [
                            {
                                "denom-market": config_key,
                                "quote_decimals": denom.quote,
                                "min_quantity_tick_size": denom.min_quantity_tick_size,
                                "min_price_tick_size": denom.min_price_tick_size,
                            },
                            {
                                "newer-market": market.id,
                                "quote_decimals": market.quote_token.decimals,
                                "min_quantity_tick_size": float(market.min_quantity_tick_size),
                                "min_price_tick_size": float(market.min_price_tick_size),
                                "ticker": market.ticker,
                            },
                        ]
                    )
            else:
                markets_not_found.append({"denom-market": config_key, "description": denom.description})

        elif config_key == "DEFAULT":
            continue
        else:
            # the configuration is a token
            peggy_denom, decimals = pyinjective.utils.denom.Denom.load_peggy_denom(
                network=network.string(), symbol=config_key
            )
            if config_key in all_tokens:
                token = all_tokens[config_key]
                if token.denom != peggy_denom or token.decimals != decimals:
                    peggy_denoms_with_diffs.append(
                        [
                            {"denom_token": config_key, "peggy_denom": peggy_denom, "decimals": decimals},
                            {"newer_token": token.symbol, "peggy_denom": token.denom, "decimals": token.decimals},
                        ]
                    )
            else:
                peggy_denoms_not_found.append(
                    {"denom_token": config_key, "peggy_denom": peggy_denom, "decimals": decimals}
                )

    return markets_with_diffs, markets_not_found, peggy_denoms_with_diffs, peggy_denoms_not_found


def print_metadata_mismatches(network: Network):
    (
        markets_with_diffs,
        markets_not_found,
        peggy_denoms_with_diffs,
        peggy_denoms_not_found,
    ) = find_metadata_inconsistencies(network=network)

    for diff_pair in markets_with_diffs:
        print(f"{diff_pair[0]}\n{diff_pair[1]}")
    print("\n\n")
    for missing_market in markets_not_found:
        print(f"{missing_market}")
    print("\n\n")
    for diff_token in peggy_denoms_with_diffs:
        print(f"{diff_token[0]}\n{diff_token[1]}")
    print("\n\n")
    for missing_peggy in peggy_denoms_not_found:
        print(f"{missing_peggy}")
