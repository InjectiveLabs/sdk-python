import asyncio

from google.protobuf import json_format

from pyinjective.async_client import AsyncClient
from pyinjective.composer import Composer
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.devnet()

    client = AsyncClient(network)
    composer = Composer(network=network.string())

    subaccount_id = "0xbdaedec95d563fb05240d6e01821008454c24c36000000000000000000000000"

    inj_usdt_market = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
    inj_usdt_perp_market = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"

    bank_balances_filter = composer.chain_stream_bank_balances_filter(
        accounts=["inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"]
    )
    subaccount_deposits_filter = composer.chain_stream_subaccount_deposits_filter(subaccount_ids=[subaccount_id])
    spot_trades_filter = composer.chain_stream_trades_filter(subaccount_ids=["*"], market_ids=[inj_usdt_market])
    derivative_trades_filter = composer.chain_stream_trades_filter(
        subaccount_ids=["*"], market_ids=[inj_usdt_perp_market]
    )
    spot_orders_filter = composer.chain_stream_orders_filter(
        subaccount_ids=[subaccount_id], market_ids=[inj_usdt_market]
    )
    derivative_orders_filter = composer.chain_stream_orders_filter(
        subaccount_ids=[subaccount_id], market_ids=[inj_usdt_perp_market]
    )
    spot_orderbooks_filter = composer.chain_stream_orderbooks_filter(market_ids=[inj_usdt_market])
    derivative_orderbooks_filter = composer.chain_stream_orderbooks_filter(market_ids=[inj_usdt_perp_market])
    positions_filter = composer.chain_stream_positions_filter(
        subaccount_ids=[subaccount_id], market_ids=[inj_usdt_perp_market]
    )
    oracle_price_filter = composer.chain_stream_oracle_price_filter(symbols=["INJ", "USDT"])
    stream = await client.chain_stream(
        bank_balances_filter=bank_balances_filter,
        subaccount_deposits_filter=subaccount_deposits_filter,
        spot_trades_filter=spot_trades_filter,
        derivative_trades_filter=derivative_trades_filter,
        spot_orders_filter=spot_orders_filter,
        derivative_orders_filter=derivative_orders_filter,
        spot_orderbooks_filter=spot_orderbooks_filter,
        derivative_orderbooks_filter=derivative_orderbooks_filter,
        positions_filter=positions_filter,
        oracle_price_filter=oracle_price_filter,
    )
    async for event in stream:
        print(
            json_format.MessageToJson(
                message=event, including_default_value_fields=True, preserving_proto_field_name=True
            )
        )


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
