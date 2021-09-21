import asyncio
import logging
import grpc

import pyinjective.proto.exchange.injective_spot_exchange_rpc_pb2 as spot_exchange_rpc_pb
import pyinjective.proto.exchange.injective_spot_exchange_rpc_pb2_grpc as spot_exchange_rpc_grpc
import pyinjective.proto.exchange.injective_derivative_exchange_rpc_pb2 as derivative_exchange_rpc_pb
import pyinjective.proto.exchange.injective_derivative_exchange_rpc_pb2_grpc as derivative_exchange_rpc_grpc

from pyinjective.constant import Network

metadata_template = """[{}]
description = '{} {} {}'
base = {}
quote = {}
min_price_tick_size = {}
min_quantity_tick_size = {}

"""

testnet_denom_output = ''
mainnet_denom_output = ''

async def fetch_denom(network) -> str:
    denom_output = ''

    # fetch meta data for spot markets
    async with grpc.aio.insecure_channel(network.grpc_exchange_endpoint) as channel:
        spot_exchange_rpc = spot_exchange_rpc_grpc.InjectiveSpotExchangeRPCStub(channel)
        status = "active"
        mresp = await spot_exchange_rpc.Markets(spot_exchange_rpc_pb.MarketsRequest(market_status=status))
        for market in mresp.markets:
            config = metadata_template.format(
                market.market_id,
                network.string().capitalize(), 'Spot', market.ticker,
                market.base_token_meta.decimals,
                market.quote_token_meta.decimals,
                market.min_price_tick_size,
                market.min_quantity_tick_size
            )
            denom_output += config

    # fetch meta data for derivative markets
    async with grpc.aio.insecure_channel(network.grpc_exchange_endpoint) as channel:
        derivative_exchange_rpc = derivative_exchange_rpc_grpc.InjectiveDerivativeExchangeRPCStub(channel)
        status = "active"
        mresp = await derivative_exchange_rpc.Markets(derivative_exchange_rpc_pb.MarketsRequest(market_status=status))
        for market in mresp.markets:
            config = metadata_template.format(
                market.market_id,
                network.string().capitalize(), 'Derivative', market.ticker,
                18,
                market.quote_token_meta.decimals,
                market.min_price_tick_size,
                market.min_quantity_tick_size
            )
            denom_output += config

    return denom_output

async def main() -> None:
    testnet = Network.testnet()
    data = await fetch_denom(testnet)
    with open("./pyinjective/testnet_denoms.ini", "w") as text_file:
        text_file.write(data)

    mainnet = Network.mainnet()
    data = await fetch_denom(mainnet)
    with open("./pyinjective/mainnet_denoms.ini", "w") as text_file:
        text_file.write(data)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
