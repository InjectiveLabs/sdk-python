# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/authz/v1beta1/event.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/authz/v1beta1/event.proto\x12\x14\x63osmos.authz.v1beta1\x1a\x19\x63osmos_proto/cosmos.proto\"x\n\nEventGrant\x12\x14\n\x0cmsg_type_url\x18\x02 \x01(\t\x12)\n\x07granter\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12)\n\x07grantee\x18\x04 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\"y\n\x0b\x45ventRevoke\x12\x14\n\x0cmsg_type_url\x18\x02 \x01(\t\x12)\n\x07granter\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12)\n\x07grantee\x18\x04 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringB&Z$github.com/cosmos/cosmos-sdk/x/authzb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.authz.v1beta1.event_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z$github.com/cosmos/cosmos-sdk/x/authz'
  _EVENTGRANT.fields_by_name['granter']._options = None
  _EVENTGRANT.fields_by_name['granter']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _EVENTGRANT.fields_by_name['grantee']._options = None
  _EVENTGRANT.fields_by_name['grantee']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _EVENTREVOKE.fields_by_name['granter']._options = None
  _EVENTREVOKE.fields_by_name['granter']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _EVENTREVOKE.fields_by_name['grantee']._options = None
  _EVENTREVOKE.fields_by_name['grantee']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _EVENTGRANT._serialized_start=85
  _EVENTGRANT._serialized_end=205
  _EVENTREVOKE._serialized_start=207
  _EVENTREVOKE._serialized_end=328
# @@protoc_insertion_point(module_scope)
