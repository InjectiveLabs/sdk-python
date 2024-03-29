# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exchange/event_provider_api.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!exchange/event_provider_api.proto\x12\x12\x65vent_provider_api\"\x18\n\x16GetLatestHeightRequest\"o\n\x17GetLatestHeightResponse\x12\t\n\x01v\x18\x01 \x01(\t\x12\t\n\x01s\x18\x02 \x01(\t\x12\t\n\x01\x65\x18\x03 \x01(\t\x12\x33\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32%.event_provider_api.LatestBlockHeight\"#\n\x11LatestBlockHeight\x12\x0e\n\x06height\x18\x01 \x01(\x04\";\n\x18StreamBlockEventsRequest\x12\x0f\n\x07\x62\x61\x63kend\x18\x01 \x01(\t\x12\x0e\n\x06height\x18\x02 \x01(\x11\"F\n\x19StreamBlockEventsResponse\x12)\n\x06\x62locks\x18\x01 \x03(\x0b\x32\x19.event_provider_api.Block\"i\n\x05\x42lock\x12\x0e\n\x06height\x18\x01 \x01(\x12\x12\x0f\n\x07version\x18\x02 \x01(\t\x12.\n\x06\x65vents\x18\x03 \x03(\x0b\x32\x1e.event_provider_api.BlockEvent\x12\x0f\n\x07in_sync\x18\x04 \x01(\x08\">\n\nBlockEvent\x12\x10\n\x08type_url\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x0f\n\x07tx_hash\x18\x03 \x01(\x0c\";\n\x18GetBlockEventsRPCRequest\x12\x0f\n\x07\x62\x61\x63kend\x18\x01 \x01(\t\x12\x0e\n\x06height\x18\x02 \x01(\x11\"n\n\x19GetBlockEventsRPCResponse\x12\t\n\x01v\x18\x01 \x01(\t\x12\t\n\x01s\x18\x02 \x01(\t\x12\t\n\x01\x65\x18\x03 \x01(\t\x12\x30\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\".event_provider_api.BlockEventsRPC\"\xa5\x01\n\x0e\x42lockEventsRPC\x12\r\n\x05types\x18\x01 \x03(\t\x12\x0e\n\x06\x65vents\x18\x02 \x03(\x0c\x12\x43\n\ttx_hashes\x18\x03 \x03(\x0b\x32\x30.event_provider_api.BlockEventsRPC.TxHashesEntry\x1a/\n\rTxHashesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x11\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"L\n\x19GetCustomEventsRPCRequest\x12\x0f\n\x07\x62\x61\x63kend\x18\x01 \x01(\t\x12\x0e\n\x06height\x18\x02 \x01(\x11\x12\x0e\n\x06\x65vents\x18\x03 \x01(\t\"o\n\x1aGetCustomEventsRPCResponse\x12\t\n\x01v\x18\x01 \x01(\t\x12\t\n\x01s\x18\x02 \x01(\t\x12\t\n\x01\x65\x18\x03 \x01(\t\x12\x30\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\".event_provider_api.BlockEventsRPC\"@\n\x19GetABCIBlockEventsRequest\x12\x0e\n\x06height\x18\x01 \x01(\x11\x12\x13\n\x0b\x65vent_types\x18\x02 \x03(\t\"n\n\x1aGetABCIBlockEventsResponse\x12\t\n\x01v\x18\x01 \x01(\t\x12\t\n\x01s\x18\x02 \x01(\t\x12\t\n\x01\x65\x18\x03 \x01(\t\x12/\n\traw_block\x18\x04 \x01(\x0b\x32\x1c.event_provider_api.RawBlock\"\xce\x01\n\x08RawBlock\x12\x0e\n\x06height\x18\x01 \x01(\x12\x12>\n\x0btxs_results\x18\x02 \x03(\x0b\x32).event_provider_api.ABCIResponseDeliverTx\x12\x39\n\x12\x62\x65gin_block_events\x18\x03 \x03(\x0b\x32\x1d.event_provider_api.ABCIEvent\x12\x37\n\x10\x65nd_block_events\x18\x04 \x03(\x0b\x32\x1d.event_provider_api.ABCIEvent\"\xa8\x01\n\x15\x41\x42\x43IResponseDeliverTx\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x11\x12\x0b\n\x03log\x18\x02 \x01(\t\x12\x0c\n\x04info\x18\x03 \x01(\t\x12\x12\n\ngas_wanted\x18\x04 \x01(\x12\x12\x10\n\x08gas_used\x18\x05 \x01(\x12\x12-\n\x06\x65vents\x18\x06 \x03(\x0b\x32\x1d.event_provider_api.ABCIEvent\x12\x11\n\tcodespace\x18\x07 \x01(\t\"P\n\tABCIEvent\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x35\n\nattributes\x18\x02 \x03(\x0b\x32!.event_provider_api.ABCIAttribute\"+\n\rABCIAttribute\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t2\xce\x04\n\x10\x45ventProviderAPI\x12j\n\x0fGetLatestHeight\x12*.event_provider_api.GetLatestHeightRequest\x1a+.event_provider_api.GetLatestHeightResponse\x12r\n\x11StreamBlockEvents\x12,.event_provider_api.StreamBlockEventsRequest\x1a-.event_provider_api.StreamBlockEventsResponse0\x01\x12p\n\x11GetBlockEventsRPC\x12,.event_provider_api.GetBlockEventsRPCRequest\x1a-.event_provider_api.GetBlockEventsRPCResponse\x12s\n\x12GetCustomEventsRPC\x12-.event_provider_api.GetCustomEventsRPCRequest\x1a..event_provider_api.GetCustomEventsRPCResponse\x12s\n\x12GetABCIBlockEvents\x12-.event_provider_api.GetABCIBlockEventsRequest\x1a..event_provider_api.GetABCIBlockEventsResponseB\x17Z\x15/event_provider_apipbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exchange.event_provider_api_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\025/event_provider_apipb'
  _globals['_BLOCKEVENTSRPC_TXHASHESENTRY']._options = None
  _globals['_BLOCKEVENTSRPC_TXHASHESENTRY']._serialized_options = b'8\001'
  _globals['_GETLATESTHEIGHTREQUEST']._serialized_start=57
  _globals['_GETLATESTHEIGHTREQUEST']._serialized_end=81
  _globals['_GETLATESTHEIGHTRESPONSE']._serialized_start=83
  _globals['_GETLATESTHEIGHTRESPONSE']._serialized_end=194
  _globals['_LATESTBLOCKHEIGHT']._serialized_start=196
  _globals['_LATESTBLOCKHEIGHT']._serialized_end=231
  _globals['_STREAMBLOCKEVENTSREQUEST']._serialized_start=233
  _globals['_STREAMBLOCKEVENTSREQUEST']._serialized_end=292
  _globals['_STREAMBLOCKEVENTSRESPONSE']._serialized_start=294
  _globals['_STREAMBLOCKEVENTSRESPONSE']._serialized_end=364
  _globals['_BLOCK']._serialized_start=366
  _globals['_BLOCK']._serialized_end=471
  _globals['_BLOCKEVENT']._serialized_start=473
  _globals['_BLOCKEVENT']._serialized_end=535
  _globals['_GETBLOCKEVENTSRPCREQUEST']._serialized_start=537
  _globals['_GETBLOCKEVENTSRPCREQUEST']._serialized_end=596
  _globals['_GETBLOCKEVENTSRPCRESPONSE']._serialized_start=598
  _globals['_GETBLOCKEVENTSRPCRESPONSE']._serialized_end=708
  _globals['_BLOCKEVENTSRPC']._serialized_start=711
  _globals['_BLOCKEVENTSRPC']._serialized_end=876
  _globals['_BLOCKEVENTSRPC_TXHASHESENTRY']._serialized_start=829
  _globals['_BLOCKEVENTSRPC_TXHASHESENTRY']._serialized_end=876
  _globals['_GETCUSTOMEVENTSRPCREQUEST']._serialized_start=878
  _globals['_GETCUSTOMEVENTSRPCREQUEST']._serialized_end=954
  _globals['_GETCUSTOMEVENTSRPCRESPONSE']._serialized_start=956
  _globals['_GETCUSTOMEVENTSRPCRESPONSE']._serialized_end=1067
  _globals['_GETABCIBLOCKEVENTSREQUEST']._serialized_start=1069
  _globals['_GETABCIBLOCKEVENTSREQUEST']._serialized_end=1133
  _globals['_GETABCIBLOCKEVENTSRESPONSE']._serialized_start=1135
  _globals['_GETABCIBLOCKEVENTSRESPONSE']._serialized_end=1245
  _globals['_RAWBLOCK']._serialized_start=1248
  _globals['_RAWBLOCK']._serialized_end=1454
  _globals['_ABCIRESPONSEDELIVERTX']._serialized_start=1457
  _globals['_ABCIRESPONSEDELIVERTX']._serialized_end=1625
  _globals['_ABCIEVENT']._serialized_start=1627
  _globals['_ABCIEVENT']._serialized_end=1707
  _globals['_ABCIATTRIBUTE']._serialized_start=1709
  _globals['_ABCIATTRIBUTE']._serialized_end=1752
  _globals['_EVENTPROVIDERAPI']._serialized_start=1755
  _globals['_EVENTPROVIDERAPI']._serialized_end=2345
# @@protoc_insertion_point(module_scope)
