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

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    market_ids = [
        "0x74b17b0d6855feba39f1f7ab1e8bad0363bd510ee1dcc74e40c2adfe1502f781",
        "0x26413a70c9b78a495023e5ab8003c9cf963ef963f6755f8b57255feb5744bf31"
    ]

    markets = await client.get_spot_orderbooks(market_ids=market_ids)
    print(markets)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
