import grpc
import time

from typing import List, Optional

from .exceptions import NotFoundError, EmptyMsgError

from .proto.cosmos.base.abci.v1beta1 import abci_pb2 as abci_type
from .proto.cosmos.base.tendermint.v1beta1 import (
    query_pb2_grpc as tendermint_query_grpc,
    query_pb2 as tendermint_query,
)
from .proto.cosmos.auth.v1beta1 import (
    query_pb2_grpc as auth_query_grpc,
    query_pb2 as auth_query,
    auth_pb2 as auth_type,
)
from .proto.cosmos.tx.v1beta1 import (
    service_pb2_grpc as tx_service_grpc,
    service_pb2 as tx_service,
)
from .proto.exchange import (
    injective_accounts_rpc_pb2 as exchange_accounts_rpc_pb,
    injective_accounts_rpc_pb2_grpc as exchange_accounts_rpc_grpc
)

from .constant import Network

class Client:
    def __init__(
        self,
        network: Network,
        insecure: bool = False,
        credentials: grpc.ChannelCredentials = None,
    ):
        # chain stubs
        chain_channel = (
            grpc.insecure_channel(network.grpc_endpoint)
            if insecure
            else grpc.secure_channel(
                grpc_endpoint,
                credentials or grpc.ssl_channel_credentials(),
            )
        )
        self.stubCosmosTendermint = tendermint_query_grpc.ServiceStub(chain_channel)
        self.stubAuth = auth_query_grpc.QueryStub(chain_channel)
        self.stubTx = tx_service_grpc.ServiceStub(chain_channel)

        # exchange stubs
        exchange_channel = (
            grpc.insecure_channel(network.grpc_exchange_endpoint)
            if insecure
            else grpc.secure_channel(
                grpc_endpoint,
                credentials or grpc.ssl_channel_credentials(),
            )
        )
        self.stubExchangeAccount = exchange_accounts_rpc_grpc.InjectiveAccountsRPCStub(exchange_channel)

    # default client methods
    def get_latest_block(self) -> tendermint_query.GetLatestBlockResponse:
        return self.stubCosmosTendermint.GetLatestBlock(tendermint_query.GetLatestBlockRequest())

    def get_account(self, address: str) -> Optional[auth_type.BaseAccount]:
        try:
            account_any = self.stubAuth.Account(auth_query.QueryAccountRequest(address=address)).account
            account = auth_type.BaseAccount()
            if account_any.Is(account.DESCRIPTOR):
                account_any.Unpack(account)
                return account
        except:
            return None

    def get_request_id_by_tx_hash(self, tx_hash: bytes) -> List[int]:
        tx = self.stubTx.GetTx(tx_service.GetTxRequest(hash=tx_hash))
        request_ids = []
        for tx in tx.tx_response.logs:
            request_event = [event for event in tx.events if event.type == "request" or event.type == "report"]
            if len(request_event) == 1:
                attrs = request_event[0].attributes
                attr_id = [attr for attr in attrs if attr.key == "id"]
                if len(attr_id) == 1:
                    request_id = attr_id[0].value
                    request_ids.append(int(request_id))
        if len(request_ids) == 0:
            raise NotFoundError("Request Id is not found")
        return request_ids

    def simulate_tx(self, tx_byte: bytes) -> abci_type.SimulationResponse:
        try:
            return (self.stubTx.Simulate(
                tx_service.SimulateRequest(tx_bytes=tx_byte)
            ).result, True)
        except grpc.RpcError as err:
            return (err, False)

    def send_tx_sync_mode(self, tx_byte: bytes) -> abci_type.TxResponse:
        return self.stubTx.BroadcastTx(
            tx_service.BroadcastTxRequest(tx_bytes=tx_byte, mode=tx_service.BroadcastMode.BROADCAST_MODE_SYNC)
        ).tx_response

    def send_tx_async_mode(self, tx_byte: bytes) -> abci_type.TxResponse:
        return self.stubTx.BroadcastTx(
            tx_service.BroadcastTxRequest(tx_bytes=tx_byte, mode=tx_service.BroadcastMode.BROADCAST_MODE_ASYNC)
        ).tx_response

    def send_tx_block_mode(self, tx_byte: bytes) -> abci_type.TxResponse:
        return self.stubTx.BroadcastTx(
            tx_service.BroadcastTxRequest(tx_bytes=tx_byte, mode=tx_service.BroadcastMode.BROADCAST_MODE_BLOCK)
        ).tx_response

    def get_chain_id(self) -> str:
        latest_block = self.get_latest_block()
        return latest_block.block.header.chain_id

    # injective exchange client methods
    def stream_exchange_subaccount_balance(self, subaccount_id):
        req = exchange_accounts_rpc_pb.StreamSubaccountBalanceRequest(subaccount_id=subaccount_id)
        return self.stubExchangeAccount.StreamSubaccountBalance(req)

    def get_exchange_subaccount_balance(self, subaccount_id, denom):
        req = exchange_accounts_rpc_pb.SubaccountBalanceRequest(subaccount_id=subaccount_id, denom=denom)
        return self.stubExchangeAccount.SubaccountBalanceEndpoint(req)
