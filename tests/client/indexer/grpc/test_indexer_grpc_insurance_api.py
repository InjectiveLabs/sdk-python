import grpc
import pytest

from pyinjective.client.indexer.grpc.indexer_grpc_insurance_api import IndexerGrpcInsuranceApi
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.exchange import injective_insurance_rpc_pb2 as exchange_insurance_pb
from tests.client.indexer.configurable_insurance_query_servicer import ConfigurableInsuranceQueryServicer


@pytest.fixture
def insurance_servicer():
    return ConfigurableInsuranceQueryServicer()


class TestIndexerGrpcInsuranceApi:
    @pytest.mark.asyncio
    async def test_fetch_insurance_funds(
        self,
        insurance_servicer,
    ):
        insurance_fund = exchange_insurance_pb.InsuranceFund(
            market_ticker="inj/usdt",
            market_id="0x7f15b4f4484e6820fc446e42cd447ca6d9bfd7c0592304294270c2bef5f589cd",
            deposit_denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            pool_token_denom="share132",
            redemption_notice_period_duration=1209600,
            balance="920389040000",
            total_share="1000000000000000000",
            oracle_base="0x31775e1d6897129e8a84eeba975778fb50015b88039e9bc140bbd839694ac0ae",
            oracle_quote="USD",
            oracle_type="coinbase",
            expiry=1696539600,
        )

        insurance_servicer.funds_responses.append(
            exchange_insurance_pb.FundsResponse(
                funds=[insurance_fund],
            )
        )

        api = self._api_instance(servicer=insurance_servicer)

        result_insurance_list = await api.fetch_insurance_funds()
        expected_insurance_list = {
            "funds": [
                {
                    "marketTicker": insurance_fund.market_ticker,
                    "marketId": insurance_fund.market_id,
                    "depositDenom": insurance_fund.deposit_denom,
                    "poolTokenDenom": insurance_fund.pool_token_denom,
                    "redemptionNoticePeriodDuration": str(insurance_fund.redemption_notice_period_duration),
                    "balance": insurance_fund.balance,
                    "totalShare": insurance_fund.total_share,
                    "oracleBase": insurance_fund.oracle_base,
                    "oracleQuote": insurance_fund.oracle_quote,
                    "oracleType": insurance_fund.oracle_type,
                    "expiry": str(insurance_fund.expiry),
                }
            ]
        }

        assert result_insurance_list == expected_insurance_list

    @pytest.mark.asyncio
    async def test_fetch_redemptions(
        self,
        insurance_servicer,
    ):
        redemption_schedule = exchange_insurance_pb.RedemptionSchedule(
            redemption_id=1,
            status="disbursed",
            redeemer="inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku",
            claimable_redemption_time=1674798129093000,
            redemption_amount="500000000000000000",
            redemption_denom="share4",
            requested_at=1673588529093000,
            disbursed_amount="5000000",
            disbursed_denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            disbursed_at=1674798130965000,
        )

        insurance_servicer.redemptions_responses.append(
            exchange_insurance_pb.RedemptionsResponse(
                redemption_schedules=[redemption_schedule],
            )
        )

        api = self._api_instance(servicer=insurance_servicer)

        result_insurance_list = await api.fetch_redemptions(
            address=redemption_schedule.redeemer,
            denom=redemption_schedule.redemption_denom,
            status=redemption_schedule.status,
        )
        expected_insurance_list = {
            "redemptionSchedules": [
                {
                    "redemptionId": str(redemption_schedule.redemption_id),
                    "status": redemption_schedule.status,
                    "redeemer": redemption_schedule.redeemer,
                    "claimableRedemptionTime": str(redemption_schedule.claimable_redemption_time),
                    "redemptionAmount": str(redemption_schedule.redemption_amount),
                    "redemptionDenom": redemption_schedule.redemption_denom,
                    "requestedAt": str(redemption_schedule.requested_at),
                    "disbursedAmount": redemption_schedule.disbursed_amount,
                    "disbursedDenom": redemption_schedule.disbursed_denom,
                    "disbursedAt": str(redemption_schedule.disbursed_at),
                }
            ]
        }

        assert result_insurance_list == expected_insurance_list

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = IndexerGrpcInsuranceApi(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer

        return api
