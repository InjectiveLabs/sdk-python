import asyncio
import json
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network


async def main() -> None:
    # network: Network = Network.testnet()
    network: Network = Network.testnet()
    client: AsyncClient = AsyncClient(network)

    pagination = PaginationOption(limit=5)
    senders = ["inj17xpfvakm2amg962yls6f84z3kell8c5l6s5ye9"]

    bank_transfers = await client.fetch_bank_transfers(senders=senders, pagination=pagination)
    print("Bank transfers:")
    print(json.dumps(bank_transfers, indent=2))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
