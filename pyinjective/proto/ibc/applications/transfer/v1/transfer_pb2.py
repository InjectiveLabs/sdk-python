# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/transfer/v1/transfer.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+ibc/applications/transfer/v1/transfer.proto\x12\x1cibc.applications.transfer.v1\x1a\x14gogoproto/gogo.proto\".\n\nDenomTrace\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x12\n\nbase_denom\x18\x02 \x01(\t\"l\n\x06Params\x12-\n\x0csend_enabled\x18\x01 \x01(\x08\x42\x17\xf2\xde\x1f\x13yaml:\"send_enabled\"\x12\x33\n\x0freceive_enabled\x18\x02 \x01(\x08\x42\x1a\xf2\xde\x1f\x16yaml:\"receive_enabled\"B9Z7github.com/cosmos/ibc-go/v7/modules/apps/transfer/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.transfer.v1.transfer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/cosmos/ibc-go/v7/modules/apps/transfer/types'
  _globals['_PARAMS'].fields_by_name['send_enabled']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['send_enabled']._serialized_options = b'\362\336\037\023yaml:\"send_enabled\"'
  _globals['_PARAMS'].fields_by_name['receive_enabled']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['receive_enabled']._serialized_options = b'\362\336\037\026yaml:\"receive_enabled\"'
  _globals['_DENOMTRACE']._serialized_start=99
  _globals['_DENOMTRACE']._serialized_end=145
  _globals['_PARAMS']._serialized_start=147
  _globals['_PARAMS']._serialized_end=255
# @@protoc_insertion_point(module_scope)
