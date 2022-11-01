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
import sys
sys.path.insert(0, '/Users/nam/desktop/injective/sdk-python/')

import asyncio
import logging

from pyinjective.async_client import AsyncClient, OrderBookUpdate
from pyinjective.constant import Network

async def main() -> None:
    network = Network.devnet()
    client = AsyncClient(network, insecure=True)
    market_ids = [
        '0xa508cb32923323679f29a032c70342c147c17d0145625922b0ef22e955c844c0',
        '0x74b17b0d6855feba39f1f7ab1e8bad0363bd510ee1dcc74e40c2adfe1502f781',
    ]
    async for e in client.stream_event_orderbook_update(orderbook_type=OrderBookUpdate.SPOT, market_ids=market_ids):
       print(e)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
