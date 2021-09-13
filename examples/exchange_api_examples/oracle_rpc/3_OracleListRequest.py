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

import pyinjective.proto.exchange.injective_oracle_rpc_pb2 as oracle_rpc_pb
import pyinjective.proto.exchange.injective_oracle_rpc_pb2_grpc as oracle_rpc_grpc

from pyinjective.constant import Network

network = Network.testnet()

async def main() -> None:
    async with grpc.aio.insecure_channel(network.grpc_exchange_endpoint) as channel:
        oracle_exchange_rpc = oracle_rpc_grpc.InjectiveOracleRPCStub(channel)

        base_s = "BTC"
        quote_s = "USD"
        oracle_t = "coinbase"
        oracle_scale_f = 6

        oracle_list = await oracle_exchange_rpc.OracleList(oracle_rpc_pb.OracleListRequest())
        print("\n-- Oracle List Update:\n", oracle_list)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
