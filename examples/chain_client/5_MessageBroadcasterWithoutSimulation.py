import asyncio
import os
import uuid
from decimal import Decimal

import dotenv

from pyinjective.composer import Composer as ProtoMsgComposer
from pyinjective.core.broadcaster import MsgBroadcasterWithPk
from pyinjective.core.network import Network
from pyinjective.wallet import PrivateKey


async def main() -> None:
    dotenv.load_dotenv()
    private_key_in_hexa = os.getenv("INJECTIVE_PRIVATE_KEY")

    # select network: local, testnet, mainnet
    network = Network.testnet()
    composer = ProtoMsgComposer(network=network.string())

    message_broadcaster = MsgBroadcasterWithPk.new_without_simulation(
        network=network,
        private_key=private_key_in_hexa,
    )

    priv_key = PrivateKey.from_hex(private_key_in_hexa)
    pub_key = priv_key.to_public_key()
    address = pub_key.to_address()
    subaccount_id = address.get_subaccount_id(index=0)

    # prepare trade info
    fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"

    spot_market_id_create = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"

    spot_orders_to_create = [
        composer.spot_order(
            market_id=spot_market_id_create,
            subaccount_id=subaccount_id,
            fee_recipient=fee_recipient,
            price=Decimal("3"),
            quantity=Decimal("55"),
            order_type="BUY",
            cid=str(uuid.uuid4()),
        ),
        composer.spot_order(
            market_id=spot_market_id_create,
            subaccount_id=subaccount_id,
            fee_recipient=fee_recipient,
            price=Decimal("300"),
            quantity=Decimal("55"),
            order_type="SELL",
            cid=str(uuid.uuid4()),
        ),
    ]

    # prepare tx msg
    msg = composer.msg_batch_update_orders(
        sender=address.to_acc_bech32(),
        spot_orders_to_create=spot_orders_to_create,
    )

    # broadcast the transaction
    result = await message_broadcaster.broadcast([msg])
    print("---Transaction Response---")
    print(result)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
