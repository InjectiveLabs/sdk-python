from decimal import Decimal

import pytest

from pyinjective import PrivateKey
from pyinjective.composer_v2 import Composer
from pyinjective.core.network import Network
from pyinjective.orderhash import OrderHashManager


class TestOrderHashManager:
    @pytest.mark.parametrize(
        "market_type, order_type, expected_hash",
        [
            ("spot", "BUY_ATOMIC", "0xd7f96af457ff8a4716b6efafef25eaf180402b09f5b3aefd9a81c36ed40cc643"),
            ("spot", "SELL_ATOMIC", "0x0239ab5b044a60423f96e54c5357b1925232b5961459b68b4cc42a0ed27dbd1b"),
            ("derivative", "BUY_ATOMIC", "0xde67507b057368a290901557bd927dbcd92f70750ca02ac42acbcc5560883f1e"),
            ("derivative", "SELL_ATOMIC", "0xb02d0f3591047de953ae451b775487340dd3e4f38e308bc52556a9219a4bdb4f"),
        ],
    )
    def test_atomic_order_hash(self, requests_mock, market_type, order_type, expected_hash):
        # Fixed vectors use an independent EIP-712 encoder and the chain's typed-data schema.
        network = Network.devnet()
        composer = Composer(network=network.string())
        address = PrivateKey.from_mnemonic("test one few words").to_public_key().to_address()
        subaccount_id = address.get_subaccount_id(index=0)
        url = network.lcd_endpoint + "/injective/exchange/v1beta1/exchange/" + subaccount_id
        requests_mock.get(url, json={"nonce": 0})
        manager = OrderHashManager(address=address, network=network, subaccount_indexes=[0])

        market_id = (
            "0xa508cb32923323679f29a032c70342c147c17d0145625922b0ef22e955c844c0"
            if market_type == "spot"
            else "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
        )
        arguments = {
            "market_id": market_id,
            "sender": address.to_acc_bech32(),
            "subaccount_id": subaccount_id,
            "fee_recipient": "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r",
            "price": Decimal("100.5"),
            "quantity": Decimal("2"),
            "order_type": order_type,
        }
        if market_type == "derivative":
            arguments["margin"] = Decimal("20.1")
        order = getattr(composer, f"msg_create_{market_type}_market_order")(**arguments).order

        hashes = manager.compute_order_hashes(
            spot_orders=[order] if market_type == "spot" else [],
            derivative_orders=[order] if market_type == "derivative" else [],
            subaccount_index=0,
        )

        assert hashes.spot == ([expected_hash] if market_type == "spot" else [])
        assert hashes.derivative == ([expected_hash] if market_type == "derivative" else [])

    def test_spot_order_hash(self, requests_mock):
        network = Network.devnet()
        composer = Composer(network=network.string())
        priv_key = PrivateKey.from_mnemonic("test one few words")
        pub_key = priv_key.to_public_key()
        address = pub_key.to_address()

        subaccount_id = address.get_subaccount_id(index=0)

        url = network.lcd_endpoint + "/injective/exchange/v1beta1/exchange/" + subaccount_id
        requests_mock.get(url, json={"nonce": 0})
        order_hash_manager = OrderHashManager(address=address, network=network, subaccount_indexes=[0])

        spot_market_id = "0xa508cb32923323679f29a032c70342c147c17d0145625922b0ef22e955c844c0"
        fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"

        spot_orders = [
            composer.spot_order(
                market_id=spot_market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=Decimal("0.524"),
                quantity=Decimal("0.01"),
                order_type="BUY",
            ),
            composer.spot_order(
                market_id=spot_market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=Decimal("27.92"),
                quantity=Decimal("0.01"),
                order_type="SELL",
            ),
        ]

        order_hashes_response = order_hash_manager.compute_order_hashes(
            spot_orders=spot_orders, derivative_orders=[], subaccount_index=0
        )

        assert len(order_hashes_response.spot) == 2
        assert len(order_hashes_response.derivative) == 0
        assert order_hashes_response.spot[0] == "0x4f70723b33db271e6c56201e42c5911dd97a9f5345c7fcf12eb69c2689f94e78"
        assert order_hashes_response.spot[1] == "0x2cc1acacf0e576ea41e9381725f4c78fc5c191f9df4e3e98402c09b8ad2c82e8"
