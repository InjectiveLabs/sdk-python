import asyncio
import json

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    address = "inj1cml96vmptgw99syqrrz8az79xer2pcgp0a885r"
    all_bank_balances = await client.fetch_bank_balances(address=address)
    print(json.dumps(all_bank_balances, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
