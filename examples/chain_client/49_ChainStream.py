import asyncio

from google.protobuf import json_format

from pyinjective.composer import Composer
from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    # network = Network.devnet()
    network = Network.custom(
        lcd_endpoint="https://staging.lcd.injective.network:443",
        tm_websocket_endpoint="wss://staging.tm.injective.network:443/websocket",
        grpc_endpoint="staging.chain.grpc.injective.network:443",
        grpc_exchange_endpoint="staging.exchange.grpc.injective.network:443",
        grpc_explorer_endpoint="staging.explorer.grpc.injective.network:443",
        chain_stream_endpoint="staging.stream.injective.network:443",
        chain_id="injective-1",
        env='mainnet',
        use_secure_connection=True,
    )

    client = AsyncClient(network)
    composer = Composer(network=network.string())

    inj_usdt_market = "0xfbc729e93b05b4c48916c1433c9f9c2ddb24605a73483303ea0f87a8886b52af"

    bank_balances_filter = composer.chain_stream_bank_balances_filter()
    subaccount_deposits_filter = composer.chain_stream_subaccount_deposits_filter()
    spot_trades_filter = composer.chain_stream_trades_filter()
    derivative_trades_filter = composer.chain_stream_trades_filter()
    spot_orders_filter = composer.chain_stream_orders_filter()
    derivative_orders_filter = composer.chain_stream_orders_filter()
    spot_orderbooks_filter = composer.chain_stream_orderbooks_filter()
    derivative_orderbooks_filter = composer.chain_stream_orderbooks_filter()
    positions_filter = composer.chain_stream_positions_filter()
    oracle_price_filter = composer.chain_stream_oracle_price_filter()
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
        oracle_price_filter=oracle_price_filter
    )
    async for event in stream:
        print(json_format.MessageToJson(
            message=event,
            including_default_value_fields=True,
            preserving_proto_field_name=True)
        )


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
