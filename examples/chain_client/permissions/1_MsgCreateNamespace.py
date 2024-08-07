import asyncio
import os

import dotenv

from pyinjective.composer import Composer as ProtoMsgComposer
from pyinjective.core.broadcaster import MsgBroadcasterWithPk
from pyinjective.core.network import Network
from pyinjective.wallet import PrivateKey


async def main() -> None:
    dotenv.load_dotenv()
    private_key_in_hexa = os.getenv("INJECTIVE_PRIVATE_KEY")

    # select network: local, testnet, mainnet
    network = Network.devnet()
    composer = ProtoMsgComposer(network=network.string())

    message_broadcaster = MsgBroadcasterWithPk.new_using_simulation(
        network=network,
        private_key=private_key_in_hexa,
    )

    priv_key = PrivateKey.from_hex(private_key_in_hexa)
    pub_key = priv_key.to_public_key()
    address = pub_key.to_address()

    blocked_address = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
    denom = "factory/inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r/inj_test"
    role1 = composer.permissions_role(
        role=composer.DEFAULT_PERMISSIONS_EVERYONE_ROLE,
        permissions=composer.MINT_ACTION_PERMISSION
        | composer.RECEIVE_ACTION_PERMISSION
        | composer.BURN_ACTION_PERMISSION,
    )
    role2 = composer.permissions_role(role="blacklisted", permissions=composer.UNDEFINED_ACTION_PERMISSION)
    address_role1 = composer.permissions_address_roles(address=blocked_address, roles=["blacklisted"])

    message = composer.msg_create_namespace(
        sender=address.to_acc_bech32(),
        denom=denom,
        wasm_hook="",
        mints_paused=False,
        sends_paused=False,
        burns_paused=False,
        role_permissions=[role1, role2],
        address_roles=[address_role1],
    )

    # broadcast the transaction
    result = await message_broadcaster.broadcast([message])
    print("---Transaction Response---")
    print(result)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
