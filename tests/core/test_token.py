from decimal import Decimal

from tests.model_fixtures.markets_v2_fixtures import inj_token  # noqa: F401


class TestToken:
    def test_chain_formatted_value(self, inj_token):
        value = Decimal("1.3456")

        chain_formatted_value = inj_token.chain_formatted_value(human_readable_value=value)
        expected_value = value * Decimal(f"1e{inj_token.decimals}")

        assert chain_formatted_value == expected_value

    def test_human_readable_value(self, inj_token):
        value = Decimal("1345600000000000000")

        human_readable_value = inj_token.human_readable_value(chain_formatted_value=value)
        expected_value = value / Decimal(f"1e{inj_token.decimals}")

        assert human_readable_value == expected_value
