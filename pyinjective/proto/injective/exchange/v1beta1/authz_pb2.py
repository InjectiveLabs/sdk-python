# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/exchange/v1beta1/authz.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&injective/exchange/v1beta1/authz.proto\x12\x1ainjective.exchange.v1beta1\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x11\x61mino/amino.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\"\x99\x01\n\x19\x43reateSpotLimitOrderAuthz\x12#\n\rsubaccount_id\x18\x01 \x01(\tR\x0csubaccountId\x12\x1d\n\nmarket_ids\x18\x02 \x03(\tR\tmarketIds:8\xca\xb4-\rAuthorization\x8a\xe7\xb0*\"exchange/CreateSpotLimitOrderAuthz\"\x9b\x01\n\x1a\x43reateSpotMarketOrderAuthz\x12#\n\rsubaccount_id\x18\x01 \x01(\tR\x0csubaccountId\x12\x1d\n\nmarket_ids\x18\x02 \x03(\tR\tmarketIds:9\xca\xb4-\rAuthorization\x8a\xe7\xb0*#exchange/CreateSpotMarketOrderAuthz\"\xa5\x01\n\x1f\x42\x61tchCreateSpotLimitOrdersAuthz\x12#\n\rsubaccount_id\x18\x01 \x01(\tR\x0csubaccountId\x12\x1d\n\nmarket_ids\x18\x02 \x03(\tR\tmarketIds:>\xca\xb4-\rAuthorization\x8a\xe7\xb0*(exchange/BatchCreateSpotLimitOrdersAuthz\"\x8f\x01\n\x14\x43\x61ncelSpotOrderAuthz\x12#\n\rsubaccount_id\x18\x01 \x01(\tR\x0csubaccountId\x12\x1d\n\nmarket_ids\x18\x02 \x03(\tR\tmarketIds:3\xca\xb4-\rAuthorization\x8a\xe7\xb0*\x1d\x65xchange/CancelSpotOrderAuthz\"\x9b\x01\n\x1a\x42\x61tchCancelSpotOrdersAuthz\x12#\n\rsubaccount_id\x18\x01 \x01(\tR\x0csubaccountId\x12\x1d\n\nmarket_ids\x18\x02 \x03(\tR\tmarketIds:9\xca\xb4-\rAuthorization\x8a\xe7\xb0*#exchange/BatchCancelSpotOrdersAuthz\"\xa5\x01\n\x1f\x43reateDerivativeLimitOrderAuthz\x12#\n\rsubaccount_id\x18\x01 \x01(\tR\x0csubaccountId\x12\x1d\n\nmarket_ids\x18\x02 \x03(\tR\tmarketIds:>\xca\xb4-\rAuthorization\x8a\xe7\xb0*(exchange/CreateDerivativeLimitOrderAuthz\"\xa7\x01\n CreateDerivativeMarketOrderAuthz\x12#\n\rsubaccount_id\x18\x01 \x01(\tR\x0csubaccountId\x12\x1d\n\nmarket_ids\x18\x02 \x03(\tR\tmarketIds:?\xca\xb4-\rAuthorization\x8a\xe7\xb0*)exchange/CreateDerivativeMarketOrderAuthz\"\xb1\x01\n%BatchCreateDerivativeLimitOrdersAuthz\x12#\n\rsubaccount_id\x18\x01 \x01(\tR\x0csubaccountId\x12\x1d\n\nmarket_ids\x18\x02 \x03(\tR\tmarketIds:D\xca\xb4-\rAuthorization\x8a\xe7\xb0*.exchange/BatchCreateDerivativeLimitOrdersAuthz\"\x9b\x01\n\x1a\x43\x61ncelDerivativeOrderAuthz\x12#\n\rsubaccount_id\x18\x01 \x01(\tR\x0csubaccountId\x12\x1d\n\nmarket_ids\x18\x02 \x03(\tR\tmarketIds:9\xca\xb4-\rAuthorization\x8a\xe7\xb0*#exchange/CancelDerivativeOrderAuthz\"\xa7\x01\n BatchCancelDerivativeOrdersAuthz\x12#\n\rsubaccount_id\x18\x01 \x01(\tR\x0csubaccountId\x12\x1d\n\nmarket_ids\x18\x02 \x03(\tR\tmarketIds:?\xca\xb4-\rAuthorization\x8a\xe7\xb0*)exchange/BatchCancelDerivativeOrdersAuthz\"\xc6\x01\n\x16\x42\x61tchUpdateOrdersAuthz\x12#\n\rsubaccount_id\x18\x01 \x01(\tR\x0csubaccountId\x12!\n\x0cspot_markets\x18\x02 \x03(\tR\x0bspotMarkets\x12-\n\x12\x64\x65rivative_markets\x18\x03 \x03(\tR\x11\x64\x65rivativeMarkets:5\xca\xb4-\rAuthorization\x8a\xe7\xb0*\x1f\x65xchange/BatchUpdateOrdersAuthz\"\x89\x02\n\x1cGenericExchangeAuthorization\x12\x10\n\x03msg\x18\x01 \x01(\tR\x03msg\x12\x82\x01\n\x0bspend_limit\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01R\nspendLimit:R\xca\xb4-\"cosmos.authz.v1beta1.Authorization\x8a\xe7\xb0*\'cosmos-sdk/GenericExchangeAuthorizationB\x86\x02\n\x1e\x63om.injective.exchange.v1beta1B\nAuthzProtoP\x01ZNgithub.com/InjectiveLabs/injective-core/injective-chain/modules/exchange/types\xa2\x02\x03IEX\xaa\x02\x1aInjective.Exchange.V1beta1\xca\x02\x1aInjective\\Exchange\\V1beta1\xe2\x02&Injective\\Exchange\\V1beta1\\GPBMetadata\xea\x02\x1cInjective::Exchange::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.exchange.v1beta1.authz_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.injective.exchange.v1beta1B\nAuthzProtoP\001ZNgithub.com/InjectiveLabs/injective-core/injective-chain/modules/exchange/types\242\002\003IEX\252\002\032Injective.Exchange.V1beta1\312\002\032Injective\\Exchange\\V1beta1\342\002&Injective\\Exchange\\V1beta1\\GPBMetadata\352\002\034Injective::Exchange::V1beta1'
  _globals['_CREATESPOTLIMITORDERAUTHZ']._loaded_options = None
  _globals['_CREATESPOTLIMITORDERAUTHZ']._serialized_options = b'\312\264-\rAuthorization\212\347\260*\"exchange/CreateSpotLimitOrderAuthz'
  _globals['_CREATESPOTMARKETORDERAUTHZ']._loaded_options = None
  _globals['_CREATESPOTMARKETORDERAUTHZ']._serialized_options = b'\312\264-\rAuthorization\212\347\260*#exchange/CreateSpotMarketOrderAuthz'
  _globals['_BATCHCREATESPOTLIMITORDERSAUTHZ']._loaded_options = None
  _globals['_BATCHCREATESPOTLIMITORDERSAUTHZ']._serialized_options = b'\312\264-\rAuthorization\212\347\260*(exchange/BatchCreateSpotLimitOrdersAuthz'
  _globals['_CANCELSPOTORDERAUTHZ']._loaded_options = None
  _globals['_CANCELSPOTORDERAUTHZ']._serialized_options = b'\312\264-\rAuthorization\212\347\260*\035exchange/CancelSpotOrderAuthz'
  _globals['_BATCHCANCELSPOTORDERSAUTHZ']._loaded_options = None
  _globals['_BATCHCANCELSPOTORDERSAUTHZ']._serialized_options = b'\312\264-\rAuthorization\212\347\260*#exchange/BatchCancelSpotOrdersAuthz'
  _globals['_CREATEDERIVATIVELIMITORDERAUTHZ']._loaded_options = None
  _globals['_CREATEDERIVATIVELIMITORDERAUTHZ']._serialized_options = b'\312\264-\rAuthorization\212\347\260*(exchange/CreateDerivativeLimitOrderAuthz'
  _globals['_CREATEDERIVATIVEMARKETORDERAUTHZ']._loaded_options = None
  _globals['_CREATEDERIVATIVEMARKETORDERAUTHZ']._serialized_options = b'\312\264-\rAuthorization\212\347\260*)exchange/CreateDerivativeMarketOrderAuthz'
  _globals['_BATCHCREATEDERIVATIVELIMITORDERSAUTHZ']._loaded_options = None
  _globals['_BATCHCREATEDERIVATIVELIMITORDERSAUTHZ']._serialized_options = b'\312\264-\rAuthorization\212\347\260*.exchange/BatchCreateDerivativeLimitOrdersAuthz'
  _globals['_CANCELDERIVATIVEORDERAUTHZ']._loaded_options = None
  _globals['_CANCELDERIVATIVEORDERAUTHZ']._serialized_options = b'\312\264-\rAuthorization\212\347\260*#exchange/CancelDerivativeOrderAuthz'
  _globals['_BATCHCANCELDERIVATIVEORDERSAUTHZ']._loaded_options = None
  _globals['_BATCHCANCELDERIVATIVEORDERSAUTHZ']._serialized_options = b'\312\264-\rAuthorization\212\347\260*)exchange/BatchCancelDerivativeOrdersAuthz'
  _globals['_BATCHUPDATEORDERSAUTHZ']._loaded_options = None
  _globals['_BATCHUPDATEORDERSAUTHZ']._serialized_options = b'\312\264-\rAuthorization\212\347\260*\037exchange/BatchUpdateOrdersAuthz'
  _globals['_GENERICEXCHANGEAUTHORIZATION'].fields_by_name['spend_limit']._loaded_options = None
  _globals['_GENERICEXCHANGEAUTHORIZATION'].fields_by_name['spend_limit']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\232\347\260*\014legacy_coins\250\347\260*\001'
  _globals['_GENERICEXCHANGEAUTHORIZATION']._loaded_options = None
  _globals['_GENERICEXCHANGEAUTHORIZATION']._serialized_options = b'\312\264-\"cosmos.authz.v1beta1.Authorization\212\347\260*\'cosmos-sdk/GenericExchangeAuthorization'
  _globals['_CREATESPOTLIMITORDERAUTHZ']._serialized_start=171
  _globals['_CREATESPOTLIMITORDERAUTHZ']._serialized_end=324
  _globals['_CREATESPOTMARKETORDERAUTHZ']._serialized_start=327
  _globals['_CREATESPOTMARKETORDERAUTHZ']._serialized_end=482
  _globals['_BATCHCREATESPOTLIMITORDERSAUTHZ']._serialized_start=485
  _globals['_BATCHCREATESPOTLIMITORDERSAUTHZ']._serialized_end=650
  _globals['_CANCELSPOTORDERAUTHZ']._serialized_start=653
  _globals['_CANCELSPOTORDERAUTHZ']._serialized_end=796
  _globals['_BATCHCANCELSPOTORDERSAUTHZ']._serialized_start=799
  _globals['_BATCHCANCELSPOTORDERSAUTHZ']._serialized_end=954
  _globals['_CREATEDERIVATIVELIMITORDERAUTHZ']._serialized_start=957
  _globals['_CREATEDERIVATIVELIMITORDERAUTHZ']._serialized_end=1122
  _globals['_CREATEDERIVATIVEMARKETORDERAUTHZ']._serialized_start=1125
  _globals['_CREATEDERIVATIVEMARKETORDERAUTHZ']._serialized_end=1292
  _globals['_BATCHCREATEDERIVATIVELIMITORDERSAUTHZ']._serialized_start=1295
  _globals['_BATCHCREATEDERIVATIVELIMITORDERSAUTHZ']._serialized_end=1472
  _globals['_CANCELDERIVATIVEORDERAUTHZ']._serialized_start=1475
  _globals['_CANCELDERIVATIVEORDERAUTHZ']._serialized_end=1630
  _globals['_BATCHCANCELDERIVATIVEORDERSAUTHZ']._serialized_start=1633
  _globals['_BATCHCANCELDERIVATIVEORDERSAUTHZ']._serialized_end=1800
  _globals['_BATCHUPDATEORDERSAUTHZ']._serialized_start=1803
  _globals['_BATCHUPDATEORDERSAUTHZ']._serialized_end=2001
  _globals['_GENERICEXCHANGEAUTHORIZATION']._serialized_start=2004
  _globals['_GENERICEXCHANGEAUTHORIZATION']._serialized_end=2269
# @@protoc_insertion_point(module_scope)
