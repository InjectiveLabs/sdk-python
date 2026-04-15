from collections import deque

from pyinjective.proto.exchange import (
    injective_meta_rpc_pb2 as exchange_meta_pb,
    injective_meta_rpc_pb2_grpc as exchange_meta_grpc,
)


class ConfigurableMetaQueryServicer(exchange_meta_grpc.InjectiveMetaRPCServicer):
    def __init__(self):
        super().__init__()
        self.ping_responses = deque()
        self.version_responses = deque()
        self.info_responses = deque()
        self.stream_keepalive_responses = deque()

    async def Ping(self, request: exchange_meta_pb.PingRequest, context=None, metadata=None):
        return self.ping_responses.pop()

    async def Version(self, request: exchange_meta_pb.VersionRequest, context=None, metadata=None):
        return self.version_responses.pop()

    async def Info(self, request: exchange_meta_pb.InfoRequest, context=None, metadata=None):
        return self.info_responses.pop()

    async def StreamKeepalive(self, request: exchange_meta_pb.StreamKeepaliveRequest, context=None, metadata=None):
        for event in self.stream_keepalive_responses:
            yield event
