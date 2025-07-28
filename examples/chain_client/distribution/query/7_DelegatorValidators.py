import asyncio
import json

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    delegator_address = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
    validators = await client.fetch_delegator_validators(
        delegator_address=delegator_address,
    )
    print(json.dumps(validators, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
