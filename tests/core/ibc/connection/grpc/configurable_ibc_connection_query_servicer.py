from collections import deque

from pyinjective.proto.ibc.core.connection.v1 import (
    query_pb2 as ibc_connection_query,
    query_pb2_grpc as ibc_connection_query_grpc,
)


class ConfigurableIBCConnectionQueryServicer(ibc_connection_query_grpc.QueryServicer):
    def __init__(self):
        super().__init__()
        self.connection_responses = deque()
        self.connections_responses = deque()
        self.client_connections_responses = deque()
        self.connection_client_state_responses = deque()
        self.connection_consensus_state_responses = deque()
        self.connection_params_responses = deque()

    async def Connection(self, request: ibc_connection_query.QueryConnectionRequest, context=None, metadata=None):
        return self.connection_responses.pop()

    async def Connections(self, request: ibc_connection_query.QueryConnectionsRequest, context=None, metadata=None):
        return self.connections_responses.pop()

    async def ClientConnections(
        self, request: ibc_connection_query.QueryClientConnectionsRequest, context=None, metadata=None
    ):
        return self.client_connections_responses.pop()

    async def ConnectionClientState(
        self, request: ibc_connection_query.QueryConnectionClientStateRequest, context=None, metadata=None
    ):
        return self.connection_client_state_responses.pop()

    async def ConnectionConsensusState(
        self, request: ibc_connection_query.QueryConnectionConsensusStateRequest, context=None, metadata=None
    ):
        return self.connection_consensus_state_responses.pop()

    async def ConnectionParams(
        self, request: ibc_connection_query.QueryConnectionParamsRequest, context=None, metadata=None
    ):
        return self.connection_params_responses.pop()
