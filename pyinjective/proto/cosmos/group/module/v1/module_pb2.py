# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/group/module/v1/module.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.cosmos.app.v1alpha1 import module_pb2 as cosmos_dot_app_dot_v1alpha1_dot_module__pb2
from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#cosmos/group/module/v1/module.proto\x12\x16\x63osmos.group.module.v1\x1a cosmos/app/v1alpha1/module.proto\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x11\x61mino/amino.proto\"\xbc\x01\n\x06Module\x12Z\n\x14max_execution_period\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\r\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xa8\xe7\xb0*\x01R\x12maxExecutionPeriod\x12(\n\x10max_metadata_len\x18\x02 \x01(\x04R\x0emaxMetadataLen:,\xba\xc0\x96\xda\x01&\n$github.com/cosmos/cosmos-sdk/x/groupB\xa4\x01\n\x1a\x63om.cosmos.group.module.v1B\x0bModuleProtoP\x01\xa2\x02\x03\x43GM\xaa\x02\x16\x43osmos.Group.Module.V1\xca\x02\x16\x43osmos\\Group\\Module\\V1\xe2\x02\"Cosmos\\Group\\Module\\V1\\GPBMetadata\xea\x02\x19\x43osmos::Group::Module::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.group.module.v1.module_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.cosmos.group.module.v1B\013ModuleProtoP\001\242\002\003CGM\252\002\026Cosmos.Group.Module.V1\312\002\026Cosmos\\Group\\Module\\V1\342\002\"Cosmos\\Group\\Module\\V1\\GPBMetadata\352\002\031Cosmos::Group::Module::V1'
  _globals['_MODULE'].fields_by_name['max_execution_period']._options = None
  _globals['_MODULE'].fields_by_name['max_execution_period']._serialized_options = b'\310\336\037\000\230\337\037\001\250\347\260*\001'
  _globals['_MODULE']._options = None
  _globals['_MODULE']._serialized_options = b'\272\300\226\332\001&\n$github.com/cosmos/cosmos-sdk/x/group'
  _globals['_MODULE']._serialized_start=171
  _globals['_MODULE']._serialized_end=359
# @@protoc_insertion_point(module_scope)
