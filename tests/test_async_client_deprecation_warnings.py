from warnings import catch_warnings

import pytest

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network
from pyinjective.proto.injective.exchange.v1beta1 import query_pb2 as exchange_query_pb
from tests.client.chain.grpc.configurable_exchange_query_servicer import ConfigurableExchangeQueryServicer
from tests.client.chain.stream_grpc.configurable_chain_stream_query_servicer import ConfigurableChainStreamQueryServicer


@pytest.fixture
def chain_stream_servicer():
    return ConfigurableChainStreamQueryServicer()


@pytest.fixture
def exchange_servicer():
    return ConfigurableExchangeQueryServicer()


class TestAsyncClientDeprecationWarnings:
    @pytest.mark.asyncio
    async def test_fetch_aggregate_volume_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.aggregate_volume_responses.append(exchange_query_pb.QueryAggregateVolumeResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_aggregate_volume(
                account="inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_aggregate_volume_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_aggregate_volumes_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.aggregate_volumes_responses.append(exchange_query_pb.QueryAggregateVolumesResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_aggregate_volumes(
                accounts=["inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"],
                market_ids=["0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"],
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_aggregate_volumes_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_aggregate_market_volume_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.aggregate_market_volume_responses.append(
            exchange_query_pb.QueryAggregateMarketVolumeResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_aggregate_market_volume(
                market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_aggregate_market_volume_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_aggregate_market_volumes_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.aggregate_market_volumes_responses.append(
            exchange_query_pb.QueryAggregateMarketVolumesResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_aggregate_market_volumes(
                market_ids=["0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"],
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_aggregate_market_volumes_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_chain_spot_markets_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.spot_markets_responses.append(exchange_query_pb.QuerySpotMarketsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_chain_spot_markets()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_chain_spot_markets_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_chain_spot_market_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.spot_market_responses.append(exchange_query_pb.QuerySpotMarketResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_chain_spot_market(
                market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_chain_spot_market_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_chain_full_spot_markets_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.full_spot_markets_responses.append(exchange_query_pb.QueryFullSpotMarketsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_chain_full_spot_markets()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_chain_full_spot_markets_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_chain_full_spot_markets_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.full_spot_market_responses.append(exchange_query_pb.QueryFullSpotMarketResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_chain_full_spot_market(
                market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_chain_full_spot_market_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_chain_spot_orderbook_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.spot_orderbook_responses.append(exchange_query_pb.QuerySpotOrderbookResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_chain_spot_orderbook(
                market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_chain_spot_orderbook_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_chain_trader_spot_orders_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.trader_spot_orders_responses.append(exchange_query_pb.QueryTraderSpotOrdersResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_chain_trader_spot_orders(
                market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
                subaccount_id="0x5303d92e49a619bb29de8fb6f59c0e7589213cc8000000000000000000000001",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_chain_trader_spot_orders_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_chain_account_address_spot_orders_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.account_address_spot_orders_responses.append(
            exchange_query_pb.QueryAccountAddressSpotOrdersResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_chain_account_address_spot_orders(
                market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
                account_address="inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_chain_account_address_spot_orders_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_chain_spot_orders_by_hashes_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.spot_orders_by_hashes_responses.append(exchange_query_pb.QuerySpotOrdersByHashesResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_chain_spot_orders_by_hashes(
                market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
                subaccount_id="0x5303d92e49a619bb29de8fb6f59c0e7589213cc8000000000000000000000001",
                order_hashes=["0x57a01cd26f1e2080860af3264e865d7c9c034a701e30946d01c1dc7a303cf2c1"],
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_chain_spot_orders_by_hashes_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_chain_subaccount_orders_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.subaccount_orders_responses.append(exchange_query_pb.QuerySubaccountOrdersResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_chain_subaccount_orders(
                subaccount_id="0x5303d92e49a619bb29de8fb6f59c0e7589213cc8000000000000000000000001",
                market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_chain_subaccount_orders_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_chain_trader_spot_transient_orders_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.trader_spot_transient_orders_responses.append(
            exchange_query_pb.QueryTraderSpotOrdersResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_chain_trader_spot_transient_orders(
                market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
                subaccount_id="0x5303d92e49a619bb29de8fb6f59c0e7589213cc8000000000000000000000001",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_chain_trader_spot_transient_orders_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_spot_mid_price_and_tob_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.spot_mid_price_and_tob_responses.append(exchange_query_pb.QuerySpotMidPriceAndTOBResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_spot_mid_price_and_tob(
                market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_spot_mid_price_and_tob_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_derivative_mid_price_and_tob_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.derivative_mid_price_and_tob_responses.append(
            exchange_query_pb.QueryDerivativeMidPriceAndTOBResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_derivative_mid_price_and_tob(
                market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_derivative_mid_price_and_tob_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_chain_derivative_orderbook_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.derivative_orderbook_responses.append(exchange_query_pb.QueryDerivativeOrderbookResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_chain_derivative_orderbook(
                market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_chain_derivative_orderbook_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_chain_trader_derivative_orders_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.trader_derivative_orders_responses.append(
            exchange_query_pb.QueryTraderDerivativeOrdersResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_chain_trader_derivative_orders(
                market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
                subaccount_id="0x5303d92e49a619bb29de8fb6f59c0e7589213cc8000000000000000000000001",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_chain_trader_derivative_orders_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_chain_account_address_derivative_orders_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.account_address_derivative_orders_responses.append(
            exchange_query_pb.QueryAccountAddressDerivativeOrdersResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_chain_account_address_derivative_orders(
                market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
                account_address="inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_chain_account_address_derivative_orders_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_chain_derivative_orders_by_hashes_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.derivative_orders_by_hashes_responses.append(
            exchange_query_pb.QueryDerivativeOrdersByHashesResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_chain_derivative_orders_by_hashes(
                market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
                subaccount_id="0x5303d92e49a619bb29de8fb6f59c0e7589213cc8000000000000000000000001",
                order_hashes=["0x57a01cd26f1e2080860af3264e865d7c9c034a701e30946d01c1dc7a303cf2c1"],
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_chain_derivative_orders_by_hashes_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_chain_trader_derivative_transient_orders_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.trader_derivative_transient_orders_responses.append(
            exchange_query_pb.QueryTraderDerivativeOrdersResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_chain_trader_derivative_transient_orders(
                market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
                subaccount_id="0x5303d92e49a619bb29de8fb6f59c0e7589213cc8000000000000000000000001",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_chain_trader_derivative_transient_orders_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_chain_derivative_markets_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.derivative_markets_responses.append(exchange_query_pb.QueryDerivativeMarketsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_chain_derivative_markets()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_chain_derivative_markets_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_chain_derivative_market_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.derivative_market_responses.append(exchange_query_pb.QueryDerivativeMarketResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_chain_derivative_market(
                market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_chain_derivative_market_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_chain_positions_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.positions_responses.append(exchange_query_pb.QueryPositionsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_chain_positions()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_chain_positions_v2 instead"

    @pytest.mark.asyncio
    async def test_fetch_chain_subaccount_positions_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.subaccount_positions_responses.append(exchange_query_pb.QuerySubaccountPositionsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_chain_subaccount_positions(
                subaccount_id="0x5303d92e49a619bb29de8fb6f59c0e7589213cc8000000000000000000000001",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_chain_subaccount_positions_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_chain_subaccount_position_in_market_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.subaccount_position_in_market_responses.append(
            exchange_query_pb.QuerySubaccountPositionInMarketResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_chain_subaccount_position_in_market(
                subaccount_id="0x5303d92e49a619bb29de8fb6f59c0e7589213cc8000000000000000000000001",
                market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_chain_subaccount_position_in_market_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_chain_subaccount_effective_position_in_market_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.subaccount_effective_position_in_market_responses.append(
            exchange_query_pb.QuerySubaccountEffectivePositionInMarketResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_chain_subaccount_effective_position_in_market(
                subaccount_id="0x5303d92e49a619bb29de8fb6f59c0e7589213cc8000000000000000000000001",
                market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_chain_subaccount_effective_position_in_market_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_chain_expiry_futures_market_info_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.expiry_futures_market_info_responses.append(
            exchange_query_pb.QueryExpiryFuturesMarketInfoResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_chain_expiry_futures_market_info(
                market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_chain_expiry_futures_market_info_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_chain_perpetual_market_funding_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.perpetual_market_funding_responses.append(
            exchange_query_pb.QueryPerpetualMarketFundingResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_chain_perpetual_market_funding(
                market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_chain_perpetual_market_funding_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_subaccount_order_metadata_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.subaccount_order_metadata_responses.append(
            exchange_query_pb.QuerySubaccountOrderMetadataResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_subaccount_order_metadata(
                subaccount_id="0x5303d92e49a619bb29de8fb6f59c0e7589213cc8000000000000000000000001",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_subaccount_order_metadata_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_fee_discount_account_info_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.fee_discount_account_info_responses.append(
            exchange_query_pb.QueryFeeDiscountAccountInfoResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_fee_discount_account_info(
                account="inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_fee_discount_account_info_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_fee_discount_schedule_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.fee_discount_schedule_responses.append(exchange_query_pb.QueryFeeDiscountScheduleResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_fee_discount_schedule()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_fee_discount_schedule_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_historical_trade_records_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.historical_trade_records_responses.append(
            exchange_query_pb.QueryHistoricalTradeRecordsResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_historical_trade_records(
                market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_historical_trade_records_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_market_volatility_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.market_volatility_responses.append(exchange_query_pb.QueryMarketVolatilityResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_market_volatility(
                market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_market_volatility_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_chain_binary_options_markets_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.binary_options_markets_responses.append(exchange_query_pb.QueryBinaryMarketsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_chain_binary_options_markets()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_chain_binary_options_markets_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_trader_derivative_conditional_orders_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.trader_derivative_conditional_orders_responses.append(
            exchange_query_pb.QueryTraderDerivativeConditionalOrdersResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_trader_derivative_conditional_orders()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_trader_derivative_conditional_orders_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_l3_derivative_orderbook_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.l3_derivative_orderbook_responses.append(
            exchange_query_pb.QueryFullDerivativeOrderbookResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_l3_derivative_orderbook(
                market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_l3_derivative_orderbook_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_l3_spot_orderbook_deprecation_warning(
        self,
        exchange_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_api._stub = exchange_servicer

        exchange_servicer.l3_spot_orderbook_responses.append(exchange_query_pb.QueryFullSpotOrderbookResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.fetch_l3_spot_orderbook(
                market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_l3_spot_orderbook_v2 instead"
        )
