import asyncio
import os
import uuid
from decimal import Decimal

import dotenv

from pyinjective.async_client import AsyncClient
from pyinjective.constant import GAS_FEE_BUFFER_AMOUNT, GAS_PRICE
from pyinjective.core.network import Network
from pyinjective.orderhash import OrderHashManager
from pyinjective.transaction import Transaction
from pyinjective.wallet import PrivateKey


async def main() -> None:
    dotenv.load_dotenv()
    configured_private_key = os.getenv("INJECTIVE_PRIVATE_KEY")

    # select network: local, testnet, mainnet
    network = Network.testnet()

    # initialize grpc client
    client = AsyncClient(network)
    composer = await client.composer()
    await client.sync_timeout_height()

    # load account
    priv_key = PrivateKey.from_hex(configured_private_key)
    pub_key = priv_key.to_public_key()
    address = pub_key.to_address()
    await client.fetch_account(address.to_acc_bech32())
    subaccount_id = address.get_subaccount_id(index=0)
    subaccount_id_2 = address.get_subaccount_id(index=1)

    order_hash_manager = OrderHashManager(address=address, network=network, subaccount_indexes=[0, 1, 2, 7])

    # prepare trade info
    spot_market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
    deriv_market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
    fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"

    spot_orders = [
        composer.create_v2_spot_order(
            market_id=spot_market_id,
            subaccount_id=subaccount_id,
            fee_recipient=fee_recipient,
            price=Decimal("0.524"),
            quantity=Decimal("0.01"),
            order_type="BUY",
            cid=str(uuid.uuid4()),
        ),
        composer.create_v2_spot_order(
            market_id=spot_market_id,
            subaccount_id=subaccount_id,
            fee_recipient=fee_recipient,
            price=Decimal("27.92"),
            quantity=Decimal("0.01"),
            order_type="SELL",
            cid=str(uuid.uuid4()),
        ),
    ]

    derivative_orders = [
        composer.create_v2_derivative_order(
            market_id=deriv_market_id,
            subaccount_id=subaccount_id,
            fee_recipient=fee_recipient,
            price=Decimal(10500),
            quantity=Decimal(0.01),
            margin=composer.calculate_margin(
                quantity=Decimal(0.01), price=Decimal(10500), leverage=Decimal(2), is_reduce_only=False
            ),
            order_type="BUY",
            cid=str(uuid.uuid4()),
        ),
        composer.create_v2_derivative_order(
            market_id=deriv_market_id,
            subaccount_id=subaccount_id,
            fee_recipient=fee_recipient,
            price=Decimal(65111),
            quantity=Decimal(0.01),
            margin=composer.calculate_margin(
                quantity=Decimal(0.01), price=Decimal(65111), leverage=Decimal(2), is_reduce_only=False
            ),
            order_type="SELL",
            cid=str(uuid.uuid4()),
        ),
    ]

    # prepare tx msg
    spot_msg = composer.msg_batch_create_spot_limit_orders_v2(sender=address.to_acc_bech32(), orders=spot_orders)

    deriv_msg = composer.msg_batch_create_derivative_limit_orders_v2(
        sender=address.to_acc_bech32(), orders=derivative_orders
    )

    # compute order hashes
    order_hashes = order_hash_manager.compute_order_hashes(
        spot_orders=spot_orders, derivative_orders=derivative_orders, subaccount_index=0
    )

    print("computed spot order hashes", order_hashes.spot)
    print("computed derivative order hashes", order_hashes.derivative)

    # build tx 1
    tx = (
        Transaction()
        .with_messages(spot_msg, deriv_msg)
        .with_sequence(client.get_sequence())
        .with_account_num(client.get_number())
        .with_chain_id(network.chain_id)
    )
    gas_price = GAS_PRICE
    base_gas = 85000
    gas_limit = base_gas + GAS_FEE_BUFFER_AMOUNT  # add buffer for gas fee computation
    gas_fee = "{:.18f}".format((gas_price * gas_limit) / pow(10, 18)).rstrip("0")
    fee = [
        composer.coin(
            amount=gas_price * gas_limit,
            denom=network.fee_denom,
        )
    ]
    tx = tx.with_gas(gas_limit).with_fee(fee).with_memo("").with_timeout_height(client.timeout_height)
    sign_doc = tx.get_sign_doc(pub_key)
    sig = priv_key.sign(sign_doc.SerializeToString())
    tx_raw_bytes = tx.get_tx_data(sig, pub_key)

    # broadcast tx: send_tx_async_mode, send_tx_sync_mode, send_tx_block_mode
    res = await client.broadcast_tx_sync_mode(tx_raw_bytes)
    print(res)
    print("gas wanted: {}".format(gas_limit))
    print("gas fee: {} INJ".format(gas_fee))

    # compute order hashes
    order_hashes = order_hash_manager.compute_order_hashes(
        spot_orders=spot_orders, derivative_orders=derivative_orders, subaccount_index=0
    )

    print("computed spot order hashes", order_hashes.spot)
    print("computed derivative order hashes", order_hashes.derivative)

    # build tx 2
    tx = (
        Transaction()
        .with_messages(spot_msg, deriv_msg)
        .with_sequence(client.get_sequence())
        .with_account_num(client.get_number())
        .with_chain_id(network.chain_id)
    )
    gas_price = GAS_PRICE
    base_gas = 85000
    gas_limit = base_gas + GAS_FEE_BUFFER_AMOUNT  # add buffer for gas fee computation
    gas_fee = "{:.18f}".format((gas_price * gas_limit) / pow(10, 18)).rstrip("0")
    fee = [
        composer.coin(
            amount=gas_price * gas_limit,
            denom=network.fee_denom,
        )
    ]
    tx = tx.with_gas(gas_limit).with_fee(fee).with_memo("").with_timeout_height(client.timeout_height)
    sign_doc = tx.get_sign_doc(pub_key)
    sig = priv_key.sign(sign_doc.SerializeToString())
    tx_raw_bytes = tx.get_tx_data(sig, pub_key)

    # broadcast tx: send_tx_async_mode, send_tx_sync_mode, send_tx_block_mode
    res = await client.broadcast_tx_sync_mode(tx_raw_bytes)
    print(res)
    print("gas wanted: {}".format(gas_limit))
    print("gas fee: {} INJ".format(gas_fee))

    spot_orders = [
        composer.spot_order(
            market_id=spot_market_id,
            subaccount_id=subaccount_id_2,
            fee_recipient=fee_recipient,
            price=Decimal("1.524"),
            quantity=Decimal("0.01"),
            order_type="BUY_PO",
            cid=str(uuid.uuid4()),
        ),
        composer.spot_order(
            market_id=spot_market_id,
            subaccount_id=subaccount_id_2,
            fee_recipient=fee_recipient,
            price=Decimal("27.92"),
            quantity=Decimal("0.01"),
            order_type="SELL_PO",
            cid=str(uuid.uuid4()),
        ),
    ]

    derivative_orders = [
        composer.derivative_order(
            market_id=deriv_market_id,
            subaccount_id=subaccount_id_2,
            fee_recipient=fee_recipient,
            price=Decimal(25111),
            quantity=Decimal(0.01),
            margin=composer.calculate_margin(
                quantity=Decimal(0.01), price=Decimal(25111), leverage=Decimal("1.5"), is_reduce_only=False
            ),
            order_type="BUY",
            cid=str(uuid.uuid4()),
        ),
        composer.derivative_order(
            market_id=deriv_market_id,
            subaccount_id=subaccount_id_2,
            fee_recipient=fee_recipient,
            price=Decimal(65111),
            quantity=Decimal(0.01),
            margin=composer.calculate_margin(
                quantity=Decimal(0.01), price=Decimal(25111), leverage=Decimal(2), is_reduce_only=False
            ),
            order_type="SELL",
            cid=str(uuid.uuid4()),
        ),
    ]

    # prepare tx msg
    spot_msg = composer.msg_batch_create_spot_limit_orders_v2(sender=address.to_acc_bech32(), orders=spot_orders)

    deriv_msg = composer.msg_batch_create_derivative_limit_orders_v2(
        sender=address.to_acc_bech32(), orders=derivative_orders
    )

    # compute order hashes
    order_hashes = order_hash_manager.compute_order_hashes(
        spot_orders=spot_orders, derivative_orders=derivative_orders, subaccount_index=1
    )

    print("computed spot order hashes", order_hashes.spot)
    print("computed derivative order hashes", order_hashes.derivative)

    # build tx 3
    tx = (
        Transaction()
        .with_messages(spot_msg, deriv_msg)
        .with_sequence(client.get_sequence())
        .with_account_num(client.get_number())
        .with_chain_id(network.chain_id)
    )
    gas_price = GAS_PRICE
    base_gas = 85000
    gas_limit = base_gas + GAS_FEE_BUFFER_AMOUNT  # add buffer for gas fee computation
    gas_fee = "{:.18f}".format((gas_price * gas_limit) / pow(10, 18)).rstrip("0")
    fee = [
        composer.coin(
            amount=gas_price * gas_limit,
            denom=network.fee_denom,
        )
    ]
    tx = tx.with_gas(gas_limit).with_fee(fee).with_memo("").with_timeout_height(client.timeout_height)
    sign_doc = tx.get_sign_doc(pub_key)
    sig = priv_key.sign(sign_doc.SerializeToString())
    tx_raw_bytes = tx.get_tx_data(sig, pub_key)

    # broadcast tx: send_tx_async_mode, send_tx_sync_mode, send_tx_block_mode
    res = await client.broadcast_tx_sync_mode(tx_raw_bytes)
    print(res)
    print("gas wanted: {}".format(gas_limit))
    print("gas fee: {} INJ".format(gas_fee))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
