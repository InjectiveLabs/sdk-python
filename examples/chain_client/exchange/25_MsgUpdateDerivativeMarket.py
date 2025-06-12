import asyncio
import json
import os
from decimal import Decimal

import dotenv

from pyinjective.async_client_v2 import AsyncClient
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

    gas_price = await client.current_chain_gas_price()
    # adjust gas price to make it valid even if it changes between the time it is requested and the TX is broadcasted
    gas_price = int(gas_price * 1.1)

    message_broadcaster = MsgBroadcasterWithPk.new_using_simulation(
        network=network,
        private_key=configured_private_key,
        gas_price=gas_price,
        client=client,
        composer=composer,
    )

    # load account
    priv_key = PrivateKey.from_hex(configured_private_key)
    pub_key = priv_key.to_public_key()
    address = pub_key.to_address()
    await client.fetch_account(address.to_acc_bech32())

    # prepare tx msg
    message = composer.msg_update_derivative_market(
        admin=address.to_acc_bech32(),
        market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
        new_ticker="INJ/USDT PERP 2",
        new_min_price_tick_size=Decimal("1"),
        new_min_quantity_tick_size=Decimal("1"),
        new_min_notional=Decimal("2"),
        new_initial_margin_ratio=Decimal("0.40"),
        new_maintenance_margin_ratio=Decimal("0.085"),
        new_reduce_margin_ratio=Decimal("3.5"),
    )

    # broadcast the transaction
    result = await message_broadcaster.broadcast([message])
    print("---Transaction Response---")
    print(json.dumps(result, indent=2))

    gas_price = await client.current_chain_gas_price()
    # adjust gas price to make it valid even if it changes between the time it is requested and the TX is broadcasted
    gas_price = int(gas_price * 1.1)
    message_broadcaster.update_gas_price(gas_price=gas_price)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
