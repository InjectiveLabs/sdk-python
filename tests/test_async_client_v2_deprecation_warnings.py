import warnings

import pytest

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network
from pyinjective.proto.injective.exchange.v2 import exchange_pb2 as exchange_pb
from pyinjective.proto.injective.exchange.v2 import query_pb2 as exchange_query_pb
from tests.client.chain.grpc.configurable_exchange_v2_query_servicer import ConfigurableExchangeV2QueryServicer


@pytest.fixture
def exchange_servicer():
    return ConfigurableExchangeV2QueryServicer()


class TestAsyncClientV2DeprecationWarnings:
    @pytest.mark.asyncio
    async def test_fetch_denom_decimal_deprecation_warning(self, exchange_servicer):
        decimal = 18
        exchange_servicer.auction_exchange_transfer_denom_decimal_responses.append(
            exchange_query_pb.QueryAuctionExchangeTransferDenomDecimalResponse(
                decimal=decimal,
            )
        )

        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_v2_api._stub = exchange_servicer

        with warnings.catch_warnings(record=True) as all_warnings:
            warnings.simplefilter("always")
            result = await client.fetch_denom_decimal(denom="inj")

        # Verify the method still works correctly
        assert result == {"decimal": str(decimal)}

        # Verify deprecation warning was issued
        deprecation_warnings = [
            warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)
        ]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_auction_exchange_transfer_denom_decimal instead"
        )

    @pytest.mark.asyncio
    async def test_fetch_denom_decimals_deprecation_warning(self, exchange_servicer):
        denom_decimal = exchange_pb.DenomDecimals(
            denom="inj",
            decimals=18,
        )
        exchange_servicer.auction_exchange_transfer_denom_decimals_responses.append(
            exchange_query_pb.QueryAuctionExchangeTransferDenomDecimalsResponse(
                denom_decimals=[denom_decimal],
            )
        )

        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_exchange_v2_api._stub = exchange_servicer

        with warnings.catch_warnings(record=True) as all_warnings:
            warnings.simplefilter("always")
            result = await client.fetch_denom_decimals(denoms=["inj"])

        # Verify the method still works correctly
        expected_result = {
            "denomDecimals": [
                {
                    "denom": denom_decimal.denom,
                    "decimals": str(denom_decimal.decimals),
                }
            ]
        }
        assert result == expected_result

        # Verify deprecation warning was issued
        deprecation_warnings = [
            warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)
        ]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_auction_exchange_transfer_denom_decimals instead"
        )