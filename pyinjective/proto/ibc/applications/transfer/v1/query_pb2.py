# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/transfer/v1/query.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from pyinjective.proto.cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from pyinjective.proto.ibc.applications.transfer.v1 import transfer_pb2 as ibc_dot_applications_dot_transfer_dot_v1_dot_transfer__pb2
from pyinjective.proto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(ibc/applications/transfer/v1/query.proto\x12\x1cibc.applications.transfer.v1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a+ibc/applications/transfer/v1/transfer.proto\x1a\x1cgoogle/api/annotations.proto\"&\n\x16QueryDenomTraceRequest\x12\x0c\n\x04hash\x18\x01 \x01(\t\"X\n\x17QueryDenomTraceResponse\x12=\n\x0b\x64\x65nom_trace\x18\x01 \x01(\x0b\x32(.ibc.applications.transfer.v1.DenomTrace\"U\n\x17QueryDenomTracesRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\xa7\x01\n\x18QueryDenomTracesResponse\x12N\n\x0c\x64\x65nom_traces\x18\x01 \x03(\x0b\x32(.ibc.applications.transfer.v1.DenomTraceB\x0e\xc8\xde\x1f\x00\xaa\xdf\x1f\x06Traces\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x14\n\x12QueryParamsRequest\"K\n\x13QueryParamsResponse\x12\x34\n\x06params\x18\x01 \x01(\x0b\x32$.ibc.applications.transfer.v1.Params\"&\n\x15QueryDenomHashRequest\x12\r\n\x05trace\x18\x01 \x01(\t\"&\n\x16QueryDenomHashResponse\x12\x0c\n\x04hash\x18\x01 \x01(\t\"@\n\x19QueryEscrowAddressRequest\x12\x0f\n\x07port_id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t\"4\n\x1aQueryEscrowAddressResponse\x12\x16\n\x0e\x65scrow_address\x18\x01 \x01(\t\"0\n\x1fQueryTotalEscrowForDenomRequest\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\"S\n QueryTotalEscrowForDenomResponse\x12/\n\x06\x61mount\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x32\xd8\x08\n\x05Query\x12\xaf\x01\n\nDenomTrace\x12\x34.ibc.applications.transfer.v1.QueryDenomTraceRequest\x1a\x35.ibc.applications.transfer.v1.QueryDenomTraceResponse\"4\x82\xd3\xe4\x93\x02.\x12,/ibc/apps/transfer/v1/denom_traces/{hash=**}\x12\xa8\x01\n\x0b\x44\x65nomTraces\x12\x35.ibc.applications.transfer.v1.QueryDenomTracesRequest\x1a\x36.ibc.applications.transfer.v1.QueryDenomTracesResponse\"*\x82\xd3\xe4\x93\x02$\x12\"/ibc/apps/transfer/v1/denom_traces\x12\x93\x01\n\x06Params\x12\x30.ibc.applications.transfer.v1.QueryParamsRequest\x1a\x31.ibc.applications.transfer.v1.QueryParamsResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/ibc/apps/transfer/v1/params\x12\xad\x01\n\tDenomHash\x12\x33.ibc.applications.transfer.v1.QueryDenomHashRequest\x1a\x34.ibc.applications.transfer.v1.QueryDenomHashResponse\"5\x82\xd3\xe4\x93\x02/\x12-/ibc/apps/transfer/v1/denom_hashes/{trace=**}\x12\xd6\x01\n\rEscrowAddress\x12\x37.ibc.applications.transfer.v1.QueryEscrowAddressRequest\x1a\x38.ibc.applications.transfer.v1.QueryEscrowAddressResponse\"R\x82\xd3\xe4\x93\x02L\x12J/ibc/apps/transfer/v1/channels/{channel_id}/ports/{port_id}/escrow_address\x12\xd2\x01\n\x13TotalEscrowForDenom\x12=.ibc.applications.transfer.v1.QueryTotalEscrowForDenomRequest\x1a>.ibc.applications.transfer.v1.QueryTotalEscrowForDenomResponse\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/ibc/apps/transfer/v1/denoms/{denom=**}/total_escrowB9Z7github.com/cosmos/ibc-go/v7/modules/apps/transfer/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.transfer.v1.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/cosmos/ibc-go/v7/modules/apps/transfer/types'
  _globals['_QUERYDENOMTRACESRESPONSE'].fields_by_name['denom_traces']._loaded_options = None
  _globals['_QUERYDENOMTRACESRESPONSE'].fields_by_name['denom_traces']._serialized_options = b'\310\336\037\000\252\337\037\006Traces'
  _globals['_QUERYTOTALESCROWFORDENOMRESPONSE'].fields_by_name['amount']._loaded_options = None
  _globals['_QUERYTOTALESCROWFORDENOMRESPONSE'].fields_by_name['amount']._serialized_options = b'\310\336\037\000'
  _globals['_QUERY'].methods_by_name['DenomTrace']._loaded_options = None
  _globals['_QUERY'].methods_by_name['DenomTrace']._serialized_options = b'\202\323\344\223\002.\022,/ibc/apps/transfer/v1/denom_traces/{hash=**}'
  _globals['_QUERY'].methods_by_name['DenomTraces']._loaded_options = None
  _globals['_QUERY'].methods_by_name['DenomTraces']._serialized_options = b'\202\323\344\223\002$\022\"/ibc/apps/transfer/v1/denom_traces'
  _globals['_QUERY'].methods_by_name['Params']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Params']._serialized_options = b'\202\323\344\223\002\036\022\034/ibc/apps/transfer/v1/params'
  _globals['_QUERY'].methods_by_name['DenomHash']._loaded_options = None
  _globals['_QUERY'].methods_by_name['DenomHash']._serialized_options = b'\202\323\344\223\002/\022-/ibc/apps/transfer/v1/denom_hashes/{trace=**}'
  _globals['_QUERY'].methods_by_name['EscrowAddress']._loaded_options = None
  _globals['_QUERY'].methods_by_name['EscrowAddress']._serialized_options = b'\202\323\344\223\002L\022J/ibc/apps/transfer/v1/channels/{channel_id}/ports/{port_id}/escrow_address'
  _globals['_QUERY'].methods_by_name['TotalEscrowForDenom']._loaded_options = None
  _globals['_QUERY'].methods_by_name['TotalEscrowForDenom']._serialized_options = b'\202\323\344\223\0026\0224/ibc/apps/transfer/v1/denoms/{denom=**}/total_escrow'
  _globals['_QUERYDENOMTRACEREQUEST']._serialized_start=247
  _globals['_QUERYDENOMTRACEREQUEST']._serialized_end=285
  _globals['_QUERYDENOMTRACERESPONSE']._serialized_start=287
  _globals['_QUERYDENOMTRACERESPONSE']._serialized_end=375
  _globals['_QUERYDENOMTRACESREQUEST']._serialized_start=377
  _globals['_QUERYDENOMTRACESREQUEST']._serialized_end=462
  _globals['_QUERYDENOMTRACESRESPONSE']._serialized_start=465
  _globals['_QUERYDENOMTRACESRESPONSE']._serialized_end=632
  _globals['_QUERYPARAMSREQUEST']._serialized_start=634
  _globals['_QUERYPARAMSREQUEST']._serialized_end=654
  _globals['_QUERYPARAMSRESPONSE']._serialized_start=656
  _globals['_QUERYPARAMSRESPONSE']._serialized_end=731
  _globals['_QUERYDENOMHASHREQUEST']._serialized_start=733
  _globals['_QUERYDENOMHASHREQUEST']._serialized_end=771
  _globals['_QUERYDENOMHASHRESPONSE']._serialized_start=773
  _globals['_QUERYDENOMHASHRESPONSE']._serialized_end=811
  _globals['_QUERYESCROWADDRESSREQUEST']._serialized_start=813
  _globals['_QUERYESCROWADDRESSREQUEST']._serialized_end=877
  _globals['_QUERYESCROWADDRESSRESPONSE']._serialized_start=879
  _globals['_QUERYESCROWADDRESSRESPONSE']._serialized_end=931
  _globals['_QUERYTOTALESCROWFORDENOMREQUEST']._serialized_start=933
  _globals['_QUERYTOTALESCROWFORDENOMREQUEST']._serialized_end=981
  _globals['_QUERYTOTALESCROWFORDENOMRESPONSE']._serialized_start=983
  _globals['_QUERYTOTALESCROWFORDENOMRESPONSE']._serialized_end=1066
  _globals['_QUERY']._serialized_start=1069
  _globals['_QUERY']._serialized_end=2181
# @@protoc_insertion_point(module_scope)
