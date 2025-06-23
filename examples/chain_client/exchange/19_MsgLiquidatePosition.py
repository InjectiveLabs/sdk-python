import asyncio
import json
import os
import uuid
from decimal import Decimal

import dotenv

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.broadcaster import MsgBroadcasterWithPk
from pyinjective.core.network import Network
from pyinjective.wallet import PrivateKey


async def main() -> None:
    dotenv.load_dotenv()
    private_key_in_hexa = os.getenv("INJECTIVE_PRIVATE_KEY")

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
    subaccount_id = address.get_subaccount_id(index=0)

    # prepare trade info
    market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
    fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
    cid = str(uuid.uuid4())

    order = composer.derivative_order(
        market_id=market_id,
        subaccount_id=subaccount_id,
        fee_recipient=fee_recipient,
        price=Decimal(39.01),  # This should be the liquidation price
        quantity=Decimal(0.147),
        margin=composer.calculate_margin(
            quantity=Decimal(0.147), price=Decimal(39.01), leverage=Decimal(1), is_reduce_only=False
        ),
        order_type="SELL",
        cid=cid,
    )

    # prepare tx msg
    msg = composer.msg_liquidate_position(
        sender=address.to_acc_bech32(),
        subaccount_id="0x156df4d5bc8e7dd9191433e54bd6a11eeb390921000000000000000000000000",
        market_id=market_id,
        order=order,
    )

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
