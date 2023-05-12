# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/vesting/v1beta1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from cosmos.vesting.v1beta1 import vesting_pb2 as cosmos_dot_vesting_dot_v1beta1_dot_vesting__pb2
from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63osmos/vesting/v1beta1/tx.proto\x12\x16\x63osmos.vesting.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a$cosmos/vesting/v1beta1/vesting.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x11\x61mino/amino.proto\"\xba\x02\n\x17MsgCreateVestingAccount\x12.\n\x0c\x66rom_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12,\n\nto_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12`\n\x06\x61mount\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB5\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12\x10\n\x08\x65nd_time\x18\x04 \x01(\x03\x12\x0f\n\x07\x64\x65layed\x18\x05 \x01(\x08:<\x82\xe7\xb0*\x0c\x66rom_address\x8a\xe7\xb0*\"cosmos-sdk/MsgCreateVestingAccount\xe8\xa0\x1f\x01\"!\n\x1fMsgCreateVestingAccountResponse\"\x9e\x02\n\x1fMsgCreatePermanentLockedAccount\x12-\n\x0c\x66rom_address\x18\x01 \x01(\tB\x17\xf2\xde\x1f\x13yaml:\"from_address\"\x12)\n\nto_address\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:\"to_address\"\x12`\n\x06\x61mount\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB5\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:?\x82\xe7\xb0*\x0c\x66rom_address\x8a\xe7\xb0*%cosmos-sdk/MsgCreatePermLockedAccount\xe8\xa0\x1f\x01\")\n\'MsgCreatePermanentLockedAccountResponse\"\xe9\x01\n\x1fMsgCreatePeriodicVestingAccount\x12\x14\n\x0c\x66rom_address\x18\x01 \x01(\t\x12\x12\n\nto_address\x18\x02 \x01(\t\x12\x12\n\nstart_time\x18\x03 \x01(\x03\x12\x42\n\x0fvesting_periods\x18\x04 \x03(\x0b\x32\x1e.cosmos.vesting.v1beta1.PeriodB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:D\x82\xe7\xb0*\x0c\x66rom_address\x8a\xe7\xb0**cosmos-sdk/MsgCreatePeriodicVestingAccount\xe8\xa0\x1f\x00\")\n\'MsgCreatePeriodicVestingAccountResponse2\xc5\x03\n\x03Msg\x12\x80\x01\n\x14\x43reateVestingAccount\x12/.cosmos.vesting.v1beta1.MsgCreateVestingAccount\x1a\x37.cosmos.vesting.v1beta1.MsgCreateVestingAccountResponse\x12\x98\x01\n\x1c\x43reatePermanentLockedAccount\x12\x37.cosmos.vesting.v1beta1.MsgCreatePermanentLockedAccount\x1a?.cosmos.vesting.v1beta1.MsgCreatePermanentLockedAccountResponse\x12\x98\x01\n\x1c\x43reatePeriodicVestingAccount\x12\x37.cosmos.vesting.v1beta1.MsgCreatePeriodicVestingAccount\x1a?.cosmos.vesting.v1beta1.MsgCreatePeriodicVestingAccountResponse\x1a\x05\x80\xe7\xb0*\x01\x42\x33Z1github.com/cosmos/cosmos-sdk/x/auth/vesting/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.vesting.v1beta1.tx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/x/auth/vesting/types'
  _MSGCREATEVESTINGACCOUNT.fields_by_name['from_address']._options = None
  _MSGCREATEVESTINGACCOUNT.fields_by_name['from_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGCREATEVESTINGACCOUNT.fields_by_name['to_address']._options = None
  _MSGCREATEVESTINGACCOUNT.fields_by_name['to_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGCREATEVESTINGACCOUNT.fields_by_name['amount']._options = None
  _MSGCREATEVESTINGACCOUNT.fields_by_name['amount']._serialized_options = b'\310\336\037\000\250\347\260*\001\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _MSGCREATEVESTINGACCOUNT._options = None
  _MSGCREATEVESTINGACCOUNT._serialized_options = b'\202\347\260*\014from_address\212\347\260*\"cosmos-sdk/MsgCreateVestingAccount\350\240\037\001'
  _MSGCREATEPERMANENTLOCKEDACCOUNT.fields_by_name['from_address']._options = None
  _MSGCREATEPERMANENTLOCKEDACCOUNT.fields_by_name['from_address']._serialized_options = b'\362\336\037\023yaml:\"from_address\"'
  _MSGCREATEPERMANENTLOCKEDACCOUNT.fields_by_name['to_address']._options = None
  _MSGCREATEPERMANENTLOCKEDACCOUNT.fields_by_name['to_address']._serialized_options = b'\362\336\037\021yaml:\"to_address\"'
  _MSGCREATEPERMANENTLOCKEDACCOUNT.fields_by_name['amount']._options = None
  _MSGCREATEPERMANENTLOCKEDACCOUNT.fields_by_name['amount']._serialized_options = b'\310\336\037\000\250\347\260*\001\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _MSGCREATEPERMANENTLOCKEDACCOUNT._options = None
  _MSGCREATEPERMANENTLOCKEDACCOUNT._serialized_options = b'\202\347\260*\014from_address\212\347\260*%cosmos-sdk/MsgCreatePermLockedAccount\350\240\037\001'
  _MSGCREATEPERIODICVESTINGACCOUNT.fields_by_name['vesting_periods']._options = None
  _MSGCREATEPERIODICVESTINGACCOUNT.fields_by_name['vesting_periods']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _MSGCREATEPERIODICVESTINGACCOUNT._options = None
  _MSGCREATEPERIODICVESTINGACCOUNT._serialized_options = b'\202\347\260*\014from_address\212\347\260**cosmos-sdk/MsgCreatePeriodicVestingAccount\350\240\037\000'
  _MSG._options = None
  _MSG._serialized_options = b'\200\347\260*\001'
  _MSGCREATEVESTINGACCOUNT._serialized_start=223
  _MSGCREATEVESTINGACCOUNT._serialized_end=537
  _MSGCREATEVESTINGACCOUNTRESPONSE._serialized_start=539
  _MSGCREATEVESTINGACCOUNTRESPONSE._serialized_end=572
  _MSGCREATEPERMANENTLOCKEDACCOUNT._serialized_start=575
  _MSGCREATEPERMANENTLOCKEDACCOUNT._serialized_end=861
  _MSGCREATEPERMANENTLOCKEDACCOUNTRESPONSE._serialized_start=863
  _MSGCREATEPERMANENTLOCKEDACCOUNTRESPONSE._serialized_end=904
  _MSGCREATEPERIODICVESTINGACCOUNT._serialized_start=907
  _MSGCREATEPERIODICVESTINGACCOUNT._serialized_end=1140
  _MSGCREATEPERIODICVESTINGACCOUNTRESPONSE._serialized_start=1142
  _MSGCREATEPERIODICVESTINGACCOUNTRESPONSE._serialized_end=1183
  _MSG._serialized_start=1186
  _MSG._serialized_end=1639
# @@protoc_insertion_point(module_scope)
