# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/wasmx/v1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective.wasmx.v1 import wasmx_pb2 as injective_dot_wasmx_dot_v1_dot_wasmx__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n injective/wasmx/v1/genesis.proto\x12\x12injective.wasmx.v1\x1a\x1einjective/wasmx/v1/wasmx.proto\x1a\x14gogoproto/gogo.proto\"u\n\x1dRegisteredContractWithAddress\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x43\n\x13registered_contract\x18\x02 \x01(\x0b\x32&.injective.wasmx.v1.RegisteredContract\"\x97\x01\n\x0cGenesisState\x12\x30\n\x06params\x18\x01 \x01(\x0b\x32\x1a.injective.wasmx.v1.ParamsB\x04\xc8\xde\x1f\x00\x12U\n\x14registered_contracts\x18\x02 \x03(\x0b\x32\x31.injective.wasmx.v1.RegisteredContractWithAddressB\x04\xc8\xde\x1f\x00\x42MZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/wasmx/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.wasmx.v1.genesis_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/wasmx/types'
  _GENESISSTATE.fields_by_name['params']._options = None
  _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['registered_contracts']._options = None
  _GENESISSTATE.fields_by_name['registered_contracts']._serialized_options = b'\310\336\037\000'
  _REGISTEREDCONTRACTWITHADDRESS._serialized_start=110
  _REGISTEREDCONTRACTWITHADDRESS._serialized_end=227
  _GENESISSTATE._serialized_start=230
  _GENESISSTATE._serialized_end=381
# @@protoc_insertion_point(module_scope)
