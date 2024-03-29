# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/permissions/v1beta1/tx.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2
from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from injective.permissions.v1beta1 import params_pb2 as injective_dot_permissions_dot_v1beta1_dot_params__pb2
from injective.permissions.v1beta1 import permissions_pb2 as injective_dot_permissions_dot_v1beta1_dot_permissions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&injective/permissions/v1beta1/tx.proto\x12\x1dinjective.permissions.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1e\x63osmos/bank/v1beta1/bank.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a*injective/permissions/v1beta1/params.proto\x1a/injective/permissions/v1beta1/permissions.proto\"\x8b\x01\n\x0fMsgUpdateParams\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12;\n\x06params\x18\x02 \x01(\x0b\x32%.injective.permissions.v1beta1.ParamsB\x04\xc8\xde\x1f\x00:\x0e\x82\xe7\xb0*\tauthority\"\x19\n\x17MsgUpdateParamsResponse\"\x87\x01\n\x12MsgCreateNamespace\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"\x12\x41\n\tnamespace\x18\x02 \x01(\x0b\x32(.injective.permissions.v1beta1.NamespaceB\x04\xc8\xde\x1f\x00:\x0b\x82\xe7\xb0*\x06sender\"\x1c\n\x1aMsgCreateNamespaceResponse\"]\n\x12MsgDeleteNamespace\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"\x12\x17\n\x0fnamespace_denom\x18\x02 \x01(\t:\x0b\x82\xe7\xb0*\x06sender\"\x1c\n\x1aMsgDeleteNamespaceResponse\"\xe0\x04\n\x12MsgUpdateNamespace\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"\x12\x17\n\x0fnamespace_denom\x18\x02 \x01(\t\x12S\n\twasm_hook\x18\x03 \x01(\x0b\x32@.injective.permissions.v1beta1.MsgUpdateNamespace.MsgSetWasmHook\x12Y\n\x0cmints_paused\x18\x04 \x01(\x0b\x32\x43.injective.permissions.v1beta1.MsgUpdateNamespace.MsgSetMintsPaused\x12Y\n\x0csends_paused\x18\x05 \x01(\x0b\x32\x43.injective.permissions.v1beta1.MsgUpdateNamespace.MsgSetSendsPaused\x12Y\n\x0c\x62urns_paused\x18\x06 \x01(\x0b\x32\x43.injective.permissions.v1beta1.MsgUpdateNamespace.MsgSetBurnsPaused\x1a#\n\x0eMsgSetWasmHook\x12\x11\n\tnew_value\x18\x01 \x01(\t\x1a&\n\x11MsgSetMintsPaused\x12\x11\n\tnew_value\x18\x01 \x01(\x08\x1a&\n\x11MsgSetSendsPaused\x12\x11\n\tnew_value\x18\x01 \x01(\x08\x1a&\n\x11MsgSetBurnsPaused\x12\x11\n\tnew_value\x18\x01 \x01(\x08:\x0b\x82\xe7\xb0*\x06sender\"\x1c\n\x1aMsgUpdateNamespaceResponse\"\xe5\x01\n\x17MsgUpdateNamespaceRoles\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"\x12\x17\n\x0fnamespace_denom\x18\x02 \x01(\t\x12=\n\x10role_permissions\x18\x03 \x03(\x0b\x32#.injective.permissions.v1beta1.Role\x12\x42\n\raddress_roles\x18\x04 \x03(\x0b\x32+.injective.permissions.v1beta1.AddressRoles:\x0b\x82\xe7\xb0*\x06sender\"!\n\x1fMsgUpdateNamespaceRolesResponse\"\xb0\x01\n\x17MsgRevokeNamespaceRoles\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"\x12\x17\n\x0fnamespace_denom\x18\x02 \x01(\t\x12L\n\x17\x61\x64\x64ress_roles_to_revoke\x18\x03 \x03(\x0b\x32+.injective.permissions.v1beta1.AddressRoles:\x0b\x82\xe7\xb0*\x06sender\"!\n\x1fMsgRevokeNamespaceRolesResponse\"U\n\x0fMsgClaimVoucher\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"\x12\x12\n\noriginator\x18\x02 \x01(\t:\x0b\x82\xe7\xb0*\x06sender\"\x19\n\x17MsgClaimVoucherResponse2\x9a\x07\n\x03Msg\x12v\n\x0cUpdateParams\x12..injective.permissions.v1beta1.MsgUpdateParams\x1a\x36.injective.permissions.v1beta1.MsgUpdateParamsResponse\x12\x7f\n\x0f\x43reateNamespace\x12\x31.injective.permissions.v1beta1.MsgCreateNamespace\x1a\x39.injective.permissions.v1beta1.MsgCreateNamespaceResponse\x12\x7f\n\x0f\x44\x65leteNamespace\x12\x31.injective.permissions.v1beta1.MsgDeleteNamespace\x1a\x39.injective.permissions.v1beta1.MsgDeleteNamespaceResponse\x12\x7f\n\x0fUpdateNamespace\x12\x31.injective.permissions.v1beta1.MsgUpdateNamespace\x1a\x39.injective.permissions.v1beta1.MsgUpdateNamespaceResponse\x12\x8e\x01\n\x14UpdateNamespaceRoles\x12\x36.injective.permissions.v1beta1.MsgUpdateNamespaceRoles\x1a>.injective.permissions.v1beta1.MsgUpdateNamespaceRolesResponse\x12\x8e\x01\n\x14RevokeNamespaceRoles\x12\x36.injective.permissions.v1beta1.MsgRevokeNamespaceRoles\x1a>.injective.permissions.v1beta1.MsgRevokeNamespaceRolesResponse\x12v\n\x0c\x43laimVoucher\x12..injective.permissions.v1beta1.MsgClaimVoucher\x1a\x36.injective.permissions.v1beta1.MsgClaimVoucherResponseBSZQgithub.com/InjectiveLabs/injective-core/injective-chain/modules/permissions/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.permissions.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZQgithub.com/InjectiveLabs/injective-core/injective-chain/modules/permissions/types'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_MSGUPDATEPARAMS']._options = None
  _globals['_MSGUPDATEPARAMS']._serialized_options = b'\202\347\260*\tauthority'
  _globals['_MSGCREATENAMESPACE'].fields_by_name['sender']._options = None
  _globals['_MSGCREATENAMESPACE'].fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _globals['_MSGCREATENAMESPACE'].fields_by_name['namespace']._options = None
  _globals['_MSGCREATENAMESPACE'].fields_by_name['namespace']._serialized_options = b'\310\336\037\000'
  _globals['_MSGCREATENAMESPACE']._options = None
  _globals['_MSGCREATENAMESPACE']._serialized_options = b'\202\347\260*\006sender'
  _globals['_MSGDELETENAMESPACE'].fields_by_name['sender']._options = None
  _globals['_MSGDELETENAMESPACE'].fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _globals['_MSGDELETENAMESPACE']._options = None
  _globals['_MSGDELETENAMESPACE']._serialized_options = b'\202\347\260*\006sender'
  _globals['_MSGUPDATENAMESPACE'].fields_by_name['sender']._options = None
  _globals['_MSGUPDATENAMESPACE'].fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _globals['_MSGUPDATENAMESPACE']._options = None
  _globals['_MSGUPDATENAMESPACE']._serialized_options = b'\202\347\260*\006sender'
  _globals['_MSGUPDATENAMESPACEROLES'].fields_by_name['sender']._options = None
  _globals['_MSGUPDATENAMESPACEROLES'].fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _globals['_MSGUPDATENAMESPACEROLES']._options = None
  _globals['_MSGUPDATENAMESPACEROLES']._serialized_options = b'\202\347\260*\006sender'
  _globals['_MSGREVOKENAMESPACEROLES'].fields_by_name['sender']._options = None
  _globals['_MSGREVOKENAMESPACEROLES'].fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _globals['_MSGREVOKENAMESPACEROLES']._options = None
  _globals['_MSGREVOKENAMESPACEROLES']._serialized_options = b'\202\347\260*\006sender'
  _globals['_MSGCLAIMVOUCHER'].fields_by_name['sender']._options = None
  _globals['_MSGCLAIMVOUCHER'].fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _globals['_MSGCLAIMVOUCHER']._options = None
  _globals['_MSGCLAIMVOUCHER']._serialized_options = b'\202\347\260*\006sender'
  _globals['_MSGUPDATEPARAMS']._serialized_start=305
  _globals['_MSGUPDATEPARAMS']._serialized_end=444
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start=446
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end=471
  _globals['_MSGCREATENAMESPACE']._serialized_start=474
  _globals['_MSGCREATENAMESPACE']._serialized_end=609
  _globals['_MSGCREATENAMESPACERESPONSE']._serialized_start=611
  _globals['_MSGCREATENAMESPACERESPONSE']._serialized_end=639
  _globals['_MSGDELETENAMESPACE']._serialized_start=641
  _globals['_MSGDELETENAMESPACE']._serialized_end=734
  _globals['_MSGDELETENAMESPACERESPONSE']._serialized_start=736
  _globals['_MSGDELETENAMESPACERESPONSE']._serialized_end=764
  _globals['_MSGUPDATENAMESPACE']._serialized_start=767
  _globals['_MSGUPDATENAMESPACE']._serialized_end=1375
  _globals['_MSGUPDATENAMESPACE_MSGSETWASMHOOK']._serialized_start=1207
  _globals['_MSGUPDATENAMESPACE_MSGSETWASMHOOK']._serialized_end=1242
  _globals['_MSGUPDATENAMESPACE_MSGSETMINTSPAUSED']._serialized_start=1244
  _globals['_MSGUPDATENAMESPACE_MSGSETMINTSPAUSED']._serialized_end=1282
  _globals['_MSGUPDATENAMESPACE_MSGSETSENDSPAUSED']._serialized_start=1284
  _globals['_MSGUPDATENAMESPACE_MSGSETSENDSPAUSED']._serialized_end=1322
  _globals['_MSGUPDATENAMESPACE_MSGSETBURNSPAUSED']._serialized_start=1324
  _globals['_MSGUPDATENAMESPACE_MSGSETBURNSPAUSED']._serialized_end=1362
  _globals['_MSGUPDATENAMESPACERESPONSE']._serialized_start=1377
  _globals['_MSGUPDATENAMESPACERESPONSE']._serialized_end=1405
  _globals['_MSGUPDATENAMESPACEROLES']._serialized_start=1408
  _globals['_MSGUPDATENAMESPACEROLES']._serialized_end=1637
  _globals['_MSGUPDATENAMESPACEROLESRESPONSE']._serialized_start=1639
  _globals['_MSGUPDATENAMESPACEROLESRESPONSE']._serialized_end=1672
  _globals['_MSGREVOKENAMESPACEROLES']._serialized_start=1675
  _globals['_MSGREVOKENAMESPACEROLES']._serialized_end=1851
  _globals['_MSGREVOKENAMESPACEROLESRESPONSE']._serialized_start=1853
  _globals['_MSGREVOKENAMESPACEROLESRESPONSE']._serialized_end=1886
  _globals['_MSGCLAIMVOUCHER']._serialized_start=1888
  _globals['_MSGCLAIMVOUCHER']._serialized_end=1973
  _globals['_MSGCLAIMVOUCHERRESPONSE']._serialized_start=1975
  _globals['_MSGCLAIMVOUCHERRESPONSE']._serialized_end=2000
  _globals['_MSG']._serialized_start=2003
  _globals['_MSG']._serialized_end=2925
# @@protoc_insertion_point(module_scope)
