# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/crisis/v1beta1/tx.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x63osmos/crisis/v1beta1/tx.proto\x12\x15\x63osmos.crisis.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x11\x61mino/amino.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\xad\x01\n\x12MsgVerifyInvariant\x12(\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x1d\n\x15invariant_module_name\x18\x02 \x01(\t\x12\x17\n\x0finvariant_route\x18\x03 \x01(\t:5\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x1d\x63osmos-sdk/MsgVerifyInvariant\"\x1c\n\x1aMsgVerifyInvariantResponse\"\xb2\x01\n\x0fMsgUpdateParams\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12:\n\x0c\x63onstant_fee\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:6\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*#cosmos-sdk/x/crisis/MsgUpdateParams\"\x19\n\x17MsgUpdateParamsResponse2\xe5\x01\n\x03Msg\x12o\n\x0fVerifyInvariant\x12).cosmos.crisis.v1beta1.MsgVerifyInvariant\x1a\x31.cosmos.crisis.v1beta1.MsgVerifyInvariantResponse\x12\x66\n\x0cUpdateParams\x12&.cosmos.crisis.v1beta1.MsgUpdateParams\x1a..cosmos.crisis.v1beta1.MsgUpdateParamsResponse\x1a\x05\x80\xe7\xb0*\x01\x42-Z+github.com/cosmos/cosmos-sdk/x/crisis/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.crisis.v1beta1.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z+github.com/cosmos/cosmos-sdk/x/crisis/types'
  _globals['_MSGVERIFYINVARIANT'].fields_by_name['sender']._loaded_options = None
  _globals['_MSGVERIFYINVARIANT'].fields_by_name['sender']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGVERIFYINVARIANT']._loaded_options = None
  _globals['_MSGVERIFYINVARIANT']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\006sender\212\347\260*\035cosmos-sdk/MsgVerifyInvariant'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['constant_fee']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['constant_fee']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_MSGUPDATEPARAMS']._loaded_options = None
  _globals['_MSGUPDATEPARAMS']._serialized_options = b'\202\347\260*\tauthority\212\347\260*#cosmos-sdk/x/crisis/MsgUpdateParams'
  _globals['_MSG']._loaded_options = None
  _globals['_MSG']._serialized_options = b'\200\347\260*\001'
  _globals['_MSGVERIFYINVARIANT']._serialized_start=183
  _globals['_MSGVERIFYINVARIANT']._serialized_end=356
  _globals['_MSGVERIFYINVARIANTRESPONSE']._serialized_start=358
  _globals['_MSGVERIFYINVARIANTRESPONSE']._serialized_end=386
  _globals['_MSGUPDATEPARAMS']._serialized_start=389
  _globals['_MSGUPDATEPARAMS']._serialized_end=567
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start=569
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end=594
  _globals['_MSG']._serialized_start=597
  _globals['_MSG']._serialized_end=826
# @@protoc_insertion_point(module_scope)
