from collections import deque

from pyinjective.proto.injective.stream.v1beta1 import query_pb2 as chain_stream_pb, query_pb2_grpc as chain_stream_grpc
from pyinjective.proto.injective.stream.v2 import (
    query_pb2 as chain_stream_v2_pb,
    query_pb2_grpc as chain_stream_v2_grpc,
)


class ConfigurableChainStreamQueryServicer(chain_stream_grpc.StreamServicer):
    def __init__(self):
        super().__init__()
        self.stream_responses = deque()
        self.stream_v2_responses = deque()

    async def Stream(self, request: chain_stream_pb.StreamRequest, context=None, metadata=None):
        for event in self.stream_responses:
            yield event


class ConfigurableChainStreamV2QueryServicer(chain_stream_v2_grpc.StreamServicer):
    def __init__(self):
        super().__init__()
        self.stream_responses = deque()

    async def StreamV2(self, request: chain_stream_v2_pb.StreamRequest, context=None, metadata=None):
        for event in self.stream_responses:
            yield event
