from collections import deque

from pyinjective.proto.ibc.core.channel.v1 import (
    query_pb2 as ibc_channel_query,
    query_pb2_grpc as ibc_channel_query_grpc,
)


class ConfigurableIBCChannelQueryServicer(ibc_channel_query_grpc.QueryServicer):
    def __init__(self):
        super().__init__()
        self.channel_responses = deque()
        self.channels_responses = deque()
        self.connection_channels_responses = deque()
        self.channel_client_state_responses = deque()
        self.channel_consensus_state_responses = deque()
        self.packet_commitment_responses = deque()
        self.packet_commitments_responses = deque()
        self.packet_receipt_responses = deque()
        self.packet_acknowledgement_responses = deque()
        self.packet_acknowledgements_responses = deque()
        self.unreceived_packets_responses = deque()
        self.unreceived_acks_responses = deque()
        self.next_sequence_receive_responses = deque()

    async def Channel(self, request: ibc_channel_query.QueryChannelRequest, context=None, metadata=None):
        return self.channel_responses.pop()

    async def Channels(self, request: ibc_channel_query.QueryChannelsRequest, context=None, metadata=None):
        return self.channels_responses.pop()

    async def ConnectionChannels(
        self, request: ibc_channel_query.QueryConnectionChannelsRequest, context=None, metadata=None
    ):
        return self.connection_channels_responses.pop()

    async def ChannelClientState(
        self, request: ibc_channel_query.QueryChannelClientStateRequest, context=None, metadata=None
    ):
        return self.channel_client_state_responses.pop()

    async def ChannelConsensusState(
        self, request: ibc_channel_query.QueryChannelConsensusStateRequest, context=None, metadata=None
    ):
        return self.channel_consensus_state_responses.pop()

    async def PacketCommitment(
        self, request: ibc_channel_query.QueryPacketCommitmentRequest, context=None, metadata=None
    ):
        return self.packet_commitment_responses.pop()

    async def PacketCommitments(
        self, request: ibc_channel_query.QueryPacketCommitmentsRequest, context=None, metadata=None
    ):
        return self.packet_commitments_responses.pop()

    async def PacketReceipt(self, request: ibc_channel_query.QueryPacketReceiptRequest, context=None, metadata=None):
        return self.packet_receipt_responses.pop()

    async def PacketAcknowledgement(
        self, request: ibc_channel_query.QueryPacketAcknowledgementRequest, context=None, metadata=None
    ):
        return self.packet_acknowledgement_responses.pop()

    async def PacketAcknowledgements(
        self, request: ibc_channel_query.QueryPacketAcknowledgementsRequest, context=None, metadata=None
    ):
        return self.packet_acknowledgements_responses.pop()

    async def UnreceivedPackets(
        self, request: ibc_channel_query.QueryUnreceivedPacketsRequest, context=None, metadata=None
    ):
        return self.unreceived_packets_responses.pop()

    async def UnreceivedAcks(self, request: ibc_channel_query.QueryUnreceivedAcksRequest, context=None, metadata=None):
        return self.unreceived_acks_responses.pop()

    async def NextSequenceReceive(
        self, request: ibc_channel_query.QueryNextSequenceReceiveRequest, context=None, metadata=None
    ):
        return self.next_sequence_receive_responses.pop()
