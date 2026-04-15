from collections import deque

from pyinjective.proto.injective.tokenfactory.v1beta1 import (
    query_pb2 as token_factory_query_pb,
    query_pb2_grpc as token_factory_query_grpc,
)


class ConfigurableTokenFactoryQueryServicer(token_factory_query_grpc.QueryServicer):
    def __init__(self):
        super().__init__()
        self.params_responses = deque()
        self.denom_authority_metadata_responses = deque()
        self.denoms_from_creator_responses = deque()
        self.tokenfactory_module_state_responses = deque()

    async def Params(self, request: token_factory_query_pb.QueryParamsRequest, context=None, metadata=None):
        return self.params_responses.pop()

    async def DenomAuthorityMetadata(
        self, request: token_factory_query_pb.QueryDenomAuthorityMetadataRequest, context=None, metadata=None
    ):
        return self.denom_authority_metadata_responses.pop()

    async def DenomsFromCreator(
        self, request: token_factory_query_pb.QueryDenomsFromCreatorRequest, context=None, metadata=None
    ):
        return self.denoms_from_creator_responses.pop()

    async def TokenfactoryModuleState(
        self, request: token_factory_query_pb.QueryModuleStateRequest, context=None, metadata=None
    ):
        return self.tokenfactory_module_state_responses.pop()
