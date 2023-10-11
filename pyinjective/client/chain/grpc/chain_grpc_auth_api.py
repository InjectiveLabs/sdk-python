from typing import List, Tuple

from grpc.aio import Channel

from pyinjective.client.chain.model.account import Account
from pyinjective.client.chain.model.auth_params import AuthParams
from pyinjective.client.model.pagination import Pagination, PaginationOption
from pyinjective.proto.cosmos.auth.v1beta1 import query_pb2 as auth_query_pb, query_pb2_grpc as auth_query_grpc


class ChainGrpcAuthApi:
    def __init__(self, channel: Channel):
        self._stub = auth_query_grpc.QueryStub(channel)

    async def fetch_module_params(self) -> AuthParams:
        request = auth_query_pb.QueryParamsRequest()
        response = await self._stub.Params(request)

        module_params = AuthParams.from_proto_response(response=response)

        return module_params

    async def fetch_account(self, address: str) -> Account:
        request = auth_query_pb.QueryAccountRequest(address=address)
        response = await self._stub.Account(request)

        account = Account.from_proto(proto_account=response.account)

        return account

    async def fetch_accounts(self, pagination_option: PaginationOption) -> Tuple[List[Account], PaginationOption]:
        request = auth_query_pb.QueryAccountsRequest(pagination=pagination_option.create_pagination_request())
        response = await self._stub.Accounts(request)

        accounts = [Account.from_proto(proto_account=proto_account) for proto_account in response.accounts]
        response_pagination = Pagination.from_proto(proto_pagination=response.pagination)

        return accounts, response_pagination
