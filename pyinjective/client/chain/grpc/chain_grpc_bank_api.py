from typing import Dict, Any

from grpc.aio import Channel

from pyinjective.proto.cosmos.bank.v1beta1 import (
    query_pb2_grpc as bank_query_grpc,
    query_pb2 as bank_query_pb,
)

class ChainGrpcBankApi:

    def __init__(self, channel: Channel):
        self._stub = bank_query_grpc.QueryStub(channel)

    async def fetch_module_params(self) -> Dict[str, Any]:
        request = bank_query_pb.QueryParamsRequest()
        response = await self._stub.Params(request)

        module_params = {
            "default_send_enabled": response.params.default_send_enabled,
        }

        return module_params

    async def fetch_balance(self, account_address: str, denom: str) -> Dict[str, Any]:
        request = bank_query_pb.QueryBalanceRequest(address=account_address, denom=denom)
        response = await self._stub.Balance(request)

        bank_balance = {
            "amount": response.balance.amount,
            "denom": response.balance.denom,
        }

        return bank_balance

    async def fetch_balances(self, account_address: str) -> Dict[str, Any]:
        request = bank_query_pb.QueryAllBalancesRequest(address=account_address)
        response = await self._stub.AllBalances(request)

        bank_balances = {
            "balances": [{"amount": coin.amount, "denom": coin.denom} for coin in response.balances],
            "pagination": {"total": response.pagination.total}}

        return bank_balances

    async def fetch_total_supply(self) -> Dict[str, Any]:
        request = bank_query_pb.QueryTotalSupplyRequest()
        response = await self._stub.TotalSupply(request)

        total_supply = {
            "supply": [{"amount": coin.amount, "denom": coin.denom} for coin in response.supply],
            "pagination": {
                "next": response.pagination.next_key,
                "total": response.pagination.total
            }
        }

        return total_supply
