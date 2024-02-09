import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    delegator_address = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
    withdraw_address = await client.fetch_delegator_withdraw_address(
        delegator_address=delegator_address,
    )
    print(withdraw_address)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
