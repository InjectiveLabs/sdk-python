# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/authz/v1beta1/query.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from pyinjective.proto.cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from pyinjective.proto.cosmos.authz.v1beta1 import authz_pb2 as cosmos_dot_authz_dot_v1beta1_dot_authz__pb2
from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/authz/v1beta1/query.proto\x12\x14\x63osmos.authz.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a cosmos/authz/v1beta1/authz.proto\x1a\x19\x63osmos_proto/cosmos.proto\"\xe6\x01\n\x12QueryGrantsRequest\x12\x32\n\x07granter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07granter\x12\x32\n\x07grantee\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07grantee\x12 \n\x0cmsg_type_url\x18\x03 \x01(\tR\nmsgTypeUrl\x12\x46\n\npagination\x18\x04 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\x93\x01\n\x13QueryGrantsResponse\x12\x33\n\x06grants\x18\x01 \x03(\x0b\x32\x1b.cosmos.authz.v1beta1.GrantR\x06grants\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"\x97\x01\n\x19QueryGranterGrantsRequest\x12\x32\n\x07granter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07granter\x12\x46\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\xa7\x01\n\x1aQueryGranterGrantsResponse\x12@\n\x06grants\x18\x01 \x03(\x0b\x32(.cosmos.authz.v1beta1.GrantAuthorizationR\x06grants\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"\x97\x01\n\x19QueryGranteeGrantsRequest\x12\x32\n\x07grantee\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07grantee\x12\x46\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\xa7\x01\n\x1aQueryGranteeGrantsResponse\x12@\n\x06grants\x18\x01 \x03(\x0b\x32(.cosmos.authz.v1beta1.GrantAuthorizationR\x06grants\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination2\xe7\x03\n\x05Query\x12\x83\x01\n\x06Grants\x12(.cosmos.authz.v1beta1.QueryGrantsRequest\x1a).cosmos.authz.v1beta1.QueryGrantsResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/cosmos/authz/v1beta1/grants\x12\xaa\x01\n\rGranterGrants\x12/.cosmos.authz.v1beta1.QueryGranterGrantsRequest\x1a\x30.cosmos.authz.v1beta1.QueryGranterGrantsResponse\"6\x82\xd3\xe4\x93\x02\x30\x12./cosmos/authz/v1beta1/grants/granter/{granter}\x12\xaa\x01\n\rGranteeGrants\x12/.cosmos.authz.v1beta1.QueryGranteeGrantsRequest\x1a\x30.cosmos.authz.v1beta1.QueryGranteeGrantsResponse\"6\x82\xd3\xe4\x93\x02\x30\x12./cosmos/authz/v1beta1/grants/grantee/{grantee}B\xbe\x01\n\x18\x63om.cosmos.authz.v1beta1B\nQueryProtoP\x01Z$github.com/cosmos/cosmos-sdk/x/authz\xa2\x02\x03\x43\x41X\xaa\x02\x14\x43osmos.Authz.V1beta1\xca\x02\x14\x43osmos\\Authz\\V1beta1\xe2\x02 Cosmos\\Authz\\V1beta1\\GPBMetadata\xea\x02\x16\x43osmos::Authz::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.authz.v1beta1.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.cosmos.authz.v1beta1B\nQueryProtoP\001Z$github.com/cosmos/cosmos-sdk/x/authz\242\002\003CAX\252\002\024Cosmos.Authz.V1beta1\312\002\024Cosmos\\Authz\\V1beta1\342\002 Cosmos\\Authz\\V1beta1\\GPBMetadata\352\002\026Cosmos::Authz::V1beta1'
  _globals['_QUERYGRANTSREQUEST'].fields_by_name['granter']._loaded_options = None
  _globals['_QUERYGRANTSREQUEST'].fields_by_name['granter']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERYGRANTSREQUEST'].fields_by_name['grantee']._loaded_options = None
  _globals['_QUERYGRANTSREQUEST'].fields_by_name['grantee']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERYGRANTERGRANTSREQUEST'].fields_by_name['granter']._loaded_options = None
  _globals['_QUERYGRANTERGRANTSREQUEST'].fields_by_name['granter']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERYGRANTEEGRANTSREQUEST'].fields_by_name['grantee']._loaded_options = None
  _globals['_QUERYGRANTEEGRANTSREQUEST'].fields_by_name['grantee']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERY'].methods_by_name['Grants']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Grants']._serialized_options = b'\202\323\344\223\002\036\022\034/cosmos/authz/v1beta1/grants'
  _globals['_QUERY'].methods_by_name['GranterGrants']._loaded_options = None
  _globals['_QUERY'].methods_by_name['GranterGrants']._serialized_options = b'\202\323\344\223\0020\022./cosmos/authz/v1beta1/grants/granter/{granter}'
  _globals['_QUERY'].methods_by_name['GranteeGrants']._loaded_options = None
  _globals['_QUERY'].methods_by_name['GranteeGrants']._serialized_options = b'\202\323\344\223\0020\022./cosmos/authz/v1beta1/grants/grantee/{grantee}'
  _globals['_QUERYGRANTSREQUEST']._serialized_start=194
  _globals['_QUERYGRANTSREQUEST']._serialized_end=424
  _globals['_QUERYGRANTSRESPONSE']._serialized_start=427
  _globals['_QUERYGRANTSRESPONSE']._serialized_end=574
  _globals['_QUERYGRANTERGRANTSREQUEST']._serialized_start=577
  _globals['_QUERYGRANTERGRANTSREQUEST']._serialized_end=728
  _globals['_QUERYGRANTERGRANTSRESPONSE']._serialized_start=731
  _globals['_QUERYGRANTERGRANTSRESPONSE']._serialized_end=898
  _globals['_QUERYGRANTEEGRANTSREQUEST']._serialized_start=901
  _globals['_QUERYGRANTEEGRANTSREQUEST']._serialized_end=1052
  _globals['_QUERYGRANTEEGRANTSRESPONSE']._serialized_start=1055
  _globals['_QUERYGRANTEEGRANTSRESPONSE']._serialized_end=1222
  _globals['_QUERY']._serialized_start=1225
  _globals['_QUERY']._serialized_end=1712
# @@protoc_insertion_point(module_scope)
