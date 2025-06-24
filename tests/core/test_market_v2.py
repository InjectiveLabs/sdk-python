from decimal import Decimal

from pyinjective.constant import ADDITIONAL_CHAIN_FORMAT_DECIMALS
from pyinjective.core.market_v2 import BinaryOptionMarket, DerivativeMarket, SpotMarket
from pyinjective.utils.denom import Denom
from tests.model_fixtures.markets_v2_fixtures import (  # noqa: F401
    btc_usdt_perp_market,
    first_match_bet_market,
    inj_token,
    inj_usdt_spot_market,
    usdt_perp_token,
    usdt_token,
)


class TestSpotMarket:
    def test_convert_quantity_to_chain_format(self, inj_usdt_spot_market: SpotMarket):
        original_quantity = Decimal("123.456789")

        chain_value = inj_usdt_spot_market.quantity_to_chain_format(human_readable_value=original_quantity)
        quantized_quantity = (
            original_quantity // inj_usdt_spot_market.min_quantity_tick_size
        ) * inj_usdt_spot_market.min_quantity_tick_size
        expected_value = quantized_quantity * Decimal(f"1e{inj_usdt_spot_market.base_token.decimals}")
        quantized_chain_format_value = expected_value * Decimal("1e18")

        assert quantized_chain_format_value == chain_value

    def test_convert_price_to_chain_format(self, inj_usdt_spot_market: SpotMarket):
        original_quantity = Decimal("123.456789")

        chain_value = inj_usdt_spot_market.price_to_chain_format(human_readable_value=original_quantity)
        price_decimals = inj_usdt_spot_market.quote_token.decimals - inj_usdt_spot_market.base_token.decimals
        quantized_value = (
            original_quantity // inj_usdt_spot_market.min_price_tick_size
        ) * inj_usdt_spot_market.min_price_tick_size
        expected_value = quantized_value * Decimal(f"1e{price_decimals}")
        quantized_chain_format_value = expected_value * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        assert quantized_chain_format_value == chain_value

    def test_convert_notional_to_chain_format(self, inj_usdt_spot_market: SpotMarket):
        original_notional = Decimal("123.456789")

        chain_value = inj_usdt_spot_market.notional_to_chain_format(human_readable_value=original_notional)
        notional_decimals = inj_usdt_spot_market.quote_token.decimals
        expected_value = original_notional * Decimal(f"1e{notional_decimals}")
        expected_chain_format_value = expected_value * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        assert expected_chain_format_value == chain_value

    def test_convert_quantity_from_chain_format(self, inj_usdt_spot_market: SpotMarket):
        expected_quantity = Decimal("123.456")

        chain_format_quantity = expected_quantity * Decimal(f"1e{inj_usdt_spot_market.base_token.decimals}")
        human_readable_quantity = inj_usdt_spot_market.quantity_from_chain_format(chain_value=chain_format_quantity)

        assert expected_quantity == human_readable_quantity

    def test_convert_price_from_chain_format(self, inj_usdt_spot_market: SpotMarket):
        expected_price = Decimal("123.456")

        price_decimals = inj_usdt_spot_market.quote_token.decimals - inj_usdt_spot_market.base_token.decimals
        chain_format_price = expected_price * Decimal(f"1e{price_decimals}")
        human_readable_price = inj_usdt_spot_market.price_from_chain_format(chain_value=chain_format_price)

        assert expected_price == human_readable_price

    def test_convert_notional_from_chain_format(self, inj_usdt_spot_market: SpotMarket):
        expected_notional = Decimal("123.456")

        notional_decimals = inj_usdt_spot_market.quote_token.decimals
        chain_format_notional = expected_notional * Decimal(f"1e{notional_decimals}")
        human_readable_notional = inj_usdt_spot_market.notional_from_chain_format(chain_value=chain_format_notional)

        assert expected_notional == human_readable_notional

    def test_convert_quantity_from_extended_chain_format(self, inj_usdt_spot_market: SpotMarket):
        expected_quantity = Decimal("123.456")

        chain_format_quantity = (
            expected_quantity
            * Decimal(f"1e{inj_usdt_spot_market.base_token.decimals}")
            * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        )
        human_readable_quantity = inj_usdt_spot_market.quantity_from_extended_chain_format(
            chain_value=chain_format_quantity
        )

        assert expected_quantity == human_readable_quantity

    def test_convert_price_from_extended_chain_format(self, inj_usdt_spot_market: SpotMarket):
        expected_price = Decimal("123.456")

        price_decimals = inj_usdt_spot_market.quote_token.decimals - inj_usdt_spot_market.base_token.decimals
        chain_format_price = (
            expected_price * Decimal(f"1e{price_decimals}") * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        )
        human_readable_price = inj_usdt_spot_market.price_from_extended_chain_format(chain_value=chain_format_price)

        assert expected_price == human_readable_price

    def test_convert_notional_from_extended_chain_format(self, inj_usdt_spot_market: SpotMarket):
        expected_notional = Decimal("123.456")

        notional_decimals = inj_usdt_spot_market.quote_token.decimals
        chain_format_notional = (
            expected_notional * Decimal(f"1e{notional_decimals}") * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        )
        human_readable_notional = inj_usdt_spot_market.notional_from_extended_chain_format(
            chain_value=chain_format_notional
        )

        assert expected_notional == human_readable_notional


