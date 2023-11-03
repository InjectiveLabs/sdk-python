import grpc
import pytest

from pyinjective.client.indexer.grpc.indexer_grpc_spot_api import IndexerGrpcSpotApi
from pyinjective.core.network import Network
from pyinjective.proto.exchange import injective_spot_exchange_rpc_pb2 as exchange_spot_pb
from tests.client.indexer.configurable_spot_query_servicer import ConfigurableSpotQueryServicer


@pytest.fixture
def spot_servicer():
    return ConfigurableSpotQueryServicer()


class TestIndexerGrpcSpotApi:
    @pytest.mark.asyncio
    async def test_fetch_markets(
        self,
        spot_servicer,
    ):
        base_token_meta = exchange_spot_pb.TokenMeta(
            name="Injective Protocol",
            address="0xe28b3B32B6c345A34Ff64674606124Dd5Aceca30",
            symbol="INJ",
            logo="https://static.alchemyapi.io/images/assets/7226.png",
            decimals=18,
            updated_at=1683119359318,
        )
        quote_token_meta = exchange_spot_pb.TokenMeta(
            name="Testnet Tether USDT",
            address="0x0000000000000000000000000000000000000000",
            symbol="USDT",
            logo="https://static.alchemyapi.io/images/assets/825.png",
            decimals=6,
            updated_at=1683119359320,
        )

        market = exchange_spot_pb.SpotMarketInfo(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            market_status="active",
            ticker="INJ/USDT",
            base_denom="inj",
            base_token_meta=base_token_meta,
            quote_denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            quote_token_meta=quote_token_meta,
            maker_fee_rate="-0.0001",
            taker_fee_rate="0.001",
            service_provider_fee="0.4",
            min_price_tick_size="0.000000000000001",
            min_quantity_tick_size="1000000000000000",
        )

        spot_servicer.markets_responses.append(
            exchange_spot_pb.MarketsResponse(
                markets=[market],
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcSpotApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = spot_servicer

        result_markets = await api.fetch_markets(
            market_status=market.market_status,
            base_denom=market.base_denom,
            quote_denom=market.quote_denom,
        )
        expected_markets = {
            "markets": [
                {
                    "marketId": market.market_id,
                    "marketStatus": market.market_status,
                    "ticker": market.ticker,
                    "baseDenom": market.base_denom,
                    "baseTokenMeta": {
                        "name": market.base_token_meta.name,
                        "address": market.base_token_meta.address,
                        "symbol": market.base_token_meta.symbol,
                        "logo": market.base_token_meta.logo,
                        "decimals": market.base_token_meta.decimals,
                        "updatedAt": str(market.base_token_meta.updated_at),
                    },
                    "quoteDenom": market.quote_denom,
                    "quoteTokenMeta": {
                        "name": market.quote_token_meta.name,
                        "address": market.quote_token_meta.address,
                        "symbol": market.quote_token_meta.symbol,
                        "logo": market.quote_token_meta.logo,
                        "decimals": market.quote_token_meta.decimals,
                        "updatedAt": str(market.quote_token_meta.updated_at),
                    },
                    "takerFeeRate": market.taker_fee_rate,
                    "makerFeeRate": market.maker_fee_rate,
                    "serviceProviderFee": market.service_provider_fee,
                    "minPriceTickSize": market.min_price_tick_size,
                    "minQuantityTickSize": market.min_quantity_tick_size,
                }
            ]
        }

        assert result_markets == expected_markets

    @pytest.mark.asyncio
    async def test_fetch_market(
        self,
        spot_servicer,
    ):
        base_token_meta = exchange_spot_pb.TokenMeta(
            name="Injective Protocol",
            address="0xe28b3B32B6c345A34Ff64674606124Dd5Aceca30",
            symbol="INJ",
            logo="https://static.alchemyapi.io/images/assets/7226.png",
            decimals=18,
            updated_at=1683119359318,
        )
        quote_token_meta = exchange_spot_pb.TokenMeta(
            name="Testnet Tether USDT",
            address="0x0000000000000000000000000000000000000000",
            symbol="USDT",
            logo="https://static.alchemyapi.io/images/assets/825.png",
            decimals=6,
            updated_at=1683119359320,
        )

        market = exchange_spot_pb.SpotMarketInfo(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            market_status="active",
            ticker="INJ/USDT",
            base_denom="inj",
            base_token_meta=base_token_meta,
            quote_denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            quote_token_meta=quote_token_meta,
            maker_fee_rate="-0.0001",
            taker_fee_rate="0.001",
            service_provider_fee="0.4",
            min_price_tick_size="0.000000000000001",
            min_quantity_tick_size="1000000000000000",
        )

        spot_servicer.market_responses.append(
            exchange_spot_pb.MarketResponse(
                market=market,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcSpotApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = spot_servicer

        result_market = await api.fetch_market(market_id=market.market_id)
        expected_market = {
            "market": {
                "marketId": market.market_id,
                "marketStatus": market.market_status,
                "ticker": market.ticker,
                "baseDenom": market.base_denom,
                "baseTokenMeta": {
                    "name": market.base_token_meta.name,
                    "address": market.base_token_meta.address,
                    "symbol": market.base_token_meta.symbol,
                    "logo": market.base_token_meta.logo,
                    "decimals": market.base_token_meta.decimals,
                    "updatedAt": str(market.base_token_meta.updated_at),
                },
                "quoteDenom": market.quote_denom,
                "quoteTokenMeta": {
                    "name": market.quote_token_meta.name,
                    "address": market.quote_token_meta.address,
                    "symbol": market.quote_token_meta.symbol,
                    "logo": market.quote_token_meta.logo,
                    "decimals": market.quote_token_meta.decimals,
                    "updatedAt": str(market.quote_token_meta.updated_at),
                },
                "takerFeeRate": market.taker_fee_rate,
                "makerFeeRate": market.maker_fee_rate,
                "serviceProviderFee": market.service_provider_fee,
                "minPriceTickSize": market.min_price_tick_size,
                "minQuantityTickSize": market.min_quantity_tick_size,
            }
        }

        assert result_market == expected_market

    @pytest.mark.asyncio
    async def test_fetch_orderbook_v2(
        self,
        spot_servicer,
    ):
        buy = exchange_spot_pb.PriceLevel(
            price="0.000000000014198",
            quantity="142000000000000000000",
            timestamp=1698982052141,
        )
        sell = exchange_spot_pb.PriceLevel(
            price="0.00000000095699",
            quantity="189000000000000000",
            timestamp=1698920369246,
        )

        orderbook = exchange_spot_pb.SpotLimitOrderbookV2(
            buys=[buy],
            sells=[sell],
            sequence=5506752,
            timestamp=1698982083606,
        )

        spot_servicer.orderbook_v2_responses.append(
            exchange_spot_pb.OrderbookV2Response(
                orderbook=orderbook,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcSpotApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = spot_servicer

        result_orderbook = await api.fetch_orderbook_v2(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        )
        expected_orderbook = {
            "orderbook": {
                "buys": [
                    {
                        "price": buy.price,
                        "quantity": buy.quantity,
                        "timestamp": str(buy.timestamp),
                    }
                ],
                "sells": [
                    {
                        "price": sell.price,
                        "quantity": sell.quantity,
                        "timestamp": str(sell.timestamp),
                    }
                ],
                "sequence": str(orderbook.sequence),
                "timestamp": str(orderbook.timestamp),
            }
        }

        assert result_orderbook == expected_orderbook

    async def _dummy_metadata_provider(self):
        return None
