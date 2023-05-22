import pytest


@pytest.fixture
def inj_token_meta():
    from pyinjective.proto.exchange.injective_spot_exchange_rpc_pb2 import TokenMeta

    token = TokenMeta(
        name="Injective Protocol",
        address="0xe28b3B32B6c345A34Ff64674606124Dd5Aceca30",
        symbol="INJ",
        logo="https://static.alchemyapi.io/images/assets/7226.png",
        decimals=18,
        updated_at=1681739137644
    )

    return token

@pytest.fixture
def ape_token_meta():
    from pyinjective.proto.exchange.injective_spot_exchange_rpc_pb2 import TokenMeta

    token = TokenMeta(
        name="APE",
        address="0x0000000000000000000000000000000000000000",
        symbol="APE",
        logo="https://assets.coingecko.com/coins/images/24383/small/apecoin.jpg?1647476455",
        decimals=18,
        updated_at=1681739137646
    )

    return token

@pytest.fixture
def usdt_token_meta():
    from pyinjective.proto.exchange.injective_spot_exchange_rpc_pb2 import TokenMeta

    token = TokenMeta(
        name="USDT",
        address="0x0000000000000000000000000000000000000000",
        symbol="USDT",
        logo="https://static.alchemyapi.io/images/assets/825.png",
        decimals=6,
        updated_at=1681739137645
    )

    return token

@pytest.fixture
def ape_usdt_spot_market(ape_token_meta, usdt_token_meta):
    from pyinjective.proto.exchange.injective_spot_exchange_rpc_pb2 import SpotMarketInfo

    market_request = SpotMarketInfo(
        market_id="0x7a57e705bb4e09c88aecfc295569481dbf2fe1d5efe364651fbe72385938e9b0",
        market_status="active",
        ticker="APE/USDT",
        base_denom="peggy0x44C21afAaF20c270EBbF5914Cfc3b5022173FEB7",
        base_token_meta=ape_token_meta,
        quote_denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
        quote_token_meta=usdt_token_meta,
        maker_fee_rate="-0.0001",
        taker_fee_rate="0.001",
        service_provider_fee="0.4",
        min_price_tick_size="0.000000000000001",
        min_quantity_tick_size="1000000000000000",
    )

    return market_request

@pytest.fixture
def inj_usdt_spot_market(inj_token_meta, usdt_token_meta):
    from pyinjective.proto.exchange.injective_spot_exchange_rpc_pb2 import SpotMarketInfo

    market_request = SpotMarketInfo(
        market_id="0x7a57e705bb4e09c88aecfc295569481dbf2fe1d5efe364651fbe72385938e9b0",
        market_status="active",
        ticker="INJ/USDT",
        base_denom="peggy0x44C21afAaF20c270EBbF5914Cfc3b5022173FEB7",
        base_token_meta=inj_token_meta,
        quote_denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
        quote_token_meta=usdt_token_meta,
        maker_fee_rate="-0.0001",
        taker_fee_rate="0.001",
        service_provider_fee="0.4",
        min_price_tick_size="0.000000000000001",
        min_quantity_tick_size="1000000000000000",
    )

    return market_request
