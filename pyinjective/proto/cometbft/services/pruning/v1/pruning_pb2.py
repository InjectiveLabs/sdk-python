# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cometbft/services/pruning/v1/pruning.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*cometbft/services/pruning/v1/pruning.proto\x12\x1c\x63ometbft.services.pruning.v1\"5\n\x1bSetBlockRetainHeightRequest\x12\x16\n\x06height\x18\x01 \x01(\x04R\x06height\"\x1e\n\x1cSetBlockRetainHeightResponse\"\x1d\n\x1bGetBlockRetainHeightRequest\"\x8d\x01\n\x1cGetBlockRetainHeightResponse\x12*\n\x11\x61pp_retain_height\x18\x01 \x01(\x04R\x0f\x61ppRetainHeight\x12\x41\n\x1dpruning_service_retain_height\x18\x02 \x01(\x04R\x1apruningServiceRetainHeight\"<\n\"SetBlockResultsRetainHeightRequest\x12\x16\n\x06height\x18\x01 \x01(\x04R\x06height\"%\n#SetBlockResultsRetainHeightResponse\"$\n\"GetBlockResultsRetainHeightRequest\"h\n#GetBlockResultsRetainHeightResponse\x12\x41\n\x1dpruning_service_retain_height\x18\x01 \x01(\x04R\x1apruningServiceRetainHeight\"9\n\x1fSetTxIndexerRetainHeightRequest\x12\x16\n\x06height\x18\x01 \x01(\x04R\x06height\"\"\n SetTxIndexerRetainHeightResponse\"!\n\x1fGetTxIndexerRetainHeightRequest\":\n GetTxIndexerRetainHeightResponse\x12\x16\n\x06height\x18\x01 \x01(\x04R\x06height\"<\n\"SetBlockIndexerRetainHeightRequest\x12\x16\n\x06height\x18\x01 \x01(\x04R\x06height\"%\n#SetBlockIndexerRetainHeightResponse\"$\n\"GetBlockIndexerRetainHeightRequest\"=\n#GetBlockIndexerRetainHeightResponse\x12\x16\n\x06height\x18\x01 \x01(\x04R\x06heightB\xc3\x01\n com.cometbft.services.pruning.v1B\x0cPruningProtoP\x01\xa2\x02\x03\x43SP\xaa\x02\x1c\x43ometbft.Services.Pruning.V1\xca\x02\x1c\x43ometbft\\Services\\Pruning\\V1\xe2\x02(Cometbft\\Services\\Pruning\\V1\\GPBMetadata\xea\x02\x1f\x43ometbft::Services::Pruning::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cometbft.services.pruning.v1.pruning_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.cometbft.services.pruning.v1B\014PruningProtoP\001\242\002\003CSP\252\002\034Cometbft.Services.Pruning.V1\312\002\034Cometbft\\Services\\Pruning\\V1\342\002(Cometbft\\Services\\Pruning\\V1\\GPBMetadata\352\002\037Cometbft::Services::Pruning::V1'
  _globals['_SETBLOCKRETAINHEIGHTREQUEST']._serialized_start=76
  _globals['_SETBLOCKRETAINHEIGHTREQUEST']._serialized_end=129
  _globals['_SETBLOCKRETAINHEIGHTRESPONSE']._serialized_start=131
  _globals['_SETBLOCKRETAINHEIGHTRESPONSE']._serialized_end=161
  _globals['_GETBLOCKRETAINHEIGHTREQUEST']._serialized_start=163
  _globals['_GETBLOCKRETAINHEIGHTREQUEST']._serialized_end=192
  _globals['_GETBLOCKRETAINHEIGHTRESPONSE']._serialized_start=195
  _globals['_GETBLOCKRETAINHEIGHTRESPONSE']._serialized_end=336
  _globals['_SETBLOCKRESULTSRETAINHEIGHTREQUEST']._serialized_start=338
  _globals['_SETBLOCKRESULTSRETAINHEIGHTREQUEST']._serialized_end=398
  _globals['_SETBLOCKRESULTSRETAINHEIGHTRESPONSE']._serialized_start=400
  _globals['_SETBLOCKRESULTSRETAINHEIGHTRESPONSE']._serialized_end=437
  _globals['_GETBLOCKRESULTSRETAINHEIGHTREQUEST']._serialized_start=439
  _globals['_GETBLOCKRESULTSRETAINHEIGHTREQUEST']._serialized_end=475
  _globals['_GETBLOCKRESULTSRETAINHEIGHTRESPONSE']._serialized_start=477
  _globals['_GETBLOCKRESULTSRETAINHEIGHTRESPONSE']._serialized_end=581
  _globals['_SETTXINDEXERRETAINHEIGHTREQUEST']._serialized_start=583
  _globals['_SETTXINDEXERRETAINHEIGHTREQUEST']._serialized_end=640
  _globals['_SETTXINDEXERRETAINHEIGHTRESPONSE']._serialized_start=642
  _globals['_SETTXINDEXERRETAINHEIGHTRESPONSE']._serialized_end=676
  _globals['_GETTXINDEXERRETAINHEIGHTREQUEST']._serialized_start=678
  _globals['_GETTXINDEXERRETAINHEIGHTREQUEST']._serialized_end=711
  _globals['_GETTXINDEXERRETAINHEIGHTRESPONSE']._serialized_start=713
  _globals['_GETTXINDEXERRETAINHEIGHTRESPONSE']._serialized_end=771
  _globals['_SETBLOCKINDEXERRETAINHEIGHTREQUEST']._serialized_start=773
  _globals['_SETBLOCKINDEXERRETAINHEIGHTREQUEST']._serialized_end=833
  _globals['_SETBLOCKINDEXERRETAINHEIGHTRESPONSE']._serialized_start=835
  _globals['_SETBLOCKINDEXERRETAINHEIGHTRESPONSE']._serialized_end=872
  _globals['_GETBLOCKINDEXERRETAINHEIGHTREQUEST']._serialized_start=874
  _globals['_GETBLOCKINDEXERRETAINHEIGHTREQUEST']._serialized_end=910
  _globals['_GETBLOCKINDEXERRETAINHEIGHTRESPONSE']._serialized_start=912
  _globals['_GETBLOCKINDEXERRETAINHEIGHTRESPONSE']._serialized_end=973
# @@protoc_insertion_point(module_scope)
