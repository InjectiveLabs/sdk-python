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

import pyinjective.proto.exchange.injective_accounts_rpc_pb2 as accounts_rpc_pb
import pyinjective.proto.exchange.injective_accounts_rpc_pb2_grpc as accounts_rpc_grpc

from pyinjective.constant import Network

network = Network.testnet()

async def main() -> None:
    async with grpc.aio.insecure_channel(network.grpc_exchange_endpoint) as channel:
        accounts_exchange_rpc = accounts_rpc_grpc.InjectiveAccountsRPCStub(channel)

        addr = "inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku"

        subacc_list = await accounts_exchange_rpc.SubaccountsList(accounts_rpc_pb.SubaccountsListRequest(account_address=addr))
        print("\n-- Subaccount List Update:\n", subacc_list)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
