# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/txfees/v1beta1/query.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from pyinjective.proto.injective.txfees.v1beta1 import txfees_pb2 as injective_dot_txfees_dot_v1beta1_dot_txfees__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$injective/txfees/v1beta1/query.proto\x12\x18injective.txfees.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a%injective/txfees/v1beta1/txfees.proto\"_\n\nEipBaseFee\x12Q\n\x08\x62\x61se_fee\x18\x01 \x01(\tB6\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xf2\xde\x1f\x0fyaml:\"base_fee\"R\x07\x62\x61seFee\"\x14\n\x12QueryParamsRequest\"U\n\x13QueryParamsResponse\x12>\n\x06params\x18\x01 \x01(\x0b\x32 .injective.txfees.v1beta1.ParamsB\x04\xc8\xde\x1f\x00R\x06params\"\x18\n\x16QueryEipBaseFeeRequest\"Z\n\x17QueryEipBaseFeeResponse\x12?\n\x08\x62\x61se_fee\x18\x01 \x01(\x0b\x32$.injective.txfees.v1beta1.EipBaseFeeR\x07\x62\x61seFee2\xc4\x02\n\x05Query\x12\x8f\x01\n\x06Params\x12,.injective.txfees.v1beta1.QueryParamsRequest\x1a-.injective.txfees.v1beta1.QueryParamsResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /injective/txfees/v1beta1/params\x12\xa8\x01\n\rGetEipBaseFee\x12\x30.injective.txfees.v1beta1.QueryEipBaseFeeRequest\x1a\x31.injective.txfees.v1beta1.QueryEipBaseFeeResponse\"2\x82\xd3\xe4\x93\x02,\x12*/injective/txfees/v1beta1/cur_eip_base_feeB\xfa\x01\n\x1c\x63om.injective.txfees.v1beta1B\nQueryProtoP\x01ZLgithub.com/InjectiveLabs/injective-core/injective-chain/modules/txfees/types\xa2\x02\x03ITX\xaa\x02\x18Injective.Txfees.V1beta1\xca\x02\x18Injective\\Txfees\\V1beta1\xe2\x02$Injective\\Txfees\\V1beta1\\GPBMetadata\xea\x02\x1aInjective::Txfees::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.txfees.v1beta1.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.injective.txfees.v1beta1B\nQueryProtoP\001ZLgithub.com/InjectiveLabs/injective-core/injective-chain/modules/txfees/types\242\002\003ITX\252\002\030Injective.Txfees.V1beta1\312\002\030Injective\\Txfees\\V1beta1\342\002$Injective\\Txfees\\V1beta1\\GPBMetadata\352\002\032Injective::Txfees::V1beta1'
  _globals['_EIPBASEFEE'].fields_by_name['base_fee']._loaded_options = None
  _globals['_EIPBASEFEE'].fields_by_name['base_fee']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\362\336\037\017yaml:\"base_fee\"'
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._loaded_options = None
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_QUERY'].methods_by_name['Params']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Params']._serialized_options = b'\202\323\344\223\002\"\022 /injective/txfees/v1beta1/params'
  _globals['_QUERY'].methods_by_name['GetEipBaseFee']._loaded_options = None
  _globals['_QUERY'].methods_by_name['GetEipBaseFee']._serialized_options = b'\202\323\344\223\002,\022*/injective/txfees/v1beta1/cur_eip_base_fee'
  _globals['_EIPBASEFEE']._serialized_start=157
  _globals['_EIPBASEFEE']._serialized_end=252
  _globals['_QUERYPARAMSREQUEST']._serialized_start=254
  _globals['_QUERYPARAMSREQUEST']._serialized_end=274
  _globals['_QUERYPARAMSRESPONSE']._serialized_start=276
  _globals['_QUERYPARAMSRESPONSE']._serialized_end=361
  _globals['_QUERYEIPBASEFEEREQUEST']._serialized_start=363
  _globals['_QUERYEIPBASEFEEREQUEST']._serialized_end=387
  _globals['_QUERYEIPBASEFEERESPONSE']._serialized_start=389
  _globals['_QUERYEIPBASEFEERESPONSE']._serialized_end=479
  _globals['_QUERY']._serialized_start=482
  _globals['_QUERY']._serialized_end=806
# @@protoc_insertion_point(module_scope)
