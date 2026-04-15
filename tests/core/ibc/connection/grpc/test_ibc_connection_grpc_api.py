import base64

import grpc
import pytest
from google.protobuf import any_pb2

from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.ibc.connection.grpc.ibc_connection_grpc_api import IBCConnectionGrpcApi
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.cosmos.base.query.v1beta1 import pagination_pb2 as pagination_pb
from pyinjective.proto.cosmos.ics23.v1 import proofs_pb2 as ics23_proofs
from pyinjective.proto.ibc.core.client.v1 import client_pb2 as ibc_client
from pyinjective.proto.ibc.core.commitment.v1 import commitment_pb2 as ibc_commitment
from pyinjective.proto.ibc.core.connection.v1 import connection_pb2 as ibc_connection, query_pb2 as ibc_connection_query
from pyinjective.proto.ibc.lightclients.tendermint.v1 import tendermint_pb2 as ibc_tendermint
from tests.core.ibc.connection.grpc.configurable_ibc_connection_query_servicer import (
    ConfigurableIBCConnectionQueryServicer,
)


@pytest.fixture
def ibc_connection_servicer():
    return ConfigurableIBCConnectionQueryServicer()


class TestIBCConnectionGrpcApi:
    @pytest.mark.asyncio
    async def test_fetch_connection(
        self,
        ibc_connection_servicer,
    ):
        version = ibc_connection.Version(
            identifier="connection-0",
            features=["ORDER_ORDERED", "ORDER_UNORDERED"],
        )
        prefix = ibc_commitment.MerklePrefix(key_prefix=b"prefix")
        counterparty = ibc_connection.Counterparty(
            client_id="07-tendermint-0",
            connection_id="connection-0",
            prefix=prefix,
        )
        connection = ibc_connection.ConnectionEnd(
            client_id="07-tendermint-0",
            versions=[version],
            state=3,
            counterparty=counterparty,
            delay_period=5,
        )
        proof = b"proof"
        proof_height = ibc_client.Height(
            revision_number=1,
            revision_height=2,
        )

        ibc_connection_servicer.connection_responses.append(
            ibc_connection_query.QueryConnectionResponse(
                connection=connection,
                proof=proof,
                proof_height=proof_height,
            )
        )

        api = self._api_instance(servicer=ibc_connection_servicer)

        result_connection = await api.fetch_connection(connection_id=counterparty.connection_id)
        expected_connection = {
            "connection": {
                "clientId": connection.client_id,
                "versions": [{"identifier": version.identifier, "features": version.features}],
                "state": ibc_connection.State.Name(connection.state),
                "counterparty": {
                    "clientId": counterparty.client_id,
                    "connectionId": counterparty.connection_id,
                    "prefix": {"keyPrefix": base64.b64encode(prefix.key_prefix).decode()},
                },
                "delayPeriod": str(connection.delay_period),
            },
            "proof": base64.b64encode(proof).decode(),
            "proofHeight": {
                "revisionNumber": str(proof_height.revision_number),
                "revisionHeight": str(proof_height.revision_height),
            },
        }

        assert result_connection == expected_connection

    @pytest.mark.asyncio
    async def test_fetch_connections(
        self,
        ibc_connection_servicer,
    ):
        version = ibc_connection.Version(
            identifier="connection-0",
            features=["ORDER_ORDERED", "ORDER_UNORDERED"],
        )
        prefix = ibc_commitment.MerklePrefix(key_prefix=b"prefix")
        counterparty = ibc_connection.Counterparty(
            client_id="07-tendermint-0",
            connection_id="connection-0",
            prefix=prefix,
        )
        connection = ibc_connection.IdentifiedConnection(
            id="connection-0",
            client_id="07-tendermint-0",
            versions=[version],
            state=3,
            counterparty=counterparty,
            delay_period=5,
        )
        height = ibc_client.Height(
            revision_number=1,
            revision_height=2,
        )
        result_pagination = pagination_pb.PageResponse(
            next_key=b"\001\032\264\007Z\224$]\377s8\343\004-\265\267\314?B\341",
            total=16036,
        )

        ibc_connection_servicer.connections_responses.append(
            ibc_connection_query.QueryConnectionsResponse(
                connections=[connection],
                pagination=result_pagination,
                height=height,
            )
        )

        api = self._api_instance(servicer=ibc_connection_servicer)

        pagination_option = PaginationOption(
            skip=10,
            limit=30,
            reverse=False,
            count_total=True,
        )

        result_connections = await api.fetch_connections(pagination=pagination_option)
        expected_connections = {
            "connections": [
                {
                    "id": connection.id,
                    "clientId": connection.client_id,
                    "versions": [{"identifier": version.identifier, "features": version.features}],
                    "state": ibc_connection.State.Name(connection.state),
                    "counterparty": {
                        "clientId": counterparty.client_id,
                        "connectionId": counterparty.connection_id,
                        "prefix": {"keyPrefix": base64.b64encode(prefix.key_prefix).decode()},
                    },
                    "delayPeriod": str(connection.delay_period),
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

        assert result_connections == expected_connections

    @pytest.mark.asyncio
    async def test_fetch_client_connections(
        self,
        ibc_connection_servicer,
    ):
        connection_path = "connection path"
        proof = b"proof"
        proof_height = ibc_client.Height(
            revision_number=1,
            revision_height=2,
        )

        ibc_connection_servicer.client_connections_responses.append(
            ibc_connection_query.QueryClientConnectionsResponse(
                connection_paths=[connection_path],
                proof=proof,
                proof_height=proof_height,
            )
        )

        api = self._api_instance(servicer=ibc_connection_servicer)

        result_connection = await api.fetch_client_connections(client_id="07-tendermint-0")
        expected_connection = {
            "connectionPaths": [connection_path],
            "proof": base64.b64encode(proof).decode(),
            "proofHeight": {
                "revisionNumber": str(proof_height.revision_number),
                "revisionHeight": str(proof_height.revision_height),
            },
        }

        assert result_connection == expected_connection

    @pytest.mark.asyncio
    async def test_fetch_connection_client_state(
        self,
        ibc_connection_servicer,
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
        identified_client_state = ibc_client.IdentifiedClientState(
            client_id="07-tendermint-0",
            client_state=any_client_state,
        )
        proof = b"proof"
        proof_height = ibc_client.Height(
            revision_number=1,
            revision_height=2,
        )

        ibc_connection_servicer.connection_client_state_responses.append(
            ibc_connection_query.QueryConnectionClientStateResponse(
                identified_client_state=identified_client_state,
                proof=proof,
                proof_height=proof_height,
            )
        )

        api = self._api_instance(servicer=ibc_connection_servicer)

        result_state = await api.fetch_connection_client_state(connection_id="connection-0")
        expected_state = {
            "identifiedClientState": {
                "clientId": identified_client_state.client_id,
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

        result_state["identifiedClientState"] = dict(result_state["identifiedClientState"])

        assert result_state == expected_state

    @pytest.mark.asyncio
    async def test_fetch_connection_consensus_state(
        self,
        ibc_connection_servicer,
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
        client_id = "07-tendermint-0"
        proof = b"proof"
        proof_height = ibc_client.Height(
            revision_number=1,
            revision_height=2,
        )

        ibc_connection_servicer.connection_consensus_state_responses.append(
            ibc_connection_query.QueryConnectionConsensusStateResponse(
                consensus_state=any_consensus_state,
                client_id=client_id,
                proof=proof,
                proof_height=proof_height,
            )
        )

        api = self._api_instance(servicer=ibc_connection_servicer)

        result_state = await api.fetch_connection_consensus_state(
            connection_id="connection-0",
            revision_number=proof_height.revision_number,
            revision_height=proof_height.revision_height,
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

        result_state["consensusState"] = dict(result_state["consensusState"])

        assert result_state == expected_state

    @pytest.mark.asyncio
    async def test_fetch_connection_params(
        self,
        ibc_connection_servicer,
    ):
        params = ibc_connection.Params(
            max_expected_time_per_block=30000000000,
        )

        ibc_connection_servicer.connection_params_responses.append(
            ibc_connection_query.QueryConnectionParamsResponse(
                params=params,
            )
        )

        api = self._api_instance(servicer=ibc_connection_servicer)

        result_params = await api.fetch_connection_params()
        expected_params = {
            "params": {
                "maxExpectedTimePerBlock": str(params.max_expected_time_per_block),
            },
        }

        assert result_params == expected_params

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = IBCConnectionGrpcApi(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer

        return api
