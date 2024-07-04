# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/tokenfactory/v1beta1/tx.proto
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
from pyinjective.proto.cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2
from pyinjective.proto.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.injective.tokenfactory.v1beta1 import params_pb2 as injective_dot_tokenfactory_dot_v1beta1_dot_params__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'injective/tokenfactory/v1beta1/tx.proto\x12\x1einjective.tokenfactory.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1e\x63osmos/bank/v1beta1/bank.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a+injective/tokenfactory/v1beta1/params.proto\"\xc9\x01\n\x0eMsgCreateDenom\x12)\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"R\x06sender\x12/\n\x08subdenom\x18\x02 \x01(\tB\x13\xf2\xde\x1f\x0fyaml:\"subdenom\"R\x08subdenom\x12#\n\x04name\x18\x03 \x01(\tB\x0f\xf2\xde\x1f\x0byaml:\"name\"R\x04name\x12)\n\x06symbol\x18\x04 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"symbol\"R\x06symbol:\x0b\x82\xe7\xb0*\x06sender\"\\\n\x16MsgCreateDenomResponse\x12\x42\n\x0fnew_token_denom\x18\x01 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:\"new_token_denom\"R\rnewTokenDenom\"\x8b\x01\n\x07MsgMint\x12)\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"R\x06sender\x12H\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x15\xc8\xde\x1f\x00\xf2\xde\x1f\ryaml:\"amount\"R\x06\x61mount:\x0b\x82\xe7\xb0*\x06sender\"\x11\n\x0fMsgMintResponse\"\x8b\x01\n\x07MsgBurn\x12)\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"R\x06sender\x12H\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x15\xc8\xde\x1f\x00\xf2\xde\x1f\ryaml:\"amount\"R\x06\x61mount:\x0b\x82\xe7\xb0*\x06sender\"\x11\n\x0fMsgBurnResponse\"\xa3\x01\n\x0eMsgChangeAdmin\x12)\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"R\x06sender\x12&\n\x05\x64\x65nom\x18\x02 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:\"denom\"R\x05\x64\x65nom\x12\x31\n\tnew_admin\x18\x03 \x01(\tB\x14\xf2\xde\x1f\x10yaml:\"new_admin\"R\x08newAdmin:\x0b\x82\xe7\xb0*\x06sender\"\x18\n\x16MsgChangeAdminResponse\"\xa1\x01\n\x13MsgSetDenomMetadata\x12)\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"R\x06sender\x12R\n\x08metadata\x18\x02 \x01(\x0b\x32\x1d.cosmos.bank.v1beta1.MetadataB\x17\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:\"metadata\"R\x08metadata:\x0b\x82\xe7\xb0*\x06sender\"\x1d\n\x1bMsgSetDenomMetadataResponse\"\x9f\x01\n\x0fMsgUpdateParams\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12\x44\n\x06params\x18\x02 \x01(\x0b\x32&.injective.tokenfactory.v1beta1.ParamsB\x04\xc8\xde\x1f\x00R\x06params:\x0e\x82\xe7\xb0*\tauthority\"\x19\n\x17MsgUpdateParamsResponse2\xb8\x05\n\x03Msg\x12u\n\x0b\x43reateDenom\x12..injective.tokenfactory.v1beta1.MsgCreateDenom\x1a\x36.injective.tokenfactory.v1beta1.MsgCreateDenomResponse\x12`\n\x04Mint\x12\'.injective.tokenfactory.v1beta1.MsgMint\x1a/.injective.tokenfactory.v1beta1.MsgMintResponse\x12`\n\x04\x42urn\x12\'.injective.tokenfactory.v1beta1.MsgBurn\x1a/.injective.tokenfactory.v1beta1.MsgBurnResponse\x12u\n\x0b\x43hangeAdmin\x12..injective.tokenfactory.v1beta1.MsgChangeAdmin\x1a\x36.injective.tokenfactory.v1beta1.MsgChangeAdminResponse\x12\x84\x01\n\x10SetDenomMetadata\x12\x33.injective.tokenfactory.v1beta1.MsgSetDenomMetadata\x1a;.injective.tokenfactory.v1beta1.MsgSetDenomMetadataResponse\x12x\n\x0cUpdateParams\x12/.injective.tokenfactory.v1beta1.MsgUpdateParams\x1a\x37.injective.tokenfactory.v1beta1.MsgUpdateParamsResponseB\x9b\x02\n\"com.injective.tokenfactory.v1beta1B\x07TxProtoP\x01ZRgithub.com/InjectiveLabs/injective-core/injective-chain/modules/tokenfactory/types\xa2\x02\x03ITX\xaa\x02\x1eInjective.Tokenfactory.V1beta1\xca\x02\x1eInjective\\Tokenfactory\\V1beta1\xe2\x02*Injective\\Tokenfactory\\V1beta1\\GPBMetadata\xea\x02 Injective::Tokenfactory::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.tokenfactory.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.injective.tokenfactory.v1beta1B\007TxProtoP\001ZRgithub.com/InjectiveLabs/injective-core/injective-chain/modules/tokenfactory/types\242\002\003ITX\252\002\036Injective.Tokenfactory.V1beta1\312\002\036Injective\\Tokenfactory\\V1beta1\342\002*Injective\\Tokenfactory\\V1beta1\\GPBMetadata\352\002 Injective::Tokenfactory::V1beta1'
  _globals['_MSGCREATEDENOM'].fields_by_name['sender']._options = None
  _globals['_MSGCREATEDENOM'].fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _globals['_MSGCREATEDENOM'].fields_by_name['subdenom']._options = None
  _globals['_MSGCREATEDENOM'].fields_by_name['subdenom']._serialized_options = b'\362\336\037\017yaml:\"subdenom\"'
  _globals['_MSGCREATEDENOM'].fields_by_name['name']._options = None
  _globals['_MSGCREATEDENOM'].fields_by_name['name']._serialized_options = b'\362\336\037\013yaml:\"name\"'
  _globals['_MSGCREATEDENOM'].fields_by_name['symbol']._options = None
  _globals['_MSGCREATEDENOM'].fields_by_name['symbol']._serialized_options = b'\362\336\037\ryaml:\"symbol\"'
  _globals['_MSGCREATEDENOM']._options = None
  _globals['_MSGCREATEDENOM']._serialized_options = b'\202\347\260*\006sender'
  _globals['_MSGCREATEDENOMRESPONSE'].fields_by_name['new_token_denom']._options = None
  _globals['_MSGCREATEDENOMRESPONSE'].fields_by_name['new_token_denom']._serialized_options = b'\362\336\037\026yaml:\"new_token_denom\"'
  _globals['_MSGMINT'].fields_by_name['sender']._options = None
  _globals['_MSGMINT'].fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _globals['_MSGMINT'].fields_by_name['amount']._options = None
  _globals['_MSGMINT'].fields_by_name['amount']._serialized_options = b'\310\336\037\000\362\336\037\ryaml:\"amount\"'
  _globals['_MSGMINT']._options = None
  _globals['_MSGMINT']._serialized_options = b'\202\347\260*\006sender'
  _globals['_MSGBURN'].fields_by_name['sender']._options = None
  _globals['_MSGBURN'].fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _globals['_MSGBURN'].fields_by_name['amount']._options = None
  _globals['_MSGBURN'].fields_by_name['amount']._serialized_options = b'\310\336\037\000\362\336\037\ryaml:\"amount\"'
  _globals['_MSGBURN']._options = None
  _globals['_MSGBURN']._serialized_options = b'\202\347\260*\006sender'
  _globals['_MSGCHANGEADMIN'].fields_by_name['sender']._options = None
  _globals['_MSGCHANGEADMIN'].fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _globals['_MSGCHANGEADMIN'].fields_by_name['denom']._options = None
  _globals['_MSGCHANGEADMIN'].fields_by_name['denom']._serialized_options = b'\362\336\037\014yaml:\"denom\"'
  _globals['_MSGCHANGEADMIN'].fields_by_name['new_admin']._options = None
  _globals['_MSGCHANGEADMIN'].fields_by_name['new_admin']._serialized_options = b'\362\336\037\020yaml:\"new_admin\"'
  _globals['_MSGCHANGEADMIN']._options = None
  _globals['_MSGCHANGEADMIN']._serialized_options = b'\202\347\260*\006sender'
  _globals['_MSGSETDENOMMETADATA'].fields_by_name['sender']._options = None
  _globals['_MSGSETDENOMMETADATA'].fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _globals['_MSGSETDENOMMETADATA'].fields_by_name['metadata']._options = None
  _globals['_MSGSETDENOMMETADATA'].fields_by_name['metadata']._serialized_options = b'\310\336\037\000\362\336\037\017yaml:\"metadata\"'
  _globals['_MSGSETDENOMMETADATA']._options = None
  _globals['_MSGSETDENOMMETADATA']._serialized_options = b'\202\347\260*\006sender'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_MSGUPDATEPARAMS']._options = None
  _globals['_MSGUPDATEPARAMS']._serialized_options = b'\202\347\260*\tauthority'
  _globals['_MSGCREATEDENOM']._serialized_start=259
  _globals['_MSGCREATEDENOM']._serialized_end=460
  _globals['_MSGCREATEDENOMRESPONSE']._serialized_start=462
  _globals['_MSGCREATEDENOMRESPONSE']._serialized_end=554
  _globals['_MSGMINT']._serialized_start=557
  _globals['_MSGMINT']._serialized_end=696
  _globals['_MSGMINTRESPONSE']._serialized_start=698
  _globals['_MSGMINTRESPONSE']._serialized_end=715
  _globals['_MSGBURN']._serialized_start=718
  _globals['_MSGBURN']._serialized_end=857
  _globals['_MSGBURNRESPONSE']._serialized_start=859
  _globals['_MSGBURNRESPONSE']._serialized_end=876
  _globals['_MSGCHANGEADMIN']._serialized_start=879
  _globals['_MSGCHANGEADMIN']._serialized_end=1042
  _globals['_MSGCHANGEADMINRESPONSE']._serialized_start=1044
  _globals['_MSGCHANGEADMINRESPONSE']._serialized_end=1068
  _globals['_MSGSETDENOMMETADATA']._serialized_start=1071
  _globals['_MSGSETDENOMMETADATA']._serialized_end=1232
  _globals['_MSGSETDENOMMETADATARESPONSE']._serialized_start=1234
  _globals['_MSGSETDENOMMETADATARESPONSE']._serialized_end=1263
  _globals['_MSGUPDATEPARAMS']._serialized_start=1266
  _globals['_MSGUPDATEPARAMS']._serialized_end=1425
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start=1427
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end=1452
  _globals['_MSG']._serialized_start=1455
  _globals['_MSG']._serialized_end=2151
# @@protoc_insertion_point(module_scope)
