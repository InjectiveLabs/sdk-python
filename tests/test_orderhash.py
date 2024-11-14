from decimal import Decimal

import pytest

from pyinjective import PrivateKey
from pyinjective.composer import Composer
from pyinjective.core.network import Network
from pyinjective.orderhash import OrderHashManager
from tests.model_fixtures.markets_fixtures import (  # noqa: F401
    btc_usdt_perp_market,
    first_match_bet_market,
    inj_token,
    inj_usdt_spot_market,
    usdt_perp_token,
    usdt_token,
)


class TestOrderHashManager:
    @pytest.fixture
    def basic_composer(self, inj_usdt_spot_market, btc_usdt_perp_market, first_match_bet_market):
        composer = Composer(
            network=Network.devnet().string(),
            spot_markets={inj_usdt_spot_market.id: inj_usdt_spot_market},
            derivative_markets={btc_usdt_perp_market.id: btc_usdt_perp_market},
            binary_option_markets={first_match_bet_market.id: first_match_bet_market},
            tokens={
                inj_usdt_spot_market.base_token.symbol: inj_usdt_spot_market.base_token,
                inj_usdt_spot_market.quote_token.symbol: inj_usdt_spot_market.quote_token,
                btc_usdt_perp_market.quote_token.symbol: btc_usdt_perp_market.quote_token,
            },
        )

        return composer

    def test_spot_order_hash(self, requests_mock, basic_composer):
        network = Network.devnet()
        priv_key = PrivateKey.from_mnemonic("test one few words")
        pub_key = priv_key.to_public_key()
        address = pub_key.to_address()

        subaccount_id = address.get_subaccount_id(index=0)

        url = network.lcd_endpoint + "/injective/exchange/v1beta1/exchange/" + subaccount_id
        requests_mock.get(url, json={"nonce": 0})
        order_hash_manager = OrderHashManager(address=address, network=network, subaccount_indexes=[0])

        spot_market_id = list(basic_composer.spot_markets.keys())[0]
        fee_recipient = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"

        spot_orders = [
            basic_composer.spot_order(
                market_id=spot_market_id,
                subaccount_id=subaccount_id,
                fee_recipient=fee_recipient,
                price=Decimal("0.524"),
                quantity=Decimal("0.01"),
                order_type="BUY",
            ),
            basic_composer.spot_order(
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
        assert order_hashes_response.spot[0] == "0x79f259a10d813f11c9582b94950b5a0922180c1b2785638d8aefa04e0c8ae4aa"
        assert order_hashes_response.spot[1] == "0x96c2c4a5d38a20457e8f3319b9aac194ad03b2ce80d0acd718190487bf12e434"
