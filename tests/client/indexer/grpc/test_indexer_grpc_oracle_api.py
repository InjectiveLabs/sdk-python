import grpc
import pytest

from pyinjective.client.indexer.grpc.indexer_grpc_oracle_api import IndexerGrpcOracleApi
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.exchange import injective_oracle_rpc_pb2 as exchange_oracle_pb
from tests.client.indexer.configurable_oracle_query_servicer import ConfigurableOracleQueryServicer


@pytest.fixture
def oracle_servicer():
    return ConfigurableOracleQueryServicer()


class TestIndexerGrpcOracleApi:
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

        api = self._api_instance(servicer=oracle_servicer)

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

        api = self._api_instance(servicer=oracle_servicer)

        result_oracle_list = await api.fetch_oracle_price(
            base_symbol="Gold",
            quote_symbol="USDT",
            oracle_type="pricefeed",
            oracle_scale_factor=6,
        )
        expected_oracle_list = {"price": price}

        assert result_oracle_list == expected_oracle_list

    @pytest.mark.asyncio
    async def test_fetch_oracle_price_v2(
        self,
        oracle_servicer,
    ):
        price_result = exchange_oracle_pb.PriceV2Result(
            base_symbol="Gold",
            quote_symbol="USDT",
            oracle_type="pricefeed",
            oracle_scale_factor=6,
            price="10.56",
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
        )

        price_response = exchange_oracle_pb.PriceV2Response(prices=[price_result])

        oracle_servicer.price_v2_responses.append(price_response)

        api = self._api_instance(servicer=oracle_servicer)

        filter = exchange_oracle_pb.PricePayloadV2(
            base_symbol="Gold",
            quote_symbol="USDT",
            oracle_type="pricefeed",
            oracle_scale_factor=6,
        )
        result_oracle_list = await api.fetch_oracle_price_v2(filters=[filter])
        expected_oracle_list = {
            "prices": [
                {
                    "baseSymbol": price_result.base_symbol,
                    "quoteSymbol": price_result.quote_symbol,
                    "oracleType": price_result.oracle_type,
                    "oracleScaleFactor": price_result.oracle_scale_factor,
                    "price": price_result.price,
                    "marketId": price_result.market_id,
                }
            ]
        }

        assert result_oracle_list == expected_oracle_list

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = IndexerGrpcOracleApi(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer

        return api
