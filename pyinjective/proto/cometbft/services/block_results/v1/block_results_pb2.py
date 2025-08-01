# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cometbft/services/block_results/v1/block_results.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.cometbft.abci.v1 import types_pb2 as cometbft_dot_abci_dot_v1_dot_types__pb2
from pyinjective.proto.cometbft.types.v1 import params_pb2 as cometbft_dot_types_dot_v1_dot_params__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6cometbft/services/block_results/v1/block_results.proto\x12\"cometbft.services.block_results.v1\x1a\x1c\x63ometbft/abci/v1/types.proto\x1a\x1e\x63ometbft/types/v1/params.proto\"0\n\x16GetBlockResultsRequest\x12\x16\n\x06height\x18\x01 \x01(\x03R\x06height\"\x84\x03\n\x17GetBlockResultsResponse\x12\x16\n\x06height\x18\x01 \x01(\x03R\x06height\x12=\n\ntx_results\x18\x02 \x03(\x0b\x32\x1e.cometbft.abci.v1.ExecTxResultR\ttxResults\x12K\n\x15\x66inalize_block_events\x18\x03 \x03(\x0b\x32\x17.cometbft.abci.v1.EventR\x13\x66inalizeBlockEvents\x12N\n\x11validator_updates\x18\x04 \x03(\x0b\x32!.cometbft.abci.v1.ValidatorUpdateR\x10validatorUpdates\x12Z\n\x17\x63onsensus_param_updates\x18\x05 \x01(\x0b\x32\".cometbft.types.v1.ConsensusParamsR\x15\x63onsensusParamUpdates\x12\x19\n\x08\x61pp_hash\x18\x06 \x01(\x0cR\x07\x61ppHashB\xa7\x02\n&com.cometbft.services.block_results.v1B\x11\x42lockResultsProtoP\x01ZCgithub.com/cometbft/cometbft/api/cometbft/services/block_results/v1\xa2\x02\x03\x43SB\xaa\x02!Cometbft.Services.BlockResults.V1\xca\x02!Cometbft\\Services\\BlockResults\\V1\xe2\x02-Cometbft\\Services\\BlockResults\\V1\\GPBMetadata\xea\x02$Cometbft::Services::BlockResults::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cometbft.services.block_results.v1.block_results_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.cometbft.services.block_results.v1B\021BlockResultsProtoP\001ZCgithub.com/cometbft/cometbft/api/cometbft/services/block_results/v1\242\002\003CSB\252\002!Cometbft.Services.BlockResults.V1\312\002!Cometbft\\Services\\BlockResults\\V1\342\002-Cometbft\\Services\\BlockResults\\V1\\GPBMetadata\352\002$Cometbft::Services::BlockResults::V1'
  _globals['_GETBLOCKRESULTSREQUEST']._serialized_start=156
  _globals['_GETBLOCKRESULTSREQUEST']._serialized_end=204
  _globals['_GETBLOCKRESULTSRESPONSE']._serialized_start=207
  _globals['_GETBLOCKRESULTSRESPONSE']._serialized_end=595
# @@protoc_insertion_point(module_scope)
