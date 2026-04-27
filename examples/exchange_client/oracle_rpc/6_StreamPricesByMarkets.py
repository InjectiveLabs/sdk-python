import asyncio
from typing import Any, Dict

from grpc import RpcError

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def price_event_processor(event: Dict[str, Any]):
    print(event)


def stream_error_processor(exception: RpcError):
    print(f"There was an error listening to oracle prices by markets updates ({exception})")


def stream_closed_processor():
    print("The oracle prices by markets updates stream has been closed")


async def main() -> None:
    network = Network.testnet()
    client = IndexerClient(network)
    market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"

    task = asyncio.get_event_loop().create_task(
        client.listen_oracle_prices_by_markets_updates(
            market_ids=[market_id],
            callback=price_event_processor,
            on_end_callback=stream_closed_processor,
            on_status_callback=stream_error_processor,
        )
    )

    await asyncio.sleep(delay=60)
    task.cancel()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
