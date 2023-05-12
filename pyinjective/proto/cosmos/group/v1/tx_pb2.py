# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/group/v1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from cosmos.group.v1 import types_pb2 as cosmos_dot_group_dot_v1_dot_types__pb2
from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x63osmos/group/v1/tx.proto\x12\x0f\x63osmos.group.v1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x19google/protobuf/any.proto\x1a\x1b\x63osmos/group/v1/types.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x11\x61mino/amino.proto\"\xb1\x01\n\x0eMsgCreateGroup\x12\'\n\x05\x61\x64min\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12:\n\x07members\x18\x02 \x03(\x0b\x32\x1e.cosmos.group.v1.MemberRequestB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12\x10\n\x08metadata\x18\x03 \x01(\t:(\x82\xe7\xb0*\x05\x61\x64min\x8a\xe7\xb0*\x19\x63osmos-sdk/MsgCreateGroup\"*\n\x16MsgCreateGroupResponse\x12\x10\n\x08group_id\x18\x01 \x01(\x04\"\xc6\x01\n\x15MsgUpdateGroupMembers\x12\'\n\x05\x61\x64min\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x10\n\x08group_id\x18\x02 \x01(\x04\x12\x41\n\x0emember_updates\x18\x03 \x03(\x0b\x32\x1e.cosmos.group.v1.MemberRequestB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:/\x82\xe7\xb0*\x05\x61\x64min\x8a\xe7\xb0* cosmos-sdk/MsgUpdateGroupMembers\"\x1f\n\x1dMsgUpdateGroupMembersResponse\"\xac\x01\n\x13MsgUpdateGroupAdmin\x12\'\n\x05\x61\x64min\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x10\n\x08group_id\x18\x02 \x01(\x04\x12+\n\tnew_admin\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:-\x82\xe7\xb0*\x05\x61\x64min\x8a\xe7\xb0*\x1e\x63osmos-sdk/MsgUpdateGroupAdmin\"\x1d\n\x1bMsgUpdateGroupAdminResponse\"\x97\x01\n\x16MsgUpdateGroupMetadata\x12\'\n\x05\x61\x64min\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x10\n\x08group_id\x18\x02 \x01(\x04\x12\x10\n\x08metadata\x18\x03 \x01(\t:0\x82\xe7\xb0*\x05\x61\x64min\x8a\xe7\xb0*!cosmos-sdk/MsgUpdateGroupMetadata\" \n\x1eMsgUpdateGroupMetadataResponse\"\xea\x01\n\x14MsgCreateGroupPolicy\x12\'\n\x05\x61\x64min\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x10\n\x08group_id\x18\x02 \x01(\x04\x12\x10\n\x08metadata\x18\x03 \x01(\t\x12Q\n\x0f\x64\x65\x63ision_policy\x18\x04 \x01(\x0b\x32\x14.google.protobuf.AnyB\"\xca\xb4-\x1e\x63osmos.group.v1.DecisionPolicy:2\x82\xe7\xb0*\x05\x61\x64min\x8a\xe7\xb0*\x1f\x63osmos-sdk/MsgCreateGroupPolicy\x88\xa0\x1f\x00\"I\n\x1cMsgCreateGroupPolicyResponse\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\"\xde\x01\n\x19MsgUpdateGroupPolicyAdmin\x12\'\n\x05\x61\x64min\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x36\n\x14group_policy_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12+\n\tnew_admin\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:3\x82\xe7\xb0*\x05\x61\x64min\x8a\xe7\xb0*$cosmos-sdk/MsgUpdateGroupPolicyAdmin\"#\n!MsgUpdateGroupPolicyAdminResponse\"\xe0\x02\n\x18MsgCreateGroupWithPolicy\x12\'\n\x05\x61\x64min\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12:\n\x07members\x18\x02 \x03(\x0b\x32\x1e.cosmos.group.v1.MemberRequestB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12\x16\n\x0egroup_metadata\x18\x03 \x01(\t\x12\x1d\n\x15group_policy_metadata\x18\x04 \x01(\t\x12\x1d\n\x15group_policy_as_admin\x18\x05 \x01(\x08\x12Q\n\x0f\x64\x65\x63ision_policy\x18\x06 \x01(\x0b\x32\x14.google.protobuf.AnyB\"\xca\xb4-\x1e\x63osmos.group.v1.DecisionPolicy:6\x82\xe7\xb0*\x05\x61\x64min\x8a\xe7\xb0*#cosmos-sdk/MsgCreateGroupWithPolicy\x88\xa0\x1f\x00\"l\n MsgCreateGroupWithPolicyResponse\x12\x10\n\x08group_id\x18\x01 \x01(\x04\x12\x36\n\x14group_policy_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\"\x94\x02\n\"MsgUpdateGroupPolicyDecisionPolicy\x12\'\n\x05\x61\x64min\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x36\n\x14group_policy_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12Q\n\x0f\x64\x65\x63ision_policy\x18\x03 \x01(\x0b\x32\x14.google.protobuf.AnyB\"\xca\xb4-\x1e\x63osmos.group.v1.DecisionPolicy::\x82\xe7\xb0*\x05\x61\x64min\x8a\xe7\xb0*\'cosmos-sdk/MsgUpdateGroupDecisionPolicy\x88\xa0\x1f\x00\",\n*MsgUpdateGroupPolicyDecisionPolicyResponse\"\xc9\x01\n\x1cMsgUpdateGroupPolicyMetadata\x12\'\n\x05\x61\x64min\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x36\n\x14group_policy_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x10\n\x08metadata\x18\x03 \x01(\t:6\x82\xe7\xb0*\x05\x61\x64min\x8a\xe7\xb0*\'cosmos-sdk/MsgUpdateGroupPolicyMetadata\"&\n$MsgUpdateGroupPolicyMetadataResponse\"\x98\x02\n\x11MsgSubmitProposal\x12\x36\n\x14group_policy_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x11\n\tproposers\x18\x02 \x03(\t\x12\x10\n\x08metadata\x18\x03 \x01(\t\x12&\n\x08messages\x18\x04 \x03(\x0b\x32\x14.google.protobuf.Any\x12#\n\x04\x65xec\x18\x05 \x01(\x0e\x32\x15.cosmos.group.v1.Exec\x12\r\n\x05title\x18\x06 \x01(\t\x12\x0f\n\x07summary\x18\x07 \x01(\t:9\x82\xe7\xb0*\tproposers\x8a\xe7\xb0*\"cosmos-sdk/group/MsgSubmitProposal\x88\xa0\x1f\x00\"0\n\x19MsgSubmitProposalResponse\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\"\x8c\x01\n\x13MsgWithdrawProposal\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12)\n\x07\x61\x64\x64ress\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:5\x82\xe7\xb0*\x07\x61\x64\x64ress\x8a\xe7\xb0*$cosmos-sdk/group/MsgWithdrawProposal\"\x1d\n\x1bMsgWithdrawProposalResponse\"\xd4\x01\n\x07MsgVote\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12\'\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12+\n\x06option\x18\x03 \x01(\x0e\x32\x1b.cosmos.group.v1.VoteOption\x12\x10\n\x08metadata\x18\x04 \x01(\t\x12#\n\x04\x65xec\x18\x05 \x01(\x0e\x32\x15.cosmos.group.v1.Exec:\'\x82\xe7\xb0*\x05voter\x8a\xe7\xb0*\x18\x63osmos-sdk/group/MsgVote\"\x11\n\x0fMsgVoteResponse\"t\n\x07MsgExec\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12*\n\x08\x65xecutor\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:(\x82\xe7\xb0*\x06signer\x8a\xe7\xb0*\x18\x63osmos-sdk/group/MsgExec\"J\n\x0fMsgExecResponse\x12\x37\n\x06result\x18\x02 \x01(\x0e\x32\'.cosmos.group.v1.ProposalExecutorResult\"}\n\rMsgLeaveGroup\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x10\n\x08group_id\x18\x02 \x01(\x04:/\x82\xe7\xb0*\x07\x61\x64\x64ress\x8a\xe7\xb0*\x1e\x63osmos-sdk/group/MsgLeaveGroup\"\x17\n\x15MsgLeaveGroupResponse**\n\x04\x45xec\x12\x14\n\x10\x45XEC_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x45XEC_TRY\x10\x01\x32\xca\x0b\n\x03Msg\x12W\n\x0b\x43reateGroup\x12\x1f.cosmos.group.v1.MsgCreateGroup\x1a\'.cosmos.group.v1.MsgCreateGroupResponse\x12l\n\x12UpdateGroupMembers\x12&.cosmos.group.v1.MsgUpdateGroupMembers\x1a..cosmos.group.v1.MsgUpdateGroupMembersResponse\x12\x66\n\x10UpdateGroupAdmin\x12$.cosmos.group.v1.MsgUpdateGroupAdmin\x1a,.cosmos.group.v1.MsgUpdateGroupAdminResponse\x12o\n\x13UpdateGroupMetadata\x12\'.cosmos.group.v1.MsgUpdateGroupMetadata\x1a/.cosmos.group.v1.MsgUpdateGroupMetadataResponse\x12i\n\x11\x43reateGroupPolicy\x12%.cosmos.group.v1.MsgCreateGroupPolicy\x1a-.cosmos.group.v1.MsgCreateGroupPolicyResponse\x12u\n\x15\x43reateGroupWithPolicy\x12).cosmos.group.v1.MsgCreateGroupWithPolicy\x1a\x31.cosmos.group.v1.MsgCreateGroupWithPolicyResponse\x12x\n\x16UpdateGroupPolicyAdmin\x12*.cosmos.group.v1.MsgUpdateGroupPolicyAdmin\x1a\x32.cosmos.group.v1.MsgUpdateGroupPolicyAdminResponse\x12\x93\x01\n\x1fUpdateGroupPolicyDecisionPolicy\x12\x33.cosmos.group.v1.MsgUpdateGroupPolicyDecisionPolicy\x1a;.cosmos.group.v1.MsgUpdateGroupPolicyDecisionPolicyResponse\x12\x81\x01\n\x19UpdateGroupPolicyMetadata\x12-.cosmos.group.v1.MsgUpdateGroupPolicyMetadata\x1a\x35.cosmos.group.v1.MsgUpdateGroupPolicyMetadataResponse\x12`\n\x0eSubmitProposal\x12\".cosmos.group.v1.MsgSubmitProposal\x1a*.cosmos.group.v1.MsgSubmitProposalResponse\x12\x66\n\x10WithdrawProposal\x12$.cosmos.group.v1.MsgWithdrawProposal\x1a,.cosmos.group.v1.MsgWithdrawProposalResponse\x12\x42\n\x04Vote\x12\x18.cosmos.group.v1.MsgVote\x1a .cosmos.group.v1.MsgVoteResponse\x12\x42\n\x04\x45xec\x12\x18.cosmos.group.v1.MsgExec\x1a .cosmos.group.v1.MsgExecResponse\x12T\n\nLeaveGroup\x12\x1e.cosmos.group.v1.MsgLeaveGroup\x1a&.cosmos.group.v1.MsgLeaveGroupResponse\x1a\x05\x80\xe7\xb0*\x01\x42&Z$github.com/cosmos/cosmos-sdk/x/groupb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.group.v1.tx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z$github.com/cosmos/cosmos-sdk/x/group'
  _MSGCREATEGROUP.fields_by_name['admin']._options = None
  _MSGCREATEGROUP.fields_by_name['admin']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGCREATEGROUP.fields_by_name['members']._options = None
  _MSGCREATEGROUP.fields_by_name['members']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _MSGCREATEGROUP._options = None
  _MSGCREATEGROUP._serialized_options = b'\202\347\260*\005admin\212\347\260*\031cosmos-sdk/MsgCreateGroup'
  _MSGUPDATEGROUPMEMBERS.fields_by_name['admin']._options = None
  _MSGUPDATEGROUPMEMBERS.fields_by_name['admin']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEGROUPMEMBERS.fields_by_name['member_updates']._options = None
  _MSGUPDATEGROUPMEMBERS.fields_by_name['member_updates']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _MSGUPDATEGROUPMEMBERS._options = None
  _MSGUPDATEGROUPMEMBERS._serialized_options = b'\202\347\260*\005admin\212\347\260* cosmos-sdk/MsgUpdateGroupMembers'
  _MSGUPDATEGROUPADMIN.fields_by_name['admin']._options = None
  _MSGUPDATEGROUPADMIN.fields_by_name['admin']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEGROUPADMIN.fields_by_name['new_admin']._options = None
  _MSGUPDATEGROUPADMIN.fields_by_name['new_admin']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEGROUPADMIN._options = None
  _MSGUPDATEGROUPADMIN._serialized_options = b'\202\347\260*\005admin\212\347\260*\036cosmos-sdk/MsgUpdateGroupAdmin'
  _MSGUPDATEGROUPMETADATA.fields_by_name['admin']._options = None
  _MSGUPDATEGROUPMETADATA.fields_by_name['admin']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEGROUPMETADATA._options = None
  _MSGUPDATEGROUPMETADATA._serialized_options = b'\202\347\260*\005admin\212\347\260*!cosmos-sdk/MsgUpdateGroupMetadata'
  _MSGCREATEGROUPPOLICY.fields_by_name['admin']._options = None
  _MSGCREATEGROUPPOLICY.fields_by_name['admin']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGCREATEGROUPPOLICY.fields_by_name['decision_policy']._options = None
  _MSGCREATEGROUPPOLICY.fields_by_name['decision_policy']._serialized_options = b'\312\264-\036cosmos.group.v1.DecisionPolicy'
  _MSGCREATEGROUPPOLICY._options = None
  _MSGCREATEGROUPPOLICY._serialized_options = b'\202\347\260*\005admin\212\347\260*\037cosmos-sdk/MsgCreateGroupPolicy\210\240\037\000'
  _MSGCREATEGROUPPOLICYRESPONSE.fields_by_name['address']._options = None
  _MSGCREATEGROUPPOLICYRESPONSE.fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEGROUPPOLICYADMIN.fields_by_name['admin']._options = None
  _MSGUPDATEGROUPPOLICYADMIN.fields_by_name['admin']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEGROUPPOLICYADMIN.fields_by_name['group_policy_address']._options = None
  _MSGUPDATEGROUPPOLICYADMIN.fields_by_name['group_policy_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEGROUPPOLICYADMIN.fields_by_name['new_admin']._options = None
  _MSGUPDATEGROUPPOLICYADMIN.fields_by_name['new_admin']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEGROUPPOLICYADMIN._options = None
  _MSGUPDATEGROUPPOLICYADMIN._serialized_options = b'\202\347\260*\005admin\212\347\260*$cosmos-sdk/MsgUpdateGroupPolicyAdmin'
  _MSGCREATEGROUPWITHPOLICY.fields_by_name['admin']._options = None
  _MSGCREATEGROUPWITHPOLICY.fields_by_name['admin']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGCREATEGROUPWITHPOLICY.fields_by_name['members']._options = None
  _MSGCREATEGROUPWITHPOLICY.fields_by_name['members']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _MSGCREATEGROUPWITHPOLICY.fields_by_name['decision_policy']._options = None
  _MSGCREATEGROUPWITHPOLICY.fields_by_name['decision_policy']._serialized_options = b'\312\264-\036cosmos.group.v1.DecisionPolicy'
  _MSGCREATEGROUPWITHPOLICY._options = None
  _MSGCREATEGROUPWITHPOLICY._serialized_options = b'\202\347\260*\005admin\212\347\260*#cosmos-sdk/MsgCreateGroupWithPolicy\210\240\037\000'
  _MSGCREATEGROUPWITHPOLICYRESPONSE.fields_by_name['group_policy_address']._options = None
  _MSGCREATEGROUPWITHPOLICYRESPONSE.fields_by_name['group_policy_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEGROUPPOLICYDECISIONPOLICY.fields_by_name['admin']._options = None
  _MSGUPDATEGROUPPOLICYDECISIONPOLICY.fields_by_name['admin']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEGROUPPOLICYDECISIONPOLICY.fields_by_name['group_policy_address']._options = None
  _MSGUPDATEGROUPPOLICYDECISIONPOLICY.fields_by_name['group_policy_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEGROUPPOLICYDECISIONPOLICY.fields_by_name['decision_policy']._options = None
  _MSGUPDATEGROUPPOLICYDECISIONPOLICY.fields_by_name['decision_policy']._serialized_options = b'\312\264-\036cosmos.group.v1.DecisionPolicy'
  _MSGUPDATEGROUPPOLICYDECISIONPOLICY._options = None
  _MSGUPDATEGROUPPOLICYDECISIONPOLICY._serialized_options = b'\202\347\260*\005admin\212\347\260*\'cosmos-sdk/MsgUpdateGroupDecisionPolicy\210\240\037\000'
  _MSGUPDATEGROUPPOLICYMETADATA.fields_by_name['admin']._options = None
  _MSGUPDATEGROUPPOLICYMETADATA.fields_by_name['admin']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEGROUPPOLICYMETADATA.fields_by_name['group_policy_address']._options = None
  _MSGUPDATEGROUPPOLICYMETADATA.fields_by_name['group_policy_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEGROUPPOLICYMETADATA._options = None
  _MSGUPDATEGROUPPOLICYMETADATA._serialized_options = b'\202\347\260*\005admin\212\347\260*\'cosmos-sdk/MsgUpdateGroupPolicyMetadata'
  _MSGSUBMITPROPOSAL.fields_by_name['group_policy_address']._options = None
  _MSGSUBMITPROPOSAL.fields_by_name['group_policy_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGSUBMITPROPOSAL._options = None
  _MSGSUBMITPROPOSAL._serialized_options = b'\202\347\260*\tproposers\212\347\260*\"cosmos-sdk/group/MsgSubmitProposal\210\240\037\000'
  _MSGWITHDRAWPROPOSAL.fields_by_name['address']._options = None
  _MSGWITHDRAWPROPOSAL.fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGWITHDRAWPROPOSAL._options = None
  _MSGWITHDRAWPROPOSAL._serialized_options = b'\202\347\260*\007address\212\347\260*$cosmos-sdk/group/MsgWithdrawProposal'
  _MSGVOTE.fields_by_name['voter']._options = None
  _MSGVOTE.fields_by_name['voter']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGVOTE._options = None
  _MSGVOTE._serialized_options = b'\202\347\260*\005voter\212\347\260*\030cosmos-sdk/group/MsgVote'
  _MSGEXEC.fields_by_name['executor']._options = None
  _MSGEXEC.fields_by_name['executor']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGEXEC._options = None
  _MSGEXEC._serialized_options = b'\202\347\260*\006signer\212\347\260*\030cosmos-sdk/group/MsgExec'
  _MSGLEAVEGROUP.fields_by_name['address']._options = None
  _MSGLEAVEGROUP.fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGLEAVEGROUP._options = None
  _MSGLEAVEGROUP._serialized_options = b'\202\347\260*\007address\212\347\260*\036cosmos-sdk/group/MsgLeaveGroup'
  _MSG._options = None
  _MSG._serialized_options = b'\200\347\260*\001'
  _EXEC._serialized_start=3741
  _EXEC._serialized_end=3783
  _MSGCREATEGROUP._serialized_start=195
  _MSGCREATEGROUP._serialized_end=372
  _MSGCREATEGROUPRESPONSE._serialized_start=374
  _MSGCREATEGROUPRESPONSE._serialized_end=416
  _MSGUPDATEGROUPMEMBERS._serialized_start=419
  _MSGUPDATEGROUPMEMBERS._serialized_end=617
  _MSGUPDATEGROUPMEMBERSRESPONSE._serialized_start=619
  _MSGUPDATEGROUPMEMBERSRESPONSE._serialized_end=650
  _MSGUPDATEGROUPADMIN._serialized_start=653
  _MSGUPDATEGROUPADMIN._serialized_end=825
  _MSGUPDATEGROUPADMINRESPONSE._serialized_start=827
  _MSGUPDATEGROUPADMINRESPONSE._serialized_end=856
  _MSGUPDATEGROUPMETADATA._serialized_start=859
  _MSGUPDATEGROUPMETADATA._serialized_end=1010
  _MSGUPDATEGROUPMETADATARESPONSE._serialized_start=1012
  _MSGUPDATEGROUPMETADATARESPONSE._serialized_end=1044
  _MSGCREATEGROUPPOLICY._serialized_start=1047
  _MSGCREATEGROUPPOLICY._serialized_end=1281
  _MSGCREATEGROUPPOLICYRESPONSE._serialized_start=1283
  _MSGCREATEGROUPPOLICYRESPONSE._serialized_end=1356
  _MSGUPDATEGROUPPOLICYADMIN._serialized_start=1359
  _MSGUPDATEGROUPPOLICYADMIN._serialized_end=1581
  _MSGUPDATEGROUPPOLICYADMINRESPONSE._serialized_start=1583
  _MSGUPDATEGROUPPOLICYADMINRESPONSE._serialized_end=1618
  _MSGCREATEGROUPWITHPOLICY._serialized_start=1621
  _MSGCREATEGROUPWITHPOLICY._serialized_end=1973
  _MSGCREATEGROUPWITHPOLICYRESPONSE._serialized_start=1975
  _MSGCREATEGROUPWITHPOLICYRESPONSE._serialized_end=2083
  _MSGUPDATEGROUPPOLICYDECISIONPOLICY._serialized_start=2086
  _MSGUPDATEGROUPPOLICYDECISIONPOLICY._serialized_end=2362
  _MSGUPDATEGROUPPOLICYDECISIONPOLICYRESPONSE._serialized_start=2364
  _MSGUPDATEGROUPPOLICYDECISIONPOLICYRESPONSE._serialized_end=2408
  _MSGUPDATEGROUPPOLICYMETADATA._serialized_start=2411
  _MSGUPDATEGROUPPOLICYMETADATA._serialized_end=2612
  _MSGUPDATEGROUPPOLICYMETADATARESPONSE._serialized_start=2614
  _MSGUPDATEGROUPPOLICYMETADATARESPONSE._serialized_end=2652
  _MSGSUBMITPROPOSAL._serialized_start=2655
  _MSGSUBMITPROPOSAL._serialized_end=2935
  _MSGSUBMITPROPOSALRESPONSE._serialized_start=2937
  _MSGSUBMITPROPOSALRESPONSE._serialized_end=2985
  _MSGWITHDRAWPROPOSAL._serialized_start=2988
  _MSGWITHDRAWPROPOSAL._serialized_end=3128
  _MSGWITHDRAWPROPOSALRESPONSE._serialized_start=3130
  _MSGWITHDRAWPROPOSALRESPONSE._serialized_end=3159
  _MSGVOTE._serialized_start=3162
  _MSGVOTE._serialized_end=3374
  _MSGVOTERESPONSE._serialized_start=3376
  _MSGVOTERESPONSE._serialized_end=3393
  _MSGEXEC._serialized_start=3395
  _MSGEXEC._serialized_end=3511
  _MSGEXECRESPONSE._serialized_start=3513
  _MSGEXECRESPONSE._serialized_end=3587
  _MSGLEAVEGROUP._serialized_start=3589
  _MSGLEAVEGROUP._serialized_end=3714
  _MSGLEAVEGROUPRESPONSE._serialized_start=3716
  _MSGLEAVEGROUPRESPONSE._serialized_end=3739
  _MSG._serialized_start=3786
  _MSG._serialized_end=5268
# @@protoc_insertion_point(module_scope)
