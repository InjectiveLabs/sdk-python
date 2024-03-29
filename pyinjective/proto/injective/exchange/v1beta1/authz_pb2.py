# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/exchange/v1beta1/authz.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&injective/exchange/v1beta1/authz.proto\x12\x1ainjective.exchange.v1beta1\x1a\x19\x63osmos_proto/cosmos.proto\"Y\n\x19\x43reateSpotLimitOrderAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:\x11\xca\xb4-\rAuthorization\"Z\n\x1a\x43reateSpotMarketOrderAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:\x11\xca\xb4-\rAuthorization\"_\n\x1f\x42\x61tchCreateSpotLimitOrdersAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:\x11\xca\xb4-\rAuthorization\"T\n\x14\x43\x61ncelSpotOrderAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:\x11\xca\xb4-\rAuthorization\"Z\n\x1a\x42\x61tchCancelSpotOrdersAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:\x11\xca\xb4-\rAuthorization\"_\n\x1f\x43reateDerivativeLimitOrderAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:\x11\xca\xb4-\rAuthorization\"`\n CreateDerivativeMarketOrderAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:\x11\xca\xb4-\rAuthorization\"e\n%BatchCreateDerivativeLimitOrdersAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:\x11\xca\xb4-\rAuthorization\"Z\n\x1a\x43\x61ncelDerivativeOrderAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:\x11\xca\xb4-\rAuthorization\"`\n BatchCancelDerivativeOrdersAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:\x11\xca\xb4-\rAuthorization\"t\n\x16\x42\x61tchUpdateOrdersAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x14\n\x0cspot_markets\x18\x02 \x03(\t\x12\x1a\n\x12\x64\x65rivative_markets\x18\x03 \x03(\t:\x11\xca\xb4-\rAuthorizationBPZNgithub.com/InjectiveLabs/injective-core/injective-chain/modules/exchange/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.exchange.v1beta1.authz_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZNgithub.com/InjectiveLabs/injective-core/injective-chain/modules/exchange/types'
  _globals['_CREATESPOTLIMITORDERAUTHZ']._options = None
  _globals['_CREATESPOTLIMITORDERAUTHZ']._serialized_options = b'\312\264-\rAuthorization'
  _globals['_CREATESPOTMARKETORDERAUTHZ']._options = None
  _globals['_CREATESPOTMARKETORDERAUTHZ']._serialized_options = b'\312\264-\rAuthorization'
  _globals['_BATCHCREATESPOTLIMITORDERSAUTHZ']._options = None
  _globals['_BATCHCREATESPOTLIMITORDERSAUTHZ']._serialized_options = b'\312\264-\rAuthorization'
  _globals['_CANCELSPOTORDERAUTHZ']._options = None
  _globals['_CANCELSPOTORDERAUTHZ']._serialized_options = b'\312\264-\rAuthorization'
  _globals['_BATCHCANCELSPOTORDERSAUTHZ']._options = None
  _globals['_BATCHCANCELSPOTORDERSAUTHZ']._serialized_options = b'\312\264-\rAuthorization'
  _globals['_CREATEDERIVATIVELIMITORDERAUTHZ']._options = None
  _globals['_CREATEDERIVATIVELIMITORDERAUTHZ']._serialized_options = b'\312\264-\rAuthorization'
  _globals['_CREATEDERIVATIVEMARKETORDERAUTHZ']._options = None
  _globals['_CREATEDERIVATIVEMARKETORDERAUTHZ']._serialized_options = b'\312\264-\rAuthorization'
  _globals['_BATCHCREATEDERIVATIVELIMITORDERSAUTHZ']._options = None
  _globals['_BATCHCREATEDERIVATIVELIMITORDERSAUTHZ']._serialized_options = b'\312\264-\rAuthorization'
  _globals['_CANCELDERIVATIVEORDERAUTHZ']._options = None
  _globals['_CANCELDERIVATIVEORDERAUTHZ']._serialized_options = b'\312\264-\rAuthorization'
  _globals['_BATCHCANCELDERIVATIVEORDERSAUTHZ']._options = None
  _globals['_BATCHCANCELDERIVATIVEORDERSAUTHZ']._serialized_options = b'\312\264-\rAuthorization'
  _globals['_BATCHUPDATEORDERSAUTHZ']._options = None
  _globals['_BATCHUPDATEORDERSAUTHZ']._serialized_options = b'\312\264-\rAuthorization'
  _globals['_CREATESPOTLIMITORDERAUTHZ']._serialized_start=97
  _globals['_CREATESPOTLIMITORDERAUTHZ']._serialized_end=186
  _globals['_CREATESPOTMARKETORDERAUTHZ']._serialized_start=188
  _globals['_CREATESPOTMARKETORDERAUTHZ']._serialized_end=278
  _globals['_BATCHCREATESPOTLIMITORDERSAUTHZ']._serialized_start=280
  _globals['_BATCHCREATESPOTLIMITORDERSAUTHZ']._serialized_end=375
  _globals['_CANCELSPOTORDERAUTHZ']._serialized_start=377
  _globals['_CANCELSPOTORDERAUTHZ']._serialized_end=461
  _globals['_BATCHCANCELSPOTORDERSAUTHZ']._serialized_start=463
  _globals['_BATCHCANCELSPOTORDERSAUTHZ']._serialized_end=553
  _globals['_CREATEDERIVATIVELIMITORDERAUTHZ']._serialized_start=555
  _globals['_CREATEDERIVATIVELIMITORDERAUTHZ']._serialized_end=650
  _globals['_CREATEDERIVATIVEMARKETORDERAUTHZ']._serialized_start=652
  _globals['_CREATEDERIVATIVEMARKETORDERAUTHZ']._serialized_end=748
  _globals['_BATCHCREATEDERIVATIVELIMITORDERSAUTHZ']._serialized_start=750
  _globals['_BATCHCREATEDERIVATIVELIMITORDERSAUTHZ']._serialized_end=851
  _globals['_CANCELDERIVATIVEORDERAUTHZ']._serialized_start=853
  _globals['_CANCELDERIVATIVEORDERAUTHZ']._serialized_end=943
  _globals['_BATCHCANCELDERIVATIVEORDERSAUTHZ']._serialized_start=945
  _globals['_BATCHCANCELDERIVATIVEORDERSAUTHZ']._serialized_end=1041
  _globals['_BATCHUPDATEORDERSAUTHZ']._serialized_start=1043
  _globals['_BATCHUPDATEORDERSAUTHZ']._serialized_end=1159
# @@protoc_insertion_point(module_scope)
