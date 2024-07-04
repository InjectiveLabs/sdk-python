# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/permissions/v1beta1/permissions.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/injective/permissions/v1beta1/permissions.proto\x12\x1dinjective.permissions.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\xc9\x02\n\tNamespace\x12\x14\n\x05\x64\x65nom\x18\x01 \x01(\tR\x05\x64\x65nom\x12\x1b\n\twasm_hook\x18\x02 \x01(\tR\x08wasmHook\x12!\n\x0cmints_paused\x18\x03 \x01(\x08R\x0bmintsPaused\x12!\n\x0csends_paused\x18\x04 \x01(\x08R\x0bsendsPaused\x12!\n\x0c\x62urns_paused\x18\x05 \x01(\x08R\x0b\x62urnsPaused\x12N\n\x10role_permissions\x18\x06 \x03(\x0b\x32#.injective.permissions.v1beta1.RoleR\x0frolePermissions\x12P\n\raddress_roles\x18\x07 \x03(\x0b\x32+.injective.permissions.v1beta1.AddressRolesR\x0c\x61\x64\x64ressRoles\">\n\x0c\x41\x64\x64ressRoles\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\x12\x14\n\x05roles\x18\x02 \x03(\tR\x05roles\"<\n\x04Role\x12\x12\n\x04role\x18\x01 \x01(\tR\x04role\x12 \n\x0bpermissions\x18\x02 \x01(\rR\x0bpermissions\"$\n\x07RoleIDs\x12\x19\n\x08role_ids\x18\x01 \x03(\rR\x07roleIds\"l\n\x07Voucher\x12\x61\n\x05\x63oins\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.CoinsR\x05\x63oins\"l\n\x0e\x41\x64\x64ressVoucher\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\x12@\n\x07voucher\x18\x02 \x01(\x0b\x32&.injective.permissions.v1beta1.VoucherR\x07voucher*:\n\x06\x41\x63tion\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x08\n\x04MINT\x10\x01\x12\x0b\n\x07RECEIVE\x10\x02\x12\x08\n\x04\x42URN\x10\x04\x42\x9e\x02\n!com.injective.permissions.v1beta1B\x10PermissionsProtoP\x01ZQgithub.com/InjectiveLabs/injective-core/injective-chain/modules/permissions/types\xa2\x02\x03IPX\xaa\x02\x1dInjective.Permissions.V1beta1\xca\x02\x1dInjective\\Permissions\\V1beta1\xe2\x02)Injective\\Permissions\\V1beta1\\GPBMetadata\xea\x02\x1fInjective::Permissions::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.permissions.v1beta1.permissions_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!com.injective.permissions.v1beta1B\020PermissionsProtoP\001ZQgithub.com/InjectiveLabs/injective-core/injective-chain/modules/permissions/types\242\002\003IPX\252\002\035Injective.Permissions.V1beta1\312\002\035Injective\\Permissions\\V1beta1\342\002)Injective\\Permissions\\V1beta1\\GPBMetadata\352\002\037Injective::Permissions::V1beta1'
  _globals['_VOUCHER'].fields_by_name['coins']._options = None
  _globals['_VOUCHER'].fields_by_name['coins']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _globals['_ACTION']._serialized_start=852
  _globals['_ACTION']._serialized_end=910
  _globals['_NAMESPACE']._serialized_start=137
  _globals['_NAMESPACE']._serialized_end=466
  _globals['_ADDRESSROLES']._serialized_start=468
  _globals['_ADDRESSROLES']._serialized_end=530
  _globals['_ROLE']._serialized_start=532
  _globals['_ROLE']._serialized_end=592
  _globals['_ROLEIDS']._serialized_start=594
  _globals['_ROLEIDS']._serialized_end=630
  _globals['_VOUCHER']._serialized_start=632
  _globals['_VOUCHER']._serialized_end=740
  _globals['_ADDRESSVOUCHER']._serialized_start=742
  _globals['_ADDRESSVOUCHER']._serialized_end=850
# @@protoc_insertion_point(module_scope)
