from collections import deque

from pyinjective.proto.cosmos.base.tendermint.v1beta1 import (
    query_pb2 as tendermint_query,
    query_pb2_grpc as tendermint_query_grpc,
)


class ConfigurableTendermintQueryServicer(tendermint_query_grpc.ServiceServicer):
    def __init__(self):
        super().__init__()
        self.get_node_info_responses = deque()
        self.get_syncing_responses = deque()
        self.get_latest_block_responses = deque()
        self.get_block_by_height_responses = deque()
        self.get_latest_validator_set_responses = deque()
        self.get_validator_set_by_height_responses = deque()
        self.abci_query_responses = deque()

    async def GetNodeInfo(self, request: tendermint_query.GetNodeInfoRequest, context=None, metadata=None):
        return self.get_node_info_responses.pop()

    async def GetSyncing(self, request: tendermint_query.GetSyncingRequest, context=None, metadata=None):
        return self.get_syncing_responses.pop()

    async def GetLatestBlock(self, request: tendermint_query.GetLatestBlockRequest, context=None, metadata=None):
        return self.get_latest_block_responses.pop()

    async def GetBlockByHeight(self, request: tendermint_query.GetBlockByHeightRequest, context=None, metadata=None):
        return self.get_block_by_height_responses.pop()

    async def GetLatestValidatorSet(
        self, request: tendermint_query.GetLatestValidatorSetRequest, context=None, metadata=None
    ):
        return self.get_latest_validator_set_responses.pop()

    async def GetValidatorSetByHeight(
        self, request: tendermint_query.GetValidatorSetByHeightRequest, context=None, metadata=None
    ):
        return self.get_validator_set_by_height_responses.pop()

    async def ABCIQuery(self, request: tendermint_query.ABCIQueryRequest, context=None, metadata=None):
        return self.abci_query_responses.pop()
