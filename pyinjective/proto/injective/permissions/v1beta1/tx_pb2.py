# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/permissions/v1beta1/tx.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from pyinjective.proto.cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2
from pyinjective.proto.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.injective.permissions.v1beta1 import params_pb2 as injective_dot_permissions_dot_v1beta1_dot_params__pb2
from pyinjective.proto.injective.permissions.v1beta1 import permissions_pb2 as injective_dot_permissions_dot_v1beta1_dot_permissions__pb2
from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&injective/permissions/v1beta1/tx.proto\x12\x1dinjective.permissions.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1e\x63osmos/bank/v1beta1/bank.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a*injective/permissions/v1beta1/params.proto\x1a/injective/permissions/v1beta1/permissions.proto\x1a\x11\x61mino/amino.proto\"\xbe\x01\n\x0fMsgUpdateParams\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12\x43\n\x06params\x18\x02 \x01(\x0b\x32%.injective.permissions.v1beta1.ParamsB\x04\xc8\xde\x1f\x00R\x06params:.\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x1bpermissions/MsgUpdateParams\"\x19\n\x17MsgUpdateParamsResponse\"\xbd\x01\n\x12MsgCreateNamespace\x12)\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"R\x06sender\x12L\n\tnamespace\x18\x02 \x01(\x0b\x32(.injective.permissions.v1beta1.NamespaceB\x04\xc8\xde\x1f\x00R\tnamespace:.\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x1epermissions/MsgCreateNamespace\"\x1c\n\x1aMsgCreateNamespaceResponse\"\x8c\x05\n\x12MsgUpdateNamespace\x12)\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"R\x06sender\x12\x14\n\x05\x64\x65nom\x18\x02 \x01(\tR\x05\x64\x65nom\x12\x66\n\rcontract_hook\x18\x03 \x01(\x0b\x32\x41.injective.permissions.v1beta1.MsgUpdateNamespace.SetContractHookR\x0c\x63ontractHook\x12N\n\x10role_permissions\x18\x04 \x03(\x0b\x32#.injective.permissions.v1beta1.RoleR\x0frolePermissions\x12O\n\rrole_managers\x18\x05 \x03(\x0b\x32*.injective.permissions.v1beta1.RoleManagerR\x0croleManagers\x12T\n\x0fpolicy_statuses\x18\x06 \x03(\x0b\x32+.injective.permissions.v1beta1.PolicyStatusR\x0epolicyStatuses\x12v\n\x1bpolicy_manager_capabilities\x18\x07 \x03(\x0b\x32\x36.injective.permissions.v1beta1.PolicyManagerCapabilityR\x19policyManagerCapabilities\x1a.\n\x0fSetContractHook\x12\x1b\n\tnew_value\x18\x01 \x01(\tR\x08newValue:.\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x1epermissions/MsgUpdateNamespace\"\x1c\n\x1aMsgUpdateNamespaceResponse\"\xbd\x02\n\x13MsgUpdateActorRoles\x12)\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"R\x06sender\x12\x14\n\x05\x64\x65nom\x18\x02 \x01(\tR\x05\x64\x65nom\x12V\n\x12role_actors_to_add\x18\x03 \x03(\x0b\x32).injective.permissions.v1beta1.RoleActorsR\x0froleActorsToAdd\x12\\\n\x15role_actors_to_revoke\x18\x05 \x03(\x0b\x32).injective.permissions.v1beta1.RoleActorsR\x12roleActorsToRevoke:/\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x1fpermissions/MsgUpdateActorRoles\"\x1d\n\x1bMsgUpdateActorRolesResponse\"\x7f\n\x0fMsgClaimVoucher\x12)\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"R\x06sender\x12\x14\n\x05\x64\x65nom\x18\x02 \x01(\tR\x05\x64\x65nom:+\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x1bpermissions/MsgClaimVoucher\"\x19\n\x17MsgClaimVoucherResponse2\x83\x05\n\x03Msg\x12v\n\x0cUpdateParams\x12..injective.permissions.v1beta1.MsgUpdateParams\x1a\x36.injective.permissions.v1beta1.MsgUpdateParamsResponse\x12\x7f\n\x0f\x43reateNamespace\x12\x31.injective.permissions.v1beta1.MsgCreateNamespace\x1a\x39.injective.permissions.v1beta1.MsgCreateNamespaceResponse\x12\x7f\n\x0fUpdateNamespace\x12\x31.injective.permissions.v1beta1.MsgUpdateNamespace\x1a\x39.injective.permissions.v1beta1.MsgUpdateNamespaceResponse\x12\x82\x01\n\x10UpdateActorRoles\x12\x32.injective.permissions.v1beta1.MsgUpdateActorRoles\x1a:.injective.permissions.v1beta1.MsgUpdateActorRolesResponse\x12v\n\x0c\x43laimVoucher\x12..injective.permissions.v1beta1.MsgClaimVoucher\x1a\x36.injective.permissions.v1beta1.MsgClaimVoucherResponse\x1a\x05\x80\xe7\xb0*\x01\x42\x95\x02\n!com.injective.permissions.v1beta1B\x07TxProtoP\x01ZQgithub.com/InjectiveLabs/injective-core/injective-chain/modules/permissions/types\xa2\x02\x03IPX\xaa\x02\x1dInjective.Permissions.V1beta1\xca\x02\x1dInjective\\Permissions\\V1beta1\xe2\x02)Injective\\Permissions\\V1beta1\\GPBMetadata\xea\x02\x1fInjective::Permissions::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.permissions.v1beta1.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!com.injective.permissions.v1beta1B\007TxProtoP\001ZQgithub.com/InjectiveLabs/injective-core/injective-chain/modules/permissions/types\242\002\003IPX\252\002\035Injective.Permissions.V1beta1\312\002\035Injective\\Permissions\\V1beta1\342\002)Injective\\Permissions\\V1beta1\\GPBMetadata\352\002\037Injective::Permissions::V1beta1'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_MSGUPDATEPARAMS']._loaded_options = None
  _globals['_MSGUPDATEPARAMS']._serialized_options = b'\202\347\260*\tauthority\212\347\260*\033permissions/MsgUpdateParams'
  _globals['_MSGCREATENAMESPACE'].fields_by_name['sender']._loaded_options = None
  _globals['_MSGCREATENAMESPACE'].fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _globals['_MSGCREATENAMESPACE'].fields_by_name['namespace']._loaded_options = None
  _globals['_MSGCREATENAMESPACE'].fields_by_name['namespace']._serialized_options = b'\310\336\037\000'
  _globals['_MSGCREATENAMESPACE']._loaded_options = None
  _globals['_MSGCREATENAMESPACE']._serialized_options = b'\202\347\260*\006sender\212\347\260*\036permissions/MsgCreateNamespace'
  _globals['_MSGUPDATENAMESPACE'].fields_by_name['sender']._loaded_options = None
  _globals['_MSGUPDATENAMESPACE'].fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _globals['_MSGUPDATENAMESPACE']._loaded_options = None
  _globals['_MSGUPDATENAMESPACE']._serialized_options = b'\202\347\260*\006sender\212\347\260*\036permissions/MsgUpdateNamespace'
  _globals['_MSGUPDATEACTORROLES'].fields_by_name['sender']._loaded_options = None
  _globals['_MSGUPDATEACTORROLES'].fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _globals['_MSGUPDATEACTORROLES']._loaded_options = None
  _globals['_MSGUPDATEACTORROLES']._serialized_options = b'\202\347\260*\006sender\212\347\260*\037permissions/MsgUpdateActorRoles'
  _globals['_MSGCLAIMVOUCHER'].fields_by_name['sender']._loaded_options = None
  _globals['_MSGCLAIMVOUCHER'].fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _globals['_MSGCLAIMVOUCHER']._loaded_options = None
  _globals['_MSGCLAIMVOUCHER']._serialized_options = b'\202\347\260*\006sender\212\347\260*\033permissions/MsgClaimVoucher'
  _globals['_MSG']._loaded_options = None
  _globals['_MSG']._serialized_options = b'\200\347\260*\001'
  _globals['_MSGUPDATEPARAMS']._serialized_start=324
  _globals['_MSGUPDATEPARAMS']._serialized_end=514
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start=516
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end=541
  _globals['_MSGCREATENAMESPACE']._serialized_start=544
  _globals['_MSGCREATENAMESPACE']._serialized_end=733
  _globals['_MSGCREATENAMESPACERESPONSE']._serialized_start=735
  _globals['_MSGCREATENAMESPACERESPONSE']._serialized_end=763
  _globals['_MSGUPDATENAMESPACE']._serialized_start=766
  _globals['_MSGUPDATENAMESPACE']._serialized_end=1418
  _globals['_MSGUPDATENAMESPACE_SETCONTRACTHOOK']._serialized_start=1324
  _globals['_MSGUPDATENAMESPACE_SETCONTRACTHOOK']._serialized_end=1370
  _globals['_MSGUPDATENAMESPACERESPONSE']._serialized_start=1420
  _globals['_MSGUPDATENAMESPACERESPONSE']._serialized_end=1448
  _globals['_MSGUPDATEACTORROLES']._serialized_start=1451
  _globals['_MSGUPDATEACTORROLES']._serialized_end=1768
  _globals['_MSGUPDATEACTORROLESRESPONSE']._serialized_start=1770
  _globals['_MSGUPDATEACTORROLESRESPONSE']._serialized_end=1799
  _globals['_MSGCLAIMVOUCHER']._serialized_start=1801
  _globals['_MSGCLAIMVOUCHER']._serialized_end=1928
  _globals['_MSGCLAIMVOUCHERRESPONSE']._serialized_start=1930
  _globals['_MSGCLAIMVOUCHERRESPONSE']._serialized_end=1955
  _globals['_MSG']._serialized_start=1958
  _globals['_MSG']._serialized_end=2601
# @@protoc_insertion_point(module_scope)