class TestDerivativeMarket:
    def test_convert_quantity_to_chain_format(self, btc_usdt_perp_market: DerivativeMarket):
        original_quantity = Decimal("123.456789")

        chain_value = btc_usdt_perp_market.quantity_to_chain_format(human_readable_value=original_quantity)
        quantized_value = (
            original_quantity // btc_usdt_perp_market.min_quantity_tick_size
        ) * btc_usdt_perp_market.min_quantity_tick_size
        quantized_chain_format_value = quantized_value * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        assert quantized_chain_format_value == chain_value

    def test_convert_price_to_chain_format(self, btc_usdt_perp_market: DerivativeMarket):
        original_quantity = Decimal("123.456789")

        chain_value = btc_usdt_perp_market.price_to_chain_format(human_readable_value=original_quantity)
        price_decimals = btc_usdt_perp_market.quote_token.decimals
        quantized_value = (
            original_quantity // btc_usdt_perp_market.min_price_tick_size
        ) * btc_usdt_perp_market.min_price_tick_size
        expected_value = quantized_value * Decimal(f"1e{price_decimals}")
        quantized_chain_format_value = expected_value * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        assert quantized_chain_format_value == chain_value

    def test_convert_margin_to_chain_format(self, btc_usdt_perp_market: DerivativeMarket):
        original_quantity = Decimal("123.456789")

        chain_value = btc_usdt_perp_market.margin_to_chain_format(human_readable_value=original_quantity)
        margin_decimals = btc_usdt_perp_market.quote_token.decimals
        expected_value = original_quantity * Decimal(f"1e{margin_decimals}")
        quantized_value = (
            expected_value // btc_usdt_perp_market.min_quantity_tick_size
        ) * btc_usdt_perp_market.min_quantity_tick_size
        quantized_chain_format_value = quantized_value * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        assert quantized_chain_format_value == chain_value

    def test_convert_notional_to_chain_format(self, btc_usdt_perp_market: DerivativeMarket):
        original_notional = Decimal("123.456789")

        chain_value = btc_usdt_perp_market.notional_to_chain_format(human_readable_value=original_notional)
        notional_decimals = btc_usdt_perp_market.quote_token.decimals
        expected_value = original_notional * Decimal(f"1e{notional_decimals}")
        expected_chain_format_value = expected_value * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        assert expected_chain_format_value == chain_value

    def test_convert_quantity_from_chain_format(self, btc_usdt_perp_market: DerivativeMarket):
        expected_quantity = Decimal("123.456")

        chain_format_quantity = expected_quantity
        human_readable_quantity = btc_usdt_perp_market.quantity_from_chain_format(chain_value=chain_format_quantity)

        assert expected_quantity == human_readable_quantity

    def test_convert_price_from_chain_format(self, btc_usdt_perp_market: DerivativeMarket):
        expected_price = Decimal("123.456")

        price_decimals = btc_usdt_perp_market.quote_token.decimals
        chain_format_price = expected_price * Decimal(f"1e{price_decimals}")
        human_readable_price = btc_usdt_perp_market.price_from_chain_format(chain_value=chain_format_price)

        assert expected_price == human_readable_price

    def test_convert_margin_from_chain_format(self, btc_usdt_perp_market: DerivativeMarket):
        expected_margin = Decimal("123.456")

        price_decimals = btc_usdt_perp_market.quote_token.decimals
        chain_format_margin = expected_margin * Decimal(f"1e{price_decimals}")
        human_readable_margin = btc_usdt_perp_market.margin_from_chain_format(chain_value=chain_format_margin)

        assert expected_margin == human_readable_margin

    def test_convert_notional_from_chain_format(self, btc_usdt_perp_market: DerivativeMarket):
        expected_notional = Decimal("123.456")

        notional_decimals = btc_usdt_perp_market.quote_token.decimals
        chain_format_notional = expected_notional * Decimal(f"1e{notional_decimals}")
        human_readable_notional = btc_usdt_perp_market.notional_from_chain_format(chain_value=chain_format_notional)

        assert expected_notional == human_readable_notional

    def test_convert_quantity_from_extended_chain_format(self, btc_usdt_perp_market: DerivativeMarket):
        expected_quantity = Decimal("123.456")

        chain_format_quantity = expected_quantity * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        human_readable_quantity = btc_usdt_perp_market.quantity_from_extended_chain_format(
            chain_value=chain_format_quantity
        )

        assert expected_quantity == human_readable_quantity

    def test_convert_price_from_extended_chain_format(self, btc_usdt_perp_market: DerivativeMarket):
        expected_price = Decimal("123.456")

        price_decimals = btc_usdt_perp_market.quote_token.decimals
        chain_format_price = (
            expected_price * Decimal(f"1e{price_decimals}") * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        )
        human_readable_price = btc_usdt_perp_market.price_from_extended_chain_format(chain_value=chain_format_price)

        assert expected_price == human_readable_price

    def test_convert_margin_from_extended_chain_format(self, btc_usdt_perp_market: DerivativeMarket):
        expected_margin = Decimal("123.456")

        price_decimals = btc_usdt_perp_market.quote_token.decimals
        chain_format_margin = (
            expected_margin * Decimal(f"1e{price_decimals}") * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        )
        human_readable_margin = btc_usdt_perp_market.margin_from_extended_chain_format(chain_value=chain_format_margin)

        assert expected_margin == human_readable_margin

    def test_convert_notional_from_extended_chain_format(self, btc_usdt_perp_market: DerivativeMarket):
        expected_notional = Decimal("123.456")

        notional_decimals = btc_usdt_perp_market.quote_token.decimals
        chain_format_notional = (
            expected_notional * Decimal(f"1e{notional_decimals}") * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        )
        human_readable_notional = btc_usdt_perp_market.notional_from_extended_chain_format(
            chain_value=chain_format_notional
        )

        assert expected_notional == human_readable_notional


