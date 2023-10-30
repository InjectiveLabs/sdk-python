import asyncio
from typing import Any, Dict

from grpc import RpcError

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


def stream_error_processor(exception: RpcError):
    print(f"There was an error listening to keepalive updates ({exception})")


def stream_closed_processor():
    print("The keepalive stream has been closed")


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    tasks = []

    async def keepalive_event_processor(event: Dict[str, Any]):
        print("Server announce:", event)
        for task in tasks:
            task.cancel()
        print("Cancelled all tasks")

    market_task = asyncio.get_event_loop().create_task(get_markets(client))
    tasks.append(market_task)
    keepalive_task = asyncio.get_event_loop().create_task(
        client.listen_keepalive(
            callback=keepalive_event_processor,
            on_end_callback=stream_closed_processor,
            on_status_callback=stream_error_processor,
        )
    )

    try:
        await asyncio.gather(market_task, keepalive_task)
    except asyncio.CancelledError:
        print("main(): get_markets is cancelled now")


async def get_markets(client):
    stream = await client.stream_spot_markets()
    async for market in stream:
        print(market)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
