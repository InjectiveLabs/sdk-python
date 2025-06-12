import asyncio
from typing import Any, Dict

from grpc import RpcError

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def orderbook_event_processor(event: Dict[str, Any]):
    print(event)


def stream_error_processor(exception: RpcError):
    print(f"There was an error listening to spot orderbook snapshots ({exception})")


def stream_closed_processor():
    print("The spot orderbook snapshots stream has been closed")


async def main() -> None:
    network = Network.testnet()
    client = IndexerClient(network)
    market_ids = [
        "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
        "0x7a57e705bb4e09c88aecfc295569481dbf2fe1d5efe364651fbe72385938e9b0",
    ]

    task = asyncio.get_event_loop().create_task(
        client.listen_spot_orderbook_snapshots(
            market_ids=market_ids,
            callback=orderbook_event_processor,
            on_end_callback=stream_closed_processor,
            on_status_callback=stream_error_processor,
        )
    )

    await asyncio.sleep(delay=60)
    task.cancel()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
