# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exchange/injective_oracle_rpc.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#exchange/injective_oracle_rpc.proto\x12\x14injective_oracle_rpc\"\x13\n\x11OracleListRequest\"L\n\x12OracleListResponse\x12\x36\n\x07oracles\x18\x01 \x03(\x0b\x32\x1c.injective_oracle_rpc.OracleR\x07oracles\"\x9b\x01\n\x06Oracle\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12\x1f\n\x0b\x62\x61se_symbol\x18\x02 \x01(\tR\nbaseSymbol\x12!\n\x0cquote_symbol\x18\x03 \x01(\tR\x0bquoteSymbol\x12\x1f\n\x0boracle_type\x18\x04 \x01(\tR\noracleType\x12\x14\n\x05price\x18\x05 \x01(\tR\x05price\"\xa3\x01\n\x0cPriceRequest\x12\x1f\n\x0b\x62\x61se_symbol\x18\x01 \x01(\tR\nbaseSymbol\x12!\n\x0cquote_symbol\x18\x02 \x01(\tR\x0bquoteSymbol\x12\x1f\n\x0boracle_type\x18\x03 \x01(\tR\noracleType\x12.\n\x13oracle_scale_factor\x18\x04 \x01(\rR\x11oracleScaleFactor\"%\n\rPriceResponse\x12\x14\n\x05price\x18\x01 \x01(\tR\x05price\"P\n\x0ePriceV2Request\x12>\n\x07\x66ilters\x18\x01 \x03(\x0b\x32$.injective_oracle_rpc.PricePayloadV2R\x07\x66ilters\"\xa5\x01\n\x0ePricePayloadV2\x12\x1f\n\x0b\x62\x61se_symbol\x18\x01 \x01(\tR\nbaseSymbol\x12!\n\x0cquote_symbol\x18\x02 \x01(\tR\x0bquoteSymbol\x12\x1f\n\x0boracle_type\x18\x03 \x01(\tR\noracleType\x12.\n\x13oracle_scale_factor\x18\x04 \x01(\rR\x11oracleScaleFactor\"N\n\x0fPriceV2Response\x12;\n\x06prices\x18\x01 \x03(\x0b\x32#.injective_oracle_rpc.PriceV2ResultR\x06prices\"\xd7\x01\n\rPriceV2Result\x12\x1f\n\x0b\x62\x61se_symbol\x18\x01 \x01(\tR\nbaseSymbol\x12!\n\x0cquote_symbol\x18\x02 \x01(\tR\x0bquoteSymbol\x12\x1f\n\x0boracle_type\x18\x03 \x01(\tR\noracleType\x12.\n\x13oracle_scale_factor\x18\x04 \x01(\rR\x11oracleScaleFactor\x12\x14\n\x05price\x18\x05 \x01(\tR\x05price\x12\x1b\n\tmarket_id\x18\x06 \x01(\tR\x08marketId\"z\n\x13StreamPricesRequest\x12\x1f\n\x0b\x62\x61se_symbol\x18\x01 \x01(\tR\nbaseSymbol\x12!\n\x0cquote_symbol\x18\x02 \x01(\tR\x0bquoteSymbol\x12\x1f\n\x0boracle_type\x18\x03 \x01(\tR\noracleType\"J\n\x14StreamPricesResponse\x12\x14\n\x05price\x18\x01 \x01(\tR\x05price\x12\x1c\n\ttimestamp\x18\x02 \x01(\x12R\ttimestamp\"=\n\x1cStreamPricesByMarketsRequest\x12\x1d\n\nmarket_ids\x18\x01 \x03(\tR\tmarketIds\"p\n\x1dStreamPricesByMarketsResponse\x12\x14\n\x05price\x18\x01 \x01(\tR\x05price\x12\x1c\n\ttimestamp\x18\x02 \x01(\x12R\ttimestamp\x12\x1b\n\tmarket_id\x18\x03 \x01(\tR\x08marketId2\x8d\x04\n\x12InjectiveOracleRPC\x12_\n\nOracleList\x12\'.injective_oracle_rpc.OracleListRequest\x1a(.injective_oracle_rpc.OracleListResponse\x12P\n\x05Price\x12\".injective_oracle_rpc.PriceRequest\x1a#.injective_oracle_rpc.PriceResponse\x12V\n\x07PriceV2\x12$.injective_oracle_rpc.PriceV2Request\x1a%.injective_oracle_rpc.PriceV2Response\x12g\n\x0cStreamPrices\x12).injective_oracle_rpc.StreamPricesRequest\x1a*.injective_oracle_rpc.StreamPricesResponse0\x01\x12\x82\x01\n\x15StreamPricesByMarkets\x12\x32.injective_oracle_rpc.StreamPricesByMarketsRequest\x1a\x33.injective_oracle_rpc.StreamPricesByMarketsResponse0\x01\x42\xb4\x01\n\x18\x63om.injective_oracle_rpcB\x17InjectiveOracleRpcProtoP\x01Z\x17/injective_oracle_rpcpb\xa2\x02\x03IXX\xaa\x02\x12InjectiveOracleRpc\xca\x02\x12InjectiveOracleRpc\xe2\x02\x1eInjectiveOracleRpc\\GPBMetadata\xea\x02\x12InjectiveOracleRpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exchange.injective_oracle_rpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.injective_oracle_rpcB\027InjectiveOracleRpcProtoP\001Z\027/injective_oracle_rpcpb\242\002\003IXX\252\002\022InjectiveOracleRpc\312\002\022InjectiveOracleRpc\342\002\036InjectiveOracleRpc\\GPBMetadata\352\002\022InjectiveOracleRpc'
  _globals['_ORACLELISTREQUEST']._serialized_start=61
  _globals['_ORACLELISTREQUEST']._serialized_end=80
  _globals['_ORACLELISTRESPONSE']._serialized_start=82
  _globals['_ORACLELISTRESPONSE']._serialized_end=158
  _globals['_ORACLE']._serialized_start=161
  _globals['_ORACLE']._serialized_end=316
  _globals['_PRICEREQUEST']._serialized_start=319
  _globals['_PRICEREQUEST']._serialized_end=482
  _globals['_PRICERESPONSE']._serialized_start=484
  _globals['_PRICERESPONSE']._serialized_end=521
  _globals['_PRICEV2REQUEST']._serialized_start=523
  _globals['_PRICEV2REQUEST']._serialized_end=603
  _globals['_PRICEPAYLOADV2']._serialized_start=606
  _globals['_PRICEPAYLOADV2']._serialized_end=771
  _globals['_PRICEV2RESPONSE']._serialized_start=773
  _globals['_PRICEV2RESPONSE']._serialized_end=851
  _globals['_PRICEV2RESULT']._serialized_start=854
  _globals['_PRICEV2RESULT']._serialized_end=1069
  _globals['_STREAMPRICESREQUEST']._serialized_start=1071
  _globals['_STREAMPRICESREQUEST']._serialized_end=1193
  _globals['_STREAMPRICESRESPONSE']._serialized_start=1195
  _globals['_STREAMPRICESRESPONSE']._serialized_end=1269
  _globals['_STREAMPRICESBYMARKETSREQUEST']._serialized_start=1271
  _globals['_STREAMPRICESBYMARKETSREQUEST']._serialized_end=1332
  _globals['_STREAMPRICESBYMARKETSRESPONSE']._serialized_start=1334
  _globals['_STREAMPRICESBYMARKETSRESPONSE']._serialized_end=1446
  _globals['_INJECTIVEORACLERPC']._serialized_start=1449
  _globals['_INJECTIVEORACLERPC']._serialized_end=1974
# @@protoc_insertion_point(module_scope)
