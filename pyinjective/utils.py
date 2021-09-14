from decimal import Decimal
from math import floor

import grpc

import pyinjective.proto.exchange.injective_spot_exchange_rpc_pb2 as spot_exchange_rpc_pb
import pyinjective.proto.exchange.injective_spot_exchange_rpc_pb2_grpc as spot_exchange_rpc_grpc
import pyinjective.proto.exchange.injective_derivative_exchange_rpc_pb2 as derivative_exchange_rpc_pb
import pyinjective.proto.exchange.injective_derivative_exchange_rpc_pb2_grpc as derivative_exchange_rpc_grpc

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
This makes sense since since it's defining th3e minimum price increment of the relative exchange of INJ to USDT.

Note that this market also happens to have a MinQuantityTickSize of 1e15.
This also makes sense since it refers to the minimum INJ quantity tick size each order must have, which is 1e15/1e18 = 0.001 INJ.

"""

def spot_price_to_backend(price, denom, precision=18) -> str:
    scale_tick_size = int(denom.base - denom.quote)
    price_tick_size = denom.min_price_tick_size
    scale_price = Decimal(18 + denom.quote - denom.base)
    exchange_price = floor_to(price, price_tick_size) *pow(10, scale_price)
    return str(int(exchange_price))

def spot_quantity_to_backend(quantity, denom, precision=18) -> str:
    scale_tick_size = float(0 - denom.base)
    quantity_tick_size = float(denom.min_quantity_tick_size) *pow(10, scale_tick_size)
    scale_quantity = Decimal(18 + denom.base)
    exchange_quantity = floor_to(quantity, quantity_tick_size) *pow(10, scale_quantity)
    return str(int(exchange_quantity))

def derivative_price_to_backend(price, denom, precision=18) -> str:
    scale = int(0 - denom.quote)
    price_tick_size = float(denom.min_price_tick_size) * pow(10, scale)
    exchange_price = floor_to(price, price_tick_size) * pow(10, 18 + denom.quote)
    return str(int(exchange_price))

def derivative_quantity_to_backend(quantity, denom, precision=18) -> str:
    scale_tick_size = float(0 - denom.base)
    quantity_tick_size = float(denom.min_quantity_tick_size) *pow(10, scale_tick_size)
    scale_quantity = Decimal(denom.base)
    exchange_quantity = floor_to(quantity, quantity_tick_size) *pow(10, scale_quantity)
    return str(int(exchange_quantity))

def derivative_margin_to_backend(price, quantity, leverage, denom, precision=18) -> str:
    scale = int(0 - denom.quote)
    price_tick_size = float(denom.min_price_tick_size) * pow(10, scale)
    margin = (price * quantity) / leverage
    exchange_margin = floor_to(margin, price_tick_size) * pow(10, 18 + denom.quote)
    return str(int(exchange_margin))

def floor_to(value: float, target: float) -> str:
    value = Decimal(str(value))
    target = Decimal(str(target))
    result = Decimal(int(floor(value / target)) * target)
    return result
#
# async def derivative_price_to_backend(endpoint, market, price, quote_decimals, precision=18) -> str:
#
#     """
#     Args:
#         endpoint ([string]): the endpoint for the gRPC request
#         market ([string]): the market_id of the pair
#         price ([float]): normal price, you can read it directly in exchange front-end
#         quote_decimals ([int]): decimals of quote asset
#         precision (int, optional): [description]. Defaults to 18.
#
#     Returns:
#         str: relative price for the quote asset. For INJ/USDT of 6.9, the price you end up getting is 6.9*10 ^ (6) = 6.9e6.
#     """
#
#     async with grpc.aio.insecure_channel(endpoint) as channel:
#         derivative_exchange_rpc = derivative_exchange_rpc_grpc.InjectiveDerivativeExchangeRPCStub(channel)
#         mresp = await derivative_exchange_rpc.Market(derivative_exchange_rpc_pb.MarketRequest(market_id=market))
#
#
#     scale = int(0 - quote_decimals)
#     price_tick_size = float(mresp.market.min_price_tick_size) * pow(10, scale)
#     exchange_price = floor_to(price, price_tick_size) * pow(10, quote_decimals)
#     price_string = ("{:."+str(precision)+"f}").format(exchange_price)
#     print("price string :{}".format(price_string))
#     return price_string
#
# async def derivative_margin_to_backend(endpoint, market, price, quantity, leverage, quote_decimals, precision=18) -> str:
#
#     """
#     Args:
#         endpoint ([string]): the endpoint for the gRPC request
#         market ([string]): the market_id of the pair
#         price ([float]): normal price, you can read it directly in exchange front-end
#         quantity ([float]): normal quantity, you can read it directly in exchange front-end
#         leverage ([float]): normal leverage, you can read it directly in exchange front-end
#         quote_decimals ([int]): decimals of quote asset
#         precision (int, optional): [description]. Defaults to 18.
#
#     Returns:
#         str: relative price for the quote asset. For INJ/USDT of 6.9, the price you end up getting is 6.9*10 ^ (6) = 6.9e6.
#     """
#
#     async with grpc.aio.insecure_channel(endpoint) as channel:
#         derivative_exchange_rpc = derivative_exchange_rpc_grpc.InjectiveDerivativeExchangeRPCStub(channel)
#         mresp = await derivative_exchange_rpc.Market(derivative_exchange_rpc_pb.MarketRequest(market_id=market))
#
#     scale = int(0 - quote_decimals)
#     price_tick_size = float(mresp.market.min_price_tick_size) * pow(10, scale)
#     margin = (price * quantity) / leverage
#     exchange_margin = floor_to(margin, price_tick_size) * pow(10, quote_decimals)
#     price_string = ("{:."+str(precision)+"f}").format(exchange_margin)
#     print("margin string :{}".format(price_string))
#     return price_string
#
#
# async def derivative_quantity_to_backend(endpoint, market, quantity, quote_decimals, precision=18) -> str:
#
#     """
#     Args:
#         endpoint ([string]): the endpoint for the gRPC request
#         market ([string]): the market_id of the pair
#         quantity ([float]):  normal quantity, you can read it in exchange front-end
#         quote_decimals ([int]): decimals of quote asset
#         precision (int, optional): [description]. Defaults to 18.
#
#     Returns:
#         str:  actual quantity of quote asset[data type: string] For 1 USDT, the quantity you end up is 1.000000000000000000 USDT
#     """
#
#     async with grpc.aio.insecure_channel(endpoint) as channel:
#         derivative_exchange_rpc = derivative_exchange_rpc_grpc.InjectiveDerivativeExchangeRPCStub(channel)
#         mresp = await derivative_exchange_rpc.Market(derivative_exchange_rpc_pb.MarketRequest(market_id=market))
#
#     quantity_tick_size = float(mresp.market.min_quantity_tick_size)
#     exchange_quantity = floor_to(quantity, quantity_tick_size)
#     quantity_string = ("{:."+str(precision)+"f}").format(exchange_quantity)
#     print("quantity string :{}".format(quantity_string))
#     return quantity_string

