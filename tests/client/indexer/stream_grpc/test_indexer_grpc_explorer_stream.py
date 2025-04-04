import asyncio

import grpc
import pytest

from pyinjective.client.indexer.grpc_stream.indexer_grpc_explorer_stream import IndexerGrpcExplorerStream
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.exchange import injective_explorer_rpc_pb2 as exchange_explorer_pb
from tests.client.indexer.configurable_explorer_query_servicer import ConfigurableExplorerQueryServicer


@pytest.fixture
def explorer_servicer():
    return ConfigurableExplorerQueryServicer()


class TestIndexerGrpcAuctionStream:
    @pytest.mark.asyncio
    async def test_stream_txs(
        self,
        explorer_servicer,
    ):
        code = 5
        claim_id = 100
        tx_data = exchange_explorer_pb.StreamTxsResponse(
            id="test id",
            block_number=18138926,
            block_timestamp="2023-11-07 23:19:55.371 +0000 UTC",
            hash="0x3790ade2bea6c8605851ec89fa968adf2a2037a5ecac11ca95e99260508a3b7e",
            codespace="test codespace",
            messages='[{"type":"/cosmos.bank.v1beta1.MsgSend",'
            '"value":{"from_address":"inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex",'
            '"to_address":"inj1d6qx83nhx3a3gx7e654x4su8hur5s83u84h2xc",'
            '"amount":[{"denom":"factory/inj17vytdwqczqz72j65saukplrktd4gyfme5agf6c/weth",'
            '"amount":"100000000000000000"}]}}]',
            tx_number=221429,
            error_log="",
            code=code,
            claim_ids=[claim_id],
        )

        explorer_servicer.stream_txs_responses.append(tx_data)

        api = self._api_instance(servicer=explorer_servicer)

        txs_updates = asyncio.Queue()
        end_event = asyncio.Event()

        callback = lambda update: txs_updates.put_nowait(update)
        error_callback = lambda exception: pytest.fail(str(exception))
        end_callback = lambda: end_event.set()

        asyncio.get_event_loop().create_task(
            api.stream_txs(
                callback=callback,
                on_end_callback=end_callback,
                on_status_callback=error_callback,
            )
        )
        expected_update = {
            "id": tx_data.id,
            "blockNumber": str(tx_data.block_number),
            "blockTimestamp": tx_data.block_timestamp,
            "hash": tx_data.hash,
            "codespace": tx_data.codespace,
            "messages": tx_data.messages,
            "txNumber": str(tx_data.tx_number),
            "errorLog": tx_data.error_log,
            "code": tx_data.code,
            "claimIds": [str(claim_id)],
        }

        first_update = await asyncio.wait_for(txs_updates.get(), timeout=1)

        assert first_update == expected_update
        assert end_event.is_set()

    @pytest.mark.asyncio
    async def test_stream_blocks(
        self,
        explorer_servicer,
    ):
        block_info = exchange_explorer_pb.StreamBlocksResponse(
            height=19034578,
            proposer="injvalcons18x63wcw5hjxlf535lgn4qy20yer7mm0qedu0la",
            moniker="InjectiveNode1",
            block_hash="0x7f7bfe8caaa0eed042315d1447ef1ed726a80f5da23fdbe6831fc66775197db1",
            parent_hash="0x44287ba5fad21d0109a3ec6f19d447580763e5a709e5a5ceb767174e99ae3bd8",
            num_pre_commits=20,
            num_txs=4,
            timestamp="2023-11-29 20:23:33.842 +0000 UTC",
            block_unix_timestamp=1699744939364,
        )

        explorer_servicer.stream_blocks_responses.append(block_info)

        api = self._api_instance(servicer=explorer_servicer)

        blocks_updates = asyncio.Queue()
        end_event = asyncio.Event()

        callback = lambda update: blocks_updates.put_nowait(update)
        error_callback = lambda exception: pytest.fail(str(exception))
        end_callback = lambda: end_event.set()

        asyncio.get_event_loop().create_task(
            api.stream_blocks(
                callback=callback,
                on_end_callback=end_callback,
                on_status_callback=error_callback,
            )
        )
        expected_update = {
            "height": str(block_info.height),
            "proposer": block_info.proposer,
            "moniker": block_info.moniker,
            "blockHash": block_info.block_hash,
            "parentHash": block_info.parent_hash,
            "numPreCommits": str(block_info.num_pre_commits),
            "numTxs": str(block_info.num_txs),
            "txs": [],
            "timestamp": block_info.timestamp,
            "blockUnixTimestamp": str(block_info.block_unix_timestamp),
        }

        first_update = await asyncio.wait_for(blocks_updates.get(), timeout=1)

        assert first_update == expected_update
        assert end_event.is_set()

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = IndexerGrpcExplorerStream(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer

        return api
