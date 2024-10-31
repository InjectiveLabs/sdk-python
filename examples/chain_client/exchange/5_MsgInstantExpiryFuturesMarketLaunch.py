import asyncio
import os
from decimal import Decimal

import dotenv

from pyinjective.async_client import AsyncClient
from pyinjective.core.broadcaster import MsgBroadcasterWithPk
from pyinjective.core.network import Network
from pyinjective.wallet import PrivateKey


async def main() -> None:
    dotenv.load_dotenv()
    configured_private_key = os.getenv("INJECTIVE_PRIVATE_KEY")

    # select network: local, testnet, mainnet
    network = Network.testnet()

    # initialize grpc client
    client = AsyncClient(network)
    await client.initialize_tokens_from_chain_denoms()
    composer = await client.composer()
    await client.sync_timeout_height()

    message_broadcaster = MsgBroadcasterWithPk.new_using_simulation(
        network=network,
        private_key=configured_private_key,
    )

    # load account
    priv_key = PrivateKey.from_hex(configured_private_key)
    pub_key = priv_key.to_public_key()
    address = pub_key.to_address()
    await client.fetch_account(address.to_acc_bech32())

    # prepare tx msg
    message = composer.msg_instant_expiry_futures_market_launch_v2(
        sender=address.to_acc_bech32(),
        ticker="INJ/USDC FUT",
        quote_denom="factory/inj17vytdwqczqz72j65saukplrktd4gyfme5agf6c/usdc",
        oracle_base="INJ",
        oracle_quote="USDC",
        oracle_scale_factor=6,
        oracle_type="Band",
        expiry=2000000000,
        maker_fee_rate=Decimal("-0.0001"),
        taker_fee_rate=Decimal("0.001"),
        initial_margin_ratio=Decimal("0.33"),
        maintenance_margin_ratio=Decimal("0.095"),
        min_price_tick_size=Decimal("0.001"),
        min_quantity_tick_size=Decimal("0.01"),
        min_notional=Decimal("1"),
    )

    # broadcast the transaction
    result = await message_broadcaster.broadcast([message])
    print("---Transaction Response---")
    print(result)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