# def spot_price_from_backend(price_string, base_decimals, quote_decimals) -> float:
#
#     """
#     Args:
#         price_string ([string]): price with string data type that injective-exchange backend returns
#         base_decimals ([int]): decimal of base asset
#         quote_decimals ([int]): decimal of quote asset
#
#     Returns:
#         float: actual price what you can read directly from front-end.
#         For 6.9e-12 inj/peggy0xdac17f958d2ee523a2206206994597c13d831ec7**, the price you end up getting is 6.9 INJ/USDT.
#     """
#
#     scale = float(base_decimals - quote_decimals)
#     return float(price_string) * pow(10, scale)
#
# async def spot_quantity_from_backend(endpoint, market, quantity_string, base_decimals) -> float:
#
#     """
#     Args:
#         quantity_string ([type]): quantity string that injective-exchange backend returns
#         base_decimals ([type]): decimal of base asset
#         endpoint ([string]): the endpoint for the gRPC request
#         market ([string]): the market_id of the pair
#
#     Returns:
#         float: actual quantity, for 1e18 inj, you will get 1 INJ
#     """
#     async with grpc.aio.insecure_channel(endpoint) as channel:
#         spot_exchange_rpc = spot_exchange_rpc_grpc.InjectiveSpotExchangeRPCStub(channel)
#         mresp = await spot_exchange_rpc.Market(spot_exchange_rpc_pb.MarketRequest(market_id=market))
#
#     scale = float(0 - base_decimals)
#     quantity_tick_size = float(mresp.market.min_quantity_tick_size) *pow(10, scale)
#     quantity = float(quantity_string) * pow(10, scale)
#     return floor_to(quantity, quantity_tick_size)
#
#
# def derivative_price_from_backend(price_string, quote_decimals=6) -> float:
#
#     """
#     Args:
#         price_string ([string]): price with string data type that injective-exchange backend returns
#         quote_decimals ([int]): decimals of quote asset. Defaults to 6
#
#     Returns:
#         float: actual price which you can read directly from the front-end.
#         For 6.9e6 inj/peggy0xdac17f958d2ee523a2206206994597c13d831ec7**, the price you end up getting is 6.9 INJ/USDT.
#     """
#
#     scale = float(0 - quote_decimals)
#     return float(price_string) * pow(10, scale)
#
