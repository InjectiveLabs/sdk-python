import asyncio
from typing import Any, Dict

from grpc import RpcError

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def market_event_processor(event: Dict[str, Any]):
    print(event)


def stream_error_processor(exception: RpcError):
    print(f"There was an error listening to derivative trades updates ({exception})")


def stream_closed_processor():
    print("The derivative trades updates stream has been closed")


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = IndexerClient(network)
    market_ids = [
        "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
        "0x70bc8d7feab38b23d5fdfb12b9c3726e400c265edbcbf449b6c80c31d63d3a02",
    ]
    subaccount_ids = ["0xc6fe5d33615a1c52c08018c47e8bc53646a0e101000000000000000000000000"]

    task = asyncio.get_event_loop().create_task(
        client.listen_derivative_trades_updates(
            callback=market_event_processor,
            on_end_callback=stream_closed_processor,
            on_status_callback=stream_error_processor,
            market_ids=market_ids,
            subaccount_ids=subaccount_ids,
        )
    )

    await asyncio.sleep(delay=60)
    task.cancel()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
