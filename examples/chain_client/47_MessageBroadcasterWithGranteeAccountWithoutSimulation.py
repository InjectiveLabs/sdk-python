import asyncio

from pyinjective.composer import Composer as ProtoMsgComposer
from pyinjective.async_client import AsyncClient
from pyinjective.core.broadcaster import MsgBroadcasterWithPk
from pyinjective.constant import Network
from pyinjective.wallet import PrivateKey, Address


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    composer = ProtoMsgComposer(network=network.string())

    # initialize grpc client
    client = AsyncClient(network, insecure=False)
    await client.sync_timeout_height()

    # load account
    private_key_in_hexa = "5d386fbdbf11f1141010f81a46b40f94887367562bd33b452bbaa6ce1cd1381e"
    priv_key = PrivateKey.from_hex(private_key_in_hexa)
    pub_key = priv_key.to_public_key()
    address = pub_key.to_address()

    message_broadcaster = MsgBroadcasterWithPk.new_for_grantee_account_without_simulation(
        network=network,
        grantee_private_key=private_key_in_hexa,
        use_secure_connection=True
    )

    # prepare tx msg
    market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
    granter_inj_address = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
    granter_address = Address.from_acc_bech32(granter_inj_address)
    granter_subaccount_id = granter_address.get_subaccount_id(index=0)

    msg = composer.MsgCreateSpotLimitOrder(
        sender=granter_inj_address,
        market_id=market_id,
        subaccount_id=granter_subaccount_id,
        fee_recipient=address.to_acc_bech32(),
        price=7.523,
        quantity=0.01,
        is_buy=True,
        is_po=False
    )

    # broadcast the transaction
    result = await message_broadcaster.broadcast([msg])
    print("---Transaction Response---")
    print(result)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
