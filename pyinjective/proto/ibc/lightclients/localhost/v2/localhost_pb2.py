# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/lightclients/localhost/v2/localhost.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2
from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-ibc/lightclients/localhost/v2/localhost.proto\x12\x1dibc.lightclients.localhost.v2\x1a\x1fibc/core/client/v1/client.proto\x1a\x14gogoproto/gogo.proto\"Z\n\x0b\x43lientState\x12\x45\n\rlatest_height\x18\x01 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00R\x0clatestHeight:\x04\x88\xa0\x1f\x00\x42\x94\x02\n!com.ibc.lightclients.localhost.v2B\x0eLocalhostProtoP\x01ZHgithub.com/cosmos/ibc-go/v7/modules/light-clients/09-localhost;localhost\xa2\x02\x03ILL\xaa\x02\x1dIbc.Lightclients.Localhost.V2\xca\x02\x1dIbc\\Lightclients\\Localhost\\V2\xe2\x02)Ibc\\Lightclients\\Localhost\\V2\\GPBMetadata\xea\x02 Ibc::Lightclients::Localhost::V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.lightclients.localhost.v2.localhost_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!com.ibc.lightclients.localhost.v2B\016LocalhostProtoP\001ZHgithub.com/cosmos/ibc-go/v7/modules/light-clients/09-localhost;localhost\242\002\003ILL\252\002\035Ibc.Lightclients.Localhost.V2\312\002\035Ibc\\Lightclients\\Localhost\\V2\342\002)Ibc\\Lightclients\\Localhost\\V2\\GPBMetadata\352\002 Ibc::Lightclients::Localhost::V2'
  _globals['_CLIENTSTATE'].fields_by_name['latest_height']._options = None
  _globals['_CLIENTSTATE'].fields_by_name['latest_height']._serialized_options = b'\310\336\037\000'
  _globals['_CLIENTSTATE']._options = None
  _globals['_CLIENTSTATE']._serialized_options = b'\210\240\037\000'
  _globals['_CLIENTSTATE']._serialized_start=135
  _globals['_CLIENTSTATE']._serialized_end=225
# @@protoc_insertion_point(module_scope)
