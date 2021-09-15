import grpc
import time

from typing import List, Optional

from .exceptions import NotFoundError, EmptyMsgError
from pyinjective.wallet import PrivateKey, PublicKey, Address

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
    injective_derivative_exchange_rpc_pb2 as derivative_exchange_rpc_pb,
    injective_derivative_exchange_rpc_pb2_grpc as derivative_exchange_rpc_grpc,
    injective_spot_exchange_rpc_pb2 as spot_exchange_rpc_pb,
    injective_spot_exchange_rpc_pb2_grpc as spot_exchange_rpc_grpc,
    injective_accounts_rpc_pb2 as spot_accounts_rpc_pb,
    injective_accounts_rpc_pb2_grpc as accounts_rpc_grpc,
    injective_insurance_rpc_pb2 as insurance_rpc_pb,
    injective_insurance_rpc_pb2_grpc as insurance_rpc_grpc,
    injective_oracle_rpc_pb2 as oracle_rpc_pb,
    injective_oracle_rpc_pb2_grpc as oracle_rpc_grpc
)


async def create_client(
        private_key: str,
        chain_node_endpoint: str,
        exchange_endpoint: str,
        insecure: bool = False,
        credentials: grpc.ChannelCredentials = None,
):
    client = Client(private_key, chain_node_endpoint, exchange_endpoint, insecure, credentials)
    await client._init()
    return client


class Client(object):
    def __init__(
            self,
            private_key: str,
            chain_node_endpoint: str,
            exchange_endpoint: str,
            insecure: bool = False,
            credentials: grpc.ChannelCredentials = None,
    ):
        chain_channel = (
            grpc.insecure_channel(chain_node_endpoint)
            if insecure
            else grpc.secure_channel(
                chain_node_endpoint,
                credentials or grpc.ssl_channel_credentials(),
            )
        )

        exchange_channel = (
            grpc.insecure_channel(exchange_endpoint)
            if insecure
            else grpc.secure_channel(
                exchange_endpoint,
                credentials or grpc.ssl_channel_credentials(),
            )
        )

        self.derivativesClient = derivative_exchange_rpc_grpc.InjectiveDerivativeExchangeRPCStub(exchange_channel)
        self.spotClient = spot_exchange_rpc_grpc.InjectiveSpotExchangeRPCStub(exchange_channel)
        self.accountsClient = accounts_rpc_grpc.InjectiveAccountsRPCStub(exchange_channel)
        self.insuranceClient = insurance_rpc_grpc.InjectiveInsuranceRPCStub(exchange_channel)
        self.oracleClient = oracle_rpc_grpc.InjectiveOracleRPCStub(exchange_channel)

        self.stubCosmosTendermint = tendermint_query_grpc.ServiceStub(chain_channel)
        self.stubAuth = auth_query_grpc.QueryStub(chain_channel)
        self.stubTx = tx_service_grpc.ServiceStub(chain_channel)
        self.privateKey = PrivateKey.from_hex(private_key)
        self.publicKey = self.privateKey.to_public_key()
        self.address = self.publicKey.to_address()
        self.subaccountID = self.address.get_subaccount_id(index=0)

    async def _init(self):
        self.derivativeMarkets = await self.derivativesClient.Markets(derivative_exchange_rpc_pb.MarketsRequest())
        self.spotMarkets = await self.spotClient.Markets(spot_exchange_rpc_pb.MarketsRequest())
        self.denoms = None # TODO populate

    def create_spot_limit_order(self, price: float, quantity: float, isBuy: bool):
        # TODO abstract away everything related to decimal conversions and tick sizes and simply return the MsgCreateSpotLimitOrder
        pass



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
