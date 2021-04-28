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

import injective_exchange_rpc_pb2
import injective_exchange_rpc_pb2_grpc
import injective_spot_exchange_rpc_pb2
import injective_spot_exchange_rpc_pb2_grpc
import injective_derivative_exchange_rpc_pb2
import injective_derivative_exchange_rpc_pb2_grpc

async def main() -> None:
    async with grpc.aio.insecure_channel('localhost:9910') as channel:
        exchange_rpc = injective_exchange_rpc_pb2_grpc.InjectiveExchangeRPCStub(channel)
        spot_exchange_rpc = injective_spot_exchange_rpc_pb2_grpc.InjectiveSpotExchangeRPCStub(channel)

        resp = await exchange_rpc.Version(injective_exchange_rpc_pb2.VersionRequest())
        print("-- Connected to Injective Exchange (version: %s, built %s)" % (resp.version, resp.meta_data["BuildDate"]))

        resp = await spot_exchange_rpc.Markets(injective_spot_exchange_rpc_pb2.MarketsRequest())
        print("\n-- Available markets:")
        for m in resp.markets:
            print(m.ticker, "=", m.market_id)

        selected_market = resp.markets[0]
        print("\n-- Watching for order updates on market %s" % selected_market.ticker)
        stream_req = injective_spot_exchange_rpc_pb2.StreamOrdersRequest(market_id=selected_market.market_id)
        orders_stream = spot_exchange_rpc.StreamOrders(stream_req)
        async for order in orders_stream:
            print("\n-- Order Update:", order)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())