# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: google/longrunning/operations.proto
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
    'google/longrunning/operations.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from pyinjective.proto.google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/longrunning/operations.proto\x12\x12google.longrunning\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x17google/rpc/status.proto\x1a google/protobuf/descriptor.proto\"\xcf\x01\n\tOperation\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x30\n\x08metadata\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyR\x08metadata\x12\x12\n\x04\x64one\x18\x03 \x01(\x08R\x04\x64one\x12*\n\x05\x65rror\x18\x04 \x01(\x0b\x32\x12.google.rpc.StatusH\x00R\x05\x65rror\x12\x32\n\x08response\x18\x05 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00R\x08responseB\x08\n\x06result\")\n\x13GetOperationRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\"\x7f\n\x15ListOperationsRequest\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name\x12\x16\n\x06\x66ilter\x18\x01 \x01(\tR\x06\x66ilter\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\"\x7f\n\x16ListOperationsResponse\x12=\n\noperations\x18\x01 \x03(\x0b\x32\x1d.google.longrunning.OperationR\noperations\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\",\n\x16\x43\x61ncelOperationRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\",\n\x16\x44\x65leteOperationRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\"_\n\x14WaitOperationRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x33\n\x07timeout\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x07timeout\"Y\n\rOperationInfo\x12#\n\rresponse_type\x18\x01 \x01(\tR\x0cresponseType\x12#\n\rmetadata_type\x18\x02 \x01(\tR\x0cmetadataType2\xaa\x05\n\nOperations\x12\x94\x01\n\x0eListOperations\x12).google.longrunning.ListOperationsRequest\x1a*.google.longrunning.ListOperationsResponse\"+\xda\x41\x0bname,filter\x82\xd3\xe4\x93\x02\x17\x12\x15/v1/{name=operations}\x12\x7f\n\x0cGetOperation\x12\'.google.longrunning.GetOperationRequest\x1a\x1d.google.longrunning.Operation\"\'\xda\x41\x04name\x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/{name=operations/**}\x12~\n\x0f\x44\x65leteOperation\x12*.google.longrunning.DeleteOperationRequest\x1a\x16.google.protobuf.Empty\"\'\xda\x41\x04name\x82\xd3\xe4\x93\x02\x1a*\x18/v1/{name=operations/**}\x12\x88\x01\n\x0f\x43\x61ncelOperation\x12*.google.longrunning.CancelOperationRequest\x1a\x16.google.protobuf.Empty\"1\xda\x41\x04name\x82\xd3\xe4\x93\x02$\"\x1f/v1/{name=operations/**}:cancel:\x01*\x12Z\n\rWaitOperation\x12(.google.longrunning.WaitOperationRequest\x1a\x1d.google.longrunning.Operation\"\x00\x1a\x1d\xca\x41\x1alongrunning.googleapis.com:i\n\x0eoperation_info\x12\x1e.google.protobuf.MethodOptions\x18\x99\x08 \x01(\x0b\x32!.google.longrunning.OperationInfoR\roperationInfoB\xda\x01\n\x16\x63om.google.longrunningB\x0fOperationsProtoP\x01ZCcloud.google.com/go/longrunning/autogen/longrunningpb;longrunningpb\xf8\x01\x01\xa2\x02\x03GLX\xaa\x02\x12Google.Longrunning\xca\x02\x12Google\\Longrunning\xe2\x02\x1eGoogle\\Longrunning\\GPBMetadata\xea\x02\x13Google::Longrunningb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.longrunning.operations_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.google.longrunningB\017OperationsProtoP\001ZCcloud.google.com/go/longrunning/autogen/longrunningpb;longrunningpb\370\001\001\242\002\003GLX\252\002\022Google.Longrunning\312\002\022Google\\Longrunning\342\002\036Google\\Longrunning\\GPBMetadata\352\002\023Google::Longrunning'
  _globals['_OPERATIONS']._loaded_options = None
  _globals['_OPERATIONS']._serialized_options = b'\312A\032longrunning.googleapis.com'
  _globals['_OPERATIONS'].methods_by_name['ListOperations']._loaded_options = None
  _globals['_OPERATIONS'].methods_by_name['ListOperations']._serialized_options = b'\332A\013name,filter\202\323\344\223\002\027\022\025/v1/{name=operations}'
  _globals['_OPERATIONS'].methods_by_name['GetOperation']._loaded_options = None
  _globals['_OPERATIONS'].methods_by_name['GetOperation']._serialized_options = b'\332A\004name\202\323\344\223\002\032\022\030/v1/{name=operations/**}'
  _globals['_OPERATIONS'].methods_by_name['DeleteOperation']._loaded_options = None
  _globals['_OPERATIONS'].methods_by_name['DeleteOperation']._serialized_options = b'\332A\004name\202\323\344\223\002\032*\030/v1/{name=operations/**}'
  _globals['_OPERATIONS'].methods_by_name['CancelOperation']._loaded_options = None
  _globals['_OPERATIONS'].methods_by_name['CancelOperation']._serialized_options = b'\332A\004name\202\323\344\223\002$\"\037/v1/{name=operations/**}:cancel:\001*'
  _globals['_OPERATION']._serialized_start=262
  _globals['_OPERATION']._serialized_end=469
  _globals['_GETOPERATIONREQUEST']._serialized_start=471
  _globals['_GETOPERATIONREQUEST']._serialized_end=512
  _globals['_LISTOPERATIONSREQUEST']._serialized_start=514
  _globals['_LISTOPERATIONSREQUEST']._serialized_end=641
  _globals['_LISTOPERATIONSRESPONSE']._serialized_start=643
  _globals['_LISTOPERATIONSRESPONSE']._serialized_end=770
  _globals['_CANCELOPERATIONREQUEST']._serialized_start=772
  _globals['_CANCELOPERATIONREQUEST']._serialized_end=816
  _globals['_DELETEOPERATIONREQUEST']._serialized_start=818
  _globals['_DELETEOPERATIONREQUEST']._serialized_end=862
  _globals['_WAITOPERATIONREQUEST']._serialized_start=864
  _globals['_WAITOPERATIONREQUEST']._serialized_end=959
  _globals['_OPERATIONINFO']._serialized_start=961
  _globals['_OPERATIONINFO']._serialized_end=1050
  _globals['_OPERATIONS']._serialized_start=1053
  _globals['_OPERATIONS']._serialized_end=1735
# @@protoc_insertion_point(module_scope)
