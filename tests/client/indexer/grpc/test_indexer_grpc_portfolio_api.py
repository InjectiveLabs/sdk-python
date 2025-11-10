import grpc
import pytest

from pyinjective.client.indexer.grpc.indexer_grpc_portfolio_api import IndexerGrpcPortfolioApi
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.exchange import injective_portfolio_rpc_pb2 as exchange_portfolio_pb
from tests.client.indexer.configurable_portfolio_query_servicer import ConfigurablePortfolioQueryServicer


@pytest.fixture
def portfolio_servicer():
    return ConfigurablePortfolioQueryServicer()


class TestIndexerGrpcPortfolioApi:
    @pytest.mark.asyncio
    async def test_fetch_account_portfolio(
        self,
        portfolio_servicer,
    ):
        coin = exchange_portfolio_pb.Coin(
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            amount="2322098",
            usd_value="1000000000000000000",
        )
        subaccount_deposit = exchange_portfolio_pb.SubaccountDeposit(
            total_balance="0.170858923182467801",
            available_balance="0.170858923182467801",
            total_balance_usd="200.000000000000000000",
            available_balance_usd="112.000000000000000000",
        )
        subaccount_balance = exchange_portfolio_pb.SubaccountBalanceV2(
            subaccount_id="0xc7dca7c15c364865f77a4fb67ab11dc95502e6fe000000000000000000000000",
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            deposit=subaccount_deposit,
        )
        position = exchange_portfolio_pb.DerivativePosition(
            ticker="INJ/USDT PERP",
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            subaccount_id="0x1383dabde57e5aed55960ee43e158ae7118057d3000000000000000000000000",
            direction="short",
            quantity="0.070294765766186502",
            entry_price="15980281.340438795311756847",
            margin="561065.540974",
            liquidation_price="23492052.224777",
            mark_price="16197000",
            aggregate_reduce_only_quantity="0",
            updated_at=1700161202147,
            created_at=-62135596800000,
            funding_last="1000.123456789",
            funding_sum="9999.123456789",
        )
        positions_with_upnl = exchange_portfolio_pb.PositionsWithUPNL(
            position=position,
            unrealized_pnl="-364.479654577777780880",
        )

        portfolio = exchange_portfolio_pb.Portfolio(
            account_address="inj1clw20s2uxeyxtam6f7m84vgae92s9eh7vygagt",
            bank_balances=[coin],
            subaccounts=[subaccount_balance],
            positions_with_upnl=[positions_with_upnl],
        )

        portfolio_servicer.account_portfolio_responses.append(
            exchange_portfolio_pb.AccountPortfolioResponse(
                portfolio=portfolio,
            )
        )

        api = self._api_instance(servicer=portfolio_servicer)

        result_auction = await api.fetch_account_portfolio(account_address=portfolio.account_address)
        expected_auction = {
            "portfolio": {
                "accountAddress": portfolio.account_address,
                "bankBalances": [
                    {
                        "denom": coin.denom,
                        "amount": coin.amount,
                        "usdValue": coin.usd_value,
                    }
                ],
                "subaccounts": [
                    {
                        "subaccountId": subaccount_balance.subaccount_id,
                        "denom": subaccount_balance.denom,
                        "deposit": {
                            "totalBalance": subaccount_deposit.total_balance,
                            "availableBalance": subaccount_deposit.available_balance,
                            "totalBalanceUsd": subaccount_deposit.total_balance_usd,
                            "availableBalanceUsd": subaccount_deposit.available_balance_usd,
                        },
                    }
                ],
                "positionsWithUpnl": [
                    {
                        "position": {
                            "ticker": position.ticker,
                            "marketId": position.market_id,
                            "subaccountId": position.subaccount_id,
                            "direction": position.direction,
                            "quantity": position.quantity,
                            "entryPrice": position.entry_price,
                            "margin": position.margin,
                            "liquidationPrice": position.liquidation_price,
                            "markPrice": position.mark_price,
                            "aggregateReduceOnlyQuantity": position.aggregate_reduce_only_quantity,
                            "createdAt": str(position.created_at),
                            "updatedAt": str(position.updated_at),
                            "fundingLast": position.funding_last,
                            "fundingSum": position.funding_sum,
                        },
                        "unrealizedPnl": positions_with_upnl.unrealized_pnl,
                    },
                ],
            }
        }

        assert result_auction == expected_auction

    @pytest.mark.asyncio
    async def test_fetch_account_portfolio_balances(
        self,
        portfolio_servicer,
    ):
        coin = exchange_portfolio_pb.Coin(
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            amount="2322098",
            usd_value="120.000000000000000000",
        )
        subaccount_deposit = exchange_portfolio_pb.SubaccountDeposit(
            total_balance="0.170858923182467801",
            available_balance="0.170858923182467801",
            total_balance_usd="120.000000000000000000",
            available_balance_usd="120.000000000000000000",
        )
        subaccount_balance = exchange_portfolio_pb.SubaccountBalanceV2(
            subaccount_id="0xc7dca7c15c364865f77a4fb67ab11dc95502e6fe000000000000000000000000",
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            deposit=subaccount_deposit,
        )

        portfolio = exchange_portfolio_pb.PortfolioBalances(
            account_address="inj1clw20s2uxeyxtam6f7m84vgae92s9eh7vygagt",
            bank_balances=[coin],
            subaccounts=[subaccount_balance],
            total_usd="300.000000000000000000",
        )

        portfolio_servicer.account_portfolio_balances_responses.append(
            exchange_portfolio_pb.AccountPortfolioBalancesResponse(
                portfolio=portfolio,
            )
        )

        api = self._api_instance(servicer=portfolio_servicer)

        result_auction = await api.fetch_account_portfolio_balances(account_address=portfolio.account_address, usd=True)
        expected_auction = {
            "portfolio": {
                "accountAddress": portfolio.account_address,
                "bankBalances": [
                    {
                        "denom": coin.denom,
                        "amount": coin.amount,
                        "usdValue": coin.usd_value,
                    }
                ],
                "subaccounts": [
                    {
                        "subaccountId": subaccount_balance.subaccount_id,
                        "denom": subaccount_balance.denom,
                        "deposit": {
                            "totalBalance": subaccount_deposit.total_balance,
                            "availableBalance": subaccount_deposit.available_balance,
                            "totalBalanceUsd": subaccount_deposit.total_balance_usd,
                            "availableBalanceUsd": subaccount_deposit.available_balance_usd,
                        },
                    }
                ],
                "totalUsd": portfolio.total_usd,
            }
        }

        assert result_auction == expected_auction

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = IndexerGrpcPortfolioApi(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer

        return api
