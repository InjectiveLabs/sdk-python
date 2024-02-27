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
    network = Network.testnet()
    composer = ProtoMsgComposer(network=network.string())

    message_broadcaster = MsgBroadcasterWithPk.new_without_simulation(
        network=network,
        private_key=private_key_in_hexa,
    )

    priv_key = PrivateKey.from_hex(private_key_in_hexa)
    pub_key = priv_key.to_public_key()
    address = pub_key.to_address()

    message = composer.msg_change_admin(
        sender=address.to_acc_bech32(),
        denom="factory/inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r/inj_test",
        new_admin="inj1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqe2hm49",  # This is the zero address to remove admin permissions
    )

    # broadcast the transaction
    result = await message_broadcaster.broadcast([message])
    print("---Transaction Response---")
    print(result)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
