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

from pyinjective.client import Client
from pyinjective.constant import Network


async def main() -> None:
    network = Network.testnet()
    client = Client(network, insecure=True)
    market_id = "0xd0f46edfba58827fe692aab7c8d46395d1696239fdf6aeddfa668b73ca82ea30"
    subaccount_id = "0xc6fe5d33615a1c52c08018c47e8bc53646a0e101000000000000000000000000"
    trades = client.stream_derivative_trades(
        market_id=market_id,
        subaccount_id=subaccount_id
    )
    for trade in trades:
        print(trade)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
