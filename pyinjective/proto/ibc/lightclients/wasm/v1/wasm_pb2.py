# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: ibc/lightclients/wasm/v1/wasm.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'ibc/lightclients/wasm/v1/wasm.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#ibc/lightclients/wasm/v1/wasm.proto\x12\x18ibc.lightclients.wasm.v1\x1a\x14gogoproto/gogo.proto\x1a\x1fibc/core/client/v1/client.proto\"\x8a\x01\n\x0b\x43lientState\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x0cR\x04\x64\x61ta\x12\x1a\n\x08\x63hecksum\x18\x02 \x01(\x0cR\x08\x63hecksum\x12\x45\n\rlatest_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00R\x0clatestHeight:\x04\x88\xa0\x1f\x00\"*\n\x0e\x43onsensusState\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x0cR\x04\x64\x61ta:\x04\x88\xa0\x1f\x00\")\n\rClientMessage\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x0cR\x04\x64\x61ta:\x04\x88\xa0\x1f\x00\"-\n\tChecksums\x12\x1c\n\tchecksums\x18\x01 \x03(\x0cR\tchecksums:\x02\x18\x01\x42\xea\x01\n\x1c\x63om.ibc.lightclients.wasm.v1B\tWasmProtoP\x01Z<github.com/cosmos/ibc-go/modules/light-clients/08-wasm/types\xa2\x02\x03ILW\xaa\x02\x18Ibc.Lightclients.Wasm.V1\xca\x02\x18Ibc\\Lightclients\\Wasm\\V1\xe2\x02$Ibc\\Lightclients\\Wasm\\V1\\GPBMetadata\xea\x02\x1bIbc::Lightclients::Wasm::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.lightclients.wasm.v1.wasm_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.ibc.lightclients.wasm.v1B\tWasmProtoP\001Z<github.com/cosmos/ibc-go/modules/light-clients/08-wasm/types\242\002\003ILW\252\002\030Ibc.Lightclients.Wasm.V1\312\002\030Ibc\\Lightclients\\Wasm\\V1\342\002$Ibc\\Lightclients\\Wasm\\V1\\GPBMetadata\352\002\033Ibc::Lightclients::Wasm::V1'
  _globals['_CLIENTSTATE'].fields_by_name['latest_height']._loaded_options = None
  _globals['_CLIENTSTATE'].fields_by_name['latest_height']._serialized_options = b'\310\336\037\000'
  _globals['_CLIENTSTATE']._loaded_options = None
  _globals['_CLIENTSTATE']._serialized_options = b'\210\240\037\000'
  _globals['_CONSENSUSSTATE']._loaded_options = None
  _globals['_CONSENSUSSTATE']._serialized_options = b'\210\240\037\000'
  _globals['_CLIENTMESSAGE']._loaded_options = None
  _globals['_CLIENTMESSAGE']._serialized_options = b'\210\240\037\000'
  _globals['_CHECKSUMS']._loaded_options = None
  _globals['_CHECKSUMS']._serialized_options = b'\030\001'
  _globals['_CLIENTSTATE']._serialized_start=121
  _globals['_CLIENTSTATE']._serialized_end=259
  _globals['_CONSENSUSSTATE']._serialized_start=261
  _globals['_CONSENSUSSTATE']._serialized_end=303
  _globals['_CLIENTMESSAGE']._serialized_start=305
  _globals['_CLIENTMESSAGE']._serialized_end=346
  _globals['_CHECKSUMS']._serialized_start=348
  _globals['_CHECKSUMS']._serialized_end=393
# @@protoc_insertion_point(module_scope)