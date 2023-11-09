import time

import grpc
import pytest

from pyinjective.client.indexer.grpc.indexer_grpc_account_api import IndexerGrpcAccountApi
from pyinjective.core.network import Network
from pyinjective.proto.exchange import injective_accounts_rpc_pb2 as exchange_accounts_pb
from tests.client.indexer.configurable_account_query_servicer import ConfigurableAccountQueryServicer


@pytest.fixture
def account_servicer():
    return ConfigurableAccountQueryServicer()


class TestIndexerGrpcAccountApi:
    @pytest.mark.asyncio
    async def test_fetch_portfolio(
        self,
        account_servicer,
    ):
        subaccount_portfolio = exchange_accounts_pb.SubaccountPortfolio(
            subaccount_id="0xaf79152ac5df276d9a8e1e2e22822f9713474902000000000000000000000006",
            available_balance="1",
            locked_balance="2",
            unrealized_pnl="3",
        )
        portfolio = exchange_accounts_pb.AccountPortfolio(
            portfolio_value="173706.418",
            available_balance="99.8782",
            locked_balance="186055.7038",
            unrealized_pnl="-12449.1635",
            subaccounts=[subaccount_portfolio],
        )
        account_servicer.portfolio_responses.append(exchange_accounts_pb.PortfolioResponse(portfolio=portfolio))

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcAccountApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = account_servicer

        account_address = "inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku"
        result_portfolio = await api.fetch_portfolio(account_address=account_address)
        expected_portfolio = {
            "portfolio": {
                "portfolioValue": portfolio.portfolio_value,
                "availableBalance": portfolio.available_balance,
                "lockedBalance": portfolio.locked_balance,
                "unrealizedPnl": portfolio.unrealized_pnl,
                "subaccounts": [
                    {
                        "subaccountId": subaccount_portfolio.subaccount_id,
                        "availableBalance": subaccount_portfolio.available_balance,
                        "lockedBalance": subaccount_portfolio.locked_balance,
                        "unrealizedPnl": subaccount_portfolio.unrealized_pnl,
                    },
                ],
            }
        }

        assert expected_portfolio == result_portfolio

    @pytest.mark.asyncio
    async def test_order_states(
        self,
        account_servicer,
    ):
        order_state = exchange_accounts_pb.OrderStateRecord(
            order_hash="0xce0d9b701f77cd6ddfda5dd3a4fe7b2d53ba83e5d6c054fb2e9e886200b7b7bb",
            subaccount_id="0xaf79152ac5df276d9a8e1e2e22822f9713474902000000000000000000000006",
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            order_type="buy_po",
            order_side="buy",
            state="canceled",
            quantity_filled="0",
            quantity_remaining="1000000000000000",
            created_at=1669998526840,
            updated_at=1670919410587,
        )
        account_servicer.order_states_responses.append(
            exchange_accounts_pb.OrderStatesResponse(spot_order_states=[order_state])
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcAccountApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = account_servicer

        result_order_states = await api.fetch_order_states(spot_order_hashes=[order_state.order_hash])
        expected_order_states = {
            "spotOrderStates": [
                {
                    "orderHash": order_state.order_hash,
                    "subaccountId": order_state.subaccount_id,
                    "marketId": order_state.market_id,
                    "orderType": order_state.order_type,
                    "orderSide": order_state.order_side,
                    "state": order_state.state,
                    "quantityFilled": order_state.quantity_filled,
                    "quantityRemaining": order_state.quantity_remaining,
                    "createdAt": str(order_state.created_at),
                    "updatedAt": str(order_state.updated_at),
                }
            ],
            "derivativeOrderStates": [],
        }

        assert result_order_states == expected_order_states

    @pytest.mark.asyncio
    async def test_subaccounts_list(
        self,
        account_servicer,
    ):
        account_servicer.subaccounts_list_responses.append(
            exchange_accounts_pb.SubaccountsListResponse(
                subaccounts=["0xaf79152ac5df276d9a8e1e2e22822f9713474902000000000000000000000006"]
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcAccountApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = account_servicer

        result_subaccounts_list = await api.fetch_subaccounts_list(address="testAddress")
        expected_subaccounts_list = {
            "subaccounts": ["0xaf79152ac5df276d9a8e1e2e22822f9713474902000000000000000000000006"]
        }

        assert result_subaccounts_list == expected_subaccounts_list

    @pytest.mark.asyncio
    async def test_subaccount_balances_list(
        self,
        account_servicer,
    ):
        deposit = exchange_accounts_pb.SubaccountDeposit(
            total_balance="20",
            available_balance="10",
        )
        balance = exchange_accounts_pb.SubaccountBalance(
            subaccount_id="0xaf79152ac5df276d9a8e1e2e22822f9713474902000000000000000000000000",
            account_address="inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku",
            denom="inj",
            deposit=deposit,
        )
        account_servicer.subaccount_balances_list_responses.append(
            exchange_accounts_pb.SubaccountBalancesListResponse(balances=[balance])
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcAccountApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = account_servicer

        result_subaccount_balances_list = await api.fetch_subaccount_balances_list(
            subaccount_id=balance.subaccount_id, denoms=[balance.denom]
        )
        expected_subaccount_balances_list = {
            "balances": [
                {
                    "subaccountId": balance.subaccount_id,
                    "accountAddress": balance.account_address,
                    "denom": balance.denom,
                    "deposit": {
                        "totalBalance": deposit.total_balance,
                        "availableBalance": deposit.available_balance,
                    },
                },
            ]
        }

        assert result_subaccount_balances_list == expected_subaccount_balances_list

    @pytest.mark.asyncio
    async def test_subaccount_balance(
        self,
        account_servicer,
    ):
        deposit = exchange_accounts_pb.SubaccountDeposit(
            total_balance="20",
            available_balance="10",
        )
        balance = exchange_accounts_pb.SubaccountBalance(
            subaccount_id="0xaf79152ac5df276d9a8e1e2e22822f9713474902000000000000000000000000",
            account_address="inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku",
            denom="inj",
            deposit=deposit,
        )
        account_servicer.subaccount_balance_responses.append(
            exchange_accounts_pb.SubaccountBalanceEndpointResponse(balance=balance)
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcAccountApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = account_servicer

        result_subaccount_balance = await api.fetch_subaccount_balance(
            subaccount_id=balance.subaccount_id,
            denom=balance.denom,
        )
        expected_subaccount_balance = {
            "balance": {
                "subaccountId": balance.subaccount_id,
                "accountAddress": balance.account_address,
                "denom": balance.denom,
                "deposit": {
                    "totalBalance": deposit.total_balance,
                    "availableBalance": deposit.available_balance,
                },
            },
        }

        assert result_subaccount_balance == expected_subaccount_balance

    @pytest.mark.asyncio
    async def test_subaccount_history(
        self,
        account_servicer,
    ):
        transfer = exchange_accounts_pb.SubaccountBalanceTransfer(
            transfer_type="deposit",
            src_account_address="inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku",
            dst_subaccount_id="0xaf79152ac5df276d9a8e1e2e22822f9713474902000000000000000000000000",
            amount=exchange_accounts_pb.CosmosCoin(
                denom="inj",
                amount="2000000000000000000",
            ),
            executed_at=1665117493543,
            src_subaccount_id="",
            dst_account_address="",
        )

        paging = exchange_accounts_pb.Paging(total=5, to=5, count_by_subaccount=10, next=["next1", "next2"])
        setattr(paging, "from", 1)

        account_servicer.subaccount_history_responses.append(
            exchange_accounts_pb.SubaccountHistoryResponse(transfers=[transfer], paging=paging)
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcAccountApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = account_servicer

        result_subaccount_history = await api.fetch_subaccount_history(
            subaccount_id=transfer.dst_subaccount_id,
            denom=transfer.amount.denom,
            transfer_types=[transfer.transfer_type],
            skip=0,
            limit=5,
            end_time=int(time.time() * 1e3),
        )
        expected_subaccount_history = {
            "transfers": [
                {
                    "transferType": transfer.transfer_type,
                    "srcAccountAddress": transfer.src_account_address,
                    "dstSubaccountId": transfer.dst_subaccount_id,
                    "amount": {"denom": transfer.amount.denom, "amount": "2000000000000000000"},
                    "executedAt": str(transfer.executed_at),
                    "srcSubaccountId": transfer.src_subaccount_id,
                    "dstAccountAddress": transfer.dst_account_address,
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

        assert result_subaccount_history == expected_subaccount_history

    @pytest.mark.asyncio
    async def test_subaccount_order_summary(
        self,
        account_servicer,
    ):
        account_servicer.subaccount_order_summary_responses.append(
            exchange_accounts_pb.SubaccountOrderSummaryResponse(spot_orders_total=0, derivative_orders_total=20)
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcAccountApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = account_servicer

        result_subaccount_order_summary = await api.fetch_subaccount_order_summary(
            subaccount_id="0xaf79152ac5df276d9a8e1e2e22822f9713474902000000000000000000000000",
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            order_direction="buy",
        )
        expected_subaccount_order_summary = {"derivativeOrdersTotal": "20", "spotOrdersTotal": "0"}

        assert result_subaccount_order_summary == expected_subaccount_order_summary

    @pytest.mark.asyncio
    async def test_fetch_rewards(
        self,
        account_servicer,
    ):
        single_reward = exchange_accounts_pb.Coin(
            denom="inj",
            amount="2000000000000000000",
        )

        reward = exchange_accounts_pb.Reward(
            account_address="inj1qra8c03h70y36j85dpvtj05juxe9z7acuvz6vg",
            rewards=[single_reward],
            distributed_at=1672218001897,
        )

        account_servicer.rewards_responses.append(exchange_accounts_pb.RewardsResponse(rewards=[reward]))

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcAccountApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = account_servicer

        result_rewards = await api.fetch_rewards(account_address=reward.account_address, epoch=1)
        expected_rewards = {
            "rewards": [
                {
                    "accountAddress": reward.account_address,
                    "rewards": [
                        {
                            "denom": single_reward.denom,
                            "amount": single_reward.amount,
                        }
                    ],
                    "distributedAt": str(reward.distributed_at),
                }
            ]
        }

        assert result_rewards == expected_rewards

    @pytest.mark.asyncio
    async def test_fetch_rewards(
        self,
        account_servicer,
    ):
        single_reward = exchange_accounts_pb.Coin(
            denom="inj",
            amount="2000000000000000000",
        )

        reward = exchange_accounts_pb.Reward(
            account_address="inj1qra8c03h70y36j85dpvtj05juxe9z7acuvz6vg",
            rewards=[single_reward],
            distributed_at=1672218001897,
        )

        account_servicer.rewards_responses.append(exchange_accounts_pb.RewardsResponse(rewards=[reward]))

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcAccountApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = account_servicer

        result_rewards = await api.fetch_rewards(account_address=reward.account_address, epoch=1)
        expected_rewards = {
            "rewards": [
                {
                    "accountAddress": reward.account_address,
                    "rewards": [
                        {
                            "denom": single_reward.denom,
                            "amount": single_reward.amount,
                        }
                    ],
                    "distributedAt": str(reward.distributed_at),
                }
            ]
        }

        assert result_rewards == expected_rewards

    async def _dummy_metadata_provider(self):
        return None
