import grpc
import pytest

from pyinjective.client.indexer.grpc.indexer_grpc_oracle_api import IndexerGrpcOracleApi
from pyinjective.core.network import Network
from pyinjective.proto.exchange import injective_oracle_rpc_pb2 as exchange_oracle_pb
from tests.client.indexer.configurable_oracle_query_servicer import ConfigurableOracleQueryServicer


@pytest.fixture
def oracle_servicer():
    return ConfigurableOracleQueryServicer()


class TestIndexerGrpcMetaApi:
    @pytest.mark.asyncio
    async def test_fetch_oracle_list(
        self,
        oracle_servicer,
    ):
        oracle = exchange_oracle_pb.Oracle(
            symbol="Gold/USDT",
            base_symbol="Gold",
            quote_symbol="USDT",
            oracle_type="pricefeed",
            price="1",
        )

        oracle_servicer.oracle_list_responses.append(
            exchange_oracle_pb.OracleListResponse(
                oracles=[oracle],
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcOracleApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = oracle_servicer

        result_oracle_list = await api.fetch_oracle_list()
        expected_oracle_list = {
            "oracles": [
                {
                    "symbol": oracle.symbol,
                    "baseSymbol": oracle.base_symbol,
                    "quoteSymbol": oracle.quote_symbol,
                    "oracleType": oracle.oracle_type,
                    "price": oracle.price,
                }
            ]
        }

        assert result_oracle_list == expected_oracle_list

    @pytest.mark.asyncio
    async def test_fetch_oracle_price(
        self,
        oracle_servicer,
    ):
        price = "0.00000002"

        oracle_servicer.price_responses.append(
            exchange_oracle_pb.PriceResponse(
                price=price,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcOracleApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = oracle_servicer

        result_oracle_list = await api.fetch_oracle_price(
            base_symbol="Gold",
            quote_symbol="USDT",
            oracle_type="pricefeed",
            oracle_scale_factor=6,
        )
        expected_oracle_list = {"price": price}

        assert result_oracle_list == expected_oracle_list

    async def _dummy_metadata_provider(self):
        return None
