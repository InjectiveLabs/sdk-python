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
import json
import websockets

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    network = Network.mainnet()
    client = AsyncClient(network, insecure=False)

    event_filter = "tm.event='Tx' AND message.sender='inj1rwv4zn3jptsqs7l8lpa3uvzhs57y8duemete9e' AND message.action='/injective.exchange.v1beta1.MsgBatchUpdateOrders'"
    query = json.dumps({
        "jsonrpc": "2.0",
        "method": "subscribe",
        "id": "0",
        "params": {
            "query": event_filter
        },
    })

    async with websockets.connect(network.tm_websocket_endpoint) as ws:
        await ws.send(query)
        while True:
            events = await ws.recv()
            print(events)
            await asyncio.sleep(1)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
