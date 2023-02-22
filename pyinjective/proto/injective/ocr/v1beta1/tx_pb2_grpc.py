# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from injective.ocr.v1beta1 import tx_pb2 as injective_dot_ocr_dot_v1beta1_dot_tx__pb2


class MsgStub(object):
    """Msg defines the OCR Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateFeed = channel.unary_unary(
                '/injective.ocr.v1beta1.Msg/CreateFeed',
                request_serializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgCreateFeed.SerializeToString,
                response_deserializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgCreateFeedResponse.FromString,
                )
        self.UpdateFeed = channel.unary_unary(
                '/injective.ocr.v1beta1.Msg/UpdateFeed',
                request_serializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgUpdateFeed.SerializeToString,
                response_deserializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgUpdateFeedResponse.FromString,
                )
        self.Transmit = channel.unary_unary(
                '/injective.ocr.v1beta1.Msg/Transmit',
                request_serializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgTransmit.SerializeToString,
                response_deserializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgTransmitResponse.FromString,
                )
        self.FundFeedRewardPool = channel.unary_unary(
                '/injective.ocr.v1beta1.Msg/FundFeedRewardPool',
                request_serializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgFundFeedRewardPool.SerializeToString,
                response_deserializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgFundFeedRewardPoolResponse.FromString,
                )
        self.WithdrawFeedRewardPool = channel.unary_unary(
                '/injective.ocr.v1beta1.Msg/WithdrawFeedRewardPool',
                request_serializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgWithdrawFeedRewardPool.SerializeToString,
                response_deserializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgWithdrawFeedRewardPoolResponse.FromString,
                )
        self.SetPayees = channel.unary_unary(
                '/injective.ocr.v1beta1.Msg/SetPayees',
                request_serializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgSetPayees.SerializeToString,
                response_deserializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgSetPayeesResponse.FromString,
                )
        self.TransferPayeeship = channel.unary_unary(
                '/injective.ocr.v1beta1.Msg/TransferPayeeship',
                request_serializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgTransferPayeeship.SerializeToString,
                response_deserializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgTransferPayeeshipResponse.FromString,
                )
        self.AcceptPayeeship = channel.unary_unary(
                '/injective.ocr.v1beta1.Msg/AcceptPayeeship',
                request_serializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgAcceptPayeeship.SerializeToString,
                response_deserializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgAcceptPayeeshipResponse.FromString,
                )


class MsgServicer(object):
    """Msg defines the OCR Msg service.
    """

    def CreateFeed(self, request, context):
        """CreateFeed defines a method for creating feed by module admin
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateFeed(self, request, context):
        """CreateFeed defines a method for creating feed by feed admin or feed billing admin
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Transmit(self, request, context):
        """Transmit defines a method for transmitting the feed info by transmitter
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FundFeedRewardPool(self, request, context):
        """FundFeedRewardPool defines a method to put funds into feed reward pool
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WithdrawFeedRewardPool(self, request, context):
        """WithdrawFeedRewardPool defines a method to witdhraw feed reward by feed admin or billing admin
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetPayees(self, request, context):
        """SetPayees defines a method to set payees for transmitters (batch action)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TransferPayeeship(self, request, context):
        """TransferPayeeship defines a method for a payee to transfer reward receive ownership
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AcceptPayeeship(self, request, context):
        """AcceptPayeeship defines a method for a new payee to accept reward receive ownership
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateFeed': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFeed,
                    request_deserializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgCreateFeed.FromString,
                    response_serializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgCreateFeedResponse.SerializeToString,
            ),
            'UpdateFeed': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateFeed,
                    request_deserializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgUpdateFeed.FromString,
                    response_serializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgUpdateFeedResponse.SerializeToString,
            ),
            'Transmit': grpc.unary_unary_rpc_method_handler(
                    servicer.Transmit,
                    request_deserializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgTransmit.FromString,
                    response_serializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgTransmitResponse.SerializeToString,
            ),
            'FundFeedRewardPool': grpc.unary_unary_rpc_method_handler(
                    servicer.FundFeedRewardPool,
                    request_deserializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgFundFeedRewardPool.FromString,
                    response_serializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgFundFeedRewardPoolResponse.SerializeToString,
            ),
            'WithdrawFeedRewardPool': grpc.unary_unary_rpc_method_handler(
                    servicer.WithdrawFeedRewardPool,
                    request_deserializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgWithdrawFeedRewardPool.FromString,
                    response_serializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgWithdrawFeedRewardPoolResponse.SerializeToString,
            ),
            'SetPayees': grpc.unary_unary_rpc_method_handler(
                    servicer.SetPayees,
                    request_deserializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgSetPayees.FromString,
                    response_serializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgSetPayeesResponse.SerializeToString,
            ),
            'TransferPayeeship': grpc.unary_unary_rpc_method_handler(
                    servicer.TransferPayeeship,
                    request_deserializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgTransferPayeeship.FromString,
                    response_serializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgTransferPayeeshipResponse.SerializeToString,
            ),
            'AcceptPayeeship': grpc.unary_unary_rpc_method_handler(
                    servicer.AcceptPayeeship,
                    request_deserializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgAcceptPayeeship.FromString,
                    response_serializer=injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgAcceptPayeeshipResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective.ocr.v1beta1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the OCR Msg service.
    """

    @staticmethod
    def CreateFeed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.ocr.v1beta1.Msg/CreateFeed',
            injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgCreateFeed.SerializeToString,
            injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgCreateFeedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateFeed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.ocr.v1beta1.Msg/UpdateFeed',
            injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgUpdateFeed.SerializeToString,
            injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgUpdateFeedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Transmit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.ocr.v1beta1.Msg/Transmit',
            injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgTransmit.SerializeToString,
            injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgTransmitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FundFeedRewardPool(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.ocr.v1beta1.Msg/FundFeedRewardPool',
            injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgFundFeedRewardPool.SerializeToString,
            injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgFundFeedRewardPoolResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WithdrawFeedRewardPool(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.ocr.v1beta1.Msg/WithdrawFeedRewardPool',
            injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgWithdrawFeedRewardPool.SerializeToString,
            injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgWithdrawFeedRewardPoolResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetPayees(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.ocr.v1beta1.Msg/SetPayees',
            injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgSetPayees.SerializeToString,
            injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgSetPayeesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TransferPayeeship(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.ocr.v1beta1.Msg/TransferPayeeship',
            injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgTransferPayeeship.SerializeToString,
            injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgTransferPayeeshipResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AcceptPayeeship(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.ocr.v1beta1.Msg/AcceptPayeeship',
            injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgAcceptPayeeship.SerializeToString,
            injective_dot_ocr_dot_v1beta1_dot_tx__pb2.MsgAcceptPayeeshipResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)