import asyncio
import json

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()

    # initialize grpc client
    client = AsyncClient(network)

    market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
    trade_grouping_sec = 10
    max_age = 0
    include_raw_history = True
    include_metadata = True
    volatility = await client.fetch_market_volatility(
        market_id=market_id,
        trade_grouping_sec=trade_grouping_sec,
        max_age=max_age,
        include_raw_history=include_raw_history,
        include_metadata=include_metadata,
    )
    print(json.dumps(volatility, indent=4))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
