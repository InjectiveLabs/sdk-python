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

import injective.exchange_api.injective_oracle_rpc_pb2 as oracle_rpc_pb
import injective.exchange_api.injective_oracle_rpc_pb2_grpc as oracle_rpc_grpc

async def main() -> None:
    async with grpc.aio.insecure_channel('testnet-sentry0.injective.network:9910') as channel:
        oracle_exchange_rpc = oracle_rpc_grpc.InjectiveOracleRPCStub(channel)

        base_s = "BTC"
        quote_s = "USD"
        oracle_t = "coinbase"
        
        stream_req = oracle_rpc_pb.StreamPricesRequest(base_symbol = base_s, quote_symbol = quote_s, oracle_type = oracle_t)
        stream_resp = oracle_exchange_rpc.StreamPrices(stream_req)
        async for oracle in stream_resp:
            print("\n-- Oracle Prices Update:\n", oracle)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())








