# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/ocr/v1beta1/ocr.proto
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
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1finjective/ocr/v1beta1/ocr.proto\x12\x15injective.ocr.v1beta1\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x84\x01\n\x06Params\x12\x1d\n\nlink_denom\x18\x01 \x01(\tR\tlinkDenom\x12\x32\n\x15payout_block_interval\x18\x02 \x01(\x04R\x13payoutBlockInterval\x12!\n\x0cmodule_admin\x18\x03 \x01(\tR\x0bmoduleAdmin:\x04\xe8\xa0\x1f\x01\"\xaa\x02\n\nFeedConfig\x12\x18\n\x07signers\x18\x01 \x03(\tR\x07signers\x12\"\n\x0ctransmitters\x18\x02 \x03(\tR\x0ctransmitters\x12\x0c\n\x01\x66\x18\x03 \x01(\rR\x01\x66\x12%\n\x0eonchain_config\x18\x04 \x01(\x0cR\ronchainConfig\x12\x36\n\x17offchain_config_version\x18\x05 \x01(\x04R\x15offchainConfigVersion\x12\'\n\x0foffchain_config\x18\x06 \x01(\x0cR\x0eoffchainConfig\x12H\n\rmodule_params\x18\x07 \x01(\x0b\x32#.injective.ocr.v1beta1.ModuleParamsR\x0cmoduleParams\"\xbe\x01\n\x0e\x46\x65\x65\x64\x43onfigInfo\x12\x30\n\x14latest_config_digest\x18\x01 \x01(\x0cR\x12latestConfigDigest\x12\x0c\n\x01\x66\x18\x02 \x01(\rR\x01\x66\x12\x0c\n\x01n\x18\x03 \x01(\rR\x01n\x12!\n\x0c\x63onfig_count\x18\x04 \x01(\x04R\x0b\x63onfigCount\x12;\n\x1alatest_config_block_number\x18\x05 \x01(\x03R\x17latestConfigBlockNumber\"\xb7\x04\n\x0cModuleParams\x12\x17\n\x07\x66\x65\x65\x64_id\x18\x01 \x01(\tR\x06\x66\x65\x65\x64Id\x12M\n\nmin_answer\x18\x02 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\tminAnswer\x12M\n\nmax_answer\x18\x03 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\tmaxAnswer\x12`\n\x14link_per_observation\x18\x04 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.IntR\x12linkPerObservation\x12\x62\n\x15link_per_transmission\x18\x05 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.IntR\x13linkPerTransmission\x12\x1d\n\nlink_denom\x18\x06 \x01(\tR\tlinkDenom\x12%\n\x0eunique_reports\x18\x07 \x01(\x08R\runiqueReports\x12 \n\x0b\x64\x65scription\x18\x08 \x01(\tR\x0b\x64\x65scription\x12\x1d\n\nfeed_admin\x18\t \x01(\tR\tfeedAdmin\x12#\n\rbilling_admin\x18\n \x01(\tR\x0c\x62illingAdmin\"\x87\x02\n\x0e\x43ontractConfig\x12!\n\x0c\x63onfig_count\x18\x01 \x01(\x04R\x0b\x63onfigCount\x12\x18\n\x07signers\x18\x02 \x03(\tR\x07signers\x12\"\n\x0ctransmitters\x18\x03 \x03(\tR\x0ctransmitters\x12\x0c\n\x01\x66\x18\x04 \x01(\rR\x01\x66\x12%\n\x0eonchain_config\x18\x05 \x01(\x0cR\ronchainConfig\x12\x36\n\x17offchain_config_version\x18\x06 \x01(\x04R\x15offchainConfigVersion\x12\'\n\x0foffchain_config\x18\x07 \x01(\x0cR\x0eoffchainConfig\"\xae\x01\n\x11SetConfigProposal\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x39\n\x06\x63onfig\x18\x03 \x01(\x0b\x32!.injective.ocr.v1beta1.FeedConfigR\x06\x63onfig:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\xec\x04\n\x0e\x46\x65\x65\x64Properties\x12\x17\n\x07\x66\x65\x65\x64_id\x18\x01 \x01(\tR\x06\x66\x65\x65\x64Id\x12\x0c\n\x01\x66\x18\x02 \x01(\rR\x01\x66\x12%\n\x0eonchain_config\x18\x03 \x01(\x0cR\ronchainConfig\x12\x36\n\x17offchain_config_version\x18\x04 \x01(\x04R\x15offchainConfigVersion\x12\'\n\x0foffchain_config\x18\x05 \x01(\x0cR\x0eoffchainConfig\x12M\n\nmin_answer\x18\x06 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\tminAnswer\x12M\n\nmax_answer\x18\x07 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\tmaxAnswer\x12`\n\x14link_per_observation\x18\x08 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.IntR\x12linkPerObservation\x12\x62\n\x15link_per_transmission\x18\t \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.IntR\x13linkPerTransmission\x12%\n\x0eunique_reports\x18\n \x01(\x08R\runiqueReports\x12 \n\x0b\x64\x65scription\x18\x0b \x01(\tR\x0b\x64\x65scription\"\xa5\x02\n\x16SetBatchConfigProposal\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x18\n\x07signers\x18\x03 \x03(\tR\x07signers\x12\"\n\x0ctransmitters\x18\x04 \x03(\tR\x0ctransmitters\x12\x1d\n\nlink_denom\x18\x05 \x01(\tR\tlinkDenom\x12N\n\x0f\x66\x65\x65\x64_properties\x18\x06 \x03(\x0b\x32%.injective.ocr.v1beta1.FeedPropertiesR\x0e\x66\x65\x65\x64Properties:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"2\n\x18OracleObservationsCounts\x12\x16\n\x06\x63ounts\x18\x01 \x03(\rR\x06\x63ounts\"V\n\x11GasReimbursements\x12\x41\n\x0ereimbursements\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinR\x0ereimbursements\"U\n\x05Payee\x12)\n\x10transmitter_addr\x18\x01 \x01(\tR\x0ftransmitterAddr\x12!\n\x0cpayment_addr\x18\x02 \x01(\tR\x0bpaymentAddr\"\xc4\x01\n\x0cTransmission\x12\x46\n\x06\x61nswer\x18\x01 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x06\x61nswer\x12\x35\n\x16observations_timestamp\x18\x02 \x01(\x03R\x15observationsTimestamp\x12\x35\n\x16transmission_timestamp\x18\x03 \x01(\x03R\x15transmissionTimestamp\";\n\rEpochAndRound\x12\x14\n\x05\x65poch\x18\x01 \x01(\x04R\x05\x65poch\x12\x14\n\x05round\x18\x02 \x01(\x04R\x05round\"\xb1\x01\n\x06Report\x12\x35\n\x16observations_timestamp\x18\x01 \x01(\x03R\x15observationsTimestamp\x12\x1c\n\tobservers\x18\x02 \x01(\x0cR\tobservers\x12R\n\x0cobservations\x18\x03 \x03(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x0cobservations\"\x96\x01\n\x0cReportToSign\x12#\n\rconfig_digest\x18\x01 \x01(\x0cR\x0c\x63onfigDigest\x12\x14\n\x05\x65poch\x18\x02 \x01(\x04R\x05\x65poch\x12\x14\n\x05round\x18\x03 \x01(\x04R\x05round\x12\x1d\n\nextra_hash\x18\x04 \x01(\x0cR\textraHash\x12\x16\n\x06report\x18\x05 \x01(\x0cR\x06report\"\x94\x01\n\x0f\x45ventOraclePaid\x12)\n\x10transmitter_addr\x18\x01 \x01(\tR\x0ftransmitterAddr\x12\x1d\n\npayee_addr\x18\x02 \x01(\tR\tpayeeAddr\x12\x37\n\x06\x61mount\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00R\x06\x61mount\"\xee\x01\n\x12\x45ventAnswerUpdated\x12H\n\x07\x63urrent\x18\x01 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.IntR\x07\x63urrent\x12I\n\x08round_id\x18\x02 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.IntR\x07roundId\x12\x43\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01R\tupdatedAt\"\xbe\x01\n\rEventNewRound\x12I\n\x08round_id\x18\x01 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.IntR\x07roundId\x12\x1d\n\nstarted_by\x18\x02 \x01(\tR\tstartedBy\x12\x43\n\nstarted_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01R\tstartedAt\"M\n\x10\x45ventTransmitted\x12#\n\rconfig_digest\x18\x01 \x01(\x0cR\x0c\x63onfigDigest\x12\x14\n\x05\x65poch\x18\x02 \x01(\x04R\x05\x65poch\"\xe5\x03\n\x14\x45ventNewTransmission\x12\x17\n\x07\x66\x65\x65\x64_id\x18\x01 \x01(\tR\x06\x66\x65\x65\x64Id\x12.\n\x13\x61ggregator_round_id\x18\x02 \x01(\rR\x11\x61ggregatorRoundId\x12\x46\n\x06\x61nswer\x18\x03 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x06\x61nswer\x12 \n\x0btransmitter\x18\x04 \x01(\tR\x0btransmitter\x12\x35\n\x16observations_timestamp\x18\x05 \x01(\x03R\x15observationsTimestamp\x12R\n\x0cobservations\x18\x06 \x03(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecR\x0cobservations\x12\x1c\n\tobservers\x18\x07 \x01(\x0cR\tobservers\x12#\n\rconfig_digest\x18\x08 \x01(\x0cR\x0c\x63onfigDigest\x12L\n\x0f\x65poch_and_round\x18\t \x01(\x0b\x32$.injective.ocr.v1beta1.EpochAndRoundR\repochAndRound\"\xf9\x01\n\x0e\x45ventConfigSet\x12#\n\rconfig_digest\x18\x01 \x01(\x0cR\x0c\x63onfigDigest\x12?\n\x1cprevious_config_block_number\x18\x02 \x01(\x03R\x19previousConfigBlockNumber\x12\x39\n\x06\x63onfig\x18\x03 \x01(\x0b\x32!.injective.ocr.v1beta1.FeedConfigR\x06\x63onfig\x12\x46\n\x0b\x63onfig_info\x18\x04 \x01(\x0b\x32%.injective.ocr.v1beta1.FeedConfigInfoR\nconfigInfoB\xe6\x01\n\x19\x63om.injective.ocr.v1beta1B\x08OcrProtoP\x01ZIgithub.com/InjectiveLabs/injective-core/injective-chain/modules/ocr/types\xa2\x02\x03IOX\xaa\x02\x15Injective.Ocr.V1beta1\xca\x02\x15Injective\\Ocr\\V1beta1\xe2\x02!Injective\\Ocr\\V1beta1\\GPBMetadata\xea\x02\x17Injective::Ocr::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.ocr.v1beta1.ocr_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.injective.ocr.v1beta1B\010OcrProtoP\001ZIgithub.com/InjectiveLabs/injective-core/injective-chain/modules/ocr/types\242\002\003IOX\252\002\025Injective.Ocr.V1beta1\312\002\025Injective\\Ocr\\V1beta1\342\002!Injective\\Ocr\\V1beta1\\GPBMetadata\352\002\027Injective::Ocr::V1beta1'
  _globals['_PARAMS']._options = None
  _globals['_PARAMS']._serialized_options = b'\350\240\037\001'
  _globals['_MODULEPARAMS'].fields_by_name['min_answer']._options = None
  _globals['_MODULEPARAMS'].fields_by_name['min_answer']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_MODULEPARAMS'].fields_by_name['max_answer']._options = None
  _globals['_MODULEPARAMS'].fields_by_name['max_answer']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_MODULEPARAMS'].fields_by_name['link_per_observation']._options = None
  _globals['_MODULEPARAMS'].fields_by_name['link_per_observation']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int'
  _globals['_MODULEPARAMS'].fields_by_name['link_per_transmission']._options = None
  _globals['_MODULEPARAMS'].fields_by_name['link_per_transmission']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int'
  _globals['_SETCONFIGPROPOSAL']._options = None
  _globals['_SETCONFIGPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_FEEDPROPERTIES'].fields_by_name['min_answer']._options = None
  _globals['_FEEDPROPERTIES'].fields_by_name['min_answer']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_FEEDPROPERTIES'].fields_by_name['max_answer']._options = None
  _globals['_FEEDPROPERTIES'].fields_by_name['max_answer']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_FEEDPROPERTIES'].fields_by_name['link_per_observation']._options = None
  _globals['_FEEDPROPERTIES'].fields_by_name['link_per_observation']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int'
  _globals['_FEEDPROPERTIES'].fields_by_name['link_per_transmission']._options = None
  _globals['_FEEDPROPERTIES'].fields_by_name['link_per_transmission']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int'
  _globals['_SETBATCHCONFIGPROPOSAL']._options = None
  _globals['_SETBATCHCONFIGPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_TRANSMISSION'].fields_by_name['answer']._options = None
  _globals['_TRANSMISSION'].fields_by_name['answer']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_REPORT'].fields_by_name['observations']._options = None
  _globals['_REPORT'].fields_by_name['observations']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_EVENTORACLEPAID'].fields_by_name['amount']._options = None
  _globals['_EVENTORACLEPAID'].fields_by_name['amount']._serialized_options = b'\310\336\037\000'
  _globals['_EVENTANSWERUPDATED'].fields_by_name['current']._options = None
  _globals['_EVENTANSWERUPDATED'].fields_by_name['current']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int'
  _globals['_EVENTANSWERUPDATED'].fields_by_name['round_id']._options = None
  _globals['_EVENTANSWERUPDATED'].fields_by_name['round_id']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int'
  _globals['_EVENTANSWERUPDATED'].fields_by_name['updated_at']._options = None
  _globals['_EVENTANSWERUPDATED'].fields_by_name['updated_at']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_EVENTNEWROUND'].fields_by_name['round_id']._options = None
  _globals['_EVENTNEWROUND'].fields_by_name['round_id']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int'
  _globals['_EVENTNEWROUND'].fields_by_name['started_at']._options = None
  _globals['_EVENTNEWROUND'].fields_by_name['started_at']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_EVENTNEWTRANSMISSION'].fields_by_name['answer']._options = None
  _globals['_EVENTNEWTRANSMISSION'].fields_by_name['answer']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_EVENTNEWTRANSMISSION'].fields_by_name['observations']._options = None
  _globals['_EVENTNEWTRANSMISSION'].fields_by_name['observations']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_PARAMS']._serialized_start=173
  _globals['_PARAMS']._serialized_end=305
  _globals['_FEEDCONFIG']._serialized_start=308
  _globals['_FEEDCONFIG']._serialized_end=606
  _globals['_FEEDCONFIGINFO']._serialized_start=609
  _globals['_FEEDCONFIGINFO']._serialized_end=799
  _globals['_MODULEPARAMS']._serialized_start=802
  _globals['_MODULEPARAMS']._serialized_end=1369
  _globals['_CONTRACTCONFIG']._serialized_start=1372
  _globals['_CONTRACTCONFIG']._serialized_end=1635
  _globals['_SETCONFIGPROPOSAL']._serialized_start=1638
  _globals['_SETCONFIGPROPOSAL']._serialized_end=1812
  _globals['_FEEDPROPERTIES']._serialized_start=1815
  _globals['_FEEDPROPERTIES']._serialized_end=2435
  _globals['_SETBATCHCONFIGPROPOSAL']._serialized_start=2438
  _globals['_SETBATCHCONFIGPROPOSAL']._serialized_end=2731
  _globals['_ORACLEOBSERVATIONSCOUNTS']._serialized_start=2733
  _globals['_ORACLEOBSERVATIONSCOUNTS']._serialized_end=2783
  _globals['_GASREIMBURSEMENTS']._serialized_start=2785
  _globals['_GASREIMBURSEMENTS']._serialized_end=2871
  _globals['_PAYEE']._serialized_start=2873
  _globals['_PAYEE']._serialized_end=2958
  _globals['_TRANSMISSION']._serialized_start=2961
  _globals['_TRANSMISSION']._serialized_end=3157
  _globals['_EPOCHANDROUND']._serialized_start=3159
  _globals['_EPOCHANDROUND']._serialized_end=3218
  _globals['_REPORT']._serialized_start=3221
  _globals['_REPORT']._serialized_end=3398
  _globals['_REPORTTOSIGN']._serialized_start=3401
  _globals['_REPORTTOSIGN']._serialized_end=3551
  _globals['_EVENTORACLEPAID']._serialized_start=3554
  _globals['_EVENTORACLEPAID']._serialized_end=3702
  _globals['_EVENTANSWERUPDATED']._serialized_start=3705
  _globals['_EVENTANSWERUPDATED']._serialized_end=3943
  _globals['_EVENTNEWROUND']._serialized_start=3946
  _globals['_EVENTNEWROUND']._serialized_end=4136
  _globals['_EVENTTRANSMITTED']._serialized_start=4138
  _globals['_EVENTTRANSMITTED']._serialized_end=4215
  _globals['_EVENTNEWTRANSMISSION']._serialized_start=4218
  _globals['_EVENTNEWTRANSMISSION']._serialized_end=4703
  _globals['_EVENTCONFIGSET']._serialized_start=4706
  _globals['_EVENTCONFIGSET']._serialized_end=4955
# @@protoc_insertion_point(module_scope)
