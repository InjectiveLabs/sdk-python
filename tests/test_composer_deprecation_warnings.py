import warnings

import pytest

from pyinjective.composer import Composer as ComposerV1
from pyinjective.core.network import Network
from tests.model_fixtures.markets_fixtures import (  # noqa: F401
    btc_usdt_perp_market,
    first_match_bet_market,
    inj_token,
    inj_usdt_spot_market,
    usdt_perp_token,
    usdt_token,
)


class TestComposerDeprecationWarnings:
    @pytest.fixture
    def basic_v1_composer(self, inj_usdt_spot_market, btc_usdt_perp_market, first_match_bet_market):
        composer = ComposerV1(
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

    def test_composer_v1_msg_bid_deprecation_warning(self):
        composer = ComposerV1(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgBid(sender="sender", bid_amount=1.1, round=2)

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_bid instead"

    def test_composer_v1_msg_grant_generic_deprecation_warning(self):
        composer = ComposerV1(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgGrantGeneric(granter="granter", grantee="grantee", msg_type="type", expire_in=1000)

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_grant_generic instead"

    def test_composer_v1_msg_exec_deprecation_warning(self):
        composer = ComposerV1(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgExec(grantee="grantee", msgs=[])

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_exec instead"

    def test_composer_v1_msg_revoke_deprecation_warning(self):
        composer = ComposerV1(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgRevoke(granter="granter", grantee="grantee", msg_type="type")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_revoke instead"

    def test_composer_v1_msg_send_deprecation_warning(self, basic_v1_composer, inj_usdt_spot_market):
        composer = basic_v1_composer
        denom = list(composer.tokens.keys())[0]

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgSend(from_address="from_address", to_address="to_address", amount=1, denom=denom)

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_send instead"

    def test_composer_v1_msg_create_insurance_fund_warning(self, basic_v1_composer, usdt_perp_token):
        composer = basic_v1_composer
        denom = usdt_perp_token.symbol

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgCreateInsuranceFund(
                sender="sender",
                ticker="ticker",
                quote_denom=denom,
                oracle_base="oracle_base",
                oracle_quote="oracle_quote",
                oracle_type=1,
                expiry=1,
                initial_deposit=1000,
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_create_insurance_fund instead"
        )

    def test_composer_v1_msg_underwrite_deprecation_warning(self, basic_v1_composer, inj_usdt_spot_market):
        composer = basic_v1_composer
        denom = list(composer.tokens.keys())[0]

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgUnderwrite(sender="sender", market_id="market_id", quote_denom=denom, amount=1000)

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_underwrite instead"

    def test_composer_v1_msg_request_redemption_deprecation_warning(self):
        composer = ComposerV1(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgRequestRedemption(
                sender="sender", market_id="market_id", share_denom="share_denom", amount=1000
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_request_redemption instead"

    def test_composer_v1_msg_relay_provider_prices_deprecation_warning(self):
        composer = ComposerV1(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgRelayProviderPrices(sender="sender", provider="provider", symbols=["symbol"], prices=[1000])

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_relay_provider_prices instead"
        )

    def test_composer_v1_msg_relay_price_feed_price_deprecation_warning(self):
        composer = ComposerV1(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgRelayPriceFeedPrice(sender="sender", base=["base"], quote=["quote"], price=["1000"])

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_relay_price_feed_price instead"
        )

    def test_composer_v1_msg_send_to_eth_deprecation_warning(self, basic_v1_composer, usdt_token):
        composer = basic_v1_composer
        denom = usdt_token.symbol

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgSendToEth(denom=denom, sender="sender", eth_dest="eth_dest", amount=1000, bridge_fee=1000)

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_send_to_eth instead"

    def test_composer_v1_msg_delegate_deprecation_warning(self):
        composer = ComposerV1(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgDelegate(
                delegator_address="delegator_address", validator_address="validator_address", amount=1000
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_delegate instead"

    def test_composer_v1_msg_instantiate_contract_deprecation_warning(self):
        composer = ComposerV1(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgInstantiateContract(
                sender="sender", admin="admin", code_id=1, label="label", message=b"message"
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_instantiate_contract instead"

    def test_composer_v1_msg_execute_contract_deprecation_warning(self):
        composer = ComposerV1(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgExecuteContract(sender="sender", contract="contract", msg="msg")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_execute_contract instead"

    def test_composer_v1_msg_grant_typed_deprecation_warning(self):
        composer = ComposerV1(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgGrantTyped(
                granter="granter",
                grantee="grantee",
                msg_type="CreateSpotLimitOrderAuthz",
                expire_in=1000,
                subaccount_id="subaccount_id",
                market_ids=["market_id"],
                spot_markets=["spot_market_id"],
                derivative_markets=["derivative_market_id"],
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_grant_typed instead"

    def test_composer_v1_msg_vote_deprecation_warning(self):
        composer = ComposerV1(network=Network.devnet().string())

        with warnings.catch_warnings(record=True) as all_warnings:
            composer.MsgVote(proposal_id=100, voter="voter", option=1)

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use msg_vote instead"

    def test_composer_v1_constructor_deprecation_warning(self):
        with warnings.catch_warnings(record=True) as all_warnings:
            composer = ComposerV1(network=Network.devnet().string())

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "Composer from pyinjective.composer is deprecated. Please use Composer from pyinjective.composer_v2 instead."
