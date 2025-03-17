# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exchange/injective_chart_rpc.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"exchange/injective_chart_rpc.proto\x12\x13injective_chart_rpc\"\xb1\x01\n\x18SpotMarketHistoryRequest\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12\x1b\n\tmarket_id\x18\x02 \x01(\tR\x08marketId\x12\x1e\n\nresolution\x18\x03 \x01(\tR\nresolution\x12\x12\n\x04\x66rom\x18\x04 \x01(\x11R\x04\x66rom\x12\x0e\n\x02to\x18\x05 \x01(\x11R\x02to\x12\x1c\n\tcountback\x18\x06 \x01(\x11R\tcountback\"}\n\x19SpotMarketHistoryResponse\x12\x0c\n\x01t\x18\x01 \x03(\x11R\x01t\x12\x0c\n\x01o\x18\x02 \x03(\x01R\x01o\x12\x0c\n\x01h\x18\x03 \x03(\x01R\x01h\x12\x0c\n\x01l\x18\x04 \x03(\x01R\x01l\x12\x0c\n\x01\x63\x18\x05 \x03(\x01R\x01\x63\x12\x0c\n\x01v\x18\x06 \x03(\x01R\x01v\x12\x0c\n\x01s\x18\x07 \x01(\tR\x01s\"\xb7\x01\n\x1e\x44\x65rivativeMarketHistoryRequest\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12\x1b\n\tmarket_id\x18\x02 \x01(\tR\x08marketId\x12\x1e\n\nresolution\x18\x03 \x01(\tR\nresolution\x12\x12\n\x04\x66rom\x18\x04 \x01(\x11R\x04\x66rom\x12\x0e\n\x02to\x18\x05 \x01(\x11R\x02to\x12\x1c\n\tcountback\x18\x06 \x01(\x11R\tcountback\"\x83\x01\n\x1f\x44\x65rivativeMarketHistoryResponse\x12\x0c\n\x01t\x18\x01 \x03(\x11R\x01t\x12\x0c\n\x01o\x18\x02 \x03(\x01R\x01o\x12\x0c\n\x01h\x18\x03 \x03(\x01R\x01h\x12\x0c\n\x01l\x18\x04 \x03(\x01R\x01l\x12\x0c\n\x01\x63\x18\x05 \x03(\x01R\x01\x63\x12\x0c\n\x01v\x18\x06 \x03(\x01R\x01v\x12\x0c\n\x01s\x18\x07 \x01(\tR\x01s\"W\n\x18SpotMarketSummaryRequest\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12\x1e\n\nresolution\x18\x02 \x01(\tR\nresolution\"\xb8\x01\n\x19SpotMarketSummaryResponse\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12\x12\n\x04open\x18\x02 \x01(\x01R\x04open\x12\x12\n\x04high\x18\x03 \x01(\x01R\x04high\x12\x10\n\x03low\x18\x04 \x01(\x01R\x03low\x12\x16\n\x06volume\x18\x05 \x01(\x01R\x06volume\x12\x14\n\x05price\x18\x06 \x01(\x01R\x05price\x12\x16\n\x06\x63hange\x18\x07 \x01(\x01R\x06\x63hange\"=\n\x1b\x41llSpotMarketSummaryRequest\x12\x1e\n\nresolution\x18\x01 \x01(\tR\nresolution\"\\\n\x1c\x41llSpotMarketSummaryResponse\x12<\n\x05\x66ield\x18\x01 \x03(\x0b\x32&.injective_chart_rpc.MarketSummaryRespR\x05\x66ield\"\xb0\x01\n\x11MarketSummaryResp\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12\x12\n\x04open\x18\x02 \x01(\x01R\x04open\x12\x12\n\x04high\x18\x03 \x01(\x01R\x04high\x12\x10\n\x03low\x18\x04 \x01(\x01R\x03low\x12\x16\n\x06volume\x18\x05 \x01(\x01R\x06volume\x12\x14\n\x05price\x18\x06 \x01(\x01R\x05price\x12\x16\n\x06\x63hange\x18\x07 \x01(\x01R\x06\x63hange\"~\n\x1e\x44\x65rivativeMarketSummaryRequest\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12\x1f\n\x0bindex_price\x18\x02 \x01(\x08R\nindexPrice\x12\x1e\n\nresolution\x18\x03 \x01(\tR\nresolution\"\xbe\x01\n\x1f\x44\x65rivativeMarketSummaryResponse\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12\x12\n\x04open\x18\x02 \x01(\x01R\x04open\x12\x12\n\x04high\x18\x03 \x01(\x01R\x04high\x12\x10\n\x03low\x18\x04 \x01(\x01R\x03low\x12\x16\n\x06volume\x18\x05 \x01(\x01R\x06volume\x12\x14\n\x05price\x18\x06 \x01(\x01R\x05price\x12\x16\n\x06\x63hange\x18\x07 \x01(\x01R\x06\x63hange\"C\n!AllDerivativeMarketSummaryRequest\x12\x1e\n\nresolution\x18\x01 \x01(\tR\nresolution\"b\n\"AllDerivativeMarketSummaryResponse\x12<\n\x05\x66ield\x18\x01 \x03(\x0b\x32&.injective_chart_rpc.MarketSummaryRespR\x05\x66ield2\x96\x06\n\x11InjectiveChartRPC\x12r\n\x11SpotMarketHistory\x12-.injective_chart_rpc.SpotMarketHistoryRequest\x1a..injective_chart_rpc.SpotMarketHistoryResponse\x12\x84\x01\n\x17\x44\x65rivativeMarketHistory\x12\x33.injective_chart_rpc.DerivativeMarketHistoryRequest\x1a\x34.injective_chart_rpc.DerivativeMarketHistoryResponse\x12r\n\x11SpotMarketSummary\x12-.injective_chart_rpc.SpotMarketSummaryRequest\x1a..injective_chart_rpc.SpotMarketSummaryResponse\x12{\n\x14\x41llSpotMarketSummary\x12\x30.injective_chart_rpc.AllSpotMarketSummaryRequest\x1a\x31.injective_chart_rpc.AllSpotMarketSummaryResponse\x12\x84\x01\n\x17\x44\x65rivativeMarketSummary\x12\x33.injective_chart_rpc.DerivativeMarketSummaryRequest\x1a\x34.injective_chart_rpc.DerivativeMarketSummaryResponse\x12\x8d\x01\n\x1a\x41llDerivativeMarketSummary\x12\x36.injective_chart_rpc.AllDerivativeMarketSummaryRequest\x1a\x37.injective_chart_rpc.AllDerivativeMarketSummaryResponseB\xad\x01\n\x17\x63om.injective_chart_rpcB\x16InjectiveChartRpcProtoP\x01Z\x16/injective_chart_rpcpb\xa2\x02\x03IXX\xaa\x02\x11InjectiveChartRpc\xca\x02\x11InjectiveChartRpc\xe2\x02\x1dInjectiveChartRpc\\GPBMetadata\xea\x02\x11InjectiveChartRpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exchange.injective_chart_rpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027com.injective_chart_rpcB\026InjectiveChartRpcProtoP\001Z\026/injective_chart_rpcpb\242\002\003IXX\252\002\021InjectiveChartRpc\312\002\021InjectiveChartRpc\342\002\035InjectiveChartRpc\\GPBMetadata\352\002\021InjectiveChartRpc'
  _globals['_SPOTMARKETHISTORYREQUEST']._serialized_start=60
  _globals['_SPOTMARKETHISTORYREQUEST']._serialized_end=237
  _globals['_SPOTMARKETHISTORYRESPONSE']._serialized_start=239
  _globals['_SPOTMARKETHISTORYRESPONSE']._serialized_end=364
  _globals['_DERIVATIVEMARKETHISTORYREQUEST']._serialized_start=367
  _globals['_DERIVATIVEMARKETHISTORYREQUEST']._serialized_end=550
  _globals['_DERIVATIVEMARKETHISTORYRESPONSE']._serialized_start=553
  _globals['_DERIVATIVEMARKETHISTORYRESPONSE']._serialized_end=684
  _globals['_SPOTMARKETSUMMARYREQUEST']._serialized_start=686
  _globals['_SPOTMARKETSUMMARYREQUEST']._serialized_end=773
  _globals['_SPOTMARKETSUMMARYRESPONSE']._serialized_start=776
  _globals['_SPOTMARKETSUMMARYRESPONSE']._serialized_end=960
  _globals['_ALLSPOTMARKETSUMMARYREQUEST']._serialized_start=962
  _globals['_ALLSPOTMARKETSUMMARYREQUEST']._serialized_end=1023
  _globals['_ALLSPOTMARKETSUMMARYRESPONSE']._serialized_start=1025
  _globals['_ALLSPOTMARKETSUMMARYRESPONSE']._serialized_end=1117
  _globals['_MARKETSUMMARYRESP']._serialized_start=1120
  _globals['_MARKETSUMMARYRESP']._serialized_end=1296
  _globals['_DERIVATIVEMARKETSUMMARYREQUEST']._serialized_start=1298
  _globals['_DERIVATIVEMARKETSUMMARYREQUEST']._serialized_end=1424
  _globals['_DERIVATIVEMARKETSUMMARYRESPONSE']._serialized_start=1427
  _globals['_DERIVATIVEMARKETSUMMARYRESPONSE']._serialized_end=1617
  _globals['_ALLDERIVATIVEMARKETSUMMARYREQUEST']._serialized_start=1619
  _globals['_ALLDERIVATIVEMARKETSUMMARYREQUEST']._serialized_end=1686
  _globals['_ALLDERIVATIVEMARKETSUMMARYRESPONSE']._serialized_start=1688
  _globals['_ALLDERIVATIVEMARKETSUMMARYRESPONSE']._serialized_end=1786
  _globals['_INJECTIVECHARTRPC']._serialized_start=1789
  _globals['_INJECTIVECHARTRPC']._serialized_end=2579
# @@protoc_insertion_point(module_scope)
