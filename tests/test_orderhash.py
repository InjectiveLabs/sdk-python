from decimal import Decimal

from pyinjective import PrivateKey
from pyinjective.composer import Composer
from pyinjective.core.network import Network
from pyinjective.orderhash import OrderHashManager


class TestOrderHashManager:
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
        assert order_hashes_response.spot[0] == "0x6b1e4d1fb3012735dd5e386175eb4541c024e0d8dbfeb452767b973d70ae0924"
        assert order_hashes_response.spot[1] == "0xb36146f913955d989269732d167ec554e6d0d544411d82d7f86aef18350b252b"
