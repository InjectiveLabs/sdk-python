# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/oracle/v1beta1/proposal.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.injective.oracle.v1beta1 import oracle_pb2 as injective_dot_oracle_dot_v1beta1_dot_oracle__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'injective/oracle/v1beta1/proposal.proto\x12\x18injective.oracle.v1beta1\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a%injective/oracle/v1beta1/oracle.proto\"\x9e\x01\n GrantBandOraclePrivilegeProposal\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x1a\n\x08relayers\x18\x03 \x03(\tR\x08relayers:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\x9f\x01\n!RevokeBandOraclePrivilegeProposal\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x1a\n\x08relayers\x18\x03 \x03(\tR\x08relayers:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\xc9\x01\n!GrantPriceFeederPrivilegeProposal\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x12\n\x04\x62\x61se\x18\x03 \x01(\tR\x04\x62\x61se\x12\x14\n\x05quote\x18\x04 \x01(\tR\x05quote\x12\x1a\n\x08relayers\x18\x05 \x03(\tR\x08relayers:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\xb8\x01\n\x1eGrantProviderPrivilegeProposal\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x1a\n\x08provider\x18\x03 \x01(\tR\x08provider\x12\x1a\n\x08relayers\x18\x04 \x03(\tR\x08relayers:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\xb9\x01\n\x1fRevokeProviderPrivilegeProposal\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x1a\n\x08provider\x18\x03 \x01(\tR\x08provider\x12\x1a\n\x08relayers\x18\x05 \x03(\tR\x08relayers:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\xca\x01\n\"RevokePriceFeederPrivilegeProposal\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x12\n\x04\x62\x61se\x18\x03 \x01(\tR\x04\x62\x61se\x12\x14\n\x05quote\x18\x04 \x01(\tR\x05quote\x12\x1a\n\x08relayers\x18\x05 \x03(\tR\x08relayers:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\xd1\x01\n\"AuthorizeBandOracleRequestProposal\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12K\n\x07request\x18\x03 \x01(\x0b\x32+.injective.oracle.v1beta1.BandOracleRequestB\x04\xc8\xde\x1f\x00R\x07request:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\x90\x02\n\x1fUpdateBandOracleRequestProposal\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12,\n\x12\x64\x65lete_request_ids\x18\x03 \x03(\x04R\x10\x64\x65leteRequestIds\x12_\n\x15update_oracle_request\x18\x04 \x01(\x0b\x32+.injective.oracle.v1beta1.BandOracleRequestR\x13updateOracleRequest:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\xce\x01\n\x15\x45nableBandIBCProposal\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12U\n\x0f\x62\x61nd_ibc_params\x18\x03 \x01(\x0b\x32\'.injective.oracle.v1beta1.BandIBCParamsB\x04\xc8\xde\x1f\x00R\rbandIbcParams:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.ContentB\xfd\x01\n\x1c\x63om.injective.oracle.v1beta1B\rProposalProtoP\x01ZLgithub.com/InjectiveLabs/injective-core/injective-chain/modules/oracle/types\xa2\x02\x03IOX\xaa\x02\x18Injective.Oracle.V1beta1\xca\x02\x18Injective\\Oracle\\V1beta1\xe2\x02$Injective\\Oracle\\V1beta1\\GPBMetadata\xea\x02\x1aInjective::Oracle::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.oracle.v1beta1.proposal_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.injective.oracle.v1beta1B\rProposalProtoP\001ZLgithub.com/InjectiveLabs/injective-core/injective-chain/modules/oracle/types\242\002\003IOX\252\002\030Injective.Oracle.V1beta1\312\002\030Injective\\Oracle\\V1beta1\342\002$Injective\\Oracle\\V1beta1\\GPBMetadata\352\002\032Injective::Oracle::V1beta1'
  _globals['_GRANTBANDORACLEPRIVILEGEPROPOSAL']._options = None
  _globals['_GRANTBANDORACLEPRIVILEGEPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_REVOKEBANDORACLEPRIVILEGEPROPOSAL']._options = None
  _globals['_REVOKEBANDORACLEPRIVILEGEPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_GRANTPRICEFEEDERPRIVILEGEPROPOSAL']._options = None
  _globals['_GRANTPRICEFEEDERPRIVILEGEPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_GRANTPROVIDERPRIVILEGEPROPOSAL']._options = None
  _globals['_GRANTPROVIDERPRIVILEGEPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_REVOKEPROVIDERPRIVILEGEPROPOSAL']._options = None
  _globals['_REVOKEPROVIDERPRIVILEGEPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_REVOKEPRICEFEEDERPRIVILEGEPROPOSAL']._options = None
  _globals['_REVOKEPRICEFEEDERPRIVILEGEPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_AUTHORIZEBANDORACLEREQUESTPROPOSAL'].fields_by_name['request']._options = None
  _globals['_AUTHORIZEBANDORACLEREQUESTPROPOSAL'].fields_by_name['request']._serialized_options = b'\310\336\037\000'
  _globals['_AUTHORIZEBANDORACLEREQUESTPROPOSAL']._options = None
  _globals['_AUTHORIZEBANDORACLEREQUESTPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_UPDATEBANDORACLEREQUESTPROPOSAL']._options = None
  _globals['_UPDATEBANDORACLEREQUESTPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_ENABLEBANDIBCPROPOSAL'].fields_by_name['band_ibc_params']._options = None
  _globals['_ENABLEBANDIBCPROPOSAL'].fields_by_name['band_ibc_params']._serialized_options = b'\310\336\037\000'
  _globals['_ENABLEBANDIBCPROPOSAL']._options = None
  _globals['_ENABLEBANDIBCPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_GRANTBANDORACLEPRIVILEGEPROPOSAL']._serialized_start=190
  _globals['_GRANTBANDORACLEPRIVILEGEPROPOSAL']._serialized_end=348
  _globals['_REVOKEBANDORACLEPRIVILEGEPROPOSAL']._serialized_start=351
  _globals['_REVOKEBANDORACLEPRIVILEGEPROPOSAL']._serialized_end=510
  _globals['_GRANTPRICEFEEDERPRIVILEGEPROPOSAL']._serialized_start=513
  _globals['_GRANTPRICEFEEDERPRIVILEGEPROPOSAL']._serialized_end=714
  _globals['_GRANTPROVIDERPRIVILEGEPROPOSAL']._serialized_start=717
  _globals['_GRANTPROVIDERPRIVILEGEPROPOSAL']._serialized_end=901
  _globals['_REVOKEPROVIDERPRIVILEGEPROPOSAL']._serialized_start=904
  _globals['_REVOKEPROVIDERPRIVILEGEPROPOSAL']._serialized_end=1089
  _globals['_REVOKEPRICEFEEDERPRIVILEGEPROPOSAL']._serialized_start=1092
  _globals['_REVOKEPRICEFEEDERPRIVILEGEPROPOSAL']._serialized_end=1294
  _globals['_AUTHORIZEBANDORACLEREQUESTPROPOSAL']._serialized_start=1297
  _globals['_AUTHORIZEBANDORACLEREQUESTPROPOSAL']._serialized_end=1506
  _globals['_UPDATEBANDORACLEREQUESTPROPOSAL']._serialized_start=1509
  _globals['_UPDATEBANDORACLEREQUESTPROPOSAL']._serialized_end=1781
  _globals['_ENABLEBANDIBCPROPOSAL']._serialized_start=1784
  _globals['_ENABLEBANDIBCPROPOSAL']._serialized_end=1990
# @@protoc_insertion_point(module_scope)
