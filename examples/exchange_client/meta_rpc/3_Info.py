import asyncio
import json
import time

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = IndexerClient(network)
    resp = await client.fetch_info()
    print("[!] Info:")
    print(json.dumps(resp, indent=2))
    latency = int(time.time() * 1000) - int(resp["timestamp"])
    print(f"Server Latency: {latency}ms")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
