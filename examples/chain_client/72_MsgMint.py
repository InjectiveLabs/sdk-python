import asyncio

from pyinjective.composer import Composer as ProtoMsgComposer
from pyinjective.core.broadcaster import MsgBroadcasterWithPk
from pyinjective.core.network import Network
from pyinjective.wallet import PrivateKey


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    composer = ProtoMsgComposer(network=network.string())
    private_key_in_hexa = "f9db9bf330e23cb7839039e944adef6e9df447b90b503d5b4464c90bea9022f3"

    message_broadcaster = MsgBroadcasterWithPk.new_using_simulation(
        network=network,
        private_key=private_key_in_hexa,
    )

    priv_key = PrivateKey.from_hex(private_key_in_hexa)
    pub_key = priv_key.to_public_key()
    address = pub_key.to_address()

    amount = composer.Coin(amount=1_000_000_000, denom="factory/inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r/inj_test")

    message = composer.msg_mint(
        sender=address.to_acc_bech32(),
        amount=amount,
    )

    # broadcast the transaction
    result = await message_broadcaster.broadcast([message])
    print("---Transaction Response---")
    print(result)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
