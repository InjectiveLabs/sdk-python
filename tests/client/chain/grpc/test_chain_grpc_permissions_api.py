import grpc
import pytest

from pyinjective.client.chain.grpc.chain_grpc_permissions_api import ChainGrpcPermissionsApi
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as coin_pb
from pyinjective.proto.injective.permissions.v1beta1 import (
    genesis_pb2 as genesis_pb,
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
    async def test_fetch_namespace_denoms(
        self,
        permissions_servicer,
    ):
        denom = "peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5"
        permissions_servicer.namespace_denoms_responses.append(
            permissions_query_pb.QueryNamespaceDenomsResponse(denoms=[denom])
        )

        api = self._api_instance(servicer=permissions_servicer)

        all_denoms = await api.fetch_namespace_denoms()
        expected_denoms = {"denoms": [denom]}

        assert all_denoms == expected_denoms

    @pytest.mark.asyncio
    async def test_fetch_namespaces(
        self,
        permissions_servicer,
    ):
        role_permission = permissions_pb.Role(
            name="role1",
            role_id=1,
            permissions=3,
        )
        actor_role = permissions_pb.ActorRoles(
            actor="actor",
            roles=["role1"],
        )
        role_manager = permissions_pb.RoleManager(
            manager="manager",
            roles=["role1"],
        )
        policy_status = permissions_pb.PolicyStatus(
            action=permissions_pb.Action.Value("MINT"),
            is_disabled=False,
            is_sealed=False,
        )
        policy_manager_capability = permissions_pb.PolicyManagerCapability(
            manager="manager",
            action=permissions_pb.Action.Value("RECEIVE"),
            can_disable=True,
            can_seal=False,
        )
        namespace = permissions_pb.Namespace(
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            contract_hook="wasm_hook",
            role_permissions=[role_permission],
            actor_roles=[actor_role],
            role_managers=[role_manager],
            policy_statuses=[policy_status],
            policy_manager_capabilities=[policy_manager_capability],
        )
        permissions_servicer.namespaces_responses.append(
            permissions_query_pb.QueryNamespacesResponse(namespaces=[namespace])
        )

        api = self._api_instance(servicer=permissions_servicer)

        all_namespaces = await api.fetch_namespaces()
        expected_namespaces = {
            "namespaces": [
                {
                    "denom": namespace.denom,
                    "contractHook": namespace.contract_hook,
                    "rolePermissions": [
                        {
                            "name": role_permission.name,
                            "roleId": role_permission.role_id,
                            "permissions": role_permission.permissions,
                        }
                    ],
                    "actorRoles": [
                        {
                            "actor": actor_role.actor,
                            "roles": actor_role.roles,
                        }
                    ],
                    "roleManagers": [
                        {
                            "manager": role_manager.manager,
                            "roles": role_manager.roles,
                        }
                    ],
                    "policyStatuses": [
                        {
                            "action": permissions_pb.Action.Name(policy_status.action),
                            "isDisabled": policy_status.is_disabled,
                            "isSealed": policy_status.is_sealed,
                        }
                    ],
                    "policyManagerCapabilities": [
                        {
                            "manager": policy_manager_capability.manager,
                            "action": permissions_pb.Action.Name(policy_manager_capability.action),
                            "canDisable": policy_manager_capability.can_disable,
                            "canSeal": policy_manager_capability.can_seal,
                        }
                    ],
                }
            ]
        }

        assert all_namespaces == expected_namespaces

    @pytest.mark.asyncio
    async def test_fetch_namespace(
        self,
        permissions_servicer,
    ):
        role_permission = permissions_pb.Role(
            name="role1",
            role_id=1,
            permissions=3,
        )
        actor_role = permissions_pb.ActorRoles(
            actor="actor",
            roles=["role1"],
        )
        role_manager = permissions_pb.RoleManager(
            manager="manager",
            roles=["role1"],
        )
        policy_status = permissions_pb.PolicyStatus(
            action=permissions_pb.Action.Value("MINT"),
            is_disabled=False,
            is_sealed=False,
        )
        policy_manager_capability = permissions_pb.PolicyManagerCapability(
            manager="manager",
            action=permissions_pb.Action.Value("RECEIVE"),
            can_disable=True,
            can_seal=False,
        )
        namespace = permissions_pb.Namespace(
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            contract_hook="wasm_hook",
            role_permissions=[role_permission],
            actor_roles=[actor_role],
            role_managers=[role_manager],
            policy_statuses=[policy_status],
            policy_manager_capabilities=[policy_manager_capability],
        )
        permissions_servicer.namespace_responses.append(
            permissions_query_pb.QueryNamespaceResponse(namespace=namespace)
        )

        api = self._api_instance(servicer=permissions_servicer)

        all_namespaces = await api.fetch_namespace(denom=namespace.denom)
        expected_namespaces = {
            "namespace": {
                "denom": namespace.denom,
                "contractHook": namespace.contract_hook,
                "rolePermissions": [
                    {
                        "name": role_permission.name,
                        "roleId": role_permission.role_id,
                        "permissions": role_permission.permissions,
                    }
                ],
                "actorRoles": [
                    {
                        "actor": actor_role.actor,
                        "roles": actor_role.roles,
                    }
                ],
                "roleManagers": [
                    {
                        "manager": role_manager.manager,
                        "roles": role_manager.roles,
                    }
                ],
                "policyStatuses": [
                    {
                        "action": permissions_pb.Action.Name(policy_status.action),
                        "isDisabled": policy_status.is_disabled,
                        "isSealed": policy_status.is_sealed,
                    }
                ],
                "policyManagerCapabilities": [
                    {
                        "manager": policy_manager_capability.manager,
                        "action": permissions_pb.Action.Name(policy_manager_capability.action),
                        "canDisable": policy_manager_capability.can_disable,
                        "canSeal": policy_manager_capability.can_seal,
                    }
                ],
            }
        }

        assert all_namespaces == expected_namespaces

    @pytest.mark.asyncio
    async def test_fetch_roles_by_actor(
        self,
        permissions_servicer,
    ):
        roles = ["role1", "role2"]
        permissions_servicer.roles_by_actor_responses.append(
            permissions_query_pb.QueryRolesByActorResponse(roles=roles)
        )

        api = self._api_instance(servicer=permissions_servicer)

        roles_by_actor = await api.fetch_roles_by_actor(
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            actor="actor",
        )
        expected_roles = {
            "roles": roles,
        }

        assert roles_by_actor == expected_roles

    @pytest.mark.asyncio
    async def test_fetch_actors_by_role(
        self,
        permissions_servicer,
    ):
        actors = ["actor1", "actor2"]
        permissions_servicer.actors_by_role_responses.append(
            permissions_query_pb.QueryActorsByRoleResponse(actors=actors)
        )

        api = self._api_instance(servicer=permissions_servicer)

        actors_by_role = await api.fetch_actors_by_role(
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            role="role1",
        )
        expected_actors = {
            "actors": actors,
        }

        assert actors_by_role == expected_actors

    @pytest.mark.asyncio
    async def test_fetch_role_managers(
        self,
        permissions_servicer,
    ):
        role_manager = permissions_pb.RoleManager(
            manager="manager",
            roles=["role1"],
        )
        permissions_servicer.role_managers_responses.append(
            permissions_query_pb.QueryRoleManagersResponse(role_managers=[role_manager])
        )

        api = self._api_instance(servicer=permissions_servicer)

        managers = await api.fetch_role_managers(
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
        )
        expected_managers = {
            "roleManagers": [
                {
                    "manager": role_manager.manager,
                    "roles": role_manager.roles,
                }
            ],
        }

        assert managers == expected_managers

    @pytest.mark.asyncio
    async def test_fetch_role_manager(
        self,
        permissions_servicer,
    ):
        role_manager = permissions_pb.RoleManager(
            manager="manager",
            roles=["role1"],
        )
        permissions_servicer.role_manager_responses.append(
            permissions_query_pb.QueryRoleManagerResponse(role_manager=role_manager)
        )

        api = self._api_instance(servicer=permissions_servicer)

        managers = await api.fetch_role_manager(
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5", manager=role_manager.manager
        )
        expected_managers = {
            "roleManager": {
                "manager": role_manager.manager,
                "roles": role_manager.roles,
            }
        }

        assert managers == expected_managers

    @pytest.mark.asyncio
    async def test_fetch_policy_statuses(
        self,
        permissions_servicer,
    ):
        policy_status = permissions_pb.PolicyStatus(
            action=permissions_pb.Action.Value("MINT"),
            is_disabled=False,
            is_sealed=True,
        )
        permissions_servicer.policy_statuses_responses.append(
            permissions_query_pb.QueryPolicyStatusesResponse(policy_statuses=[policy_status])
        )

        api = self._api_instance(servicer=permissions_servicer)

        statuses = await api.fetch_policy_statuses(
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
        )
        expected_statuses = {
            "policyStatuses": [
                {
                    "action": permissions_pb.Action.Name(policy_status.action),
                    "isDisabled": policy_status.is_disabled,
                    "isSealed": policy_status.is_sealed,
                }
            ],
        }

        assert statuses == expected_statuses

    @pytest.mark.asyncio
    async def test_fetch_policy_manager_capabilities(
        self,
        permissions_servicer,
    ):
        policy_manager_capability = permissions_pb.PolicyManagerCapability(
            manager="manager",
            action=permissions_pb.Action.Value("RECEIVE"),
            can_disable=True,
            can_seal=False,
        )
        permissions_servicer.policy_manager_capabilities_responses.append(
            permissions_query_pb.QueryPolicyManagerCapabilitiesResponse(
                policy_manager_capabilities=[policy_manager_capability]
            )
        )

        api = self._api_instance(servicer=permissions_servicer)

        capabilities = await api.fetch_policy_manager_capabilities(
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
        )
        expected_capabilities = {
            "policyManagerCapabilities": [
                {
                    "manager": policy_manager_capability.manager,
                    "action": permissions_pb.Action.Name(policy_manager_capability.action),
                    "canDisable": policy_manager_capability.can_disable,
                    "canSeal": policy_manager_capability.can_seal,
                }
            ],
        }

        assert capabilities == expected_capabilities

    @pytest.mark.asyncio
    async def test_fetch_vouchers(
        self,
        permissions_servicer,
    ):
        voucher = permissions_pb.AddressVoucher(
            address="inj1ady3s7whq30l4fx8sj3x6muv5mx4dfdlcpv8n7",
            voucher=coin_pb.Coin(denom="inj", amount="1000000000"),
        )
        permissions_servicer.vouchers_responses.append(permissions_query_pb.QueryVouchersResponse(vouchers=[voucher]))

        api = self._api_instance(servicer=permissions_servicer)

        all_vouchers = await api.fetch_vouchers(
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
        )
        expected_vouchers = {
            "vouchers": [
                {
                    "address": voucher.address,
                    "voucher": {
                        "denom": voucher.voucher.denom,
                        "amount": voucher.voucher.amount,
                    },
                }
            ],
        }

        assert all_vouchers == expected_vouchers

    @pytest.mark.asyncio
    async def test_fetch_voucher(
        self,
        permissions_servicer,
    ):
        voucher = coin_pb.Coin(denom="inj", amount="1000000000")
        permissions_servicer.voucher_responses.append(permissions_query_pb.QueryVoucherResponse(voucher=voucher))

        api = self._api_instance(servicer=permissions_servicer)

        fetched_voucher = await api.fetch_voucher(
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            address="inj1ady3s7whq30l4fx8sj3x6muv5mx4dfdlcpv8n7",
        )
        expected_voucher = {
            "voucher": {
                "denom": voucher.denom,
                "amount": voucher.amount,
            },
        }

        assert fetched_voucher == expected_voucher

    @pytest.mark.asyncio
    async def test_fetch_permissions_module_state(
        self,
        permissions_servicer,
    ):
        params = permissions_params_pb.Params(
            wasm_hook_query_max_gas=1000000,
        )
        role_permission = permissions_pb.Role(
            name="role1",
            role_id=1,
            permissions=3,
        )
        actor_role = permissions_pb.ActorRoles(
            actor="actor",
            roles=["role1"],
        )
        role_manager = permissions_pb.RoleManager(
            manager="manager",
            roles=["role1"],
        )
        policy_status = permissions_pb.PolicyStatus(
            action=permissions_pb.Action.Value("MINT"),
            is_disabled=False,
            is_sealed=False,
        )
        policy_manager_capability = permissions_pb.PolicyManagerCapability(
            manager="manager",
            action=permissions_pb.Action.Value("RECEIVE"),
            can_disable=True,
            can_seal=False,
        )
        namespace = permissions_pb.Namespace(
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            contract_hook="wasm_hook",
            role_permissions=[role_permission],
            actor_roles=[actor_role],
            role_managers=[role_manager],
            policy_statuses=[policy_status],
            policy_manager_capabilities=[policy_manager_capability],
        )
        voucher = permissions_pb.AddressVoucher(
            address="inj1ady3s7whq30l4fx8sj3x6muv5mx4dfdlcpv8n7",
            voucher=coin_pb.Coin(denom="inj", amount="1000000000"),
        )
        module_state = genesis_pb.GenesisState(
            params=params,
            namespaces=[namespace],
            vouchers=[voucher],
        )
        permissions_servicer.module_state_responses.append(
            permissions_query_pb.QueryModuleStateResponse(
                state=module_state,
            )
        )

        api = self._api_instance(servicer=permissions_servicer)

        fetched_module_state = await api.fetch_permissions_module_state()
        expected_module_state = {
            "state": {
                "params": {
                    "wasmHookQueryMaxGas": str(params.wasm_hook_query_max_gas),
                },
                "namespaces": [
                    {
                        "denom": namespace.denom,
                        "contractHook": namespace.contract_hook,
                        "rolePermissions": [
                            {
                                "name": role_permission.name,
                                "roleId": role_permission.role_id,
                                "permissions": role_permission.permissions,
                            }
                        ],
                        "actorRoles": [
                            {
                                "actor": actor_role.actor,
                                "roles": actor_role.roles,
                            }
                        ],
                        "roleManagers": [
                            {
                                "manager": role_manager.manager,
                                "roles": role_manager.roles,
                            }
                        ],
                        "policyStatuses": [
                            {
                                "action": permissions_pb.Action.Name(policy_status.action),
                                "isDisabled": policy_status.is_disabled,
                                "isSealed": policy_status.is_sealed,
                            }
                        ],
                        "policyManagerCapabilities": [
                            {
                                "manager": policy_manager_capability.manager,
                                "action": permissions_pb.Action.Name(policy_manager_capability.action),
                                "canDisable": policy_manager_capability.can_disable,
                                "canSeal": policy_manager_capability.can_seal,
                            }
                        ],
                    }
                ],
                "vouchers": [
                    {
                        "address": voucher.address,
                        "voucher": {
                            "denom": voucher.voucher.denom,
                            "amount": voucher.voucher.amount,
                        },
                    }
                ],
            }
        }

        assert fetched_module_state == expected_module_state

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = ChainGrpcPermissionsApi(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer

        return api
