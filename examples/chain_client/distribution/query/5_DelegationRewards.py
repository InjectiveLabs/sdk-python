import asyncio
import json

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    delegator_address = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
    validator_address = "injvaloper156t3yxd4udv0h9gwagfcmwnmm3quy0nph7tyh5"
    rewards = await client.fetch_delegation_rewards(
        delegator_address=delegator_address, validator_address=validator_address
    )
    print(json.dumps(rewards, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
