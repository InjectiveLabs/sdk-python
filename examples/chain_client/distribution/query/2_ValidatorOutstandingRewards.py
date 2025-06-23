import asyncio
import json

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    validator_address = "injvaloper1jue5dpr9lerjn6wlwtrywxrsenrf28ru89z99z"
    rewards = await client.fetch_validator_outstanding_rewards(validator_address=validator_address)
    print(json.dumps(rewards, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
