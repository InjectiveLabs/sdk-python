import asyncio
import json
import os

import dotenv

from pyinjective.async_client import AsyncClient
from pyinjective.core.broadcaster import MsgBroadcasterWithPk
from pyinjective.core.network import Network
from pyinjective.wallet import PrivateKey


async def main() -> None:
    dotenv.load_dotenv()
    private_key_in_hexa = os.getenv("INJECTIVE_PRIVATE_KEY")

    # select network: local, testnet, mainnet
    network = Network.devnet()

    client = AsyncClient(network)
    composer = await client.composer()

    gas_price = await client.current_chain_gas_price()
    # adjust gas price to make it valid even if it changes between the time it is requested and the TX is broadcasted
    gas_price = int(gas_price * 1.1)

    message_broadcaster = MsgBroadcasterWithPk.new_using_simulation(
        network=network,
        private_key=private_key_in_hexa,
        gas_price=gas_price,
        client=client,
        composer=composer,
    )

    priv_key = PrivateKey.from_hex(private_key_in_hexa)
    pub_key = priv_key.to_public_key()
    address = pub_key.to_address()

    denom = "factory/inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r/inj_test"

    role1 = composer.permissions_role(
        name="EVERYONE",
        role_id=0,
        permissions=composer.PERMISSIONS_ACTION["UNSPECIFIED"],  # revoke all permissions
    )
    role2 = composer.permissions_role(
        name="user",
        role_id=2,
        permissions=composer.PERMISSIONS_ACTION["RECEIVE"] | composer.PERMISSIONS_ACTION["SEND"],
    )

    role_manager = composer.permissions_role_manager(
        manager="inj1manageraddress",
        roles=["admin", "user"],
    )

    policy_status1 = composer.permissions_policy_status(
        action=composer.PERMISSIONS_ACTION["MINT"],
        is_disabled=True,
        is_sealed=False,
    )
    policy_status2 = composer.permissions_policy_status(
        action=composer.PERMISSIONS_ACTION["BURN"],
        is_disabled=False,
        is_sealed=True,
    )

    policy_manager_capability = composer.permissions_policy_manager_capability(
        manager="inj1policymanageraddress",
        action=composer.PERMISSIONS_ACTION["MODIFY_ROLE_PERMISSIONS"],
        can_disable=True,
        can_seal=False,
    )

    message = composer.msg_update_namespace(
        sender=address.to_acc_bech32(),
        denom=denom,
        contract_hook="inj19ld6swyldyujcn72j7ugnu9twafhs9wxlyye5m",
        role_permissions=[role1, role2],
        role_managers=[role_manager],
        policy_statuses=[policy_status1, policy_status2],
        policy_manager_capabilities=[policy_manager_capability],
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
