# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cometbft/consensus/v1/types.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cometbft.libs.bits.v1 import types_pb2 as cometbft_dot_libs_dot_bits_dot_v1_dot_types__pb2
from pyinjective.proto.cometbft.types.v1 import types_pb2 as cometbft_dot_types_dot_v1_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!cometbft/consensus/v1/types.proto\x12\x15\x63ometbft.consensus.v1\x1a\x14gogoproto/gogo.proto\x1a!cometbft/libs/bits/v1/types.proto\x1a\x1d\x63ometbft/types/v1/types.proto\"\xb5\x01\n\x0cNewRoundStep\x12\x16\n\x06height\x18\x01 \x01(\x03R\x06height\x12\x14\n\x05round\x18\x02 \x01(\x05R\x05round\x12\x12\n\x04step\x18\x03 \x01(\rR\x04step\x12\x37\n\x18seconds_since_start_time\x18\x04 \x01(\x03R\x15secondsSinceStartTime\x12*\n\x11last_commit_round\x18\x05 \x01(\x05R\x0flastCommitRound\"\xf7\x01\n\rNewValidBlock\x12\x16\n\x06height\x18\x01 \x01(\x03R\x06height\x12\x14\n\x05round\x18\x02 \x01(\x05R\x05round\x12Y\n\x15\x62lock_part_set_header\x18\x03 \x01(\x0b\x32 .cometbft.types.v1.PartSetHeaderB\x04\xc8\xde\x1f\x00R\x12\x62lockPartSetHeader\x12@\n\x0b\x62lock_parts\x18\x04 \x01(\x0b\x32\x1f.cometbft.libs.bits.v1.BitArrayR\nblockParts\x12\x1b\n\tis_commit\x18\x05 \x01(\x08R\x08isCommit\"I\n\x08Proposal\x12=\n\x08proposal\x18\x01 \x01(\x0b\x32\x1b.cometbft.types.v1.ProposalB\x04\xc8\xde\x1f\x00R\x08proposal\"\x9d\x01\n\x0bProposalPOL\x12\x16\n\x06height\x18\x01 \x01(\x03R\x06height\x12,\n\x12proposal_pol_round\x18\x02 \x01(\x05R\x10proposalPolRound\x12H\n\x0cproposal_pol\x18\x03 \x01(\x0b\x32\x1f.cometbft.libs.bits.v1.BitArrayB\x04\xc8\xde\x1f\x00R\x0bproposalPol\"l\n\tBlockPart\x12\x16\n\x06height\x18\x01 \x01(\x03R\x06height\x12\x14\n\x05round\x18\x02 \x01(\x05R\x05round\x12\x31\n\x04part\x18\x03 \x01(\x0b\x32\x17.cometbft.types.v1.PartB\x04\xc8\xde\x1f\x00R\x04part\"3\n\x04Vote\x12+\n\x04vote\x18\x01 \x01(\x0b\x32\x17.cometbft.types.v1.VoteR\x04vote\"\x83\x01\n\x07HasVote\x12\x16\n\x06height\x18\x01 \x01(\x03R\x06height\x12\x14\n\x05round\x18\x02 \x01(\x05R\x05round\x12\x34\n\x04type\x18\x03 \x01(\x0e\x32 .cometbft.types.v1.SignedMsgTypeR\x04type\x12\x14\n\x05index\x18\x04 \x01(\x05R\x05index\"\xba\x01\n\x0cVoteSetMaj23\x12\x16\n\x06height\x18\x01 \x01(\x03R\x06height\x12\x14\n\x05round\x18\x02 \x01(\x05R\x05round\x12\x34\n\x04type\x18\x03 \x01(\x0e\x32 .cometbft.types.v1.SignedMsgTypeR\x04type\x12\x46\n\x08\x62lock_id\x18\x04 \x01(\x0b\x32\x1a.cometbft.types.v1.BlockIDB\x0f\xc8\xde\x1f\x00\xe2\xde\x1f\x07\x42lockIDR\x07\x62lockId\"\xf6\x01\n\x0bVoteSetBits\x12\x16\n\x06height\x18\x01 \x01(\x03R\x06height\x12\x14\n\x05round\x18\x02 \x01(\x05R\x05round\x12\x34\n\x04type\x18\x03 \x01(\x0e\x32 .cometbft.types.v1.SignedMsgTypeR\x04type\x12\x46\n\x08\x62lock_id\x18\x04 \x01(\x0b\x32\x1a.cometbft.types.v1.BlockIDB\x0f\xc8\xde\x1f\x00\xe2\xde\x1f\x07\x42lockIDR\x07\x62lockId\x12;\n\x05votes\x18\x05 \x01(\x0b\x32\x1f.cometbft.libs.bits.v1.BitArrayB\x04\xc8\xde\x1f\x00R\x05votes\"Z\n\x14HasProposalBlockPart\x12\x16\n\x06height\x18\x01 \x01(\x03R\x06height\x12\x14\n\x05round\x18\x02 \x01(\x05R\x05round\x12\x14\n\x05index\x18\x03 \x01(\x05R\x05index\"\xe5\x05\n\x07Message\x12K\n\x0enew_round_step\x18\x01 \x01(\x0b\x32#.cometbft.consensus.v1.NewRoundStepH\x00R\x0cnewRoundStep\x12N\n\x0fnew_valid_block\x18\x02 \x01(\x0b\x32$.cometbft.consensus.v1.NewValidBlockH\x00R\rnewValidBlock\x12=\n\x08proposal\x18\x03 \x01(\x0b\x32\x1f.cometbft.consensus.v1.ProposalH\x00R\x08proposal\x12G\n\x0cproposal_pol\x18\x04 \x01(\x0b\x32\".cometbft.consensus.v1.ProposalPOLH\x00R\x0bproposalPol\x12\x41\n\nblock_part\x18\x05 \x01(\x0b\x32 .cometbft.consensus.v1.BlockPartH\x00R\tblockPart\x12\x31\n\x04vote\x18\x06 \x01(\x0b\x32\x1b.cometbft.consensus.v1.VoteH\x00R\x04vote\x12;\n\x08has_vote\x18\x07 \x01(\x0b\x32\x1e.cometbft.consensus.v1.HasVoteH\x00R\x07hasVote\x12K\n\x0evote_set_maj23\x18\x08 \x01(\x0b\x32#.cometbft.consensus.v1.VoteSetMaj23H\x00R\x0cvoteSetMaj23\x12H\n\rvote_set_bits\x18\t \x01(\x0b\x32\".cometbft.consensus.v1.VoteSetBitsH\x00R\x0bvoteSetBits\x12\x64\n\x17has_proposal_block_part\x18\n \x01(\x0b\x32+.cometbft.consensus.v1.HasProposalBlockPartH\x00R\x14hasProposalBlockPartB\x05\n\x03sumB\xd5\x01\n\x19\x63om.cometbft.consensus.v1B\nTypesProtoP\x01Z6github.com/cometbft/cometbft/api/cometbft/consensus/v1\xa2\x02\x03\x43\x43X\xaa\x02\x15\x43ometbft.Consensus.V1\xca\x02\x15\x43ometbft\\Consensus\\V1\xe2\x02!Cometbft\\Consensus\\V1\\GPBMetadata\xea\x02\x17\x43ometbft::Consensus::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cometbft.consensus.v1.types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.cometbft.consensus.v1B\nTypesProtoP\001Z6github.com/cometbft/cometbft/api/cometbft/consensus/v1\242\002\003CCX\252\002\025Cometbft.Consensus.V1\312\002\025Cometbft\\Consensus\\V1\342\002!Cometbft\\Consensus\\V1\\GPBMetadata\352\002\027Cometbft::Consensus::V1'
  _globals['_NEWVALIDBLOCK'].fields_by_name['block_part_set_header']._loaded_options = None
  _globals['_NEWVALIDBLOCK'].fields_by_name['block_part_set_header']._serialized_options = b'\310\336\037\000'
  _globals['_PROPOSAL'].fields_by_name['proposal']._loaded_options = None
  _globals['_PROPOSAL'].fields_by_name['proposal']._serialized_options = b'\310\336\037\000'
  _globals['_PROPOSALPOL'].fields_by_name['proposal_pol']._loaded_options = None
  _globals['_PROPOSALPOL'].fields_by_name['proposal_pol']._serialized_options = b'\310\336\037\000'
  _globals['_BLOCKPART'].fields_by_name['part']._loaded_options = None
  _globals['_BLOCKPART'].fields_by_name['part']._serialized_options = b'\310\336\037\000'
  _globals['_VOTESETMAJ23'].fields_by_name['block_id']._loaded_options = None
  _globals['_VOTESETMAJ23'].fields_by_name['block_id']._serialized_options = b'\310\336\037\000\342\336\037\007BlockID'
  _globals['_VOTESETBITS'].fields_by_name['block_id']._loaded_options = None
  _globals['_VOTESETBITS'].fields_by_name['block_id']._serialized_options = b'\310\336\037\000\342\336\037\007BlockID'
  _globals['_VOTESETBITS'].fields_by_name['votes']._loaded_options = None
  _globals['_VOTESETBITS'].fields_by_name['votes']._serialized_options = b'\310\336\037\000'
  _globals['_NEWROUNDSTEP']._serialized_start=149
  _globals['_NEWROUNDSTEP']._serialized_end=330
  _globals['_NEWVALIDBLOCK']._serialized_start=333
  _globals['_NEWVALIDBLOCK']._serialized_end=580
  _globals['_PROPOSAL']._serialized_start=582
  _globals['_PROPOSAL']._serialized_end=655
  _globals['_PROPOSALPOL']._serialized_start=658
  _globals['_PROPOSALPOL']._serialized_end=815
  _globals['_BLOCKPART']._serialized_start=817
  _globals['_BLOCKPART']._serialized_end=925
  _globals['_VOTE']._serialized_start=927
  _globals['_VOTE']._serialized_end=978
  _globals['_HASVOTE']._serialized_start=981
  _globals['_HASVOTE']._serialized_end=1112
  _globals['_VOTESETMAJ23']._serialized_start=1115
  _globals['_VOTESETMAJ23']._serialized_end=1301
  _globals['_VOTESETBITS']._serialized_start=1304
  _globals['_VOTESETBITS']._serialized_end=1550
  _globals['_HASPROPOSALBLOCKPART']._serialized_start=1552
  _globals['_HASPROPOSALBLOCKPART']._serialized_end=1642
  _globals['_MESSAGE']._serialized_start=1645
  _globals['_MESSAGE']._serialized_end=2386
# @@protoc_insertion_point(module_scope)
