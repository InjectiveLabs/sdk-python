# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cometbft/consensus/v1beta1/types.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cometbft.types.v1beta1 import types_pb2 as cometbft_dot_types_dot_v1beta1_dot_types__pb2
from pyinjective.proto.cometbft.libs.bits.v1 import types_pb2 as cometbft_dot_libs_dot_bits_dot_v1_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&cometbft/consensus/v1beta1/types.proto\x12\x1a\x63ometbft.consensus.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\"cometbft/types/v1beta1/types.proto\x1a!cometbft/libs/bits/v1/types.proto\"\xb5\x01\n\x0cNewRoundStep\x12\x16\n\x06height\x18\x01 \x01(\x03R\x06height\x12\x14\n\x05round\x18\x02 \x01(\x05R\x05round\x12\x12\n\x04step\x18\x03 \x01(\rR\x04step\x12\x37\n\x18seconds_since_start_time\x18\x04 \x01(\x03R\x15secondsSinceStartTime\x12*\n\x11last_commit_round\x18\x05 \x01(\x05R\x0flastCommitRound\"\xfc\x01\n\rNewValidBlock\x12\x16\n\x06height\x18\x01 \x01(\x03R\x06height\x12\x14\n\x05round\x18\x02 \x01(\x05R\x05round\x12^\n\x15\x62lock_part_set_header\x18\x03 \x01(\x0b\x32%.cometbft.types.v1beta1.PartSetHeaderB\x04\xc8\xde\x1f\x00R\x12\x62lockPartSetHeader\x12@\n\x0b\x62lock_parts\x18\x04 \x01(\x0b\x32\x1f.cometbft.libs.bits.v1.BitArrayR\nblockParts\x12\x1b\n\tis_commit\x18\x05 \x01(\x08R\x08isCommit\"N\n\x08Proposal\x12\x42\n\x08proposal\x18\x01 \x01(\x0b\x32 .cometbft.types.v1beta1.ProposalB\x04\xc8\xde\x1f\x00R\x08proposal\"\x9d\x01\n\x0bProposalPOL\x12\x16\n\x06height\x18\x01 \x01(\x03R\x06height\x12,\n\x12proposal_pol_round\x18\x02 \x01(\x05R\x10proposalPolRound\x12H\n\x0cproposal_pol\x18\x03 \x01(\x0b\x32\x1f.cometbft.libs.bits.v1.BitArrayB\x04\xc8\xde\x1f\x00R\x0bproposalPol\"q\n\tBlockPart\x12\x16\n\x06height\x18\x01 \x01(\x03R\x06height\x12\x14\n\x05round\x18\x02 \x01(\x05R\x05round\x12\x36\n\x04part\x18\x03 \x01(\x0b\x32\x1c.cometbft.types.v1beta1.PartB\x04\xc8\xde\x1f\x00R\x04part\"8\n\x04Vote\x12\x30\n\x04vote\x18\x01 \x01(\x0b\x32\x1c.cometbft.types.v1beta1.VoteR\x04vote\"\x88\x01\n\x07HasVote\x12\x16\n\x06height\x18\x01 \x01(\x03R\x06height\x12\x14\n\x05round\x18\x02 \x01(\x05R\x05round\x12\x39\n\x04type\x18\x03 \x01(\x0e\x32%.cometbft.types.v1beta1.SignedMsgTypeR\x04type\x12\x14\n\x05index\x18\x04 \x01(\x05R\x05index\"\xc4\x01\n\x0cVoteSetMaj23\x12\x16\n\x06height\x18\x01 \x01(\x03R\x06height\x12\x14\n\x05round\x18\x02 \x01(\x05R\x05round\x12\x39\n\x04type\x18\x03 \x01(\x0e\x32%.cometbft.types.v1beta1.SignedMsgTypeR\x04type\x12K\n\x08\x62lock_id\x18\x04 \x01(\x0b\x32\x1f.cometbft.types.v1beta1.BlockIDB\x0f\xc8\xde\x1f\x00\xe2\xde\x1f\x07\x42lockIDR\x07\x62lockId\"\x80\x02\n\x0bVoteSetBits\x12\x16\n\x06height\x18\x01 \x01(\x03R\x06height\x12\x14\n\x05round\x18\x02 \x01(\x05R\x05round\x12\x39\n\x04type\x18\x03 \x01(\x0e\x32%.cometbft.types.v1beta1.SignedMsgTypeR\x04type\x12K\n\x08\x62lock_id\x18\x04 \x01(\x0b\x32\x1f.cometbft.types.v1beta1.BlockIDB\x0f\xc8\xde\x1f\x00\xe2\xde\x1f\x07\x42lockIDR\x07\x62lockId\x12;\n\x05votes\x18\x05 \x01(\x0b\x32\x1f.cometbft.libs.bits.v1.BitArrayB\x04\xc8\xde\x1f\x00R\x05votes\"\xac\x05\n\x07Message\x12P\n\x0enew_round_step\x18\x01 \x01(\x0b\x32(.cometbft.consensus.v1beta1.NewRoundStepH\x00R\x0cnewRoundStep\x12S\n\x0fnew_valid_block\x18\x02 \x01(\x0b\x32).cometbft.consensus.v1beta1.NewValidBlockH\x00R\rnewValidBlock\x12\x42\n\x08proposal\x18\x03 \x01(\x0b\x32$.cometbft.consensus.v1beta1.ProposalH\x00R\x08proposal\x12L\n\x0cproposal_pol\x18\x04 \x01(\x0b\x32\'.cometbft.consensus.v1beta1.ProposalPOLH\x00R\x0bproposalPol\x12\x46\n\nblock_part\x18\x05 \x01(\x0b\x32%.cometbft.consensus.v1beta1.BlockPartH\x00R\tblockPart\x12\x36\n\x04vote\x18\x06 \x01(\x0b\x32 .cometbft.consensus.v1beta1.VoteH\x00R\x04vote\x12@\n\x08has_vote\x18\x07 \x01(\x0b\x32#.cometbft.consensus.v1beta1.HasVoteH\x00R\x07hasVote\x12P\n\x0evote_set_maj23\x18\x08 \x01(\x0b\x32(.cometbft.consensus.v1beta1.VoteSetMaj23H\x00R\x0cvoteSetMaj23\x12M\n\rvote_set_bits\x18\t \x01(\x0b\x32\'.cometbft.consensus.v1beta1.VoteSetBitsH\x00R\x0bvoteSetBitsB\x05\n\x03sumB\xf3\x01\n\x1e\x63om.cometbft.consensus.v1beta1B\nTypesProtoP\x01Z;github.com/cometbft/cometbft/api/cometbft/consensus/v1beta1\xa2\x02\x03\x43\x43X\xaa\x02\x1a\x43ometbft.Consensus.V1beta1\xca\x02\x1a\x43ometbft\\Consensus\\V1beta1\xe2\x02&Cometbft\\Consensus\\V1beta1\\GPBMetadata\xea\x02\x1c\x43ometbft::Consensus::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cometbft.consensus.v1beta1.types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.cometbft.consensus.v1beta1B\nTypesProtoP\001Z;github.com/cometbft/cometbft/api/cometbft/consensus/v1beta1\242\002\003CCX\252\002\032Cometbft.Consensus.V1beta1\312\002\032Cometbft\\Consensus\\V1beta1\342\002&Cometbft\\Consensus\\V1beta1\\GPBMetadata\352\002\034Cometbft::Consensus::V1beta1'
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
  _globals['_NEWROUNDSTEP']._serialized_start=164
  _globals['_NEWROUNDSTEP']._serialized_end=345
  _globals['_NEWVALIDBLOCK']._serialized_start=348
  _globals['_NEWVALIDBLOCK']._serialized_end=600
  _globals['_PROPOSAL']._serialized_start=602
  _globals['_PROPOSAL']._serialized_end=680
  _globals['_PROPOSALPOL']._serialized_start=683
  _globals['_PROPOSALPOL']._serialized_end=840
  _globals['_BLOCKPART']._serialized_start=842
  _globals['_BLOCKPART']._serialized_end=955
  _globals['_VOTE']._serialized_start=957
  _globals['_VOTE']._serialized_end=1013
  _globals['_HASVOTE']._serialized_start=1016
  _globals['_HASVOTE']._serialized_end=1152
  _globals['_VOTESETMAJ23']._serialized_start=1155
  _globals['_VOTESETMAJ23']._serialized_end=1351
  _globals['_VOTESETBITS']._serialized_start=1354
  _globals['_VOTESETBITS']._serialized_end=1610
  _globals['_MESSAGE']._serialized_start=1613
  _globals['_MESSAGE']._serialized_end=2297
# @@protoc_insertion_point(module_scope)
