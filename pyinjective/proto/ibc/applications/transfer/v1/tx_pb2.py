# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/transfer/v1/tx.proto
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
from pyinjective.proto.ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%ibc/applications/transfer/v1/tx.proto\x12\x1cibc.applications.transfer.v1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1fibc/core/client/v1/client.proto\"\xe3\x02\n\x0bMsgTransfer\x12+\n\x0bsource_port\x18\x01 \x01(\tB\x16\xf2\xde\x1f\x12yaml:\"source_port\"\x12\x31\n\x0esource_channel\x18\x02 \x01(\tB\x19\xf2\xde\x1f\x15yaml:\"source_channel\"\x12.\n\x05token\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x0e\n\x06sender\x18\x04 \x01(\t\x12\x10\n\x08receiver\x18\x05 \x01(\t\x12Q\n\x0etimeout_height\x18\x06 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x1d\xc8\xde\x1f\x00\xf2\xde\x1f\x15yaml:\"timeout_height\"\x12\x37\n\x11timeout_timestamp\x18\x07 \x01(\x04\x42\x1c\xf2\xde\x1f\x18yaml:\"timeout_timestamp\"\x12\x0c\n\x04memo\x18\x08 \x01(\t:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\"\'\n\x13MsgTransferResponse\x12\x10\n\x08sequence\x18\x01 \x01(\x04\x32o\n\x03Msg\x12h\n\x08Transfer\x12).ibc.applications.transfer.v1.MsgTransfer\x1a\x31.ibc.applications.transfer.v1.MsgTransferResponseB9Z7github.com/cosmos/ibc-go/v7/modules/apps/transfer/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.transfer.v1.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/cosmos/ibc-go/v7/modules/apps/transfer/types'
  _globals['_MSGTRANSFER'].fields_by_name['source_port']._loaded_options = None
  _globals['_MSGTRANSFER'].fields_by_name['source_port']._serialized_options = b'\362\336\037\022yaml:\"source_port\"'
  _globals['_MSGTRANSFER'].fields_by_name['source_channel']._loaded_options = None
  _globals['_MSGTRANSFER'].fields_by_name['source_channel']._serialized_options = b'\362\336\037\025yaml:\"source_channel\"'
  _globals['_MSGTRANSFER'].fields_by_name['token']._loaded_options = None
  _globals['_MSGTRANSFER'].fields_by_name['token']._serialized_options = b'\310\336\037\000'
  _globals['_MSGTRANSFER'].fields_by_name['timeout_height']._loaded_options = None
  _globals['_MSGTRANSFER'].fields_by_name['timeout_height']._serialized_options = b'\310\336\037\000\362\336\037\025yaml:\"timeout_height\"'
  _globals['_MSGTRANSFER'].fields_by_name['timeout_timestamp']._loaded_options = None
  _globals['_MSGTRANSFER'].fields_by_name['timeout_timestamp']._serialized_options = b'\362\336\037\030yaml:\"timeout_timestamp\"'
  _globals['_MSGTRANSFER']._loaded_options = None
  _globals['_MSGTRANSFER']._serialized_options = b'\210\240\037\000\350\240\037\000'
  _globals['_MSGTRANSFER']._serialized_start=159
  _globals['_MSGTRANSFER']._serialized_end=514
  _globals['_MSGTRANSFERRESPONSE']._serialized_start=516
  _globals['_MSGTRANSFERRESPONSE']._serialized_end=555
  _globals['_MSG']._serialized_start=557
  _globals['_MSG']._serialized_end=668
# @@protoc_insertion_point(module_scope)
