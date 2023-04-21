# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/peggy/v1/msgs.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from injective.peggy.v1 import types_pb2 as injective_dot_peggy_dot_v1_dot_types__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dinjective/peggy/v1/msgs.proto\x12\x12injective.peggy.v1\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1einjective/peggy/v1/types.proto\x1a\x19google/protobuf/any.proto\"X\n\x1bMsgSetOrchestratorAddresses\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x14\n\x0corchestrator\x18\x02 \x01(\t\x12\x13\n\x0b\x65th_address\x18\x03 \x01(\t\"%\n#MsgSetOrchestratorAddressesResponse\"_\n\x10MsgValsetConfirm\x12\r\n\x05nonce\x18\x01 \x01(\x04\x12\x14\n\x0corchestrator\x18\x02 \x01(\t\x12\x13\n\x0b\x65th_address\x18\x03 \x01(\t\x12\x11\n\tsignature\x18\x04 \x01(\t\"\x1a\n\x18MsgValsetConfirmResponse\"\x96\x01\n\x0cMsgSendToEth\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x10\n\x08\x65th_dest\x18\x02 \x01(\t\x12/\n\x06\x61mount\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x33\n\nbridge_fee\x18\x04 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"\x16\n\x14MsgSendToEthResponse\"6\n\x0fMsgRequestBatch\x12\x14\n\x0corchestrator\x18\x01 \x01(\t\x12\r\n\x05\x64\x65nom\x18\x02 \x01(\t\"\x19\n\x17MsgRequestBatchResponse\"u\n\x0fMsgConfirmBatch\x12\r\n\x05nonce\x18\x01 \x01(\x04\x12\x16\n\x0etoken_contract\x18\x02 \x01(\t\x12\x12\n\neth_signer\x18\x03 \x01(\t\x12\x14\n\x0corchestrator\x18\x04 \x01(\t\x12\x11\n\tsignature\x18\x05 \x01(\t\"\x19\n\x17MsgConfirmBatchResponse\"\xea\x01\n\x0fMsgDepositClaim\x12\x13\n\x0b\x65vent_nonce\x18\x01 \x01(\x04\x12\x14\n\x0c\x62lock_height\x18\x02 \x01(\x04\x12\x16\n\x0etoken_contract\x18\x03 \x01(\t\x12>\n\x06\x61mount\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12\x17\n\x0f\x65thereum_sender\x18\x05 \x01(\t\x12\x17\n\x0f\x63osmos_receiver\x18\x06 \x01(\t\x12\x14\n\x0corchestrator\x18\x07 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x08 \x01(\t\"\x19\n\x17MsgDepositClaimResponse\"\x80\x01\n\x10MsgWithdrawClaim\x12\x13\n\x0b\x65vent_nonce\x18\x01 \x01(\x04\x12\x14\n\x0c\x62lock_height\x18\x02 \x01(\x04\x12\x13\n\x0b\x62\x61tch_nonce\x18\x03 \x01(\x04\x12\x16\n\x0etoken_contract\x18\x04 \x01(\t\x12\x14\n\x0corchestrator\x18\x05 \x01(\t\"\x1a\n\x18MsgWithdrawClaimResponse\"\xb6\x01\n\x15MsgERC20DeployedClaim\x12\x13\n\x0b\x65vent_nonce\x18\x01 \x01(\x04\x12\x14\n\x0c\x62lock_height\x18\x02 \x01(\x04\x12\x14\n\x0c\x63osmos_denom\x18\x03 \x01(\t\x12\x16\n\x0etoken_contract\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x0e\n\x06symbol\x18\x06 \x01(\t\x12\x10\n\x08\x64\x65\x63imals\x18\x07 \x01(\x04\x12\x14\n\x0corchestrator\x18\x08 \x01(\t\"\x1f\n\x1dMsgERC20DeployedClaimResponse\"<\n\x12MsgCancelSendToEth\x12\x16\n\x0etransaction_id\x18\x01 \x01(\x04\x12\x0e\n\x06sender\x18\x02 \x01(\t\"\x1c\n\x1aMsgCancelSendToEthResponse\"i\n\x1dMsgSubmitBadSignatureEvidence\x12%\n\x07subject\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x11\n\tsignature\x18\x02 \x01(\t\x12\x0e\n\x06sender\x18\x03 \x01(\t\"\'\n%MsgSubmitBadSignatureEvidenceResponse\"\x81\x02\n\x15MsgValsetUpdatedClaim\x12\x13\n\x0b\x65vent_nonce\x18\x01 \x01(\x04\x12\x14\n\x0cvalset_nonce\x18\x02 \x01(\x04\x12\x14\n\x0c\x62lock_height\x18\x03 \x01(\x04\x12\x34\n\x07members\x18\x04 \x03(\x0b\x32#.injective.peggy.v1.BridgeValidator\x12\x45\n\rreward_amount\x18\x05 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12\x14\n\x0creward_token\x18\x06 \x01(\t\x12\x14\n\x0corchestrator\x18\x07 \x01(\t\"\x1f\n\x1dMsgValsetUpdatedClaimResponse2\xc4\r\n\x03Msg\x12\x8f\x01\n\rValsetConfirm\x12$.injective.peggy.v1.MsgValsetConfirm\x1a,.injective.peggy.v1.MsgValsetConfirmResponse\"*\x82\xd3\xe4\x93\x02$\"\"/injective/peggy/v1/valset_confirm\x12\x80\x01\n\tSendToEth\x12 .injective.peggy.v1.MsgSendToEth\x1a(.injective.peggy.v1.MsgSendToEthResponse\"\'\x82\xd3\xe4\x93\x02!\"\x1f/injective/peggy/v1/send_to_eth\x12\x8b\x01\n\x0cRequestBatch\x12#.injective.peggy.v1.MsgRequestBatch\x1a+.injective.peggy.v1.MsgRequestBatchResponse\")\x82\xd3\xe4\x93\x02#\"!/injective/peggy/v1/request_batch\x12\x8b\x01\n\x0c\x43onfirmBatch\x12#.injective.peggy.v1.MsgConfirmBatch\x1a+.injective.peggy.v1.MsgConfirmBatchResponse\")\x82\xd3\xe4\x93\x02#\"!/injective/peggy/v1/confirm_batch\x12\x8b\x01\n\x0c\x44\x65positClaim\x12#.injective.peggy.v1.MsgDepositClaim\x1a+.injective.peggy.v1.MsgDepositClaimResponse\")\x82\xd3\xe4\x93\x02#\"!/injective/peggy/v1/deposit_claim\x12\x8f\x01\n\rWithdrawClaim\x12$.injective.peggy.v1.MsgWithdrawClaim\x1a,.injective.peggy.v1.MsgWithdrawClaimResponse\"*\x82\xd3\xe4\x93\x02$\"\"/injective/peggy/v1/withdraw_claim\x12\xa3\x01\n\x11ValsetUpdateClaim\x12).injective.peggy.v1.MsgValsetUpdatedClaim\x1a\x31.injective.peggy.v1.MsgValsetUpdatedClaimResponse\"0\x82\xd3\xe4\x93\x02*\"(/injective/peggy/v1/valset_updated_claim\x12\xa4\x01\n\x12\x45RC20DeployedClaim\x12).injective.peggy.v1.MsgERC20DeployedClaim\x1a\x31.injective.peggy.v1.MsgERC20DeployedClaimResponse\"0\x82\xd3\xe4\x93\x02*\"(/injective/peggy/v1/erc20_deployed_claim\x12\xba\x01\n\x18SetOrchestratorAddresses\x12/.injective.peggy.v1.MsgSetOrchestratorAddresses\x1a\x37.injective.peggy.v1.MsgSetOrchestratorAddressesResponse\"4\x82\xd3\xe4\x93\x02.\",/injective/peggy/v1/set_orchestrator_address\x12\x99\x01\n\x0f\x43\x61ncelSendToEth\x12&.injective.peggy.v1.MsgCancelSendToEth\x1a..injective.peggy.v1.MsgCancelSendToEthResponse\".\x82\xd3\xe4\x93\x02(\"&/injective/peggy/v1/cancel_send_to_eth\x12\xc5\x01\n\x1aSubmitBadSignatureEvidence\x12\x31.injective.peggy.v1.MsgSubmitBadSignatureEvidence\x1a\x39.injective.peggy.v1.MsgSubmitBadSignatureEvidenceResponse\"9\x82\xd3\xe4\x93\x02\x33\"1/injective/peggy/v1/submit_bad_signature_evidenceBMZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.peggy.v1.msgs_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/types'
  _MSGSENDTOETH.fields_by_name['amount']._options = None
  _MSGSENDTOETH.fields_by_name['amount']._serialized_options = b'\310\336\037\000'
  _MSGSENDTOETH.fields_by_name['bridge_fee']._options = None
  _MSGSENDTOETH.fields_by_name['bridge_fee']._serialized_options = b'\310\336\037\000'
  _MSGDEPOSITCLAIM.fields_by_name['amount']._options = None
  _MSGDEPOSITCLAIM.fields_by_name['amount']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _MSGVALSETUPDATEDCLAIM.fields_by_name['reward_amount']._options = None
  _MSGVALSETUPDATEDCLAIM.fields_by_name['reward_amount']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _MSG.methods_by_name['ValsetConfirm']._options = None
  _MSG.methods_by_name['ValsetConfirm']._serialized_options = b'\202\323\344\223\002$\"\"/injective/peggy/v1/valset_confirm'
  _MSG.methods_by_name['SendToEth']._options = None
  _MSG.methods_by_name['SendToEth']._serialized_options = b'\202\323\344\223\002!\"\037/injective/peggy/v1/send_to_eth'
  _MSG.methods_by_name['RequestBatch']._options = None
  _MSG.methods_by_name['RequestBatch']._serialized_options = b'\202\323\344\223\002#\"!/injective/peggy/v1/request_batch'
  _MSG.methods_by_name['ConfirmBatch']._options = None
  _MSG.methods_by_name['ConfirmBatch']._serialized_options = b'\202\323\344\223\002#\"!/injective/peggy/v1/confirm_batch'
  _MSG.methods_by_name['DepositClaim']._options = None
  _MSG.methods_by_name['DepositClaim']._serialized_options = b'\202\323\344\223\002#\"!/injective/peggy/v1/deposit_claim'
  _MSG.methods_by_name['WithdrawClaim']._options = None
  _MSG.methods_by_name['WithdrawClaim']._serialized_options = b'\202\323\344\223\002$\"\"/injective/peggy/v1/withdraw_claim'
  _MSG.methods_by_name['ValsetUpdateClaim']._options = None
  _MSG.methods_by_name['ValsetUpdateClaim']._serialized_options = b'\202\323\344\223\002*\"(/injective/peggy/v1/valset_updated_claim'
  _MSG.methods_by_name['ERC20DeployedClaim']._options = None
  _MSG.methods_by_name['ERC20DeployedClaim']._serialized_options = b'\202\323\344\223\002*\"(/injective/peggy/v1/erc20_deployed_claim'
  _MSG.methods_by_name['SetOrchestratorAddresses']._options = None
  _MSG.methods_by_name['SetOrchestratorAddresses']._serialized_options = b'\202\323\344\223\002.\",/injective/peggy/v1/set_orchestrator_address'
  _MSG.methods_by_name['CancelSendToEth']._options = None
  _MSG.methods_by_name['CancelSendToEth']._serialized_options = b'\202\323\344\223\002(\"&/injective/peggy/v1/cancel_send_to_eth'
  _MSG.methods_by_name['SubmitBadSignatureEvidence']._options = None
  _MSG.methods_by_name['SubmitBadSignatureEvidence']._serialized_options = b'\202\323\344\223\0023\"1/injective/peggy/v1/submit_bad_signature_evidence'
  _MSGSETORCHESTRATORADDRESSES._serialized_start=196
  _MSGSETORCHESTRATORADDRESSES._serialized_end=284
  _MSGSETORCHESTRATORADDRESSESRESPONSE._serialized_start=286
  _MSGSETORCHESTRATORADDRESSESRESPONSE._serialized_end=323
  _MSGVALSETCONFIRM._serialized_start=325
  _MSGVALSETCONFIRM._serialized_end=420
  _MSGVALSETCONFIRMRESPONSE._serialized_start=422
  _MSGVALSETCONFIRMRESPONSE._serialized_end=448
  _MSGSENDTOETH._serialized_start=451
  _MSGSENDTOETH._serialized_end=601
  _MSGSENDTOETHRESPONSE._serialized_start=603
  _MSGSENDTOETHRESPONSE._serialized_end=625
  _MSGREQUESTBATCH._serialized_start=627
  _MSGREQUESTBATCH._serialized_end=681
  _MSGREQUESTBATCHRESPONSE._serialized_start=683
  _MSGREQUESTBATCHRESPONSE._serialized_end=708
  _MSGCONFIRMBATCH._serialized_start=710
  _MSGCONFIRMBATCH._serialized_end=827
  _MSGCONFIRMBATCHRESPONSE._serialized_start=829
  _MSGCONFIRMBATCHRESPONSE._serialized_end=854
  _MSGDEPOSITCLAIM._serialized_start=857
  _MSGDEPOSITCLAIM._serialized_end=1091
  _MSGDEPOSITCLAIMRESPONSE._serialized_start=1093
  _MSGDEPOSITCLAIMRESPONSE._serialized_end=1118
  _MSGWITHDRAWCLAIM._serialized_start=1121
  _MSGWITHDRAWCLAIM._serialized_end=1249
  _MSGWITHDRAWCLAIMRESPONSE._serialized_start=1251
  _MSGWITHDRAWCLAIMRESPONSE._serialized_end=1277
  _MSGERC20DEPLOYEDCLAIM._serialized_start=1280
  _MSGERC20DEPLOYEDCLAIM._serialized_end=1462
  _MSGERC20DEPLOYEDCLAIMRESPONSE._serialized_start=1464
  _MSGERC20DEPLOYEDCLAIMRESPONSE._serialized_end=1495
  _MSGCANCELSENDTOETH._serialized_start=1497
  _MSGCANCELSENDTOETH._serialized_end=1557
  _MSGCANCELSENDTOETHRESPONSE._serialized_start=1559
  _MSGCANCELSENDTOETHRESPONSE._serialized_end=1587
  _MSGSUBMITBADSIGNATUREEVIDENCE._serialized_start=1589
  _MSGSUBMITBADSIGNATUREEVIDENCE._serialized_end=1694
  _MSGSUBMITBADSIGNATUREEVIDENCERESPONSE._serialized_start=1696
  _MSGSUBMITBADSIGNATUREEVIDENCERESPONSE._serialized_end=1735
  _MSGVALSETUPDATEDCLAIM._serialized_start=1738
  _MSGVALSETUPDATEDCLAIM._serialized_end=1995
  _MSGVALSETUPDATEDCLAIMRESPONSE._serialized_start=1997
  _MSGVALSETUPDATEDCLAIMRESPONSE._serialized_end=2028
  _MSG._serialized_start=2031
  _MSG._serialized_end=3763
# @@protoc_insertion_point(module_scope)
