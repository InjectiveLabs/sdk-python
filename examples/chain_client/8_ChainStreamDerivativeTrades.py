import asyncio
from contextlib import suppress
from typing import Any, Dict

from grpc import RpcError

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network

INJ_USDC_PERP_MARKET_ID = "0x790aee464fbbd02cf4476444554c71d1225f7edfe15e6dc7f874c455fd883d31"


async def derivative_trade_event_processor(event: Dict[str, Any]):
    for trade in event.get("derivativeTrades", []):
        print(
            {
                "blockHeight": event["blockHeight"],
                "blockTime": event["blockTime"],
                **trade,
            }
        )


def stream_error_processor(exception: RpcError):
    print(f"There was an error listening to derivative trade updates ({exception})")


def stream_closed_processor():
    print("The derivative trade updates stream has been closed")


async def main() -> None:
    network = Network.mainnet()

    client = AsyncClient(network)
    composer = await client.composer()

    # To receive trades from all derivative markets, use composer.chain_stream_trades_filter() without arguments.
    derivative_trades_filter = composer.chain_stream_trades_filter(
        subaccount_ids=["*"], market_ids=[INJ_USDC_PERP_MARKET_ID]
    )

    task = asyncio.create_task(
        client.listen_chain_stream_updates(
            callback=derivative_trade_event_processor,
            on_end_callback=stream_closed_processor,
            on_status_callback=stream_error_processor,
            derivative_trades_filter=derivative_trades_filter,
        )
    )

    try:
        await asyncio.sleep(delay=60)
    finally:
        task.cancel()
        with suppress(asyncio.CancelledError):
            await task
        await client.close_chain_stream_channel()


if __name__ == "__main__":
    asyncio.run(main())
