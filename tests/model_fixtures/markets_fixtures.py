from decimal import Decimal

import pytest

from pyinjective.core.market import BinaryOptionMarket, DerivativeMarket, SpotMarket
from tests.model_fixtures.markets_v2_fixtures import inj_token  # noqa: F401
from tests.model_fixtures.markets_v2_fixtures import usdt_perp_token  # noqa: F401
from tests.model_fixtures.markets_v2_fixtures import usdt_token  # noqa: F401; noqa: F401


@pytest.fixture
def inj_usdt_spot_market(inj_token, usdt_token):
    market = SpotMarket(
        id="0x7a57e705bb4e09c88aecfc295569481dbf2fe1d5efe364651fbe72385938e9b0",
        status="active",
        ticker="INJ/USDT",
        base_token=inj_token,
        quote_token=usdt_token,
        maker_fee_rate=Decimal("-0.0001"),
        taker_fee_rate=Decimal("0.001"),
        service_provider_fee=Decimal("0.4"),
        min_price_tick_size=Decimal("0.000000000000001"),
        min_quantity_tick_size=Decimal("1000000000000000"),
        min_notional=Decimal("0.000000000001"),
    )

    return market


@pytest.fixture
def btc_usdt_perp_market(usdt_perp_token):
    market = DerivativeMarket(
        id="0x4ca0f92fc28be0c9761326016b5a1a2177dd6375558365116b5bdda9abc229ce",
        status="active",
        ticker="BTC/USDT PERP",
        oracle_base="BTC",
        oracle_quote=usdt_perp_token.symbol,
        oracle_type="bandibc",
        oracle_scale_factor=6,
        initial_margin_ratio=Decimal("0.095"),
        maintenance_margin_ratio=Decimal("0.025"),
        quote_token=usdt_perp_token,
        maker_fee_rate=Decimal("-0.0001"),
        taker_fee_rate=Decimal("0.001"),
        service_provider_fee=Decimal("0.4"),
        min_price_tick_size=Decimal("1000000"),
        min_quantity_tick_size=Decimal("0.0001"),
        min_notional=Decimal("0.000001"),
    )

    return market


@pytest.fixture
def first_match_bet_market(usdt_token):
    market = BinaryOptionMarket(
        id="0x230dcce315364ff6360097838701b14713e2f4007d704df20ed3d81d09eec957",
        status="active",
        ticker="5fdbe0b1-1707800399-WAS",
        oracle_symbol="Frontrunner",
        oracle_provider="Frontrunner",
        oracle_type="provider",
        oracle_scale_factor=6,
        expiration_timestamp=1707800399,
        settlement_timestamp=1707843599,
        quote_token=usdt_token,
        maker_fee_rate=Decimal("0"),
        taker_fee_rate=Decimal("0"),
        service_provider_fee=Decimal("0.4"),
        min_price_tick_size=Decimal("10000"),
        min_quantity_tick_size=Decimal("1"),
        min_notional=Decimal("0.000001"),
    )

    return market
