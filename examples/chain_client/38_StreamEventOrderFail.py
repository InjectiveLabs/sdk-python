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
import json
import websockets
import base64

from pyinjective.constant import Network

async def main() -> None:
    network = Network.mainnet()
    event_filter = "tm.event='Tx' AND message.sender='inj1rwv4zn3jptsqs7l8lpa3uvzhs57y8duemete9e' AND message.action='/injective.exchange.v1beta1.MsgBatchUpdateOrders' AND injective.exchange.v1beta1.EventOrderFail.flags EXISTS"
    query = json.dumps({
        "jsonrpc": "2.0",
        "method": "subscribe",
        "id": "0",
        "params": {
            "query": event_filter
        },
    })

    events_dict = {}
    failed_orders = {}
    flags = []
    order_hashes = []

    async with websockets.connect(network.tm_websocket_endpoint) as ws:
        await ws.send(query)
        while True:
            events = await ws.recv()
            events_json = json.loads(events)
            resp = events_json["result"]
            for key, value in resp.items():
                if key == "events":
                    events_dict = value
            for key, value in events_dict.items():
                if key == "injective.exchange.v1beta1.EventOrderFail.flags":
                    k = json.loads(value[0])
                    for i in range(len(k)):
                        flags.append(k[i])
                if key == "injective.exchange.v1beta1.EventOrderFail.hashes":
                    k = json.loads(value[0])
                    for i in range(len(k)):
                        hash_to_bytes = k[i].encode("utf-8")
                        bytes_to_base64 = base64.standard_b64decode(hash_to_bytes)
                        base64_to_hex = '0x' + bytes_to_base64.hex()
                        order_hashes.append(base64_to_hex)
            for i in range(len(order_hashes)):
                failed_orders[order_hashes[i]] = flags[i]
            print(failed_orders)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
