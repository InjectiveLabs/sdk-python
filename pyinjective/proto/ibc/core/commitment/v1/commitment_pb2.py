# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/commitment/v1/commitment.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from tendermint.crypto import proof_pb2 as tendermint_dot_crypto_dot_proof__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ibc/core/commitment/v1/commitment.proto',
  package='ibc.core.commitment.v1',
  syntax='proto3',
  serialized_options=b'Z;github.com/cosmos/cosmos-sdk/x/ibc/core/23-commitment/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'ibc/core/commitment/v1/commitment.proto\x12\x16ibc.core.commitment.v1\x1a\x14gogoproto/gogo.proto\x1a\x1dtendermint/crypto/proof.proto\" \n\nMerkleRoot\x12\x0c\n\x04hash\x18\x01 \x01(\x0c:\x04\x88\xa0\x1f\x00\"9\n\x0cMerklePrefix\x12)\n\nkey_prefix\x18\x01 \x01(\x0c\x42\x15\xf2\xde\x1f\x11yaml:\"key_prefix\"\"^\n\nMerklePath\x12J\n\x08key_path\x18\x01 \x01(\x0b\x32\x1f.ibc.core.commitment.v1.KeyPathB\x17\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:\"key_path\":\x04\x98\xa0\x1f\x00\"9\n\x0bMerkleProof\x12*\n\x05proof\x18\x01 \x01(\x0b\x32\x1b.tendermint.crypto.ProofOps\">\n\x07KeyPath\x12)\n\x04keys\x18\x01 \x03(\x0b\x32\x1b.ibc.core.commitment.v1.Key:\x08\x98\xa0\x1f\x00\x88\xa0\x1f\x00\"K\n\x03Key\x12\x0c\n\x04name\x18\x01 \x01(\x0c\x12\x30\n\x03\x65nc\x18\x02 \x01(\x0e\x32#.ibc.core.commitment.v1.KeyEncoding:\x04\x88\xa0\x1f\x00*]\n\x0bKeyEncoding\x12)\n\x1cKEY_ENCODING_URL_UNSPECIFIED\x10\x00\x1a\x07\x8a\x9d \x03URL\x12\x1d\n\x10KEY_ENCODING_HEX\x10\x01\x1a\x07\x8a\x9d \x03HEX\x1a\x04\x88\xa3\x1e\x00\x42=Z;github.com/cosmos/cosmos-sdk/x/ibc/core/23-commitment/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,tendermint_dot_crypto_dot_proof__pb2.DESCRIPTOR,])

_KEYENCODING = _descriptor.EnumDescriptor(
  name='KeyEncoding',
  full_name='ibc.core.commitment.v1.KeyEncoding',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='KEY_ENCODING_URL_UNSPECIFIED', index=0, number=0,
      serialized_options=b'\212\235 \003URL',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEY_ENCODING_HEX', index=1, number=1,
      serialized_options=b'\212\235 \003HEX',
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=b'\210\243\036\000',
  serialized_start=509,
  serialized_end=602,
)
_sym_db.RegisterEnumDescriptor(_KEYENCODING)

KeyEncoding = enum_type_wrapper.EnumTypeWrapper(_KEYENCODING)
KEY_ENCODING_URL_UNSPECIFIED = 0
KEY_ENCODING_HEX = 1



_MERKLEROOT = _descriptor.Descriptor(
  name='MerkleRoot',
  full_name='ibc.core.commitment.v1.MerkleRoot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='ibc.core.commitment.v1.MerkleRoot.hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=152,
)


_MERKLEPREFIX = _descriptor.Descriptor(
  name='MerklePrefix',
  full_name='ibc.core.commitment.v1.MerklePrefix',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_prefix', full_name='ibc.core.commitment.v1.MerklePrefix.key_prefix', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\021yaml:\"key_prefix\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=154,
  serialized_end=211,
)


_MERKLEPATH = _descriptor.Descriptor(
  name='MerklePath',
  full_name='ibc.core.commitment.v1.MerklePath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_path', full_name='ibc.core.commitment.v1.MerklePath.key_path', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\362\336\037\017yaml:\"key_path\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\230\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=213,
  serialized_end=307,
)


