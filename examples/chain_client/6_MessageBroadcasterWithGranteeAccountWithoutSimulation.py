import asyncio
import os
import uuid
from decimal import Decimal

import dotenv

from pyinjective.async_client import AsyncClient
from pyinjective.composer import Composer as ProtoMsgComposer
from pyinjective.core.broadcaster import MsgBroadcasterWithPk
from pyinjective.core.network import Network
from pyinjective.wallet import Address, PrivateKey


async def main() -> None:
    dotenv.load_dotenv()
    private_key_in_hexa = os.getenv("INJECTIVE_GRANTEE_PRIVATE_KEY")
    granter_inj_address = os.getenv("INJECTIVE_GRANTER_PUBLIC_ADDRESS")

    # select network: local, testnet, mainnet
    network = Network.testnet()
    composer = ProtoMsgComposer(network=network.string())

    # initialize grpc client
    client = AsyncClient(network)
    await client.sync_timeout_height()

    # load account
    priv_key = PrivateKey.from_hex(private_key_in_hexa)
    pub_key = priv_key.to_public_key()
    address = pub_key.to_address()

    message_broadcaster = MsgBroadcasterWithPk.new_for_grantee_account_without_simulation(
        network=network,
        grantee_private_key=private_key_in_hexa,
    )

    # prepare tx msg
    market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
    granter_address = Address.from_acc_bech32(granter_inj_address)
    granter_subaccount_id = granter_address.get_subaccount_id(index=0)

    msg = composer.msg_create_spot_limit_order_v2(
        market_id=market_id,
        sender=granter_inj_address,
        subaccount_id=granter_subaccount_id,
        fee_recipient=address.to_acc_bech32(),
        price=Decimal("7.523"),
        quantity=Decimal("0.01"),
        order_type="BUY",
        cid=str(uuid.uuid4()),
    )

    # broadcast the transaction
    result = await message_broadcaster.broadcast([msg])
    print("---Transaction Response---")
    print(result)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
