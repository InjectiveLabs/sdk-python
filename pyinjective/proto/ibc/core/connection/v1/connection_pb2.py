# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/connection/v1/connection.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.ibc.core.commitment.v1 import commitment_pb2 as ibc_dot_core_dot_commitment_dot_v1_dot_commitment__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'ibc/core/connection/v1/connection.proto\x12\x16ibc.core.connection.v1\x1a\x14gogoproto/gogo.proto\x1a\'ibc/core/commitment/v1/commitment.proto\"\xc6\x02\n\rConnectionEnd\x12\x31\n\tclient_id\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:\"client_id\"R\x08\x63lientId\x12;\n\x08versions\x18\x02 \x03(\x0b\x32\x1f.ibc.core.connection.v1.VersionR\x08versions\x12\x33\n\x05state\x18\x03 \x01(\x0e\x32\x1d.ibc.core.connection.v1.StateR\x05state\x12N\n\x0c\x63ounterparty\x18\x04 \x01(\x0b\x32$.ibc.core.connection.v1.CounterpartyB\x04\xc8\xde\x1f\x00R\x0c\x63ounterparty\x12:\n\x0c\x64\x65lay_period\x18\x05 \x01(\x04\x42\x17\xf2\xde\x1f\x13yaml:\"delay_period\"R\x0b\x64\x65layPeriod:\x04\x88\xa0\x1f\x00\"\xec\x02\n\x14IdentifiedConnection\x12\x1d\n\x02id\x18\x01 \x01(\tB\r\xf2\xde\x1f\tyaml:\"id\"R\x02id\x12\x31\n\tclient_id\x18\x02 \x01(\tB\x14\xf2\xde\x1f\x10yaml:\"client_id\"R\x08\x63lientId\x12;\n\x08versions\x18\x03 \x03(\x0b\x32\x1f.ibc.core.connection.v1.VersionR\x08versions\x12\x33\n\x05state\x18\x04 \x01(\x0e\x32\x1d.ibc.core.connection.v1.StateR\x05state\x12N\n\x0c\x63ounterparty\x18\x05 \x01(\x0b\x32$.ibc.core.connection.v1.CounterpartyB\x04\xc8\xde\x1f\x00R\x0c\x63ounterparty\x12:\n\x0c\x64\x65lay_period\x18\x06 \x01(\x04\x42\x17\xf2\xde\x1f\x13yaml:\"delay_period\"R\x0b\x64\x65layPeriod:\x04\x88\xa0\x1f\x00\"\xca\x01\n\x0c\x43ounterparty\x12\x31\n\tclient_id\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:\"client_id\"R\x08\x63lientId\x12=\n\rconnection_id\x18\x02 \x01(\tB\x18\xf2\xde\x1f\x14yaml:\"connection_id\"R\x0c\x63onnectionId\x12\x42\n\x06prefix\x18\x03 \x01(\x0b\x32$.ibc.core.commitment.v1.MerklePrefixB\x04\xc8\xde\x1f\x00R\x06prefix:\x04\x88\xa0\x1f\x00\"#\n\x0b\x43lientPaths\x12\x14\n\x05paths\x18\x01 \x03(\tR\x05paths\"Z\n\x0f\x43onnectionPaths\x12\x31\n\tclient_id\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:\"client_id\"R\x08\x63lientId\x12\x14\n\x05paths\x18\x02 \x03(\tR\x05paths\"K\n\x07Version\x12\x1e\n\nidentifier\x18\x01 \x01(\tR\nidentifier\x12\x1a\n\x08\x66\x65\x61tures\x18\x02 \x03(\tR\x08\x66\x65\x61tures:\x04\x88\xa0\x1f\x00\"n\n\x06Params\x12\x64\n\x1bmax_expected_time_per_block\x18\x01 \x01(\x04\x42&\xf2\xde\x1f\"yaml:\"max_expected_time_per_block\"R\x17maxExpectedTimePerBlock*\x99\x01\n\x05State\x12\x36\n\x1fSTATE_UNINITIALIZED_UNSPECIFIED\x10\x00\x1a\x11\x8a\x9d \rUNINITIALIZED\x12\x18\n\nSTATE_INIT\x10\x01\x1a\x08\x8a\x9d \x04INIT\x12\x1e\n\rSTATE_TRYOPEN\x10\x02\x1a\x0b\x8a\x9d \x07TRYOPEN\x12\x18\n\nSTATE_OPEN\x10\x03\x1a\x08\x8a\x9d \x04OPEN\x1a\x04\x88\xa3\x1e\x00\x42\xe6\x01\n\x1a\x63om.ibc.core.connection.v1B\x0f\x43onnectionProtoP\x01Z<github.com/cosmos/ibc-go/v7/modules/core/03-connection/types\xa2\x02\x03ICC\xaa\x02\x16Ibc.Core.Connection.V1\xca\x02\x16Ibc\\Core\\Connection\\V1\xe2\x02\"Ibc\\Core\\Connection\\V1\\GPBMetadata\xea\x02\x19Ibc::Core::Connection::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.core.connection.v1.connection_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.ibc.core.connection.v1B\017ConnectionProtoP\001Z<github.com/cosmos/ibc-go/v7/modules/core/03-connection/types\242\002\003ICC\252\002\026Ibc.Core.Connection.V1\312\002\026Ibc\\Core\\Connection\\V1\342\002\"Ibc\\Core\\Connection\\V1\\GPBMetadata\352\002\031Ibc::Core::Connection::V1'
  _globals['_STATE']._options = None
  _globals['_STATE']._serialized_options = b'\210\243\036\000'
  _globals['_STATE'].values_by_name["STATE_UNINITIALIZED_UNSPECIFIED"]._options = None
  _globals['_STATE'].values_by_name["STATE_UNINITIALIZED_UNSPECIFIED"]._serialized_options = b'\212\235 \rUNINITIALIZED'
  _globals['_STATE'].values_by_name["STATE_INIT"]._options = None
  _globals['_STATE'].values_by_name["STATE_INIT"]._serialized_options = b'\212\235 \004INIT'
  _globals['_STATE'].values_by_name["STATE_TRYOPEN"]._options = None
  _globals['_STATE'].values_by_name["STATE_TRYOPEN"]._serialized_options = b'\212\235 \007TRYOPEN'
  _globals['_STATE'].values_by_name["STATE_OPEN"]._options = None
  _globals['_STATE'].values_by_name["STATE_OPEN"]._serialized_options = b'\212\235 \004OPEN'
  _globals['_CONNECTIONEND'].fields_by_name['client_id']._options = None
  _globals['_CONNECTIONEND'].fields_by_name['client_id']._serialized_options = b'\362\336\037\020yaml:\"client_id\"'
  _globals['_CONNECTIONEND'].fields_by_name['counterparty']._options = None
  _globals['_CONNECTIONEND'].fields_by_name['counterparty']._serialized_options = b'\310\336\037\000'
  _globals['_CONNECTIONEND'].fields_by_name['delay_period']._options = None
  _globals['_CONNECTIONEND'].fields_by_name['delay_period']._serialized_options = b'\362\336\037\023yaml:\"delay_period\"'
  _globals['_CONNECTIONEND']._options = None
  _globals['_CONNECTIONEND']._serialized_options = b'\210\240\037\000'
  _globals['_IDENTIFIEDCONNECTION'].fields_by_name['id']._options = None
  _globals['_IDENTIFIEDCONNECTION'].fields_by_name['id']._serialized_options = b'\362\336\037\tyaml:\"id\"'
  _globals['_IDENTIFIEDCONNECTION'].fields_by_name['client_id']._options = None
  _globals['_IDENTIFIEDCONNECTION'].fields_by_name['client_id']._serialized_options = b'\362\336\037\020yaml:\"client_id\"'
  _globals['_IDENTIFIEDCONNECTION'].fields_by_name['counterparty']._options = None
  _globals['_IDENTIFIEDCONNECTION'].fields_by_name['counterparty']._serialized_options = b'\310\336\037\000'
  _globals['_IDENTIFIEDCONNECTION'].fields_by_name['delay_period']._options = None
  _globals['_IDENTIFIEDCONNECTION'].fields_by_name['delay_period']._serialized_options = b'\362\336\037\023yaml:\"delay_period\"'
  _globals['_IDENTIFIEDCONNECTION']._options = None
  _globals['_IDENTIFIEDCONNECTION']._serialized_options = b'\210\240\037\000'
  _globals['_COUNTERPARTY'].fields_by_name['client_id']._options = None
  _globals['_COUNTERPARTY'].fields_by_name['client_id']._serialized_options = b'\362\336\037\020yaml:\"client_id\"'
  _globals['_COUNTERPARTY'].fields_by_name['connection_id']._options = None
  _globals['_COUNTERPARTY'].fields_by_name['connection_id']._serialized_options = b'\362\336\037\024yaml:\"connection_id\"'
  _globals['_COUNTERPARTY'].fields_by_name['prefix']._options = None
  _globals['_COUNTERPARTY'].fields_by_name['prefix']._serialized_options = b'\310\336\037\000'
  _globals['_COUNTERPARTY']._options = None
  _globals['_COUNTERPARTY']._serialized_options = b'\210\240\037\000'
  _globals['_CONNECTIONPATHS'].fields_by_name['client_id']._options = None
  _globals['_CONNECTIONPATHS'].fields_by_name['client_id']._serialized_options = b'\362\336\037\020yaml:\"client_id\"'
  _globals['_VERSION']._options = None
  _globals['_VERSION']._serialized_options = b'\210\240\037\000'
  _globals['_PARAMS'].fields_by_name['max_expected_time_per_block']._options = None
  _globals['_PARAMS'].fields_by_name['max_expected_time_per_block']._serialized_options = b'\362\336\037\"yaml:\"max_expected_time_per_block\"'
  _globals['_STATE']._serialized_start=1350
  _globals['_STATE']._serialized_end=1503
  _globals['_CONNECTIONEND']._serialized_start=131
  _globals['_CONNECTIONEND']._serialized_end=457
  _globals['_IDENTIFIEDCONNECTION']._serialized_start=460
  _globals['_IDENTIFIEDCONNECTION']._serialized_end=824
  _globals['_COUNTERPARTY']._serialized_start=827
  _globals['_COUNTERPARTY']._serialized_end=1029
  _globals['_CLIENTPATHS']._serialized_start=1031
  _globals['_CLIENTPATHS']._serialized_end=1066
  _globals['_CONNECTIONPATHS']._serialized_start=1068
  _globals['_CONNECTIONPATHS']._serialized_end=1158
  _globals['_VERSION']._serialized_start=1160
  _globals['_VERSION']._serialized_end=1235
  _globals['_PARAMS']._serialized_start=1237
  _globals['_PARAMS']._serialized_end=1347
# @@protoc_insertion_point(module_scope)
