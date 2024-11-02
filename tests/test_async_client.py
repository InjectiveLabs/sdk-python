import logging

import pytest

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network
from pyinjective.proto.cosmos.bank.v1beta1 import query_pb2 as bank_query_pb
from pyinjective.proto.cosmos.base.query.v1beta1 import pagination_pb2 as pagination_pb
from pyinjective.proto.injective.exchange.v2 import query_pb2 as exchange_query_pb
from tests.client.chain.grpc.configurable_bank_query_servicer import ConfigurableBankQueryServicer
from tests.client.chain.grpc.configurable_exchange_v2_query_servicer import ConfigurableExchangeV2QueryServicer
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
def exchange_servicer():
    return ConfigurableExchangeV2QueryServicer()


class TestAsyncClient:
    @pytest.mark.asyncio
    async def test_sync_timeout_height_logs_exception(self, caplog):
        client = AsyncClient(
            network=Network.local(),
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
        exchange_servicer,
        inj_usdt_spot_market_meta,
        ape_usdt_spot_market_meta,
        btc_usdt_perp_market_meta,
        first_match_bet_market_meta,
        aioresponses,
    ):
        test_network = Network.local()
        tokens_list = [
            {
                "address": "0x44C21afAaF20c270EBbF5914Cfc3b5022173FEB7",
                "isNative": False,
                "tokenVerification": "verified",
                "decimals": 6,
                "symbol": "APE",
                "name": "Ape",
                "logo": "https://imagedelivery.net/lPzngbR8EltRfBOi_WYaXw/6f015260-c589-499f-b692-a57964af9900/public",
                "coinGeckoId": "",
                "denom": "peggy0x44C21afAaF20c270EBbF5914Cfc3b5022173FEB7",
                "tokenType": "erc20",
                "externalLogo": "unknown.png",
            },
            {
                "address": "0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
                "isNative": False,
                "tokenVerification": "verified",
                "decimals": 6,
                "symbol": "USDT",
                "name": "Tether",
                "logo": "https://imagedelivery.net/lPzngbR8EltRfBOi_WYaXw/a0bd252b-1005-47ef-d209-7c1c4a3cbf00/public",
                "coinGeckoId": "tether",
                "denom": "peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
                "tokenType": "erc20",
                "externalLogo": "usdt.png",
            },
            {
                "decimals": 6,
                "symbol": "USDT",
                "name": "Other USDT",
                "logo": "https://imagedelivery.net/lPzngbR8EltRfBOi_WYaXw/6f015260-c589-499f-b692-a57964af9900/public",
                "coinGeckoId": "",
                "address": "factory/inj10vkkttgxdeqcgeppu20x9qtyvuaxxev8qh0awq/usdt",
                "denom": "factory/inj10vkkttgxdeqcgeppu20x9qtyvuaxxev8qh0awq/usdt",
                "externalLogo": "unknown.png",
                "tokenType": "tokenFactory",
                "tokenVerification": "internal",
            },
            {
                "address": "inj",
                "isNative": True,
                "tokenVerification": "verified",
                "decimals": 18,
                "symbol": "INJ",
                "name": "Injective",
                "logo": "https://imagedelivery.net/lPzngbR8EltRfBOi_WYaXw/18984c0b-3e61-431d-241d-dfbb60b57600/public",
                "coinGeckoId": "injective-protocol",
                "denom": "inj",
                "tokenType": "native",
                "externalLogo": "injective-v3.png",
            },
            {
                "decimals": 6,
                "symbol": "USDTPERP",
                "name": "USDT PERP",
                "logo": "https://static.alchemyapi.io/images/assets/825.png",
                "coinGeckoId": "",
                "address": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
                "denom": "peggy0xdAC17F958D2ee523a2206206994597C13D831ec7",
                "externalLogo": "unknown.png",
                "tokenType": "tokenFactory",
                "tokenVerification": "internal",
            },
        ]
        aioresponses.get(test_network.official_tokens_list_url, payload=tokens_list)

        exchange_servicer.spot_markets_responses.append(
            exchange_query_pb.QuerySpotMarketsResponse(markets=[inj_usdt_spot_market_meta, ape_usdt_spot_market_meta])
        )
        exchange_servicer.derivative_markets_responses.append(
            exchange_query_pb.QueryDerivativeMarketsResponse(markets=[btc_usdt_perp_market_meta])
        )
        exchange_servicer.binary_options_markets_responses.append(
            exchange_query_pb.QueryBinaryMarketsResponse(markets=[first_match_bet_market_meta])
        )

        client = AsyncClient(
            network=test_network,
        )

        client.chain_exchange_v2_api._stub = exchange_servicer

        await client._initialize_tokens_and_markets()

        all_tokens = await client.all_tokens()
        assert 5 == len(all_tokens)
        inj_symbol, usdt_symbol = inj_usdt_spot_market_meta.ticker.split("/")
        ape_symbol, _ = ape_usdt_spot_market_meta.ticker.split("/")
        alternative_usdt_name = "Other USDT"
        usdt_perp_symbol = "USDTPERP"
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
        assert any(
            (btc_usdt_perp_market_meta.market.market_id == market.id for market in all_derivative_markets.values())
        )

        all_binary_option_markets = await client.all_binary_option_markets()
        assert 1 == len(all_binary_option_markets)
        assert any(
            (first_match_bet_market_meta.market_id == market.id for market in all_binary_option_markets.values())
        )

    @pytest.mark.asyncio
    async def test_tokens_and_markets_initialization_read_tokens_from_official_list(
        self,
        exchange_servicer,
        inj_usdt_spot_market_meta,
        ape_usdt_spot_market_meta,
        btc_usdt_perp_market_meta,
        first_match_bet_market_meta,
        aioresponses,
    ):
        test_network = Network.local()

        tokens_list = [
            {
                "address": "ibc/2CBC2EA121AE42563B08028466F37B600F2D7D4282342DE938283CC3FB2BC00E",
                "isNative": True,
                "tokenVerification": "verified",
                "name": "USD Coin",
                "decimals": 6,
                "symbol": "USDC",
                "logo": "https://imagedelivery.net/DYKOWp0iCc0sIkF-2e4dNw/a8bfa5f1-1dab-4be9-a68c-e15f0bd11100/public",
                "coinGeckoId": "usd-coin",
                "baseDenom": "uusdc",
                "channelId": "channel-148",
                "source": "cosmos",
                "path": "transfer/channel-148",
                "hash": "2CBC2EA121AE42563B08028466F37B600F2D7D4282342DE938283CC3FB2BC00E",
                "denom": "ibc/2CBC2EA121AE42563B08028466F37B600F2D7D4282342DE938283CC3FB2BC00E",
                "tokenType": "ibc",
                "externalLogo": "usdc.png",
            },
            {
                "address": "0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270",
                "isNative": False,
                "decimals": 18,
                "symbol": "WMATIC",
                "logo": "https://imagedelivery.net/DYKOWp0iCc0sIkF-2e4dNw/0d061e1e-a746-4b19-1399-8187b8bb1700/public",
                "name": "Wrapped Matic",
                "coinGeckoId": "wmatic",
                "denom": "0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270",
                "tokenType": "evm",
                "tokenVerification": "verified",
                "externalLogo": "polygon.png",
            },
        ]
        aioresponses.get(test_network.official_tokens_list_url, payload=tokens_list)

        exchange_servicer.spot_markets_responses.append(exchange_query_pb.QuerySpotMarketsResponse(markets=[]))
        exchange_servicer.derivative_markets_responses.append(
            exchange_query_pb.QueryDerivativeMarketsResponse(markets=[])
        )
        exchange_servicer.binary_options_markets_responses.append(
            exchange_query_pb.QueryBinaryMarketsResponse(markets=[])
        )

        client = AsyncClient(
            network=test_network,
        )

        client.chain_exchange_v2_api._stub = exchange_servicer

        await client._initialize_tokens_and_markets()

        all_tokens = await client.all_tokens()
        for token_info in tokens_list:
            assert token_info["symbol"] in all_tokens

    @pytest.mark.asyncio
    async def test_initialize_tokens_from_chain_denoms(
        self,
        bank_servicer,
        exchange_servicer,
        smart_denom_metadata,
        aioresponses,
    ):
        test_network = Network.local()
        aioresponses.get(test_network.official_tokens_list_url, payload=[])

        pagination = pagination_pb.PageResponse(
            total=1,
        )

        bank_servicer.denoms_metadata_responses.append(
            bank_query_pb.QueryDenomsMetadataResponse(
                metadatas=[smart_denom_metadata],
                pagination=pagination,
            )
        )

        exchange_servicer.spot_markets_responses.append(exchange_query_pb.QuerySpotMarketsResponse(markets=[]))
        exchange_servicer.derivative_markets_responses.append(
            exchange_query_pb.QueryDerivativeMarketsResponse(markets=[])
        )
        exchange_servicer.binary_options_markets_responses.append(
            exchange_query_pb.QueryBinaryMarketsResponse(markets=[])
        )

        client = AsyncClient(
            network=test_network,
        )

        client.chain_exchange_v2_api._stub = exchange_servicer
        client.bank_api._stub = bank_servicer

        await client._initialize_tokens_and_markets()
        await client.initialize_tokens_from_chain_denoms()

        all_tokens = await client.all_tokens()
        assert 1 == len(all_tokens)
        assert smart_denom_metadata.symbol in all_tokens
