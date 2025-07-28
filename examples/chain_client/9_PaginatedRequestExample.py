import asyncio

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    pagination = PaginationOption(
        limit=10,
        count_total=True,
    )
    first_result = await client.fetch_total_supply(
        pagination=pagination,
    )
    print(f"First result:\n{first_result}")

    next_page_key = first_result["pagination"]["nextKey"]

    for i in range(5):
        if next_page_key == "":
            break

        next_request_pagination = PaginationOption(
            limit=pagination.limit,
            count_total=pagination.count_total,
            encoded_page_key=next_page_key,
        )

        next_result = await client.fetch_total_supply(
            pagination=next_request_pagination,
        )
        print(f"Page {i+2} result:\n{next_result}")

        next_page_key = next_result["pagination"]["nextKey"]


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
