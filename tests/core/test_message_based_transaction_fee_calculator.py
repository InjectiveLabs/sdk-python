import math
from decimal import Decimal

import pytest

from pyinjective import Transaction
from pyinjective.async_client import AsyncClient
from pyinjective.composer import Composer
from pyinjective.core.broadcaster import MessageBasedTransactionFeeCalculator
from pyinjective.core.gas_limit_estimator import (
    DefaultGasLimitEstimator,
    ExecGasLimitEstimator,
    GenericExchangeGasLimitEstimator,
    PrivilegedExecuteContractGasLimitEstimator,
)
from pyinjective.core.network import Network
from pyinjective.proto.cosmos.gov.v1beta1 import tx_pb2 as gov_tx_pb2
from pyinjective.proto.cosmwasm.wasm.v1 import tx_pb2 as wasm_tx_pb2
from pyinjective.proto.injective.exchange.v1beta1 import tx_pb2
from tests.model_fixtures.markets_fixtures import btc_usdt_perp_market  # noqa: F401
from tests.model_fixtures.markets_fixtures import first_match_bet_market  # noqa: F401
from tests.model_fixtures.markets_fixtures import inj_token  # noqa: F401
from tests.model_fixtures.markets_fixtures import inj_usdt_spot_market  # noqa: F401
from tests.model_fixtures.markets_fixtures import usdt_perp_token  # noqa: F401
from tests.model_fixtures.markets_fixtures import usdt_token  # noqa: F401


