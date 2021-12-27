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
    tx_hash = "0x298c3a789bb53b5978f8140fcfe9ec8a4447211b95618d8b108fcf521625fb1a"
    account = client.get_tx_by_hash(tx_hash=tx_hash)
    print(account)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
