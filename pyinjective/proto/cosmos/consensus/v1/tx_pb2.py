# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/consensus/v1/tx.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2
from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from pyinjective.proto.cometbft.types.v1 import params_pb2 as cometbft_dot_types_dot_v1_dot_params__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x63osmos/consensus/v1/tx.proto\x12\x13\x63osmos.consensus.v1\x1a\x11\x61mino/amino.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x1e\x63ometbft/types/v1/params.proto\"\xec\x03\n\x0fMsgUpdateParams\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12\x34\n\x05\x62lock\x18\x02 \x01(\x0b\x32\x1e.cometbft.types.v1.BlockParamsR\x05\x62lock\x12=\n\x08\x65vidence\x18\x03 \x01(\x0b\x32!.cometbft.types.v1.EvidenceParamsR\x08\x65vidence\x12@\n\tvalidator\x18\x04 \x01(\x0b\x32\".cometbft.types.v1.ValidatorParamsR\tvalidator\x12\x31\n\x04\x61\x62\x63i\x18\x05 \x01(\x0b\x32\x1d.cometbft.types.v1.ABCIParamsR\x04\x61\x62\x63i\x12@\n\tsynchrony\x18\x06 \x01(\x0b\x32\".cometbft.types.v1.SynchronyParamsR\tsynchrony\x12:\n\x07\x66\x65\x61ture\x18\x07 \x01(\x0b\x32 .cometbft.types.v1.FeatureParamsR\x07\x66\x65\x61ture:9\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*&cosmos-sdk/x/consensus/MsgUpdateParams\"\x19\n\x17MsgUpdateParamsResponse2p\n\x03Msg\x12\x62\n\x0cUpdateParams\x12$.cosmos.consensus.v1.MsgUpdateParams\x1a,.cosmos.consensus.v1.MsgUpdateParamsResponse\x1a\x05\x80\xe7\xb0*\x01\x42\xc0\x01\n\x17\x63om.cosmos.consensus.v1B\x07TxProtoP\x01Z.github.com/cosmos/cosmos-sdk/x/consensus/types\xa2\x02\x03\x43\x43X\xaa\x02\x13\x43osmos.Consensus.V1\xca\x02\x13\x43osmos\\Consensus\\V1\xe2\x02\x1f\x43osmos\\Consensus\\V1\\GPBMetadata\xea\x02\x15\x43osmos::Consensus::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.consensus.v1.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027com.cosmos.consensus.v1B\007TxProtoP\001Z.github.com/cosmos/cosmos-sdk/x/consensus/types\242\002\003CCX\252\002\023Cosmos.Consensus.V1\312\002\023Cosmos\\Consensus\\V1\342\002\037Cosmos\\Consensus\\V1\\GPBMetadata\352\002\025Cosmos::Consensus::V1'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATEPARAMS']._loaded_options = None
  _globals['_MSGUPDATEPARAMS']._serialized_options = b'\202\347\260*\tauthority\212\347\260*&cosmos-sdk/x/consensus/MsgUpdateParams'
  _globals['_MSG']._loaded_options = None
  _globals['_MSG']._serialized_options = b'\200\347\260*\001'
  _globals['_MSGUPDATEPARAMS']._serialized_start=157
  _globals['_MSGUPDATEPARAMS']._serialized_end=649
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start=651
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end=676
  _globals['_MSG']._serialized_start=678
  _globals['_MSG']._serialized_end=790
# @@protoc_insertion_point(module_scope)
