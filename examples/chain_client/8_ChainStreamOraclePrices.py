import asyncio
from contextlib import suppress
from typing import Any, Dict

from grpc import RpcError

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network

ORACLE_TYPE = "chainlinkdatastreams"
ORACLE_SYMBOLS = {
    "INJ": "0x000344d7a7d81f051ee273a63f94f8bef7d44ca89aa03e0c5bf4d085df19adb6",
    "USDC": "0x00038f83323b6b08116d1614cf33a9bd71ab5e0abf0c9f1b783a74a43e7bd992",
}


async def oracle_price_event_processor(event: Dict[str, Any]):
    for oracle_price in event.get("oraclePrices", []):
        print(
            {
                "blockHeight": event["blockHeight"],
                "blockTime": event["blockTime"],
                **oracle_price,
            }
        )


def stream_error_processor(exception: RpcError):
    print(f"There was an error listening to oracle price updates ({exception})")


def stream_closed_processor():
    print("The oracle price updates stream has been closed")


async def main() -> None:
    network = Network.mainnet()

    client = AsyncClient(network)
    composer = await client.composer()

    print(f"Streaming {ORACLE_TYPE} prices for {', '.join(ORACLE_SYMBOLS)}")
    # To receive all oracle price updates, use composer.chain_stream_oracle_price_filter() without symbols.
    oracle_price_filter = composer.chain_stream_oracle_price_filter(symbols=list(ORACLE_SYMBOLS.values()))

    task = asyncio.get_event_loop().create_task(
        client.listen_chain_stream_updates(
            callback=oracle_price_event_processor,
            on_end_callback=stream_closed_processor,
            on_status_callback=stream_error_processor,
            oracle_price_filter=oracle_price_filter,
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
    asyncio.get_event_loop().run_until_complete(main())
