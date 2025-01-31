# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/channel/v1/query.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2
from pyinjective.proto.cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from pyinjective.proto.ibc.core.channel.v1 import channel_pb2 as ibc_dot_core_dot_channel_dot_v1_dot_channel__pb2
from pyinjective.proto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.ibc.core.channel.v1 import upgrade_pb2 as ibc_dot_core_dot_channel_dot_v1_dot_upgrade__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fibc/core/channel/v1/query.proto\x12\x13ibc.core.channel.v1\x1a\x1fibc/core/client/v1/client.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a!ibc/core/channel/v1/channel.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto\x1a\x14gogoproto/gogo.proto\x1a!ibc/core/channel/v1/upgrade.proto\"M\n\x13QueryChannelRequest\x12\x17\n\x07port_id\x18\x01 \x01(\tR\x06portId\x12\x1d\n\nchannel_id\x18\x02 \x01(\tR\tchannelId\"\xa9\x01\n\x14QueryChannelResponse\x12\x36\n\x07\x63hannel\x18\x01 \x01(\x0b\x32\x1c.ibc.core.channel.v1.ChannelR\x07\x63hannel\x12\x14\n\x05proof\x18\x02 \x01(\x0cR\x05proof\x12\x43\n\x0cproof_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00R\x0bproofHeight\"^\n\x14QueryChannelsRequest\x12\x46\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\xde\x01\n\x15QueryChannelsResponse\x12\x42\n\x08\x63hannels\x18\x01 \x03(\x0b\x32&.ibc.core.channel.v1.IdentifiedChannelR\x08\x63hannels\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\x12\x38\n\x06height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00R\x06height\"\x88\x01\n\x1eQueryConnectionChannelsRequest\x12\x1e\n\nconnection\x18\x01 \x01(\tR\nconnection\x12\x46\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\xe8\x01\n\x1fQueryConnectionChannelsResponse\x12\x42\n\x08\x63hannels\x18\x01 \x03(\x0b\x32&.ibc.core.channel.v1.IdentifiedChannelR\x08\x63hannels\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\x12\x38\n\x06height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00R\x06height\"X\n\x1eQueryChannelClientStateRequest\x12\x17\n\x07port_id\x18\x01 \x01(\tR\x06portId\x12\x1d\n\nchannel_id\x18\x02 \x01(\tR\tchannelId\"\xdf\x01\n\x1fQueryChannelClientStateResponse\x12\x61\n\x17identified_client_state\x18\x01 \x01(\x0b\x32).ibc.core.client.v1.IdentifiedClientStateR\x15identifiedClientState\x12\x14\n\x05proof\x18\x02 \x01(\x0cR\x05proof\x12\x43\n\x0cproof_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00R\x0bproofHeight\"\xad\x01\n!QueryChannelConsensusStateRequest\x12\x17\n\x07port_id\x18\x01 \x01(\tR\x06portId\x12\x1d\n\nchannel_id\x18\x02 \x01(\tR\tchannelId\x12\'\n\x0frevision_number\x18\x03 \x01(\x04R\x0erevisionNumber\x12\'\n\x0frevision_height\x18\x04 \x01(\x04R\x0erevisionHeight\"\xdb\x01\n\"QueryChannelConsensusStateResponse\x12=\n\x0f\x63onsensus_state\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyR\x0e\x63onsensusState\x12\x1b\n\tclient_id\x18\x02 \x01(\tR\x08\x63lientId\x12\x14\n\x05proof\x18\x03 \x01(\x0cR\x05proof\x12\x43\n\x0cproof_height\x18\x04 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00R\x0bproofHeight\"r\n\x1cQueryPacketCommitmentRequest\x12\x17\n\x07port_id\x18\x01 \x01(\tR\x06portId\x12\x1d\n\nchannel_id\x18\x02 \x01(\tR\tchannelId\x12\x1a\n\x08sequence\x18\x03 \x01(\x04R\x08sequence\"\x9a\x01\n\x1dQueryPacketCommitmentResponse\x12\x1e\n\ncommitment\x18\x01 \x01(\x0cR\ncommitment\x12\x14\n\x05proof\x18\x02 \x01(\x0cR\x05proof\x12\x43\n\x0cproof_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00R\x0bproofHeight\"\x9f\x01\n\x1dQueryPacketCommitmentsRequest\x12\x17\n\x07port_id\x18\x01 \x01(\tR\x06portId\x12\x1d\n\nchannel_id\x18\x02 \x01(\tR\tchannelId\x12\x46\n\npagination\x18\x03 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\xe7\x01\n\x1eQueryPacketCommitmentsResponse\x12\x42\n\x0b\x63ommitments\x18\x01 \x03(\x0b\x32 .ibc.core.channel.v1.PacketStateR\x0b\x63ommitments\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\x12\x38\n\x06height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00R\x06height\"o\n\x19QueryPacketReceiptRequest\x12\x17\n\x07port_id\x18\x01 \x01(\tR\x06portId\x12\x1d\n\nchannel_id\x18\x02 \x01(\tR\tchannelId\x12\x1a\n\x08sequence\x18\x03 \x01(\x04R\x08sequence\"\x93\x01\n\x1aQueryPacketReceiptResponse\x12\x1a\n\x08received\x18\x02 \x01(\x08R\x08received\x12\x14\n\x05proof\x18\x03 \x01(\x0cR\x05proof\x12\x43\n\x0cproof_height\x18\x04 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00R\x0bproofHeight\"w\n!QueryPacketAcknowledgementRequest\x12\x17\n\x07port_id\x18\x01 \x01(\tR\x06portId\x12\x1d\n\nchannel_id\x18\x02 \x01(\tR\tchannelId\x12\x1a\n\x08sequence\x18\x03 \x01(\x04R\x08sequence\"\xa9\x01\n\"QueryPacketAcknowledgementResponse\x12(\n\x0f\x61\x63knowledgement\x18\x01 \x01(\x0cR\x0f\x61\x63knowledgement\x12\x14\n\x05proof\x18\x02 \x01(\x0cR\x05proof\x12\x43\n\x0cproof_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00R\x0bproofHeight\"\xe4\x01\n\"QueryPacketAcknowledgementsRequest\x12\x17\n\x07port_id\x18\x01 \x01(\tR\x06portId\x12\x1d\n\nchannel_id\x18\x02 \x01(\tR\tchannelId\x12\x46\n\npagination\x18\x03 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\x12>\n\x1bpacket_commitment_sequences\x18\x04 \x03(\x04R\x19packetCommitmentSequences\"\xf6\x01\n#QueryPacketAcknowledgementsResponse\x12L\n\x10\x61\x63knowledgements\x18\x01 \x03(\x0b\x32 .ibc.core.channel.v1.PacketStateR\x10\x61\x63knowledgements\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\x12\x38\n\x06height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00R\x06height\"\x97\x01\n\x1dQueryUnreceivedPacketsRequest\x12\x17\n\x07port_id\x18\x01 \x01(\tR\x06portId\x12\x1d\n\nchannel_id\x18\x02 \x01(\tR\tchannelId\x12>\n\x1bpacket_commitment_sequences\x18\x03 \x03(\x04R\x19packetCommitmentSequences\"x\n\x1eQueryUnreceivedPacketsResponse\x12\x1c\n\tsequences\x18\x01 \x03(\x04R\tsequences\x12\x38\n\x06height\x18\x02 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00R\x06height\"\x86\x01\n\x1aQueryUnreceivedAcksRequest\x12\x17\n\x07port_id\x18\x01 \x01(\tR\x06portId\x12\x1d\n\nchannel_id\x18\x02 \x01(\tR\tchannelId\x12\x30\n\x14packet_ack_sequences\x18\x03 \x03(\x04R\x12packetAckSequences\"u\n\x1bQueryUnreceivedAcksResponse\x12\x1c\n\tsequences\x18\x01 \x03(\x04R\tsequences\x12\x38\n\x06height\x18\x02 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00R\x06height\"Y\n\x1fQueryNextSequenceReceiveRequest\x12\x17\n\x07port_id\x18\x01 \x01(\tR\x06portId\x12\x1d\n\nchannel_id\x18\x02 \x01(\tR\tchannelId\"\xb1\x01\n QueryNextSequenceReceiveResponse\x12\x32\n\x15next_sequence_receive\x18\x01 \x01(\x04R\x13nextSequenceReceive\x12\x14\n\x05proof\x18\x02 \x01(\x0cR\x05proof\x12\x43\n\x0cproof_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00R\x0bproofHeight\"V\n\x1cQueryNextSequenceSendRequest\x12\x17\n\x07port_id\x18\x01 \x01(\tR\x06portId\x12\x1d\n\nchannel_id\x18\x02 \x01(\tR\tchannelId\"\xa8\x01\n\x1dQueryNextSequenceSendResponse\x12,\n\x12next_sequence_send\x18\x01 \x01(\x04R\x10nextSequenceSend\x12\x14\n\x05proof\x18\x02 \x01(\x0cR\x05proof\x12\x43\n\x0cproof_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00R\x0bproofHeight\"R\n\x18QueryUpgradeErrorRequest\x12\x17\n\x07port_id\x18\x01 \x01(\tR\x06portId\x12\x1d\n\nchannel_id\x18\x02 \x01(\tR\tchannelId\"\xc4\x01\n\x19QueryUpgradeErrorResponse\x12L\n\rerror_receipt\x18\x01 \x01(\x0b\x32!.ibc.core.channel.v1.ErrorReceiptB\x04\xc8\xde\x1f\x00R\x0c\x65rrorReceipt\x12\x14\n\x05proof\x18\x02 \x01(\x0cR\x05proof\x12\x43\n\x0cproof_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00R\x0bproofHeight\"M\n\x13QueryUpgradeRequest\x12\x17\n\x07port_id\x18\x01 \x01(\tR\x06portId\x12\x1d\n\nchannel_id\x18\x02 \x01(\tR\tchannelId\"\xaf\x01\n\x14QueryUpgradeResponse\x12<\n\x07upgrade\x18\x01 \x01(\x0b\x32\x1c.ibc.core.channel.v1.UpgradeB\x04\xc8\xde\x1f\x00R\x07upgrade\x12\x14\n\x05proof\x18\x02 \x01(\x0cR\x05proof\x12\x43\n\x0cproof_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00R\x0bproofHeight\"\x1b\n\x19QueryChannelParamsRequest\"Q\n\x1aQueryChannelParamsResponse\x12\x33\n\x06params\x18\x01 \x01(\x0b\x32\x1b.ibc.core.channel.v1.ParamsR\x06params2\xe5\x1b\n\x05Query\x12\xa2\x01\n\x07\x43hannel\x12(.ibc.core.channel.v1.QueryChannelRequest\x1a).ibc.core.channel.v1.QueryChannelResponse\"B\x82\xd3\xe4\x93\x02<\x12:/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}\x12\x88\x01\n\x08\x43hannels\x12).ibc.core.channel.v1.QueryChannelsRequest\x1a*.ibc.core.channel.v1.QueryChannelsResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/ibc/core/channel/v1/channels\x12\xbf\x01\n\x12\x43onnectionChannels\x12\x33.ibc.core.channel.v1.QueryConnectionChannelsRequest\x1a\x34.ibc.core.channel.v1.QueryConnectionChannelsResponse\">\x82\xd3\xe4\x93\x02\x38\x12\x36/ibc/core/channel/v1/connections/{connection}/channels\x12\xd0\x01\n\x12\x43hannelClientState\x12\x33.ibc.core.channel.v1.QueryChannelClientStateRequest\x1a\x34.ibc.core.channel.v1.QueryChannelClientStateResponse\"O\x82\xd3\xe4\x93\x02I\x12G/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/client_state\x12\x92\x02\n\x15\x43hannelConsensusState\x12\x36.ibc.core.channel.v1.QueryChannelConsensusStateRequest\x1a\x37.ibc.core.channel.v1.QueryChannelConsensusStateResponse\"\x87\x01\x82\xd3\xe4\x93\x02\x80\x01\x12~/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/consensus_state/revision/{revision_number}/height/{revision_height}\x12\xdb\x01\n\x10PacketCommitment\x12\x31.ibc.core.channel.v1.QueryPacketCommitmentRequest\x1a\x32.ibc.core.channel.v1.QueryPacketCommitmentResponse\"`\x82\xd3\xe4\x93\x02Z\x12X/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_commitments/{sequence}\x12\xd3\x01\n\x11PacketCommitments\x12\x32.ibc.core.channel.v1.QueryPacketCommitmentsRequest\x1a\x33.ibc.core.channel.v1.QueryPacketCommitmentsResponse\"U\x82\xd3\xe4\x93\x02O\x12M/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_commitments\x12\xcf\x01\n\rPacketReceipt\x12..ibc.core.channel.v1.QueryPacketReceiptRequest\x1a/.ibc.core.channel.v1.QueryPacketReceiptResponse\"]\x82\xd3\xe4\x93\x02W\x12U/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_receipts/{sequence}\x12\xe3\x01\n\x15PacketAcknowledgement\x12\x36.ibc.core.channel.v1.QueryPacketAcknowledgementRequest\x1a\x37.ibc.core.channel.v1.QueryPacketAcknowledgementResponse\"Y\x82\xd3\xe4\x93\x02S\x12Q/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_acks/{sequence}\x12\xe7\x01\n\x16PacketAcknowledgements\x12\x37.ibc.core.channel.v1.QueryPacketAcknowledgementsRequest\x1a\x38.ibc.core.channel.v1.QueryPacketAcknowledgementsResponse\"Z\x82\xd3\xe4\x93\x02T\x12R/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_acknowledgements\x12\x86\x02\n\x11UnreceivedPackets\x12\x32.ibc.core.channel.v1.QueryUnreceivedPacketsRequest\x1a\x33.ibc.core.channel.v1.QueryUnreceivedPacketsResponse\"\x87\x01\x82\xd3\xe4\x93\x02\x80\x01\x12~/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_commitments/{packet_commitment_sequences}/unreceived_packets\x12\xf1\x01\n\x0eUnreceivedAcks\x12/.ibc.core.channel.v1.QueryUnreceivedAcksRequest\x1a\x30.ibc.core.channel.v1.QueryUnreceivedAcksResponse\"|\x82\xd3\xe4\x93\x02v\x12t/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_commitments/{packet_ack_sequences}/unreceived_acks\x12\xd4\x01\n\x13NextSequenceReceive\x12\x34.ibc.core.channel.v1.QueryNextSequenceReceiveRequest\x1a\x35.ibc.core.channel.v1.QueryNextSequenceReceiveResponse\"P\x82\xd3\xe4\x93\x02J\x12H/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/next_sequence\x12\xd0\x01\n\x10NextSequenceSend\x12\x31.ibc.core.channel.v1.QueryNextSequenceSendRequest\x1a\x32.ibc.core.channel.v1.QueryNextSequenceSendResponse\"U\x82\xd3\xe4\x93\x02O\x12M/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/next_sequence_send\x12\xbf\x01\n\x0cUpgradeError\x12-.ibc.core.channel.v1.QueryUpgradeErrorRequest\x1a..ibc.core.channel.v1.QueryUpgradeErrorResponse\"P\x82\xd3\xe4\x93\x02J\x12H/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/upgrade_error\x12\xaa\x01\n\x07Upgrade\x12(.ibc.core.channel.v1.QueryUpgradeRequest\x1a).ibc.core.channel.v1.QueryUpgradeResponse\"J\x82\xd3\xe4\x93\x02\x44\x12\x42/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/upgrade\x12\x95\x01\n\rChannelParams\x12..ibc.core.channel.v1.QueryChannelParamsRequest\x1a/.ibc.core.channel.v1.QueryChannelParamsResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/ibc/core/channel/v1/paramsB\xcf\x01\n\x17\x63om.ibc.core.channel.v1B\nQueryProtoP\x01Z9github.com/cosmos/ibc-go/v8/modules/core/04-channel/types\xa2\x02\x03ICC\xaa\x02\x13Ibc.Core.Channel.V1\xca\x02\x13Ibc\\Core\\Channel\\V1\xe2\x02\x1fIbc\\Core\\Channel\\V1\\GPBMetadata\xea\x02\x16Ibc::Core::Channel::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.core.channel.v1.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027com.ibc.core.channel.v1B\nQueryProtoP\001Z9github.com/cosmos/ibc-go/v8/modules/core/04-channel/types\242\002\003ICC\252\002\023Ibc.Core.Channel.V1\312\002\023Ibc\\Core\\Channel\\V1\342\002\037Ibc\\Core\\Channel\\V1\\GPBMetadata\352\002\026Ibc::Core::Channel::V1'
  _globals['_QUERYCHANNELRESPONSE'].fields_by_name['proof_height']._loaded_options = None
  _globals['_QUERYCHANNELRESPONSE'].fields_by_name['proof_height']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYCHANNELSRESPONSE'].fields_by_name['height']._loaded_options = None
  _globals['_QUERYCHANNELSRESPONSE'].fields_by_name['height']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYCONNECTIONCHANNELSRESPONSE'].fields_by_name['height']._loaded_options = None
  _globals['_QUERYCONNECTIONCHANNELSRESPONSE'].fields_by_name['height']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYCHANNELCLIENTSTATERESPONSE'].fields_by_name['proof_height']._loaded_options = None
  _globals['_QUERYCHANNELCLIENTSTATERESPONSE'].fields_by_name['proof_height']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYCHANNELCONSENSUSSTATERESPONSE'].fields_by_name['proof_height']._loaded_options = None
  _globals['_QUERYCHANNELCONSENSUSSTATERESPONSE'].fields_by_name['proof_height']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYPACKETCOMMITMENTRESPONSE'].fields_by_name['proof_height']._loaded_options = None
  _globals['_QUERYPACKETCOMMITMENTRESPONSE'].fields_by_name['proof_height']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYPACKETCOMMITMENTSRESPONSE'].fields_by_name['height']._loaded_options = None
  _globals['_QUERYPACKETCOMMITMENTSRESPONSE'].fields_by_name['height']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYPACKETRECEIPTRESPONSE'].fields_by_name['proof_height']._loaded_options = None
  _globals['_QUERYPACKETRECEIPTRESPONSE'].fields_by_name['proof_height']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYPACKETACKNOWLEDGEMENTRESPONSE'].fields_by_name['proof_height']._loaded_options = None
  _globals['_QUERYPACKETACKNOWLEDGEMENTRESPONSE'].fields_by_name['proof_height']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYPACKETACKNOWLEDGEMENTSRESPONSE'].fields_by_name['height']._loaded_options = None
  _globals['_QUERYPACKETACKNOWLEDGEMENTSRESPONSE'].fields_by_name['height']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYUNRECEIVEDPACKETSRESPONSE'].fields_by_name['height']._loaded_options = None
  _globals['_QUERYUNRECEIVEDPACKETSRESPONSE'].fields_by_name['height']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYUNRECEIVEDACKSRESPONSE'].fields_by_name['height']._loaded_options = None
  _globals['_QUERYUNRECEIVEDACKSRESPONSE'].fields_by_name['height']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYNEXTSEQUENCERECEIVERESPONSE'].fields_by_name['proof_height']._loaded_options = None
  _globals['_QUERYNEXTSEQUENCERECEIVERESPONSE'].fields_by_name['proof_height']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYNEXTSEQUENCESENDRESPONSE'].fields_by_name['proof_height']._loaded_options = None
  _globals['_QUERYNEXTSEQUENCESENDRESPONSE'].fields_by_name['proof_height']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYUPGRADEERRORRESPONSE'].fields_by_name['error_receipt']._loaded_options = None
  _globals['_QUERYUPGRADEERRORRESPONSE'].fields_by_name['error_receipt']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYUPGRADEERRORRESPONSE'].fields_by_name['proof_height']._loaded_options = None
  _globals['_QUERYUPGRADEERRORRESPONSE'].fields_by_name['proof_height']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYUPGRADERESPONSE'].fields_by_name['upgrade']._loaded_options = None
  _globals['_QUERYUPGRADERESPONSE'].fields_by_name['upgrade']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYUPGRADERESPONSE'].fields_by_name['proof_height']._loaded_options = None
  _globals['_QUERYUPGRADERESPONSE'].fields_by_name['proof_height']._serialized_options = b'\310\336\037\000'
  _globals['_QUERY'].methods_by_name['Channel']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Channel']._serialized_options = b'\202\323\344\223\002<\022:/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}'
  _globals['_QUERY'].methods_by_name['Channels']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Channels']._serialized_options = b'\202\323\344\223\002\037\022\035/ibc/core/channel/v1/channels'
  _globals['_QUERY'].methods_by_name['ConnectionChannels']._loaded_options = None
  _globals['_QUERY'].methods_by_name['ConnectionChannels']._serialized_options = b'\202\323\344\223\0028\0226/ibc/core/channel/v1/connections/{connection}/channels'
  _globals['_QUERY'].methods_by_name['ChannelClientState']._loaded_options = None
  _globals['_QUERY'].methods_by_name['ChannelClientState']._serialized_options = b'\202\323\344\223\002I\022G/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/client_state'
  _globals['_QUERY'].methods_by_name['ChannelConsensusState']._loaded_options = None
  _globals['_QUERY'].methods_by_name['ChannelConsensusState']._serialized_options = b'\202\323\344\223\002\200\001\022~/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/consensus_state/revision/{revision_number}/height/{revision_height}'
  _globals['_QUERY'].methods_by_name['PacketCommitment']._loaded_options = None
  _globals['_QUERY'].methods_by_name['PacketCommitment']._serialized_options = b'\202\323\344\223\002Z\022X/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_commitments/{sequence}'
  _globals['_QUERY'].methods_by_name['PacketCommitments']._loaded_options = None
  _globals['_QUERY'].methods_by_name['PacketCommitments']._serialized_options = b'\202\323\344\223\002O\022M/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_commitments'
  _globals['_QUERY'].methods_by_name['PacketReceipt']._loaded_options = None
  _globals['_QUERY'].methods_by_name['PacketReceipt']._serialized_options = b'\202\323\344\223\002W\022U/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_receipts/{sequence}'
  _globals['_QUERY'].methods_by_name['PacketAcknowledgement']._loaded_options = None
  _globals['_QUERY'].methods_by_name['PacketAcknowledgement']._serialized_options = b'\202\323\344\223\002S\022Q/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_acks/{sequence}'
  _globals['_QUERY'].methods_by_name['PacketAcknowledgements']._loaded_options = None
  _globals['_QUERY'].methods_by_name['PacketAcknowledgements']._serialized_options = b'\202\323\344\223\002T\022R/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_acknowledgements'
  _globals['_QUERY'].methods_by_name['UnreceivedPackets']._loaded_options = None
  _globals['_QUERY'].methods_by_name['UnreceivedPackets']._serialized_options = b'\202\323\344\223\002\200\001\022~/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_commitments/{packet_commitment_sequences}/unreceived_packets'
  _globals['_QUERY'].methods_by_name['UnreceivedAcks']._loaded_options = None
  _globals['_QUERY'].methods_by_name['UnreceivedAcks']._serialized_options = b'\202\323\344\223\002v\022t/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_commitments/{packet_ack_sequences}/unreceived_acks'
  _globals['_QUERY'].methods_by_name['NextSequenceReceive']._loaded_options = None
  _globals['_QUERY'].methods_by_name['NextSequenceReceive']._serialized_options = b'\202\323\344\223\002J\022H/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/next_sequence'
  _globals['_QUERY'].methods_by_name['NextSequenceSend']._loaded_options = None
  _globals['_QUERY'].methods_by_name['NextSequenceSend']._serialized_options = b'\202\323\344\223\002O\022M/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/next_sequence_send'
  _globals['_QUERY'].methods_by_name['UpgradeError']._loaded_options = None
  _globals['_QUERY'].methods_by_name['UpgradeError']._serialized_options = b'\202\323\344\223\002J\022H/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/upgrade_error'
  _globals['_QUERY'].methods_by_name['Upgrade']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Upgrade']._serialized_options = b'\202\323\344\223\002D\022B/ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/upgrade'
  _globals['_QUERY'].methods_by_name['ChannelParams']._loaded_options = None
  _globals['_QUERY'].methods_by_name['ChannelParams']._serialized_options = b'\202\323\344\223\002\035\022\033/ibc/core/channel/v1/params'
  _globals['_QUERYCHANNELREQUEST']._serialized_start=282
  _globals['_QUERYCHANNELREQUEST']._serialized_end=359
  _globals['_QUERYCHANNELRESPONSE']._serialized_start=362
  _globals['_QUERYCHANNELRESPONSE']._serialized_end=531
  _globals['_QUERYCHANNELSREQUEST']._serialized_start=533
  _globals['_QUERYCHANNELSREQUEST']._serialized_end=627
  _globals['_QUERYCHANNELSRESPONSE']._serialized_start=630
  _globals['_QUERYCHANNELSRESPONSE']._serialized_end=852
  _globals['_QUERYCONNECTIONCHANNELSREQUEST']._serialized_start=855
  _globals['_QUERYCONNECTIONCHANNELSREQUEST']._serialized_end=991
  _globals['_QUERYCONNECTIONCHANNELSRESPONSE']._serialized_start=994
  _globals['_QUERYCONNECTIONCHANNELSRESPONSE']._serialized_end=1226
  _globals['_QUERYCHANNELCLIENTSTATEREQUEST']._serialized_start=1228
  _globals['_QUERYCHANNELCLIENTSTATEREQUEST']._serialized_end=1316
  _globals['_QUERYCHANNELCLIENTSTATERESPONSE']._serialized_start=1319
  _globals['_QUERYCHANNELCLIENTSTATERESPONSE']._serialized_end=1542
  _globals['_QUERYCHANNELCONSENSUSSTATEREQUEST']._serialized_start=1545
  _globals['_QUERYCHANNELCONSENSUSSTATEREQUEST']._serialized_end=1718
  _globals['_QUERYCHANNELCONSENSUSSTATERESPONSE']._serialized_start=1721
  _globals['_QUERYCHANNELCONSENSUSSTATERESPONSE']._serialized_end=1940
  _globals['_QUERYPACKETCOMMITMENTREQUEST']._serialized_start=1942
  _globals['_QUERYPACKETCOMMITMENTREQUEST']._serialized_end=2056
  _globals['_QUERYPACKETCOMMITMENTRESPONSE']._serialized_start=2059
  _globals['_QUERYPACKETCOMMITMENTRESPONSE']._serialized_end=2213
  _globals['_QUERYPACKETCOMMITMENTSREQUEST']._serialized_start=2216
  _globals['_QUERYPACKETCOMMITMENTSREQUEST']._serialized_end=2375
  _globals['_QUERYPACKETCOMMITMENTSRESPONSE']._serialized_start=2378
  _globals['_QUERYPACKETCOMMITMENTSRESPONSE']._serialized_end=2609
  _globals['_QUERYPACKETRECEIPTREQUEST']._serialized_start=2611
  _globals['_QUERYPACKETRECEIPTREQUEST']._serialized_end=2722
  _globals['_QUERYPACKETRECEIPTRESPONSE']._serialized_start=2725
  _globals['_QUERYPACKETRECEIPTRESPONSE']._serialized_end=2872
  _globals['_QUERYPACKETACKNOWLEDGEMENTREQUEST']._serialized_start=2874
  _globals['_QUERYPACKETACKNOWLEDGEMENTREQUEST']._serialized_end=2993
  _globals['_QUERYPACKETACKNOWLEDGEMENTRESPONSE']._serialized_start=2996
  _globals['_QUERYPACKETACKNOWLEDGEMENTRESPONSE']._serialized_end=3165
  _globals['_QUERYPACKETACKNOWLEDGEMENTSREQUEST']._serialized_start=3168
  _globals['_QUERYPACKETACKNOWLEDGEMENTSREQUEST']._serialized_end=3396
  _globals['_QUERYPACKETACKNOWLEDGEMENTSRESPONSE']._serialized_start=3399
  _globals['_QUERYPACKETACKNOWLEDGEMENTSRESPONSE']._serialized_end=3645
  _globals['_QUERYUNRECEIVEDPACKETSREQUEST']._serialized_start=3648
  _globals['_QUERYUNRECEIVEDPACKETSREQUEST']._serialized_end=3799
  _globals['_QUERYUNRECEIVEDPACKETSRESPONSE']._serialized_start=3801
  _globals['_QUERYUNRECEIVEDPACKETSRESPONSE']._serialized_end=3921
  _globals['_QUERYUNRECEIVEDACKSREQUEST']._serialized_start=3924
  _globals['_QUERYUNRECEIVEDACKSREQUEST']._serialized_end=4058
  _globals['_QUERYUNRECEIVEDACKSRESPONSE']._serialized_start=4060
  _globals['_QUERYUNRECEIVEDACKSRESPONSE']._serialized_end=4177
  _globals['_QUERYNEXTSEQUENCERECEIVEREQUEST']._serialized_start=4179
  _globals['_QUERYNEXTSEQUENCERECEIVEREQUEST']._serialized_end=4268
  _globals['_QUERYNEXTSEQUENCERECEIVERESPONSE']._serialized_start=4271
  _globals['_QUERYNEXTSEQUENCERECEIVERESPONSE']._serialized_end=4448
  _globals['_QUERYNEXTSEQUENCESENDREQUEST']._serialized_start=4450
  _globals['_QUERYNEXTSEQUENCESENDREQUEST']._serialized_end=4536
  _globals['_QUERYNEXTSEQUENCESENDRESPONSE']._serialized_start=4539
  _globals['_QUERYNEXTSEQUENCESENDRESPONSE']._serialized_end=4707
  _globals['_QUERYUPGRADEERRORREQUEST']._serialized_start=4709
  _globals['_QUERYUPGRADEERRORREQUEST']._serialized_end=4791
  _globals['_QUERYUPGRADEERRORRESPONSE']._serialized_start=4794
  _globals['_QUERYUPGRADEERRORRESPONSE']._serialized_end=4990
  _globals['_QUERYUPGRADEREQUEST']._serialized_start=4992
  _globals['_QUERYUPGRADEREQUEST']._serialized_end=5069
  _globals['_QUERYUPGRADERESPONSE']._serialized_start=5072
  _globals['_QUERYUPGRADERESPONSE']._serialized_end=5247
  _globals['_QUERYCHANNELPARAMSREQUEST']._serialized_start=5249
  _globals['_QUERYCHANNELPARAMSREQUEST']._serialized_end=5276
  _globals['_QUERYCHANNELPARAMSRESPONSE']._serialized_start=5278
  _globals['_QUERYCHANNELPARAMSRESPONSE']._serialized_end=5359
  _globals['_QUERY']._serialized_start=5362
  _globals['_QUERY']._serialized_end=8919
# @@protoc_insertion_point(module_scope)
