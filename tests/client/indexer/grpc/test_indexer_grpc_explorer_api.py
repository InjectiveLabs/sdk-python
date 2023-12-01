import base64

import grpc
import pytest

from pyinjective.client.indexer.grpc.indexer_grpc_explorer_api import IndexerGrpcExplorerApi
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network
from pyinjective.proto.exchange import injective_explorer_rpc_pb2 as exchange_explorer_pb
from tests.client.indexer.configurable_explorer_query_servicer import ConfigurableExplorerQueryServicer


@pytest.fixture
def explorer_servicer():
    return ConfigurableExplorerQueryServicer()


class TestIndexerGrpcExplorerApi:
    @pytest.mark.asyncio
    async def test_fetch_account_txs(
        self,
        explorer_servicer,
    ):
        code = 5
        coin = exchange_explorer_pb.CosmosCoin(
            denom="inj",
            amount="200000000000000",
        )
        gas_fee = exchange_explorer_pb.GasFee(
            amount=[coin], gas_limit=400000, payer="inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex", granter="test granter"
        )
        event = exchange_explorer_pb.Event(type="test event type", attributes={"first_attribute": "attribute 1"})
        signature = exchange_explorer_pb.Signature(
            pubkey="02c33c539e2aea9f97137e8168f6e22f57b829876823fa04b878a2b7c2010465d9",
            address="inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex",
            sequence=223460,
            signature="gFXPJ5QENzq9SUHshE8g++aRLIlRCRVcOsYq+EOr3T4QgAAs5bVHf8NhugBjJP9B+AfQjQNNneHXPF9dEp4Uehs=",
        )
        claim_id = 100

        tx_data = exchange_explorer_pb.TxDetailData(
            id="test id",
            block_number=18138926,
            block_timestamp="2023-11-07 23:19:55.371 +0000 UTC",
            hash="0x3790ade2bea6c8605851ec89fa968adf2a2037a5ecac11ca95e99260508a3b7e",
            code=code,
            data=b"\022&\n$/cosmos.bank.v1beta1.MsgSendResponse",
            info="test info",
            gas_wanted=400000,
            gas_used=93696,
            gas_fee=gas_fee,
            codespace="test codespace",
            events=[event],
            tx_type="injective-web3",
            messages=b'[{"type":"/cosmos.bank.v1beta1.MsgSend","value":{'
            b'"from_address":"inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex",'
            b'"to_address":"inj1d6qx83nhx3a3gx7e654x4su8hur5s83u84h2xc",'
            b'"amount":[{"denom":"factory/inj17vytdwqczqz72j65saukplrktd4gyfme5agf6c/weth",'
            b'"amount":"100000000000000000"}]}}]',
            signatures=[signature],
            memo="test memo",
            tx_number=221429,
            block_unix_timestamp=1699399195371,
            error_log="",
            logs=b'[{"msg_index":0,"events":[{"type":"message","attributes":[{"key":"action",'
            b'"value":"/cosmos.bank.v1beta1.MsgSend"},{"key":"sender",'
            b'"value":"inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex"},{"key":"module","value":"bank"}]},'
            b'{"type":"coin_spent","attributes":[{"key":"spender",'
            b'"value":"inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex"},{"key":"amount",'
            b'"value":"100000000000000000factory/inj17vytdwqczqz72j65saukplrktd4gyfme5agf6c/weth"}]},'
            b'{"type":"coin_received","attributes":[{"key":"receiver",'
            b'"value":"inj1d6qx83nhx3a3gx7e654x4su8hur5s83u84h2xc"},{"key":"amount",'
            b'"value":"100000000000000000factory/inj17vytdwqczqz72j65saukplrktd4gyfme5agf6c/weth"}]},'
            b'{"type":"transfer","attributes":[{"key":"recipient",'
            b'"value":"inj1d6qx83nhx3a3gx7e654x4su8hur5s83u84h2xc"},'
            b'{"key":"sender","value":"inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex"},'
            b'{"key":"amount","value":"100000000000000000factory/inj17vytdwqczqz72j65saukplrktd4gyfme5agf6c/weth"}'
            b']},{"type":"message","attributes":[{"key":"sender",'
            b'"value":"inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex"}]}]}]',
            claim_ids=[claim_id],
        )

        paging = exchange_explorer_pb.Paging(total=5, to=5, count_by_subaccount=10, next=["next1", "next2"])
        setattr(paging, "from", 1)

        explorer_servicer.account_txs_responses.append(
            exchange_explorer_pb.GetAccountTxsResponse(
                data=[tx_data],
                paging=paging,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcExplorerApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = explorer_servicer

        result_txs = await api.fetch_account_txs(
            address="inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex",
            before=221439,
            after=221419,
            message_type="cosmos.bank.v1beta1.MsgSend",
            module="bank",
            from_number=221419,
            to_number=221439,
            status="status",
            pagination=PaginationOption(
                skip=0,
                limit=100,
                start_time=1699544939364,
                end_time=1699744939364,
            ),
        )
        expected_txs = {
            "data": [
                {
                    "id": tx_data.id,
                    "blockNumber": str(tx_data.block_number),
                    "blockTimestamp": tx_data.block_timestamp,
                    "hash": tx_data.hash,
                    "code": tx_data.code,
                    "data": base64.b64encode(tx_data.data).decode(),
                    "info": tx_data.info,
                    "gasWanted": str(tx_data.gas_wanted),
                    "gasUsed": str(tx_data.gas_used),
                    "gasFee": {
                        "amount": [
                            {
                                "denom": coin.denom,
                                "amount": coin.amount,
                            }
                        ],
                        "gasLimit": str(gas_fee.gas_limit),
                        "payer": gas_fee.payer,
                        "granter": gas_fee.granter,
                    },
                    "codespace": tx_data.codespace,
                    "events": [
                        {
                            "type": event.type,
                            "attributes": event.attributes,
                        }
                    ],
                    "txType": tx_data.tx_type,
                    "messages": base64.b64encode(tx_data.messages).decode(),
                    "signatures": [
                        {
                            "pubkey": signature.pubkey,
                            "address": signature.address,
                            "sequence": str(signature.sequence),
                            "signature": signature.signature,
                        }
                    ],
                    "memo": tx_data.memo,
                    "txNumber": str(tx_data.tx_number),
                    "blockUnixTimestamp": str(tx_data.block_unix_timestamp),
                    "errorLog": tx_data.error_log,
                    "logs": base64.b64encode(tx_data.logs).decode(),
                    "claimIds": [str(claim_id)],
                },
            ],
            "paging": {
                "total": str(paging.total),
                "from": getattr(paging, "from"),
                "to": paging.to,
                "countBySubaccount": str(paging.count_by_subaccount),
                "next": paging.next,
            },
        }

        assert result_txs == expected_txs

    @pytest.mark.asyncio
    async def test_fetch_contract_txs(
        self,
        explorer_servicer,
    ):
        code = 5
        coin = exchange_explorer_pb.CosmosCoin(
            denom="inj",
            amount="200000000000000",
        )
        gas_fee = exchange_explorer_pb.GasFee(
            amount=[coin], gas_limit=400000, payer="inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex", granter="test granter"
        )
        event = exchange_explorer_pb.Event(type="test event type", attributes={"first_attribute": "attribute 1"})
        signature = exchange_explorer_pb.Signature(
            pubkey="02c33c539e2aea9f97137e8168f6e22f57b829876823fa04b878a2b7c2010465d9",
            address="inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex",
            sequence=223460,
            signature="gFXPJ5QENzq9SUHshE8g++aRLIlRCRVcOsYq+EOr3T4QgAAs5bVHf8NhugBjJP9B+AfQjQNNneHXPF9dEp4Uehs=",
        )
        claim_id = 100

        tx_data = exchange_explorer_pb.TxDetailData(
            id="test id",
            block_number=18138926,
            block_timestamp="2023-11-07 23:19:55.371 +0000 UTC",
            hash="0x3790ade2bea6c8605851ec89fa968adf2a2037a5ecac11ca95e99260508a3b7e",
            code=code,
            data=b"\022&\n$/cosmos.bank.v1beta1.MsgSendResponse",
            info="test info",
            gas_wanted=400000,
            gas_used=93696,
            gas_fee=gas_fee,
            codespace="test codespace",
            events=[event],
            tx_type="injective-web3",
            messages=b'[{"type":"/cosmos.bank.v1beta1.MsgSend","value":{'
            b'"from_address":"inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex",'
            b'"to_address":"inj1d6qx83nhx3a3gx7e654x4su8hur5s83u84h2xc",'
            b'"amount":[{"denom":"factory/inj17vytdwqczqz72j65saukplrktd4gyfme5agf6c/weth",'
            b'"amount":"100000000000000000"}]}}]',
            signatures=[signature],
            memo="test memo",
            tx_number=221429,
            block_unix_timestamp=1699399195371,
            error_log="",
            logs=b'[{"msg_index":0,"events":[{"type":"message","attributes":['
            b'{"key":"action","value":"/cosmos.bank.v1beta1.MsgSend"},'
            b'{"key":"sender","value":"inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex"},'
            b'{"key":"module","value":"bank"}]},{"type":"coin_spent","attributes":['
            b'{"key":"spender","value":"inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex"},'
            b'{"key":"amount","value":"100000000000000000factory/inj17vytdwqczqz72j65saukplrktd4gyfme5agf6c/weth"}'
            b']},{"type":"coin_received","attributes":['
            b'{"key":"receiver","value":"inj1d6qx83nhx3a3gx7e654x4su8hur5s83u84h2xc"},'
            b'{"key":"amount","value":"100000000000000000factory/inj17vytdwqczqz72j65saukplrktd4gyfme5agf6c/weth"}'
            b']},{"type":"transfer","attributes":['
            b'{"key":"recipient","value":"inj1d6qx83nhx3a3gx7e654x4su8hur5s83u84h2xc"},'
            b'{"key":"sender","value":"inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex"},'
            b'{"key":"amount","value":"100000000000000000factory/inj17vytdwqczqz72j65saukplrktd4gyfme5agf6c/weth"}'
            b']},{"type":"message","attributes":['
            b'{"key":"sender","value":"inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex"}]}]}]',
            claim_ids=[claim_id],
        )

        paging = exchange_explorer_pb.Paging(total=5, to=5, count_by_subaccount=10, next=["next1", "next2"])
        setattr(paging, "from", 1)

        explorer_servicer.contract_txs_responses.append(
            exchange_explorer_pb.GetContractTxsResponse(
                data=[tx_data],
                paging=paging,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcExplorerApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = explorer_servicer

        result_contract_txs = await api.fetch_contract_txs(
            address="inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex",
            from_number=221419,
            to_number=221439,
            pagination=PaginationOption(
                skip=0,
                limit=100,
            ),
        )
        expected_contract_txs = {
            "data": [
                {
                    "id": tx_data.id,
                    "blockNumber": str(tx_data.block_number),
                    "blockTimestamp": tx_data.block_timestamp,
                    "hash": tx_data.hash,
                    "code": tx_data.code,
                    "data": base64.b64encode(tx_data.data).decode(),
                    "info": tx_data.info,
                    "gasWanted": str(tx_data.gas_wanted),
                    "gasUsed": str(tx_data.gas_used),
                    "gasFee": {
                        "amount": [
                            {
                                "denom": coin.denom,
                                "amount": coin.amount,
                            }
                        ],
                        "gasLimit": str(gas_fee.gas_limit),
                        "payer": gas_fee.payer,
                        "granter": gas_fee.granter,
                    },
                    "codespace": tx_data.codespace,
                    "events": [
                        {
                            "type": event.type,
                            "attributes": event.attributes,
                        }
                    ],
                    "txType": tx_data.tx_type,
                    "messages": base64.b64encode(tx_data.messages).decode(),
                    "signatures": [
                        {
                            "pubkey": signature.pubkey,
                            "address": signature.address,
                            "sequence": str(signature.sequence),
                            "signature": signature.signature,
                        }
                    ],
                    "memo": tx_data.memo,
                    "txNumber": str(tx_data.tx_number),
                    "blockUnixTimestamp": str(tx_data.block_unix_timestamp),
                    "errorLog": tx_data.error_log,
                    "logs": base64.b64encode(tx_data.logs).decode(),
                    "claimIds": [str(claim_id)],
                },
            ],
            "paging": {
                "total": str(paging.total),
                "from": getattr(paging, "from"),
                "to": paging.to,
                "countBySubaccount": str(paging.count_by_subaccount),
                "next": paging.next,
            },
        }

        assert result_contract_txs == expected_contract_txs

    @pytest.mark.asyncio
    async def test_fetch_blocks(
        self,
        explorer_servicer,
    ):
        block_info = exchange_explorer_pb.BlockInfo(
            height=19034578,
            proposer="injvalcons18x63wcw5hjxlf535lgn4qy20yer7mm0qedu0la",
            moniker="InjectiveNode1",
            block_hash="0x7f7bfe8caaa0eed042315d1447ef1ed726a80f5da23fdbe6831fc66775197db1",
            parent_hash="0x44287ba5fad21d0109a3ec6f19d447580763e5a709e5a5ceb767174e99ae3bd8",
            num_pre_commits=20,
            num_txs=4,
            timestamp="2023-11-29 20:23:33.842 +0000 UTC",
        )

        paging = exchange_explorer_pb.Paging(total=5, to=5, count_by_subaccount=10, next=["next1", "next2"])
        setattr(paging, "from", 1)

        explorer_servicer.blocks_responses.append(
            exchange_explorer_pb.GetBlocksResponse(
                data=[block_info],
                paging=paging,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcExplorerApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = explorer_servicer

        result_blocks = await api.fetch_blocks(
            before=221419,
            after=221439,
            pagination=PaginationOption(
                limit=100,
            ),
        )
        expected_blocks = {
            "data": [
                {
                    "height": str(block_info.height),
                    "proposer": block_info.proposer,
                    "moniker": block_info.moniker,
                    "blockHash": block_info.block_hash,
                    "parentHash": block_info.parent_hash,
                    "numPreCommits": str(block_info.num_pre_commits),
                    "numTxs": str(block_info.num_txs),
                    "txs": [],
                    "timestamp": block_info.timestamp,
                },
            ],
            "paging": {
                "total": str(paging.total),
                "from": getattr(paging, "from"),
                "to": paging.to,
                "countBySubaccount": str(paging.count_by_subaccount),
                "next": paging.next,
            },
        }

        assert result_blocks == expected_blocks

    @pytest.mark.asyncio
    async def test_fetch_block(
        self,
        explorer_servicer,
    ):
        tx_data = exchange_explorer_pb.TxData(
            id="tx id",
            block_number=5825046,
            block_timestamp="2022-12-11 22:06:49.182 +0000 UTC",
            hash="0xbe8c8ca9a41196adf59b88fe9efd78e7532e04169152e779be3dc14ba7c360d9",
            messages=b"null",
            tx_number=994979,
            tx_msg_types=b'["/injective.exchange.v1beta1.MsgCreateBinaryOptionsLimitOrder"]',
        )
        block_info = exchange_explorer_pb.BlockDetailInfo(
            height=19034578,
            proposer="injvalcons18x63wcw5hjxlf535lgn4qy20yer7mm0qedu0la",
            moniker="InjectiveNode1",
            block_hash="0x7f7bfe8caaa0eed042315d1447ef1ed726a80f5da23fdbe6831fc66775197db1",
            parent_hash="0x44287ba5fad21d0109a3ec6f19d447580763e5a709e5a5ceb767174e99ae3bd8",
            num_pre_commits=20,
            num_txs=4,
            total_txs=5,
            txs=[tx_data],
            timestamp="2023-11-29 20:23:33.842 +0000 UTC",
        )

        explorer_servicer.block_responses.append(
            exchange_explorer_pb.GetBlockResponse(
                s="ok",
                errmsg="test error message",
                data=block_info,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcExplorerApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = explorer_servicer

        result_block = await api.fetch_block(block_id=str(block_info.height))
        expected_block = {
            "s": "ok",
            "errmsg": "test error message",
            "data": {
                "height": str(block_info.height),
                "proposer": block_info.proposer,
                "moniker": block_info.moniker,
                "blockHash": block_info.block_hash,
                "parentHash": block_info.parent_hash,
                "numPreCommits": str(block_info.num_pre_commits),
                "numTxs": str(block_info.num_txs),
                "totalTxs": str(block_info.total_txs),
                "txs": [
                    {
                        "id": tx_data.id,
                        "blockNumber": str(tx_data.block_number),
                        "blockTimestamp": tx_data.block_timestamp,
                        "hash": tx_data.hash,
                        "codespace": tx_data.codespace,
                        "messages": base64.b64encode(tx_data.messages).decode(),
                        "txNumber": str(tx_data.tx_number),
                        "errorLog": tx_data.error_log,
                        "code": tx_data.code,
                        "txMsgTypes": base64.b64encode(tx_data.tx_msg_types).decode(),
                        "logs": base64.b64encode(tx_data.logs).decode(),
                        "claimIds": tx_data.claim_ids,
                    }
                ],
                "timestamp": block_info.timestamp,
            },
        }

        assert result_block == expected_block

    @pytest.mark.asyncio
    async def test_fetch_validators(
        self,
        explorer_servicer,
    ):
        validator_description = exchange_explorer_pb.ValidatorDescription(moniker="InjectiveNode0")
        validator = exchange_explorer_pb.Validator(
            id="test id",
            moniker="InjectiveNode0",
            operator_address="injvaloper156t3yxd4udv0h9gwagfcmwnmm3quy0nph7tyh5",
            consensus_address="injvalcons1xwg7xkmpqp8q804c37sa4dzyfwgnh4a74ll9pz",
            jailed=False,
            status=3,
            tokens="200059138606549756596244963211573",
            delegator_shares="200079146521201876783922319320744.623595039617821538",
            description=validator_description,
            unbonding_height=2489050,
            unbonding_time="2022-09-18 14:44:56.825 +0000 UTC",
            commission_rate="0.100000000000000000",
            commission_max_rate="1.000000000000000000",
            commission_max_change_rate="1.000000000000000000",
            commission_update_time="2022-07-05 00:43:31.747 +0000 UTC",
            proposed=4140681,
            signed=10764141,
            missed=0,
            timestamp="2023-11-30 15:17:26.124 +0000 UTC",
            uptime_percentage=99.906641771138965,
        )

        explorer_servicer.validators_responses.append(
            exchange_explorer_pb.GetValidatorsResponse(
                s="ok",
                errmsg="test error message",
                data=[validator],
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcExplorerApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = explorer_servicer

        result_validators = await api.fetch_validators()
        expected_validators = {
            "s": "ok",
            "errmsg": "test error message",
            "data": [
                {
                    "id": validator.id,
                    "moniker": validator.moniker,
                    "operatorAddress": validator.operator_address,
                    "consensusAddress": validator.consensus_address,
                    "jailed": validator.jailed,
                    "status": validator.status,
                    "tokens": validator.tokens,
                    "delegatorShares": validator.delegator_shares,
                    "description": {
                        "moniker": validator_description.moniker,
                        "identity": validator_description.identity,
                        "website": validator_description.website,
                        "securityContact": validator_description.security_contact,
                        "details": validator_description.details,
                        "imageUrl": validator_description.image_url,
                    },
                    "unbondingHeight": str(validator.unbonding_height),
                    "unbondingTime": validator.unbonding_time,
                    "commissionRate": validator.commission_rate,
                    "commissionMaxRate": validator.commission_max_rate,
                    "commissionMaxChangeRate": validator.commission_max_change_rate,
                    "commissionUpdateTime": validator.commission_update_time,
                    "proposed": str(validator.proposed),
                    "signed": str(validator.signed),
                    "missed": str(validator.missed),
                    "timestamp": validator.timestamp,
                    "uptimes": validator.uptimes,
                    "slashingEvents": validator.slashing_events,
                    "uptimePercentage": validator.uptime_percentage,
                    "imageUrl": validator.image_url,
                },
            ],
        }

        assert result_validators == expected_validators

    @pytest.mark.asyncio
    async def test_fetch_validator(
        self,
        explorer_servicer,
    ):
        validator_description = exchange_explorer_pb.ValidatorDescription(moniker="InjectiveNode0")
        validator = exchange_explorer_pb.Validator(
            id="test id",
            moniker="InjectiveNode0",
            operator_address="injvaloper156t3yxd4udv0h9gwagfcmwnmm3quy0nph7tyh5",
            consensus_address="injvalcons1xwg7xkmpqp8q804c37sa4dzyfwgnh4a74ll9pz",
            jailed=False,
            status=3,
            tokens="200059138606549756596244963211573",
            delegator_shares="200079146521201876783922319320744.623595039617821538",
            description=validator_description,
            unbonding_height=2489050,
            unbonding_time="2022-09-18 14:44:56.825 +0000 UTC",
            commission_rate="0.100000000000000000",
            commission_max_rate="1.000000000000000000",
            commission_max_change_rate="1.000000000000000000",
            commission_update_time="2022-07-05 00:43:31.747 +0000 UTC",
            proposed=4140681,
            signed=10764141,
            missed=0,
            timestamp="2023-11-30 15:17:26.124 +0000 UTC",
            uptime_percentage=99.906641771138965,
        )

        explorer_servicer.validator_responses.append(
            exchange_explorer_pb.GetValidatorResponse(
                s="ok",
                errmsg="test error message",
                data=validator,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcExplorerApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = explorer_servicer

        result_validator = await api.fetch_validator(address=validator.operator_address)
        expected_validator = {
            "s": "ok",
            "errmsg": "test error message",
            "data": {
                "id": validator.id,
                "moniker": validator.moniker,
                "operatorAddress": validator.operator_address,
                "consensusAddress": validator.consensus_address,
                "jailed": validator.jailed,
                "status": validator.status,
                "tokens": validator.tokens,
                "delegatorShares": validator.delegator_shares,
                "description": {
                    "moniker": validator_description.moniker,
                    "identity": validator_description.identity,
                    "website": validator_description.website,
                    "securityContact": validator_description.security_contact,
                    "details": validator_description.details,
                    "imageUrl": validator_description.image_url,
                },
                "unbondingHeight": str(validator.unbonding_height),
                "unbondingTime": validator.unbonding_time,
                "commissionRate": validator.commission_rate,
                "commissionMaxRate": validator.commission_max_rate,
                "commissionMaxChangeRate": validator.commission_max_change_rate,
                "commissionUpdateTime": validator.commission_update_time,
                "proposed": str(validator.proposed),
                "signed": str(validator.signed),
                "missed": str(validator.missed),
                "timestamp": validator.timestamp,
                "uptimes": validator.uptimes,
                "slashingEvents": validator.slashing_events,
                "uptimePercentage": validator.uptime_percentage,
                "imageUrl": validator.image_url,
            },
        }

        assert result_validator == expected_validator

    @pytest.mark.asyncio
    async def test_fetch_validator_uptime(
        self,
        explorer_servicer,
    ):
        validator_uptime = exchange_explorer_pb.ValidatorUptime(
            block_number=2489050,
            status="3",
        )

        explorer_servicer.validator_uptime_responses.append(
            exchange_explorer_pb.GetValidatorUptimeResponse(
                s="ok",
                errmsg="test error message",
                data=[validator_uptime],
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcExplorerApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = explorer_servicer

        result_validator = await api.fetch_validator_uptime(address="injvaloper156t3yxd4udv0h9gwagfcmwnmm3quy0nph7tyh5")
        expected_validator = {
            "s": "ok",
            "errmsg": "test error message",
            "data": [
                {
                    "blockNumber": str(validator_uptime.block_number),
                    "status": validator_uptime.status,
                },
            ],
        }

        assert result_validator == expected_validator

    @pytest.mark.asyncio
    async def test_fetch_txs(
        self,
        explorer_servicer,
    ):
        code = 5
        claim_id = 100

        tx_data = exchange_explorer_pb.TxData(
            id="test id",
            block_number=18138926,
            block_timestamp="2023-11-07 23:19:55.371 +0000 UTC",
            hash="0x3790ade2bea6c8605851ec89fa968adf2a2037a5ecac11ca95e99260508a3b7e",
            codespace="test codespace",
            messages=b'[{"type":"/cosmos.bank.v1beta1.MsgSend",'
            b'"value":{"from_address":"inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex",'
            b'"to_address":"inj1d6qx83nhx3a3gx7e654x4su8hur5s83u84h2xc",'
            b'"amount":[{"denom":"factory/inj17vytdwqczqz72j65saukplrktd4gyfme5agf6c/weth",'
            b'"amount":"100000000000000000"}]}}]',
            tx_number=221429,
            error_log="",
            code=code,
            tx_msg_types=b'["/injective.exchange.v1beta1.MsgCreateBinaryOptionsLimitOrder"]',
            logs=b'[{"msg_index":0,"events":[{"type":"message","attributes":['
            b'{"key":"action","value":"/cosmos.bank.v1beta1.MsgSend"},'
            b'{"key":"sender","value":"inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex"},'
            b'{"key":"module","value":"bank"}]},{"type":"coin_spent","attributes":['
            b'{"key":"spender","value":"inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex"},'
            b'{"key":"amount","value":"100000000000000000factory/inj17vytdwqczqz72j65saukplrktd4gyfme5agf6c/weth"}'
            b']},{"type":"coin_received","attributes":['
            b'{"key":"receiver","value":"inj1d6qx83nhx3a3gx7e654x4su8hur5s83u84h2xc"},'
            b'{"key":"amount","value":"100000000000000000factory/inj17vytdwqczqz72j65saukplrktd4gyfme5agf6c/weth"}'
            b']},{"type":"transfer","attributes":['
            b'{"key":"recipient","value":"inj1d6qx83nhx3a3gx7e654x4su8hur5s83u84h2xc"},'
            b'{"key":"sender","value":"inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex"},'
            b'{"key":"amount","value":"100000000000000000factory/inj17vytdwqczqz72j65saukplrktd4gyfme5agf6c/weth"}'
            b']},{"type":"message","attributes":['
            b'{"key":"sender","value":"inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex"}]}]}]',
            claim_ids=[claim_id],
        )

        paging = exchange_explorer_pb.Paging(total=5, to=5, count_by_subaccount=10, next=["next1", "next2"])
        setattr(paging, "from", 1)

        explorer_servicer.txs_responses.append(
            exchange_explorer_pb.GetTxsResponse(
                data=[tx_data],
                paging=paging,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcExplorerApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = explorer_servicer

        result_txs = await api.fetch_txs(
            before=221439,
            after=221419,
            message_type="cosmos.bank.v1beta1.MsgSend",
            module="bank",
            from_number=221419,
            to_number=221439,
            status="status",
            pagination=PaginationOption(
                skip=0,
                limit=100,
                start_time=1699544939364,
                end_time=1699744939364,
            ),
        )
        expected_txs = {
            "data": [
                {
                    "id": tx_data.id,
                    "blockNumber": str(tx_data.block_number),
                    "blockTimestamp": tx_data.block_timestamp,
                    "hash": tx_data.hash,
                    "codespace": tx_data.codespace,
                    "messages": base64.b64encode(tx_data.messages).decode(),
                    "txNumber": str(tx_data.tx_number),
                    "errorLog": tx_data.error_log,
                    "code": tx_data.code,
                    "txMsgTypes": base64.b64encode(tx_data.tx_msg_types).decode(),
                    "logs": base64.b64encode(tx_data.logs).decode(),
                    "claimIds": [str(claim_id)],
                },
            ],
            "paging": {
                "total": str(paging.total),
                "from": getattr(paging, "from"),
                "to": paging.to,
                "countBySubaccount": str(paging.count_by_subaccount),
                "next": paging.next,
            },
        }

        assert result_txs == expected_txs

    @pytest.mark.asyncio
    async def test_fetch_tx_by_hash(
        self,
        explorer_servicer,
    ):
        code = 5
        coin = exchange_explorer_pb.CosmosCoin(
            denom="inj",
            amount="200000000000000",
        )
        gas_fee = exchange_explorer_pb.GasFee(
            amount=[coin], gas_limit=400000, payer="inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex", granter="test granter"
        )
        event = exchange_explorer_pb.Event(type="test event type", attributes={"first_attribute": "attribute 1"})
        signature = exchange_explorer_pb.Signature(
            pubkey="02c33c539e2aea9f97137e8168f6e22f57b829876823fa04b878a2b7c2010465d9",
            address="inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex",
            sequence=223460,
            signature="gFXPJ5QENzq9SUHshE8g++aRLIlRCRVcOsYq+EOr3T4QgAAs5bVHf8NhugBjJP9B+AfQjQNNneHXPF9dEp4Uehs=",
        )
        claim_id = 100

        tx_data = exchange_explorer_pb.TxDetailData(
            id="test id",
            block_number=18138926,
            block_timestamp="2023-11-07 23:19:55.371 +0000 UTC",
            hash="0x3790ade2bea6c8605851ec89fa968adf2a2037a5ecac11ca95e99260508a3b7e",
            code=code,
            data=b"\022&\n$/cosmos.bank.v1beta1.MsgSendResponse",
            info="test info",
            gas_wanted=400000,
            gas_used=93696,
            gas_fee=gas_fee,
            codespace="test codespace",
            events=[event],
            tx_type="injective-web3",
            messages=b'[{"type":"/cosmos.bank.v1beta1.MsgSend",'
            b'"value":{"from_address":"inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex",'
            b'"to_address":"inj1d6qx83nhx3a3gx7e654x4su8hur5s83u84h2xc",'
            b'"amount":[{"denom":"factory/inj17vytdwqczqz72j65saukplrktd4gyfme5agf6c/weth",'
            b'"amount":"100000000000000000"}]}}]',
            signatures=[signature],
            memo="test memo",
            tx_number=221429,
            block_unix_timestamp=1699399195371,
            error_log="",
            logs=b'[{"msg_index":0,"events":[{"type":"message","attributes":['
            b'{"key":"action","value":"/cosmos.bank.v1beta1.MsgSend"},'
            b'{"key":"sender","value":"inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex"},'
            b'{"key":"module","value":"bank"}]},{"type":"coin_spent","attributes":['
            b'{"key":"spender","value":"inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex"},'
            b'{"key":"amount","value":"100000000000000000factory/inj17vytdwqczqz72j65saukplrktd4gyfme5agf6c/weth"}'
            b']},{"type":"coin_received","attributes":['
            b'{"key":"receiver","value":"inj1d6qx83nhx3a3gx7e654x4su8hur5s83u84h2xc"},'
            b'{"key":"amount","value":"100000000000000000factory/inj17vytdwqczqz72j65saukplrktd4gyfme5agf6c/weth"}'
            b']},{"type":"transfer","attributes":['
            b'{"key":"recipient","value":"inj1d6qx83nhx3a3gx7e654x4su8hur5s83u84h2xc"},'
            b'{"key":"sender","value":"inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex"},'
            b'{"key":"amount","value":"100000000000000000factory/inj17vytdwqczqz72j65saukplrktd4gyfme5agf6c/weth"}'
            b']},{"type":"message","attributes":['
            b'{"key":"sender","value":"inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex"}]}]}]',
            claim_ids=[claim_id],
        )

        explorer_servicer.tx_by_tx_hash_responses.append(
            exchange_explorer_pb.GetTxByTxHashResponse(
                s="ok",
                errmsg="test error message",
                data=tx_data,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcExplorerApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = explorer_servicer

        result_tx = await api.fetch_tx_by_tx_hash(tx_hash=tx_data.hash)
        expected_tx = {
            "s": "ok",
            "errmsg": "test error message",
            "data": {
                "id": tx_data.id,
                "blockNumber": str(tx_data.block_number),
                "blockTimestamp": tx_data.block_timestamp,
                "hash": tx_data.hash,
                "code": tx_data.code,
                "data": base64.b64encode(tx_data.data).decode(),
                "info": tx_data.info,
                "gasWanted": str(tx_data.gas_wanted),
                "gasUsed": str(tx_data.gas_used),
                "gasFee": {
                    "amount": [
                        {
                            "denom": coin.denom,
                            "amount": coin.amount,
                        }
                    ],
                    "gasLimit": str(gas_fee.gas_limit),
                    "payer": gas_fee.payer,
                    "granter": gas_fee.granter,
                },
                "codespace": tx_data.codespace,
                "events": [
                    {
                        "type": event.type,
                        "attributes": event.attributes,
                    }
                ],
                "txType": tx_data.tx_type,
                "messages": base64.b64encode(tx_data.messages).decode(),
                "signatures": [
                    {
                        "pubkey": signature.pubkey,
                        "address": signature.address,
                        "sequence": str(signature.sequence),
                        "signature": signature.signature,
                    }
                ],
                "memo": tx_data.memo,
                "txNumber": str(tx_data.tx_number),
                "blockUnixTimestamp": str(tx_data.block_unix_timestamp),
                "errorLog": tx_data.error_log,
                "logs": base64.b64encode(tx_data.logs).decode(),
                "claimIds": [str(claim_id)],
            },
        }

        assert result_tx == expected_tx

    @pytest.mark.asyncio
    async def test_fetch_peggy_deposit_txs(
        self,
        explorer_servicer,
    ):
        tx_hash = "0x028a43ad2089cad45a8855143508f7381787d7f17cc19e3cda1bc2300c1d043f"
        tx_data = exchange_explorer_pb.PeggyDepositTx(
            sender="0x197E6c3f19951eA0bA90Ddf465bcC79790cDD12d",
            receiver="inj1r9lxc0cej502pw5smh6xt0x8j7gvm5fdrj6xhk",
            event_nonce=624,
            event_height=10122722,
            amount="500000000000000000",
            denom="0xAD1794307245443B3Cb55d88e79EEE4d8a548C03",
            orchestrator_address="inj1c8rpu79mr70hqsgzutdd6rhvzhej9vntm6fqku",
            state="Completed",
            claim_type=1,
            tx_hashes=[tx_hash],
            created_at="2023-11-28 16:55:54.841 +0000 UTC",
            updated_at="2023-11-28 16:56:07.944 +0000 UTC",
        )

        explorer_servicer.peggy_deposit_txs_responses.append(
            exchange_explorer_pb.GetPeggyDepositTxsResponse(field=[tx_data])
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcExplorerApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = explorer_servicer

        result_tx = await api.fetch_peggy_deposit_txs(
            sender=tx_data.sender,
            receiver=tx_data.receiver,
            pagination=PaginationOption(
                skip=0,
                limit=100,
            ),
        )
        expected_tx = {
            "field": [
                {
                    "sender": tx_data.sender,
                    "receiver": tx_data.receiver,
                    "eventNonce": str(tx_data.event_nonce),
                    "eventHeight": str(tx_data.event_height),
                    "amount": tx_data.amount,
                    "denom": tx_data.denom,
                    "orchestratorAddress": tx_data.orchestrator_address,
                    "state": tx_data.state,
                    "claimType": tx_data.claim_type,
                    "txHashes": [tx_hash],
                    "createdAt": tx_data.created_at,
                    "updatedAt": tx_data.updated_at,
                },
            ]
        }

        assert result_tx == expected_tx

    @pytest.mark.asyncio
    async def test_fetch_peggy_withdrawal_txs(
        self,
        explorer_servicer,
    ):
        tx_hash = "0x028a43ad2089cad45a8855143508f7381787d7f17cc19e3cda1bc2300c1d043f"
        tx_data = exchange_explorer_pb.PeggyWithdrawalTx(
            sender="0x197E6c3f19951eA0bA90Ddf465bcC79790cDD12d",
            receiver="inj1r9lxc0cej502pw5smh6xt0x8j7gvm5fdrj6xhk",
            amount="500000000000000000",
            denom="0xAD1794307245443B3Cb55d88e79EEE4d8a548C03",
            bridge_fee="575043128234617596",
            outgoing_tx_id=1136,
            batch_timeout=10125614,
            batch_nonce=1600,
            orchestrator_address="inj1c8rpu79mr70hqsgzutdd6rhvzhej9vntm6fqku",
            event_nonce=624,
            event_height=10122722,
            state="Completed",
            claim_type=1,
            tx_hashes=[tx_hash],
            created_at="2023-11-28 16:55:54.841 +0000 UTC",
            updated_at="2023-11-28 16:56:07.944 +0000 UTC",
        )

        explorer_servicer.peggy_withdrawal_txs_responses.append(
            exchange_explorer_pb.GetPeggyWithdrawalTxsResponse(field=[tx_data])
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcExplorerApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = explorer_servicer

        result_tx = await api.fetch_peggy_withdrawal_txs(
            sender=tx_data.sender,
            receiver=tx_data.receiver,
            pagination=PaginationOption(
                skip=0,
                limit=100,
            ),
        )
        expected_tx = {
            "field": [
                {
                    "sender": tx_data.sender,
                    "receiver": tx_data.receiver,
                    "amount": tx_data.amount,
                    "denom": tx_data.denom,
                    "bridgeFee": tx_data.bridge_fee,
                    "outgoingTxId": str(tx_data.outgoing_tx_id),
                    "batchTimeout": str(tx_data.batch_timeout),
                    "batchNonce": str(tx_data.batch_nonce),
                    "orchestratorAddress": tx_data.orchestrator_address,
                    "eventNonce": str(tx_data.event_nonce),
                    "eventHeight": str(tx_data.event_height),
                    "state": tx_data.state,
                    "claimType": tx_data.claim_type,
                    "txHashes": [tx_hash],
                    "createdAt": tx_data.created_at,
                    "updatedAt": tx_data.updated_at,
                },
            ]
        }

        assert result_tx == expected_tx

    @pytest.mark.asyncio
    async def test_fetch_ibc_transfer_txs(
        self,
        explorer_servicer,
    ):
        tx_hash = "0x028a43ad2089cad45a8855143508f7381787d7f17cc19e3cda1bc2300c1d043f"
        tx_data = exchange_explorer_pb.IBCTransferTx(
            sender="0x197E6c3f19951eA0bA90Ddf465bcC79790cDD12d",
            receiver="inj1r9lxc0cej502pw5smh6xt0x8j7gvm5fdrj6xhk",
            source_port="transfer",
            source_channel="channel-74",
            destination_port="transfer",
            destination_channel="channel-33",
            amount="500000000000000000",
            denom="0xAD1794307245443B3Cb55d88e79EEE4d8a548C03",
            timeout_height="0-0",
            timeout_timestamp=1701460751755119600,
            packet_sequence=16607,
            data_hex=b"7b22616d6f756e74223a2231303030303030222c2264656e6f6d223a227472616e736665722f6368616e6e656c2d3734"
            b"2f756e6f6973222c227265636569766572223a226e6f6973316d7675757067726537706a78336b35746d353732396672"
            b"6b6e396e766a75367067737861776334377067616d63747970647a6c736d3768673930222c2273656e646572223a2269"
            b"6e6a31346e656e6474737a306334306e3778747a776b6a6d646338646b757a3833356a64796478686e227d",
            state="Completed",
            tx_hashes=[tx_hash],
            created_at="2023-11-28 16:55:54.841 +0000 UTC",
            updated_at="2023-11-28 16:56:07.944 +0000 UTC",
        )

        explorer_servicer.ibc_transfer_txs_responses.append(
            exchange_explorer_pb.GetIBCTransferTxsResponse(field=[tx_data])
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcExplorerApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = explorer_servicer

        result_tx = await api.fetch_ibc_transfer_txs(
            sender=tx_data.sender,
            receiver=tx_data.receiver,
            src_channel=tx_data.source_channel,
            src_port=tx_data.source_port,
            dest_channel=tx_data.destination_channel,
            dest_port=tx_data.destination_port,
            pagination=PaginationOption(
                skip=0,
                limit=100,
            ),
        )
        expected_tx = {
            "field": [
                {
                    "sender": tx_data.sender,
                    "receiver": tx_data.receiver,
                    "sourcePort": tx_data.source_port,
                    "sourceChannel": tx_data.source_channel,
                    "destinationPort": tx_data.destination_port,
                    "destinationChannel": tx_data.destination_channel,
                    "amount": tx_data.amount,
                    "denom": tx_data.denom,
                    "timeoutHeight": tx_data.timeout_height,
                    "timeoutTimestamp": str(tx_data.timeout_timestamp),
                    "packetSequence": str(tx_data.packet_sequence),
                    "dataHex": base64.b64encode(tx_data.data_hex).decode(),
                    "state": tx_data.state,
                    "txHashes": [tx_hash],
                    "createdAt": tx_data.created_at,
                    "updatedAt": tx_data.updated_at,
                },
            ]
        }

        assert result_tx == expected_tx

    @pytest.mark.asyncio
    async def test_fetch_wasm_codes(
        self,
        explorer_servicer,
    ):
        checksum = exchange_explorer_pb.Checksum(
            algorithm="sha256",
            hash="0xadecb2d943c03eeee77e111791df61198a9dee097f47f14a811b8f9657122624",
        )
        permission = exchange_explorer_pb.ContractPermission(
            access_type=3,
            address="test address",
        )
        wasm_code = exchange_explorer_pb.WasmCode(
            code_id=245,
            tx_hash="0xa5da295f9252dc932861be6f2a4dbc9a8c0f44bb42a473ded5ec349407a1c708",
            checksum=checksum,
            created_at=1701373663980,
            contract_type="test contract type",
            version="test version",
            permission=permission,
            code_schema="test code schema",
            code_view="test code view",
            instantiates=0,
            creator="inj17vytdwqczqz72j65saukplrktd4gyfme5agf6c",
            code_number=253,
            proposal_id=0,
        )

        paging = exchange_explorer_pb.Paging(total=5, to=5, count_by_subaccount=10, next=["next1", "next2"])
        setattr(paging, "from", 1)

        explorer_servicer.wasm_codes_responses.append(
            exchange_explorer_pb.GetWasmCodesResponse(paging=paging, data=[wasm_code])
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcExplorerApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = explorer_servicer

        result_wasm_codes = await api.fetch_wasm_codes(
            from_number=1,
            to_number=1000,
            pagination=PaginationOption(
                limit=100,
            ),
        )
        expected_wasm_codes = {
            "data": [
                {
                    "codeId": str(wasm_code.code_id),
                    "txHash": wasm_code.tx_hash,
                    "checksum": {
                        "algorithm": checksum.algorithm,
                        "hash": checksum.hash,
                    },
                    "createdAt": str(wasm_code.created_at),
                    "contractType": wasm_code.contract_type,
                    "version": wasm_code.version,
                    "permission": {
                        "accessType": permission.access_type,
                        "address": permission.address,
                    },
                    "codeSchema": wasm_code.code_schema,
                    "codeView": wasm_code.code_view,
                    "instantiates": str(wasm_code.instantiates),
                    "creator": wasm_code.creator,
                    "codeNumber": str(wasm_code.code_number),
                    "proposalId": str(wasm_code.proposal_id),
                },
            ],
            "paging": {
                "total": str(paging.total),
                "from": getattr(paging, "from"),
                "to": paging.to,
                "countBySubaccount": str(paging.count_by_subaccount),
                "next": paging.next,
            },
        }

        assert result_wasm_codes == expected_wasm_codes

    @pytest.mark.asyncio
    async def test_fetch_wasm_code_by_id(
        self,
        explorer_servicer,
    ):
        checksum = exchange_explorer_pb.Checksum(
            algorithm="sha256",
            hash="0xadecb2d943c03eeee77e111791df61198a9dee097f47f14a811b8f9657122624",
        )
        permission = exchange_explorer_pb.ContractPermission(
            access_type=3,
            address="test address",
        )
        wasm_code = exchange_explorer_pb.GetWasmCodeByIDResponse(
            code_id=245,
            tx_hash="0xa5da295f9252dc932861be6f2a4dbc9a8c0f44bb42a473ded5ec349407a1c708",
            checksum=checksum,
            created_at=1701373663980,
            contract_type="test contract type",
            version="test version",
            permission=permission,
            code_schema="test code schema",
            code_view="test code view",
            instantiates=0,
            creator="inj17vytdwqczqz72j65saukplrktd4gyfme5agf6c",
            code_number=253,
            proposal_id=0,
        )

        explorer_servicer.wasm_code_by_id_responses.append(wasm_code)

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcExplorerApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = explorer_servicer

        result_wasm_code = await api.fetch_wasm_code_by_id(code_id=wasm_code.code_id)
        expected_wasm_code = {
            "codeId": str(wasm_code.code_id),
            "txHash": wasm_code.tx_hash,
            "checksum": {
                "algorithm": checksum.algorithm,
                "hash": checksum.hash,
            },
            "createdAt": str(wasm_code.created_at),
            "contractType": wasm_code.contract_type,
            "version": wasm_code.version,
            "permission": {
                "accessType": permission.access_type,
                "address": permission.address,
            },
            "codeSchema": wasm_code.code_schema,
            "codeView": wasm_code.code_view,
            "instantiates": str(wasm_code.instantiates),
            "creator": wasm_code.creator,
            "codeNumber": str(wasm_code.code_number),
            "proposalId": str(wasm_code.proposal_id),
        }

        assert result_wasm_code == expected_wasm_code

    @pytest.mark.asyncio
    async def test_fetch_wasm_contracts(
        self,
        explorer_servicer,
    ):
        wasm_contract = exchange_explorer_pb.WasmContract(
            label="Talis candy machine",
            address="inj1t4lnxfu9gtyd50uqmf0ahpwk3vtg5yk9pe7uj4",
            tx_hash="0x7462ce393fd7691c5179107dcd5ee47c79e7a348538c0c976e160bbbfdae338c",
            creator="inj1fh92xcg28rat7apzhw5aw8x4x83wrprq4sp3tj",
            executes=23,
            instantiated_at=1701320950004,
            init_message='{"admin":"inj1maeyvxfamtn8lfyxpjca8kuvauuf2qeu6gtxm3","codeId":"104",'
            '"label":"Talis candy machine","msg":"",'
            '"sender":"inj1fh92xcg28rat7apzhw5aw8x4x83wrprq4sp3tj","fundsList":[],'
            '"contract_address":"inj1mhsrt6ulz07wnesppy39wwygjntk0stmk39ftg",'
            '"owner":"inj1fh92xcg28rat7apzhw5aw8x4x83wrprq4sp3tj",'
            '"fee_collector":"inj1maeyvxfamtn8lfyxpjca8kuvauuf2qeu6gtxm3",'
            '"operator_pubkey":"Aq9ExLymJrae0ol4Pq13vZkDARZeunbFWJGXgsHtkzkx",'
            '"public_phase":{"id":0,"private":false,"start":1701363602,"end":1701489600,'
            '"price":{"native":[{"denom":"inj","amount":"100000000000000000"}]},"mint_limit":5},'
            '"reserved_tokens":11,"total_tokens":111}',
            last_executed_at=1701395446228,
            funds=[],
            code_id=104,
            admin="inj1maeyvxfamtn8lfyxpjca8kuvauuf2qeu6gtxm3",
            current_migrate_message="",
            contract_number=1037,
            version="test version",
            type="test_type",
            proposal_id=0,
        )

        paging = exchange_explorer_pb.Paging(total=5, to=5, count_by_subaccount=10, next=["next1", "next2"])
        setattr(paging, "from", 1)

        explorer_servicer.wasm_contracts_responses.append(
            exchange_explorer_pb.GetWasmContractsResponse(paging=paging, data=[wasm_contract])
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcExplorerApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = explorer_servicer

        result_wasm_contracts = await api.fetch_wasm_contracts(
            code_id=wasm_contract.code_id,
            from_number=1,
            to_number=1000,
            assets_only=False,
            label=wasm_contract.label,
            pagination=PaginationOption(
                limit=100,
                skip=10,
            ),
        )
        expected_wasm_contracts = {
            "data": [
                {
                    "label": wasm_contract.label,
                    "address": wasm_contract.address,
                    "txHash": wasm_contract.tx_hash,
                    "creator": wasm_contract.creator,
                    "executes": str(wasm_contract.executes),
                    "instantiatedAt": str(wasm_contract.instantiated_at),
                    "initMessage": wasm_contract.init_message,
                    "lastExecutedAt": str(wasm_contract.last_executed_at),
                    "funds": wasm_contract.funds,
                    "codeId": str(wasm_contract.code_id),
                    "admin": wasm_contract.admin,
                    "currentMigrateMessage": wasm_contract.current_migrate_message,
                    "contractNumber": str(wasm_contract.contract_number),
                    "version": wasm_contract.version,
                    "type": wasm_contract.type,
                    "proposalId": str(wasm_contract.proposal_id),
                },
            ],
            "paging": {
                "total": str(paging.total),
                "from": getattr(paging, "from"),
                "to": paging.to,
                "countBySubaccount": str(paging.count_by_subaccount),
                "next": paging.next,
            },
        }

        assert result_wasm_contracts == expected_wasm_contracts

    @pytest.mark.asyncio
    async def test_fetch_wasm_contract_by_address(
        self,
        explorer_servicer,
    ):
        wasm_contract = exchange_explorer_pb.GetWasmContractByAddressResponse(
            label="Talis candy machine",
            address="inj1t4lnxfu9gtyd50uqmf0ahpwk3vtg5yk9pe7uj4",
            tx_hash="0x7462ce393fd7691c5179107dcd5ee47c79e7a348538c0c976e160bbbfdae338c",
            creator="inj1fh92xcg28rat7apzhw5aw8x4x83wrprq4sp3tj",
            executes=23,
            instantiated_at=1701320950004,
            init_message='{"admin":"inj1maeyvxfamtn8lfyxpjca8kuvauuf2qeu6gtxm3","codeId":"104",'
            '"label":"Talis candy machine","msg":"","sender":"inj1fh92xcg28rat7apzhw5aw8x4x83wrprq4sp3tj",'
            '"fundsList":[],"contract_address":"inj1mhsrt6ulz07wnesppy39wwygjntk0stmk39ftg",'
            '"owner":"inj1fh92xcg28rat7apzhw5aw8x4x83wrprq4sp3tj",'
            '"fee_collector":"inj1maeyvxfamtn8lfyxpjca8kuvauuf2qeu6gtxm3",'
            '"operator_pubkey":"Aq9ExLymJrae0ol4Pq13vZkDARZeunbFWJGXgsHtkzkx",'
            '"public_phase":{"id":0,"private":false,"start":1701363602,"end":1701489600,'
            '"price":{"native":[{"denom":"inj","amount":"100000000000000000"}]},"mint_limit":5},'
            '"reserved_tokens":11,"total_tokens":111}',
            last_executed_at=1701395446228,
            funds=[],
            code_id=104,
            admin="inj1maeyvxfamtn8lfyxpjca8kuvauuf2qeu6gtxm3",
            current_migrate_message="",
            contract_number=1037,
            version="test version",
            type="test_type",
            proposal_id=0,
        )

        explorer_servicer.wasm_contract_by_address_responses.append(wasm_contract)

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcExplorerApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = explorer_servicer

        result_wasm_contract = await api.fetch_wasm_contract_by_address(address=wasm_contract.address)
        expected_wasm_contract = {
            "label": wasm_contract.label,
            "address": wasm_contract.address,
            "txHash": wasm_contract.tx_hash,
            "creator": wasm_contract.creator,
            "executes": str(wasm_contract.executes),
            "instantiatedAt": str(wasm_contract.instantiated_at),
            "initMessage": wasm_contract.init_message,
            "lastExecutedAt": str(wasm_contract.last_executed_at),
            "funds": wasm_contract.funds,
            "codeId": str(wasm_contract.code_id),
            "admin": wasm_contract.admin,
            "currentMigrateMessage": wasm_contract.current_migrate_message,
            "contractNumber": str(wasm_contract.contract_number),
            "version": wasm_contract.version,
            "type": wasm_contract.type,
            "proposalId": str(wasm_contract.proposal_id),
        }

        assert result_wasm_contract == expected_wasm_contract

    @pytest.mark.asyncio
    async def test_fetch_cw20_balance(
        self,
        explorer_servicer,
    ):
        token_info = exchange_explorer_pb.Cw20TokenInfo(
            name="Tether",
            symbol="USDT",
            decimals=6,
            total_supply="100000000000",
        )
        marketing_info = exchange_explorer_pb.Cw20MarketingInfo(
            project="Tether",
            description="Tether project",
            logo="test logo",
            marketing=b"Test marketing info",
        )
        cw20_metadata = exchange_explorer_pb.Cw20Metadata(
            token_info=token_info,
            marketing_info=marketing_info,
        )
        wasm_balance = exchange_explorer_pb.WasmCw20Balance(
            account="0xaf79152ac5df276d9a8e1e2e22822f9713474902",
            balance="1000",
            contract_address="inj1t4lnxfu9gtyd50uqmf0ahpwk3vtg5yk9pe7uj4",
            cw20_metadata=cw20_metadata,
            updated_at=1701395446228,
        )

        explorer_servicer.cw20_balance_responses.append(
            exchange_explorer_pb.GetCw20BalanceResponse(field=[wasm_balance])
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcExplorerApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = explorer_servicer

        result_wasm_contract = await api.fetch_cw20_balance(
            address=wasm_balance.account,
            pagination=PaginationOption(
                limit=100,
            ),
        )
        expected_wasm_contract = {
            "field": [
                {
                    "account": wasm_balance.account,
                    "balance": wasm_balance.balance,
                    "contractAddress": wasm_balance.contract_address,
                    "cw20Metadata": {
                        "tokenInfo": {
                            "name": token_info.name,
                            "symbol": token_info.symbol,
                            "decimals": str(token_info.decimals),
                            "totalSupply": token_info.total_supply,
                        },
                        "marketingInfo": {
                            "project": marketing_info.project,
                            "description": marketing_info.description,
                            "logo": marketing_info.logo,
                            "marketing": base64.b64encode(marketing_info.marketing).decode(),
                        },
                    },
                    "updatedAt": str(wasm_balance.updated_at),
                },
            ]
        }

        assert result_wasm_contract == expected_wasm_contract

    @pytest.mark.asyncio
    async def test_fetch_relayers(
        self,
        explorer_servicer,
    ):
        relayer = exchange_explorer_pb.Relayer(
            name="Injdojo",
            cta="https://injdojo.exchange",
        )
        relayers = exchange_explorer_pb.RelayerMarkets(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe", relayers=[relayer]
        )

        explorer_servicer.relayers_responses.append(exchange_explorer_pb.RelayersResponse(field=[relayers]))

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcExplorerApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = explorer_servicer

        result_wasm_contract = await api.fetch_relayers(
            market_ids=[relayers.market_id],
        )
        expected_wasm_contract = {
            "field": [
                {
                    "marketId": relayers.market_id,
                    "relayers": [
                        {
                            "name": relayer.name,
                            "cta": relayer.cta,
                        },
                    ],
                },
            ]
        }

        assert result_wasm_contract == expected_wasm_contract

    @pytest.mark.asyncio
    async def test_fetch_bank_transfers(
        self,
        explorer_servicer,
    ):
        coin = exchange_explorer_pb.Coin(
            denom="inj",
            amount="200000000000000",
        )
        bank_transfer = exchange_explorer_pb.BankTransfer(
            sender="inj17xpfvakm2amg962yls6f84z3kell8c5l6s5ye9",
            recipient="inj1jv65s3grqf6v6jl3dp4t6c9t9rk99cd8dkncm8",
            amounts=[coin],
            block_number=52990746,
            block_timestamp="2023-12-01 14:25:28.266 +0000 UTC",
        )

        paging = exchange_explorer_pb.Paging(total=5, to=5, count_by_subaccount=10, next=["next1", "next2"])
        setattr(paging, "from", 1)

        explorer_servicer.bank_transfers_responses.append(
            exchange_explorer_pb.GetBankTransfersResponse(paging=paging, data=[bank_transfer])
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcExplorerApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = explorer_servicer

        result_transfers = await api.fetch_bank_transfers(
            senders=[bank_transfer.sender],
            recipients=[bank_transfer.recipient],
            is_community_pool_related=False,
            address=["inj1t4lnxfu9gtyd50uqmf0ahpwk3vtg5yk9pe7uj4"],
            per_page=20,
            token="inj",
            pagination=PaginationOption(
                skip=0,
                limit=100,
                start_time=1699544939364,
                end_time=1699744939364,
            ),
        )
        expected_transfers = {
            "data": [
                {
                    "sender": bank_transfer.sender,
                    "recipient": bank_transfer.recipient,
                    "amounts": [
                        {
                            "denom": coin.denom,
                            "amount": coin.amount,
                        }
                    ],
                    "blockNumber": str(bank_transfer.block_number),
                    "blockTimestamp": bank_transfer.block_timestamp,
                },
            ],
            "paging": {
                "total": str(paging.total),
                "from": getattr(paging, "from"),
                "to": paging.to,
                "countBySubaccount": str(paging.count_by_subaccount),
                "next": paging.next,
            },
        }

        assert result_transfers == expected_transfers

    async def _dummy_metadata_provider(self):
        return None
