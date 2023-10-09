import asyncio

from google.protobuf import json_format

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)
    market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
    skip = 10
    limit = 3
    positions = await client.get_derivative_liquidable_positions(
        market_id=market_id,
        skip=skip,
        limit=limit,
    )
    print(
        json_format.MessageToJson(
            message=positions,
            including_default_value_fields=True,
            preserving_proto_field_name=True,
        )
    )


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
