# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/crypto/ed25519/keys.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2
from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/crypto/ed25519/keys.proto\x12\x15\x63osmos.crypto.ed25519\x1a\x11\x61mino/amino.proto\x1a\x14gogoproto/gogo.proto\"i\n\x06PubKey\x12.\n\x03key\x18\x01 \x01(\x0c\x42\x1c\xfa\xde\x1f\x18\x63rypto/ed25519.PublicKeyR\x03key:/\x98\xa0\x1f\x00\x8a\xe7\xb0*\x18tendermint/PubKeyEd25519\x92\xe7\xb0*\tkey_field\"h\n\x07PrivKey\x12/\n\x03key\x18\x01 \x01(\x0c\x42\x1d\xfa\xde\x1f\x19\x63rypto/ed25519.PrivateKeyR\x03key:,\x8a\xe7\xb0*\x19tendermint/PrivKeyEd25519\x92\xe7\xb0*\tkey_fieldB\xce\x01\n\x19\x63om.cosmos.crypto.ed25519B\tKeysProtoP\x01Z0github.com/cosmos/cosmos-sdk/crypto/keys/ed25519\xa2\x02\x03\x43\x43\x45\xaa\x02\x15\x43osmos.Crypto.Ed25519\xca\x02\x15\x43osmos\\Crypto\\Ed25519\xe2\x02!Cosmos\\Crypto\\Ed25519\\GPBMetadata\xea\x02\x17\x43osmos::Crypto::Ed25519b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.crypto.ed25519.keys_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.cosmos.crypto.ed25519B\tKeysProtoP\001Z0github.com/cosmos/cosmos-sdk/crypto/keys/ed25519\242\002\003CCE\252\002\025Cosmos.Crypto.Ed25519\312\002\025Cosmos\\Crypto\\Ed25519\342\002!Cosmos\\Crypto\\Ed25519\\GPBMetadata\352\002\027Cosmos::Crypto::Ed25519'
  _globals['_PUBKEY'].fields_by_name['key']._options = None
  _globals['_PUBKEY'].fields_by_name['key']._serialized_options = b'\372\336\037\030crypto/ed25519.PublicKey'
  _globals['_PUBKEY']._options = None
  _globals['_PUBKEY']._serialized_options = b'\230\240\037\000\212\347\260*\030tendermint/PubKeyEd25519\222\347\260*\tkey_field'
  _globals['_PRIVKEY'].fields_by_name['key']._options = None
  _globals['_PRIVKEY'].fields_by_name['key']._serialized_options = b'\372\336\037\031crypto/ed25519.PrivateKey'
  _globals['_PRIVKEY']._options = None
  _globals['_PRIVKEY']._serialized_options = b'\212\347\260*\031tendermint/PrivKeyEd25519\222\347\260*\tkey_field'
  _globals['_PUBKEY']._serialized_start=100
  _globals['_PUBKEY']._serialized_end=205
  _globals['_PRIVKEY']._serialized_start=207
  _globals['_PRIVKEY']._serialized_end=311
# @@protoc_insertion_point(module_scope)
