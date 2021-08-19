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

import injective.exchange_api.injective_spot_exchange_rpc_pb2 as spot_exchange_rpc_pb
import injective.exchange_api.injective_spot_exchange_rpc_pb2_grpc as spot_exchange_rpc_grpc

async def main() -> None:
    async with grpc.aio.insecure_channel('testnet-sentry0.injective.network:9910') as channel:
        spot_exchange_rpc = spot_exchange_rpc_grpc.InjectiveSpotExchangeRPCStub(channel)

        mkt_id = "0xa508cb32923323679f29a032c70342c147c17d0145625922b0ef22e955c844c0"
        
        stream_req = spot_exchange_rpc_pb.StreamOrderbookRequest(market_id=mkt_id)
        stream_resp = spot_exchange_rpc.StreamOrderbook(stream_req)
        async for orderbook in stream_resp:
            print("\n-- Orderbook Update:\n", orderbook)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())









