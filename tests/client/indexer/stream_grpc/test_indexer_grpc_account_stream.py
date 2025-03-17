import asyncio

import grpc
import pytest

from pyinjective.client.indexer.grpc_stream.indexer_grpc_account_stream import IndexerGrpcAccountStream
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.exchange import injective_accounts_rpc_pb2 as exchange_accounts_pb
from tests.client.indexer.configurable_account_query_servicer import ConfigurableAccountQueryServicer


@pytest.fixture
def account_servicer():
    return ConfigurableAccountQueryServicer()


class TestIndexerGrpcAccountStream:
    @pytest.mark.asyncio
    async def test_fetch_portfolio(
        self,
        account_servicer,
    ):
        deposit = exchange_accounts_pb.SubaccountDeposit(
            total_balance="20",
            available_balance="10",
            total_balance_usd="1000000000000000000",
            available_balance_usd="500000000000000000",
        )
        balance = exchange_accounts_pb.SubaccountBalance(
            subaccount_id="0xaf79152ac5df276d9a8e1e2e22822f9713474902000000000000000000000000",
            account_address="inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku",
            denom="inj",
            deposit=deposit,
        )
        account_servicer.stream_subaccount_balance_responses.append(
            exchange_accounts_pb.StreamSubaccountBalanceResponse(balance=balance, timestamp=1672218001897)
        )

        api = self._api_instance(servicer=account_servicer)

        balance_updates = asyncio.Queue()
        end_event = asyncio.Event()

        callback = lambda update: balance_updates.put_nowait(update)
        error_callback = lambda exception: pytest.fail(str(exception))
        end_callback = lambda: end_event.set()

        asyncio.get_event_loop().create_task(
            api.stream_subaccount_balance(
                subaccount_id=balance.subaccount_id,
                callback=callback,
                on_end_callback=end_callback,
                on_status_callback=error_callback,
                denoms=["inj"],
            )
        )
        expected_balance_update = {
            "balance": {
                "accountAddress": balance.account_address,
                "denom": balance.denom,
                "deposit": {
                    "availableBalance": balance.deposit.available_balance,
                    "totalBalance": balance.deposit.total_balance,
                    "totalBalanceUsd": balance.deposit.total_balance_usd,
                    "availableBalanceUsd": balance.deposit.available_balance_usd,
                },
                "subaccountId": balance.subaccount_id,
            },
            "timestamp": "1672218001897",
        }

        first_balance_update = await asyncio.wait_for(balance_updates.get(), timeout=1)

        assert first_balance_update == expected_balance_update
        assert end_event.is_set()

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = IndexerGrpcAccountStream(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer

        return api
