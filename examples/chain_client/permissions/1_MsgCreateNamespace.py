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

    denom = "factory/inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r/inj_test"
    role1 = composer.permissions_role(
        name="EVERYONE",
        role_id=0,
        permissions=composer.PERMISSIONS_ACTION["RECEIVE"] | composer.PERMISSIONS_ACTION["SEND"],
    )
    role2 = composer.permissions_role(
        name="admin",
        role_id=1,
        permissions=composer.PERMISSIONS_ACTION["MODIFY_ROLE_PERMISSIONS"]
        | composer.PERMISSIONS_ACTION["MODIFY_ADDRESS_ROLES"],
    )
    role3 = composer.permissions_role(
        name="user",
        role_id=2,
        permissions=composer.PERMISSIONS_ACTION["MINT"]
        | composer.PERMISSIONS_ACTION["RECEIVE"]
        | composer.PERMISSIONS_ACTION["BURN"]
        | composer.PERMISSIONS_ACTION["SEND"],
    )

    actor_role1 = composer.permissions_actor_roles(
        actor="inj1specificactoraddress",
        roles=["admin"],
    )
    actor_role2 = composer.permissions_actor_roles(
        actor="inj1anotheractoraddress",
        roles=["user"],
    )

    role_manager = composer.permissions_role_manager(
        manager="inj1manageraddress",
        roles=["admin"],
    )

    policy_status1 = composer.permissions_policy_status(
        action=composer.PERMISSIONS_ACTION["MINT"],
        is_disabled=False,
        is_sealed=False,
    )
    policy_status2 = composer.permissions_policy_status(
        action=composer.PERMISSIONS_ACTION["BURN"],
        is_disabled=False,
        is_sealed=False,
    )

    policy_manager_capability = composer.permissions_policy_manager_capability(
        manager="inj1policymanageraddress",
        action=composer.PERMISSIONS_ACTION["MODIFY_CONTRACT_HOOK"],
        can_disable=True,
        can_seal=False,
    )

    message = composer.msg_create_namespace(
        sender=address.to_acc_bech32(),
        denom=denom,
        contract_hook="",
        role_permissions=[role1, role2, role3],
        actor_roles=[actor_role1, actor_role2],
        role_managers=[role_manager],
        policy_statuses=[policy_status1, policy_status2],
        policy_manager_capabilities=[policy_manager_capability],
    )

    # broadcast the transaction
    result = await message_broadcaster.broadcast([message])
    print("---Transaction Response---")
    print(result)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
