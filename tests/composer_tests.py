import logging

import pytest

from pyinjective.composer import Composer
from pyinjective.constant import Denom, Network


class TestComposer:

    @pytest.fixture
    def inj_usdt_market_id(self):
        return "0xa508cb32923323679f29a032c70342c147c17d0145625922b0ef22e955c844c0"

    def test_spot_order_creation_logs_market_data_loaded_info(self, caplog, inj_usdt_market_id):
        caplog.set_level(logging.INFO)

        composer = Composer(network=Network.devnet().string())

        composer.SpotOrder(
            market_id=inj_usdt_market_id,
            subaccount_id="",
            fee_recipient="",
            price=1.0,
            quantity=1.0,
        )

        expected_log_message_prefix = "Loaded market metadata for: 'Devnet Spot INJ/USDT'"
        expected_log_record = ("pyinjective.composer.Composer", logging.INFO, expected_log_message_prefix)
        assert(expected_log_record in caplog.record_tuples)

    def test_derivative_order_creation_logs_market_data_loaded_info(self, caplog, inj_usdt_market_id):
        caplog.set_level(logging.INFO)

        composer = Composer(network=Network.devnet().string())

        composer.DerivativeOrder(
            market_id=inj_usdt_market_id,
            subaccount_id="",
            fee_recipient="",
            price=1.0,
            quantity=1.0,
            leverage=1.0,
        )

        expected_log_message_prefix = "Loaded market metadata for: 'Devnet Spot INJ/USDT'"
        expected_log_record = ("pyinjective.composer.Composer", logging.INFO, expected_log_message_prefix)
        assert(expected_log_record in caplog.record_tuples)

    def test_binary_order_creation_logs_market_data_loaded_info(self, caplog, inj_usdt_market_id):
        caplog.set_level(logging.INFO)

        composer = Composer(network=Network.devnet().string())

        composer.BinaryOptionsOrder(
            market_id=inj_usdt_market_id,
            subaccount_id="",
            fee_recipient="",
            price=1.0,
            quantity=1.0,
        )

        expected_log_message_prefix = "Loaded market metadata for: 'Devnet Spot INJ/USDT'"
        expected_log_record = ("pyinjective.composer.Composer", logging.INFO, expected_log_message_prefix)
        assert(expected_log_record in caplog.record_tuples)

    def test_msg_send_logs_market_data_loaded_info(self, caplog):
        caplog.set_level(logging.INFO)

        composer = Composer(network=Network.devnet().string())

        composer.MsgSend(
            from_address="",
            to_address="",
            amount=1.0,
            denom="INJ",
        )

        expected_log_message_prefix = f"Loaded send symbol INJ (inj) with decimals = 18"
        expected_log_record = ("pyinjective.composer.Composer", logging.INFO, expected_log_message_prefix)
        assert(expected_log_record in caplog.record_tuples)

    def test_msg_deposit_logs_market_data_loaded_info(self, caplog):
        caplog.set_level(logging.INFO)

        composer = Composer(network=Network.devnet().string())

        composer.MsgDeposit(
            sender="",
            subaccount_id="",
            amount=1.0,
            denom="INJ",
        )

        expected_log_message_prefix = f"Loaded deposit symbol INJ (inj) with decimals = 18"
        expected_log_record = ("pyinjective.composer.Composer", logging.INFO, expected_log_message_prefix)
        assert(expected_log_record in caplog.record_tuples)

    def test_msg_withdraw_logs_market_data_loaded_info(self, caplog):
        caplog.set_level(logging.INFO)

        composer = Composer(network=Network.devnet().string())

        composer.MsgWithdraw(
            sender="",
            subaccount_id="",
            amount=1.0,
            denom="INJ",
        )

        expected_log_message_prefix = f"Loaded withdrawal symbol INJ (inj) with decimals = 18"
        expected_log_record = ("pyinjective.composer.Composer", logging.INFO, expected_log_message_prefix)
        assert(expected_log_record in caplog.record_tuples)

    def test_msg_external_transfer_logs_market_data_loaded_info(self, caplog):
        caplog.set_level(logging.INFO)

        composer = Composer(network=Network.devnet().string())

        composer.MsgExternalTransfer(
            sender="",
            source_subaccount_id="",
            destination_subaccount_id="",
            amount=1.0,
            denom="INJ",
        )

        expected_log_message_prefix = f"Loaded send symbol INJ (inj) with decimals = 18"
        expected_log_record = ("pyinjective.composer.Composer", logging.INFO, expected_log_message_prefix)
        assert(expected_log_record in caplog.record_tuples)

    def test_msg_send_to_eth_logs_market_data_loaded_info(self, caplog):
        caplog.set_level(logging.INFO)

        composer = Composer(network=Network.devnet().string())

        composer.MsgSendToEth(
            denom="INJ",
            sender="",
            eth_dest="",
            amount=1.0,
            bridge_fee=1.0,
        )

        expected_log_message_prefix = f"Loaded withdrawal symbol INJ (inj) with decimals = 18"
        expected_log_record = ("pyinjective.composer.Composer", logging.INFO, expected_log_message_prefix)
        assert(expected_log_record in caplog.record_tuples)

    def test_msg_create_insurance_fund_logs_market_data_loaded_info(self, caplog):
        caplog.set_level(logging.INFO)

        composer = Composer(network=Network.devnet().string())

        composer.MsgCreateInsuranceFund(
            sender="",
            ticker="",
            quote_denom="INJ",
            oracle_base="",
            oracle_quote="",
            oracle_type=1,
            expiry=1,
            initial_deposit=1,
        )

        expected_log_message_prefix = f"Loaded send symbol INJ (inj) with decimals = 18"
        expected_log_record = ("pyinjective.composer.Composer", logging.INFO, expected_log_message_prefix)
        assert(expected_log_record in caplog.record_tuples)

    def test_msg_underwrite_logs_market_data_loaded_info(self, caplog, inj_usdt_market_id):
        caplog.set_level(logging.INFO)

        composer = Composer(network=Network.devnet().string())

        composer.MsgUnderwrite(
            sender="",
            market_id=inj_usdt_market_id,
            quote_denom="INJ",
            amount=1,
        )

        expected_log_message_prefix = f"Loaded send symbol INJ (inj) with decimals = 18"
        expected_log_record = ("pyinjective.composer.Composer", logging.INFO, expected_log_message_prefix)
        assert(expected_log_record in caplog.record_tuples)
