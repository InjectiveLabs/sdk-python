import base64

import grpc
import pytest

from pyinjective.client.chain.grpc.chain_grpc_distribution_api import ChainGrpcDistributionApi
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.cosmos.base.query.v1beta1 import pagination_pb2 as pagination_pb
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as coin_pb
from pyinjective.proto.cosmos.distribution.v1beta1 import (
    distribution_pb2 as distribution_pb,
    query_pb2 as distribution_query_pb,
)
from tests.client.chain.grpc.configurable_distribution_query_servicer import ConfigurableDistributionQueryServicer


@pytest.fixture
def distribution_servicer():
    return ConfigurableDistributionQueryServicer()


class TestChainGrpcAuthApi:
    @pytest.mark.asyncio
    async def test_fetch_module_params(
        self,
        distribution_servicer,
    ):
        params = distribution_pb.Params(
            community_tax="0.050000000000000000",
            base_proposer_reward="0.060000000000000000",
            bonus_proposer_reward="0.070000000000000000",
            withdraw_addr_enabled=True,
        )

        distribution_servicer.distribution_params.append(distribution_query_pb.QueryParamsResponse(params=params))

        api = self._api_instance(servicer=distribution_servicer)

        module_params = await api.fetch_module_params()
        expected_params = {
            "params": {
                "communityTax": params.community_tax,
                "baseProposerReward": params.base_proposer_reward,
                "bonusProposerReward": params.bonus_proposer_reward,
                "withdrawAddrEnabled": params.withdraw_addr_enabled,
            }
        }

        assert expected_params == module_params

    @pytest.mark.asyncio
    async def test_fetch_validator_distribution_info(
        self,
        distribution_servicer,
    ):
        operator = "inj1zpy3qf7us3m0pxpqkp72gzjv55t70huyxh7slz"
        reward = coin_pb.DecCoin(denom="inj", amount="1000000000")
        commission = coin_pb.DecCoin(denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5", amount="54497408")

        distribution_servicer.validator_distribution_info_responses.append(
            distribution_query_pb.QueryValidatorDistributionInfoResponse(
                operator_address=operator, self_bond_rewards=[reward], commission=[commission]
            )
        )

        api = self._api_instance(servicer=distribution_servicer)

        validator_info = await api.fetch_validator_distribution_info(validator_address=operator)
        expected_info = {
            "operatorAddress": operator,
            "selfBondRewards": [{"denom": reward.denom, "amount": reward.amount}],
            "commission": [{"denom": commission.denom, "amount": commission.amount}],
        }

        assert expected_info == validator_info

    @pytest.mark.asyncio
    async def test_fetch_validator_outstanding_rewards(
        self,
        distribution_servicer,
    ):
        operator = "inj1zpy3qf7us3m0pxpqkp72gzjv55t70huyxh7slz"
        reward = coin_pb.DecCoin(denom="inj", amount="1000000000")
        rewards = distribution_pb.ValidatorOutstandingRewards(rewards=[reward])

        distribution_servicer.validator_outstanding_rewards_responses.append(
            distribution_query_pb.QueryValidatorOutstandingRewardsResponse(
                rewards=rewards,
            )
        )

        api = self._api_instance(servicer=distribution_servicer)

        validator_rewards = await api.fetch_validator_outstanding_rewards(validator_address=operator)
        expected_rewards = {"rewards": {"rewards": [{"denom": reward.denom, "amount": reward.amount}]}}

        assert expected_rewards == validator_rewards

    @pytest.mark.asyncio
    async def test_fetch_validator_commission(
        self,
        distribution_servicer,
    ):
        operator = "inj1zpy3qf7us3m0pxpqkp72gzjv55t70huyxh7slz"
        first_commission = coin_pb.DecCoin(denom="inj", amount="1000000000")
        commission = distribution_pb.ValidatorAccumulatedCommission(commission=[first_commission])

        distribution_servicer.validator_commission_responses.append(
            distribution_query_pb.QueryValidatorCommissionResponse(
                commission=commission,
            )
        )

        api = self._api_instance(servicer=distribution_servicer)

        commission = await api.fetch_validator_commission(validator_address=operator)
        expected_commission = {
            "commission": {"commission": [{"denom": first_commission.denom, "amount": first_commission.amount}]}
        }

        assert expected_commission == commission

    @pytest.mark.asyncio
    async def test_fetch_validator_slashes(
        self,
        distribution_servicer,
    ):
        operator = "inj1zpy3qf7us3m0pxpqkp72gzjv55t70huyxh7slz"
        slash = distribution_pb.ValidatorSlashEvent(
            validator_period=1,
            fraction="4",
        )
        pagination = pagination_pb.PageResponse(total=2)

        distribution_servicer.validator_slashes_responses.append(
            distribution_query_pb.QueryValidatorSlashesResponse(
                slashes=[slash],
                pagination=pagination,
            )
        )

        api = self._api_instance(servicer=distribution_servicer)

        slashes = await api.fetch_validator_slashes(
            validator_address=operator,
            starting_height=20,
            ending_height=100,
            pagination=PaginationOption(
                skip=0,
                limit=100,
            ),
        )
        expected_slashes = {
            "slashes": [
                {
                    "validatorPeriod": str(slash.validator_period),
                    "fraction": slash.fraction,
                }
            ],
            "pagination": {"nextKey": base64.b64encode(pagination.next_key).decode(), "total": str(pagination.total)},
        }

        assert slashes == expected_slashes

    @pytest.mark.asyncio
    async def test_fetch_delegation_rewards(
        self,
        distribution_servicer,
    ):
        delegator = "inj1cml96vmptgw99syqrrz8az79xer2pcgp0a885r"
        validator = "injvaloper16gdnrnl224ylje5z9vd0vn0msym7p58f00qauj"
        reward = coin_pb.DecCoin(denom="inj", amount="1000000000")

        distribution_servicer.delegation_rewards_responses.append(
            distribution_query_pb.QueryDelegationRewardsResponse(
                rewards=[reward],
            )
        )

        api = self._api_instance(servicer=distribution_servicer)

        rewards = await api.fetch_delegation_rewards(
            delegator_address=delegator,
            validator_address=validator,
        )
        expected_rewards = {"rewards": [{"denom": reward.denom, "amount": reward.amount}]}

        assert rewards == expected_rewards

    @pytest.mark.asyncio
    async def test_fetch_delegation_total_rewards(
        self,
        distribution_servicer,
    ):
        delegator = "inj1cml96vmptgw99syqrrz8az79xer2pcgp0a885r"
        validator = "injvaloper16gdnrnl224ylje5z9vd0vn0msym7p58f00qauj"
        reward = coin_pb.DecCoin(denom="inj", amount="1000000000")
        delegation_delegator_reward = distribution_pb.DelegationDelegatorReward(
            validator_address=validator,
            reward=[reward],
        )
        total = coin_pb.DecCoin(denom="inj", amount="2000000000")

        distribution_servicer.delegation_total_rewards_responses.append(
            distribution_query_pb.QueryDelegationTotalRewardsResponse(
                rewards=[delegation_delegator_reward],
                total=[total],
            )
        )

        api = self._api_instance(servicer=distribution_servicer)

        rewards = await api.fetch_delegation_total_rewards(
            delegator_address=delegator,
        )
        expected_rewards = {
            "rewards": [
                {
                    "validatorAddress": validator,
                    "reward": [{"denom": reward.denom, "amount": reward.amount}],
                }
            ],
            "total": [{"denom": total.denom, "amount": total.amount}],
        }

        assert rewards == expected_rewards

    @pytest.mark.asyncio
    async def test_fetch_delegator_validators(
        self,
        distribution_servicer,
    ):
        delegator = "inj1cml96vmptgw99syqrrz8az79xer2pcgp0a885r"
        validator = "injvaloper16gdnrnl224ylje5z9vd0vn0msym7p58f00qauj"

        distribution_servicer.delegator_validators_responses.append(
            distribution_query_pb.QueryDelegatorValidatorsResponse(
                validators=[validator],
            )
        )

        api = self._api_instance(servicer=distribution_servicer)

        validators = await api.fetch_delegator_validators(
            delegator_address=delegator,
        )
        expected_validators = {
            "validators": [validator],
        }

        assert validators == expected_validators

    @pytest.mark.asyncio
    async def test_fetch_delegator_withdraw_address(
        self,
        distribution_servicer,
    ):
        delegator = "inj1cml96vmptgw99syqrrz8az79xer2pcgp0a885r"

        distribution_servicer.delegator_withdraw_address_responses.append(
            distribution_query_pb.QueryDelegatorWithdrawAddressResponse(
                withdraw_address=delegator,
            )
        )

        api = self._api_instance(servicer=distribution_servicer)

        withdraw_address = await api.fetch_delegator_withdraw_address(
            delegator_address=delegator,
        )
        expected_withdraw_address = {
            "withdrawAddress": delegator,
        }

        assert withdraw_address == expected_withdraw_address

    @pytest.mark.asyncio
    async def test_fetch_community_pool(
        self,
        distribution_servicer,
    ):
        coin = coin_pb.DecCoin(denom="inj", amount="1000000000")
        distribution_servicer.community_pool_responses.append(
            distribution_query_pb.QueryCommunityPoolResponse(
                pool=[coin],
            )
        )

        api = self._api_instance(servicer=distribution_servicer)

        community_pool = await api.fetch_community_pool()
        expected_community_pool = {"pool": [{"denom": coin.denom, "amount": coin.amount}]}

        assert community_pool == expected_community_pool

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = ChainGrpcDistributionApi(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer

        return api
