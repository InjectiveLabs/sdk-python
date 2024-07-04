# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/ocr/v1beta1/query.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from pyinjective.proto.injective.ocr.v1beta1 import ocr_pb2 as injective_dot_ocr_dot_v1beta1_dot_ocr__pb2
from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from pyinjective.proto.injective.ocr.v1beta1 import genesis_pb2 as injective_dot_ocr_dot_v1beta1_dot_genesis__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!injective/ocr/v1beta1/query.proto\x12\x15injective.ocr.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x1finjective/ocr/v1beta1/ocr.proto\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a#injective/ocr/v1beta1/genesis.proto\"\x14\n\x12QueryParamsRequest\"R\n\x13QueryParamsResponse\x12;\n\x06params\x18\x01 \x01(\x0b\x32\x1d.injective.ocr.v1beta1.ParamsB\x04\xc8\xde\x1f\x00R\x06params\"1\n\x16QueryFeedConfigRequest\x12\x17\n\x07\x66\x65\x65\x64_id\x18\x01 \x01(\tR\x06\x66\x65\x65\x64Id\"\xae\x01\n\x17QueryFeedConfigResponse\x12O\n\x10\x66\x65\x65\x64_config_info\x18\x01 \x01(\x0b\x32%.injective.ocr.v1beta1.FeedConfigInfoR\x0e\x66\x65\x65\x64\x43onfigInfo\x12\x42\n\x0b\x66\x65\x65\x64_config\x18\x02 \x01(\x0b\x32!.injective.ocr.v1beta1.FeedConfigR\nfeedConfig\"5\n\x1aQueryFeedConfigInfoRequest\x12\x17\n\x07\x66\x65\x65\x64_id\x18\x01 \x01(\tR\x06\x66\x65\x65\x64Id\"\xbc\x01\n\x1bQueryFeedConfigInfoResponse\x12O\n\x10\x66\x65\x65\x64_config_info\x18\x01 \x01(\x0b\x32%.injective.ocr.v1beta1.FeedConfigInfoR\x0e\x66\x65\x65\x64\x43onfigInfo\x12L\n\x0f\x65poch_and_round\x18\x02 \x01(\x0b\x32$.injective.ocr.v1beta1.EpochAndRoundR\repochAndRound\"2\n\x17QueryLatestRoundRequest\x12\x17\n\x07\x66\x65\x65\x64_id\x18\x01 \x01(\tR\x06\x66\x65\x65\x64Id\"{\n\x18QueryLatestRoundResponse\x12&\n\x0flatest_round_id\x18\x01 \x01(\x04R\rlatestRoundId\x12\x37\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32#.injective.ocr.v1beta1.TransmissionR\x04\x64\x61ta\"@\n%QueryLatestTransmissionDetailsRequest\x12\x17\n\x07\x66\x65\x65\x64_id\x18\x01 \x01(\tR\x06\x66\x65\x65\x64Id\"\xd4\x01\n&QueryLatestTransmissionDetailsResponse\x12#\n\rconfig_digest\x18\x01 \x01(\x0cR\x0c\x63onfigDigest\x12L\n\x0f\x65poch_and_round\x18\x02 \x01(\x0b\x32$.injective.ocr.v1beta1.EpochAndRoundR\repochAndRound\x12\x37\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32#.injective.ocr.v1beta1.TransmissionR\x04\x64\x61ta\":\n\x16QueryOwedAmountRequest\x12 \n\x0btransmitter\x18\x01 \x01(\tR\x0btransmitter\"R\n\x17QueryOwedAmountResponse\x12\x37\n\x06\x61mount\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00R\x06\x61mount\"\x19\n\x17QueryModuleStateRequest\"U\n\x18QueryModuleStateResponse\x12\x39\n\x05state\x18\x01 \x01(\x0b\x32#.injective.ocr.v1beta1.GenesisStateR\x05state2\xbb\t\n\x05Query\x12\x86\x01\n\x06Params\x12).injective.ocr.v1beta1.QueryParamsRequest\x1a*.injective.ocr.v1beta1.QueryParamsResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/chainlink/ocr/v1beta1/params\x12\xa1\x01\n\nFeedConfig\x12-.injective.ocr.v1beta1.QueryFeedConfigRequest\x1a..injective.ocr.v1beta1.QueryFeedConfigResponse\"4\x82\xd3\xe4\x93\x02.\x12,/chainlink/ocr/v1beta1/feed_config/{feed_id}\x12\xb2\x01\n\x0e\x46\x65\x65\x64\x43onfigInfo\x12\x31.injective.ocr.v1beta1.QueryFeedConfigInfoRequest\x1a\x32.injective.ocr.v1beta1.QueryFeedConfigInfoResponse\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/chainlink/ocr/v1beta1/feed_config_info/{feed_id}\x12\xa5\x01\n\x0bLatestRound\x12..injective.ocr.v1beta1.QueryLatestRoundRequest\x1a/.injective.ocr.v1beta1.QueryLatestRoundResponse\"5\x82\xd3\xe4\x93\x02/\x12-/chainlink/ocr/v1beta1/latest_round/{feed_id}\x12\xde\x01\n\x19LatestTransmissionDetails\x12<.injective.ocr.v1beta1.QueryLatestTransmissionDetailsRequest\x1a=.injective.ocr.v1beta1.QueryLatestTransmissionDetailsResponse\"D\x82\xd3\xe4\x93\x02>\x12</chainlink/ocr/v1beta1/latest_transmission_details/{feed_id}\x12\xa5\x01\n\nOwedAmount\x12-.injective.ocr.v1beta1.QueryOwedAmountRequest\x1a..injective.ocr.v1beta1.QueryOwedAmountResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/chainlink/ocr/v1beta1/owed_amount/{transmitter}\x12\x9e\x01\n\x0eOcrModuleState\x12..injective.ocr.v1beta1.QueryModuleStateRequest\x1a/.injective.ocr.v1beta1.QueryModuleStateResponse\"+\x82\xd3\xe4\x93\x02%\x12#/chainlink/ocr/v1beta1/module_stateB\xe8\x01\n\x19\x63om.injective.ocr.v1beta1B\nQueryProtoP\x01ZIgithub.com/InjectiveLabs/injective-core/injective-chain/modules/ocr/types\xa2\x02\x03IOX\xaa\x02\x15Injective.Ocr.V1beta1\xca\x02\x15Injective\\Ocr\\V1beta1\xe2\x02!Injective\\Ocr\\V1beta1\\GPBMetadata\xea\x02\x17Injective::Ocr::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.ocr.v1beta1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.injective.ocr.v1beta1B\nQueryProtoP\001ZIgithub.com/InjectiveLabs/injective-core/injective-chain/modules/ocr/types\242\002\003IOX\252\002\025Injective.Ocr.V1beta1\312\002\025Injective\\Ocr\\V1beta1\342\002!Injective\\Ocr\\V1beta1\\GPBMetadata\352\002\027Injective::Ocr::V1beta1'
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._options = None
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYOWEDAMOUNTRESPONSE'].fields_by_name['amount']._options = None
  _globals['_QUERYOWEDAMOUNTRESPONSE'].fields_by_name['amount']._serialized_options = b'\310\336\037\000'
  _globals['_QUERY'].methods_by_name['Params']._options = None
  _globals['_QUERY'].methods_by_name['Params']._serialized_options = b'\202\323\344\223\002\037\022\035/chainlink/ocr/v1beta1/params'
  _globals['_QUERY'].methods_by_name['FeedConfig']._options = None
  _globals['_QUERY'].methods_by_name['FeedConfig']._serialized_options = b'\202\323\344\223\002.\022,/chainlink/ocr/v1beta1/feed_config/{feed_id}'
  _globals['_QUERY'].methods_by_name['FeedConfigInfo']._options = None
  _globals['_QUERY'].methods_by_name['FeedConfigInfo']._serialized_options = b'\202\323\344\223\0023\0221/chainlink/ocr/v1beta1/feed_config_info/{feed_id}'
  _globals['_QUERY'].methods_by_name['LatestRound']._options = None
  _globals['_QUERY'].methods_by_name['LatestRound']._serialized_options = b'\202\323\344\223\002/\022-/chainlink/ocr/v1beta1/latest_round/{feed_id}'
  _globals['_QUERY'].methods_by_name['LatestTransmissionDetails']._options = None
  _globals['_QUERY'].methods_by_name['LatestTransmissionDetails']._serialized_options = b'\202\323\344\223\002>\022</chainlink/ocr/v1beta1/latest_transmission_details/{feed_id}'
  _globals['_QUERY'].methods_by_name['OwedAmount']._options = None
  _globals['_QUERY'].methods_by_name['OwedAmount']._serialized_options = b'\202\323\344\223\0022\0220/chainlink/ocr/v1beta1/owed_amount/{transmitter}'
  _globals['_QUERY'].methods_by_name['OcrModuleState']._options = None
  _globals['_QUERY'].methods_by_name['OcrModuleState']._serialized_options = b'\202\323\344\223\002%\022#/chainlink/ocr/v1beta1/module_state'
  _globals['_QUERYPARAMSREQUEST']._serialized_start=214
  _globals['_QUERYPARAMSREQUEST']._serialized_end=234
  _globals['_QUERYPARAMSRESPONSE']._serialized_start=236
  _globals['_QUERYPARAMSRESPONSE']._serialized_end=318
  _globals['_QUERYFEEDCONFIGREQUEST']._serialized_start=320
  _globals['_QUERYFEEDCONFIGREQUEST']._serialized_end=369
  _globals['_QUERYFEEDCONFIGRESPONSE']._serialized_start=372
  _globals['_QUERYFEEDCONFIGRESPONSE']._serialized_end=546
  _globals['_QUERYFEEDCONFIGINFOREQUEST']._serialized_start=548
  _globals['_QUERYFEEDCONFIGINFOREQUEST']._serialized_end=601
  _globals['_QUERYFEEDCONFIGINFORESPONSE']._serialized_start=604
  _globals['_QUERYFEEDCONFIGINFORESPONSE']._serialized_end=792
  _globals['_QUERYLATESTROUNDREQUEST']._serialized_start=794
  _globals['_QUERYLATESTROUNDREQUEST']._serialized_end=844
  _globals['_QUERYLATESTROUNDRESPONSE']._serialized_start=846
  _globals['_QUERYLATESTROUNDRESPONSE']._serialized_end=969
  _globals['_QUERYLATESTTRANSMISSIONDETAILSREQUEST']._serialized_start=971
  _globals['_QUERYLATESTTRANSMISSIONDETAILSREQUEST']._serialized_end=1035
  _globals['_QUERYLATESTTRANSMISSIONDETAILSRESPONSE']._serialized_start=1038
  _globals['_QUERYLATESTTRANSMISSIONDETAILSRESPONSE']._serialized_end=1250
  _globals['_QUERYOWEDAMOUNTREQUEST']._serialized_start=1252
  _globals['_QUERYOWEDAMOUNTREQUEST']._serialized_end=1310
  _globals['_QUERYOWEDAMOUNTRESPONSE']._serialized_start=1312
  _globals['_QUERYOWEDAMOUNTRESPONSE']._serialized_end=1394
  _globals['_QUERYMODULESTATEREQUEST']._serialized_start=1396
  _globals['_QUERYMODULESTATEREQUEST']._serialized_end=1421
  _globals['_QUERYMODULESTATERESPONSE']._serialized_start=1423
  _globals['_QUERYMODULESTATERESPONSE']._serialized_end=1508
  _globals['_QUERY']._serialized_start=1511
  _globals['_QUERY']._serialized_end=2722
# @@protoc_insertion_point(module_scope)
