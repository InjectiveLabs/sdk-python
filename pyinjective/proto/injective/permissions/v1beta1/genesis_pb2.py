# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/permissions/v1beta1/genesis.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.injective.permissions.v1beta1 import params_pb2 as injective_dot_permissions_dot_v1beta1_dot_params__pb2
from pyinjective.proto.injective.permissions.v1beta1 import permissions_pb2 as injective_dot_permissions_dot_v1beta1_dot_permissions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+injective/permissions/v1beta1/genesis.proto\x12\x1dinjective.permissions.v1beta1\x1a\x14gogoproto/gogo.proto\x1a*injective/permissions/v1beta1/params.proto\x1a/injective/permissions/v1beta1/permissions.proto\"\xee\x01\n\x0cGenesisState\x12\x43\n\x06params\x18\x01 \x01(\x0b\x32%.injective.permissions.v1beta1.ParamsB\x04\xc8\xde\x1f\x00R\x06params\x12N\n\nnamespaces\x18\x02 \x03(\x0b\x32(.injective.permissions.v1beta1.NamespaceB\x04\xc8\xde\x1f\x00R\nnamespaces\x12I\n\x08vouchers\x18\x03 \x03(\x0b\x32-.injective.permissions.v1beta1.AddressVoucherR\x08vouchersB\x9a\x02\n!com.injective.permissions.v1beta1B\x0cGenesisProtoP\x01ZQgithub.com/InjectiveLabs/injective-core/injective-chain/modules/permissions/types\xa2\x02\x03IPX\xaa\x02\x1dInjective.Permissions.V1beta1\xca\x02\x1dInjective\\Permissions\\V1beta1\xe2\x02)Injective\\Permissions\\V1beta1\\GPBMetadata\xea\x02\x1fInjective::Permissions::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.permissions.v1beta1.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!com.injective.permissions.v1beta1B\014GenesisProtoP\001ZQgithub.com/InjectiveLabs/injective-core/injective-chain/modules/permissions/types\242\002\003IPX\252\002\035Injective.Permissions.V1beta1\312\002\035Injective\\Permissions\\V1beta1\342\002)Injective\\Permissions\\V1beta1\\GPBMetadata\352\002\037Injective::Permissions::V1beta1'
  _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['namespaces']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['namespaces']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE']._serialized_start=194
  _globals['_GENESISSTATE']._serialized_end=432
# @@protoc_insertion_point(module_scope)
