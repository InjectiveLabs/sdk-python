# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/permissions/v1beta1/query.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from injective.permissions.v1beta1 import params_pb2 as injective_dot_permissions_dot_v1beta1_dot_params__pb2
from injective.permissions.v1beta1 import genesis_pb2 as injective_dot_permissions_dot_v1beta1_dot_genesis__pb2
from injective.permissions.v1beta1 import permissions_pb2 as injective_dot_permissions_dot_v1beta1_dot_permissions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)injective/permissions/v1beta1/query.proto\x12\x1dinjective.permissions.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a*injective/permissions/v1beta1/params.proto\x1a+injective/permissions/v1beta1/genesis.proto\x1a/injective/permissions/v1beta1/permissions.proto\"\x14\n\x12QueryParamsRequest\"R\n\x13QueryParamsResponse\x12;\n\x06params\x18\x01 \x01(\x0b\x32%.injective.permissions.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\"\x1b\n\x19QueryAllNamespacesRequest\"Z\n\x1aQueryAllNamespacesResponse\x12<\n\nnamespaces\x18\x01 \x03(\x0b\x32(.injective.permissions.v1beta1.Namespace\"D\n\x1cQueryNamespaceByDenomRequest\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\x12\x15\n\rinclude_roles\x18\x02 \x01(\x08\"\\\n\x1dQueryNamespaceByDenomResponse\x12;\n\tnamespace\x18\x01 \x01(\x0b\x32(.injective.permissions.v1beta1.Namespace\":\n\x1bQueryAddressesByRoleRequest\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\x12\x0c\n\x04role\x18\x02 \x01(\t\"1\n\x1cQueryAddressesByRoleResponse\x12\x11\n\taddresses\x18\x01 \x03(\t\":\n\x18QueryAddressRolesRequest\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\"*\n\x19QueryAddressRolesResponse\x12\r\n\x05roles\x18\x01 \x03(\t\"1\n\x1eQueryVouchersForAddressRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"b\n\x1fQueryVouchersForAddressResponse\x12?\n\x08vouchers\x18\x01 \x03(\x0b\x32-.injective.permissions.v1beta1.AddressVoucher2\x89\t\n\x05Query\x12\x9e\x01\n\x06Params\x12\x31.injective.permissions.v1beta1.QueryParamsRequest\x1a\x32.injective.permissions.v1beta1.QueryParamsResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/injective/permissions/v1beta1/params\x12\xbb\x01\n\rAllNamespaces\x12\x38.injective.permissions.v1beta1.QueryAllNamespacesRequest\x1a\x39.injective.permissions.v1beta1.QueryAllNamespacesResponse\"5\x82\xd3\xe4\x93\x02/\x12-/injective/permissions/v1beta1/all_namespaces\x12\xc8\x01\n\x10NamespaceByDenom\x12;.injective.permissions.v1beta1.QueryNamespaceByDenomRequest\x1a<.injective.permissions.v1beta1.QueryNamespaceByDenomResponse\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/injective/permissions/v1beta1/namespace_by_denom\x12\xbb\x01\n\x0c\x41\x64\x64ressRoles\x12\x37.injective.permissions.v1beta1.QueryAddressRolesRequest\x1a\x38.injective.permissions.v1beta1.QueryAddressRolesResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/injective/permissions/v1beta1/addresses_by_role\x12\xc4\x01\n\x0f\x41\x64\x64ressesByRole\x12:.injective.permissions.v1beta1.QueryAddressesByRoleRequest\x1a;.injective.permissions.v1beta1.QueryAddressesByRoleResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/injective/permissions/v1beta1/addresses_by_role\x12\xd0\x01\n\x12VouchersForAddress\x12=.injective.permissions.v1beta1.QueryVouchersForAddressRequest\x1a>.injective.permissions.v1beta1.QueryVouchersForAddressResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/injective/permissions/v1beta1/vouchers_for_addressBSZQgithub.com/InjectiveLabs/injective-core/injective-chain/modules/permissions/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.permissions.v1beta1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZQgithub.com/InjectiveLabs/injective-core/injective-chain/modules/permissions/types'
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._options = None
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_QUERY'].methods_by_name['Params']._options = None
  _globals['_QUERY'].methods_by_name['Params']._serialized_options = b'\202\323\344\223\002\'\022%/injective/permissions/v1beta1/params'
  _globals['_QUERY'].methods_by_name['AllNamespaces']._options = None
  _globals['_QUERY'].methods_by_name['AllNamespaces']._serialized_options = b'\202\323\344\223\002/\022-/injective/permissions/v1beta1/all_namespaces'
  _globals['_QUERY'].methods_by_name['NamespaceByDenom']._options = None
  _globals['_QUERY'].methods_by_name['NamespaceByDenom']._serialized_options = b'\202\323\344\223\0023\0221/injective/permissions/v1beta1/namespace_by_denom'
  _globals['_QUERY'].methods_by_name['AddressRoles']._options = None
  _globals['_QUERY'].methods_by_name['AddressRoles']._serialized_options = b'\202\323\344\223\0022\0220/injective/permissions/v1beta1/addresses_by_role'
  _globals['_QUERY'].methods_by_name['AddressesByRole']._options = None
  _globals['_QUERY'].methods_by_name['AddressesByRole']._serialized_options = b'\202\323\344\223\0022\0220/injective/permissions/v1beta1/addresses_by_role'
  _globals['_QUERY'].methods_by_name['VouchersForAddress']._options = None
  _globals['_QUERY'].methods_by_name['VouchersForAddress']._serialized_options = b'\202\323\344\223\0025\0223/injective/permissions/v1beta1/vouchers_for_address'
  _globals['_QUERYPARAMSREQUEST']._serialized_start=310
  _globals['_QUERYPARAMSREQUEST']._serialized_end=330
  _globals['_QUERYPARAMSRESPONSE']._serialized_start=332
  _globals['_QUERYPARAMSRESPONSE']._serialized_end=414
  _globals['_QUERYALLNAMESPACESREQUEST']._serialized_start=416
  _globals['_QUERYALLNAMESPACESREQUEST']._serialized_end=443
  _globals['_QUERYALLNAMESPACESRESPONSE']._serialized_start=445
  _globals['_QUERYALLNAMESPACESRESPONSE']._serialized_end=535
  _globals['_QUERYNAMESPACEBYDENOMREQUEST']._serialized_start=537
  _globals['_QUERYNAMESPACEBYDENOMREQUEST']._serialized_end=605
  _globals['_QUERYNAMESPACEBYDENOMRESPONSE']._serialized_start=607
  _globals['_QUERYNAMESPACEBYDENOMRESPONSE']._serialized_end=699
  _globals['_QUERYADDRESSESBYROLEREQUEST']._serialized_start=701
  _globals['_QUERYADDRESSESBYROLEREQUEST']._serialized_end=759
  _globals['_QUERYADDRESSESBYROLERESPONSE']._serialized_start=761
  _globals['_QUERYADDRESSESBYROLERESPONSE']._serialized_end=810
  _globals['_QUERYADDRESSROLESREQUEST']._serialized_start=812
  _globals['_QUERYADDRESSROLESREQUEST']._serialized_end=870
  _globals['_QUERYADDRESSROLESRESPONSE']._serialized_start=872
  _globals['_QUERYADDRESSROLESRESPONSE']._serialized_end=914
  _globals['_QUERYVOUCHERSFORADDRESSREQUEST']._serialized_start=916
  _globals['_QUERYVOUCHERSFORADDRESSREQUEST']._serialized_end=965
  _globals['_QUERYVOUCHERSFORADDRESSRESPONSE']._serialized_start=967
  _globals['_QUERYVOUCHERSFORADDRESSRESPONSE']._serialized_end=1065
  _globals['_QUERY']._serialized_start=1068
  _globals['_QUERY']._serialized_end=2229
# @@protoc_insertion_point(module_scope)
