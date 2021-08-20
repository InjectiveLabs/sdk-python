from decimal import Decimal


def price_float_to_string(price, base_decimals, quote_decimals, precision=18) -> str:
    scale = Decimal(quote_decimals - base_decimals)
    exchange_price = Decimal(price) * pow(10, scale)
    price_string = ("{:."+str(precision)+"f}").format(exchange_price)
    print("price string :{}".format(price_string))
    return price_string


def quantity_float_to_string(quantity, base_decimals, precision=18) -> str:
    scale = Decimal(base_decimals)
    exchange_quantity = Decimal(quantity) * pow(10, scale)
    quantity_string = ("{:."+str(precision)+"f}").format(exchange_quantity)
    print("quantity string:{}".format(quantity_string))
    return quantity_string


def price_string_to_float(price_string, base_decimals, quote_decimals) -> float:
    scale = float(base_decimals - quote_decimals)
    return float(price_string) * pow(10, scale)


def quantity_string_to_float(quantity_string, base_decimals) -> float:
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
