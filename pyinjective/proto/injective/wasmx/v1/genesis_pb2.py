# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/wasmx/v1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective.wasmx.v1 import wasmx_pb2 as injective_dot_wasmx_dot_v1_dot_wasmx__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='injective/wasmx/v1/genesis.proto',
  package='injective.wasmx.v1',
  syntax='proto3',
  serialized_options=b'ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/wasmx/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n injective/wasmx/v1/genesis.proto\x12\x12injective.wasmx.v1\x1a\x1einjective/wasmx/v1/wasmx.proto\x1a\x14gogoproto/gogo.proto\"u\n\x1dRegisteredContractWithAddress\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x43\n\x13registered_contract\x18\x02 \x01(\x0b\x32&.injective.wasmx.v1.RegisteredContract\"\x97\x01\n\x0cGenesisState\x12\x30\n\x06params\x18\x01 \x01(\x0b\x32\x1a.injective.wasmx.v1.ParamsB\x04\xc8\xde\x1f\x00\x12U\n\x14registered_contracts\x18\x02 \x03(\x0b\x32\x31.injective.wasmx.v1.RegisteredContractWithAddressB\x04\xc8\xde\x1f\x00\x42MZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/wasmx/typesb\x06proto3'
  ,
  dependencies=[injective_dot_wasmx_dot_v1_dot_wasmx__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_REGISTEREDCONTRACTWITHADDRESS = _descriptor.Descriptor(
  name='RegisteredContractWithAddress',
  full_name='injective.wasmx.v1.RegisteredContractWithAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='injective.wasmx.v1.RegisteredContractWithAddress.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='registered_contract', full_name='injective.wasmx.v1.RegisteredContractWithAddress.registered_contract', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=227,
)


_GENESISSTATE = _descriptor.Descriptor(
  name='GenesisState',
  full_name='injective.wasmx.v1.GenesisState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='injective.wasmx.v1.GenesisState.params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='registered_contracts', full_name='injective.wasmx.v1.GenesisState.registered_contracts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=230,
  serialized_end=381,
)

_REGISTEREDCONTRACTWITHADDRESS.fields_by_name['registered_contract'].message_type = injective_dot_wasmx_dot_v1_dot_wasmx__pb2._REGISTEREDCONTRACT
_GENESISSTATE.fields_by_name['params'].message_type = injective_dot_wasmx_dot_v1_dot_wasmx__pb2._PARAMS
_GENESISSTATE.fields_by_name['registered_contracts'].message_type = _REGISTEREDCONTRACTWITHADDRESS
DESCRIPTOR.message_types_by_name['RegisteredContractWithAddress'] = _REGISTEREDCONTRACTWITHADDRESS
DESCRIPTOR.message_types_by_name['GenesisState'] = _GENESISSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegisteredContractWithAddress = _reflection.GeneratedProtocolMessageType('RegisteredContractWithAddress', (_message.Message,), {
  'DESCRIPTOR' : _REGISTEREDCONTRACTWITHADDRESS,
  '__module__' : 'injective.wasmx.v1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:injective.wasmx.v1.RegisteredContractWithAddress)
  })
_sym_db.RegisterMessage(RegisteredContractWithAddress)

GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'injective.wasmx.v1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:injective.wasmx.v1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)


DESCRIPTOR._options = None
_GENESISSTATE.fields_by_name['params']._options = None
_GENESISSTATE.fields_by_name['registered_contracts']._options = None
# @@protoc_insertion_point(module_scope)