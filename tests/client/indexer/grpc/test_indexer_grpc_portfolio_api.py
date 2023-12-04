import grpc
import pytest

from pyinjective.client.indexer.grpc.indexer_grpc_portfolio_api import IndexerGrpcPortfolioApi
from pyinjective.core.network import Network
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
        )
        subaccount_deposit = exchange_portfolio_pb.SubaccountDeposit(
            total_balance="0.170858923182467801",
            available_balance="0.170858923182467801",
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

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_exchange_endpoint)

        api = IndexerGrpcPortfolioApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = portfolio_servicer

        result_auction = await api.fetch_account_portfolio(account_address=portfolio.account_address)
        expected_auction = {
            "portfolio": {
                "accountAddress": portfolio.account_address,
                "bankBalances": [
                    {
                        "denom": coin.denom,
                        "amount": coin.amount,
                    }
                ],
                "subaccounts": [
                    {
                        "subaccountId": subaccount_balance.subaccount_id,
                        "denom": subaccount_balance.denom,
                        "deposit": {
                            "totalBalance": subaccount_deposit.total_balance,
                            "availableBalance": subaccount_deposit.available_balance,
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
                        },
                        "unrealizedPnl": positions_with_upnl.unrealized_pnl,
                    },
                ],
            }
        }

        assert result_auction == expected_auction

    async def _dummy_metadata_provider(self):
        return None
