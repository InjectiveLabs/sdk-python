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

import injective.exchange_api.injective_accounts_rpc_pb2 as accounts_rpc_pb
import injective.exchange_api.injective_accounts_rpc_pb2_grpc as accounts_rpc_grpc

async def main() -> None:
    async with grpc.aio.insecure_channel('testnet-sentry0.injective.network:9910') as channel:
        accounts_exchange_rpc = accounts_rpc_grpc.InjectiveAccountsRPCStub(channel)

        subacc_id = "0xaf79152ac5df276d9a8e1e2e22822f9713474902000000000000000000000000"
        dnm="peggy0x69efCB62D98f4a6ff5a0b0CFaa4AAbB122e85e08"
        
        stream_req = accounts_rpc_pb.StreamSubaccountBalanceRequest(subaccount_id=subacc_id)
        stream_resp = accounts_exchange_rpc.StreamSubaccountBalance(stream_req)
        async for subacc in stream_resp:
            print("\n-- Subaccount Balance Update:\n", subacc)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())








