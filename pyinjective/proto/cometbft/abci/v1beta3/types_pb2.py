# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cometbft/abci/v1beta3/types.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.cometbft.abci.v1beta1 import types_pb2 as cometbft_dot_abci_dot_v1beta1_dot_types__pb2
from pyinjective.proto.cometbft.abci.v1beta2 import types_pb2 as cometbft_dot_abci_dot_v1beta2_dot_types__pb2
from pyinjective.proto.cometbft.types.v1 import params_pb2 as cometbft_dot_types_dot_v1_dot_params__pb2
from pyinjective.proto.cometbft.types.v1beta1 import validator_pb2 as cometbft_dot_types_dot_v1beta1_dot_validator__pb2
from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!cometbft/abci/v1beta3/types.proto\x12\x15\x63ometbft.abci.v1beta3\x1a!cometbft/abci/v1beta1/types.proto\x1a!cometbft/abci/v1beta2/types.proto\x1a\x1e\x63ometbft/types/v1/params.proto\x1a&cometbft/types/v1beta1/validator.proto\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x9f\n\n\x07Request\x12\x38\n\x04\x65\x63ho\x18\x01 \x01(\x0b\x32\".cometbft.abci.v1beta1.RequestEchoH\x00R\x04\x65\x63ho\x12;\n\x05\x66lush\x18\x02 \x01(\x0b\x32#.cometbft.abci.v1beta1.RequestFlushH\x00R\x05\x66lush\x12\x38\n\x04info\x18\x03 \x01(\x0b\x32\".cometbft.abci.v1beta2.RequestInfoH\x00R\x04info\x12H\n\ninit_chain\x18\x05 \x01(\x0b\x32\'.cometbft.abci.v1beta3.RequestInitChainH\x00R\tinitChain\x12;\n\x05query\x18\x06 \x01(\x0b\x32#.cometbft.abci.v1beta1.RequestQueryH\x00R\x05query\x12\x42\n\x08\x63heck_tx\x18\x08 \x01(\x0b\x32%.cometbft.abci.v1beta1.RequestCheckTxH\x00R\x07\x63heckTx\x12>\n\x06\x63ommit\x18\x0b \x01(\x0b\x32$.cometbft.abci.v1beta1.RequestCommitH\x00R\x06\x63ommit\x12T\n\x0elist_snapshots\x18\x0c \x01(\x0b\x32+.cometbft.abci.v1beta1.RequestListSnapshotsH\x00R\rlistSnapshots\x12T\n\x0eoffer_snapshot\x18\r \x01(\x0b\x32+.cometbft.abci.v1beta1.RequestOfferSnapshotH\x00R\rofferSnapshot\x12\x61\n\x13load_snapshot_chunk\x18\x0e \x01(\x0b\x32/.cometbft.abci.v1beta1.RequestLoadSnapshotChunkH\x00R\x11loadSnapshotChunk\x12\x64\n\x14\x61pply_snapshot_chunk\x18\x0f \x01(\x0b\x32\x30.cometbft.abci.v1beta1.RequestApplySnapshotChunkH\x00R\x12\x61pplySnapshotChunk\x12Z\n\x10prepare_proposal\x18\x10 \x01(\x0b\x32-.cometbft.abci.v1beta3.RequestPrepareProposalH\x00R\x0fprepareProposal\x12Z\n\x10process_proposal\x18\x11 \x01(\x0b\x32-.cometbft.abci.v1beta3.RequestProcessProposalH\x00R\x0fprocessProposal\x12K\n\x0b\x65xtend_vote\x18\x12 \x01(\x0b\x32(.cometbft.abci.v1beta3.RequestExtendVoteH\x00R\nextendVote\x12g\n\x15verify_vote_extension\x18\x13 \x01(\x0b\x32\x31.cometbft.abci.v1beta3.RequestVerifyVoteExtensionH\x00R\x13verifyVoteExtension\x12T\n\x0e\x66inalize_block\x18\x14 \x01(\x0b\x32+.cometbft.abci.v1beta3.RequestFinalizeBlockH\x00R\rfinalizeBlockB\x07\n\x05valueJ\x04\x08\x04\x10\x05J\x04\x08\x07\x10\x08J\x04\x08\t\x10\nJ\x04\x08\n\x10\x0b\"\xd3\x02\n\x10RequestInitChain\x12\x38\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01R\x04time\x12\x19\n\x08\x63hain_id\x18\x02 \x01(\tR\x07\x63hainId\x12M\n\x10\x63onsensus_params\x18\x03 \x01(\x0b\x32\".cometbft.types.v1.ConsensusParamsR\x0f\x63onsensusParams\x12L\n\nvalidators\x18\x04 \x03(\x0b\x32&.cometbft.abci.v1beta1.ValidatorUpdateB\x04\xc8\xde\x1f\x00R\nvalidators\x12&\n\x0f\x61pp_state_bytes\x18\x05 \x01(\x0cR\rappStateBytes\x12%\n\x0einitial_height\x18\x06 \x01(\x03R\rinitialHeight\"\xa4\x03\n\x16RequestPrepareProposal\x12 \n\x0cmax_tx_bytes\x18\x01 \x01(\x03R\nmaxTxBytes\x12\x10\n\x03txs\x18\x02 \x03(\x0cR\x03txs\x12[\n\x11local_last_commit\x18\x03 \x01(\x0b\x32).cometbft.abci.v1beta3.ExtendedCommitInfoB\x04\xc8\xde\x1f\x00R\x0flocalLastCommit\x12J\n\x0bmisbehavior\x18\x04 \x03(\x0b\x32\".cometbft.abci.v1beta2.MisbehaviorB\x04\xc8\xde\x1f\x00R\x0bmisbehavior\x12\x16\n\x06height\x18\x05 \x01(\x03R\x06height\x12\x38\n\x04time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01R\x04time\x12\x30\n\x14next_validators_hash\x18\x07 \x01(\x0cR\x12nextValidatorsHash\x12)\n\x10proposer_address\x18\x08 \x01(\x0cR\x0fproposerAddress\"\x94\x03\n\x16RequestProcessProposal\x12\x10\n\x03txs\x18\x01 \x03(\x0cR\x03txs\x12Y\n\x14proposed_last_commit\x18\x02 \x01(\x0b\x32!.cometbft.abci.v1beta3.CommitInfoB\x04\xc8\xde\x1f\x00R\x12proposedLastCommit\x12J\n\x0bmisbehavior\x18\x03 \x03(\x0b\x32\".cometbft.abci.v1beta2.MisbehaviorB\x04\xc8\xde\x1f\x00R\x0bmisbehavior\x12\x12\n\x04hash\x18\x04 \x01(\x0cR\x04hash\x12\x16\n\x06height\x18\x05 \x01(\x03R\x06height\x12\x38\n\x04time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01R\x04time\x12\x30\n\x14next_validators_hash\x18\x07 \x01(\x0cR\x12nextValidatorsHash\x12)\n\x10proposer_address\x18\x08 \x01(\x0cR\x0fproposerAddress\"\x8f\x03\n\x11RequestExtendVote\x12\x12\n\x04hash\x18\x01 \x01(\x0cR\x04hash\x12\x16\n\x06height\x18\x02 \x01(\x03R\x06height\x12\x38\n\x04time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01R\x04time\x12\x10\n\x03txs\x18\x04 \x03(\x0cR\x03txs\x12Y\n\x14proposed_last_commit\x18\x05 \x01(\x0b\x32!.cometbft.abci.v1beta3.CommitInfoB\x04\xc8\xde\x1f\x00R\x12proposedLastCommit\x12J\n\x0bmisbehavior\x18\x06 \x03(\x0b\x32\".cometbft.abci.v1beta2.MisbehaviorB\x04\xc8\xde\x1f\x00R\x0bmisbehavior\x12\x30\n\x14next_validators_hash\x18\x07 \x01(\x0cR\x12nextValidatorsHash\x12)\n\x10proposer_address\x18\x08 \x01(\x0cR\x0fproposerAddress\"\x9c\x01\n\x1aRequestVerifyVoteExtension\x12\x12\n\x04hash\x18\x01 \x01(\x0cR\x04hash\x12+\n\x11validator_address\x18\x02 \x01(\x0cR\x10validatorAddress\x12\x16\n\x06height\x18\x03 \x01(\x03R\x06height\x12%\n\x0evote_extension\x18\x04 \x01(\x0cR\rvoteExtension\"\x90\x03\n\x14RequestFinalizeBlock\x12\x10\n\x03txs\x18\x01 \x03(\x0cR\x03txs\x12W\n\x13\x64\x65\x63ided_last_commit\x18\x02 \x01(\x0b\x32!.cometbft.abci.v1beta3.CommitInfoB\x04\xc8\xde\x1f\x00R\x11\x64\x65\x63idedLastCommit\x12J\n\x0bmisbehavior\x18\x03 \x03(\x0b\x32\".cometbft.abci.v1beta2.MisbehaviorB\x04\xc8\xde\x1f\x00R\x0bmisbehavior\x12\x12\n\x04hash\x18\x04 \x01(\x0cR\x04hash\x12\x16\n\x06height\x18\x05 \x01(\x03R\x06height\x12\x38\n\x04time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01R\x04time\x12\x30\n\x14next_validators_hash\x18\x07 \x01(\x0cR\x12nextValidatorsHash\x12)\n\x10proposer_address\x18\x08 \x01(\x0cR\x0fproposerAddress\"\xfa\n\n\x08Response\x12H\n\texception\x18\x01 \x01(\x0b\x32(.cometbft.abci.v1beta1.ResponseExceptionH\x00R\texception\x12\x39\n\x04\x65\x63ho\x18\x02 \x01(\x0b\x32#.cometbft.abci.v1beta1.ResponseEchoH\x00R\x04\x65\x63ho\x12<\n\x05\x66lush\x18\x03 \x01(\x0b\x32$.cometbft.abci.v1beta1.ResponseFlushH\x00R\x05\x66lush\x12\x39\n\x04info\x18\x04 \x01(\x0b\x32#.cometbft.abci.v1beta1.ResponseInfoH\x00R\x04info\x12I\n\ninit_chain\x18\x06 \x01(\x0b\x32(.cometbft.abci.v1beta3.ResponseInitChainH\x00R\tinitChain\x12<\n\x05query\x18\x07 \x01(\x0b\x32$.cometbft.abci.v1beta1.ResponseQueryH\x00R\x05query\x12\x43\n\x08\x63heck_tx\x18\t \x01(\x0b\x32&.cometbft.abci.v1beta3.ResponseCheckTxH\x00R\x07\x63heckTx\x12?\n\x06\x63ommit\x18\x0c \x01(\x0b\x32%.cometbft.abci.v1beta3.ResponseCommitH\x00R\x06\x63ommit\x12U\n\x0elist_snapshots\x18\r \x01(\x0b\x32,.cometbft.abci.v1beta1.ResponseListSnapshotsH\x00R\rlistSnapshots\x12U\n\x0eoffer_snapshot\x18\x0e \x01(\x0b\x32,.cometbft.abci.v1beta1.ResponseOfferSnapshotH\x00R\rofferSnapshot\x12\x62\n\x13load_snapshot_chunk\x18\x0f \x01(\x0b\x32\x30.cometbft.abci.v1beta1.ResponseLoadSnapshotChunkH\x00R\x11loadSnapshotChunk\x12\x65\n\x14\x61pply_snapshot_chunk\x18\x10 \x01(\x0b\x32\x31.cometbft.abci.v1beta1.ResponseApplySnapshotChunkH\x00R\x12\x61pplySnapshotChunk\x12[\n\x10prepare_proposal\x18\x11 \x01(\x0b\x32..cometbft.abci.v1beta2.ResponsePrepareProposalH\x00R\x0fprepareProposal\x12[\n\x10process_proposal\x18\x12 \x01(\x0b\x32..cometbft.abci.v1beta2.ResponseProcessProposalH\x00R\x0fprocessProposal\x12L\n\x0b\x65xtend_vote\x18\x13 \x01(\x0b\x32).cometbft.abci.v1beta3.ResponseExtendVoteH\x00R\nextendVote\x12h\n\x15verify_vote_extension\x18\x14 \x01(\x0b\x32\x32.cometbft.abci.v1beta3.ResponseVerifyVoteExtensionH\x00R\x13verifyVoteExtension\x12U\n\x0e\x66inalize_block\x18\x15 \x01(\x0b\x32,.cometbft.abci.v1beta3.ResponseFinalizeBlockH\x00R\rfinalizeBlockB\x07\n\x05valueJ\x04\x08\x05\x10\x06J\x04\x08\x08\x10\tJ\x04\x08\n\x10\x0bJ\x04\x08\x0b\x10\x0c\"\xcb\x01\n\x11ResponseInitChain\x12M\n\x10\x63onsensus_params\x18\x01 \x01(\x0b\x32\".cometbft.types.v1.ConsensusParamsR\x0f\x63onsensusParams\x12L\n\nvalidators\x18\x02 \x03(\x0b\x32&.cometbft.abci.v1beta1.ValidatorUpdateB\x04\xc8\xde\x1f\x00R\nvalidators\x12\x19\n\x08\x61pp_hash\x18\x03 \x01(\x0cR\x07\x61ppHash\"\xb0\x02\n\x0fResponseCheckTx\x12\x12\n\x04\x63ode\x18\x01 \x01(\rR\x04\x63ode\x12\x12\n\x04\x64\x61ta\x18\x02 \x01(\x0cR\x04\x64\x61ta\x12\x10\n\x03log\x18\x03 \x01(\tR\x03log\x12\x12\n\x04info\x18\x04 \x01(\tR\x04info\x12\x1e\n\ngas_wanted\x18\x05 \x01(\x03R\ngas_wanted\x12\x1a\n\x08gas_used\x18\x06 \x01(\x03R\x08gas_used\x12N\n\x06\x65vents\x18\x07 \x03(\x0b\x32\x1c.cometbft.abci.v1beta2.EventB\x18\xc8\xde\x1f\x00\xea\xde\x1f\x10\x65vents,omitemptyR\x06\x65vents\x12\x1c\n\tcodespace\x18\x08 \x01(\tR\tcodespaceJ\x04\x08\t\x10\x0cR\x06senderR\x08priorityR\rmempool_error\"A\n\x0eResponseCommit\x12#\n\rretain_height\x18\x03 \x01(\x03R\x0cretainHeightJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03\";\n\x12ResponseExtendVote\x12%\n\x0evote_extension\x18\x01 \x01(\x0cR\rvoteExtension\"\xab\x01\n\x1bResponseVerifyVoteExtension\x12W\n\x06status\x18\x01 \x01(\x0e\x32?.cometbft.abci.v1beta3.ResponseVerifyVoteExtension.VerifyStatusR\x06status\"3\n\x0cVerifyStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06\x41\x43\x43\x45PT\x10\x01\x12\n\n\x06REJECT\x10\x02\"\xfd\x02\n\x15ResponseFinalizeBlock\x12N\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x1c.cometbft.abci.v1beta2.EventB\x18\xc8\xde\x1f\x00\xea\xde\x1f\x10\x65vents,omitemptyR\x06\x65vents\x12\x42\n\ntx_results\x18\x02 \x03(\x0b\x32#.cometbft.abci.v1beta3.ExecTxResultR\ttxResults\x12Y\n\x11validator_updates\x18\x03 \x03(\x0b\x32&.cometbft.abci.v1beta1.ValidatorUpdateB\x04\xc8\xde\x1f\x00R\x10validatorUpdates\x12Z\n\x17\x63onsensus_param_updates\x18\x04 \x01(\x0b\x32\".cometbft.types.v1.ConsensusParamsR\x15\x63onsensusParamUpdates\x12\x19\n\x08\x61pp_hash\x18\x05 \x01(\x0cR\x07\x61ppHash\"\x9f\x01\n\x08VoteInfo\x12\x44\n\tvalidator\x18\x01 \x01(\x0b\x32 .cometbft.abci.v1beta1.ValidatorB\x04\xc8\xde\x1f\x00R\tvalidator\x12G\n\rblock_id_flag\x18\x03 \x01(\x0e\x32#.cometbft.types.v1beta1.BlockIDFlagR\x0b\x62lockIdFlagJ\x04\x08\x02\x10\x03\"\xff\x01\n\x10\x45xtendedVoteInfo\x12\x44\n\tvalidator\x18\x01 \x01(\x0b\x32 .cometbft.abci.v1beta1.ValidatorB\x04\xc8\xde\x1f\x00R\tvalidator\x12%\n\x0evote_extension\x18\x03 \x01(\x0cR\rvoteExtension\x12/\n\x13\x65xtension_signature\x18\x04 \x01(\x0cR\x12\x65xtensionSignature\x12G\n\rblock_id_flag\x18\x05 \x01(\x0e\x32#.cometbft.types.v1beta1.BlockIDFlagR\x0b\x62lockIdFlagJ\x04\x08\x02\x10\x03\"_\n\nCommitInfo\x12\x14\n\x05round\x18\x01 \x01(\x05R\x05round\x12;\n\x05votes\x18\x02 \x03(\x0b\x32\x1f.cometbft.abci.v1beta3.VoteInfoB\x04\xc8\xde\x1f\x00R\x05votes\"o\n\x12\x45xtendedCommitInfo\x12\x14\n\x05round\x18\x01 \x01(\x05R\x05round\x12\x43\n\x05votes\x18\x02 \x03(\x0b\x32\'.cometbft.abci.v1beta3.ExtendedVoteInfoB\x04\xc8\xde\x1f\x00R\x05votes\"\x86\x02\n\x0c\x45xecTxResult\x12\x12\n\x04\x63ode\x18\x01 \x01(\rR\x04\x63ode\x12\x12\n\x04\x64\x61ta\x18\x02 \x01(\x0cR\x04\x64\x61ta\x12\x10\n\x03log\x18\x03 \x01(\tR\x03log\x12\x12\n\x04info\x18\x04 \x01(\tR\x04info\x12\x1e\n\ngas_wanted\x18\x05 \x01(\x03R\ngas_wanted\x12\x1a\n\x08gas_used\x18\x06 \x01(\x03R\x08gas_used\x12N\n\x06\x65vents\x18\x07 \x03(\x0b\x32\x1c.cometbft.abci.v1beta2.EventB\x18\xc8\xde\x1f\x00\xea\xde\x1f\x10\x65vents,omitemptyR\x06\x65vents\x12\x1c\n\tcodespace\x18\x08 \x01(\tR\tcodespace\"\x8b\x01\n\x08TxResult\x12\x16\n\x06height\x18\x01 \x01(\x03R\x06height\x12\x14\n\x05index\x18\x02 \x01(\rR\x05index\x12\x0e\n\x02tx\x18\x03 \x01(\x0cR\x02tx\x12\x41\n\x06result\x18\x04 \x01(\x0b\x32#.cometbft.abci.v1beta3.ExecTxResultB\x04\xc8\xde\x1f\x00R\x06result2\xdd\x0c\n\x04\x41\x42\x43I\x12O\n\x04\x45\x63ho\x12\".cometbft.abci.v1beta1.RequestEcho\x1a#.cometbft.abci.v1beta1.ResponseEcho\x12R\n\x05\x46lush\x12#.cometbft.abci.v1beta1.RequestFlush\x1a$.cometbft.abci.v1beta1.ResponseFlush\x12O\n\x04Info\x12\".cometbft.abci.v1beta2.RequestInfo\x1a#.cometbft.abci.v1beta1.ResponseInfo\x12X\n\x07\x43heckTx\x12%.cometbft.abci.v1beta1.RequestCheckTx\x1a&.cometbft.abci.v1beta3.ResponseCheckTx\x12R\n\x05Query\x12#.cometbft.abci.v1beta1.RequestQuery\x1a$.cometbft.abci.v1beta1.ResponseQuery\x12U\n\x06\x43ommit\x12$.cometbft.abci.v1beta1.RequestCommit\x1a%.cometbft.abci.v1beta3.ResponseCommit\x12^\n\tInitChain\x12\'.cometbft.abci.v1beta3.RequestInitChain\x1a(.cometbft.abci.v1beta3.ResponseInitChain\x12j\n\rListSnapshots\x12+.cometbft.abci.v1beta1.RequestListSnapshots\x1a,.cometbft.abci.v1beta1.ResponseListSnapshots\x12j\n\rOfferSnapshot\x12+.cometbft.abci.v1beta1.RequestOfferSnapshot\x1a,.cometbft.abci.v1beta1.ResponseOfferSnapshot\x12v\n\x11LoadSnapshotChunk\x12/.cometbft.abci.v1beta1.RequestLoadSnapshotChunk\x1a\x30.cometbft.abci.v1beta1.ResponseLoadSnapshotChunk\x12y\n\x12\x41pplySnapshotChunk\x12\x30.cometbft.abci.v1beta1.RequestApplySnapshotChunk\x1a\x31.cometbft.abci.v1beta1.ResponseApplySnapshotChunk\x12p\n\x0fPrepareProposal\x12-.cometbft.abci.v1beta3.RequestPrepareProposal\x1a..cometbft.abci.v1beta2.ResponsePrepareProposal\x12p\n\x0fProcessProposal\x12-.cometbft.abci.v1beta3.RequestProcessProposal\x1a..cometbft.abci.v1beta2.ResponseProcessProposal\x12\x61\n\nExtendVote\x12(.cometbft.abci.v1beta3.RequestExtendVote\x1a).cometbft.abci.v1beta3.ResponseExtendVote\x12|\n\x13VerifyVoteExtension\x12\x31.cometbft.abci.v1beta3.RequestVerifyVoteExtension\x1a\x32.cometbft.abci.v1beta3.ResponseVerifyVoteExtension\x12j\n\rFinalizeBlock\x12+.cometbft.abci.v1beta3.RequestFinalizeBlock\x1a,.cometbft.abci.v1beta3.ResponseFinalizeBlockB\xd5\x01\n\x19\x63om.cometbft.abci.v1beta3B\nTypesProtoP\x01Z6github.com/cometbft/cometbft/api/cometbft/abci/v1beta3\xa2\x02\x03\x43\x41X\xaa\x02\x15\x43ometbft.Abci.V1beta3\xca\x02\x15\x43ometbft\\Abci\\V1beta3\xe2\x02!Cometbft\\Abci\\V1beta3\\GPBMetadata\xea\x02\x17\x43ometbft::Abci::V1beta3b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cometbft.abci.v1beta3.types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.cometbft.abci.v1beta3B\nTypesProtoP\001Z6github.com/cometbft/cometbft/api/cometbft/abci/v1beta3\242\002\003CAX\252\002\025Cometbft.Abci.V1beta3\312\002\025Cometbft\\Abci\\V1beta3\342\002!Cometbft\\Abci\\V1beta3\\GPBMetadata\352\002\027Cometbft::Abci::V1beta3'
  _globals['_REQUESTINITCHAIN'].fields_by_name['time']._loaded_options = None
  _globals['_REQUESTINITCHAIN'].fields_by_name['time']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_REQUESTINITCHAIN'].fields_by_name['validators']._loaded_options = None
  _globals['_REQUESTINITCHAIN'].fields_by_name['validators']._serialized_options = b'\310\336\037\000'
  _globals['_REQUESTPREPAREPROPOSAL'].fields_by_name['local_last_commit']._loaded_options = None
  _globals['_REQUESTPREPAREPROPOSAL'].fields_by_name['local_last_commit']._serialized_options = b'\310\336\037\000'
  _globals['_REQUESTPREPAREPROPOSAL'].fields_by_name['misbehavior']._loaded_options = None
  _globals['_REQUESTPREPAREPROPOSAL'].fields_by_name['misbehavior']._serialized_options = b'\310\336\037\000'
  _globals['_REQUESTPREPAREPROPOSAL'].fields_by_name['time']._loaded_options = None
  _globals['_REQUESTPREPAREPROPOSAL'].fields_by_name['time']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_REQUESTPROCESSPROPOSAL'].fields_by_name['proposed_last_commit']._loaded_options = None
  _globals['_REQUESTPROCESSPROPOSAL'].fields_by_name['proposed_last_commit']._serialized_options = b'\310\336\037\000'
  _globals['_REQUESTPROCESSPROPOSAL'].fields_by_name['misbehavior']._loaded_options = None
  _globals['_REQUESTPROCESSPROPOSAL'].fields_by_name['misbehavior']._serialized_options = b'\310\336\037\000'
  _globals['_REQUESTPROCESSPROPOSAL'].fields_by_name['time']._loaded_options = None
  _globals['_REQUESTPROCESSPROPOSAL'].fields_by_name['time']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_REQUESTEXTENDVOTE'].fields_by_name['time']._loaded_options = None
  _globals['_REQUESTEXTENDVOTE'].fields_by_name['time']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_REQUESTEXTENDVOTE'].fields_by_name['proposed_last_commit']._loaded_options = None
  _globals['_REQUESTEXTENDVOTE'].fields_by_name['proposed_last_commit']._serialized_options = b'\310\336\037\000'
  _globals['_REQUESTEXTENDVOTE'].fields_by_name['misbehavior']._loaded_options = None
  _globals['_REQUESTEXTENDVOTE'].fields_by_name['misbehavior']._serialized_options = b'\310\336\037\000'
  _globals['_REQUESTFINALIZEBLOCK'].fields_by_name['decided_last_commit']._loaded_options = None
  _globals['_REQUESTFINALIZEBLOCK'].fields_by_name['decided_last_commit']._serialized_options = b'\310\336\037\000'
  _globals['_REQUESTFINALIZEBLOCK'].fields_by_name['misbehavior']._loaded_options = None
  _globals['_REQUESTFINALIZEBLOCK'].fields_by_name['misbehavior']._serialized_options = b'\310\336\037\000'
  _globals['_REQUESTFINALIZEBLOCK'].fields_by_name['time']._loaded_options = None
  _globals['_REQUESTFINALIZEBLOCK'].fields_by_name['time']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_RESPONSEINITCHAIN'].fields_by_name['validators']._loaded_options = None
  _globals['_RESPONSEINITCHAIN'].fields_by_name['validators']._serialized_options = b'\310\336\037\000'
  _globals['_RESPONSECHECKTX'].fields_by_name['events']._loaded_options = None
  _globals['_RESPONSECHECKTX'].fields_by_name['events']._serialized_options = b'\310\336\037\000\352\336\037\020events,omitempty'
  _globals['_RESPONSEFINALIZEBLOCK'].fields_by_name['events']._loaded_options = None
  _globals['_RESPONSEFINALIZEBLOCK'].fields_by_name['events']._serialized_options = b'\310\336\037\000\352\336\037\020events,omitempty'
  _globals['_RESPONSEFINALIZEBLOCK'].fields_by_name['validator_updates']._loaded_options = None
  _globals['_RESPONSEFINALIZEBLOCK'].fields_by_name['validator_updates']._serialized_options = b'\310\336\037\000'
  _globals['_VOTEINFO'].fields_by_name['validator']._loaded_options = None
  _globals['_VOTEINFO'].fields_by_name['validator']._serialized_options = b'\310\336\037\000'
  _globals['_EXTENDEDVOTEINFO'].fields_by_name['validator']._loaded_options = None
  _globals['_EXTENDEDVOTEINFO'].fields_by_name['validator']._serialized_options = b'\310\336\037\000'
  _globals['_COMMITINFO'].fields_by_name['votes']._loaded_options = None
  _globals['_COMMITINFO'].fields_by_name['votes']._serialized_options = b'\310\336\037\000'
  _globals['_EXTENDEDCOMMITINFO'].fields_by_name['votes']._loaded_options = None
  _globals['_EXTENDEDCOMMITINFO'].fields_by_name['votes']._serialized_options = b'\310\336\037\000'
  _globals['_EXECTXRESULT'].fields_by_name['events']._loaded_options = None
  _globals['_EXECTXRESULT'].fields_by_name['events']._serialized_options = b'\310\336\037\000\352\336\037\020events,omitempty'
  _globals['_TXRESULT'].fields_by_name['result']._loaded_options = None
  _globals['_TXRESULT'].fields_by_name['result']._serialized_options = b'\310\336\037\000'
  _globals['_REQUEST']._serialized_start=258
  _globals['_REQUEST']._serialized_end=1569
  _globals['_REQUESTINITCHAIN']._serialized_start=1572
  _globals['_REQUESTINITCHAIN']._serialized_end=1911
  _globals['_REQUESTPREPAREPROPOSAL']._serialized_start=1914
  _globals['_REQUESTPREPAREPROPOSAL']._serialized_end=2334
  _globals['_REQUESTPROCESSPROPOSAL']._serialized_start=2337
  _globals['_REQUESTPROCESSPROPOSAL']._serialized_end=2741
  _globals['_REQUESTEXTENDVOTE']._serialized_start=2744
  _globals['_REQUESTEXTENDVOTE']._serialized_end=3143
  _globals['_REQUESTVERIFYVOTEEXTENSION']._serialized_start=3146
  _globals['_REQUESTVERIFYVOTEEXTENSION']._serialized_end=3302
  _globals['_REQUESTFINALIZEBLOCK']._serialized_start=3305
  _globals['_REQUESTFINALIZEBLOCK']._serialized_end=3705
  _globals['_RESPONSE']._serialized_start=3708
  _globals['_RESPONSE']._serialized_end=5110
  _globals['_RESPONSEINITCHAIN']._serialized_start=5113
  _globals['_RESPONSEINITCHAIN']._serialized_end=5316
  _globals['_RESPONSECHECKTX']._serialized_start=5319
  _globals['_RESPONSECHECKTX']._serialized_end=5623
  _globals['_RESPONSECOMMIT']._serialized_start=5625
  _globals['_RESPONSECOMMIT']._serialized_end=5690
  _globals['_RESPONSEEXTENDVOTE']._serialized_start=5692
  _globals['_RESPONSEEXTENDVOTE']._serialized_end=5751
  _globals['_RESPONSEVERIFYVOTEEXTENSION']._serialized_start=5754
  _globals['_RESPONSEVERIFYVOTEEXTENSION']._serialized_end=5925
  _globals['_RESPONSEVERIFYVOTEEXTENSION_VERIFYSTATUS']._serialized_start=5874
  _globals['_RESPONSEVERIFYVOTEEXTENSION_VERIFYSTATUS']._serialized_end=5925
  _globals['_RESPONSEFINALIZEBLOCK']._serialized_start=5928
  _globals['_RESPONSEFINALIZEBLOCK']._serialized_end=6309
  _globals['_VOTEINFO']._serialized_start=6312
  _globals['_VOTEINFO']._serialized_end=6471
  _globals['_EXTENDEDVOTEINFO']._serialized_start=6474
  _globals['_EXTENDEDVOTEINFO']._serialized_end=6729
  _globals['_COMMITINFO']._serialized_start=6731
  _globals['_COMMITINFO']._serialized_end=6826
  _globals['_EXTENDEDCOMMITINFO']._serialized_start=6828
  _globals['_EXTENDEDCOMMITINFO']._serialized_end=6939
  _globals['_EXECTXRESULT']._serialized_start=6942
  _globals['_EXECTXRESULT']._serialized_end=7204
  _globals['_TXRESULT']._serialized_start=7207
  _globals['_TXRESULT']._serialized_end=7346
  _globals['_ABCI']._serialized_start=7349
  _globals['_ABCI']._serialized_end=8978
# @@protoc_insertion_point(module_scope)
