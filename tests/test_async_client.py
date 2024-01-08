import logging

import pytest

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network
from pyinjective.proto.cosmos.bank.v1beta1 import query_pb2 as bank_query_pb
from pyinjective.proto.cosmos.base.query.v1beta1 import pagination_pb2 as pagination_pb
from pyinjective.proto.exchange import injective_derivative_exchange_rpc_pb2, injective_spot_exchange_rpc_pb2
from tests.client.chain.grpc.configurable_bank_query_servicer import ConfigurableBankQueryServicer
from tests.client.indexer.configurable_derivative_query_servicer import ConfigurableDerivativeQueryServicer
from tests.client.indexer.configurable_spot_query_servicer import ConfigurableSpotQueryServicer
from tests.rpc_fixtures.markets_fixtures import (  # noqa: F401
    ape_token_meta,
    ape_usdt_spot_market_meta,
    btc_usdt_perp_market_meta,
    first_match_bet_market_meta,
    inj_token_meta,
    inj_usdt_spot_market_meta,
    smart_denom_metadata,
    usdt_perp_token_meta,
    usdt_token_meta,
    usdt_token_meta_second_denom,
)


@pytest.fixture
def bank_servicer():
    return ConfigurableBankQueryServicer()


@pytest.fixture
def spot_servicer():
    return ConfigurableSpotQueryServicer()


@pytest.fixture
def derivative_servicer():
    return ConfigurableDerivativeQueryServicer()


class TestAsyncClient:
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
        assert found_log is not None
        assert found_log[0] == "pyinjective.async_client.AsyncClient"
        assert found_log[1] == logging.DEBUG

    @pytest.mark.asyncio
    async def test_get_account_logs_exception(self, caplog):
        client = AsyncClient(
            network=Network.local(),
            insecure=False,
        )

        with caplog.at_level(logging.DEBUG):
            await client.fetch_account(address="")

        expected_log_message_prefix = "error while fetching sequence and number "
        found_log = next(
            (record for record in caplog.record_tuples if record[2].startswith(expected_log_message_prefix)),
            None,
        )
        assert found_log is not None
        assert found_log[0] == "pyinjective.async_client.AsyncClient"
        assert found_log[1] == logging.DEBUG

    @pytest.mark.asyncio
    async def test_initialize_tokens_and_markets(
        self,
        spot_servicer,
        derivative_servicer,
        inj_usdt_spot_market_meta,
        ape_usdt_spot_market_meta,
        btc_usdt_perp_market_meta,
        first_match_bet_market_meta,
    ):
        spot_servicer.markets_responses.append(
            injective_spot_exchange_rpc_pb2.MarketsResponse(
                markets=[inj_usdt_spot_market_meta, ape_usdt_spot_market_meta]
            )
        )
        derivative_servicer.markets_responses.append(
            injective_derivative_exchange_rpc_pb2.MarketsResponse(markets=[btc_usdt_perp_market_meta])
        )
        derivative_servicer.binary_options_markets_responses.append(
            injective_derivative_exchange_rpc_pb2.BinaryOptionsMarketsResponse(markets=[first_match_bet_market_meta])
        )

        client = AsyncClient(
            network=Network.local(),
            insecure=False,
        )

        client.exchange_spot_api._stub = spot_servicer
        client.exchange_derivative_api._stub = derivative_servicer

        await client._initialize_tokens_and_markets()

        all_tokens = await client.all_tokens()
        assert 5 == len(all_tokens)
        inj_symbol, usdt_symbol = inj_usdt_spot_market_meta.ticker.split("/")
        ape_symbol, _ = ape_usdt_spot_market_meta.ticker.split("/")
        alternative_usdt_name = ape_usdt_spot_market_meta.quote_token_meta.name
        usdt_perp_symbol = btc_usdt_perp_market_meta.quote_token_meta.symbol
        assert inj_symbol in all_tokens
        assert usdt_symbol in all_tokens
        assert alternative_usdt_name in all_tokens
        assert ape_symbol in all_tokens
        assert usdt_perp_symbol in all_tokens

        all_spot_markets = await client.all_spot_markets()
        assert 2 == len(all_spot_markets)
        assert any((inj_usdt_spot_market_meta.market_id == market.id for market in all_spot_markets.values()))
        assert any((ape_usdt_spot_market_meta.market_id == market.id for market in all_spot_markets.values()))

        all_derivative_markets = await client.all_derivative_markets()
        assert 1 == len(all_derivative_markets)
        assert any((btc_usdt_perp_market_meta.market_id == market.id for market in all_derivative_markets.values()))

        all_binary_option_markets = await client.all_binary_option_markets()
        assert 1 == len(all_binary_option_markets)
        assert any(
            (first_match_bet_market_meta.market_id == market.id for market in all_binary_option_markets.values())
        )

    @pytest.mark.asyncio
    async def test_initialize_tokens_from_chain_denoms(
        self,
        bank_servicer,
        spot_servicer,
        derivative_servicer,
        smart_denom_metadata,
    ):
        pagination = pagination_pb.PageResponse(
            total=1,
        )

        bank_servicer.denoms_metadata_responses.append(
            bank_query_pb.QueryDenomsMetadataResponse(
                metadatas=[smart_denom_metadata],
                pagination=pagination,
            )
        )

        spot_servicer.markets_responses.append(injective_spot_exchange_rpc_pb2.MarketsResponse(markets=[]))
        derivative_servicer.markets_responses.append(injective_derivative_exchange_rpc_pb2.MarketsResponse(markets=[]))
        derivative_servicer.binary_options_markets_responses.append(
            injective_derivative_exchange_rpc_pb2.BinaryOptionsMarketsResponse(markets=[])
        )

        client = AsyncClient(
            network=Network.local(),
            insecure=False,
        )

        client.bank_api._stub = bank_servicer
        client.exchange_spot_api._stub = spot_servicer
        client.exchange_derivative_api._stub = derivative_servicer

        await client._initialize_tokens_and_markets()
        await client.initialize_tokens_from_chain_denoms()

        all_tokens = await client.all_tokens()
        assert 1 == len(all_tokens)
        assert smart_denom_metadata.symbol in all_tokens
