# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exchange/injective_exchange_rpc.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%exchange/injective_exchange_rpc.proto\x12\x16injective_exchange_rpc\"\x1c\n\x0cGetTxRequest\x12\x0c\n\x04hash\x18\x01 \x01(\t\"\x92\x01\n\rGetTxResponse\x12\x0f\n\x07tx_hash\x18\x01 \x01(\t\x12\x0e\n\x06height\x18\x02 \x01(\x12\x12\r\n\x05index\x18\x03 \x01(\r\x12\x11\n\tcodespace\x18\x04 \x01(\t\x12\x0c\n\x04\x63ode\x18\x05 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x06 \x01(\x0c\x12\x0f\n\x07raw_log\x18\x07 \x01(\t\x12\x11\n\ttimestamp\x18\x08 \x01(\t\"\xb4\x01\n\x10PrepareTxRequest\x12\x10\n\x08\x63hain_id\x18\x01 \x01(\x04\x12\x16\n\x0esigner_address\x18\x02 \x01(\t\x12\x10\n\x08sequence\x18\x03 \x01(\x04\x12\x0c\n\x04memo\x18\x04 \x01(\t\x12\x16\n\x0etimeout_height\x18\x05 \x01(\x04\x12\x30\n\x03\x66\x65\x65\x18\x06 \x01(\x0b\x32#.injective_exchange_rpc.CosmosTxFee\x12\x0c\n\x04msgs\x18\x07 \x03(\x0c\"c\n\x0b\x43osmosTxFee\x12\x31\n\x05price\x18\x01 \x03(\x0b\x32\".injective_exchange_rpc.CosmosCoin\x12\x0b\n\x03gas\x18\x02 \x01(\x04\x12\x14\n\x0c\x64\x65legate_fee\x18\x03 \x01(\x08\"+\n\nCosmosCoin\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\t\"\x86\x01\n\x11PrepareTxResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\x12\x10\n\x08sequence\x18\x02 \x01(\x04\x12\x11\n\tsign_mode\x18\x03 \x01(\t\x12\x14\n\x0cpub_key_type\x18\x04 \x01(\t\x12\x11\n\tfee_payer\x18\x05 \x01(\t\x12\x15\n\rfee_payer_sig\x18\x06 \x01(\t\"\xc2\x01\n\x12\x42roadcastTxRequest\x12\x10\n\x08\x63hain_id\x18\x01 \x01(\x04\x12\n\n\x02tx\x18\x02 \x01(\x0c\x12\x0c\n\x04msgs\x18\x03 \x03(\x0c\x12\x35\n\x07pub_key\x18\x04 \x01(\x0b\x32$.injective_exchange_rpc.CosmosPubKey\x12\x11\n\tsignature\x18\x05 \x01(\t\x12\x11\n\tfee_payer\x18\x06 \x01(\t\x12\x15\n\rfee_payer_sig\x18\x07 \x01(\t\x12\x0c\n\x04mode\x18\x08 \x01(\t\")\n\x0c\x43osmosPubKey\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\"\x98\x01\n\x13\x42roadcastTxResponse\x12\x0f\n\x07tx_hash\x18\x01 \x01(\t\x12\x0e\n\x06height\x18\x02 \x01(\x12\x12\r\n\x05index\x18\x03 \x01(\r\x12\x11\n\tcodespace\x18\x04 \x01(\t\x12\x0c\n\x04\x63ode\x18\x05 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x06 \x01(\x0c\x12\x0f\n\x07raw_log\x18\x07 \x01(\t\x12\x11\n\ttimestamp\x18\x08 \x01(\t\"\xa8\x01\n\x16PrepareCosmosTxRequest\x12\x10\n\x08\x63hain_id\x18\x01 \x01(\x04\x12\x16\n\x0esender_address\x18\x02 \x01(\t\x12\x0c\n\x04memo\x18\x03 \x01(\t\x12\x16\n\x0etimeout_height\x18\x04 \x01(\x04\x12\x30\n\x03\x66\x65\x65\x18\x05 \x01(\x0b\x32#.injective_exchange_rpc.CosmosTxFee\x12\x0c\n\x04msgs\x18\x06 \x03(\x0c\"\xb9\x01\n\x17PrepareCosmosTxResponse\x12\n\n\x02tx\x18\x01 \x01(\x0c\x12\x11\n\tsign_mode\x18\x02 \x01(\t\x12\x14\n\x0cpub_key_type\x18\x03 \x01(\t\x12\x11\n\tfee_payer\x18\x04 \x01(\t\x12\x15\n\rfee_payer_sig\x18\x05 \x01(\t\x12?\n\x11\x66\x65\x65_payer_pub_key\x18\x06 \x01(\x0b\x32$.injective_exchange_rpc.CosmosPubKey\"\x88\x01\n\x18\x42roadcastCosmosTxRequest\x12\n\n\x02tx\x18\x01 \x01(\x0c\x12\x35\n\x07pub_key\x18\x02 \x01(\x0b\x32$.injective_exchange_rpc.CosmosPubKey\x12\x11\n\tsignature\x18\x03 \x01(\t\x12\x16\n\x0esender_address\x18\x04 \x01(\t\"\x9e\x01\n\x19\x42roadcastCosmosTxResponse\x12\x0f\n\x07tx_hash\x18\x01 \x01(\t\x12\x0e\n\x06height\x18\x02 \x01(\x12\x12\r\n\x05index\x18\x03 \x01(\r\x12\x11\n\tcodespace\x18\x04 \x01(\t\x12\x0c\n\x04\x63ode\x18\x05 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x06 \x01(\x0c\x12\x0f\n\x07raw_log\x18\x07 \x01(\t\x12\x11\n\ttimestamp\x18\x08 \x01(\t\"\x14\n\x12GetFeePayerRequest\"i\n\x13GetFeePayerResponse\x12\x11\n\tfee_payer\x18\x01 \x01(\t\x12?\n\x11\x66\x65\x65_payer_pub_key\x18\x02 \x01(\x0b\x32$.injective_exchange_rpc.CosmosPubKey2\x8c\x05\n\x14InjectiveExchangeRPC\x12T\n\x05GetTx\x12$.injective_exchange_rpc.GetTxRequest\x1a%.injective_exchange_rpc.GetTxResponse\x12`\n\tPrepareTx\x12(.injective_exchange_rpc.PrepareTxRequest\x1a).injective_exchange_rpc.PrepareTxResponse\x12\x66\n\x0b\x42roadcastTx\x12*.injective_exchange_rpc.BroadcastTxRequest\x1a+.injective_exchange_rpc.BroadcastTxResponse\x12r\n\x0fPrepareCosmosTx\x12..injective_exchange_rpc.PrepareCosmosTxRequest\x1a/.injective_exchange_rpc.PrepareCosmosTxResponse\x12x\n\x11\x42roadcastCosmosTx\x12\x30.injective_exchange_rpc.BroadcastCosmosTxRequest\x1a\x31.injective_exchange_rpc.BroadcastCosmosTxResponse\x12\x66\n\x0bGetFeePayer\x12*.injective_exchange_rpc.GetFeePayerRequest\x1a+.injective_exchange_rpc.GetFeePayerResponseB\x1bZ\x19/injective_exchange_rpcpbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exchange.injective_exchange_rpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\031/injective_exchange_rpcpb'
  _globals['_GETTXREQUEST']._serialized_start=65
  _globals['_GETTXREQUEST']._serialized_end=93
  _globals['_GETTXRESPONSE']._serialized_start=96
  _globals['_GETTXRESPONSE']._serialized_end=242
  _globals['_PREPARETXREQUEST']._serialized_start=245
  _globals['_PREPARETXREQUEST']._serialized_end=425
  _globals['_COSMOSTXFEE']._serialized_start=427
  _globals['_COSMOSTXFEE']._serialized_end=526
  _globals['_COSMOSCOIN']._serialized_start=528
  _globals['_COSMOSCOIN']._serialized_end=571
  _globals['_PREPARETXRESPONSE']._serialized_start=574
  _globals['_PREPARETXRESPONSE']._serialized_end=708
  _globals['_BROADCASTTXREQUEST']._serialized_start=711
  _globals['_BROADCASTTXREQUEST']._serialized_end=905
  _globals['_COSMOSPUBKEY']._serialized_start=907
  _globals['_COSMOSPUBKEY']._serialized_end=948
  _globals['_BROADCASTTXRESPONSE']._serialized_start=951
  _globals['_BROADCASTTXRESPONSE']._serialized_end=1103
  _globals['_PREPARECOSMOSTXREQUEST']._serialized_start=1106
  _globals['_PREPARECOSMOSTXREQUEST']._serialized_end=1274
  _globals['_PREPARECOSMOSTXRESPONSE']._serialized_start=1277
  _globals['_PREPARECOSMOSTXRESPONSE']._serialized_end=1462
  _globals['_BROADCASTCOSMOSTXREQUEST']._serialized_start=1465
  _globals['_BROADCASTCOSMOSTXREQUEST']._serialized_end=1601
  _globals['_BROADCASTCOSMOSTXRESPONSE']._serialized_start=1604
  _globals['_BROADCASTCOSMOSTXRESPONSE']._serialized_end=1762
  _globals['_GETFEEPAYERREQUEST']._serialized_start=1764
  _globals['_GETFEEPAYERREQUEST']._serialized_end=1784
  _globals['_GETFEEPAYERRESPONSE']._serialized_start=1786
  _globals['_GETFEEPAYERRESPONSE']._serialized_end=1891
  _globals['_INJECTIVEEXCHANGERPC']._serialized_start=1894
  _globals['_INJECTIVEEXCHANGERPC']._serialized_end=2546
# @@protoc_insertion_point(module_scope)
