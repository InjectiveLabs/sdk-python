import grpc
import pytest
from google.protobuf import duration_pb2
from google.protobuf import timestamp_pb2

from pyinjective.client.chain.grpc.chain_grpc_insurance_api import ChainGrpcInsuranceApi
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as coin_pb
from pyinjective.proto.injective.common.vouchers.v1 import vouchers_pb2 as vouchers_pb
from pyinjective.proto.injective.insurance.v1beta1 import (
    genesis_pb2 as genesis_pb,
    insurance_pb2 as insurance_pb,
    query_pb2 as insurance_query_pb,
)
from pyinjective.proto.injective.oracle.v1beta1 import oracle_pb2 as oracle_pb
from tests.client.chain.grpc.configurable_insurance_query_servicer import ConfigurableInsuranceQueryServicer


@pytest.fixture
def insurance_servicer():
    return ConfigurableInsuranceQueryServicer()


class TestChainGrpcInsuranceApi:
    @pytest.mark.asyncio
    async def test_fetch_module_params(self, insurance_servicer):
        dur = duration_pb2.Duration(seconds=3600)
        params = insurance_pb.Params(default_redemption_notice_period_duration=dur)
        insurance_servicer.insurance_params.append(
            insurance_query_pb.QueryInsuranceParamsResponse(params=params)
        )

        api = self._api_instance(servicer=insurance_servicer)
        result = await api.fetch_module_params()

        assert result == {
            "params": {
                "defaultRedemptionNoticePeriodDuration": "3600s",
            }
        }

    @pytest.mark.asyncio
    async def test_fetch_insurance_fund(self, insurance_servicer):
        dur = duration_pb2.Duration(seconds=3600)
        fund = insurance_pb.InsuranceFund(
            deposit_denom="inj",
            insurance_pool_token_denom="pool",
            redemption_notice_period_duration=dur,
            balance="100",
            total_share="50",
            market_id="m1",
            market_ticker="MT",
            oracle_base="b",
            oracle_quote="q",
            oracle_type=oracle_pb.OracleType.Value("Band"),
            expiry=123,
        )
        insurance_servicer.insurance_fund_responses.append(
            insurance_query_pb.QueryInsuranceFundResponse(fund=fund)
        )

        api = self._api_instance(servicer=insurance_servicer)
        result = await api.fetch_insurance_fund(market_id="m1")

        assert result == {
            "fund": {
                "depositDenom": "inj",
                "insurancePoolTokenDenom": "pool",
                "redemptionNoticePeriodDuration": "3600s",
                "balance": "100",
                "totalShare": "50",
                "marketId": "m1",
                "marketTicker": "MT",
                "oracleBase": "b",
                "oracleQuote": "q",
                "oracleType": "Band",
                "expiry": "123",
            }
        }

    @pytest.mark.asyncio
    async def test_fetch_insurance_funds(self, insurance_servicer):
        dur = duration_pb2.Duration(seconds=3600)
        fund = insurance_pb.InsuranceFund(
            deposit_denom="inj",
            insurance_pool_token_denom="pool",
            redemption_notice_period_duration=dur,
            balance="100",
            total_share="50",
            market_id="m1",
            market_ticker="MT",
            oracle_base="b",
            oracle_quote="q",
            oracle_type=oracle_pb.OracleType.Value("Band"),
            expiry=123,
        )
        insurance_servicer.insurance_funds_responses.append(
            insurance_query_pb.QueryInsuranceFundsResponse(funds=[fund])
        )

        api = self._api_instance(servicer=insurance_servicer)
        result = await api.fetch_insurance_funds()

        assert result == {
            "funds": [
                {
                    "depositDenom": "inj",
                    "insurancePoolTokenDenom": "pool",
                    "redemptionNoticePeriodDuration": "3600s",
                    "balance": "100",
                    "totalShare": "50",
                    "marketId": "m1",
                    "marketTicker": "MT",
                    "oracleBase": "b",
                    "oracleQuote": "q",
                    "oracleType": "Band",
                    "expiry": "123",
                }
            ]
        }

    @pytest.mark.asyncio
    async def test_fetch_estimated_redemptions(self, insurance_servicer):
        insurance_servicer.estimated_redemptions_responses.append(
            insurance_query_pb.QueryEstimatedRedemptionsResponse(
                amount=[coin_pb.Coin(denom="inj", amount="1")]
            )
        )

        api = self._api_instance(servicer=insurance_servicer)
        result = await api.fetch_estimated_redemptions(market_id="m1", address="addr1")

        assert result == {
            "amount": [
                {
                    "denom": "inj",
                    "amount": "1",
                }
            ]
        }

    @pytest.mark.asyncio
    async def test_fetch_pending_redemptions(self, insurance_servicer):
        insurance_servicer.pending_redemptions_responses.append(
            insurance_query_pb.QueryPendingRedemptionsResponse(
                amount=[coin_pb.Coin(denom="inj", amount="2")]
            )
        )

        api = self._api_instance(servicer=insurance_servicer)
        result = await api.fetch_pending_redemptions(market_id="m2", address="addr2")

        assert result == {
            "amount": [
                {
                    "denom": "inj",
                    "amount": "2",
                }
            ]
        }

    @pytest.mark.asyncio
    async def test_fetch_module_state(self, insurance_servicer):
        state = genesis_pb.GenesisState()
        insurance_servicer.module_states.append(insurance_query_pb.QueryModuleStateResponse(state=state))

        api = self._api_instance(servicer=insurance_servicer)
        result = await api.fetch_module_state()

        assert result == {
            "state": {
                "insuranceFunds": [],
                "redemptionSchedule": [],
                "nextShareDenomId": "0",
                "nextRedemptionScheduleId": "0",
                "failedRedemptionSchedules": [],
                "nextFailedRedemptionScheduleId": "0",
                "vouchers": [],
            }
        }

    @pytest.mark.asyncio
    async def test_fetch_failed_redemptions(self, insurance_servicer):
        ts = timestamp_pb2.Timestamp(seconds=1, nanos=0)
        schedule = insurance_pb.RedemptionSchedule(
            id=2,
            marketId="m",
            redeemer="r",
            claimable_redemption_time=ts,
            redemption_amount=coin_pb.Coin(denom="inj", amount="1"),
        )
        failed = insurance_pb.FailedRedemptionSchedule(id=1, schedule=schedule, err="e")
        insurance_servicer.failed_redemptions_responses.append(
            insurance_query_pb.QueryFailedRedemptionsResponse(schedules=[failed])
        )

        api = self._api_instance(servicer=insurance_servicer)
        result = await api.fetch_failed_redemptions()

        assert result == {
            "schedules": [
                {
                    "id": "1",
                    "schedule": {
                        "id": "2",
                        "marketId": "m",
                        "redeemer": "r",
                        "claimableRedemptionTime": "1970-01-01T00:00:01Z",
                        "redemptionAmount": {
                            "denom": "inj",
                            "amount": "1",
                        },
                    },
                    "err": "e",
                }
            ]
        }

    @pytest.mark.asyncio
    async def test_fetch_vouchers(self, insurance_servicer):
        voucher = vouchers_pb.AddressVoucher(
            address="inj1ady3s7whq30l4fx8sj3x6muv5mx4dfdlcpv8n7",
            voucher=coin_pb.Coin(denom="inj", amount="1000000000"),
        )
        insurance_servicer.vouchers_responses.append(
            insurance_query_pb.QueryVouchersResponse(vouchers=[voucher])
        )

        api = self._api_instance(servicer=insurance_servicer)
        result = await api.fetch_vouchers(denom="inj")

        assert result == {
            "vouchers": [
                {
                    "address": voucher.address,
                    "voucher": {
                        "denom": voucher.voucher.denom,
                        "amount": voucher.voucher.amount,
                    },
                }
            ]
        }

    @pytest.mark.asyncio
    async def test_fetch_voucher(self, insurance_servicer):
        voucher = coin_pb.Coin(denom="inj", amount="1000000000")
        insurance_servicer.voucher_responses.append(insurance_query_pb.QueryVoucherResponse(voucher=voucher))

        api = self._api_instance(servicer=insurance_servicer)
        result = await api.fetch_voucher(
            denom="inj",
            address="inj1ady3s7whq30l4fx8sj3x6muv5mx4dfdlcpv8n7",
        )

        assert result == {
            "voucher": {
                "denom": voucher.denom,
                "amount": voucher.amount,
            }
        }

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = ChainGrpcInsuranceApi(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer

        return api
