# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/permissions/v1beta1/genesis.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from injective.permissions.v1beta1 import params_pb2 as injective_dot_permissions_dot_v1beta1_dot_params__pb2
from injective.permissions.v1beta1 import permissions_pb2 as injective_dot_permissions_dot_v1beta1_dot_permissions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+injective/permissions/v1beta1/genesis.proto\x12\x1dinjective.permissions.v1beta1\x1a\x14gogoproto/gogo.proto\x1a*injective/permissions/v1beta1/params.proto\x1a/injective/permissions/v1beta1/permissions.proto\"\x8f\x01\n\x0cGenesisState\x12;\n\x06params\x18\x01 \x01(\x0b\x32%.injective.permissions.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12\x42\n\nnamespaces\x18\x02 \x03(\x0b\x32(.injective.permissions.v1beta1.NamespaceB\x04\xc8\xde\x1f\x00\x42SZQgithub.com/InjectiveLabs/injective-core/injective-chain/modules/permissions/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.permissions.v1beta1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZQgithub.com/InjectiveLabs/injective-core/injective-chain/modules/permissions/types'
  _globals['_GENESISSTATE'].fields_by_name['params']._options = None
  _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['namespaces']._options = None
  _globals['_GENESISSTATE'].fields_by_name['namespaces']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE']._serialized_start=194
  _globals['_GENESISSTATE']._serialized_end=337
# @@protoc_insertion_point(module_scope)
