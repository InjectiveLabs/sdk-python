import pytest


@pytest.fixture
def smart_denom_metadata():
    from pyinjective.proto.cosmos.bank.v1beta1 import bank_pb2 as bank_pb

    first_denom_unit = bank_pb.DenomUnit(
        denom="factory/inj105ujajd95znwjvcy3hwcz80pgy8tc6v77spur0/SMART", exponent=0, aliases=["microSMART"]
    )
    second_denom_unit = bank_pb.DenomUnit(denom="SMART", exponent=6, aliases=["SMART"])
    metadata = bank_pb.Metadata(
        description="SMART",
        denom_units=[first_denom_unit, second_denom_unit],
        base="factory/inj105ujajd95znwjvcy3hwcz80pgy8tc6v77spur0/SMART",
        display="SMART",
        name="SMART",
        symbol="SMART",
        uri=(
            "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/"
            "Flag_of_the_People%27s_Republic_of_China.svg/"
            "2560px-Flag_of_the_People%27s_Republic_of_China.svg.png"
        ),
        uri_hash="",
    )

    return metadata

@pytest.fixture
def ape_usdt_spot_market_meta():
    from pyinjective.proto.injective.exchange.v1beta1 import exchange_pb2 as exchange_pb

    market = exchange_pb.SpotMarket(
        ticker="APE/USDT",
        base_denom="peggy0x44C21afAaF20c270EBbF5914Cfc3b5022173FEB7",
        quote_denom="factory/inj10vkkttgxdeqcgeppu20x9qtyvuaxxev8qh0awq/usdt",
        maker_fee_rate="-0.0001",
        taker_fee_rate="0.001",
        relayer_fee_share_rate="0.4",
        market_id="0x8b67e705bb4e09c88aecfc295569481dbf2fe1d5efe364651fbe72385938e000",
        status=1,
        min_price_tick_size="0.01",
        min_quantity_tick_size="1",
        min_notional="5",
        admin="inj1knhahceyp57j5x7xh69p7utegnnnfgxavmahjr",
        admin_permissions=1,
    )

    return market


@pytest.fixture
def inj_usdt_spot_market_meta(inj_token_meta, usdt_token_meta):
    from pyinjective.proto.injective.exchange.v1beta1 import exchange_pb2 as exchange_pb

    market = exchange_pb.SpotMarket(
        ticker="INJ/USDT",
        base_denom="inj",
        quote_denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
        maker_fee_rate="-0.0001",
        taker_fee_rate="0.001",
        relayer_fee_share_rate="0.4",
        market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
        status=1,
        min_price_tick_size="0.01",
        min_quantity_tick_size="1",
        min_notional="5",
        admin="inj1knhahceyp57j5x7xh69p7utegnnnfgxavmahjr",
        admin_permissions=1,
    )

    return market


@pytest.fixture
def btc_usdt_perp_market_meta(usdt_perp_token_meta):
    from pyinjective.proto.injective.exchange.v1beta1 import exchange_pb2 as exchange_pb, query_pb2 as exchange_query_pb

    market = exchange_pb.DerivativeMarket(
        ticker="BTC/USDT PERP",
        oracle_base="BTC",
        oracle_quote="USDT",
        oracle_type=10,
        oracle_scale_factor=6,
        quote_denom="peggy0xdAC17F958D2ee523a2206206994597C13D831ec7",
        market_id="0x4ca0f92fc28be0c9761326016b5a1a2177dd6375558365116b5bdda9abc229ce",
        initial_margin_ratio="0.095",
        maintenance_margin_ratio="0.025",
        maker_fee_rate="-0.0001",
        taker_fee_rate="0.001",
        relayer_fee_share_rate="0.4",
        isPerpetual=True,
        status=1,
        min_price_tick_size="0.01",
        min_quantity_tick_size="1",
        min_notional="5",
        admin="inj1knhahceyp57j5x7xh69p7utegnnnfgxavmahjr",
        admin_permissions=1,
    )
    market_info = exchange_pb.PerpetualMarketInfo(
        market_id="0x4ca0f92fc28be0c9761326016b5a1a2177dd6375558365116b5bdda9abc229ce",
        hourly_funding_rate_cap="625000000000000",
        hourly_interest_rate="4166660000000",
        next_funding_timestamp=1708099200,
        funding_interval=3600,
    )
    funding_info = exchange_pb.PerpetualMarketFunding(
        cumulative_funding="-107853477278881692857461",
        cumulative_price="0",
        last_timestamp=1708099200,
    )
    perpetual_info = exchange_query_pb.PerpetualMarketState(
        market_info=market_info,
        funding_info=funding_info,
    )
    mid_price_and_tob = exchange_pb.MidPriceAndTOB(
        mid_price="2000000000000000000",
        best_buy_price="1000000000000000000",
        best_sell_price="3000000000000000000",
    )
    full_market = exchange_query_pb.FullDerivativeMarket(
        market=market,
        perpetual_info=perpetual_info,
        mark_price="33803835513327368963000000",
        mid_price_and_tob=mid_price_and_tob,
    )

    return full_market


@pytest.fixture
def first_match_bet_market_meta(inj_usdt_spot_market_meta):
    from pyinjective.proto.injective.exchange.v1beta1 import exchange_pb2 as exchange_pb

    market = exchange_pb.BinaryOptionsMarket(
        ticker="5fdbe0b1-1707800399-WAS",
        oracle_symbol="Frontrunner",
        oracle_provider="Frontrunner",
        oracle_type=11,
        oracle_scale_factor=6,
        expiration_timestamp=1708099200,
        settlement_timestamp=1707099200,
        admin="inj1zlh5sqevkfphtwnu9cul8p89vseme2eqt0snn9",
        quote_denom=inj_usdt_spot_market_meta.quote_denom,
        market_id="0x230dcce315364ff6360097838701b14713e2f4007d704df20ed3d81d09eec957",
        maker_fee_rate="0",
        taker_fee_rate="0",
        relayer_fee_share_rate="0.4",
        status=1,
        min_price_tick_size="0.01",
        min_quantity_tick_size="1",
        settlement_price="1",
        min_notional="1",
        admin_permissions=1,
    )

    return market
