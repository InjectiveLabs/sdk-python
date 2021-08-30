from decimal import Decimal

"""
One thing you may need to pay more attention to is how to deal with decimals on the Injective Exchange. 
Different cryptocurrencies may require diffrent decimal precisions. More specifically, ERC-20 tokens(e.g. INJ) have 18 decimals whereas USDT/USC have 6 decimals.
So in our system that means ** having 1 INJ is 1e18 inj ** and that ** 1 USDT is actually 100000 peggy0xdac17f958d2ee523a2206206994597c13d831ec7**.

For spot markets, a price reflects the ** relative exchange rate ** between two tokens.
If the tokens have the same decimal scale, that's great since the prices become interpretable e.g. USDT/USDC (both have 6 decimals e.g. for USDT https://etherscan.io/address/0xdac17f958d2ee523a2206206994597c13d831ec7#readContract) 
or MATIC/INJ (both have 18 decimals) since the decimals cancel out.
Prices however start to look wonky once you have exchanges between two tokens of different decimals, which unfortunately is most pairs with USDT or USDC denominations e.g. INJ/USDT.
As such, I've created some simple utility functions by keeping a hardcoded dictionary in injective-py and you can also achieve such utilities by yourself
(e.g. you can use external API like Alchemy's getTokenMetadata to fetch decimal of base and quote asset).

So for INJ/USDT of 6.9, the price you end up getting is 6.9*10 ^ (6 - 18) = 6.9e-12. Note that this market also happens to have a MinPriceTickSize of 1e-15.
This makes sense since since it's defining the minimum price increment of the relative exchange of INJ to USDT.

Note that this market also happens to have a MinQuantityTickSize of 1e15.
This also makes sense since it refers to the minimum INJ quantity tick size each order must have, which is 1e15/1e18 = 0.001 INJ.

"""

def spot_price_conversion_to_send(price, base_decimals, quote_decimals, precision=18) -> str:

    """transfer price[float] to string which satisfies the expected format to be sent to the exchange for spot markets

    Args:
        price ([float]): normal price, you can read it directly in exchange front-end
        base_decimals ([int]): decimals of base asset
        quote_decimals ([int]): decimals of quote asset
        precision (int, optional): [description]. Defaults to 18.
    Returns: 
        str: relative price for base asset and quote asset. For INJ/USDT of 6.9, the price you end up getting is 6.9*10 ^ (6 - 18) = 6.9e-12.
    """

    scale = Decimal(quote_decimals - base_decimals)
    exchange_price = Decimal(price) * pow(10, scale)
    price_string = ("{:."+str(precision)+"f}").format(exchange_price)
    print("price string :{}".format(price_string))
    return price_string

def derivatives_price_conversion_to_send(price, quote_decimals, precision=18) -> str:

    """transfer price[float] to string which satisfies the expected format to be sent to the exchange for derivative markets

    Args:
        price ([float]): normal price, you can read it directly in exchange front-end
        quote_decimals ([int]): decimals of quote asset
        precision (int, optional): [description]. Defaults to 18.
    Returns: 
        str: relative price for the quote asset. For INJ/USDT of 6.9, the price you end up getting is 6.9*10 ^ (6) = 6.9e6.
    """

    exchange_price = Decimal(price) * pow(10, quote_decimals)
    price_string = ("{:."+str(precision)+"f}").format(exchange_price)
    print("price string :{}".format(price_string))
    return price_string

def derivatives_margin_conversion_to_send(margin, quote_decimals, precision=18) -> str:

    """transfer price[float] to string which satisfies the expected format to be sent to the exchange for derivative markets

    Args:
        price ([float]): normal price, you can read it directly in exchange front-end
        quote_decimals ([int]): decimals of quote asset
        precision (int, optional): [description]. Defaults to 18.
    Returns: 
        str: relative price for the quote asset. For INJ/USDT of 6.9, the price you end up getting is 6.9*10 ^ (6) = 6.9e6.
    """

    exchange_price = Decimal(margin) * pow(10, quote_decimals)
    price_string = ("{:."+str(precision)+"f}").format(exchange_price)
    print("price string :{}".format(price_string))
    return price_string

