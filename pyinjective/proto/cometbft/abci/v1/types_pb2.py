# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cometbft/abci/v1/types.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.cometbft.crypto.v1 import proof_pb2 as cometbft_dot_crypto_dot_v1_dot_proof__pb2
from pyinjective.proto.cometbft.types.v1 import params_pb2 as cometbft_dot_types_dot_v1_dot_params__pb2
from pyinjective.proto.cometbft.types.v1 import validator_pb2 as cometbft_dot_types_dot_v1_dot_validator__pb2
from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x63ometbft/abci/v1/types.proto\x12\x10\x63ometbft.abci.v1\x1a\x1e\x63ometbft/crypto/v1/proof.proto\x1a\x1e\x63ometbft/types/v1/params.proto\x1a!cometbft/types/v1/validator.proto\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xcf\t\n\x07Request\x12\x33\n\x04\x65\x63ho\x18\x01 \x01(\x0b\x32\x1d.cometbft.abci.v1.EchoRequestH\x00R\x04\x65\x63ho\x12\x36\n\x05\x66lush\x18\x02 \x01(\x0b\x32\x1e.cometbft.abci.v1.FlushRequestH\x00R\x05\x66lush\x12\x33\n\x04info\x18\x03 \x01(\x0b\x32\x1d.cometbft.abci.v1.InfoRequestH\x00R\x04info\x12\x43\n\ninit_chain\x18\x05 \x01(\x0b\x32\".cometbft.abci.v1.InitChainRequestH\x00R\tinitChain\x12\x36\n\x05query\x18\x06 \x01(\x0b\x32\x1e.cometbft.abci.v1.QueryRequestH\x00R\x05query\x12=\n\x08\x63heck_tx\x18\x08 \x01(\x0b\x32 .cometbft.abci.v1.CheckTxRequestH\x00R\x07\x63heckTx\x12\x39\n\x06\x63ommit\x18\x0b \x01(\x0b\x32\x1f.cometbft.abci.v1.CommitRequestH\x00R\x06\x63ommit\x12O\n\x0elist_snapshots\x18\x0c \x01(\x0b\x32&.cometbft.abci.v1.ListSnapshotsRequestH\x00R\rlistSnapshots\x12O\n\x0eoffer_snapshot\x18\r \x01(\x0b\x32&.cometbft.abci.v1.OfferSnapshotRequestH\x00R\rofferSnapshot\x12\\\n\x13load_snapshot_chunk\x18\x0e \x01(\x0b\x32*.cometbft.abci.v1.LoadSnapshotChunkRequestH\x00R\x11loadSnapshotChunk\x12_\n\x14\x61pply_snapshot_chunk\x18\x0f \x01(\x0b\x32+.cometbft.abci.v1.ApplySnapshotChunkRequestH\x00R\x12\x61pplySnapshotChunk\x12U\n\x10prepare_proposal\x18\x10 \x01(\x0b\x32(.cometbft.abci.v1.PrepareProposalRequestH\x00R\x0fprepareProposal\x12U\n\x10process_proposal\x18\x11 \x01(\x0b\x32(.cometbft.abci.v1.ProcessProposalRequestH\x00R\x0fprocessProposal\x12\x46\n\x0b\x65xtend_vote\x18\x12 \x01(\x0b\x32#.cometbft.abci.v1.ExtendVoteRequestH\x00R\nextendVote\x12\x62\n\x15verify_vote_extension\x18\x13 \x01(\x0b\x32,.cometbft.abci.v1.VerifyVoteExtensionRequestH\x00R\x13verifyVoteExtension\x12O\n\x0e\x66inalize_block\x18\x14 \x01(\x0b\x32&.cometbft.abci.v1.FinalizeBlockRequestH\x00R\rfinalizeBlockB\x07\n\x05valueJ\x04\x08\x04\x10\x05J\x04\x08\x07\x10\x08J\x04\x08\t\x10\nJ\x04\x08\n\x10\x0b\"\'\n\x0b\x45\x63hoRequest\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message\"\x0e\n\x0c\x46lushRequest\"\x90\x01\n\x0bInfoRequest\x12\x18\n\x07version\x18\x01 \x01(\tR\x07version\x12#\n\rblock_version\x18\x02 \x01(\x04R\x0c\x62lockVersion\x12\x1f\n\x0bp2p_version\x18\x03 \x01(\x04R\np2pVersion\x12!\n\x0c\x61\x62\x63i_version\x18\x04 \x01(\tR\x0b\x61\x62\x63iVersion\"\xce\x02\n\x10InitChainRequest\x12\x38\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01R\x04time\x12\x19\n\x08\x63hain_id\x18\x02 \x01(\tR\x07\x63hainId\x12M\n\x10\x63onsensus_params\x18\x03 \x01(\x0b\x32\".cometbft.types.v1.ConsensusParamsR\x0f\x63onsensusParams\x12G\n\nvalidators\x18\x04 \x03(\x0b\x32!.cometbft.abci.v1.ValidatorUpdateB\x04\xc8\xde\x1f\x00R\nvalidators\x12&\n\x0f\x61pp_state_bytes\x18\x05 \x01(\x0cR\rappStateBytes\x12%\n\x0einitial_height\x18\x06 \x01(\x03R\rinitialHeight\"d\n\x0cQueryRequest\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x0cR\x04\x64\x61ta\x12\x12\n\x04path\x18\x02 \x01(\tR\x04path\x12\x16\n\x06height\x18\x03 \x01(\x03R\x06height\x12\x14\n\x05prove\x18\x04 \x01(\x08R\x05prove\"Y\n\x0e\x43heckTxRequest\x12\x0e\n\x02tx\x18\x01 \x01(\x0cR\x02tx\x12\x31\n\x04type\x18\x03 \x01(\x0e\x32\x1d.cometbft.abci.v1.CheckTxTypeR\x04typeJ\x04\x08\x02\x10\x03\"\x0f\n\rCommitRequest\"\x16\n\x14ListSnapshotsRequest\"i\n\x14OfferSnapshotRequest\x12\x36\n\x08snapshot\x18\x01 \x01(\x0b\x32\x1a.cometbft.abci.v1.SnapshotR\x08snapshot\x12\x19\n\x08\x61pp_hash\x18\x02 \x01(\x0cR\x07\x61ppHash\"`\n\x18LoadSnapshotChunkRequest\x12\x16\n\x06height\x18\x01 \x01(\x04R\x06height\x12\x16\n\x06\x66ormat\x18\x02 \x01(\rR\x06\x66ormat\x12\x14\n\x05\x63hunk\x18\x03 \x01(\rR\x05\x63hunk\"_\n\x19\x41pplySnapshotChunkRequest\x12\x14\n\x05index\x18\x01 \x01(\rR\x05index\x12\x14\n\x05\x63hunk\x18\x02 \x01(\x0cR\x05\x63hunk\x12\x16\n\x06sender\x18\x03 \x01(\tR\x06sender\"\x9a\x03\n\x16PrepareProposalRequest\x12 \n\x0cmax_tx_bytes\x18\x01 \x01(\x03R\nmaxTxBytes\x12\x10\n\x03txs\x18\x02 \x03(\x0cR\x03txs\x12V\n\x11local_last_commit\x18\x03 \x01(\x0b\x32$.cometbft.abci.v1.ExtendedCommitInfoB\x04\xc8\xde\x1f\x00R\x0flocalLastCommit\x12\x45\n\x0bmisbehavior\x18\x04 \x03(\x0b\x32\x1d.cometbft.abci.v1.MisbehaviorB\x04\xc8\xde\x1f\x00R\x0bmisbehavior\x12\x16\n\x06height\x18\x05 \x01(\x03R\x06height\x12\x38\n\x04time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01R\x04time\x12\x30\n\x14next_validators_hash\x18\x07 \x01(\x0cR\x12nextValidatorsHash\x12)\n\x10proposer_address\x18\x08 \x01(\x0cR\x0fproposerAddress\"\x8a\x03\n\x16ProcessProposalRequest\x12\x10\n\x03txs\x18\x01 \x03(\x0cR\x03txs\x12T\n\x14proposed_last_commit\x18\x02 \x01(\x0b\x32\x1c.cometbft.abci.v1.CommitInfoB\x04\xc8\xde\x1f\x00R\x12proposedLastCommit\x12\x45\n\x0bmisbehavior\x18\x03 \x03(\x0b\x32\x1d.cometbft.abci.v1.MisbehaviorB\x04\xc8\xde\x1f\x00R\x0bmisbehavior\x12\x12\n\x04hash\x18\x04 \x01(\x0cR\x04hash\x12\x16\n\x06height\x18\x05 \x01(\x03R\x06height\x12\x38\n\x04time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01R\x04time\x12\x30\n\x14next_validators_hash\x18\x07 \x01(\x0cR\x12nextValidatorsHash\x12)\n\x10proposer_address\x18\x08 \x01(\x0cR\x0fproposerAddress\"\x85\x03\n\x11\x45xtendVoteRequest\x12\x12\n\x04hash\x18\x01 \x01(\x0cR\x04hash\x12\x16\n\x06height\x18\x02 \x01(\x03R\x06height\x12\x38\n\x04time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01R\x04time\x12\x10\n\x03txs\x18\x04 \x03(\x0cR\x03txs\x12T\n\x14proposed_last_commit\x18\x05 \x01(\x0b\x32\x1c.cometbft.abci.v1.CommitInfoB\x04\xc8\xde\x1f\x00R\x12proposedLastCommit\x12\x45\n\x0bmisbehavior\x18\x06 \x03(\x0b\x32\x1d.cometbft.abci.v1.MisbehaviorB\x04\xc8\xde\x1f\x00R\x0bmisbehavior\x12\x30\n\x14next_validators_hash\x18\x07 \x01(\x0cR\x12nextValidatorsHash\x12)\n\x10proposer_address\x18\x08 \x01(\x0cR\x0fproposerAddress\"\x9c\x01\n\x1aVerifyVoteExtensionRequest\x12\x12\n\x04hash\x18\x01 \x01(\x0cR\x04hash\x12+\n\x11validator_address\x18\x02 \x01(\x0cR\x10validatorAddress\x12\x16\n\x06height\x18\x03 \x01(\x03R\x06height\x12%\n\x0evote_extension\x18\x04 \x01(\x0cR\rvoteExtension\"\xb2\x03\n\x14\x46inalizeBlockRequest\x12\x10\n\x03txs\x18\x01 \x03(\x0cR\x03txs\x12R\n\x13\x64\x65\x63ided_last_commit\x18\x02 \x01(\x0b\x32\x1c.cometbft.abci.v1.CommitInfoB\x04\xc8\xde\x1f\x00R\x11\x64\x65\x63idedLastCommit\x12\x45\n\x0bmisbehavior\x18\x03 \x03(\x0b\x32\x1d.cometbft.abci.v1.MisbehaviorB\x04\xc8\xde\x1f\x00R\x0bmisbehavior\x12\x12\n\x04hash\x18\x04 \x01(\x0cR\x04hash\x12\x16\n\x06height\x18\x05 \x01(\x03R\x06height\x12\x38\n\x04time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01R\x04time\x12\x30\n\x14next_validators_hash\x18\x07 \x01(\x0cR\x12nextValidatorsHash\x12)\n\x10proposer_address\x18\x08 \x01(\x0cR\x0fproposerAddress\x12*\n\x11syncing_to_height\x18\t \x01(\x03R\x0fsyncingToHeight\"\xa5\n\n\x08Response\x12\x43\n\texception\x18\x01 \x01(\x0b\x32#.cometbft.abci.v1.ExceptionResponseH\x00R\texception\x12\x34\n\x04\x65\x63ho\x18\x02 \x01(\x0b\x32\x1e.cometbft.abci.v1.EchoResponseH\x00R\x04\x65\x63ho\x12\x37\n\x05\x66lush\x18\x03 \x01(\x0b\x32\x1f.cometbft.abci.v1.FlushResponseH\x00R\x05\x66lush\x12\x34\n\x04info\x18\x04 \x01(\x0b\x32\x1e.cometbft.abci.v1.InfoResponseH\x00R\x04info\x12\x44\n\ninit_chain\x18\x06 \x01(\x0b\x32#.cometbft.abci.v1.InitChainResponseH\x00R\tinitChain\x12\x37\n\x05query\x18\x07 \x01(\x0b\x32\x1f.cometbft.abci.v1.QueryResponseH\x00R\x05query\x12>\n\x08\x63heck_tx\x18\t \x01(\x0b\x32!.cometbft.abci.v1.CheckTxResponseH\x00R\x07\x63heckTx\x12:\n\x06\x63ommit\x18\x0c \x01(\x0b\x32 .cometbft.abci.v1.CommitResponseH\x00R\x06\x63ommit\x12P\n\x0elist_snapshots\x18\r \x01(\x0b\x32\'.cometbft.abci.v1.ListSnapshotsResponseH\x00R\rlistSnapshots\x12P\n\x0eoffer_snapshot\x18\x0e \x01(\x0b\x32\'.cometbft.abci.v1.OfferSnapshotResponseH\x00R\rofferSnapshot\x12]\n\x13load_snapshot_chunk\x18\x0f \x01(\x0b\x32+.cometbft.abci.v1.LoadSnapshotChunkResponseH\x00R\x11loadSnapshotChunk\x12`\n\x14\x61pply_snapshot_chunk\x18\x10 \x01(\x0b\x32,.cometbft.abci.v1.ApplySnapshotChunkResponseH\x00R\x12\x61pplySnapshotChunk\x12V\n\x10prepare_proposal\x18\x11 \x01(\x0b\x32).cometbft.abci.v1.PrepareProposalResponseH\x00R\x0fprepareProposal\x12V\n\x10process_proposal\x18\x12 \x01(\x0b\x32).cometbft.abci.v1.ProcessProposalResponseH\x00R\x0fprocessProposal\x12G\n\x0b\x65xtend_vote\x18\x13 \x01(\x0b\x32$.cometbft.abci.v1.ExtendVoteResponseH\x00R\nextendVote\x12\x63\n\x15verify_vote_extension\x18\x14 \x01(\x0b\x32-.cometbft.abci.v1.VerifyVoteExtensionResponseH\x00R\x13verifyVoteExtension\x12P\n\x0e\x66inalize_block\x18\x15 \x01(\x0b\x32\'.cometbft.abci.v1.FinalizeBlockResponseH\x00R\rfinalizeBlockB\x07\n\x05valueJ\x04\x08\x05\x10\x06J\x04\x08\x08\x10\tJ\x04\x08\n\x10\x0bJ\x04\x08\x0b\x10\x0c\")\n\x11\x45xceptionResponse\x12\x14\n\x05\x65rror\x18\x01 \x01(\tR\x05\x65rror\"(\n\x0c\x45\x63hoResponse\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message\"\x0f\n\rFlushResponse\"\xfb\x02\n\x0cInfoResponse\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\tR\x04\x64\x61ta\x12\x18\n\x07version\x18\x02 \x01(\tR\x07version\x12\x1f\n\x0b\x61pp_version\x18\x03 \x01(\x04R\nappVersion\x12*\n\x11last_block_height\x18\x04 \x01(\x03R\x0flastBlockHeight\x12-\n\x13last_block_app_hash\x18\x05 \x01(\x0cR\x10lastBlockAppHash\x12[\n\x0flane_priorities\x18\x06 \x03(\x0b\x32\x32.cometbft.abci.v1.InfoResponse.LanePrioritiesEntryR\x0elanePriorities\x12!\n\x0c\x64\x65\x66\x61ult_lane\x18\x07 \x01(\tR\x0b\x64\x65\x66\x61ultLane\x1a\x41\n\x13LanePrioritiesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\rR\x05value:\x02\x38\x01\"\xc6\x01\n\x11InitChainResponse\x12M\n\x10\x63onsensus_params\x18\x01 \x01(\x0b\x32\".cometbft.types.v1.ConsensusParamsR\x0f\x63onsensusParams\x12G\n\nvalidators\x18\x02 \x03(\x0b\x32!.cometbft.abci.v1.ValidatorUpdateB\x04\xc8\xde\x1f\x00R\nvalidators\x12\x19\n\x08\x61pp_hash\x18\x03 \x01(\x0cR\x07\x61ppHash\"\xf8\x01\n\rQueryResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\rR\x04\x63ode\x12\x10\n\x03log\x18\x03 \x01(\tR\x03log\x12\x12\n\x04info\x18\x04 \x01(\tR\x04info\x12\x14\n\x05index\x18\x05 \x01(\x03R\x05index\x12\x10\n\x03key\x18\x06 \x01(\x0cR\x03key\x12\x14\n\x05value\x18\x07 \x01(\x0cR\x05value\x12\x39\n\tproof_ops\x18\x08 \x01(\x0b\x32\x1c.cometbft.crypto.v1.ProofOpsR\x08proofOps\x12\x16\n\x06height\x18\t \x01(\x03R\x06height\x12\x1c\n\tcodespace\x18\n \x01(\tR\tcodespace\"\xc4\x02\n\x0f\x43heckTxResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\rR\x04\x63ode\x12\x12\n\x04\x64\x61ta\x18\x02 \x01(\x0cR\x04\x64\x61ta\x12\x10\n\x03log\x18\x03 \x01(\tR\x03log\x12\x12\n\x04info\x18\x04 \x01(\tR\x04info\x12\x1e\n\ngas_wanted\x18\x05 \x01(\x03R\ngas_wanted\x12\x1a\n\x08gas_used\x18\x06 \x01(\x03R\x08gas_used\x12I\n\x06\x65vents\x18\x07 \x03(\x0b\x32\x17.cometbft.abci.v1.EventB\x18\xc8\xde\x1f\x00\xea\xde\x1f\x10\x65vents,omitemptyR\x06\x65vents\x12\x1c\n\tcodespace\x18\x08 \x01(\tR\tcodespace\x12\x17\n\x07lane_id\x18\x0c \x01(\tR\x06laneIdJ\x04\x08\t\x10\x0cR\x06senderR\x08priorityR\rmempool_error\"A\n\x0e\x43ommitResponse\x12#\n\rretain_height\x18\x03 \x01(\x03R\x0cretainHeightJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03\"Q\n\x15ListSnapshotsResponse\x12\x38\n\tsnapshots\x18\x01 \x03(\x0b\x32\x1a.cometbft.abci.v1.SnapshotR\tsnapshots\"V\n\x15OfferSnapshotResponse\x12=\n\x06result\x18\x01 \x01(\x0e\x32%.cometbft.abci.v1.OfferSnapshotResultR\x06result\"1\n\x19LoadSnapshotChunkResponse\x12\x14\n\x05\x63hunk\x18\x01 \x01(\x0cR\x05\x63hunk\"\xae\x01\n\x1a\x41pplySnapshotChunkResponse\x12\x42\n\x06result\x18\x01 \x01(\x0e\x32*.cometbft.abci.v1.ApplySnapshotChunkResultR\x06result\x12%\n\x0erefetch_chunks\x18\x02 \x03(\rR\rrefetchChunks\x12%\n\x0ereject_senders\x18\x03 \x03(\tR\rrejectSenders\"+\n\x17PrepareProposalResponse\x12\x10\n\x03txs\x18\x01 \x03(\x0cR\x03txs\"Z\n\x17ProcessProposalResponse\x12?\n\x06status\x18\x01 \x01(\x0e\x32\'.cometbft.abci.v1.ProcessProposalStatusR\x06status\";\n\x12\x45xtendVoteResponse\x12%\n\x0evote_extension\x18\x01 \x01(\x0cR\rvoteExtension\"b\n\x1bVerifyVoteExtensionResponse\x12\x43\n\x06status\x18\x01 \x01(\x0e\x32+.cometbft.abci.v1.VerifyVoteExtensionStatusR\x06status\"\xee\x02\n\x15\x46inalizeBlockResponse\x12I\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x17.cometbft.abci.v1.EventB\x18\xc8\xde\x1f\x00\xea\xde\x1f\x10\x65vents,omitemptyR\x06\x65vents\x12=\n\ntx_results\x18\x02 \x03(\x0b\x32\x1e.cometbft.abci.v1.ExecTxResultR\ttxResults\x12T\n\x11validator_updates\x18\x03 \x03(\x0b\x32!.cometbft.abci.v1.ValidatorUpdateB\x04\xc8\xde\x1f\x00R\x10validatorUpdates\x12Z\n\x17\x63onsensus_param_updates\x18\x04 \x01(\x0b\x32\".cometbft.types.v1.ConsensusParamsR\x15\x63onsensusParamUpdates\x12\x19\n\x08\x61pp_hash\x18\x05 \x01(\x0cR\x07\x61ppHash\"Z\n\nCommitInfo\x12\x14\n\x05round\x18\x01 \x01(\x05R\x05round\x12\x36\n\x05votes\x18\x02 \x03(\x0b\x32\x1a.cometbft.abci.v1.VoteInfoB\x04\xc8\xde\x1f\x00R\x05votes\"j\n\x12\x45xtendedCommitInfo\x12\x14\n\x05round\x18\x01 \x01(\x05R\x05round\x12>\n\x05votes\x18\x02 \x03(\x0b\x32\".cometbft.abci.v1.ExtendedVoteInfoB\x04\xc8\xde\x1f\x00R\x05votes\"{\n\x05\x45vent\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12^\n\nattributes\x18\x02 \x03(\x0b\x32 .cometbft.abci.v1.EventAttributeB\x1c\xc8\xde\x1f\x00\xea\xde\x1f\x14\x61ttributes,omitemptyR\nattributes\"N\n\x0e\x45ventAttribute\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\x12\x14\n\x05index\x18\x03 \x01(\x08R\x05index\"\x81\x02\n\x0c\x45xecTxResult\x12\x12\n\x04\x63ode\x18\x01 \x01(\rR\x04\x63ode\x12\x12\n\x04\x64\x61ta\x18\x02 \x01(\x0cR\x04\x64\x61ta\x12\x10\n\x03log\x18\x03 \x01(\tR\x03log\x12\x12\n\x04info\x18\x04 \x01(\tR\x04info\x12\x1e\n\ngas_wanted\x18\x05 \x01(\x03R\ngas_wanted\x12\x1a\n\x08gas_used\x18\x06 \x01(\x03R\x08gas_used\x12I\n\x06\x65vents\x18\x07 \x03(\x0b\x32\x17.cometbft.abci.v1.EventB\x18\xc8\xde\x1f\x00\xea\xde\x1f\x10\x65vents,omitemptyR\x06\x65vents\x12\x1c\n\tcodespace\x18\x08 \x01(\tR\tcodespace\"\x86\x01\n\x08TxResult\x12\x16\n\x06height\x18\x01 \x01(\x03R\x06height\x12\x14\n\x05index\x18\x02 \x01(\rR\x05index\x12\x0e\n\x02tx\x18\x03 \x01(\x0cR\x02tx\x12<\n\x06result\x18\x04 \x01(\x0b\x32\x1e.cometbft.abci.v1.ExecTxResultB\x04\xc8\xde\x1f\x00R\x06result\";\n\tValidator\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0cR\x07\x61\x64\x64ress\x12\x14\n\x05power\x18\x03 \x01(\x03R\x05power\"s\n\x0fValidatorUpdate\x12\x14\n\x05power\x18\x02 \x01(\x03R\x05power\x12\"\n\rpub_key_bytes\x18\x03 \x01(\x0cR\x0bpubKeyBytes\x12 \n\x0cpub_key_type\x18\x04 \x01(\tR\npubKeyTypeJ\x04\x08\x01\x10\x02\"\x95\x01\n\x08VoteInfo\x12?\n\tvalidator\x18\x01 \x01(\x0b\x32\x1b.cometbft.abci.v1.ValidatorB\x04\xc8\xde\x1f\x00R\tvalidator\x12\x42\n\rblock_id_flag\x18\x03 \x01(\x0e\x32\x1e.cometbft.types.v1.BlockIDFlagR\x0b\x62lockIdFlagJ\x04\x08\x02\x10\x03\"\xf5\x01\n\x10\x45xtendedVoteInfo\x12?\n\tvalidator\x18\x01 \x01(\x0b\x32\x1b.cometbft.abci.v1.ValidatorB\x04\xc8\xde\x1f\x00R\tvalidator\x12%\n\x0evote_extension\x18\x03 \x01(\x0cR\rvoteExtension\x12/\n\x13\x65xtension_signature\x18\x04 \x01(\x0cR\x12\x65xtensionSignature\x12\x42\n\rblock_id_flag\x18\x05 \x01(\x0e\x32\x1e.cometbft.types.v1.BlockIDFlagR\x0b\x62lockIdFlagJ\x04\x08\x02\x10\x03\"\x85\x02\n\x0bMisbehavior\x12\x35\n\x04type\x18\x01 \x01(\x0e\x32!.cometbft.abci.v1.MisbehaviorTypeR\x04type\x12?\n\tvalidator\x18\x02 \x01(\x0b\x32\x1b.cometbft.abci.v1.ValidatorB\x04\xc8\xde\x1f\x00R\tvalidator\x12\x16\n\x06height\x18\x03 \x01(\x03R\x06height\x12\x38\n\x04time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01R\x04time\x12,\n\x12total_voting_power\x18\x05 \x01(\x03R\x10totalVotingPower\"\x82\x01\n\x08Snapshot\x12\x16\n\x06height\x18\x01 \x01(\x04R\x06height\x12\x16\n\x06\x66ormat\x18\x02 \x01(\rR\x06\x66ormat\x12\x16\n\x06\x63hunks\x18\x03 \x01(\rR\x06\x63hunks\x12\x12\n\x04hash\x18\x04 \x01(\x0cR\x04hash\x12\x1a\n\x08metadata\x18\x05 \x01(\x0cR\x08metadata*b\n\x0b\x43heckTxType\x12\x19\n\x15\x43HECK_TX_TYPE_UNKNOWN\x10\x00\x12\x19\n\x15\x43HECK_TX_TYPE_RECHECK\x10\x01\x12\x17\n\x13\x43HECK_TX_TYPE_CHECK\x10\x02\x1a\x04\x88\xa3\x1e\x00*\xf5\x01\n\x13OfferSnapshotResult\x12!\n\x1dOFFER_SNAPSHOT_RESULT_UNKNOWN\x10\x00\x12 \n\x1cOFFER_SNAPSHOT_RESULT_ACCEPT\x10\x01\x12\x1f\n\x1bOFFER_SNAPSHOT_RESULT_ABORT\x10\x02\x12 \n\x1cOFFER_SNAPSHOT_RESULT_REJECT\x10\x03\x12\'\n#OFFER_SNAPSHOT_RESULT_REJECT_FORMAT\x10\x04\x12\'\n#OFFER_SNAPSHOT_RESULT_REJECT_SENDER\x10\x05\x1a\x04\x88\xa3\x1e\x00*\xa0\x02\n\x18\x41pplySnapshotChunkResult\x12\'\n#APPLY_SNAPSHOT_CHUNK_RESULT_UNKNOWN\x10\x00\x12&\n\"APPLY_SNAPSHOT_CHUNK_RESULT_ACCEPT\x10\x01\x12%\n!APPLY_SNAPSHOT_CHUNK_RESULT_ABORT\x10\x02\x12%\n!APPLY_SNAPSHOT_CHUNK_RESULT_RETRY\x10\x03\x12.\n*APPLY_SNAPSHOT_CHUNK_RESULT_RETRY_SNAPSHOT\x10\x04\x12/\n+APPLY_SNAPSHOT_CHUNK_RESULT_REJECT_SNAPSHOT\x10\x05\x1a\x04\x88\xa3\x1e\x00*\x8a\x01\n\x15ProcessProposalStatus\x12#\n\x1fPROCESS_PROPOSAL_STATUS_UNKNOWN\x10\x00\x12\"\n\x1ePROCESS_PROPOSAL_STATUS_ACCEPT\x10\x01\x12\"\n\x1ePROCESS_PROPOSAL_STATUS_REJECT\x10\x02\x1a\x04\x88\xa3\x1e\x00*\x9d\x01\n\x19VerifyVoteExtensionStatus\x12(\n$VERIFY_VOTE_EXTENSION_STATUS_UNKNOWN\x10\x00\x12\'\n#VERIFY_VOTE_EXTENSION_STATUS_ACCEPT\x10\x01\x12\'\n#VERIFY_VOTE_EXTENSION_STATUS_REJECT\x10\x02\x1a\x04\x88\xa3\x1e\x00*\x84\x01\n\x0fMisbehaviorType\x12\x1c\n\x18MISBEHAVIOR_TYPE_UNKNOWN\x10\x00\x12#\n\x1fMISBEHAVIOR_TYPE_DUPLICATE_VOTE\x10\x01\x12(\n$MISBEHAVIOR_TYPE_LIGHT_CLIENT_ATTACK\x10\x02\x1a\x04\x88\xa3\x1e\x00\x42\xb7\x01\n\x14\x63om.cometbft.abci.v1B\nTypesProtoP\x01Z1github.com/cometbft/cometbft/api/cometbft/abci/v1\xa2\x02\x03\x43\x41X\xaa\x02\x10\x43ometbft.Abci.V1\xca\x02\x10\x43ometbft\\Abci\\V1\xe2\x02\x1c\x43ometbft\\Abci\\V1\\GPBMetadata\xea\x02\x12\x43ometbft::Abci::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cometbft.abci.v1.types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.cometbft.abci.v1B\nTypesProtoP\001Z1github.com/cometbft/cometbft/api/cometbft/abci/v1\242\002\003CAX\252\002\020Cometbft.Abci.V1\312\002\020Cometbft\\Abci\\V1\342\002\034Cometbft\\Abci\\V1\\GPBMetadata\352\002\022Cometbft::Abci::V1'
  _globals['_CHECKTXTYPE']._loaded_options = None
  _globals['_CHECKTXTYPE']._serialized_options = b'\210\243\036\000'
  _globals['_OFFERSNAPSHOTRESULT']._loaded_options = None
  _globals['_OFFERSNAPSHOTRESULT']._serialized_options = b'\210\243\036\000'
  _globals['_APPLYSNAPSHOTCHUNKRESULT']._loaded_options = None
  _globals['_APPLYSNAPSHOTCHUNKRESULT']._serialized_options = b'\210\243\036\000'
  _globals['_PROCESSPROPOSALSTATUS']._loaded_options = None
  _globals['_PROCESSPROPOSALSTATUS']._serialized_options = b'\210\243\036\000'
  _globals['_VERIFYVOTEEXTENSIONSTATUS']._loaded_options = None
  _globals['_VERIFYVOTEEXTENSIONSTATUS']._serialized_options = b'\210\243\036\000'
  _globals['_MISBEHAVIORTYPE']._loaded_options = None
  _globals['_MISBEHAVIORTYPE']._serialized_options = b'\210\243\036\000'
  _globals['_INITCHAINREQUEST'].fields_by_name['time']._loaded_options = None
  _globals['_INITCHAINREQUEST'].fields_by_name['time']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_INITCHAINREQUEST'].fields_by_name['validators']._loaded_options = None
  _globals['_INITCHAINREQUEST'].fields_by_name['validators']._serialized_options = b'\310\336\037\000'
  _globals['_PREPAREPROPOSALREQUEST'].fields_by_name['local_last_commit']._loaded_options = None
  _globals['_PREPAREPROPOSALREQUEST'].fields_by_name['local_last_commit']._serialized_options = b'\310\336\037\000'
  _globals['_PREPAREPROPOSALREQUEST'].fields_by_name['misbehavior']._loaded_options = None
  _globals['_PREPAREPROPOSALREQUEST'].fields_by_name['misbehavior']._serialized_options = b'\310\336\037\000'
  _globals['_PREPAREPROPOSALREQUEST'].fields_by_name['time']._loaded_options = None
  _globals['_PREPAREPROPOSALREQUEST'].fields_by_name['time']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_PROCESSPROPOSALREQUEST'].fields_by_name['proposed_last_commit']._loaded_options = None
  _globals['_PROCESSPROPOSALREQUEST'].fields_by_name['proposed_last_commit']._serialized_options = b'\310\336\037\000'
  _globals['_PROCESSPROPOSALREQUEST'].fields_by_name['misbehavior']._loaded_options = None
  _globals['_PROCESSPROPOSALREQUEST'].fields_by_name['misbehavior']._serialized_options = b'\310\336\037\000'
  _globals['_PROCESSPROPOSALREQUEST'].fields_by_name['time']._loaded_options = None
  _globals['_PROCESSPROPOSALREQUEST'].fields_by_name['time']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_EXTENDVOTEREQUEST'].fields_by_name['time']._loaded_options = None
  _globals['_EXTENDVOTEREQUEST'].fields_by_name['time']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_EXTENDVOTEREQUEST'].fields_by_name['proposed_last_commit']._loaded_options = None
  _globals['_EXTENDVOTEREQUEST'].fields_by_name['proposed_last_commit']._serialized_options = b'\310\336\037\000'
  _globals['_EXTENDVOTEREQUEST'].fields_by_name['misbehavior']._loaded_options = None
  _globals['_EXTENDVOTEREQUEST'].fields_by_name['misbehavior']._serialized_options = b'\310\336\037\000'
  _globals['_FINALIZEBLOCKREQUEST'].fields_by_name['decided_last_commit']._loaded_options = None
  _globals['_FINALIZEBLOCKREQUEST'].fields_by_name['decided_last_commit']._serialized_options = b'\310\336\037\000'
  _globals['_FINALIZEBLOCKREQUEST'].fields_by_name['misbehavior']._loaded_options = None
  _globals['_FINALIZEBLOCKREQUEST'].fields_by_name['misbehavior']._serialized_options = b'\310\336\037\000'
  _globals['_FINALIZEBLOCKREQUEST'].fields_by_name['time']._loaded_options = None
  _globals['_FINALIZEBLOCKREQUEST'].fields_by_name['time']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_INFORESPONSE_LANEPRIORITIESENTRY']._loaded_options = None
  _globals['_INFORESPONSE_LANEPRIORITIESENTRY']._serialized_options = b'8\001'
  _globals['_INITCHAINRESPONSE'].fields_by_name['validators']._loaded_options = None
  _globals['_INITCHAINRESPONSE'].fields_by_name['validators']._serialized_options = b'\310\336\037\000'
  _globals['_CHECKTXRESPONSE'].fields_by_name['events']._loaded_options = None
  _globals['_CHECKTXRESPONSE'].fields_by_name['events']._serialized_options = b'\310\336\037\000\352\336\037\020events,omitempty'
  _globals['_FINALIZEBLOCKRESPONSE'].fields_by_name['events']._loaded_options = None
  _globals['_FINALIZEBLOCKRESPONSE'].fields_by_name['events']._serialized_options = b'\310\336\037\000\352\336\037\020events,omitempty'
  _globals['_FINALIZEBLOCKRESPONSE'].fields_by_name['validator_updates']._loaded_options = None
  _globals['_FINALIZEBLOCKRESPONSE'].fields_by_name['validator_updates']._serialized_options = b'\310\336\037\000'
  _globals['_COMMITINFO'].fields_by_name['votes']._loaded_options = None
  _globals['_COMMITINFO'].fields_by_name['votes']._serialized_options = b'\310\336\037\000'
  _globals['_EXTENDEDCOMMITINFO'].fields_by_name['votes']._loaded_options = None
  _globals['_EXTENDEDCOMMITINFO'].fields_by_name['votes']._serialized_options = b'\310\336\037\000'
  _globals['_EVENT'].fields_by_name['attributes']._loaded_options = None
  _globals['_EVENT'].fields_by_name['attributes']._serialized_options = b'\310\336\037\000\352\336\037\024attributes,omitempty'
  _globals['_EXECTXRESULT'].fields_by_name['events']._loaded_options = None
  _globals['_EXECTXRESULT'].fields_by_name['events']._serialized_options = b'\310\336\037\000\352\336\037\020events,omitempty'
  _globals['_TXRESULT'].fields_by_name['result']._loaded_options = None
  _globals['_TXRESULT'].fields_by_name['result']._serialized_options = b'\310\336\037\000'
  _globals['_VOTEINFO'].fields_by_name['validator']._loaded_options = None
  _globals['_VOTEINFO'].fields_by_name['validator']._serialized_options = b'\310\336\037\000'
  _globals['_EXTENDEDVOTEINFO'].fields_by_name['validator']._loaded_options = None
  _globals['_EXTENDEDVOTEINFO'].fields_by_name['validator']._serialized_options = b'\310\336\037\000'
  _globals['_MISBEHAVIOR'].fields_by_name['validator']._loaded_options = None
  _globals['_MISBEHAVIOR'].fields_by_name['validator']._serialized_options = b'\310\336\037\000'
  _globals['_MISBEHAVIOR'].fields_by_name['time']._loaded_options = None
  _globals['_MISBEHAVIOR'].fields_by_name['time']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_CHECKTXTYPE']._serialized_start=9806
  _globals['_CHECKTXTYPE']._serialized_end=9904
  _globals['_OFFERSNAPSHOTRESULT']._serialized_start=9907
  _globals['_OFFERSNAPSHOTRESULT']._serialized_end=10152
  _globals['_APPLYSNAPSHOTCHUNKRESULT']._serialized_start=10155
  _globals['_APPLYSNAPSHOTCHUNKRESULT']._serialized_end=10443
  _globals['_PROCESSPROPOSALSTATUS']._serialized_start=10446
  _globals['_PROCESSPROPOSALSTATUS']._serialized_end=10584
  _globals['_VERIFYVOTEEXTENSIONSTATUS']._serialized_start=10587
  _globals['_VERIFYVOTEEXTENSIONSTATUS']._serialized_end=10744
  _globals['_MISBEHAVIORTYPE']._serialized_start=10747
  _globals['_MISBEHAVIORTYPE']._serialized_end=10879
  _globals['_REQUEST']._serialized_start=205
  _globals['_REQUEST']._serialized_end=1436
  _globals['_ECHOREQUEST']._serialized_start=1438
  _globals['_ECHOREQUEST']._serialized_end=1477
  _globals['_FLUSHREQUEST']._serialized_start=1479
  _globals['_FLUSHREQUEST']._serialized_end=1493
  _globals['_INFOREQUEST']._serialized_start=1496
  _globals['_INFOREQUEST']._serialized_end=1640
  _globals['_INITCHAINREQUEST']._serialized_start=1643
  _globals['_INITCHAINREQUEST']._serialized_end=1977
  _globals['_QUERYREQUEST']._serialized_start=1979
  _globals['_QUERYREQUEST']._serialized_end=2079
  _globals['_CHECKTXREQUEST']._serialized_start=2081
  _globals['_CHECKTXREQUEST']._serialized_end=2170
  _globals['_COMMITREQUEST']._serialized_start=2172
  _globals['_COMMITREQUEST']._serialized_end=2187
  _globals['_LISTSNAPSHOTSREQUEST']._serialized_start=2189
  _globals['_LISTSNAPSHOTSREQUEST']._serialized_end=2211
  _globals['_OFFERSNAPSHOTREQUEST']._serialized_start=2213
  _globals['_OFFERSNAPSHOTREQUEST']._serialized_end=2318
  _globals['_LOADSNAPSHOTCHUNKREQUEST']._serialized_start=2320
  _globals['_LOADSNAPSHOTCHUNKREQUEST']._serialized_end=2416
  _globals['_APPLYSNAPSHOTCHUNKREQUEST']._serialized_start=2418
  _globals['_APPLYSNAPSHOTCHUNKREQUEST']._serialized_end=2513
  _globals['_PREPAREPROPOSALREQUEST']._serialized_start=2516
  _globals['_PREPAREPROPOSALREQUEST']._serialized_end=2926
  _globals['_PROCESSPROPOSALREQUEST']._serialized_start=2929
  _globals['_PROCESSPROPOSALREQUEST']._serialized_end=3323
  _globals['_EXTENDVOTEREQUEST']._serialized_start=3326
  _globals['_EXTENDVOTEREQUEST']._serialized_end=3715
  _globals['_VERIFYVOTEEXTENSIONREQUEST']._serialized_start=3718
  _globals['_VERIFYVOTEEXTENSIONREQUEST']._serialized_end=3874
  _globals['_FINALIZEBLOCKREQUEST']._serialized_start=3877
  _globals['_FINALIZEBLOCKREQUEST']._serialized_end=4311
  _globals['_RESPONSE']._serialized_start=4314
  _globals['_RESPONSE']._serialized_end=5631
  _globals['_EXCEPTIONRESPONSE']._serialized_start=5633
  _globals['_EXCEPTIONRESPONSE']._serialized_end=5674
  _globals['_ECHORESPONSE']._serialized_start=5676
  _globals['_ECHORESPONSE']._serialized_end=5716
  _globals['_FLUSHRESPONSE']._serialized_start=5718
  _globals['_FLUSHRESPONSE']._serialized_end=5733
  _globals['_INFORESPONSE']._serialized_start=5736
  _globals['_INFORESPONSE']._serialized_end=6115
  _globals['_INFORESPONSE_LANEPRIORITIESENTRY']._serialized_start=6050
  _globals['_INFORESPONSE_LANEPRIORITIESENTRY']._serialized_end=6115
  _globals['_INITCHAINRESPONSE']._serialized_start=6118
  _globals['_INITCHAINRESPONSE']._serialized_end=6316
  _globals['_QUERYRESPONSE']._serialized_start=6319
  _globals['_QUERYRESPONSE']._serialized_end=6567
  _globals['_CHECKTXRESPONSE']._serialized_start=6570
  _globals['_CHECKTXRESPONSE']._serialized_end=6894
  _globals['_COMMITRESPONSE']._serialized_start=6896
  _globals['_COMMITRESPONSE']._serialized_end=6961
  _globals['_LISTSNAPSHOTSRESPONSE']._serialized_start=6963
  _globals['_LISTSNAPSHOTSRESPONSE']._serialized_end=7044
  _globals['_OFFERSNAPSHOTRESPONSE']._serialized_start=7046
  _globals['_OFFERSNAPSHOTRESPONSE']._serialized_end=7132
  _globals['_LOADSNAPSHOTCHUNKRESPONSE']._serialized_start=7134
  _globals['_LOADSNAPSHOTCHUNKRESPONSE']._serialized_end=7183
  _globals['_APPLYSNAPSHOTCHUNKRESPONSE']._serialized_start=7186
  _globals['_APPLYSNAPSHOTCHUNKRESPONSE']._serialized_end=7360
  _globals['_PREPAREPROPOSALRESPONSE']._serialized_start=7362
  _globals['_PREPAREPROPOSALRESPONSE']._serialized_end=7405
  _globals['_PROCESSPROPOSALRESPONSE']._serialized_start=7407
  _globals['_PROCESSPROPOSALRESPONSE']._serialized_end=7497
  _globals['_EXTENDVOTERESPONSE']._serialized_start=7499
  _globals['_EXTENDVOTERESPONSE']._serialized_end=7558
  _globals['_VERIFYVOTEEXTENSIONRESPONSE']._serialized_start=7560
  _globals['_VERIFYVOTEEXTENSIONRESPONSE']._serialized_end=7658
  _globals['_FINALIZEBLOCKRESPONSE']._serialized_start=7661
  _globals['_FINALIZEBLOCKRESPONSE']._serialized_end=8027
  _globals['_COMMITINFO']._serialized_start=8029
  _globals['_COMMITINFO']._serialized_end=8119
  _globals['_EXTENDEDCOMMITINFO']._serialized_start=8121
  _globals['_EXTENDEDCOMMITINFO']._serialized_end=8227
  _globals['_EVENT']._serialized_start=8229
  _globals['_EVENT']._serialized_end=8352
  _globals['_EVENTATTRIBUTE']._serialized_start=8354
  _globals['_EVENTATTRIBUTE']._serialized_end=8432
  _globals['_EXECTXRESULT']._serialized_start=8435
  _globals['_EXECTXRESULT']._serialized_end=8692
  _globals['_TXRESULT']._serialized_start=8695
  _globals['_TXRESULT']._serialized_end=8829
  _globals['_VALIDATOR']._serialized_start=8831
  _globals['_VALIDATOR']._serialized_end=8890
  _globals['_VALIDATORUPDATE']._serialized_start=8892
  _globals['_VALIDATORUPDATE']._serialized_end=9007
  _globals['_VOTEINFO']._serialized_start=9010
  _globals['_VOTEINFO']._serialized_end=9159
  _globals['_EXTENDEDVOTEINFO']._serialized_start=9162
  _globals['_EXTENDEDVOTEINFO']._serialized_end=9407
  _globals['_MISBEHAVIOR']._serialized_start=9410
  _globals['_MISBEHAVIOR']._serialized_end=9671
  _globals['_SNAPSHOT']._serialized_start=9674
  _globals['_SNAPSHOT']._serialized_end=9804
# @@protoc_insertion_point(module_scope)
