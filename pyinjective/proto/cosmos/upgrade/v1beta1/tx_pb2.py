# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/upgrade/v1beta1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from cosmos.upgrade.v1beta1 import upgrade_pb2 as cosmos_dot_upgrade_dot_v1beta1_dot_upgrade__pb2
from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63osmos/upgrade/v1beta1/tx.proto\x12\x16\x63osmos.upgrade.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a$cosmos/upgrade/v1beta1/upgrade.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x11\x61mino/amino.proto\"\xaa\x01\n\x12MsgSoftwareUpgrade\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x35\n\x04plan\x18\x02 \x01(\x0b\x32\x1c.cosmos.upgrade.v1beta1.PlanB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:0\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x1d\x63osmos-sdk/MsgSoftwareUpgrade\"\x1c\n\x1aMsgSoftwareUpgradeResponse\"o\n\x10MsgCancelUpgrade\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:.\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x1b\x63osmos-sdk/MsgCancelUpgrade\"\x1a\n\x18MsgCancelUpgradeResponse2\xec\x01\n\x03Msg\x12q\n\x0fSoftwareUpgrade\x12*.cosmos.upgrade.v1beta1.MsgSoftwareUpgrade\x1a\x32.cosmos.upgrade.v1beta1.MsgSoftwareUpgradeResponse\x12k\n\rCancelUpgrade\x12(.cosmos.upgrade.v1beta1.MsgCancelUpgrade\x1a\x30.cosmos.upgrade.v1beta1.MsgCancelUpgradeResponse\x1a\x05\x80\xe7\xb0*\x01\x42.Z,github.com/cosmos/cosmos-sdk/x/upgrade/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.upgrade.v1beta1.tx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/x/upgrade/types'
  _MSGSOFTWAREUPGRADE.fields_by_name['authority']._options = None
  _MSGSOFTWAREUPGRADE.fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGSOFTWAREUPGRADE.fields_by_name['plan']._options = None
  _MSGSOFTWAREUPGRADE.fields_by_name['plan']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _MSGSOFTWAREUPGRADE._options = None
  _MSGSOFTWAREUPGRADE._serialized_options = b'\202\347\260*\tauthority\212\347\260*\035cosmos-sdk/MsgSoftwareUpgrade'
  _MSGCANCELUPGRADE.fields_by_name['authority']._options = None
  _MSGCANCELUPGRADE.fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGCANCELUPGRADE._options = None
  _MSGCANCELUPGRADE._serialized_options = b'\202\347\260*\tauthority\212\347\260*\033cosmos-sdk/MsgCancelUpgrade'
  _MSG._options = None
  _MSG._serialized_options = b'\200\347\260*\001'
  _MSGSOFTWAREUPGRADE._serialized_start=191
  _MSGSOFTWAREUPGRADE._serialized_end=361
  _MSGSOFTWAREUPGRADERESPONSE._serialized_start=363
  _MSGSOFTWAREUPGRADERESPONSE._serialized_end=391
  _MSGCANCELUPGRADE._serialized_start=393
  _MSGCANCELUPGRADE._serialized_end=504
  _MSGCANCELUPGRADERESPONSE._serialized_start=506
  _MSGCANCELUPGRADERESPONSE._serialized_end=532
  _MSG._serialized_start=535
  _MSG._serialized_end=771
# @@protoc_insertion_point(module_scope)