def spot_quantity_conversion_to_send(quantity, base_decimals, precision=18) -> str:

    """transfer price[float] to string which satisfies the expected format to be sent to the exchange for spot markets

    Args:
        quantity ([type]):  normal quantity, you can read it in exchange front-end
        base_decimals ([type]): decimals of base asset
        precision (int, optional): [description]. Defaults to 18.

    Returns:
        str:  actual quantity of base asset[data type: string] For 1 INJ, the quantity you end up getting is 1e18 inj
    """

    scale = Decimal(base_decimals)
    exchange_quantity = Decimal(quantity) * pow(10, scale)
    quantity_string = ("{:."+str(precision)+"f}").format(exchange_quantity)
    print("quantity string:{}".format(quantity_string))
    return quantity_string

def derivatives_quantity_conversion_to_send(quantity, quote_decimals, precision=18) -> str:
    """transfer price[float] to string which satisfies the expected format to be sent to the exchange for derivative markets

    Args:
        quantity ([type]):  normal quantity, you can read it in exchange front-end
        quote_decimals ([type]): decimals of quote asset
        precision (int, optional): [description]. Defaults to 18.

    Returns:
        str:  actual quantity of quote asset[data type: string] For 1 USDT, the quantity you end up is 1.000000000000000000 USDT
    """
    exchange_quantity = Decimal(quantity)
    quantity_string = ("{:."+str(precision)+"f}").format(exchange_quantity)
    print("quantity string :{}".format(quantity_string))
    return quantity_string

def spot_price_conversion_from_backend(price_string, base_decimals, quote_decimals) -> float:

    """
    Args:
        price_string ([type]): price with string data type that injective-exchange backend returns
        base_decimals ([type]): decimal of base asset
        quote_decimals ([type]): decimal of quote asset

    Returns:
        float: actual price what you can read directly from front-end.
        For 6.9e-12 inj/peggy0xdac17f958d2ee523a2206206994597c13d831ec7**, the price you end up getting is 6.9 INJ/USDT.
    """

    scale = float(base_decimals - quote_decimals)
    return float(price_string) * pow(10, scale)

def derivatives_price_conversion_from_backend(price_string, quote_decimals=6) -> float:

    """
    Args:
        price_string ([type]): price with string data type that injective-exchange backend returns
        quote_decimals ([type]): decimals of quote asset. Defaults to 6

    Returns:
        float: actual price which you can read directly from the front-end.
        For 6.9e6 inj/peggy0xdac17f958d2ee523a2206206994597c13d831ec7**, the price you end up getting is 6.9 INJ/USDT.
    """
    
    scale = float(0 - quote_decimals)
    return float(price_string) * pow(10, scale)


def spot_quantity_from_backend(quantity_string, base_decimals) -> float:
    """

    Args:
        quantity_string ([type]): quantity string that injective-exchange backend returns
        base_decimals ([type]): decimal of base asset

    Returns:
        float: actual quantity, for 1e18 inj, you will get 1 INJ
    """
    scale = float(0 - base_decimals)
    return float(quantity_string) * pow(10, scale)


# test
if __name__ == "__main__":
    assert "0.000000005000000000" == price_float_to_string(
        5000, 18, 6, 18), "result of get_price is wrong."

    assert "1222000000000000000000.000000000000000000" == quantity_float_to_string(
        1222, 18, 18), "result of get_quantity is wrong."

    assert 5000 == price_string_to_float(price_float_to_string(
        5000, 18, 6, 18), 18, 6), "something is wrong."

    assert 1222 == quantity_string_to_float(
        quantity_float_to_string(1222, 18, 18), 18), "something is wrong."
