# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cometbft/abci/v1/service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.cometbft.abci.v1 import types_pb2 as cometbft_dot_abci_dot_v1_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x63ometbft/abci/v1/service.proto\x12\x10\x63ometbft.abci.v1\x1a\x1c\x63ometbft/abci/v1/types.proto2\xc4\x0b\n\x0b\x41\x42\x43IService\x12\x45\n\x04\x45\x63ho\x12\x1d.cometbft.abci.v1.EchoRequest\x1a\x1e.cometbft.abci.v1.EchoResponse\x12H\n\x05\x46lush\x12\x1e.cometbft.abci.v1.FlushRequest\x1a\x1f.cometbft.abci.v1.FlushResponse\x12\x45\n\x04Info\x12\x1d.cometbft.abci.v1.InfoRequest\x1a\x1e.cometbft.abci.v1.InfoResponse\x12N\n\x07\x43heckTx\x12 .cometbft.abci.v1.CheckTxRequest\x1a!.cometbft.abci.v1.CheckTxResponse\x12H\n\x05Query\x12\x1e.cometbft.abci.v1.QueryRequest\x1a\x1f.cometbft.abci.v1.QueryResponse\x12K\n\x06\x43ommit\x12\x1f.cometbft.abci.v1.CommitRequest\x1a .cometbft.abci.v1.CommitResponse\x12T\n\tInitChain\x12\".cometbft.abci.v1.InitChainRequest\x1a#.cometbft.abci.v1.InitChainResponse\x12`\n\rListSnapshots\x12&.cometbft.abci.v1.ListSnapshotsRequest\x1a\'.cometbft.abci.v1.ListSnapshotsResponse\x12`\n\rOfferSnapshot\x12&.cometbft.abci.v1.OfferSnapshotRequest\x1a\'.cometbft.abci.v1.OfferSnapshotResponse\x12l\n\x11LoadSnapshotChunk\x12*.cometbft.abci.v1.LoadSnapshotChunkRequest\x1a+.cometbft.abci.v1.LoadSnapshotChunkResponse\x12o\n\x12\x41pplySnapshotChunk\x12+.cometbft.abci.v1.ApplySnapshotChunkRequest\x1a,.cometbft.abci.v1.ApplySnapshotChunkResponse\x12\x66\n\x0fPrepareProposal\x12(.cometbft.abci.v1.PrepareProposalRequest\x1a).cometbft.abci.v1.PrepareProposalResponse\x12\x66\n\x0fProcessProposal\x12(.cometbft.abci.v1.ProcessProposalRequest\x1a).cometbft.abci.v1.ProcessProposalResponse\x12W\n\nExtendVote\x12#.cometbft.abci.v1.ExtendVoteRequest\x1a$.cometbft.abci.v1.ExtendVoteResponse\x12r\n\x13VerifyVoteExtension\x12,.cometbft.abci.v1.VerifyVoteExtensionRequest\x1a-.cometbft.abci.v1.VerifyVoteExtensionResponse\x12`\n\rFinalizeBlock\x12&.cometbft.abci.v1.FinalizeBlockRequest\x1a\'.cometbft.abci.v1.FinalizeBlockResponseB\xb9\x01\n\x14\x63om.cometbft.abci.v1B\x0cServiceProtoP\x01Z1github.com/cometbft/cometbft/api/cometbft/abci/v1\xa2\x02\x03\x43\x41X\xaa\x02\x10\x43ometbft.Abci.V1\xca\x02\x10\x43ometbft\\Abci\\V1\xe2\x02\x1c\x43ometbft\\Abci\\V1\\GPBMetadata\xea\x02\x12\x43ometbft::Abci::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cometbft.abci.v1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.cometbft.abci.v1B\014ServiceProtoP\001Z1github.com/cometbft/cometbft/api/cometbft/abci/v1\242\002\003CAX\252\002\020Cometbft.Abci.V1\312\002\020Cometbft\\Abci\\V1\342\002\034Cometbft\\Abci\\V1\\GPBMetadata\352\002\022Cometbft::Abci::V1'
  _globals['_ABCISERVICE']._serialized_start=83
  _globals['_ABCISERVICE']._serialized_end=1559
# @@protoc_insertion_point(module_scope)
