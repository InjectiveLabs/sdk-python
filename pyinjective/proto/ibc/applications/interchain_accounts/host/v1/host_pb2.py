# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/interchain_accounts/host/v1/host.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7ibc/applications/interchain_accounts/host/v1/host.proto\x12,ibc.applications.interchain_accounts.host.v1\x1a\x14gogoproto/gogo.proto\"\x86\x01\n\x06Params\x12:\n\x0chost_enabled\x18\x01 \x01(\x08\x42\x17\xf2\xde\x1f\x13yaml:\"host_enabled\"R\x0bhostEnabled\x12@\n\x0e\x61llow_messages\x18\x02 \x03(\tB\x19\xf2\xde\x1f\x15yaml:\"allow_messages\"R\rallowMessagesB\xda\x02\n0com.ibc.applications.interchain_accounts.host.v1B\tHostProtoP\x01ZJgithub.com/cosmos/ibc-go/v7/modules/apps/27-interchain-accounts/host/types\xa2\x02\x04IAIH\xaa\x02+Ibc.Applications.InterchainAccounts.Host.V1\xca\x02+Ibc\\Applications\\InterchainAccounts\\Host\\V1\xe2\x02\x37Ibc\\Applications\\InterchainAccounts\\Host\\V1\\GPBMetadata\xea\x02/Ibc::Applications::InterchainAccounts::Host::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.interchain_accounts.host.v1.host_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n0com.ibc.applications.interchain_accounts.host.v1B\tHostProtoP\001ZJgithub.com/cosmos/ibc-go/v7/modules/apps/27-interchain-accounts/host/types\242\002\004IAIH\252\002+Ibc.Applications.InterchainAccounts.Host.V1\312\002+Ibc\\Applications\\InterchainAccounts\\Host\\V1\342\0027Ibc\\Applications\\InterchainAccounts\\Host\\V1\\GPBMetadata\352\002/Ibc::Applications::InterchainAccounts::Host::V1'
  _globals['_PARAMS'].fields_by_name['host_enabled']._options = None
  _globals['_PARAMS'].fields_by_name['host_enabled']._serialized_options = b'\362\336\037\023yaml:\"host_enabled\"'
  _globals['_PARAMS'].fields_by_name['allow_messages']._options = None
  _globals['_PARAMS'].fields_by_name['allow_messages']._serialized_options = b'\362\336\037\025yaml:\"allow_messages\"'
  _globals['_PARAMS']._serialized_start=128
  _globals['_PARAMS']._serialized_end=262
# @@protoc_insertion_point(module_scope)
