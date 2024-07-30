from typing import Any, Callable, Dict

from grpc.aio import Channel

from pyinjective.core.network import CookieAssistant
from pyinjective.proto.injective.permissions.v1beta1 import (
    query_pb2 as permissions_query_pb,
    query_pb2_grpc as permissions_query_grpc,
)
from pyinjective.utils.grpc_api_request_assistant import GrpcApiRequestAssistant


class ChainGrpcPermissionsApi:
    def __init__(self, channel: Channel, cookie_assistant: CookieAssistant):
        self._stub = permissions_query_grpc.QueryStub(channel)
        self._assistant = GrpcApiRequestAssistant(cookie_assistant=cookie_assistant)

    async def fetch_module_params(self) -> Dict[str, Any]:
        request = permissions_query_pb.QueryParamsRequest()
        response = await self._execute_call(call=self._stub.Params, request=request)

        return response

    async def fetch_all_namespaces(self) -> Dict[str, Any]:
        request = permissions_query_pb.QueryAllNamespacesRequest()
        response = await self._execute_call(call=self._stub.AllNamespaces, request=request)

        return response

    async def fetch_namespace_by_denom(self, denom: str, include_roles: bool) -> Dict[str, Any]:
        request = permissions_query_pb.QueryNamespaceByDenomRequest(denom=denom, include_roles=include_roles)
        response = await self._execute_call(call=self._stub.NamespaceByDenom, request=request)

        return response

    async def fetch_address_roles(self, denom: str, address: str) -> Dict[str, Any]:
        request = permissions_query_pb.QueryAddressRolesRequest(denom=denom, address=address)
        response = await self._execute_call(call=self._stub.AddressRoles, request=request)

        return response

    async def fetch_addresses_by_role(self, denom: str, role: str) -> Dict[str, Any]:
        request = permissions_query_pb.QueryAddressesByRoleRequest(denom=denom, role=role)
        response = await self._execute_call(call=self._stub.AddressesByRole, request=request)

        return response

    async def fetch_vouchers_for_address(self, address: str) -> Dict[str, Any]:
        request = permissions_query_pb.QueryVouchersForAddressRequest(address=address)
        response = await self._execute_call(call=self._stub.VouchersForAddress, request=request)

        return response

    async def _execute_call(self, call: Callable, request) -> Dict[str, Any]:
        return await self._assistant.execute_call(call=call, request=request)
