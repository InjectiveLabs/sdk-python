# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/exchange/v2/market.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.injective.oracle.v1beta1 import oracle_pb2 as injective_dot_oracle_dot_v1beta1_dot_oracle__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"injective/exchange/v2/market.proto\x12\x15injective.exchange.v2\x1a\x14gogoproto/gogo.proto\x1a%injective/oracle/v1beta1/oracle.proto\"\x84\x01\n\x13MarketFeeMultiplier\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12J\n\x0e\x66\x65\x65_multiplier\x18\x02 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\rfeeMultiplier:\x04\x88\xa0\x1f\x00\"\xb3\x06\n\nSpotMarket\x12\x16\n\x06ticker\x18\x01 \x01(\tR\x06ticker\x12\x1d\n\nbase_denom\x18\x02 \x01(\tR\tbaseDenom\x12\x1f\n\x0bquote_denom\x18\x03 \x01(\tR\nquoteDenom\x12I\n\x0emaker_fee_rate\x18\x04 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x0cmakerFeeRate\x12I\n\x0etaker_fee_rate\x18\x05 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x0ctakerFeeRate\x12X\n\x16relayer_fee_share_rate\x18\x06 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x13relayerFeeShareRate\x12\x1b\n\tmarket_id\x18\x07 \x01(\tR\x08marketId\x12;\n\x06status\x18\x08 \x01(\x0e\x32#.injective.exchange.v2.MarketStatusR\x06status\x12R\n\x13min_price_tick_size\x18\t \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x10minPriceTickSize\x12X\n\x16min_quantity_tick_size\x18\n \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x13minQuantityTickSize\x12\x46\n\x0cmin_notional\x18\x0b \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x0bminNotional\x12\x14\n\x05\x61\x64min\x18\x0c \x01(\tR\x05\x61\x64min\x12+\n\x11\x61\x64min_permissions\x18\r \x01(\rR\x10\x61\x64minPermissions\x12#\n\rbase_decimals\x18\x0e \x01(\rR\x0c\x62\x61seDecimals\x12%\n\x0equote_decimals\x18\x0f \x01(\rR\rquoteDecimals\"\xf9\x08\n\x13\x42inaryOptionsMarket\x12\x16\n\x06ticker\x18\x01 \x01(\tR\x06ticker\x12#\n\roracle_symbol\x18\x02 \x01(\tR\x0coracleSymbol\x12\'\n\x0foracle_provider\x18\x03 \x01(\tR\x0eoracleProvider\x12\x45\n\x0boracle_type\x18\x04 \x01(\x0e\x32$.injective.oracle.v1beta1.OracleTypeR\noracleType\x12.\n\x13oracle_scale_factor\x18\x05 \x01(\rR\x11oracleScaleFactor\x12\x31\n\x14\x65xpiration_timestamp\x18\x06 \x01(\x03R\x13\x65xpirationTimestamp\x12\x31\n\x14settlement_timestamp\x18\x07 \x01(\x03R\x13settlementTimestamp\x12\x14\n\x05\x61\x64min\x18\x08 \x01(\tR\x05\x61\x64min\x12\x1f\n\x0bquote_denom\x18\t \x01(\tR\nquoteDenom\x12\x1b\n\tmarket_id\x18\n \x01(\tR\x08marketId\x12I\n\x0emaker_fee_rate\x18\x0b \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x0cmakerFeeRate\x12I\n\x0etaker_fee_rate\x18\x0c \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x0ctakerFeeRate\x12X\n\x16relayer_fee_share_rate\x18\r \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x13relayerFeeShareRate\x12;\n\x06status\x18\x0e \x01(\x0e\x32#.injective.exchange.v2.MarketStatusR\x06status\x12R\n\x13min_price_tick_size\x18\x0f \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x10minPriceTickSize\x12X\n\x16min_quantity_tick_size\x18\x10 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x13minQuantityTickSize\x12N\n\x10settlement_price\x18\x11 \x01(\tB#\xc8\xde\x1f\x01\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x0fsettlementPrice\x12\x46\n\x0cmin_notional\x18\x12 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x0bminNotional\x12+\n\x11\x61\x64min_permissions\x18\x13 \x01(\rR\x10\x61\x64minPermissions\x12%\n\x0equote_decimals\x18\x14 \x01(\rR\rquoteDecimals:\x04\x88\xa0\x1f\x00\"\xe3\t\n\x10\x44\x65rivativeMarket\x12\x16\n\x06ticker\x18\x01 \x01(\tR\x06ticker\x12\x1f\n\x0boracle_base\x18\x02 \x01(\tR\noracleBase\x12!\n\x0coracle_quote\x18\x03 \x01(\tR\x0boracleQuote\x12\x45\n\x0boracle_type\x18\x04 \x01(\x0e\x32$.injective.oracle.v1beta1.OracleTypeR\noracleType\x12.\n\x13oracle_scale_factor\x18\x05 \x01(\rR\x11oracleScaleFactor\x12\x1f\n\x0bquote_denom\x18\x06 \x01(\tR\nquoteDenom\x12\x1b\n\tmarket_id\x18\x07 \x01(\tR\x08marketId\x12U\n\x14initial_margin_ratio\x18\x08 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x12initialMarginRatio\x12]\n\x18maintenance_margin_ratio\x18\t \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x16maintenanceMarginRatio\x12I\n\x0emaker_fee_rate\x18\n \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x0cmakerFeeRate\x12I\n\x0etaker_fee_rate\x18\x0b \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x0ctakerFeeRate\x12X\n\x16relayer_fee_share_rate\x18\x0c \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x13relayerFeeShareRate\x12 \n\x0bisPerpetual\x18\r \x01(\x08R\x0bisPerpetual\x12;\n\x06status\x18\x0e \x01(\x0e\x32#.injective.exchange.v2.MarketStatusR\x06status\x12R\n\x13min_price_tick_size\x18\x0f \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x10minPriceTickSize\x12X\n\x16min_quantity_tick_size\x18\x10 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x13minQuantityTickSize\x12\x46\n\x0cmin_notional\x18\x11 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x0bminNotional\x12\x14\n\x05\x61\x64min\x18\x12 \x01(\tR\x05\x61\x64min\x12+\n\x11\x61\x64min_permissions\x18\x13 \x01(\rR\x10\x61\x64minPermissions\x12%\n\x0equote_decimals\x18\x14 \x01(\rR\rquoteDecimals\x12S\n\x13reduce_margin_ratio\x18\x15 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x11reduceMarginRatio:\x04\x88\xa0\x1f\x00\"\x8d\x01\n\x1e\x44\x65rivativeMarketSettlementInfo\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12N\n\x10settlement_price\x18\x02 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x0fsettlementPrice\"n\n\x0cMarketVolume\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12\x41\n\x06volume\x18\x02 \x01(\x0b\x32#.injective.exchange.v2.VolumeRecordB\x04\xc8\xde\x1f\x00R\x06volume\"\x9e\x01\n\x0cVolumeRecord\x12\x46\n\x0cmaker_volume\x18\x01 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x0bmakerVolume\x12\x46\n\x0ctaker_volume\x18\x02 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x0btakerVolume\"\x8c\x01\n\x1c\x45xpiryFuturesMarketInfoState\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12O\n\x0bmarket_info\x18\x02 \x01(\x0b\x32..injective.exchange.v2.ExpiryFuturesMarketInfoR\nmarketInfo\"\x83\x01\n\x1bPerpetualMarketFundingState\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12G\n\x07\x66unding\x18\x02 \x01(\x0b\x32-.injective.exchange.v2.PerpetualMarketFundingR\x07\x66unding\"\xe4\x02\n\x17\x45xpiryFuturesMarketInfo\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12\x31\n\x14\x65xpiration_timestamp\x18\x02 \x01(\x03R\x13\x65xpirationTimestamp\x12\x30\n\x14twap_start_timestamp\x18\x03 \x01(\x03R\x12twapStartTimestamp\x12w\n&expiration_twap_start_price_cumulative\x18\x04 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\"expirationTwapStartPriceCumulative\x12N\n\x10settlement_price\x18\x05 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x0fsettlementPrice\"\xc6\x02\n\x13PerpetualMarketInfo\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12Z\n\x17hourly_funding_rate_cap\x18\x02 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x14hourlyFundingRateCap\x12U\n\x14hourly_interest_rate\x18\x03 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x12hourlyInterestRate\x12\x34\n\x16next_funding_timestamp\x18\x04 \x01(\x03R\x14nextFundingTimestamp\x12)\n\x10\x66unding_interval\x18\x05 \x01(\x03R\x0f\x66undingInterval\"\xe3\x01\n\x16PerpetualMarketFunding\x12R\n\x12\x63umulative_funding\x18\x01 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x11\x63umulativeFunding\x12N\n\x10\x63umulative_price\x18\x02 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDecR\x0f\x63umulativePrice\x12%\n\x0elast_timestamp\x18\x03 \x01(\x03R\rlastTimestamp*T\n\x0cMarketStatus\x12\x0f\n\x0bUnspecified\x10\x00\x12\n\n\x06\x41\x63tive\x10\x01\x12\n\n\x06Paused\x10\x02\x12\x0e\n\nDemolished\x10\x03\x12\x0b\n\x07\x45xpired\x10\x04\x42\xf1\x01\n\x19\x63om.injective.exchange.v2B\x0bMarketProtoP\x01ZQgithub.com/InjectiveLabs/injective-core/injective-chain/modules/exchange/types/v2\xa2\x02\x03IEX\xaa\x02\x15Injective.Exchange.V2\xca\x02\x15Injective\\Exchange\\V2\xe2\x02!Injective\\Exchange\\V2\\GPBMetadata\xea\x02\x17Injective::Exchange::V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.exchange.v2.market_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.injective.exchange.v2B\013MarketProtoP\001ZQgithub.com/InjectiveLabs/injective-core/injective-chain/modules/exchange/types/v2\242\002\003IEX\252\002\025Injective.Exchange.V2\312\002\025Injective\\Exchange\\V2\342\002!Injective\\Exchange\\V2\\GPBMetadata\352\002\027Injective::Exchange::V2'
  _globals['_MARKETFEEMULTIPLIER'].fields_by_name['fee_multiplier']._loaded_options = None
  _globals['_MARKETFEEMULTIPLIER'].fields_by_name['fee_multiplier']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_MARKETFEEMULTIPLIER']._loaded_options = None
  _globals['_MARKETFEEMULTIPLIER']._serialized_options = b'\210\240\037\000'
  _globals['_SPOTMARKET'].fields_by_name['maker_fee_rate']._loaded_options = None
  _globals['_SPOTMARKET'].fields_by_name['maker_fee_rate']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_SPOTMARKET'].fields_by_name['taker_fee_rate']._loaded_options = None
  _globals['_SPOTMARKET'].fields_by_name['taker_fee_rate']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_SPOTMARKET'].fields_by_name['relayer_fee_share_rate']._loaded_options = None
  _globals['_SPOTMARKET'].fields_by_name['relayer_fee_share_rate']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_SPOTMARKET'].fields_by_name['min_price_tick_size']._loaded_options = None
  _globals['_SPOTMARKET'].fields_by_name['min_price_tick_size']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_SPOTMARKET'].fields_by_name['min_quantity_tick_size']._loaded_options = None
  _globals['_SPOTMARKET'].fields_by_name['min_quantity_tick_size']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_SPOTMARKET'].fields_by_name['min_notional']._loaded_options = None
  _globals['_SPOTMARKET'].fields_by_name['min_notional']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_BINARYOPTIONSMARKET'].fields_by_name['maker_fee_rate']._loaded_options = None
  _globals['_BINARYOPTIONSMARKET'].fields_by_name['maker_fee_rate']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_BINARYOPTIONSMARKET'].fields_by_name['taker_fee_rate']._loaded_options = None
  _globals['_BINARYOPTIONSMARKET'].fields_by_name['taker_fee_rate']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_BINARYOPTIONSMARKET'].fields_by_name['relayer_fee_share_rate']._loaded_options = None
  _globals['_BINARYOPTIONSMARKET'].fields_by_name['relayer_fee_share_rate']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_BINARYOPTIONSMARKET'].fields_by_name['min_price_tick_size']._loaded_options = None
  _globals['_BINARYOPTIONSMARKET'].fields_by_name['min_price_tick_size']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_BINARYOPTIONSMARKET'].fields_by_name['min_quantity_tick_size']._loaded_options = None
  _globals['_BINARYOPTIONSMARKET'].fields_by_name['min_quantity_tick_size']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_BINARYOPTIONSMARKET'].fields_by_name['settlement_price']._loaded_options = None
  _globals['_BINARYOPTIONSMARKET'].fields_by_name['settlement_price']._serialized_options = b'\310\336\037\001\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_BINARYOPTIONSMARKET'].fields_by_name['min_notional']._loaded_options = None
  _globals['_BINARYOPTIONSMARKET'].fields_by_name['min_notional']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_BINARYOPTIONSMARKET']._loaded_options = None
  _globals['_BINARYOPTIONSMARKET']._serialized_options = b'\210\240\037\000'
  _globals['_DERIVATIVEMARKET'].fields_by_name['initial_margin_ratio']._loaded_options = None
  _globals['_DERIVATIVEMARKET'].fields_by_name['initial_margin_ratio']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_DERIVATIVEMARKET'].fields_by_name['maintenance_margin_ratio']._loaded_options = None
  _globals['_DERIVATIVEMARKET'].fields_by_name['maintenance_margin_ratio']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_DERIVATIVEMARKET'].fields_by_name['maker_fee_rate']._loaded_options = None
  _globals['_DERIVATIVEMARKET'].fields_by_name['maker_fee_rate']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_DERIVATIVEMARKET'].fields_by_name['taker_fee_rate']._loaded_options = None
  _globals['_DERIVATIVEMARKET'].fields_by_name['taker_fee_rate']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_DERIVATIVEMARKET'].fields_by_name['relayer_fee_share_rate']._loaded_options = None
  _globals['_DERIVATIVEMARKET'].fields_by_name['relayer_fee_share_rate']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_DERIVATIVEMARKET'].fields_by_name['min_price_tick_size']._loaded_options = None
  _globals['_DERIVATIVEMARKET'].fields_by_name['min_price_tick_size']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_DERIVATIVEMARKET'].fields_by_name['min_quantity_tick_size']._loaded_options = None
  _globals['_DERIVATIVEMARKET'].fields_by_name['min_quantity_tick_size']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_DERIVATIVEMARKET'].fields_by_name['min_notional']._loaded_options = None
  _globals['_DERIVATIVEMARKET'].fields_by_name['min_notional']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_DERIVATIVEMARKET'].fields_by_name['reduce_margin_ratio']._loaded_options = None
  _globals['_DERIVATIVEMARKET'].fields_by_name['reduce_margin_ratio']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_DERIVATIVEMARKET']._loaded_options = None
  _globals['_DERIVATIVEMARKET']._serialized_options = b'\210\240\037\000'
  _globals['_DERIVATIVEMARKETSETTLEMENTINFO'].fields_by_name['settlement_price']._loaded_options = None
  _globals['_DERIVATIVEMARKETSETTLEMENTINFO'].fields_by_name['settlement_price']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_MARKETVOLUME'].fields_by_name['volume']._loaded_options = None
  _globals['_MARKETVOLUME'].fields_by_name['volume']._serialized_options = b'\310\336\037\000'
  _globals['_VOLUMERECORD'].fields_by_name['maker_volume']._loaded_options = None
  _globals['_VOLUMERECORD'].fields_by_name['maker_volume']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_VOLUMERECORD'].fields_by_name['taker_volume']._loaded_options = None
  _globals['_VOLUMERECORD'].fields_by_name['taker_volume']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_EXPIRYFUTURESMARKETINFO'].fields_by_name['expiration_twap_start_price_cumulative']._loaded_options = None
  _globals['_EXPIRYFUTURESMARKETINFO'].fields_by_name['expiration_twap_start_price_cumulative']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_EXPIRYFUTURESMARKETINFO'].fields_by_name['settlement_price']._loaded_options = None
  _globals['_EXPIRYFUTURESMARKETINFO'].fields_by_name['settlement_price']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_PERPETUALMARKETINFO'].fields_by_name['hourly_funding_rate_cap']._loaded_options = None
  _globals['_PERPETUALMARKETINFO'].fields_by_name['hourly_funding_rate_cap']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_PERPETUALMARKETINFO'].fields_by_name['hourly_interest_rate']._loaded_options = None
  _globals['_PERPETUALMARKETINFO'].fields_by_name['hourly_interest_rate']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_PERPETUALMARKETFUNDING'].fields_by_name['cumulative_funding']._loaded_options = None
  _globals['_PERPETUALMARKETFUNDING'].fields_by_name['cumulative_funding']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_PERPETUALMARKETFUNDING'].fields_by_name['cumulative_price']._loaded_options = None
  _globals['_PERPETUALMARKETFUNDING'].fields_by_name['cumulative_price']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_MARKETSTATUS']._serialized_start=5093
  _globals['_MARKETSTATUS']._serialized_end=5177
  _globals['_MARKETFEEMULTIPLIER']._serialized_start=123
  _globals['_MARKETFEEMULTIPLIER']._serialized_end=255
  _globals['_SPOTMARKET']._serialized_start=258
  _globals['_SPOTMARKET']._serialized_end=1077
  _globals['_BINARYOPTIONSMARKET']._serialized_start=1080
  _globals['_BINARYOPTIONSMARKET']._serialized_end=2225
  _globals['_DERIVATIVEMARKET']._serialized_start=2228
  _globals['_DERIVATIVEMARKET']._serialized_end=3479
  _globals['_DERIVATIVEMARKETSETTLEMENTINFO']._serialized_start=3482
  _globals['_DERIVATIVEMARKETSETTLEMENTINFO']._serialized_end=3623
  _globals['_MARKETVOLUME']._serialized_start=3625
  _globals['_MARKETVOLUME']._serialized_end=3735
  _globals['_VOLUMERECORD']._serialized_start=3738
  _globals['_VOLUMERECORD']._serialized_end=3896
  _globals['_EXPIRYFUTURESMARKETINFOSTATE']._serialized_start=3899
  _globals['_EXPIRYFUTURESMARKETINFOSTATE']._serialized_end=4039
  _globals['_PERPETUALMARKETFUNDINGSTATE']._serialized_start=4042
  _globals['_PERPETUALMARKETFUNDINGSTATE']._serialized_end=4173
  _globals['_EXPIRYFUTURESMARKETINFO']._serialized_start=4176
  _globals['_EXPIRYFUTURESMARKETINFO']._serialized_end=4532
  _globals['_PERPETUALMARKETINFO']._serialized_start=4535
  _globals['_PERPETUALMARKETINFO']._serialized_end=4861
  _globals['_PERPETUALMARKETFUNDING']._serialized_start=4864
  _globals['_PERPETUALMARKETFUNDING']._serialized_end=5091
# @@protoc_insertion_point(module_scope)
