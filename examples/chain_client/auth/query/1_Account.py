import asyncio
import json

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    address = "inj1knhahceyp57j5x7xh69p7utegnnnfgxavmahjr"
    acc = await client.fetch_account(address=address)
    print(json.dumps(acc, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
