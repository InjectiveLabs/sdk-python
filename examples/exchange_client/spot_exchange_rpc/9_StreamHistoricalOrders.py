import asyncio
from typing import Any, Dict

from grpc import RpcError

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def order_event_processor(event: Dict[str, Any]):
    print(event)


def stream_error_processor(exception: RpcError):
    print(f"There was an error listening to spot orders history updates ({exception})")


def stream_closed_processor():
    print("The spot orders history updates stream has been closed")


async def main() -> None:
    network = Network.testnet()
    client = IndexerClient(network)
    market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
    order_direction = "buy"

    task = asyncio.get_event_loop().create_task(
        client.listen_spot_orders_history_updates(
            callback=order_event_processor,
            on_end_callback=stream_closed_processor,
            on_status_callback=stream_error_processor,
            market_id=market_id,
            direction=order_direction,
        )
    )

    await asyncio.sleep(delay=60)
    task.cancel()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
