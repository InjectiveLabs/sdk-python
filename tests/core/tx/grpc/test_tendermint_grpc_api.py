import base64

import grpc
import pytest

from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network
from pyinjective.core.tx.grpc.tenderming_grpc_api import TendermintGrpcApi
from pyinjective.proto.cosmos.base.query.v1beta1 import pagination_pb2 as pagination_pb
from pyinjective.proto.cosmos.base.tendermint.v1beta1 import query_pb2 as tendermint_query
from pyinjective.proto.tendermint.p2p import types_pb2 as tendermint_p2p_types
from pyinjective.proto.tendermint.types import types_pb2 as tendermint_types
from tests.core.tx.grpc.configurable_tendermint_query_servicer import ConfigurableTendermintQueryServicer


@pytest.fixture
def tendermint_servicer():
    return ConfigurableTendermintQueryServicer()


class TestTxGrpcApi:
    @pytest.mark.asyncio
    async def test_fetch_node_info(
        self,
        tendermint_servicer,
    ):
        protocol_version = tendermint_p2p_types.ProtocolVersion(
            p2p=7,
            block=10,
            app=0,
        )
        other = tendermint_p2p_types.DefaultNodeInfoOther(
            tx_index="on",
            rpc_address="tcp://0.0.0.0:26657",
        )
        node_info = tendermint_p2p_types.DefaultNodeInfo(
            protocol_version=protocol_version,
            default_node_id="dda2a9ee6dc43955d0942be709a16a301f7ba318",
            listen_addr="tcp://0.0.0.0:26656",
            network="injective-1",
            version="0.34.13",
            channels="channels".encode(),
            moniker="injective",
            other=other,
        )
        module = tendermint_query.Module(
            path="cloud.google.com/go",
            version="v0.110.4",
            sum="h1:1JYyxKMN9hd5dR2MYTPWkGUgcoxVVhg0LKNKEo0qvmk=",
        )
        application_version = tendermint_query.VersionInfo(
            name="injective",
            app_name="injectived",
            version="0.0.1",
            git_commit="1f0a39381",
            build_tags="netgo,ledger",
            go_version="go version go1.19.13 linux/amd64",
            build_deps=[module],
            cosmos_sdk_version="v0.47.5",
        )

        tendermint_servicer.get_node_info_responses.append(
            tendermint_query.GetNodeInfoResponse(
                default_node_info=node_info,
                application_version=application_version,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = TendermintGrpcApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = tendermint_servicer

        result_info = await api.fetch_node_info()
        expected_info = {
            "defaultNodeInfo": {
                "protocolVersion": {
                    "p2p": str(protocol_version.p2p),
                    "block": str(protocol_version.block),
                    "app": str(protocol_version.app),
                },
                "defaultNodeId": node_info.default_node_id,
                "listenAddr": node_info.listen_addr,
                "network": node_info.network,
                "version": node_info.version,
                "channels": base64.b64encode(node_info.channels).decode(),
                "moniker": node_info.moniker,
                "other": {
                    "txIndex": other.tx_index,
                    "rpcAddress": other.rpc_address,
                },
            },
            "applicationVersion": {
                "name": application_version.name,
                "appName": application_version.app_name,
                "version": application_version.version,
                "gitCommit": application_version.git_commit,
                "buildTags": application_version.build_tags,
                "goVersion": application_version.go_version,
                "buildDeps": [
                    {
                        "path": module.path,
                        "version": module.version,
                        "sum": module.sum,
                    }
                ],
                "cosmosSdkVersion": application_version.cosmos_sdk_version,
            },
        }

        assert result_info == expected_info

    @pytest.mark.asyncio
    async def test_fetch_syncing(
        self,
        tendermint_servicer,
    ):
        response = tendermint_query.GetSyncingResponse(
            syncing=True,
        )

        tendermint_servicer.get_syncing_responses.append(response)

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = TendermintGrpcApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = tendermint_servicer

        result_syncing = await api.fetch_syncing()
        expected_syncing = {
            "syncing": response.syncing,
        }

        assert result_syncing == expected_syncing

    @pytest.mark.asyncio
    async def test_fetch_latest_block(
        self,
        tendermint_servicer,
    ):
        block_id = tendermint_types.BlockID(
            hash="bdc7f6e819864a8fd050dd4494dd560c1a1519fba3383dfabbec0ea271a34979".encode(),
            part_set_header=tendermint_types.PartSetHeader(
                total=1,
                hash="859e00bfb56409cc182a308bd72d0816e24d57f18fe5f2c5748111daaeb19fbd".encode(),
            ),
        )

        tendermint_servicer.get_latest_block_responses.append(
            tendermint_query.GetLatestBlockResponse(
                block_id=block_id,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = TendermintGrpcApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = tendermint_servicer

        result_block = await api.fetch_latest_block()
        expected_block = {
            "blockId": {
                "hash": base64.b64encode(block_id.hash).decode(),
                "partSetHeader": {
                    "total": block_id.part_set_header.total,
                    "hash": base64.b64encode(block_id.part_set_header.hash).decode(),
                },
            },
        }

        assert result_block == expected_block

    @pytest.mark.asyncio
    async def test_fetch_block_by_height(
        self,
        tendermint_servicer,
    ):
        block_id = tendermint_types.BlockID(
            hash="bdc7f6e819864a8fd050dd4494dd560c1a1519fba3383dfabbec0ea271a34979".encode(),
            part_set_header=tendermint_types.PartSetHeader(
                total=1,
                hash="859e00bfb56409cc182a308bd72d0816e24d57f18fe5f2c5748111daaeb19fbd".encode(),
            ),
        )

        tendermint_servicer.get_block_by_height_responses.append(
            tendermint_query.GetBlockByHeightResponse(
                block_id=block_id,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = TendermintGrpcApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = tendermint_servicer

        result_block = await api.fetch_block_by_height(height=1)
        expected_block = {
            "blockId": {
                "hash": base64.b64encode(block_id.hash).decode(),
                "partSetHeader": {
                    "total": block_id.part_set_header.total,
                    "hash": base64.b64encode(block_id.part_set_header.hash).decode(),
                },
            },
        }

        assert result_block == expected_block

    @pytest.mark.asyncio
    async def test_fetch_latest_validator_set(
        self,
        tendermint_servicer,
    ):
        block_height = 1
        validator = tendermint_query.Validator(
            address="inj1xml3ew93xmjtuf5zwpcl9jzznphte30hvdre9a",
            voting_power=10,
            proposer_priority=1,
        )
        result_pagination = pagination_pb.PageResponse(
            next_key=b"\001\032\264\007Z\224$]\377s8\343\004-\265\267\314?B\341",
            total=16036,
        )
        tendermint_servicer.get_latest_validator_set_responses.append(
            tendermint_query.GetLatestValidatorSetResponse(
                block_height=block_height,
                validators=[validator],
                pagination=result_pagination,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = TendermintGrpcApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = tendermint_servicer

        result_validator_set = await api.fetch_latest_validator_set()
        expected_validator_set = {
            "blockHeight": str(block_height),
            "validators": [
                {
                    "address": validator.address,
                    "votingPower": str(validator.voting_power),
                    "proposerPriority": str(validator.proposer_priority),
                }
            ],
            "pagination": {
                "nextKey": base64.b64encode(result_pagination.next_key).decode(),
                "total": str(result_pagination.total),
            },
        }

        assert result_validator_set == expected_validator_set

    @pytest.mark.asyncio
    async def test_fetch_validator_set_by_height(
        self,
        tendermint_servicer,
    ):
        block_height = 1
        validator = tendermint_query.Validator(
            address="inj1xml3ew93xmjtuf5zwpcl9jzznphte30hvdre9a",
            voting_power=10,
            proposer_priority=1,
        )
        result_pagination = pagination_pb.PageResponse(
            next_key=b"\001\032\264\007Z\224$]\377s8\343\004-\265\267\314?B\341",
            total=16036,
        )
        tendermint_servicer.get_validator_set_by_height_responses.append(
            tendermint_query.GetValidatorSetByHeightResponse(
                block_height=block_height,
                validators=[validator],
                pagination=result_pagination,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = TendermintGrpcApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = tendermint_servicer

        pagination_option = PaginationOption(
            skip=10,
            limit=30,
            reverse=False,
            count_total=True,
        )

        result_validator_set = await api.fetch_validator_set_by_height(
            height=block_height, pagination=pagination_option
        )
        expected_validator_set = {
            "blockHeight": str(block_height),
            "validators": [
                {
                    "address": validator.address,
                    "votingPower": str(validator.voting_power),
                    "proposerPriority": str(validator.proposer_priority),
                }
            ],
            "pagination": {
                "nextKey": base64.b64encode(result_pagination.next_key).decode(),
                "total": str(result_pagination.total),
            },
        }

        assert result_validator_set == expected_validator_set

    @pytest.mark.asyncio
    async def test_abci_query(
        self,
        tendermint_servicer,
    ):
        proof_op = tendermint_query.ProofOp(
            type="test type",
            key="proof key".encode(),
            data="proof data".encode(),
        )

        code = 0
        log = "test log"
        info = "test info"
        index = 1
        key = "test key".encode()
        value = "test value".encode()
        proof_ops = tendermint_query.ProofOps(ops=[proof_op])
        height = 4567
        codespace = "test codespace"

        tendermint_servicer.abci_query_responses.append(
            tendermint_query.ABCIQueryResponse(
                code=code,
                log=log,
                info=info,
                index=index,
                key=key,
                value=value,
                proof_ops=proof_ops,
                height=height,
                codespace=codespace,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = TendermintGrpcApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = tendermint_servicer

        result_validator_set = await api.abci_query(
            data="query data".encode(),
            path="/custom/test",
            height=height,
            prove=True,
        )
        expected_validator_set = {
            "code": code,
            "log": log,
            "info": info,
            "index": str(index),
            "key": base64.b64encode(key).decode(),
            "value": base64.b64encode(value).decode(),
            "proofOps": {
                "ops": [
                    {
                        "type": proof_op.type,
                        "key": base64.b64encode(proof_op.key).decode(),
                        "data": base64.b64encode(proof_op.data).decode(),
                    }
                ]
            },
            "height": str(height),
            "codespace": codespace,
        }

        assert result_validator_set == expected_validator_set

    async def _dummy_metadata_provider(self):
        return None
