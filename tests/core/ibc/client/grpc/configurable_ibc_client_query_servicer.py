from collections import deque

from pyinjective.proto.ibc.core.client.v1 import query_pb2 as ibc_client_query, query_pb2_grpc as ibc_client_query_grpc


class ConfigurableIBCClientQueryServicer(ibc_client_query_grpc.QueryServicer):
    def __init__(self):
        super().__init__()
        self.client_state_responses = deque()
        self.client_states_responses = deque()
        self.consensus_state_responses = deque()
        self.consensus_states_responses = deque()
        self.consensus_state_heights_responses = deque()
        self.client_status_responses = deque()
        self.client_params_responses = deque()
        self.upgraded_client_state_responses = deque()
        self.upgraded_consensus_state_responses = deque()

    async def ClientState(self, request: ibc_client_query.QueryClientStateRequest, context=None, metadata=None):
        return self.client_state_responses.pop()

    async def ClientStates(self, request: ibc_client_query.QueryClientStatesRequest, context=None, metadata=None):
        return self.client_states_responses.pop()

    async def ConsensusState(self, request: ibc_client_query.QueryConsensusStateRequest, context=None, metadata=None):
        return self.consensus_state_responses.pop()

    async def ConsensusStates(self, request: ibc_client_query.QueryConsensusStatesRequest, context=None, metadata=None):
        return self.consensus_states_responses.pop()

    async def ConsensusStateHeights(
        self, request: ibc_client_query.QueryConsensusStateHeightsRequest, context=None, metadata=None
    ):
        return self.consensus_state_heights_responses.pop()

    async def ClientStatus(self, request: ibc_client_query.QueryClientStatusRequest, context=None, metadata=None):
        return self.client_status_responses.pop()

    async def ClientParams(self, request: ibc_client_query.QueryClientParamsRequest, context=None, metadata=None):
        return self.client_params_responses.pop()

    async def UpgradedClientState(
        self, request: ibc_client_query.QueryUpgradedClientStateRequest, context=None, metadata=None
    ):
        return self.upgraded_client_state_responses.pop()

    async def UpgradedConsensusState(
        self, request: ibc_client_query.QueryUpgradedConsensusStateRequest, context=None, metadata=None
    ):
        return self.upgraded_consensus_state_responses.pop()
