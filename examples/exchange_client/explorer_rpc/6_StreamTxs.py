import asyncio
from typing import Any, Dict

from grpc import RpcError

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def tx_event_processor(event: Dict[str, Any]):
    print(event)


def stream_error_processor(exception: RpcError):
    print(f"There was an error listening to txs updates ({exception})")


def stream_closed_processor():
    print("The txs updates stream has been closed")


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = IndexerClient(network=network)

    task = asyncio.get_event_loop().create_task(
        client.listen_txs_updates(
            callback=tx_event_processor,
            on_end_callback=stream_closed_processor,
            on_status_callback=stream_error_processor,
        )
    )

    await asyncio.sleep(delay=60)
    task.cancel()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
