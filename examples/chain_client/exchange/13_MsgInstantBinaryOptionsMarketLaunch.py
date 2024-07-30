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
    message = composer.msg_instant_binary_options_market_launch(
        sender=address.to_acc_bech32(),
        ticker="UFC-KHABIB-TKO-05/30/2023",
        oracle_symbol="UFC-KHABIB-TKO-05/30/2023",
        oracle_provider="UFC",
        oracle_type="Provider",
        oracle_scale_factor=6,
        maker_fee_rate=Decimal("0.0005"),  # 0.05%
        taker_fee_rate=Decimal("0.0010"),  # 0.10%
        expiration_timestamp=1680730982,
        settlement_timestamp=1690730982,
        admin=address.to_acc_bech32(),
        quote_denom="peggy0xdAC17F958D2ee523a2206206994597C13D831ec7",
        min_price_tick_size=Decimal("0.01"),
        min_quantity_tick_size=Decimal("0.01"),
        min_notional=Decimal("1"),
    )

    # broadcast the transaction
    result = await message_broadcaster.broadcast([message])
    print("---Transaction Response---")
    print(result)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
