from collections import deque

from pyinjective.proto.cosmos.distribution.v1beta1 import (
    query_pb2 as distribution_query_pb,
    query_pb2_grpc as distribution_query_grpc,
)


class ConfigurableDistributionQueryServicer(distribution_query_grpc.QueryServicer):
    def __init__(self):
        super().__init__()
        self.distribution_params = deque()
        self.validator_distribution_info_responses = deque()
        self.validator_outstanding_rewards_responses = deque()
        self.validator_commission_responses = deque()
        self.validator_slashes_responses = deque()
        self.delegation_rewards_responses = deque()
        self.delegation_total_rewards_responses = deque()
        self.delegator_validators_responses = deque()
        self.delegator_withdraw_address_responses = deque()
        self.community_pool_responses = deque()

    async def Params(self, request: distribution_query_pb.QueryParamsRequest, context=None, metadata=None):
        return self.distribution_params.pop()

    async def ValidatorDistributionInfo(
        self, request: distribution_query_pb.QueryValidatorDistributionInfoRequest, context=None, metadata=None
    ):
        return self.validator_distribution_info_responses.pop()

    async def ValidatorOutstandingRewards(
        self, request: distribution_query_pb.QueryValidatorOutstandingRewardsRequest, context=None, metadata=None
    ):
        return self.validator_outstanding_rewards_responses.pop()

    async def ValidatorCommission(
        self, request: distribution_query_pb.QueryValidatorCommissionRequest, context=None, metadata=None
    ):
        return self.validator_commission_responses.pop()

    async def ValidatorSlashes(
        self, request: distribution_query_pb.QueryValidatorSlashesRequest, context=None, metadata=None
    ):
        return self.validator_slashes_responses.pop()

    async def DelegationRewards(
        self, request: distribution_query_pb.QueryDelegationRewardsRequest, context=None, metadata=None
    ):
        return self.delegation_rewards_responses.pop()

    async def DelegationTotalRewards(
        self, request: distribution_query_pb.QueryDelegationTotalRewardsRequest, context=None, metadata=None
    ):
        return self.delegation_total_rewards_responses.pop()

    async def DelegatorValidators(
        self, request: distribution_query_pb.QueryDelegatorValidatorsRequest, context=None, metadata=None
    ):
        return self.delegator_validators_responses.pop()

    async def DelegatorWithdrawAddress(
        self, request: distribution_query_pb.QueryDelegatorWithdrawAddressRequest, context=None, metadata=None
    ):
        return self.delegator_withdraw_address_responses.pop()

    async def CommunityPool(
        self, request: distribution_query_pb.QueryCommunityPoolRequest, context=None, metadata=None
    ):
        return self.community_pool_responses.pop()
