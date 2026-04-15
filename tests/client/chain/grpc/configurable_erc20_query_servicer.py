from collections import deque

from pyinjective.proto.injective.erc20.v1beta1 import query_pb2 as erc20_query_pb, query_pb2_grpc as erc20_query_grpc


class ConfigurableERC20QueryServicer(erc20_query_grpc.QueryServicer):
    def __init__(self):
        super().__init__()
        self.erc20_params_responses = deque()
        self.all_token_pairs_responses = deque()
        self.token_pair_by_denom_responses = deque()
        self.token_pair_by_erc20_address_responses = deque()

    async def Params(self, request: erc20_query_pb.QueryParamsRequest, context=None, metadata=None):
        return self.erc20_params_responses.pop()

    async def AllTokenPairs(self, request: erc20_query_pb.QueryAllTokenPairsRequest, context=None, metadata=None):
        return self.all_token_pairs_responses.pop()

    async def TokenPairByDenom(self, request: erc20_query_pb.QueryTokenPairByDenomRequest, context=None, metadata=None):
        return self.token_pair_by_denom_responses.pop()

    async def TokenPairByERC20Address(
        self, request: erc20_query_pb.QueryTokenPairByERC20AddressRequest, context=None, metadata=None
    ):
        return self.token_pair_by_erc20_address_responses.pop()
