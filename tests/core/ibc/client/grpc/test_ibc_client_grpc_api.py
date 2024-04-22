import base64

import grpc
import pytest
from google.protobuf import any_pb2

from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.ibc.client.ibc_client_grpc_api import IBCClientGrpcApi
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.cosmos.base.query.v1beta1 import pagination_pb2 as pagination_pb
from pyinjective.proto.cosmos.ics23.v1 import proofs_pb2 as ics23_proofs
from pyinjective.proto.ibc.core.client.v1 import client_pb2 as ibc_client, query_pb2 as ibc_client_query
from pyinjective.proto.ibc.core.commitment.v1 import commitment_pb2 as ibc_commitment
from pyinjective.proto.ibc.lightclients.tendermint.v1 import tendermint_pb2 as ibc_tendermint
from tests.core.ibc.client.grpc.configurable_ibc_client_query_servicer import ConfigurableIBCClientQueryServicer


@pytest.fixture
def ibc_client_servicer():
    return ConfigurableIBCClientQueryServicer()


class TestIBCClientGrpcApi:
    @pytest.mark.asyncio
    async def test_fetch_client_state(
        self,
        ibc_client_servicer,
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
        proof = b"proof"
        proof_height = ibc_client.Height(
            revision_number=1,
            revision_height=2,
        )

        ibc_client_servicer.client_state_responses.append(
            ibc_client_query.QueryClientStateResponse(
                client_state=any_client_state,
                proof=proof,
                proof_height=proof_height,
            )
        )

        api = self._api_instance(servicer=ibc_client_servicer)

        result_client_state = await api.fetch_client_state(client_id="client-id")
        expected_client_state = {
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
            "proof": base64.b64encode(proof).decode(),
            "proofHeight": {
                "revisionNumber": str(proof_height.revision_number),
                "revisionHeight": str(proof_height.revision_height),
            },
        }

        result_client_state["clientState"] = dict(result_client_state["clientState"])

        assert result_client_state == expected_client_state

    @pytest.mark.asyncio
    async def test_fetch_client_states(
        self,
        ibc_client_servicer,
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
        client_state = ibc_client.IdentifiedClientState(
            client_id="client-1",
            client_state=any_client_state,
        )
        result_pagination = pagination_pb.PageResponse(
            next_key=b"\001\032\264\007Z\224$]\377s8\343\004-\265\267\314?B\341",
            total=16036,
        )

        ibc_client_servicer.client_states_responses.append(
            ibc_client_query.QueryClientStatesResponse(
                client_states=[client_state],
                pagination=result_pagination,
            )
        )

        api = self._api_instance(servicer=ibc_client_servicer)

        pagination_option = PaginationOption(
            skip=10,
            limit=30,
            reverse=False,
            count_total=True,
        )

        result_client_states = await api.fetch_client_states(pagination=pagination_option)
        expected_client_states = {
            "clientStates": [
                {
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
            ],
            "pagination": {
                "nextKey": base64.b64encode(result_pagination.next_key).decode(),
                "total": str(result_pagination.total),
            },
        }

        assert result_client_states == expected_client_states

    @pytest.mark.asyncio
    async def test_fetch_consensus_state(
        self,
        ibc_client_servicer,
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
        proof = b"proof"
        proof_height = ibc_client.Height(
            revision_number=1,
            revision_height=2,
        )

        ibc_client_servicer.consensus_state_responses.append(
            ibc_client_query.QueryConsensusStateResponse(
                consensus_state=any_consensus_state,
                proof=proof,
                proof_height=proof_height,
            )
        )

        api = self._api_instance(servicer=ibc_client_servicer)

        result_state = await api.fetch_consensus_state(
            client_id="client-id",
            revision_number=1,
            revision_height=2,
            latest_height=False,
        )
        expected_state = {
            "consensusState": {
                "@type": "type.googleapis.com/ibc.lightclients.tendermint.v1.ConsensusState",
                "root": {
                    "hash": base64.b64encode(root.hash).decode(),
                },
                "nextValidatorsHash": base64.b64encode(consensus_state.next_validators_hash).decode(),
            },
            "proof": base64.b64encode(proof).decode(),
            "proofHeight": {
                "revisionNumber": str(proof_height.revision_number),
                "revisionHeight": str(proof_height.revision_height),
            },
        }

        assert result_state == expected_state

    @pytest.mark.asyncio
    async def test_fetch_consensus_states(
        self,
        ibc_client_servicer,
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
        proof_height = ibc_client.Height(
            revision_number=1,
            revision_height=2,
        )

        state_with_height = ibc_client.ConsensusStateWithHeight(
            consensus_state=any_consensus_state,
            height=proof_height,
        )
        result_pagination = pagination_pb.PageResponse(
            next_key=b"\001\032\264\007Z\224$]\377s8\343\004-\265\267\314?B\341",
            total=16036,
        )

        ibc_client_servicer.consensus_states_responses.append(
            ibc_client_query.QueryConsensusStatesResponse(
                consensus_states=[state_with_height],
                pagination=result_pagination,
            )
        )

        api = self._api_instance(servicer=ibc_client_servicer)

        pagination_option = PaginationOption(
            skip=10,
            limit=30,
            reverse=False,
            count_total=True,
        )

        result_states = await api.fetch_consensus_states(
            client_id="client-id",
            pagination=pagination_option,
        )
        expected_states = {
            "consensusStates": [
                {
                    "consensusState": {
                        "@type": "type.googleapis.com/ibc.lightclients.tendermint.v1.ConsensusState",
                        "root": {
                            "hash": base64.b64encode(root.hash).decode(),
                        },
                        "nextValidatorsHash": base64.b64encode(consensus_state.next_validators_hash).decode(),
                    },
                    "height": {
                        "revisionNumber": str(proof_height.revision_number),
                        "revisionHeight": str(proof_height.revision_height),
                    },
                },
            ],
            "pagination": {
                "nextKey": base64.b64encode(result_pagination.next_key).decode(),
                "total": str(result_pagination.total),
            },
        }

        assert result_states == expected_states

    @pytest.mark.asyncio
    async def test_fetch_consensus_state_heights(
        self,
        ibc_client_servicer,
    ):
        height = ibc_client.Height(
            revision_number=1,
            revision_height=2,
        )
        result_pagination = pagination_pb.PageResponse(
            next_key=b"\001\032\264\007Z\224$]\377s8\343\004-\265\267\314?B\341",
            total=16036,
        )

        ibc_client_servicer.consensus_state_heights_responses.append(
            ibc_client_query.QueryConsensusStateHeightsResponse(
                consensus_state_heights=[height],
                pagination=result_pagination,
            )
        )

        api = self._api_instance(servicer=ibc_client_servicer)

        pagination_option = PaginationOption(
            skip=10,
            limit=30,
            reverse=False,
            count_total=True,
        )

        result_heights = await api.fetch_consensus_state_heights(
            client_id="client-id",
            pagination=pagination_option,
        )
        expected_heights = {
            "consensusStateHeights": [
                {
                    "revisionNumber": str(height.revision_number),
                    "revisionHeight": str(height.revision_height),
                },
            ],
            "pagination": {
                "nextKey": base64.b64encode(result_pagination.next_key).decode(),
                "total": str(result_pagination.total),
            },
        }

        assert result_heights == expected_heights

    @pytest.mark.asyncio
    async def test_fetch_client_status(
        self,
        ibc_client_servicer,
    ):
        status = "Expired"

        ibc_client_servicer.client_status_responses.append(ibc_client_query.QueryClientStatusResponse(status=status))

        api = self._api_instance(servicer=ibc_client_servicer)

        result_status = await api.fetch_client_status(
            client_id="client-id",
        )
        expected_status = {"status": status}

        assert result_status == expected_status

    @pytest.mark.asyncio
    async def test_fetch_client_params(
        self,
        ibc_client_servicer,
    ):
        params = ibc_client.Params(
            allowed_clients=["injective-1", "injective-2"],
        )

        ibc_client_servicer.client_params_responses.append(ibc_client_query.QueryClientParamsResponse(params=params))

        api = self._api_instance(servicer=ibc_client_servicer)

        result_params = await api.fetch_client_params()
        expected_params = {
            "params": {
                "allowedClients": params.allowed_clients,
            },
        }

        assert result_params == expected_params

    @pytest.mark.asyncio
    async def test_fetch_upgraded_client_state(
        self,
        ibc_client_servicer,
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

        ibc_client_servicer.upgraded_client_state_responses.append(
            ibc_client_query.QueryUpgradedClientStateResponse(
                upgraded_client_state=any_client_state,
            )
        )

        api = self._api_instance(servicer=ibc_client_servicer)

        result_client_state = await api.fetch_upgraded_client_state()
        expected_client_state = {
            "upgradedClientState": {
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
        }

        result_client_state["upgradedClientState"] = dict(result_client_state["upgradedClientState"])

        assert result_client_state == expected_client_state

    @pytest.mark.asyncio
    async def test_fetch_upgraded_consensus_state(
        self,
        ibc_client_servicer,
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

        ibc_client_servicer.upgraded_consensus_state_responses.append(
            ibc_client_query.QueryUpgradedConsensusStateResponse(
                upgraded_consensus_state=any_consensus_state,
            )
        )

        api = self._api_instance(servicer=ibc_client_servicer)

        result_state = await api.fetch_upgraded_consensus_state()
        expected_state = {
            "upgradedConsensusState": {
                "@type": "type.googleapis.com/ibc.lightclients.tendermint.v1.ConsensusState",
                "root": {
                    "hash": base64.b64encode(root.hash).decode(),
                },
                "nextValidatorsHash": base64.b64encode(consensus_state.next_validators_hash).decode(),
            },
        }

        assert result_state == expected_state

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = IBCClientGrpcApi(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer

        return api
