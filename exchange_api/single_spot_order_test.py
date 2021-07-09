# Copyright 2021 Injective Labs
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Injective Exchange API client for Python. Example only."""

import asyncio
import logging
import grpc


import injective_accounts_rpc_pb2 as accounts_rpc_pb
import injective_accounts_rpc_pb2_grpc as accounts_rpc_grpc
import injective_derivative_exchange_rpc_pb2 as derivative_exchange_rpc_pb
import injective_derivative_exchange_rpc_pb2_grpc as derivative_exchange_rpc_grpc
import injective_exchange_rpc_pb2 as exchange_rpc_pb
import injective_exchange_rpc_pb2_grpc as exchange_rpc_grpc
import injective_insurance_rpc_pb2 as insurance_rpc_pb
import injective_insurance_rpc_pb2_grpc as insurance_rpc_grpc
import injective_oracle_rpc_pb2 as oracle_rpc_pb
import injective_oracle_rpc_pb2_grpc as oracle_rpc_grpc
import injective_spot_exchange_rpc_pb2 as spot_exchange_rpc_pb
import injective_spot_exchange_rpc_pb2_grpc as spot_exchange_rpc_grpc


async def main() -> None:
    async with grpc.aio.insecure_channel('localhost:9910') as channel:
        exchange_rpc = exchange_rpc_grpc.InjectiveExchangeRPCStub(channel)
        spot_exchange_rpc = spot_exchange_rpc_grpc.InjectiveSpotExchangeRPCStub(channel)
        

        resp = await exchange_rpc.Version(exchange_rpc_pb.VersionRequest())
        print("-- Connected to Injective Exchange (version: %s, built %s)" % (resp.version, resp.meta_data["BuildDate"]))

        resp = await spot_exchange_rpc.Markets(spot_exchange_rpc_pb.MarketsRequest())
        print("\n-- Available markets:")
        for m in resp.markets:
            print(m.ticker, "=", m.market_id)

        selected_market = resp.markets[0]

        # 4.1 get market response 
        # market_response = spot_exchange_rpc_pb.Market(spot_exchange_rpc_pb.MarketRequest(selected_market.market_id))
        # print(f"\n-- Market response:{market_response}")

        # 4.2 listen to market order update 
        '''
        print("\n-- Watching for order updates on market %s" % selected_market.ticker)
        #stream_req = spot_exchange_rpc_pb.StreamOrdersRequest(market_id=selected_market.market_id)
        mkt_id = "0x17d9b5fb67666df72a5a858eb9b81104b99da760e3036a8243e05532d50e1c7c"
        acct_id = "0xbdaedec95d563fb05240d6e01821008454c24c36000000000000000000000000"
        stream_req = spot_exchange_rpc_pb.StreamOrdersRequest(market_id=mkt_id, subaccount_id=acct_id, order_type='buy')
        orders_stream = spot_exchange_rpc.StreamOrders(stream_req)
        async for order in orders_stream:
            print("\n-- Order Update:", order)
        '''

        # 4.3 listen to market trade updates
        
        print("\n-- Watching for trades updates on market %s" % selected_market.ticker)
        stream_req = spot_exchange_rpc_pb.StreamTradesRequest(market_id=selected_market.market_id, direction='buy')
        trades_stream = spot_exchange_rpc.StreamTrades(stream_req)
        async for trade in trades_stream:
            print("\n-- Trader Update:", trade)
        

        # 4.4 test subaccountOrdersList
        '''
        mkt_id = "0x17d9b5fb67666df72a5a858eb9b81104b99da760e3036a8243e05532d50e1c7c"
        acct_id = "0xbdaedec95d563fb05240d6e01821008454c24c36000000000000000000000000"
        subaccountOrdersList_req = spot_exchange_rpc_pb.SubaccountOrdersListRequest(market_id=mkt_id, subaccount_id=acct_id)
        subaccountOrders = spot_exchange_rpc.SubaccountOrdersList(subaccountOrdersList_req)
        for order in subaccountOrders: 
            print(order)
        '''

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())









