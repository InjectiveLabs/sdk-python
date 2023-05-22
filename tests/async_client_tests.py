import logging

import pytest
from pyinjective.constant import Network

from pyinjective.async_client import AsyncClient
from pyinjective.proto.exchange.injective_spot_exchange_rpc_pb2 import (
    MarketRequest,
    MarketsRequest,
    MarketResponse,
    MarketsResponse,
)
from tests.rpc_fixtures.markets_fixtures import inj_token_meta, ape_token_meta, usdt_token_meta, inj_usdt_spot_market, ape_usdt_spot_market

@pytest.fixture(scope='module')
def grpc_add_to_server():
    from pyinjective.proto.exchange.injective_spot_exchange_rpc_pb2_grpc import add_InjectiveSpotExchangeRPCServicer_to_server

    return add_InjectiveSpotExchangeRPCServicer_to_server


@pytest.fixture(scope='module')
def grpc_servicer():
    from tests.rpc_fixtures.configurable_servicers import ConfigurableInjectiveSpotExchangeRPCServicer

    return ConfigurableInjectiveSpotExchangeRPCServicer()


@pytest.fixture(scope='module')
def grpc_stub_cls(grpc_channel):
    from pyinjective.proto.exchange.injective_spot_exchange_rpc_pb2_grpc import InjectiveSpotExchangeRPCStub

    return InjectiveSpotExchangeRPCStub

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
            grpc_stub,
            grpc_servicer,
            inj_usdt_spot_market,
            ape_usdt_spot_market
    ):
        grpc_servicer.markets_queue.append(MarketsResponse(
            markets=[inj_usdt_spot_market, ape_usdt_spot_market]
        ))

        client = AsyncClient(
            network=Network.local(),
            insecure=False,
        )

        client.stubSpotExchange = grpc_stub

        await client._initialize_tokens_and_markets()

        assert(3 == len(client.tokens))
        assert(any((inj_usdt_spot_market.base_token_meta.symbol == token.symbol for token in client.tokens)))
        assert (any((inj_usdt_spot_market.quote_token_meta.symbol == token.symbol for token in client.tokens)))
        assert (any((ape_usdt_spot_market.base_token_meta.symbol == token.symbol for token in client.tokens)))

        assert (2 == len(client.markets))
        assert (any((inj_usdt_spot_market.market_id == market.id for market in client.markets)))
        assert (any((ape_usdt_spot_market.market_id == market.id for market in client.markets)))
