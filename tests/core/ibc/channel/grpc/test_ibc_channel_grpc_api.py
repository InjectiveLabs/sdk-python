import base64

import grpc
import pytest
from google.protobuf import any_pb2

from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.ibc.channel.grpc.ibc_channel_grpc_api import IBCChannelGrpcApi
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.cosmos.base.query.v1beta1 import pagination_pb2 as pagination_pb
from pyinjective.proto.cosmos.ics23.v1 import proofs_pb2 as ics23_proofs
from pyinjective.proto.ibc.core.channel.v1 import channel_pb2 as ibc_channel, query_pb2 as ibc_channel_query
from pyinjective.proto.ibc.core.client.v1 import client_pb2 as ibc_client
from pyinjective.proto.ibc.core.commitment.v1 import commitment_pb2 as ibc_commitment
from pyinjective.proto.ibc.lightclients.tendermint.v1 import tendermint_pb2 as ibc_tendermint
from tests.core.ibc.channel.grpc.configurable_ibc_channel_query_servicer import ConfigurableIBCChannelQueryServicer


@pytest.fixture
def ibc_channel_servicer():
    return ConfigurableIBCChannelQueryServicer()


class TestIBCChannelGrpcApi:
    @pytest.mark.asyncio
    async def test_fetch_channel(
        self,
        ibc_channel_servicer,
    ):
        counterparty = ibc_channel.Counterparty(
            port_id="transfer",
            channel_id="channel-126",
        )
        connection_hop = "connection-182"
        version = (
            '{"version":"ics27-1","controller_connection_id":"connection-9",'
            '"host_connection_id":"connection-182",'
            '"address":"inj1urqc59ft3hl75mxhru4848xusu5rhpghz48zdfypyuu923w2gzyqm8y02d","encoding":"proto3",'
            '"tx_type":"sdk_multi_msg"}'
        )
        channel = ibc_channel.Channel(
            state=3,
            ordering=1,
            counterparty=counterparty,
            connection_hops=[connection_hop],
            version=version,
        )
        proof = b"proof"
        proof_height = ibc_client.Height(
            revision_number=1,
            revision_height=2,
        )

        ibc_channel_servicer.channel_responses.append(
            ibc_channel_query.QueryChannelResponse(
                channel=channel,
                proof=proof,
                proof_height=proof_height,
            )
        )

        api = self._api_instance(servicer=ibc_channel_servicer)

        result_channel = await api.fetch_channel(port_id=counterparty.port_id, channel_id=counterparty.channel_id)
        expected_channel = {
            "channel": {
                "state": ibc_channel.State.Name(channel.state),
                "ordering": ibc_channel.Order.Name(channel.ordering),
                "counterparty": {
                    "portId": counterparty.port_id,
                    "channelId": counterparty.channel_id,
                },
                "connectionHops": [connection_hop],
                "version": version,
            },
            "proof": base64.b64encode(proof).decode(),
            "proofHeight": {
                "revisionNumber": str(proof_height.revision_number),
                "revisionHeight": str(proof_height.revision_height),
            },
        }

        assert result_channel == expected_channel

    @pytest.mark.asyncio
    async def test_fetch_channels(
        self,
        ibc_channel_servicer,
    ):
        counterparty = ibc_channel.Counterparty(
            port_id="transfer",
            channel_id="channel-126",
        )
        connection_hop = "connection-182"
        version = (
            '{"version":"ics27-1","controller_connection_id":"connection-9",'
            '"host_connection_id":"connection-182",'
            '"address":"inj1urqc59ft3hl75mxhru4848xusu5rhpghz48zdfypyuu923w2gzyqm8y02d","encoding":"proto3",'
            '"tx_type":"sdk_multi_msg"}'
        )
        port_id = "wasm.xion18pmp7n2j6a84dkmuqlc7lwp2pgr0gg3ssmvrm8vgjuy2vs66e4usm2w3ln"
        channel_id = "channel-34"
        channel = ibc_channel.IdentifiedChannel(
            state=3,
            ordering=1,
            counterparty=counterparty,
            connection_hops=[connection_hop],
            version=version,
            port_id=port_id,
            channel_id=channel_id,
        )
        height = ibc_client.Height(
            revision_number=1,
            revision_height=2,
        )
        result_pagination = pagination_pb.PageResponse(
            next_key=b"\001\032\264\007Z\224$]\377s8\343\004-\265\267\314?B\341",
            total=16036,
        )

        ibc_channel_servicer.channels_responses.append(
            ibc_channel_query.QueryChannelsResponse(
                channels=[channel],
                pagination=result_pagination,
                height=height,
            )
        )

        api = self._api_instance(servicer=ibc_channel_servicer)

        pagination_option = PaginationOption(
            skip=10,
            limit=30,
            reverse=False,
            count_total=True,
        )

        result_channels = await api.fetch_channels(pagination=pagination_option)
        expected_channels = {
            "channels": [
                {
                    "state": ibc_channel.State.Name(channel.state),
                    "ordering": ibc_channel.Order.Name(channel.ordering),
                    "counterparty": {
                        "portId": counterparty.port_id,
                        "channelId": counterparty.channel_id,
                    },
                    "connectionHops": [connection_hop],
                    "version": version,
                    "portId": port_id,
                    "channelId": channel_id,
                },
            ],
            "pagination": {
                "nextKey": base64.b64encode(result_pagination.next_key).decode(),
                "total": str(result_pagination.total),
            },
            "height": {
                "revisionNumber": str(height.revision_number),
                "revisionHeight": str(height.revision_height),
            },
        }

        assert result_channels == expected_channels

    @pytest.mark.asyncio
    async def test_fetch_connection_channels(
        self,
        ibc_channel_servicer,
    ):
        counterparty = ibc_channel.Counterparty(
            port_id="transfer",
            channel_id="channel-126",
        )
        connection_hop = "connection-182"
        version = (
            '{"version":"ics27-1","controller_connection_id":"connection-9",'
            '"host_connection_id":"connection-182",'
            '"address":"inj1urqc59ft3hl75mxhru4848xusu5rhpghz48zdfypyuu923w2gzyqm8y02d","encoding":"proto3",'
            '"tx_type":"sdk_multi_msg"}'
        )
        port_id = "wasm.xion18pmp7n2j6a84dkmuqlc7lwp2pgr0gg3ssmvrm8vgjuy2vs66e4usm2w3ln"
        channel_id = "channel-34"
        channel = ibc_channel.IdentifiedChannel(
            state=3,
            ordering=1,
            counterparty=counterparty,
            connection_hops=[connection_hop],
            version=version,
            port_id=port_id,
            channel_id=channel_id,
        )
        height = ibc_client.Height(
            revision_number=1,
            revision_height=2,
        )
        result_pagination = pagination_pb.PageResponse(
            next_key=b"\001\032\264\007Z\224$]\377s8\343\004-\265\267\314?B\341",
            total=16036,
        )

        ibc_channel_servicer.connection_channels_responses.append(
            ibc_channel_query.QueryConnectionChannelsResponse(
                channels=[channel],
                pagination=result_pagination,
                height=height,
            )
        )

        api = self._api_instance(servicer=ibc_channel_servicer)

        pagination_option = PaginationOption(
            skip=10,
            limit=30,
            reverse=False,
            count_total=True,
        )

        result_channels = await api.fetch_connection_channels(connection=connection_hop, pagination=pagination_option)
        expected_channels = {
            "channels": [
                {
                    "state": ibc_channel.State.Name(channel.state),
                    "ordering": ibc_channel.Order.Name(channel.ordering),
                    "counterparty": {
                        "portId": counterparty.port_id,
                        "channelId": counterparty.channel_id,
                    },
                    "connectionHops": [connection_hop],
                    "version": version,
                    "portId": port_id,
                    "channelId": channel_id,
                },
            ],
            "pagination": {
                "nextKey": base64.b64encode(result_pagination.next_key).decode(),
                "total": str(result_pagination.total),
            },
            "height": {
                "revisionNumber": str(height.revision_number),
                "revisionHeight": str(height.revision_height),
            },
        }

        assert result_channels == expected_channels

    @pytest.mark.asyncio
    async def test_fetch_connection_client_state(
        self,
        ibc_channel_servicer,
    ):
        trust_level = ibc_tendermint.Fraction(
            numerator=1,
            denominator=3,
        )
        leaf_spec = ics23_proofs.LeafOp(
            hash=0,
            prehash_key=1,
            prehash_value=2,
            length=3,
            prefix=b"prefix",
        )
        inner_spec = ics23_proofs.InnerSpec(
            child_order=[0, 1, 2, 3],
            child_size=4,
            min_prefix_length=5,
            max_prefix_length=6,
            empty_child=b"empty",
            hash=1,
        )
        proof_spec = ics23_proofs.ProofSpec(
            leaf_spec=leaf_spec,
            inner_spec=inner_spec,
            max_depth=5,
            min_depth=1,
            prehash_key_before_comparison=True,
        )
        tendermint_client_state = ibc_tendermint.ClientState(
            chain_id="injective-1",
            trust_level=trust_level,
            # trusting_period="10s",
            # unbonding_period="20s",
            # max_clock_drift="1s",
            frozen_height=ibc_client.Height(
                revision_number=1,
                revision_height=2,
            ),
            latest_height=ibc_client.Height(
                revision_number=3,
                revision_height=4,
            ),
            proof_specs=[proof_spec],
            upgrade_path=["upgrade", "upgradedIBCState"],
            allow_update_after_expiry=False,
            allow_update_after_misbehaviour=False,
        )
        any_client_state = any_pb2.Any()
        any_client_state.Pack(tendermint_client_state)
        client_state = ibc_client.IdentifiedClientState(
            client_id="client-1",
            client_state=any_client_state,
        )
        proof = b"proof"
        proof_height = ibc_client.Height(
            revision_number=1,
            revision_height=2,
        )

        ibc_channel_servicer.channel_client_state_responses.append(
            ibc_channel_query.QueryChannelClientStateResponse(
                identified_client_state=client_state,
                proof=proof,
                proof_height=proof_height,
            )
        )

        api = self._api_instance(servicer=ibc_channel_servicer)

        result_client_state = await api.fetch_channel_client_state(
            port_id="icahost",
            channel_id="channel-1",
        )
        expected_client_state = {
            "identifiedClientState": {
                "clientId": client_state.client_id,
                "clientState": {
                    "@type": "type.googleapis.com/ibc.lightclients.tendermint.v1.ClientState",
                    "chainId": tendermint_client_state.chain_id,
                    "trustLevel": {
                        "numerator": str(trust_level.numerator),
                        "denominator": str(trust_level.denominator),
                    },
                    "frozenHeight": {
                        "revisionNumber": str(tendermint_client_state.frozen_height.revision_number),
                        "revisionHeight": str(tendermint_client_state.frozen_height.revision_height),
                    },
                    "latestHeight": {
                        "revisionNumber": str(tendermint_client_state.latest_height.revision_number),
                        "revisionHeight": str(tendermint_client_state.latest_height.revision_height),
                    },
                    "proofSpecs": [
                        {
                            "leafSpec": {
                                "hash": ics23_proofs.HashOp.Name(leaf_spec.hash),
                                "prehashKey": ics23_proofs.HashOp.Name(leaf_spec.prehash_key),
                                "prehashValue": ics23_proofs.HashOp.Name(leaf_spec.prehash_value),
                                "length": ics23_proofs.LengthOp.Name(leaf_spec.length),
                                "prefix": base64.b64encode(leaf_spec.prefix).decode(),
                            },
                            "innerSpec": {
                                "childOrder": inner_spec.child_order,
                                "childSize": inner_spec.child_size,
                                "minPrefixLength": inner_spec.min_prefix_length,
                                "maxPrefixLength": inner_spec.max_prefix_length,
                                "emptyChild": base64.b64encode(inner_spec.empty_child).decode(),
                                "hash": ics23_proofs.HashOp.Name(inner_spec.hash),
                            },
                            "maxDepth": proof_spec.max_depth,
                            "minDepth": proof_spec.min_depth,
                            "prehashKeyBeforeComparison": proof_spec.prehash_key_before_comparison,
                        },
                    ],
                    "upgradePath": tendermint_client_state.upgrade_path,
                    "allowUpdateAfterExpiry": tendermint_client_state.allow_update_after_expiry,
                    "allowUpdateAfterMisbehaviour": tendermint_client_state.allow_update_after_misbehaviour,
                },
            },
            "proof": base64.b64encode(proof).decode(),
            "proofHeight": {
                "revisionNumber": str(proof_height.revision_number),
                "revisionHeight": str(proof_height.revision_height),
            },
        }

        result_client_state["identifiedClientState"]["clientState"] = dict(
            result_client_state["identifiedClientState"]["clientState"]
        )

        assert result_client_state == expected_client_state

    @pytest.mark.asyncio
    async def test_fetch_channel_consensus_state(
        self,
        ibc_channel_servicer,
    ):
        root = ibc_commitment.MerkleRoot(
            hash=b"root",
        )
        consensus_state = ibc_tendermint.ConsensusState(
            root=root,
            next_validators_hash=b"next_validators_hash",
        )
        any_consensus_state = any_pb2.Any()
        any_consensus_state.Pack(consensus_state)
        client_id = "client-1"
        proof = b"proof"
        proof_height = ibc_client.Height(
            revision_number=1,
            revision_height=2,
        )

        ibc_channel_servicer.channel_consensus_state_responses.append(
            ibc_channel_query.QueryChannelConsensusStateResponse(
                consensus_state=any_consensus_state,
                client_id=client_id,
                proof=proof,
                proof_height=proof_height,
            )
        )

        api = self._api_instance(servicer=ibc_channel_servicer)

        result_state = await api.fetch_channel_consensus_state(
            port_id="icahost",
            channel_id="channel-1",
            revision_number=1,
            revision_height=2,
        )
        expected_state = {
            "consensusState": {
                "@type": "type.googleapis.com/ibc.lightclients.tendermint.v1.ConsensusState",
                "root": {
                    "hash": base64.b64encode(root.hash).decode(),
                },
                "nextValidatorsHash": base64.b64encode(consensus_state.next_validators_hash).decode(),
            },
            "clientId": client_id,
            "proof": base64.b64encode(proof).decode(),
            "proofHeight": {
                "revisionNumber": str(proof_height.revision_number),
                "revisionHeight": str(proof_height.revision_height),
            },
        }

        assert result_state == expected_state

    @pytest.mark.asyncio
    async def test_fetch_packet_commitment(
        self,
        ibc_channel_servicer,
    ):
        commitment = b"commitment"
        proof = b"proof"
        proof_height = ibc_client.Height(
            revision_number=1,
            revision_height=2,
        )

        ibc_channel_servicer.packet_commitment_responses.append(
            ibc_channel_query.QueryPacketCommitmentResponse(
                commitment=commitment,
                proof=proof,
                proof_height=proof_height,
            )
        )

        api = self._api_instance(servicer=ibc_channel_servicer)

        result_commitment = await api.fetch_packet_commitment(
            port_id="icahost",
            channel_id="channel-1",
            sequence=1,
        )
        expected_commitment = {
            "commitment": base64.b64encode(commitment).decode(),
            "proof": base64.b64encode(proof).decode(),
            "proofHeight": {
                "revisionNumber": str(proof_height.revision_number),
                "revisionHeight": str(proof_height.revision_height),
            },
        }

        assert result_commitment == expected_commitment

    @pytest.mark.asyncio
    async def test_fetch_packet_commitments(
        self,
        ibc_channel_servicer,
    ):
        packet_state = ibc_channel.PacketState(
            port_id="transfer",
            channel_id="channel-126",
            sequence=1,
            data=b"data",
        )
        result_pagination = pagination_pb.PageResponse(
            next_key=b"\001\032\264\007Z\224$]\377s8\343\004-\265\267\314?B\341",
            total=16036,
        )
        height = ibc_client.Height(
            revision_number=1,
            revision_height=2,
        )

        ibc_channel_servicer.packet_commitments_responses.append(
            ibc_channel_query.QueryPacketCommitmentsResponse(
                commitments=[packet_state],
                pagination=result_pagination,
                height=height,
            )
        )

        api = self._api_instance(servicer=ibc_channel_servicer)

        pagination_option = PaginationOption(
            skip=10,
            limit=30,
            reverse=False,
            count_total=True,
        )

        result_commitments = await api.fetch_packet_commitments(
            port_id="icahost",
            channel_id="channel-1",
            pagination=pagination_option,
        )
        expected_commitments = {
            "commitments": [
                {
                    "portId": packet_state.port_id,
                    "channelId": packet_state.channel_id,
                    "sequence": str(packet_state.sequence),
                    "data": base64.b64encode(packet_state.data).decode(),
                }
            ],
            "height": {
                "revisionNumber": str(height.revision_number),
                "revisionHeight": str(height.revision_height),
            },
            "pagination": {
                "nextKey": base64.b64encode(result_pagination.next_key).decode(),
                "total": str(result_pagination.total),
            },
        }

        assert result_commitments == expected_commitments

    @pytest.mark.asyncio
    async def test_fetch_packet_receipt(
        self,
        ibc_channel_servicer,
    ):
        received = True
        proof = b"proof"
        proof_height = ibc_client.Height(
            revision_number=1,
            revision_height=2,
        )

        ibc_channel_servicer.packet_receipt_responses.append(
            ibc_channel_query.QueryPacketReceiptResponse(
                received=received,
                proof=proof,
                proof_height=proof_height,
            )
        )

        api = self._api_instance(servicer=ibc_channel_servicer)

        result_receipt = await api.fetch_packet_receipt(
            port_id="icahost",
            channel_id="channel-1",
            sequence=1,
        )
        expected_receipt = {
            "received": received,
            "proof": base64.b64encode(proof).decode(),
            "proofHeight": {
                "revisionNumber": str(proof_height.revision_number),
                "revisionHeight": str(proof_height.revision_height),
            },
        }

        assert result_receipt == expected_receipt

    @pytest.mark.asyncio
    async def test_fetch_packet_acknowledgement(
        self,
        ibc_channel_servicer,
    ):
        acknowledgement = b"acknowledgement"
        proof = b"proof"
        proof_height = ibc_client.Height(
            revision_number=1,
            revision_height=2,
        )

        ibc_channel_servicer.packet_acknowledgement_responses.append(
            ibc_channel_query.QueryPacketAcknowledgementResponse(
                acknowledgement=acknowledgement,
                proof=proof,
                proof_height=proof_height,
            )
        )

        api = self._api_instance(servicer=ibc_channel_servicer)

        result_acknowledgement = await api.fetch_packet_acknowledgement(
            port_id="icahost",
            channel_id="channel-1",
            sequence=1,
        )
        expected_acknowledgement = {
            "acknowledgement": base64.b64encode(acknowledgement).decode(),
            "proof": base64.b64encode(proof).decode(),
            "proofHeight": {
                "revisionNumber": str(proof_height.revision_number),
                "revisionHeight": str(proof_height.revision_height),
            },
        }

        assert result_acknowledgement == expected_acknowledgement

    @pytest.mark.asyncio
    async def test_fetch_packet_acknowledgements(
        self,
        ibc_channel_servicer,
    ):
        packet_state = ibc_channel.PacketState(
            port_id="transfer",
            channel_id="channel-126",
            sequence=1,
            data=b"data",
        )
        result_pagination = pagination_pb.PageResponse(
            next_key=b"\001\032\264\007Z\224$]\377s8\343\004-\265\267\314?B\341",
            total=16036,
        )
        height = ibc_client.Height(
            revision_number=1,
            revision_height=2,
        )

        ibc_channel_servicer.packet_acknowledgements_responses.append(
            ibc_channel_query.QueryPacketAcknowledgementsResponse(
                acknowledgements=[packet_state],
                pagination=result_pagination,
                height=height,
            )
        )

        api = self._api_instance(servicer=ibc_channel_servicer)

        pagination_option = PaginationOption(
            skip=10,
            limit=30,
            reverse=False,
            count_total=True,
        )

        result_acknowledgement = await api.fetch_packet_acknowledgements(
            port_id="icahost",
            channel_id="channel-1",
            packet_commitment_sequences=[1, 2],
            pagination=pagination_option,
        )
        expected_acknowledgement = {
            "acknowledgements": [
                {
                    "portId": packet_state.port_id,
                    "channelId": packet_state.channel_id,
                    "sequence": str(packet_state.sequence),
                    "data": base64.b64encode(packet_state.data).decode(),
                }
            ],
            "pagination": {
                "nextKey": base64.b64encode(result_pagination.next_key).decode(),
                "total": str(result_pagination.total),
            },
            "height": {
                "revisionNumber": str(height.revision_number),
                "revisionHeight": str(height.revision_height),
            },
        }

        assert result_acknowledgement == expected_acknowledgement

    @pytest.mark.asyncio
    async def test_fetch_unreceived_packets(
        self,
        ibc_channel_servicer,
    ):
        sequences = [1, 2]
        height = ibc_client.Height(
            revision_number=1,
            revision_height=2,
        )

        ibc_channel_servicer.unreceived_packets_responses.append(
            ibc_channel_query.QueryUnreceivedPacketsResponse(
                sequences=sequences,
                height=height,
            )
        )

        api = self._api_instance(servicer=ibc_channel_servicer)

        result_packets = await api.fetch_unreceived_packets(
            port_id="icahost",
            channel_id="channel-1",
            packet_commitment_sequences=[1, 2],
        )
        expected_packets = {
            "sequences": [str(sequence) for sequence in sequences],
            "height": {
                "revisionNumber": str(height.revision_number),
                "revisionHeight": str(height.revision_height),
            },
        }

        assert result_packets == expected_packets

    @pytest.mark.asyncio
    async def test_fetch_unreceived_acks(
        self,
        ibc_channel_servicer,
    ):
        sequences = [1, 2]
        height = ibc_client.Height(
            revision_number=1,
            revision_height=2,
        )

        ibc_channel_servicer.unreceived_acks_responses.append(
            ibc_channel_query.QueryUnreceivedAcksResponse(
                sequences=sequences,
                height=height,
            )
        )

        api = self._api_instance(servicer=ibc_channel_servicer)

        result_packets = await api.fetch_unreceived_acks(
            port_id="icahost",
            channel_id="channel-1",
            packet_ack_sequences=[1, 2],
        )
        expected_packets = {
            "sequences": [str(sequence) for sequence in sequences],
            "height": {
                "revisionNumber": str(height.revision_number),
                "revisionHeight": str(height.revision_height),
            },
        }

        assert result_packets == expected_packets

    @pytest.mark.asyncio
    async def test_fetch_next_sequence_receive(
        self,
        ibc_channel_servicer,
    ):
        next_sequence_receive = 21
        proof = b"proof"
        proof_height = ibc_client.Height(
            revision_number=1,
            revision_height=2,
        )

        ibc_channel_servicer.next_sequence_receive_responses.append(
            ibc_channel_query.QueryNextSequenceReceiveResponse(
                next_sequence_receive=next_sequence_receive,
                proof=proof,
                proof_height=proof_height,
            )
        )

        api = self._api_instance(servicer=ibc_channel_servicer)

        result_sequence = await api.fetch_next_sequence_receive(
            port_id="icahost",
            channel_id="channel-1",
        )
        expected_sequence = {
            "nextSequenceReceive": str(next_sequence_receive),
            "proof": base64.b64encode(proof).decode(),
            "proofHeight": {
                "revisionNumber": str(proof_height.revision_number),
                "revisionHeight": str(proof_height.revision_height),
            },
        }

        assert result_sequence == expected_sequence

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = IBCChannelGrpcApi(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer

        return api
