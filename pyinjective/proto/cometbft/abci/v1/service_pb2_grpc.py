# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from pyinjective.proto.cometbft.abci.v1 import types_pb2 as cometbft_dot_abci_dot_v1_dot_types__pb2


class ABCIServiceStub(object):
    """ABCIService is a service for an ABCI application.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Echo = channel.unary_unary(
                '/cometbft.abci.v1.ABCIService/Echo',
                request_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.EchoRequest.SerializeToString,
                response_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.EchoResponse.FromString,
                _registered_method=True)
        self.Flush = channel.unary_unary(
                '/cometbft.abci.v1.ABCIService/Flush',
                request_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.FlushRequest.SerializeToString,
                response_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.FlushResponse.FromString,
                _registered_method=True)
        self.Info = channel.unary_unary(
                '/cometbft.abci.v1.ABCIService/Info',
                request_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.InfoRequest.SerializeToString,
                response_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.InfoResponse.FromString,
                _registered_method=True)
        self.CheckTx = channel.unary_unary(
                '/cometbft.abci.v1.ABCIService/CheckTx',
                request_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.CheckTxRequest.SerializeToString,
                response_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.CheckTxResponse.FromString,
                _registered_method=True)
        self.Query = channel.unary_unary(
                '/cometbft.abci.v1.ABCIService/Query',
                request_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.QueryRequest.SerializeToString,
                response_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.QueryResponse.FromString,
                _registered_method=True)
        self.Commit = channel.unary_unary(
                '/cometbft.abci.v1.ABCIService/Commit',
                request_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.CommitRequest.SerializeToString,
                response_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.CommitResponse.FromString,
                _registered_method=True)
        self.InitChain = channel.unary_unary(
                '/cometbft.abci.v1.ABCIService/InitChain',
                request_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.InitChainRequest.SerializeToString,
                response_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.InitChainResponse.FromString,
                _registered_method=True)
        self.ListSnapshots = channel.unary_unary(
                '/cometbft.abci.v1.ABCIService/ListSnapshots',
                request_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.ListSnapshotsRequest.SerializeToString,
                response_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.ListSnapshotsResponse.FromString,
                _registered_method=True)
        self.OfferSnapshot = channel.unary_unary(
                '/cometbft.abci.v1.ABCIService/OfferSnapshot',
                request_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.OfferSnapshotRequest.SerializeToString,
                response_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.OfferSnapshotResponse.FromString,
                _registered_method=True)
        self.LoadSnapshotChunk = channel.unary_unary(
                '/cometbft.abci.v1.ABCIService/LoadSnapshotChunk',
                request_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.LoadSnapshotChunkRequest.SerializeToString,
                response_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.LoadSnapshotChunkResponse.FromString,
                _registered_method=True)
        self.ApplySnapshotChunk = channel.unary_unary(
                '/cometbft.abci.v1.ABCIService/ApplySnapshotChunk',
                request_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.ApplySnapshotChunkRequest.SerializeToString,
                response_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.ApplySnapshotChunkResponse.FromString,
                _registered_method=True)
        self.PrepareProposal = channel.unary_unary(
                '/cometbft.abci.v1.ABCIService/PrepareProposal',
                request_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.PrepareProposalRequest.SerializeToString,
                response_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.PrepareProposalResponse.FromString,
                _registered_method=True)
        self.ProcessProposal = channel.unary_unary(
                '/cometbft.abci.v1.ABCIService/ProcessProposal',
                request_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.ProcessProposalRequest.SerializeToString,
                response_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.ProcessProposalResponse.FromString,
                _registered_method=True)
        self.ExtendVote = channel.unary_unary(
                '/cometbft.abci.v1.ABCIService/ExtendVote',
                request_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.ExtendVoteRequest.SerializeToString,
                response_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.ExtendVoteResponse.FromString,
                _registered_method=True)
        self.VerifyVoteExtension = channel.unary_unary(
                '/cometbft.abci.v1.ABCIService/VerifyVoteExtension',
                request_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.VerifyVoteExtensionRequest.SerializeToString,
                response_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.VerifyVoteExtensionResponse.FromString,
                _registered_method=True)
        self.FinalizeBlock = channel.unary_unary(
                '/cometbft.abci.v1.ABCIService/FinalizeBlock',
                request_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.FinalizeBlockRequest.SerializeToString,
                response_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.FinalizeBlockResponse.FromString,
                _registered_method=True)


class ABCIServiceServicer(object):
    """ABCIService is a service for an ABCI application.
    """

    def Echo(self, request, context):
        """Echo returns back the same message it is sent.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Flush(self, request, context):
        """Flush flushes the write buffer.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Info(self, request, context):
        """Info returns information about the application state.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckTx(self, request, context):
        """CheckTx validates a transaction.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Query(self, request, context):
        """Query queries the application state.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Commit(self, request, context):
        """Commit commits a block of transactions.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitChain(self, request, context):
        """InitChain initializes the blockchain.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSnapshots(self, request, context):
        """ListSnapshots lists all the available snapshots.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OfferSnapshot(self, request, context):
        """OfferSnapshot sends a snapshot offer.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadSnapshotChunk(self, request, context):
        """LoadSnapshotChunk returns a chunk of snapshot.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ApplySnapshotChunk(self, request, context):
        """ApplySnapshotChunk applies a chunk of snapshot.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PrepareProposal(self, request, context):
        """PrepareProposal returns a proposal for the next block.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProcessProposal(self, request, context):
        """ProcessProposal validates a proposal.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExtendVote(self, request, context):
        """ExtendVote extends a vote with application-injected data (vote extensions).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VerifyVoteExtension(self, request, context):
        """VerifyVoteExtension verifies a vote extension.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FinalizeBlock(self, request, context):
        """FinalizeBlock finalizes a block.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ABCIServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Echo': grpc.unary_unary_rpc_method_handler(
                    servicer.Echo,
                    request_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.EchoRequest.FromString,
                    response_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.EchoResponse.SerializeToString,
            ),
            'Flush': grpc.unary_unary_rpc_method_handler(
                    servicer.Flush,
                    request_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.FlushRequest.FromString,
                    response_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.FlushResponse.SerializeToString,
            ),
            'Info': grpc.unary_unary_rpc_method_handler(
                    servicer.Info,
                    request_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.InfoRequest.FromString,
                    response_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.InfoResponse.SerializeToString,
            ),
            'CheckTx': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckTx,
                    request_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.CheckTxRequest.FromString,
                    response_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.CheckTxResponse.SerializeToString,
            ),
            'Query': grpc.unary_unary_rpc_method_handler(
                    servicer.Query,
                    request_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.QueryRequest.FromString,
                    response_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.QueryResponse.SerializeToString,
            ),
            'Commit': grpc.unary_unary_rpc_method_handler(
                    servicer.Commit,
                    request_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.CommitRequest.FromString,
                    response_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.CommitResponse.SerializeToString,
            ),
            'InitChain': grpc.unary_unary_rpc_method_handler(
                    servicer.InitChain,
                    request_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.InitChainRequest.FromString,
                    response_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.InitChainResponse.SerializeToString,
            ),
            'ListSnapshots': grpc.unary_unary_rpc_method_handler(
                    servicer.ListSnapshots,
                    request_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.ListSnapshotsRequest.FromString,
                    response_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.ListSnapshotsResponse.SerializeToString,
            ),
            'OfferSnapshot': grpc.unary_unary_rpc_method_handler(
                    servicer.OfferSnapshot,
                    request_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.OfferSnapshotRequest.FromString,
                    response_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.OfferSnapshotResponse.SerializeToString,
            ),
            'LoadSnapshotChunk': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadSnapshotChunk,
                    request_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.LoadSnapshotChunkRequest.FromString,
                    response_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.LoadSnapshotChunkResponse.SerializeToString,
            ),
            'ApplySnapshotChunk': grpc.unary_unary_rpc_method_handler(
                    servicer.ApplySnapshotChunk,
                    request_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.ApplySnapshotChunkRequest.FromString,
                    response_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.ApplySnapshotChunkResponse.SerializeToString,
            ),
            'PrepareProposal': grpc.unary_unary_rpc_method_handler(
                    servicer.PrepareProposal,
                    request_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.PrepareProposalRequest.FromString,
                    response_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.PrepareProposalResponse.SerializeToString,
            ),
            'ProcessProposal': grpc.unary_unary_rpc_method_handler(
                    servicer.ProcessProposal,
                    request_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.ProcessProposalRequest.FromString,
                    response_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.ProcessProposalResponse.SerializeToString,
            ),
            'ExtendVote': grpc.unary_unary_rpc_method_handler(
                    servicer.ExtendVote,
                    request_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.ExtendVoteRequest.FromString,
                    response_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.ExtendVoteResponse.SerializeToString,
            ),
            'VerifyVoteExtension': grpc.unary_unary_rpc_method_handler(
                    servicer.VerifyVoteExtension,
                    request_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.VerifyVoteExtensionRequest.FromString,
                    response_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.VerifyVoteExtensionResponse.SerializeToString,
            ),
            'FinalizeBlock': grpc.unary_unary_rpc_method_handler(
                    servicer.FinalizeBlock,
                    request_deserializer=cometbft_dot_abci_dot_v1_dot_types__pb2.FinalizeBlockRequest.FromString,
                    response_serializer=cometbft_dot_abci_dot_v1_dot_types__pb2.FinalizeBlockResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cometbft.abci.v1.ABCIService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cometbft.abci.v1.ABCIService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ABCIService(object):
    """ABCIService is a service for an ABCI application.
    """

    @staticmethod
    def Echo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cometbft.abci.v1.ABCIService/Echo',
            cometbft_dot_abci_dot_v1_dot_types__pb2.EchoRequest.SerializeToString,
            cometbft_dot_abci_dot_v1_dot_types__pb2.EchoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Flush(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cometbft.abci.v1.ABCIService/Flush',
            cometbft_dot_abci_dot_v1_dot_types__pb2.FlushRequest.SerializeToString,
            cometbft_dot_abci_dot_v1_dot_types__pb2.FlushResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Info(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cometbft.abci.v1.ABCIService/Info',
            cometbft_dot_abci_dot_v1_dot_types__pb2.InfoRequest.SerializeToString,
            cometbft_dot_abci_dot_v1_dot_types__pb2.InfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CheckTx(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cometbft.abci.v1.ABCIService/CheckTx',
            cometbft_dot_abci_dot_v1_dot_types__pb2.CheckTxRequest.SerializeToString,
            cometbft_dot_abci_dot_v1_dot_types__pb2.CheckTxResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Query(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cometbft.abci.v1.ABCIService/Query',
            cometbft_dot_abci_dot_v1_dot_types__pb2.QueryRequest.SerializeToString,
            cometbft_dot_abci_dot_v1_dot_types__pb2.QueryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Commit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cometbft.abci.v1.ABCIService/Commit',
            cometbft_dot_abci_dot_v1_dot_types__pb2.CommitRequest.SerializeToString,
            cometbft_dot_abci_dot_v1_dot_types__pb2.CommitResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def InitChain(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cometbft.abci.v1.ABCIService/InitChain',
            cometbft_dot_abci_dot_v1_dot_types__pb2.InitChainRequest.SerializeToString,
            cometbft_dot_abci_dot_v1_dot_types__pb2.InitChainResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListSnapshots(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cometbft.abci.v1.ABCIService/ListSnapshots',
            cometbft_dot_abci_dot_v1_dot_types__pb2.ListSnapshotsRequest.SerializeToString,
            cometbft_dot_abci_dot_v1_dot_types__pb2.ListSnapshotsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def OfferSnapshot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cometbft.abci.v1.ABCIService/OfferSnapshot',
            cometbft_dot_abci_dot_v1_dot_types__pb2.OfferSnapshotRequest.SerializeToString,
            cometbft_dot_abci_dot_v1_dot_types__pb2.OfferSnapshotResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def LoadSnapshotChunk(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cometbft.abci.v1.ABCIService/LoadSnapshotChunk',
            cometbft_dot_abci_dot_v1_dot_types__pb2.LoadSnapshotChunkRequest.SerializeToString,
            cometbft_dot_abci_dot_v1_dot_types__pb2.LoadSnapshotChunkResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ApplySnapshotChunk(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cometbft.abci.v1.ABCIService/ApplySnapshotChunk',
            cometbft_dot_abci_dot_v1_dot_types__pb2.ApplySnapshotChunkRequest.SerializeToString,
            cometbft_dot_abci_dot_v1_dot_types__pb2.ApplySnapshotChunkResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PrepareProposal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cometbft.abci.v1.ABCIService/PrepareProposal',
            cometbft_dot_abci_dot_v1_dot_types__pb2.PrepareProposalRequest.SerializeToString,
            cometbft_dot_abci_dot_v1_dot_types__pb2.PrepareProposalResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ProcessProposal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cometbft.abci.v1.ABCIService/ProcessProposal',
            cometbft_dot_abci_dot_v1_dot_types__pb2.ProcessProposalRequest.SerializeToString,
            cometbft_dot_abci_dot_v1_dot_types__pb2.ProcessProposalResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ExtendVote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cometbft.abci.v1.ABCIService/ExtendVote',
            cometbft_dot_abci_dot_v1_dot_types__pb2.ExtendVoteRequest.SerializeToString,
            cometbft_dot_abci_dot_v1_dot_types__pb2.ExtendVoteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def VerifyVoteExtension(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cometbft.abci.v1.ABCIService/VerifyVoteExtension',
            cometbft_dot_abci_dot_v1_dot_types__pb2.VerifyVoteExtensionRequest.SerializeToString,
            cometbft_dot_abci_dot_v1_dot_types__pb2.VerifyVoteExtensionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def FinalizeBlock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cometbft.abci.v1.ABCIService/FinalizeBlock',
            cometbft_dot_abci_dot_v1_dot_types__pb2.FinalizeBlockRequest.SerializeToString,
            cometbft_dot_abci_dot_v1_dot_types__pb2.FinalizeBlockResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
