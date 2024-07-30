import grpc
import pytest

from pyinjective.client.chain.grpc.chain_grpc_permissions_api import ChainGrpcPermissionsApi
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as coin_pb
from pyinjective.proto.injective.permissions.v1beta1 import (
    params_pb2 as permissions_params_pb,
    permissions_pb2 as permissions_pb,
    query_pb2 as permissions_query_pb,
)
from tests.client.chain.grpc.configurable_permissions_query_servicer import ConfigurablePermissionsQueryServicer


@pytest.fixture
def permissions_servicer():
    return ConfigurablePermissionsQueryServicer()


class TestChainGrpcPermissionsApi:
    @pytest.mark.asyncio
    async def test_fetch_module_params(
        self,
        permissions_servicer,
    ):
        params = permissions_params_pb.Params(
            wasm_hook_query_max_gas=1000000,
        )
        permissions_servicer.permissions_params.append(permissions_query_pb.QueryParamsResponse(params=params))

        api = self._api_instance(servicer=permissions_servicer)

        module_params = await api.fetch_module_params()
        expected_params = {
            "params": {
                "wasmHookQueryMaxGas": str(params.wasm_hook_query_max_gas),
            }
        }

        assert module_params == expected_params

    @pytest.mark.asyncio
    async def test_fetch_all_namespaces(
        self,
        permissions_servicer,
    ):
        role_permission = permissions_pb.Role(
            role="role",
            permissions=3,
        )
        address_roles = permissions_pb.AddressRoles(
            address="inj1knhahceyp57j5x7xh69p7utegnnnfgxavmahjr",
            roles=["role"],
        )
        namespace = permissions_pb.Namespace(
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            wasm_hook="wasm_hook",
            mints_paused=True,
            sends_paused=False,
            burns_paused=False,
            role_permissions=[role_permission],
            address_roles=[address_roles],
        )
        permissions_servicer.all_namespaces_responses.append(
            permissions_query_pb.QueryAllNamespacesResponse(namespaces=[namespace])
        )

        api = self._api_instance(servicer=permissions_servicer)

        all_namespaces = await api.fetch_all_namespaces()
        expected_namespaces = {
            "namespaces": [
                {
                    "denom": namespace.denom,
                    "wasmHook": namespace.wasm_hook,
                    "mintsPaused": namespace.mints_paused,
                    "sendsPaused": namespace.sends_paused,
                    "burnsPaused": namespace.burns_paused,
                    "rolePermissions": [
                        {
                            "role": role_permission.role,
                            "permissions": role_permission.permissions,
                        }
                    ],
                    "addressRoles": [
                        {
                            "address": address_roles.address,
                            "roles": address_roles.roles,
                        }
                    ],
                }
            ]
        }

        assert all_namespaces == expected_namespaces

    @pytest.mark.asyncio
    async def test_fetch_namespace_by_denom(
        self,
        permissions_servicer,
    ):
        role_permission = permissions_pb.Role(
            role="role",
            permissions=3,
        )
        address_roles = permissions_pb.AddressRoles(
            address="inj1knhahceyp57j5x7xh69p7utegnnnfgxavmahjr",
            roles=["role"],
        )
        namespace = permissions_pb.Namespace(
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            wasm_hook="wasm_hook",
            mints_paused=True,
            sends_paused=False,
            burns_paused=False,
            role_permissions=[role_permission],
            address_roles=[address_roles],
        )
        permissions_servicer.namespace_by_denom_responses.append(
            permissions_query_pb.QueryNamespaceByDenomResponse(namespace=namespace)
        )

        api = self._api_instance(servicer=permissions_servicer)

        namespace_result = await api.fetch_namespace_by_denom(denom=namespace.denom, include_roles=True)
        expected_namespace = {
            "namespace": {
                "denom": namespace.denom,
                "wasmHook": namespace.wasm_hook,
                "mintsPaused": namespace.mints_paused,
                "sendsPaused": namespace.sends_paused,
                "burnsPaused": namespace.burns_paused,
                "rolePermissions": [
                    {
                        "role": role_permission.role,
                        "permissions": role_permission.permissions,
                    }
                ],
                "addressRoles": [
                    {
                        "address": address_roles.address,
                        "roles": address_roles.roles,
                    }
                ],
            }
        }

        assert namespace_result == expected_namespace

    @pytest.mark.asyncio
    async def test_fetch_address_roles(
        self,
        permissions_servicer,
    ):
        roles = ["role1", "role2"]
        permissions_servicer.address_roles_responses.append(permissions_query_pb.QueryAddressRolesResponse(roles=roles))

        api = self._api_instance(servicer=permissions_servicer)

        address_roles = await api.fetch_address_roles(
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            address="inj1knhahceyp57j5x7xh69p7utegnnnfgxavmahjr",
        )
        expected_roles = {
            "roles": roles,
        }

        assert address_roles == expected_roles

    @pytest.mark.asyncio
    async def test_fetch_addresses_by_role(
        self,
        permissions_servicer,
    ):
        addresses = ["inj1knhahceyp57j5x7xh69p7utegnnnfgxavmahjr"]
        permissions_servicer.addresses_by_role_responses.append(
            permissions_query_pb.QueryAddressesByRoleResponse(addresses=addresses)
        )

        api = self._api_instance(servicer=permissions_servicer)

        addresses_response = await api.fetch_addresses_by_role(
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            role="role1",
        )
        expected_addresses = {
            "addresses": addresses,
        }

        assert addresses_response == expected_addresses

    @pytest.mark.asyncio
    async def test_fetch_vouchers_for_address(
        self,
        permissions_servicer,
    ):
        coin = coin_pb.Coin(denom="inj", amount="988987297011197594664")

        permissions_servicer.vouchers_for_address_responses.append(
            permissions_query_pb.QueryVouchersForAddressResponse(vouchers=[coin])
        )

        api = self._api_instance(servicer=permissions_servicer)

        vouchers = await api.fetch_vouchers_for_address(
            address="inj1knhahceyp57j5x7xh69p7utegnnnfgxavmahjr",
        )
        expected_vouchers = {
            "vouchers": [{"denom": coin.denom, "amount": coin.amount}],
        }

        assert vouchers == expected_vouchers

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = ChainGrpcPermissionsApi(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer

        return api
