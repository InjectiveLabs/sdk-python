import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    address = "inj1cml96vmptgw99syqrrz8az79xer2pcgp0a885r"
    denom = "inj"
    bank_balance = await client.get_bank_balance(address=address, denom=denom)
    print(bank_balance)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