class TestMessageBasedTransactionFeeCalculator:
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

    @pytest.mark.asyncio
    async def test_gas_fee_for_privileged_execute_contract_message(self):
        network = Network.testnet(node="sentry")
        client = AsyncClient(network=network)
        composer = Composer(network=network.string())
        calculator = MessageBasedTransactionFeeCalculator(
            client=client,
            composer=composer,
            gas_price=5_000_000,
        )

        message = tx_pb2.MsgPrivilegedExecuteContract()
        transaction = Transaction()
        transaction.with_messages(message)

        await calculator.configure_gas_fee_for_transaction(transaction=transaction, private_key=None, public_key=None)

        expected_transaction_gas_limit = MessageBasedTransactionFeeCalculator.TRANSACTION_ANTE_GAS_LIMIT
        expected_gas_limit = math.ceil(
            PrivilegedExecuteContractGasLimitEstimator.BASIC_REFERENCE_GAS_LIMIT * 6 + expected_transaction_gas_limit
        )
        assert expected_gas_limit == transaction.fee.gas_limit
        assert str(expected_gas_limit * 5_000_000) == transaction.fee.amount[0].amount

    @pytest.mark.asyncio
    async def test_gas_fee_for_execute_contract_message(self):
        network = Network.testnet(node="sentry")
        client = AsyncClient(network=network)
        composer = Composer(network=network.string())
        calculator = MessageBasedTransactionFeeCalculator(
            client=client,
            composer=composer,
            gas_price=5_000_000,
        )

        message = composer.MsgExecuteContract(
            sender="",
            contract="",
            msg="",
        )
        transaction = Transaction()
        transaction.with_messages(message)

        await calculator.configure_gas_fee_for_transaction(transaction=transaction, private_key=None, public_key=None)

        expected_transaction_gas_limit = MessageBasedTransactionFeeCalculator.TRANSACTION_ANTE_GAS_LIMIT
        expected_gas_limit = math.ceil(Decimal(2.5) * 150_000 + expected_transaction_gas_limit)
        assert expected_gas_limit == transaction.fee.gas_limit
        assert str(expected_gas_limit * 5_000_000) == transaction.fee.amount[0].amount

    @pytest.mark.asyncio
    async def test_gas_fee_for_wasm_message(self):
        network = Network.testnet(node="sentry")
        client = AsyncClient(network=network)
        composer = Composer(network=network.string())
        calculator = MessageBasedTransactionFeeCalculator(
            client=client,
            composer=composer,
            gas_price=5_000_000,
        )

        message = wasm_tx_pb2.MsgInstantiateContract2()
        transaction = Transaction()
        transaction.with_messages(message)

        await calculator.configure_gas_fee_for_transaction(transaction=transaction, private_key=None, public_key=None)

        expected_transaction_gas_limit = MessageBasedTransactionFeeCalculator.TRANSACTION_ANTE_GAS_LIMIT
        expected_gas_limit = math.ceil(Decimal(1.5) * 150_000 + expected_transaction_gas_limit)
        assert expected_gas_limit == transaction.fee.gas_limit
        assert str(expected_gas_limit * 5_000_000) == transaction.fee.amount[0].amount

    @pytest.mark.asyncio
    async def test_gas_fee_for_governance_message(self):
        network = Network.testnet(node="sentry")
        client = AsyncClient(network=network)
        composer = Composer(network=network.string())
        calculator = MessageBasedTransactionFeeCalculator(
            client=client,
            composer=composer,
            gas_price=5_000_000,
        )

        message = gov_tx_pb2.MsgDeposit()
        transaction = Transaction()
        transaction.with_messages(message)

        await calculator.configure_gas_fee_for_transaction(transaction=transaction, private_key=None, public_key=None)

        expected_transaction_gas_limit = MessageBasedTransactionFeeCalculator.TRANSACTION_ANTE_GAS_LIMIT
        expected_gas_limit = math.ceil(Decimal(15) * 150_000 + expected_transaction_gas_limit)
        assert expected_gas_limit == transaction.fee.gas_limit
        assert str(expected_gas_limit * 5_000_000) == transaction.fee.amount[0].amount

    @pytest.mark.asyncio
    async def test_gas_fee_for_exchange_message(self, basic_composer):
        network = Network.testnet(node="sentry")
        client = AsyncClient(network=network)
        calculator = MessageBasedTransactionFeeCalculator(
            client=client,
            composer=basic_composer,
            gas_price=5_000_000,
        )

        market_id = list(basic_composer.spot_markets.keys())[0]

        message = basic_composer.msg_create_spot_limit_order(
            sender="sender",
            market_id=market_id,
            subaccount_id="subaccount_id",
            fee_recipient="fee_recipient",
            price=Decimal("7.523"),
            quantity=Decimal("0.01"),
            order_type="BUY",
        )
        transaction = Transaction()
        transaction.with_messages(message)

        await calculator.configure_gas_fee_for_transaction(transaction=transaction, private_key=None, public_key=None)

        expected_transaction_gas_limit = MessageBasedTransactionFeeCalculator.TRANSACTION_ANTE_GAS_LIMIT
        expected_gas_limit = math.ceil(Decimal(1) * 120_000 + expected_transaction_gas_limit)
        assert expected_gas_limit == transaction.fee.gas_limit
        assert str(expected_gas_limit * 5_000_000) == transaction.fee.amount[0].amount

    @pytest.mark.asyncio
    async def test_gas_fee_for_msg_exec_message(self, basic_composer):
        network = Network.testnet(node="sentry")
        client = AsyncClient(network=network)
        calculator = MessageBasedTransactionFeeCalculator(
            client=client,
            composer=basic_composer,
            gas_price=5_000_000,
        )

        market_id = list(basic_composer.spot_markets.keys())[0]

        inner_message = basic_composer.msg_create_spot_limit_order(
            sender="sender",
            market_id=market_id,
            subaccount_id="subaccount_id",
            fee_recipient="fee_recipient",
            price=Decimal("7.523"),
            quantity=Decimal("0.01"),
            order_type="BUY",
        )
        message = basic_composer.MsgExec(grantee="grantee", msgs=[inner_message])
        transaction = Transaction()
        transaction.with_messages(message)

        await calculator.configure_gas_fee_for_transaction(transaction=transaction, private_key=None, public_key=None)

        expected_transaction_gas_limit = MessageBasedTransactionFeeCalculator.TRANSACTION_ANTE_GAS_LIMIT
        expected_inner_message_gas_limit = GenericExchangeGasLimitEstimator.BASIC_REFERENCE_GAS_LIMIT
        expected_exec_message_gas_limit = ExecGasLimitEstimator.DEFAULT_GAS_LIMIT
        expected_gas_limit = math.ceil(
            expected_exec_message_gas_limit + expected_inner_message_gas_limit + expected_transaction_gas_limit
        )
        assert expected_gas_limit == transaction.fee.gas_limit
        assert str(expected_gas_limit * 5_000_000) == transaction.fee.amount[0].amount

    @pytest.mark.asyncio
    async def test_gas_fee_for_two_messages_in_one_transaction(self, basic_composer):
        network = Network.testnet(node="sentry")
        client = AsyncClient(network=network)
        calculator = MessageBasedTransactionFeeCalculator(
            client=client,
            composer=basic_composer,
            gas_price=5_000_000,
        )

        market_id = list(basic_composer.spot_markets.keys())[0]

        inner_message = basic_composer.msg_create_spot_limit_order(
            sender="sender",
            market_id=market_id,
            subaccount_id="subaccount_id",
            fee_recipient="fee_recipient",
            price=Decimal("7.523"),
            quantity=Decimal("0.01"),
            order_type="BUY",
        )
        message = basic_composer.MsgExec(grantee="grantee", msgs=[inner_message])

        send_message = basic_composer.MsgSend(from_address="address", to_address="to_address", amount=1, denom="INJ")

        transaction = Transaction()
        transaction.with_messages(message, send_message)

        await calculator.configure_gas_fee_for_transaction(transaction=transaction, private_key=None, public_key=None)

        expected_transaction_gas_limit = MessageBasedTransactionFeeCalculator.TRANSACTION_ANTE_GAS_LIMIT
        expected_inner_message_gas_limit = GenericExchangeGasLimitEstimator.BASIC_REFERENCE_GAS_LIMIT
        expected_exec_message_gas_limit = ExecGasLimitEstimator.DEFAULT_GAS_LIMIT
        expected_send_message_gas_limit = DefaultGasLimitEstimator.DEFAULT_GAS_LIMIT
        expected_gas_limit = math.ceil(
            expected_exec_message_gas_limit
            + expected_inner_message_gas_limit
            + expected_send_message_gas_limit
            + expected_transaction_gas_limit
        )
        assert expected_gas_limit == transaction.fee.gas_limit
        assert str(expected_gas_limit * 5_000_000) == transaction.fee.amount[0].amount
