# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/peggy/v1/pool.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dinjective/peggy/v1/pool.proto\x12\x12injective.peggy.v1\x1a\x14gogoproto/gogo.proto\"\x14\n\x05IDSet\x12\x0b\n\x03ids\x18\x01 \x03(\x04\"^\n\tBatchFees\x12\r\n\x05token\x18\x01 \x01(\t\x12\x42\n\ntotal_fees\x18\x02 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.IntBMZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.peggy.v1.pool_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/types'
  _globals['_BATCHFEES'].fields_by_name['total_fees']._options = None
  _globals['_BATCHFEES'].fields_by_name['total_fees']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int'
  _globals['_IDSET']._serialized_start=75
  _globals['_IDSET']._serialized_end=95
  _globals['_BATCHFEES']._serialized_start=97
  _globals['_BATCHFEES']._serialized_end=191
# @@protoc_insertion_point(module_scope)
