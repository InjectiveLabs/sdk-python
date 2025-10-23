import asyncio
from typing import Any, Dict

from grpc import RpcError

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def chain_stream_event_processor(event: Dict[str, Any]):
    print(event)


def stream_error_processor(exception: RpcError):
    print(f"There was an error listening to chain stream updates ({exception})")


def stream_closed_processor():
    print("The chain stream updates stream has been closed")


async def main() -> None:
    network = Network.testnet()

    client = AsyncClient(network)
    composer = await client.composer()

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
    order_failures_filter = composer.chain_stream_order_failures_filter(
        accounts=["inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"]
    )
    conditional_order_trigger_failures_filter = composer.chain_stream_conditional_order_trigger_failures_filter(
        subaccount_ids=[subaccount_id], market_ids=[inj_usdt_perp_market]
    )

    task = asyncio.get_event_loop().create_task(
        client.listen_chain_stream_updates(
            callback=chain_stream_event_processor,
            on_end_callback=stream_closed_processor,
            on_status_callback=stream_error_processor,
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
            order_failures_filter=order_failures_filter,
            conditional_order_trigger_failures_filter=conditional_order_trigger_failures_filter,
        )
    )

    await asyncio.sleep(delay=60)
    task.cancel()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
