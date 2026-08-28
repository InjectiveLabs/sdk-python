import asyncio
from typing import Any, Dict

from grpc import RpcError

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def chain_stream_event_processor(event: Dict[str, Any]):
    for funding_update in event["marketFundingUpdates"]:
        print(funding_update)


def stream_error_processor(exception: RpcError):
    print(f"There was an error listening to chain stream updates ({exception})")


def stream_closed_processor():
    print("The chain stream updates stream has been closed")


async def main() -> None:
    network = Network.mainnet()

    client = AsyncClient(network)
    composer = await client.composer()

    btc_usdc_perp_market = "0x0ee7ca44147bab6ec81ac293b5fe7915488e612af59964b2d663d6008d861dee"
    inj_usdc_perp_market = "0x790aee464fbbd02cf4476444554c71d1225f7edfe15e6dc7f874c455fd883d31"

    market_funding_filter = composer.chain_stream_market_funding_filter(
        market_ids=[btc_usdc_perp_market, inj_usdc_perp_market]
    )

    task = asyncio.get_event_loop().create_task(
        client.listen_chain_stream_updates(
            callback=chain_stream_event_processor,
            on_end_callback=stream_closed_processor,
            on_status_callback=stream_error_processor,
            market_funding_filter=market_funding_filter,
        )
    )

    await asyncio.sleep(delay=60)
    task.cancel()


if __name__ == "__main__":
    asyncio.run(main())
