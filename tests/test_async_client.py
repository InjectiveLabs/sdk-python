import logging

import pytest
from pyinjective.constant import Network

from pyinjective.async_client import AsyncClient
from pyinjective.proto.exchange import (
    injective_spot_exchange_rpc_pb2,
    injective_derivative_exchange_rpc_pb2,
)
from tests.rpc_fixtures.markets_fixtures import (
    inj_token_meta,
    ape_token_meta,
    usdt_token_meta,
    usdt_perp_token_meta,
    inj_usdt_spot_market,
    ape_usdt_spot_market,
    btc_usdt_perp_market,
    first_match_bet_market,
)
from tests.rpc_fixtures.configurable_servicers import ConfigurableInjectiveDerivativeExchangeRPCServicer, \
    ConfigurableInjectiveSpotExchangeRPCServicer


@pytest.fixture
def spot_servicer():
    return ConfigurableInjectiveSpotExchangeRPCServicer()


@pytest.fixture
def derivative_servicer():
    return ConfigurableInjectiveDerivativeExchangeRPCServicer()


class TestAsyncClient:

    def test_instance_creation_logs_session_cookie_load_info(self, caplog):
        caplog.set_level(logging.INFO)

        AsyncClient(
            network=Network.local(),
            insecure=False,
        )

        expected_log_message_prefix = "chain session cookie loaded from disk: "
        found_log = next(
            (record for record in caplog.record_tuples if record[2].startswith(expected_log_message_prefix)),
            None,
        )
        assert(found_log is not None)
        assert(found_log[0] == "pyinjective.async_client.AsyncClient")
        assert(found_log[1] == logging.INFO)


    @pytest.mark.asyncio
    async def test_sync_timeout_height_logs_exception(self, caplog):
        client = AsyncClient(
            network=Network.local(),
            insecure=False,
        )

        with caplog.at_level(logging.DEBUG):
            await client.sync_timeout_height()

        expected_log_message_prefix = "error while fetching latest block, setting timeout height to 0: "
        found_log = next(
            (record for record in caplog.record_tuples if record[2].startswith(expected_log_message_prefix)),
            None,
        )
        assert (found_log is not None)
        assert (found_log[0] == "pyinjective.async_client.AsyncClient")
        assert (found_log[1] == logging.DEBUG)

    def test_set_cookie_logs_chain_session_cookie_saved(self, caplog):
        caplog.set_level(logging.INFO)

        client = AsyncClient(
            network=Network.local(),
            insecure=False,
        )

        client.set_cookie(metadata=[("set-cookie", "test-value")], type="chain")

        expected_log_message_prefix = "chain session cookie saved to disk"
        found_log = next(
            (record for record in caplog.record_tuples if record[2].startswith(expected_log_message_prefix)),
            None,
        )
        assert (found_log is not None)
        assert (found_log[0] == "pyinjective.async_client.AsyncClient")
        assert (found_log[1] == logging.INFO)

    @pytest.mark.asyncio
    async def test_get_account_logs_exception(self, caplog):
        client = AsyncClient(
            network=Network.local(),
            insecure=False,
        )

        with caplog.at_level(logging.DEBUG):
            await client.get_account(address="")

        expected_log_message_prefix = "error while fetching sequence and number "
        found_log = next(
            (record for record in caplog.record_tuples if record[2].startswith(expected_log_message_prefix)),
            None,
        )
        assert (found_log is not None)
        assert (found_log[0] == "pyinjective.async_client.AsyncClient")
        assert (found_log[1] == logging.DEBUG)

    @pytest.mark.asyncio
    async def test_initialize_tokens_and_markets(
            self,
            spot_servicer,
            derivative_servicer,
            inj_usdt_spot_market,
            ape_usdt_spot_market,
            btc_usdt_perp_market,
            first_match_bet_market,
    ):
        spot_servicer.markets_queue.append(injective_spot_exchange_rpc_pb2.MarketsResponse(
            markets=[inj_usdt_spot_market, ape_usdt_spot_market]
        ))
        derivative_servicer.markets_queue.append(injective_derivative_exchange_rpc_pb2.MarketsResponse(
            markets=[btc_usdt_perp_market]
        ))
        derivative_servicer.binary_option_markets_queue.append(
            injective_derivative_exchange_rpc_pb2.BinaryOptionsMarketsResponse(
                markets=[first_match_bet_market]
        ))

        client = AsyncClient(
            network=Network.local(),
            insecure=False,
        )

        client.stubSpotExchange = spot_servicer
        client.stubDerivativeExchange = derivative_servicer

        await client._initialize_tokens_and_markets()

        all_tokens = await client.all_tokens()
        assert(4 == len(all_tokens))
        inj_symbol, usdt_symbol = inj_usdt_spot_market.ticker.split("/")
        ape_symbol, _ = ape_usdt_spot_market.ticker.split("/")
        usdt_perp_symbol = btc_usdt_perp_market.quote_token_meta.symbol
        assert(any((inj_symbol == token.symbol for _, token in all_tokens.items())))
        assert (any((usdt_symbol == token.symbol for _, token in all_tokens.items())))
        assert (any((ape_symbol == token.symbol for _, token in all_tokens.items())))
        assert (any((usdt_perp_symbol == token.symbol for _, token in all_tokens.items())))

        all_spot_markets = await client.all_spot_markets()
        assert (2 == len(all_spot_markets))
        assert (any((inj_usdt_spot_market.market_id == market.id for market in all_spot_markets.values())))
        assert (any((ape_usdt_spot_market.market_id == market.id for market in all_spot_markets.values())))

        all_derivative_markets = await client.all_derivative_markets()
        assert (1 == len(all_derivative_markets))
        assert (any((btc_usdt_perp_market.market_id == market.id for market in all_derivative_markets.values())))

        all_binary_option_markets = await client.all_binary_option_markets()
        assert (1 == len(all_binary_option_markets))
        assert (any((first_match_bet_market.market_id == market.id for market in all_binary_option_markets.values())))
