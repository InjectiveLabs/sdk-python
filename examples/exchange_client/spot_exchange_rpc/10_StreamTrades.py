import asyncio
from typing import Any, Dict

from grpc import RpcError

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def trade_event_processor(event: Dict[str, Any]):
    print(event)


def stream_error_processor(exception: RpcError):
    print(f"There was an error listening to spot trades updates ({exception})")


def stream_closed_processor():
    print("The spot trades updates stream has been closed")


async def main() -> None:
    network = Network.testnet()
    client = IndexerClient(network)
    market_ids = [
        "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
        "0x7a57e705bb4e09c88aecfc295569481dbf2fe1d5efe364651fbe72385938e9b0",
    ]
    execution_side = "maker"
    direction = "sell"
    subaccount_id = "0xc7dca7c15c364865f77a4fb67ab11dc95502e6fe000000000000000000000001"
    execution_types = ["limitMatchRestingOrder"]

    task = asyncio.get_event_loop().create_task(
        client.listen_spot_trades_updates(
            callback=trade_event_processor,
            on_end_callback=stream_closed_processor,
            on_status_callback=stream_error_processor,
            market_ids=market_ids,
            subaccount_ids=[subaccount_id],
            execution_side=execution_side,
            direction=direction,
            execution_types=execution_types,
        )
    )

    await asyncio.sleep(delay=60)
    task.cancel()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
