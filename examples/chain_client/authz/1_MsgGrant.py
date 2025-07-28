import asyncio
import json
import os

import dotenv

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.broadcaster import MsgBroadcasterWithPk
from pyinjective.core.network import Network
from pyinjective.wallet import PrivateKey


async def main() -> None:
    dotenv.load_dotenv()
    private_key_in_hexa = os.getenv("INJECTIVE_PRIVATE_KEY")
    grantee_public_address = os.getenv("INJECTIVE_GRANTEE_PUBLIC_ADDRESS")

    # select network: local, testnet, mainnet
    network = Network.testnet()

    # initialize grpc client
    client = AsyncClient(network)
    composer = await client.composer()

    gas_price = await client.current_chain_gas_price()
    # adjust gas price to make it valid even if it changes between the time it is requested and the TX is broadcasted
    gas_price = int(gas_price * 1.1)

    message_broadcaster = MsgBroadcasterWithPk.new_using_gas_heuristics(
        network=network,
        private_key=private_key_in_hexa,
        gas_price=gas_price,
        client=client,
        composer=composer,
    )

    priv_key = PrivateKey.from_hex(private_key_in_hexa)
    pub_key = priv_key.to_public_key()
    address = pub_key.to_address()
    # subaccount_id = address.get_subaccount_id(index=0)
    # market_ids = ["0x0511ddc4e6586f3bfe1acb2dd905f8b8a82c97e1edaef654b12ca7e6031ca0fa"]

    # prepare tx msg

    # GENERIC AUTHZ
    msg = composer.msg_grant_generic(
        granter=address.to_acc_bech32(),
        grantee=grantee_public_address,
        msg_type="/injective.exchange.v2.MsgCreateSpotLimitOrder",
        expire_in=31536000,  # 1 year
    )

    # TYPED AUTHZ
    # msg = composer.msg_grant_typed(
    #     granter = "inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku",
    #     grantee = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r",
    #     msg_type = "CreateSpotLimitOrderAuthz",
    #     expire_in=31536000, # 1 year
    #     subaccount_id=subaccount_id,
    #     market_ids=market_ids
    # )

    # broadcast the transaction
    result = await message_broadcaster.broadcast([msg])
    print("---Transaction Response---")
    print(json.dumps(result, indent=2))

    gas_price = await client.current_chain_gas_price()
    # adjust gas price to make it valid even if it changes between the time it is requested and the TX is broadcasted
    gas_price = int(gas_price * 1.1)
    message_broadcaster.update_gas_price(gas_price=gas_price)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
