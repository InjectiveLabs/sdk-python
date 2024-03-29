# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: testpb/test_schema_query.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from testpb import test_schema_pb2 as testpb_dot_test__schema__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1etestpb/test_schema_query.proto\x12\x06testpb\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x18testpb/test_schema.proto\"?\n\x16GetExampleTableRequest\x12\x0b\n\x03u32\x18\x01 \x01(\r\x12\x0b\n\x03i64\x18\x02 \x01(\x03\x12\x0b\n\x03str\x18\x03 \x01(\t\">\n\x17GetExampleTableResponse\x12#\n\x05value\x18\x01 \x01(\x0b\x32\x14.testpb.ExampleTable\":\n\x1eGetExampleTableByU64StrRequest\x12\x0b\n\x03u64\x18\x01 \x01(\x04\x12\x0b\n\x03str\x18\x02 \x01(\t\"F\n\x1fGetExampleTableByU64StrResponse\x12#\n\x05value\x18\x01 \x01(\x0b\x32\x14.testpb.ExampleTable\"\x9e\x07\n\x17ListExampleTableRequest\x12@\n\x0cprefix_query\x18\x01 \x01(\x0b\x32(.testpb.ListExampleTableRequest.IndexKeyH\x00\x12\x41\n\x0brange_query\x18\x02 \x01(\x0b\x32*.testpb.ListExampleTableRequest.RangeQueryH\x00\x12:\n\npagination\x18\x03 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\x1a\xbc\x04\n\x08IndexKey\x12K\n\ru_32_i_64_str\x18\x01 \x01(\x0b\x32\x32.testpb.ListExampleTableRequest.IndexKey.U32I64StrH\x00\x12\x43\n\x08u_64_str\x18\x02 \x01(\x0b\x32/.testpb.ListExampleTableRequest.IndexKey.U64StrH\x00\x12\x43\n\x08str_u_32\x18\x03 \x01(\x0b\x32/.testpb.ListExampleTableRequest.IndexKey.StrU32H\x00\x12@\n\x06\x62z_str\x18\x04 \x01(\x0b\x32..testpb.ListExampleTableRequest.IndexKey.BzStrH\x00\x1aY\n\tU32I64Str\x12\x10\n\x03u32\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x10\n\x03i64\x18\x02 \x01(\x03H\x01\x88\x01\x01\x12\x10\n\x03str\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\x06\n\x04_u32B\x06\n\x04_i64B\x06\n\x04_str\x1a<\n\x06U64Str\x12\x10\n\x03u64\x18\x01 \x01(\x04H\x00\x88\x01\x01\x12\x10\n\x03str\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x06\n\x04_u64B\x06\n\x04_str\x1a<\n\x06StrU32\x12\x10\n\x03str\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x03u32\x18\x02 \x01(\rH\x01\x88\x01\x01\x42\x06\n\x04_strB\x06\n\x04_u32\x1a\x39\n\x05\x42zStr\x12\x0f\n\x02\x62z\x18\x01 \x01(\x0cH\x00\x88\x01\x01\x12\x10\n\x03str\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x05\n\x03_bzB\x06\n\x04_strB\x05\n\x03key\x1az\n\nRangeQuery\x12\x36\n\x04\x66rom\x18\x01 \x01(\x0b\x32(.testpb.ListExampleTableRequest.IndexKey\x12\x34\n\x02to\x18\x02 \x01(\x0b\x32(.testpb.ListExampleTableRequest.IndexKeyB\x07\n\x05query\"}\n\x18ListExampleTableResponse\x12$\n\x06values\x18\x01 \x03(\x0b\x32\x14.testpb.ExampleTable\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"1\n#GetExampleAutoIncrementTableRequest\x12\n\n\x02id\x18\x01 \x01(\x04\"X\n$GetExampleAutoIncrementTableResponse\x12\x30\n\x05value\x18\x01 \x01(\x0b\x32!.testpb.ExampleAutoIncrementTable\"3\n&GetExampleAutoIncrementTableByXRequest\x12\t\n\x01x\x18\x01 \x01(\t\"[\n\'GetExampleAutoIncrementTableByXResponse\x12\x30\n\x05value\x18\x01 \x01(\x0b\x32!.testpb.ExampleAutoIncrementTable\"\xfc\x04\n$ListExampleAutoIncrementTableRequest\x12M\n\x0cprefix_query\x18\x01 \x01(\x0b\x32\x35.testpb.ListExampleAutoIncrementTableRequest.IndexKeyH\x00\x12N\n\x0brange_query\x18\x02 \x01(\x0b\x32\x37.testpb.ListExampleAutoIncrementTableRequest.RangeQueryH\x00\x12:\n\npagination\x18\x03 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\x1a\xd8\x01\n\x08IndexKey\x12\x46\n\x02id\x18\x01 \x01(\x0b\x32\x38.testpb.ListExampleAutoIncrementTableRequest.IndexKey.IdH\x00\x12\x44\n\x01x\x18\x02 \x01(\x0b\x32\x37.testpb.ListExampleAutoIncrementTableRequest.IndexKey.XH\x00\x1a\x1c\n\x02Id\x12\x0f\n\x02id\x18\x01 \x01(\x04H\x00\x88\x01\x01\x42\x05\n\x03_id\x1a\x19\n\x01X\x12\x0e\n\x01x\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x04\n\x02_xB\x05\n\x03key\x1a\x94\x01\n\nRangeQuery\x12\x43\n\x04\x66rom\x18\x01 \x01(\x0b\x32\x35.testpb.ListExampleAutoIncrementTableRequest.IndexKey\x12\x41\n\x02to\x18\x02 \x01(\x0b\x32\x35.testpb.ListExampleAutoIncrementTableRequest.IndexKeyB\x07\n\x05query\"\x97\x01\n%ListExampleAutoIncrementTableResponse\x12\x31\n\x06values\x18\x01 \x03(\x0b\x32!.testpb.ExampleAutoIncrementTable\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x1c\n\x1aGetExampleSingletonRequest\"F\n\x1bGetExampleSingletonResponse\x12\'\n\x05value\x18\x01 \x01(\x0b\x32\x18.testpb.ExampleSingleton\"(\n\x1aGetExampleTimestampRequest\x12\n\n\x02id\x18\x01 \x01(\x04\"F\n\x1bGetExampleTimestampResponse\x12\'\n\x05value\x18\x01 \x01(\x0b\x32\x18.testpb.ExampleTimestamp\"\xde\x04\n\x1bListExampleTimestampRequest\x12\x44\n\x0cprefix_query\x18\x01 \x01(\x0b\x32,.testpb.ListExampleTimestampRequest.IndexKeyH\x00\x12\x45\n\x0brange_query\x18\x02 \x01(\x0b\x32..testpb.ListExampleTimestampRequest.RangeQueryH\x00\x12:\n\npagination\x18\x03 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\x1a\xe7\x01\n\x08IndexKey\x12=\n\x02id\x18\x01 \x01(\x0b\x32/.testpb.ListExampleTimestampRequest.IndexKey.IdH\x00\x12=\n\x02ts\x18\x02 \x01(\x0b\x32/.testpb.ListExampleTimestampRequest.IndexKey.TsH\x00\x1a\x1c\n\x02Id\x12\x0f\n\x02id\x18\x01 \x01(\x04H\x00\x88\x01\x01\x42\x05\n\x03_id\x1a\x38\n\x02Ts\x12+\n\x02ts\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x88\x01\x01\x42\x05\n\x03_tsB\x05\n\x03key\x1a\x82\x01\n\nRangeQuery\x12:\n\x04\x66rom\x18\x01 \x01(\x0b\x32,.testpb.ListExampleTimestampRequest.IndexKey\x12\x38\n\x02to\x18\x02 \x01(\x0b\x32,.testpb.ListExampleTimestampRequest.IndexKeyB\x07\n\x05query\"\x85\x01\n\x1cListExampleTimestampResponse\x12(\n\x06values\x18\x01 \x03(\x0b\x32\x18.testpb.ExampleTimestamp\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\'\n\x17GetSimpleExampleRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"@\n\x18GetSimpleExampleResponse\x12$\n\x05value\x18\x01 \x01(\x0b\x32\x15.testpb.SimpleExample\"1\n\x1fGetSimpleExampleByUniqueRequest\x12\x0e\n\x06unique\x18\x01 \x01(\t\"H\n GetSimpleExampleByUniqueResponse\x12$\n\x05value\x18\x01 \x01(\x0b\x32\x15.testpb.SimpleExample\"\xca\x04\n\x18ListSimpleExampleRequest\x12\x41\n\x0cprefix_query\x18\x01 \x01(\x0b\x32).testpb.ListSimpleExampleRequest.IndexKeyH\x00\x12\x42\n\x0brange_query\x18\x02 \x01(\x0b\x32+.testpb.ListSimpleExampleRequest.RangeQueryH\x00\x12:\n\npagination\x18\x03 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\x1a\xe3\x01\n\x08IndexKey\x12>\n\x04name\x18\x01 \x01(\x0b\x32..testpb.ListSimpleExampleRequest.IndexKey.NameH\x00\x12\x42\n\x06unique\x18\x02 \x01(\x0b\x32\x30.testpb.ListSimpleExampleRequest.IndexKey.UniqueH\x00\x1a\"\n\x04Name\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_name\x1a(\n\x06Unique\x12\x13\n\x06unique\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_uniqueB\x05\n\x03key\x1a|\n\nRangeQuery\x12\x37\n\x04\x66rom\x18\x01 \x01(\x0b\x32).testpb.ListSimpleExampleRequest.IndexKey\x12\x35\n\x02to\x18\x02 \x01(\x0b\x32).testpb.ListSimpleExampleRequest.IndexKeyB\x07\n\x05query\"\x7f\n\x19ListSimpleExampleResponse\x12%\n\x06values\x18\x01 \x03(\x0b\x32\x15.testpb.SimpleExample\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"0\n!GetExampleAutoIncFieldNameRequest\x12\x0b\n\x03\x66oo\x18\x01 \x01(\x04\"T\n\"GetExampleAutoIncFieldNameResponse\x12.\n\x05value\x18\x01 \x01(\x0b\x32\x1f.testpb.ExampleAutoIncFieldName\"\x93\x04\n\"ListExampleAutoIncFieldNameRequest\x12K\n\x0cprefix_query\x18\x01 \x01(\x0b\x32\x33.testpb.ListExampleAutoIncFieldNameRequest.IndexKeyH\x00\x12L\n\x0brange_query\x18\x02 \x01(\x0b\x32\x35.testpb.ListExampleAutoIncFieldNameRequest.RangeQueryH\x00\x12:\n\npagination\x18\x03 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\x1az\n\x08IndexKey\x12\x46\n\x03\x66oo\x18\x01 \x01(\x0b\x32\x37.testpb.ListExampleAutoIncFieldNameRequest.IndexKey.FooH\x00\x1a\x1f\n\x03\x46oo\x12\x10\n\x03\x66oo\x18\x01 \x01(\x04H\x00\x88\x01\x01\x42\x06\n\x04_fooB\x05\n\x03key\x1a\x90\x01\n\nRangeQuery\x12\x41\n\x04\x66rom\x18\x01 \x01(\x0b\x32\x33.testpb.ListExampleAutoIncFieldNameRequest.IndexKey\x12?\n\x02to\x18\x02 \x01(\x0b\x32\x33.testpb.ListExampleAutoIncFieldNameRequest.IndexKeyB\x07\n\x05query\"\x93\x01\n#ListExampleAutoIncFieldNameResponse\x12/\n\x06values\x18\x01 \x03(\x0b\x32\x1f.testpb.ExampleAutoIncFieldName\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse2\xf9\x0b\n\x16TestSchemaQueryService\x12T\n\x0fGetExampleTable\x12\x1e.testpb.GetExampleTableRequest\x1a\x1f.testpb.GetExampleTableResponse\"\x00\x12l\n\x17GetExampleTableByU64Str\x12&.testpb.GetExampleTableByU64StrRequest\x1a\'.testpb.GetExampleTableByU64StrResponse\"\x00\x12W\n\x10ListExampleTable\x12\x1f.testpb.ListExampleTableRequest\x1a .testpb.ListExampleTableResponse\"\x00\x12{\n\x1cGetExampleAutoIncrementTable\x12+.testpb.GetExampleAutoIncrementTableRequest\x1a,.testpb.GetExampleAutoIncrementTableResponse\"\x00\x12\x84\x01\n\x1fGetExampleAutoIncrementTableByX\x12..testpb.GetExampleAutoIncrementTableByXRequest\x1a/.testpb.GetExampleAutoIncrementTableByXResponse\"\x00\x12~\n\x1dListExampleAutoIncrementTable\x12,.testpb.ListExampleAutoIncrementTableRequest\x1a-.testpb.ListExampleAutoIncrementTableResponse\"\x00\x12`\n\x13GetExampleSingleton\x12\".testpb.GetExampleSingletonRequest\x1a#.testpb.GetExampleSingletonResponse\"\x00\x12`\n\x13GetExampleTimestamp\x12\".testpb.GetExampleTimestampRequest\x1a#.testpb.GetExampleTimestampResponse\"\x00\x12\x63\n\x14ListExampleTimestamp\x12#.testpb.ListExampleTimestampRequest\x1a$.testpb.ListExampleTimestampResponse\"\x00\x12W\n\x10GetSimpleExample\x12\x1f.testpb.GetSimpleExampleRequest\x1a .testpb.GetSimpleExampleResponse\"\x00\x12o\n\x18GetSimpleExampleByUnique\x12\'.testpb.GetSimpleExampleByUniqueRequest\x1a(.testpb.GetSimpleExampleByUniqueResponse\"\x00\x12Z\n\x11ListSimpleExample\x12 .testpb.ListSimpleExampleRequest\x1a!.testpb.ListSimpleExampleResponse\"\x00\x12u\n\x1aGetExampleAutoIncFieldName\x12).testpb.GetExampleAutoIncFieldNameRequest\x1a*.testpb.GetExampleAutoIncFieldNameResponse\"\x00\x12x\n\x1bListExampleAutoIncFieldName\x12*.testpb.ListExampleAutoIncFieldNameRequest\x1a+.testpb.ListExampleAutoIncFieldNameResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'testpb.test_schema_query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GETEXAMPLETABLEREQUEST']._serialized_start=145
  _globals['_GETEXAMPLETABLEREQUEST']._serialized_end=208
  _globals['_GETEXAMPLETABLERESPONSE']._serialized_start=210
  _globals['_GETEXAMPLETABLERESPONSE']._serialized_end=272
  _globals['_GETEXAMPLETABLEBYU64STRREQUEST']._serialized_start=274
  _globals['_GETEXAMPLETABLEBYU64STRREQUEST']._serialized_end=332
  _globals['_GETEXAMPLETABLEBYU64STRRESPONSE']._serialized_start=334
  _globals['_GETEXAMPLETABLEBYU64STRRESPONSE']._serialized_end=404
  _globals['_LISTEXAMPLETABLEREQUEST']._serialized_start=407
  _globals['_LISTEXAMPLETABLEREQUEST']._serialized_end=1333
  _globals['_LISTEXAMPLETABLEREQUEST_INDEXKEY']._serialized_start=628
  _globals['_LISTEXAMPLETABLEREQUEST_INDEXKEY']._serialized_end=1200
  _globals['_LISTEXAMPLETABLEREQUEST_INDEXKEY_U32I64STR']._serialized_start=921
  _globals['_LISTEXAMPLETABLEREQUEST_INDEXKEY_U32I64STR']._serialized_end=1010
  _globals['_LISTEXAMPLETABLEREQUEST_INDEXKEY_U64STR']._serialized_start=1012
  _globals['_LISTEXAMPLETABLEREQUEST_INDEXKEY_U64STR']._serialized_end=1072
  _globals['_LISTEXAMPLETABLEREQUEST_INDEXKEY_STRU32']._serialized_start=1074
  _globals['_LISTEXAMPLETABLEREQUEST_INDEXKEY_STRU32']._serialized_end=1134
  _globals['_LISTEXAMPLETABLEREQUEST_INDEXKEY_BZSTR']._serialized_start=1136
  _globals['_LISTEXAMPLETABLEREQUEST_INDEXKEY_BZSTR']._serialized_end=1193
  _globals['_LISTEXAMPLETABLEREQUEST_RANGEQUERY']._serialized_start=1202
  _globals['_LISTEXAMPLETABLEREQUEST_RANGEQUERY']._serialized_end=1324
  _globals['_LISTEXAMPLETABLERESPONSE']._serialized_start=1335
  _globals['_LISTEXAMPLETABLERESPONSE']._serialized_end=1460
  _globals['_GETEXAMPLEAUTOINCREMENTTABLEREQUEST']._serialized_start=1462
  _globals['_GETEXAMPLEAUTOINCREMENTTABLEREQUEST']._serialized_end=1511
  _globals['_GETEXAMPLEAUTOINCREMENTTABLERESPONSE']._serialized_start=1513
  _globals['_GETEXAMPLEAUTOINCREMENTTABLERESPONSE']._serialized_end=1601
  _globals['_GETEXAMPLEAUTOINCREMENTTABLEBYXREQUEST']._serialized_start=1603
  _globals['_GETEXAMPLEAUTOINCREMENTTABLEBYXREQUEST']._serialized_end=1654
  _globals['_GETEXAMPLEAUTOINCREMENTTABLEBYXRESPONSE']._serialized_start=1656
  _globals['_GETEXAMPLEAUTOINCREMENTTABLEBYXRESPONSE']._serialized_end=1747
  _globals['_LISTEXAMPLEAUTOINCREMENTTABLEREQUEST']._serialized_start=1750
  _globals['_LISTEXAMPLEAUTOINCREMENTTABLEREQUEST']._serialized_end=2386
  _globals['_LISTEXAMPLEAUTOINCREMENTTABLEREQUEST_INDEXKEY']._serialized_start=2010
  _globals['_LISTEXAMPLEAUTOINCREMENTTABLEREQUEST_INDEXKEY']._serialized_end=2226
  _globals['_LISTEXAMPLEAUTOINCREMENTTABLEREQUEST_INDEXKEY_ID']._serialized_start=2164
  _globals['_LISTEXAMPLEAUTOINCREMENTTABLEREQUEST_INDEXKEY_ID']._serialized_end=2192
  _globals['_LISTEXAMPLEAUTOINCREMENTTABLEREQUEST_INDEXKEY_X']._serialized_start=2194
  _globals['_LISTEXAMPLEAUTOINCREMENTTABLEREQUEST_INDEXKEY_X']._serialized_end=2219
  _globals['_LISTEXAMPLEAUTOINCREMENTTABLEREQUEST_RANGEQUERY']._serialized_start=2229
  _globals['_LISTEXAMPLEAUTOINCREMENTTABLEREQUEST_RANGEQUERY']._serialized_end=2377
  _globals['_LISTEXAMPLEAUTOINCREMENTTABLERESPONSE']._serialized_start=2389
  _globals['_LISTEXAMPLEAUTOINCREMENTTABLERESPONSE']._serialized_end=2540
  _globals['_GETEXAMPLESINGLETONREQUEST']._serialized_start=2542
  _globals['_GETEXAMPLESINGLETONREQUEST']._serialized_end=2570
  _globals['_GETEXAMPLESINGLETONRESPONSE']._serialized_start=2572
  _globals['_GETEXAMPLESINGLETONRESPONSE']._serialized_end=2642
  _globals['_GETEXAMPLETIMESTAMPREQUEST']._serialized_start=2644
  _globals['_GETEXAMPLETIMESTAMPREQUEST']._serialized_end=2684
  _globals['_GETEXAMPLETIMESTAMPRESPONSE']._serialized_start=2686
  _globals['_GETEXAMPLETIMESTAMPRESPONSE']._serialized_end=2756
  _globals['_LISTEXAMPLETIMESTAMPREQUEST']._serialized_start=2759
  _globals['_LISTEXAMPLETIMESTAMPREQUEST']._serialized_end=3365
  _globals['_LISTEXAMPLETIMESTAMPREQUEST_INDEXKEY']._serialized_start=2992
  _globals['_LISTEXAMPLETIMESTAMPREQUEST_INDEXKEY']._serialized_end=3223
  _globals['_LISTEXAMPLETIMESTAMPREQUEST_INDEXKEY_ID']._serialized_start=2164
  _globals['_LISTEXAMPLETIMESTAMPREQUEST_INDEXKEY_ID']._serialized_end=2192
  _globals['_LISTEXAMPLETIMESTAMPREQUEST_INDEXKEY_TS']._serialized_start=3160
  _globals['_LISTEXAMPLETIMESTAMPREQUEST_INDEXKEY_TS']._serialized_end=3216
  _globals['_LISTEXAMPLETIMESTAMPREQUEST_RANGEQUERY']._serialized_start=3226
  _globals['_LISTEXAMPLETIMESTAMPREQUEST_RANGEQUERY']._serialized_end=3356
  _globals['_LISTEXAMPLETIMESTAMPRESPONSE']._serialized_start=3368
  _globals['_LISTEXAMPLETIMESTAMPRESPONSE']._serialized_end=3501
  _globals['_GETSIMPLEEXAMPLEREQUEST']._serialized_start=3503
  _globals['_GETSIMPLEEXAMPLEREQUEST']._serialized_end=3542
  _globals['_GETSIMPLEEXAMPLERESPONSE']._serialized_start=3544
  _globals['_GETSIMPLEEXAMPLERESPONSE']._serialized_end=3608
  _globals['_GETSIMPLEEXAMPLEBYUNIQUEREQUEST']._serialized_start=3610
  _globals['_GETSIMPLEEXAMPLEBYUNIQUEREQUEST']._serialized_end=3659
  _globals['_GETSIMPLEEXAMPLEBYUNIQUERESPONSE']._serialized_start=3661
  _globals['_GETSIMPLEEXAMPLEBYUNIQUERESPONSE']._serialized_end=3733
  _globals['_LISTSIMPLEEXAMPLEREQUEST']._serialized_start=3736
  _globals['_LISTSIMPLEEXAMPLEREQUEST']._serialized_end=4322
  _globals['_LISTSIMPLEEXAMPLEREQUEST_INDEXKEY']._serialized_start=3960
  _globals['_LISTSIMPLEEXAMPLEREQUEST_INDEXKEY']._serialized_end=4187
  _globals['_LISTSIMPLEEXAMPLEREQUEST_INDEXKEY_NAME']._serialized_start=4104
  _globals['_LISTSIMPLEEXAMPLEREQUEST_INDEXKEY_NAME']._serialized_end=4138
  _globals['_LISTSIMPLEEXAMPLEREQUEST_INDEXKEY_UNIQUE']._serialized_start=4140
  _globals['_LISTSIMPLEEXAMPLEREQUEST_INDEXKEY_UNIQUE']._serialized_end=4180
  _globals['_LISTSIMPLEEXAMPLEREQUEST_RANGEQUERY']._serialized_start=4189
  _globals['_LISTSIMPLEEXAMPLEREQUEST_RANGEQUERY']._serialized_end=4313
  _globals['_LISTSIMPLEEXAMPLERESPONSE']._serialized_start=4324
  _globals['_LISTSIMPLEEXAMPLERESPONSE']._serialized_end=4451
  _globals['_GETEXAMPLEAUTOINCFIELDNAMEREQUEST']._serialized_start=4453
  _globals['_GETEXAMPLEAUTOINCFIELDNAMEREQUEST']._serialized_end=4501
  _globals['_GETEXAMPLEAUTOINCFIELDNAMERESPONSE']._serialized_start=4503
  _globals['_GETEXAMPLEAUTOINCFIELDNAMERESPONSE']._serialized_end=4587
  _globals['_LISTEXAMPLEAUTOINCFIELDNAMEREQUEST']._serialized_start=4590
  _globals['_LISTEXAMPLEAUTOINCFIELDNAMEREQUEST']._serialized_end=5121
  _globals['_LISTEXAMPLEAUTOINCFIELDNAMEREQUEST_INDEXKEY']._serialized_start=4843
  _globals['_LISTEXAMPLEAUTOINCFIELDNAMEREQUEST_INDEXKEY']._serialized_end=4965
  _globals['_LISTEXAMPLEAUTOINCFIELDNAMEREQUEST_INDEXKEY_FOO']._serialized_start=4927
  _globals['_LISTEXAMPLEAUTOINCFIELDNAMEREQUEST_INDEXKEY_FOO']._serialized_end=4958
  _globals['_LISTEXAMPLEAUTOINCFIELDNAMEREQUEST_RANGEQUERY']._serialized_start=4968
  _globals['_LISTEXAMPLEAUTOINCFIELDNAMEREQUEST_RANGEQUERY']._serialized_end=5112
  _globals['_LISTEXAMPLEAUTOINCFIELDNAMERESPONSE']._serialized_start=5124
  _globals['_LISTEXAMPLEAUTOINCFIELDNAMERESPONSE']._serialized_end=5271
  _globals['_TESTSCHEMAQUERYSERVICE']._serialized_start=5274
  _globals['_TESTSCHEMAQUERYSERVICE']._serialized_end=6803
# @@protoc_insertion_point(module_scope)
