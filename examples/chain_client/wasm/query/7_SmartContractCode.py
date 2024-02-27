import asyncio
import base64

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    response = await client.fetch_code(code_id=290)
    print(response)

    code = base64.b64decode(response["data"]).decode(encoding="utf-8", errors="replace")

    print(f"\n\n\n{code}")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