class TestBinaryOptionMarket:
    def test_convert_quantity_to_chain_format_with_fixed_denom(self, first_match_bet_market: BinaryOptionMarket):
        original_quantity = Decimal("123.456789")
        fixed_denom = Denom(
            description="Fixed denom",
            base=2,
            quote=4,
            min_quantity_tick_size=1,
            min_price_tick_size=1,
            min_notional=1,
        )

        chain_value = first_match_bet_market.quantity_to_chain_format(
            human_readable_value=original_quantity, special_denom=fixed_denom
        )
        quantized_value = (original_quantity // Decimal(str(fixed_denom.min_quantity_tick_size))) * Decimal(
            str(fixed_denom.min_quantity_tick_size)
        )
        chain_formatted_quantity = quantized_value * Decimal(f"1e{fixed_denom.base}")
        quantized_chain_format_value = chain_formatted_quantity * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        assert quantized_chain_format_value == chain_value

    def test_convert_quantity_to_chain_format_without_fixed_denom(self, first_match_bet_market: BinaryOptionMarket):
        original_quantity = Decimal("123.456789")

        chain_value = first_match_bet_market.quantity_to_chain_format(
            human_readable_value=original_quantity,
        )
        quantized_value = (
            original_quantity // first_match_bet_market.min_quantity_tick_size
        ) * first_match_bet_market.min_quantity_tick_size
        quantized_chain_format_value = quantized_value * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        assert quantized_chain_format_value == chain_value

    def test_convert_price_to_chain_format_with_fixed_denom(self, first_match_bet_market: BinaryOptionMarket):
        original_quantity = Decimal("123.456789")
        fixed_denom = Denom(
            description="Fixed denom",
            base=2,
            quote=4,
            min_quantity_tick_size=1,
            min_price_tick_size=1,
            min_notional=1,
        )

        chain_value = first_match_bet_market.price_to_chain_format(
            human_readable_value=original_quantity,
            special_denom=fixed_denom,
        )
        price_decimals = fixed_denom.quote
        quantized_value = (original_quantity // Decimal(str(fixed_denom.min_price_tick_size))) * Decimal(
            str(fixed_denom.min_price_tick_size)
        )
        expected_value = quantized_value * Decimal(f"1e{price_decimals}")
        quantized_chain_format_value = expected_value * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        assert quantized_chain_format_value == chain_value

    def test_convert_price_to_chain_format_without_fixed_denom(self, first_match_bet_market: BinaryOptionMarket):
        original_quantity = Decimal("123.456789")

        chain_value = first_match_bet_market.price_to_chain_format(human_readable_value=original_quantity)
        price_decimals = first_match_bet_market.quote_token.decimals
        quantized_value = (
            original_quantity // first_match_bet_market.min_price_tick_size
        ) * first_match_bet_market.min_price_tick_size
        expected_value = quantized_value * Decimal(f"1e{price_decimals}")
        quantized_chain_format_value = expected_value * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        assert quantized_chain_format_value == chain_value

    def test_convert_margin_to_chain_format_with_fixed_denom(self, first_match_bet_market: BinaryOptionMarket):
        original_quantity = Decimal("123.456789")
        fixed_denom = Denom(
            description="Fixed denom",
            base=2,
            quote=4,
            min_quantity_tick_size=1,
            min_price_tick_size=1,
            min_notional=1,
        )

        chain_value = first_match_bet_market.margin_to_chain_format(
            human_readable_value=original_quantity,
            special_denom=fixed_denom,
        )
        price_decimals = fixed_denom.quote
        quantized_value = (original_quantity // Decimal(str(fixed_denom.min_quantity_tick_size))) * Decimal(
            str(fixed_denom.min_quantity_tick_size)
        )
        expected_value = quantized_value * Decimal(f"1e{price_decimals}")
        quantized_chain_format_value = expected_value * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        assert quantized_chain_format_value == chain_value

    def test_convert_margin_to_chain_format_without_fixed_denom(self, first_match_bet_market: BinaryOptionMarket):
        original_quantity = Decimal("123.456789")

        chain_value = first_match_bet_market.margin_to_chain_format(human_readable_value=original_quantity)
        price_decimals = first_match_bet_market.quote_token.decimals
        quantized_value = (
            original_quantity // first_match_bet_market.min_quantity_tick_size
        ) * first_match_bet_market.min_quantity_tick_size
        expected_value = quantized_value * Decimal(f"1e{price_decimals}")
        quantized_chain_format_value = expected_value * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        assert quantized_chain_format_value == chain_value

    def test_calculate_margin_for_buy_with_fixed_denom(self, first_match_bet_market: BinaryOptionMarket):
        original_quantity = Decimal("123.456789")
        original_price = Decimal("0.6789")
        fixed_denom = Denom(
            description="Fixed denom",
            base=2,
            quote=4,
            min_quantity_tick_size=1,
            min_price_tick_size=1,
            min_notional=1,
        )

        chain_value = first_match_bet_market.calculate_margin_in_chain_format(
            human_readable_quantity=original_quantity,
            human_readable_price=original_price,
            is_buy=True,
            special_denom=fixed_denom,
        )

        margin = original_quantity * original_price
        quantized_margin = (margin // Decimal(str(fixed_denom.min_quantity_tick_size))) * Decimal(
            str(fixed_denom.min_quantity_tick_size)
        )
        expected_margin = quantized_margin * Decimal(f"1e{fixed_denom.quote}")
        quantized_chain_format_margin = expected_margin * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        assert quantized_chain_format_margin == chain_value

    def test_calculate_margin_for_buy_without_fixed_denom(self, first_match_bet_market: BinaryOptionMarket):
        original_quantity = Decimal("123.456789")
        original_price = Decimal("0.6789")

        chain_value = first_match_bet_market.calculate_margin_in_chain_format(
            human_readable_quantity=original_quantity,
            human_readable_price=original_price,
            is_buy=True,
        )

        price_decimals = first_match_bet_market.quote_token.decimals
        margin = original_quantity * original_price
        quantized_margin = (margin // Decimal(str(first_match_bet_market.min_quantity_tick_size))) * Decimal(
            str(first_match_bet_market.min_quantity_tick_size)
        )
        expected_margin = quantized_margin * Decimal(f"1e{price_decimals}")
        quantized_chain_format_margin = expected_margin * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        assert quantized_chain_format_margin == chain_value

    def test_calculate_margin_for_sell_without_fixed_denom(self, first_match_bet_market: BinaryOptionMarket):
        original_quantity = Decimal("123.456789")
        original_price = Decimal("0.6789")

        chain_value = first_match_bet_market.calculate_margin_in_chain_format(
            human_readable_quantity=original_quantity,
            human_readable_price=original_price,
            is_buy=False,
        )

        price_decimals = first_match_bet_market.quote_token.decimals
        price = Decimal(1) - original_price
        margin = original_quantity * price
        quantized_margin = (margin // Decimal(str(first_match_bet_market.min_quantity_tick_size))) * Decimal(
            str(first_match_bet_market.min_quantity_tick_size)
        )
        expected_margin = quantized_margin * Decimal(f"1e{price_decimals}")
        quantized_chain_format_margin = expected_margin * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        assert quantized_chain_format_margin == chain_value

    def test_convert_notional_to_chain_format(self, first_match_bet_market: BinaryOptionMarket):
        original_notional = Decimal("123.456789")

        chain_value = first_match_bet_market.notional_to_chain_format(human_readable_value=original_notional)
        notional_decimals = first_match_bet_market.quote_token.decimals
        expected_value = original_notional * Decimal(f"1e{notional_decimals}")
        expected_chain_format_value = expected_value * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        assert expected_chain_format_value == chain_value

    def test_convert_quantity_from_chain_format_with_fixed_denom(self, first_match_bet_market: BinaryOptionMarket):
        original_quantity = Decimal("123.456789")
        fixed_denom = Denom(
            description="Fixed denom",
            base=2,
            quote=4,
            min_quantity_tick_size=1,
            min_price_tick_size=1,
            min_notional=1,
        )

        chain_formatted_quantity = original_quantity * Decimal(f"1e{fixed_denom.base}")

        human_readable_quantity = first_match_bet_market.quantity_from_chain_format(
            chain_value=chain_formatted_quantity, special_denom=fixed_denom
        )

        assert original_quantity == human_readable_quantity

    def test_convert_quantity_from_chain_format_without_fixed_denom(self, first_match_bet_market: BinaryOptionMarket):
        original_quantity = Decimal("123.456789")

        chain_formatted_quantity = original_quantity

        human_readable_quantity = first_match_bet_market.quantity_from_chain_format(
            chain_value=chain_formatted_quantity
        )

        assert original_quantity == human_readable_quantity

    def test_convert_price_from_chain_format_with_fixed_denom(self, first_match_bet_market: BinaryOptionMarket):
        original_price = Decimal("123.456789")
        fixed_denom = Denom(
            description="Fixed denom",
            base=2,
            quote=4,
            min_quantity_tick_size=1,
            min_price_tick_size=1,
            min_notional=1,
        )

        chain_formatted_price = original_price * Decimal(f"1e{fixed_denom.quote}")

        human_readable_price = first_match_bet_market.price_from_chain_format(
            chain_value=chain_formatted_price, special_denom=fixed_denom
        )

        assert original_price == human_readable_price

    def test_convert_price_from_chain_format_without_fixed_denom(self, first_match_bet_market: BinaryOptionMarket):
        original_price = Decimal("123.456789")
        chain_formatted_price = original_price * Decimal(f"1e{first_match_bet_market.quote_token.decimals}")

        human_readable_price = first_match_bet_market.price_from_chain_format(chain_value=chain_formatted_price)

        assert original_price == human_readable_price

    def test_convert_notional_from_chain_format(self, first_match_bet_market: BinaryOptionMarket):
        expected_notional = Decimal("123.456")

        notional_decimals = first_match_bet_market.quote_token.decimals
        chain_format_notional = expected_notional * Decimal(f"1e{notional_decimals}")
        human_readable_notional = first_match_bet_market.notional_from_chain_format(chain_value=chain_format_notional)

        assert expected_notional == human_readable_notional

    def test_convert_quantity_from_extended_chain_format_with_fixed_denom(
        self, first_match_bet_market: BinaryOptionMarket
    ):
        original_quantity = Decimal("123.456789")
        fixed_denom = Denom(
            description="Fixed denom",
            base=2,
            quote=4,
            min_quantity_tick_size=1,
            min_price_tick_size=1,
            min_notional=1,
        )

        chain_formatted_quantity = (
            original_quantity * Decimal(f"1e{fixed_denom.base}") * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        )

        human_readable_quantity = first_match_bet_market.quantity_from_extended_chain_format(
            chain_value=chain_formatted_quantity, special_denom=fixed_denom
        )

        assert original_quantity == human_readable_quantity

    def test_convert_quantity_from_extended_chain_format_without_fixed_denom(
        self, first_match_bet_market: BinaryOptionMarket
    ):
        original_quantity = Decimal("123.456789")

        chain_formatted_quantity = original_quantity * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")

        human_readable_quantity = first_match_bet_market.quantity_from_extended_chain_format(
            chain_value=chain_formatted_quantity
        )

        assert original_quantity == human_readable_quantity

    def test_convert_price_from_extended_chain_format_with_fixed_denom(
        self, first_match_bet_market: BinaryOptionMarket
    ):
        original_price = Decimal("123.456789")
        fixed_denom = Denom(
            description="Fixed denom",
            base=2,
            quote=4,
            min_quantity_tick_size=1,
            min_price_tick_size=1,
            min_notional=1,
        )

        chain_formatted_price = (
            original_price * Decimal(f"1e{fixed_denom.quote}") * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        )

        human_readable_price = first_match_bet_market.price_from_extended_chain_format(
            chain_value=chain_formatted_price, special_denom=fixed_denom
        )

        assert original_price == human_readable_price

    def test_convert_price_from_extended_chain_format_without_fixed_denom(
        self, first_match_bet_market: BinaryOptionMarket
    ):
        original_price = Decimal("123.456789")
        chain_formatted_price = (
            original_price
            * Decimal(f"1e{first_match_bet_market.quote_token.decimals}")
            * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        )

        human_readable_price = first_match_bet_market.price_from_extended_chain_format(
            chain_value=chain_formatted_price
        )

        assert original_price == human_readable_price

    def test_convert_notional_from_extended_chain_format(self, first_match_bet_market: BinaryOptionMarket):
        expected_notional = Decimal("123.456")

        notional_decimals = first_match_bet_market.quote_token.decimals
        chain_format_notional = (
            expected_notional * Decimal(f"1e{notional_decimals}") * Decimal(f"1e{ADDITIONAL_CHAIN_FORMAT_DECIMALS}")
        )
        human_readable_notional = first_match_bet_market.notional_from_extended_chain_format(
            chain_value=chain_format_notional
        )

        assert expected_notional == human_readable_notional
