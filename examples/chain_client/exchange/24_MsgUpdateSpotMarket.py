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
    message = composer.msg_update_spot_market(
        admin=address.to_acc_bech32(),
        market_id="0x215970bfdea5c94d8e964a759d3ce6eae1d113900129cc8428267db5ccdb3d1a",
        new_ticker="INJ/USDC 2",
        new_min_price_tick_size=Decimal("0.01"),
        new_min_quantity_tick_size=Decimal("0.01"),
        new_min_notional=Decimal("2"),
    )

    # broadcast the transaction
    result = await message_broadcaster.broadcast([message])
    print("---Transaction Response---")
    print(result)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
