import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    address = "inj1cml96vmptgw99syqrrz8az79xer2pcgp0a885r"
    spendable_balances = await client.fetch_spendable_balances(address=address)
    print(spendable_balances)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
