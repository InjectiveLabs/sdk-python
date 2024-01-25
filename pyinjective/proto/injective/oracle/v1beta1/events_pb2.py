# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/oracle/v1beta1/events.proto
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
from injective.oracle.v1beta1 import oracle_pb2 as injective_dot_oracle_dot_v1beta1_dot_oracle__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%injective/oracle/v1beta1/events.proto\x12\x18injective.oracle.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a%injective/oracle/v1beta1/oracle.proto\"|\n\x16SetChainlinkPriceEvent\x12\x0f\n\x07\x66\x65\x65\x64_id\x18\x01 \x01(\t\x12>\n\x06\x61nswer\x18\x02 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\x11\n\ttimestamp\x18\x03 \x01(\x04\"\x9d\x01\n\x11SetBandPriceEvent\x12\x0f\n\x07relayer\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12=\n\x05price\x18\x03 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\x14\n\x0cresolve_time\x18\x04 \x01(\x04\x12\x12\n\nrequest_id\x18\x05 \x01(\x04\"\xb5\x01\n\x14SetBandIBCPriceEvent\x12\x0f\n\x07relayer\x18\x01 \x01(\t\x12\x0f\n\x07symbols\x18\x02 \x03(\t\x12>\n\x06prices\x18\x03 \x03(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\x14\n\x0cresolve_time\x18\x04 \x01(\x04\x12\x12\n\nrequest_id\x18\x05 \x01(\x04\x12\x11\n\tclient_id\x18\x06 \x01(\x03\"?\n\x16\x45ventBandIBCAckSuccess\x12\x12\n\nack_result\x18\x01 \x01(\t\x12\x11\n\tclient_id\x18\x02 \x01(\x03\"<\n\x14\x45ventBandIBCAckError\x12\x11\n\tack_error\x18\x01 \x01(\t\x12\x11\n\tclient_id\x18\x02 \x01(\x03\"0\n\x1b\x45ventBandIBCResponseTimeout\x12\x11\n\tclient_id\x18\x01 \x01(\x03\"\x85\x01\n\x16SetPriceFeedPriceEvent\x12\x0f\n\x07relayer\x18\x01 \x01(\t\x12\x0c\n\x04\x62\x61se\x18\x02 \x01(\t\x12\r\n\x05quote\x18\x03 \x01(\t\x12=\n\x05price\x18\x04 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\"\x89\x01\n\x15SetProviderPriceEvent\x12\x10\n\x08provider\x18\x01 \x01(\t\x12\x0f\n\x07relayer\x18\x02 \x01(\t\x12\x0e\n\x06symbol\x18\x03 \x01(\t\x12=\n\x05price\x18\x04 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\"y\n\x15SetCoinbasePriceEvent\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12=\n\x05price\x18\x02 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\x11\n\ttimestamp\x18\x03 \x01(\x04\"N\n\x12\x45ventSetPythPrices\x12\x38\n\x06prices\x18\x01 \x03(\x0b\x32(.injective.oracle.v1beta1.PythPriceStateBNZLgithub.com/InjectiveLabs/injective-core/injective-chain/modules/oracle/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.oracle.v1beta1.events_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZLgithub.com/InjectiveLabs/injective-core/injective-chain/modules/oracle/types'
  _globals['_SETCHAINLINKPRICEEVENT'].fields_by_name['answer']._options = None
  _globals['_SETCHAINLINKPRICEEVENT'].fields_by_name['answer']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_SETBANDPRICEEVENT'].fields_by_name['price']._options = None
  _globals['_SETBANDPRICEEVENT'].fields_by_name['price']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_SETBANDIBCPRICEEVENT'].fields_by_name['prices']._options = None
  _globals['_SETBANDIBCPRICEEVENT'].fields_by_name['prices']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_SETPRICEFEEDPRICEEVENT'].fields_by_name['price']._options = None
  _globals['_SETPRICEFEEDPRICEEVENT'].fields_by_name['price']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_SETPROVIDERPRICEEVENT'].fields_by_name['price']._options = None
  _globals['_SETPROVIDERPRICEEVENT'].fields_by_name['price']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_SETCOINBASEPRICEEVENT'].fields_by_name['price']._options = None
  _globals['_SETCOINBASEPRICEEVENT'].fields_by_name['price']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_SETCHAINLINKPRICEEVENT']._serialized_start=160
  _globals['_SETCHAINLINKPRICEEVENT']._serialized_end=284
  _globals['_SETBANDPRICEEVENT']._serialized_start=287
  _globals['_SETBANDPRICEEVENT']._serialized_end=444
  _globals['_SETBANDIBCPRICEEVENT']._serialized_start=447
  _globals['_SETBANDIBCPRICEEVENT']._serialized_end=628
  _globals['_EVENTBANDIBCACKSUCCESS']._serialized_start=630
  _globals['_EVENTBANDIBCACKSUCCESS']._serialized_end=693
  _globals['_EVENTBANDIBCACKERROR']._serialized_start=695
  _globals['_EVENTBANDIBCACKERROR']._serialized_end=755
  _globals['_EVENTBANDIBCRESPONSETIMEOUT']._serialized_start=757
  _globals['_EVENTBANDIBCRESPONSETIMEOUT']._serialized_end=805
  _globals['_SETPRICEFEEDPRICEEVENT']._serialized_start=808
  _globals['_SETPRICEFEEDPRICEEVENT']._serialized_end=941
  _globals['_SETPROVIDERPRICEEVENT']._serialized_start=944
  _globals['_SETPROVIDERPRICEEVENT']._serialized_end=1081
  _globals['_SETCOINBASEPRICEEVENT']._serialized_start=1083
  _globals['_SETCOINBASEPRICEEVENT']._serialized_end=1204
  _globals['_EVENTSETPYTHPRICES']._serialized_start=1206
  _globals['_EVENTSETPYTHPRICES']._serialized_end=1284
# @@protoc_insertion_point(module_scope)
