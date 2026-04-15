from collections import deque

from pyinjective.proto.cosmos.tx.v1beta1 import service_pb2 as tx_service, service_pb2_grpc as tx_service_grpc


class ConfigurableTxQueryServicer(tx_service_grpc.ServiceServicer):
    def __init__(self):
        super().__init__()
        self.simulate_responses = deque()
        self.get_tx_responses = deque()
        self.broadcast_responses = deque()

    async def Simulate(self, request: tx_service.SimulateRequest, context=None, metadata=None):
        return self.simulate_responses.pop()

    async def GetTx(self, request: tx_service.GetTxRequest, context=None, metadata=None):
        return self.get_tx_responses.pop()

    async def BroadcastTx(self, request: tx_service.BroadcastTxRequest, context=None, metadata=None):
        return self.broadcast_responses.pop()
