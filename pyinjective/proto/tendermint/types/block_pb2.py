# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tendermint/types/block.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.tendermint.types import types_pb2 as tendermint_dot_types_dot_types__pb2
from pyinjective.proto.tendermint.types import evidence_pb2 as tendermint_dot_types_dot_evidence__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ctendermint/types/block.proto\x12\x10tendermint.types\x1a\x14gogoproto/gogo.proto\x1a\x1ctendermint/types/types.proto\x1a\x1ftendermint/types/evidence.proto\"\xee\x01\n\x05\x42lock\x12\x36\n\x06header\x18\x01 \x01(\x0b\x32\x18.tendermint.types.HeaderB\x04\xc8\xde\x1f\x00R\x06header\x12\x30\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x16.tendermint.types.DataB\x04\xc8\xde\x1f\x00R\x04\x64\x61ta\x12@\n\x08\x65vidence\x18\x03 \x01(\x0b\x32\x1e.tendermint.types.EvidenceListB\x04\xc8\xde\x1f\x00R\x08\x65vidence\x12\x39\n\x0blast_commit\x18\x04 \x01(\x0b\x32\x18.tendermint.types.CommitR\nlastCommitB\xb8\x01\n\x14\x63om.tendermint.typesB\nBlockProtoP\x01Z3github.com/cometbft/cometbft/proto/tendermint/types\xa2\x02\x03TTX\xaa\x02\x10Tendermint.Types\xca\x02\x10Tendermint\\Types\xe2\x02\x1cTendermint\\Types\\GPBMetadata\xea\x02\x11Tendermint::Typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tendermint.types.block_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.tendermint.typesB\nBlockProtoP\001Z3github.com/cometbft/cometbft/proto/tendermint/types\242\002\003TTX\252\002\020Tendermint.Types\312\002\020Tendermint\\Types\342\002\034Tendermint\\Types\\GPBMetadata\352\002\021Tendermint::Types'
  _globals['_BLOCK'].fields_by_name['header']._options = None
  _globals['_BLOCK'].fields_by_name['header']._serialized_options = b'\310\336\037\000'
  _globals['_BLOCK'].fields_by_name['data']._options = None
  _globals['_BLOCK'].fields_by_name['data']._serialized_options = b'\310\336\037\000'
  _globals['_BLOCK'].fields_by_name['evidence']._options = None
  _globals['_BLOCK'].fields_by_name['evidence']._serialized_options = b'\310\336\037\000'
  _globals['_BLOCK']._serialized_start=136
  _globals['_BLOCK']._serialized_end=374
# @@protoc_insertion_point(module_scope)
