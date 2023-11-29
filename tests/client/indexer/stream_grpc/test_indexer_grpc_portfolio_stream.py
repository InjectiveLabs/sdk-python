import asyncio

import grpc
import pytest

from pyinjective.client.indexer.grpc_stream.indexer_grpc_portfolio_stream import IndexerGrpcPortfolioStream
from pyinjective.core.network import Network
from pyinjective.proto.exchange import injective_portfolio_rpc_pb2 as exchange_portfolio_pb
from tests.client.indexer.configurable_portfolio_query_servicer import ConfigurablePortfolioQueryServicer


@pytest.fixture
def portfolio_servicer():
    return ConfigurablePortfolioQueryServicer()


class TestIndexerGrpcPortfolioStream:
    @pytest.mark.asyncio
    async def test_stream_account_portfolio(
        self,
        portfolio_servicer,
    ):
        update_type = "total_balance"
        denom = "peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5"
        amount = "1000000000000000000"
        subaccount_id = "0xc7dca7c15c364865f77a4fb67ab11dc95502e6fe000000000000000000000000"
        timestamp = 1675426622603

        portfolio_servicer.stream_account_portfolio_responses.append(
            exchange_portfolio_pb.StreamAccountPortfolioResponse(
                type=update_type,
                denom=denom,
                amount=amount,
                subaccount_id=subaccount_id,
                timestamp=timestamp,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcPortfolioStream(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = portfolio_servicer

        portfolio_updates = asyncio.Queue()
        end_event = asyncio.Event()

        callback = lambda update: portfolio_updates.put_nowait(update)
        error_callback = lambda exception: pytest.fail(str(exception))
        end_callback = lambda: end_event.set()

        asyncio.get_event_loop().create_task(
            api.stream_account_portfolio(
                account_address="test_address",
                callback=callback,
                on_end_callback=end_callback,
                on_status_callback=error_callback,
                subaccount_id=subaccount_id,
                update_type=update_type,
            )
        )
        expected_update = {
            "type": update_type,
            "denom": denom,
            "amount": amount,
            "subaccountId": subaccount_id,
            "timestamp": str(timestamp),
        }

        first_update = await asyncio.wait_for(portfolio_updates.get(), timeout=1)

        assert first_update == expected_update
        assert end_event.is_set()

    async def _dummy_metadata_provider(self):
        return None
