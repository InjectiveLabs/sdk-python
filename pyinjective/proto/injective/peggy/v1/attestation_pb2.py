# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/peggy/v1/attestation.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$injective/peggy/v1/attestation.proto\x12\x12injective.peggy.v1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\"\x83\x01\n\x0b\x41ttestation\x12\x1a\n\x08observed\x18\x01 \x01(\x08R\x08observed\x12\x14\n\x05votes\x18\x02 \x03(\tR\x05votes\x12\x16\n\x06height\x18\x03 \x01(\x04R\x06height\x12*\n\x05\x63laim\x18\x04 \x01(\x0b\x32\x14.google.protobuf.AnyR\x05\x63laim\"p\n\nERC20Token\x12\x1a\n\x08\x63ontract\x18\x01 \x01(\tR\x08\x63ontract\x12\x46\n\x06\x61mount\x18\x02 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.IntR\x06\x61mount*\x9f\x02\n\tClaimType\x12.\n\x12\x43LAIM_TYPE_UNKNOWN\x10\x00\x1a\x16\x8a\x9d \x12\x43LAIM_TYPE_UNKNOWN\x12.\n\x12\x43LAIM_TYPE_DEPOSIT\x10\x01\x1a\x16\x8a\x9d \x12\x43LAIM_TYPE_DEPOSIT\x12\x30\n\x13\x43LAIM_TYPE_WITHDRAW\x10\x02\x1a\x17\x8a\x9d \x13\x43LAIM_TYPE_WITHDRAW\x12<\n\x19\x43LAIM_TYPE_ERC20_DEPLOYED\x10\x03\x1a\x1d\x8a\x9d \x19\x43LAIM_TYPE_ERC20_DEPLOYED\x12<\n\x19\x43LAIM_TYPE_VALSET_UPDATED\x10\x04\x1a\x1d\x8a\x9d \x19\x43LAIM_TYPE_VALSET_UPDATED\x1a\x04\x88\xa3\x1e\x00\x42\xe1\x01\n\x16\x63om.injective.peggy.v1B\x10\x41ttestationProtoP\x01ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/types\xa2\x02\x03IPX\xaa\x02\x12Injective.Peggy.V1\xca\x02\x12Injective\\Peggy\\V1\xe2\x02\x1eInjective\\Peggy\\V1\\GPBMetadata\xea\x02\x14Injective::Peggy::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.peggy.v1.attestation_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.injective.peggy.v1B\020AttestationProtoP\001ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/types\242\002\003IPX\252\002\022Injective.Peggy.V1\312\002\022Injective\\Peggy\\V1\342\002\036Injective\\Peggy\\V1\\GPBMetadata\352\002\024Injective::Peggy::V1'
  _globals['_CLAIMTYPE']._options = None
  _globals['_CLAIMTYPE']._serialized_options = b'\210\243\036\000'
  _globals['_CLAIMTYPE'].values_by_name["CLAIM_TYPE_UNKNOWN"]._options = None
  _globals['_CLAIMTYPE'].values_by_name["CLAIM_TYPE_UNKNOWN"]._serialized_options = b'\212\235 \022CLAIM_TYPE_UNKNOWN'
  _globals['_CLAIMTYPE'].values_by_name["CLAIM_TYPE_DEPOSIT"]._options = None
  _globals['_CLAIMTYPE'].values_by_name["CLAIM_TYPE_DEPOSIT"]._serialized_options = b'\212\235 \022CLAIM_TYPE_DEPOSIT'
  _globals['_CLAIMTYPE'].values_by_name["CLAIM_TYPE_WITHDRAW"]._options = None
  _globals['_CLAIMTYPE'].values_by_name["CLAIM_TYPE_WITHDRAW"]._serialized_options = b'\212\235 \023CLAIM_TYPE_WITHDRAW'
  _globals['_CLAIMTYPE'].values_by_name["CLAIM_TYPE_ERC20_DEPLOYED"]._options = None
  _globals['_CLAIMTYPE'].values_by_name["CLAIM_TYPE_ERC20_DEPLOYED"]._serialized_options = b'\212\235 \031CLAIM_TYPE_ERC20_DEPLOYED'
  _globals['_CLAIMTYPE'].values_by_name["CLAIM_TYPE_VALSET_UPDATED"]._options = None
  _globals['_CLAIMTYPE'].values_by_name["CLAIM_TYPE_VALSET_UPDATED"]._serialized_options = b'\212\235 \031CLAIM_TYPE_VALSET_UPDATED'
  _globals['_ERC20TOKEN'].fields_by_name['amount']._options = None
  _globals['_ERC20TOKEN'].fields_by_name['amount']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int'
  _globals['_CLAIMTYPE']._serialized_start=358
  _globals['_CLAIMTYPE']._serialized_end=645
  _globals['_ATTESTATION']._serialized_start=110
  _globals['_ATTESTATION']._serialized_end=241
  _globals['_ERC20TOKEN']._serialized_start=243
  _globals['_ERC20TOKEN']._serialized_end=355
# @@protoc_insertion_point(module_scope)
