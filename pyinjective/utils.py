from decimal import Decimal
from math import floor

"""
One thing you may need to pay more attention to is how to deal with decimals on the Injective Exchange.
Different cryptocurrencies may require different decimal precisions. More specifically, ERC-20 tokens(e.g. INJ) have 18 decimals whereas USDT/USC have 6 decimals.
So in our system that means ** having 1 INJ is 1e18 inj ** and that ** 1 USDT is actually 100000 peggy0xdac17f958d2ee523a2206206994597c13d831ec7**.

For spot markets, a price reflects the ** relative exchange rate ** between two tokens.
If the tokens have the same decimal scale, that's great since the prices become interpretable e.g. USDT/USDC (both have 6 decimals e.g. for USDT https://etherscan.io/address/0xdac17f958d2ee523a2206206994597c13d831ec7#readContract)
or MATIC/INJ (both have 18 decimals) since the decimals cancel out.
Prices however start to look wonky once you have exchanges between two tokens of different decimals, which unfortunately is most pairs with USDT or USDC denominations e.g. INJ/USDT.
As such, I've created some simple utility functions by keeping a hardcoded dictionary in injective-py and you can also achieve such utilities by yourself
(e.g. you can use external API like Alchemy's getTokenMetadata to fetch decimal of base and quote asset).

So for INJ/USDT of 6.9, the price you end up getting is 6.9*10 ^ (6 - 18) = 6.9e-12. Note that this market also happens to have a MinPriceTickSize of 1e-15.
This makes sense since since it's defining th3e minimum price increment of the relative exchange of INJ to USDT.

Note that this market also happens to have a MinQuantityTickSize of 1e15.
This also makes sense since it refers to the minimum INJ quantity tick size each order must have, which is 1e15/1e18 = 0.001 INJ.

"""

def spot_price_to_backend(price, denom) -> int:
    price_tick_size = denom.min_price_tick_size
    scale_price = Decimal(18 + denom.quote - denom.base)
    exchange_price = floor_to(price, price_tick_size) * pow(Decimal(10), scale_price)
    return int(exchange_price)

def spot_quantity_to_backend(quantity, denom) -> int:
    quantity_tick_size = float(denom.min_quantity_tick_size) / pow(10, denom.base)
    scale_quantity = Decimal(18 + denom.base)
    exchange_quantity = floor_to(quantity, quantity_tick_size) * pow(Decimal(10), scale_quantity)
    return int(exchange_quantity)

def derivative_price_to_backend(price, denom) -> int:
    price_tick_size = Decimal(denom.min_price_tick_size) / pow(10, denom.quote)
    exchange_price = floor_to(price, float(price_tick_size)) * pow(10, 18 + denom.quote)
    return int(exchange_price)

def binary_options_price_to_backend(price, denom) -> int:
    price_tick_size = Decimal(denom.min_price_tick_size) / pow(10, denom.quote)
    exchange_price = floor_to(price, float(price_tick_size)) * pow(10, 18 + denom.quote)
    return int(exchange_price)

def derivative_quantity_to_backend(quantity, denom) -> int:
    quantity_tick_size = float(denom.min_quantity_tick_size) / pow(10, denom.base)
    scale_quantity = Decimal(18 + denom.base)
    exchange_quantity = floor_to(quantity, quantity_tick_size) * pow(Decimal(10), scale_quantity)
    return int(exchange_quantity)

def binary_options_quantity_to_backend(quantity, denom) -> int:
    quantity_tick_size = float(denom.min_quantity_tick_size) / pow(10, denom.base)
    scale_quantity = Decimal(18 + denom.base)
    exchange_quantity = floor_to(quantity, quantity_tick_size) * pow(Decimal(10), scale_quantity)
    return int(exchange_quantity)

def derivative_margin_to_backend(price, quantity, leverage, denom) -> int:
    price_tick_size = Decimal(denom.min_price_tick_size) / pow(10, denom.quote)
    margin = (price * quantity) / leverage
    exchange_margin = floor_to(margin, float(price_tick_size)) * pow(10, 18 + denom.quote)
    return int(exchange_margin)

def binary_options_buy_margin_to_backend(price, quantity, denom) -> int:
    price_tick_size = Decimal(denom.min_price_tick_size) / pow(10, denom.quote)
    margin = Decimal(str(price)) * Decimal(str(quantity))
    exchange_margin = floor_to(margin, float(price_tick_size)) * pow(10, 18 + denom.quote)
    return int(exchange_margin)

def binary_options_sell_margin_to_backend(price, quantity, denom) -> int:
    price_tick_size = Decimal(denom.min_price_tick_size) / pow(10, denom.quote)
    margin = (1 - (Decimal(str(price)))) * (Decimal(str(quantity)))
    exchange_margin = floor_to(margin, float(price_tick_size)) * pow(10, 18 + denom.quote)
    return int(exchange_margin)

def derivative_additional_margin_to_backend(amount, denom) -> int:
    price_tick_size = float(denom.min_price_tick_size) / pow(10, denom.quote)
    additional_margin = floor_to(amount, price_tick_size) * pow(10, 18 + denom.quote)
    return int(additional_margin)

def amount_to_backend(amount, decimals) -> int:
    be_amount = amount * pow(10, decimals)
    return int(be_amount)

def floor_to(value: float, target: float) -> Decimal:
    value_tmp = Decimal(str(value))
    target_tmp = Decimal(str(target))
    result = int(floor(value_tmp / target_tmp)) * target_tmp
    return result

def spot_price_from_backend(price, denom) -> float:
    scale = float(denom.quote - denom.base)
    return float(price) / pow(10, scale)

def spot_quantity_from_backend(quantity, denom) -> Decimal:
    scale = float(denom.base)
    quantity_tick_size = float(denom.min_quantity_tick_size) / pow(10, scale)
    quantity = float(quantity) / pow(10, scale)
    return floor_to(quantity, quantity_tick_size)

def derivative_price_from_backend(price, denom) -> float:
    scale = float(denom.quote)
    return float(price) / pow(10, scale)
