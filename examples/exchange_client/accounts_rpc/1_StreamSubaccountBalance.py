import asyncio
from typing import Any, Dict

from grpc import RpcError

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def balance_event_processor(event: Dict[str, Any]):
    print(event)


def stream_error_processor(exception: RpcError):
    print(f"There was an error listening to balance updates ({exception})")


def stream_closed_processor():
    print("The balance updates stream has been closed")


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    subaccount_id = "0xc7dca7c15c364865f77a4fb67ab11dc95502e6fe000000000000000000000001"
    denoms = ["inj", "peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5"]
    task = asyncio.get_event_loop().create_task(
        client.listen_subaccount_balance_updates(
            subaccount_id=subaccount_id,
            callback=balance_event_processor,
            on_end_callback=stream_closed_processor,
            on_status_callback=stream_error_processor,
            denoms=denoms,
        )
    )

    await asyncio.sleep(delay=60)
    task.cancel()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