_MERKLEPROOF = _descriptor.Descriptor(
  name='MerkleProof',
  full_name='ibc.core.commitment.v1.MerkleProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='proof', full_name='ibc.core.commitment.v1.MerkleProof.proof', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=309,
  serialized_end=366,
)


_KEYPATH = _descriptor.Descriptor(
  name='KeyPath',
  full_name='ibc.core.commitment.v1.KeyPath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='keys', full_name='ibc.core.commitment.v1.KeyPath.keys', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\230\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=368,
  serialized_end=430,
)


_KEY = _descriptor.Descriptor(
  name='Key',
  full_name='ibc.core.commitment.v1.Key',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ibc.core.commitment.v1.Key.name', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enc', full_name='ibc.core.commitment.v1.Key.enc', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=432,
  serialized_end=507,
)

_MERKLEPATH.fields_by_name['key_path'].message_type = _KEYPATH
_MERKLEPROOF.fields_by_name['proof'].message_type = tendermint_dot_crypto_dot_proof__pb2._PROOFOPS
_KEYPATH.fields_by_name['keys'].message_type = _KEY
_KEY.fields_by_name['enc'].enum_type = _KEYENCODING
DESCRIPTOR.message_types_by_name['MerkleRoot'] = _MERKLEROOT
DESCRIPTOR.message_types_by_name['MerklePrefix'] = _MERKLEPREFIX
DESCRIPTOR.message_types_by_name['MerklePath'] = _MERKLEPATH
DESCRIPTOR.message_types_by_name['MerkleProof'] = _MERKLEPROOF
DESCRIPTOR.message_types_by_name['KeyPath'] = _KEYPATH
DESCRIPTOR.message_types_by_name['Key'] = _KEY
DESCRIPTOR.enum_types_by_name['KeyEncoding'] = _KEYENCODING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MerkleRoot = _reflection.GeneratedProtocolMessageType('MerkleRoot', (_message.Message,), {
  'DESCRIPTOR' : _MERKLEROOT,
  '__module__' : 'ibc.core.commitment.v1.commitment_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.commitment.v1.MerkleRoot)
  })
_sym_db.RegisterMessage(MerkleRoot)

MerklePrefix = _reflection.GeneratedProtocolMessageType('MerklePrefix', (_message.Message,), {
  'DESCRIPTOR' : _MERKLEPREFIX,
  '__module__' : 'ibc.core.commitment.v1.commitment_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.commitment.v1.MerklePrefix)
  })
_sym_db.RegisterMessage(MerklePrefix)

MerklePath = _reflection.GeneratedProtocolMessageType('MerklePath', (_message.Message,), {
  'DESCRIPTOR' : _MERKLEPATH,
  '__module__' : 'ibc.core.commitment.v1.commitment_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.commitment.v1.MerklePath)
  })
_sym_db.RegisterMessage(MerklePath)

MerkleProof = _reflection.GeneratedProtocolMessageType('MerkleProof', (_message.Message,), {
  'DESCRIPTOR' : _MERKLEPROOF,
  '__module__' : 'ibc.core.commitment.v1.commitment_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.commitment.v1.MerkleProof)
  })
_sym_db.RegisterMessage(MerkleProof)

KeyPath = _reflection.GeneratedProtocolMessageType('KeyPath', (_message.Message,), {
  'DESCRIPTOR' : _KEYPATH,
  '__module__' : 'ibc.core.commitment.v1.commitment_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.commitment.v1.KeyPath)
  })
_sym_db.RegisterMessage(KeyPath)

Key = _reflection.GeneratedProtocolMessageType('Key', (_message.Message,), {
  'DESCRIPTOR' : _KEY,
  '__module__' : 'ibc.core.commitment.v1.commitment_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.commitment.v1.Key)
  })
_sym_db.RegisterMessage(Key)


DESCRIPTOR._options = None
_KEYENCODING._options = None
_KEYENCODING.values_by_name["KEY_ENCODING_URL_UNSPECIFIED"]._options = None
_KEYENCODING.values_by_name["KEY_ENCODING_HEX"]._options = None
_MERKLEROOT._options = None
_MERKLEPREFIX.fields_by_name['key_prefix']._options = None
_MERKLEPATH.fields_by_name['key_path']._options = None
_MERKLEPATH._options = None
_KEYPATH._options = None
_KEY._options = None
# @@protoc_insertion_point(module_scope)
