import base64
import json

import grpc
import pytest

from pyinjective.client.chain.grpc.chain_grpc_wasm_api import ChainGrpcWasmApi
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.cosmos.base.query.v1beta1 import pagination_pb2 as pagination_pb
from pyinjective.proto.cosmwasm.wasm.v1 import query_pb2 as wasm_query_pb, types_pb2 as wasm_types_pb
from tests.client.chain.grpc.configurable_wasm_query_servicer import ConfigurableWasmQueryServicer


@pytest.fixture
def wasm_servicer():
    return ConfigurableWasmQueryServicer()


class TestChainGrpcBankApi:
    @pytest.mark.asyncio
    async def test_fetch_module_params(
        self,
        wasm_servicer,
    ):
        access_config = wasm_types_pb.AccessConfig(
            permission=0,
            addresses=["inj1ady3s7whq30l4fx8sj3x6muv5mx4dfdlcpv8n7"],
        )
        params = wasm_types_pb.Params(
            code_upload_access=access_config,
            instantiate_default_permission=0,
        )
        wasm_servicer.params_responses.append(wasm_query_pb.QueryParamsResponse(params=params))

        api = self._api_instance(servicer=wasm_servicer)

        module_params = await api.fetch_module_params()
        expected_params = {
            "params": {
                "codeUploadAccess": {
                    "permission": wasm_types_pb.AccessType.Name(access_config.permission),
                    "addresses": access_config.addresses,
                },
                "instantiateDefaultPermission": wasm_types_pb.AccessType.Name(params.instantiate_default_permission),
            }
        }

        assert module_params == expected_params

    @pytest.mark.asyncio
    async def test_fetch_contract_info(
        self,
        wasm_servicer,
    ):
        address = "inj1cml96vmptgw99syqrrz8az79xer2pcgp0a885r"
        tx_position = wasm_types_pb.AbsoluteTxPosition(
            block_height=1234,
            tx_index=9999,
        )
        contract_info = wasm_types_pb.ContractInfo(
            code_id=10,
            creator="inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r",
            admin="inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku",
            label="test label",
            created=tx_position,
            ibc_port_id="ibc port id",
        )
        wasm_servicer.contract_info_responses.append(
            wasm_query_pb.QueryContractInfoResponse(
                address=address,
                contract_info=contract_info,
            )
        )

        api = self._api_instance(servicer=wasm_servicer)

        info = await api.fetch_contract_info(address=address)
        expected_contract_info = {
            "address": address,
            "contractInfo": {
                "codeId": str(contract_info.code_id),
                "creator": contract_info.creator,
                "admin": contract_info.admin,
                "label": contract_info.label,
                "created": {
                    "blockHeight": str(tx_position.block_height),
                    "txIndex": str(tx_position.tx_index),
                },
                "ibcPortId": contract_info.ibc_port_id,
            },
        }

        assert info == expected_contract_info

    @pytest.mark.asyncio
    async def test_fetch_contract_history(
        self,
        wasm_servicer,
    ):
        tx_position = wasm_types_pb.AbsoluteTxPosition(
            block_height=1234,
            tx_index=9999,
        )
        history_entry = wasm_types_pb.ContractCodeHistoryEntry(
            operation=0,
            code_id=3770,
            updated=tx_position,
            msg="raw message test".encode(),
        )
        pagination = pagination_pb.PageResponse(
            next_key=(
                "factory/inj1vkrp72xd67plcggcfjtjelqa4t5a093xljf2vj/" "inj1spw6nd0pj3kd3fgjljhuqpc8tv72a9v89myuja"
            ).encode(),
            total=179,
        )

        wasm_servicer.contract_history_responses.append(
            wasm_query_pb.QueryContractHistoryResponse(
                entries=[history_entry],
                pagination=pagination,
            )
        )

        api = self._api_instance(servicer=wasm_servicer)

        info = await api.fetch_contract_history(
            address="inj18pp4vjwucpgg4nw3rr4wh4zyjg9ct5t8v9wqgj",
            pagination=PaginationOption(
                skip=0,
                limit=100,
            ),
        )
        expected_contract_info = {
            "entries": [
                {
                    "operation": wasm_types_pb.ContractCodeHistoryOperationType.Name(history_entry.operation),
                    "codeId": str(history_entry.code_id),
                    "updated": {
                        "blockHeight": str(tx_position.block_height),
                        "txIndex": str(tx_position.tx_index),
                    },
                    "msg": base64.b64encode(history_entry.msg).decode(),
                }
            ],
            "pagination": {
                "nextKey": base64.b64encode(pagination.next_key).decode(),
                "total": "179",
            },
        }

        assert info == expected_contract_info

    @pytest.mark.asyncio
    async def test_fetch_contracts_by_code(
        self,
        wasm_servicer,
    ):
        contract = "inj1z4l7jc8dj3y9484aqcrmf6y8mcctvkmm9zkf7n"
        pagination = pagination_pb.PageResponse(
            next_key=(
                "factory/inj1vkrp72xd67plcggcfjtjelqa4t5a093xljf2vj/" "inj1spw6nd0pj3kd3fgjljhuqpc8tv72a9v89myuja"
            ).encode(),
            total=179,
        )

        wasm_servicer.contracts_by_code_responses.append(
            wasm_query_pb.QueryContractsByCodeResponse(
                contracts=[contract],
                pagination=pagination,
            )
        )

        api = self._api_instance(servicer=wasm_servicer)

        info = await api.fetch_contracts_by_code(
            code_id=3770,
            pagination=PaginationOption(
                skip=0,
                limit=100,
            ),
        )
        expected_contract_info = {
            "contracts": [contract],
            "pagination": {
                "nextKey": base64.b64encode(pagination.next_key).decode(),
                "total": "179",
            },
        }

        assert info == expected_contract_info

    @pytest.mark.asyncio
    async def test_fetch_all_contracts_state(
        self,
        wasm_servicer,
    ):
        model = wasm_types_pb.Model(
            key=(
                "\x00\x08redeemed\x00*inj13t085sclq8fxy8d3gcjt3jap45j4fwlc79lykw" "\x00\x00\x00\x00\x00\x00\x00\x00"
            ).encode(),
            value='{"phase_id":0,"redeemed":1,"mint_limit":1}'.encode(),
        )
        pagination = pagination_pb.PageResponse(
            next_key=(
                "factory/inj1vkrp72xd67plcggcfjtjelqa4t5a093xljf2vj/" "inj1spw6nd0pj3kd3fgjljhuqpc8tv72a9v89myuja"
            ).encode(),
            total=179,
        )

        wasm_servicer.all_contracts_state_responses.append(
            wasm_query_pb.QueryAllContractStateResponse(
                models=[model],
                pagination=pagination,
            )
        )

        api = self._api_instance(servicer=wasm_servicer)

        info = await api.fetch_all_contracts_state(
            address="inj1z4l7jc8dj3y9484aqcrmf6y8mcctvkmm9zkf7n",
            pagination=PaginationOption(
                skip=0,
                limit=100,
            ),
        )
        expected_contract_info = {
            "models": [{"key": base64.b64encode(model.key).decode(), "value": base64.b64encode(model.value).decode()}],
            "pagination": {
                "nextKey": base64.b64encode(pagination.next_key).decode(),
                "total": "179",
            },
        }

        assert info == expected_contract_info

    @pytest.mark.asyncio
    async def test_fetch_raw_contract_state(
        self,
        wasm_servicer,
    ):
        data = "test data".encode()
        wasm_servicer.raw_contract_state_responses.append(
            wasm_query_pb.QueryRawContractStateResponse(
                data=data,
            )
        )

        api = self._api_instance(servicer=wasm_servicer)

        info = await api.fetch_raw_contract_state(
            address="inj1z4l7jc8dj3y9484aqcrmf6y8mcctvkmm9zkf7n",
            query_data="query data",
        )
        expected_contract_info = {
            "data": base64.b64encode(data).decode(),
        }

        assert info == expected_contract_info

    @pytest.mark.asyncio
    async def test_fetch_smart_contract_state(
        self,
        wasm_servicer,
    ):
        data = json.dumps({"count": 1037}).encode()
        wasm_servicer.smart_contract_state_responses.append(
            wasm_query_pb.QuerySmartContractStateResponse(
                data=data,
            )
        )

        api = self._api_instance(servicer=wasm_servicer)

        info = await api.fetch_smart_contract_state(
            address="inj1z4l7jc8dj3y9484aqcrmf6y8mcctvkmm9zkf7n",
            query_data="query data",
        )
        expected_contract_info = {
            "data": base64.b64encode(data).decode(),
        }

        assert info == expected_contract_info

    @pytest.mark.asyncio
    async def test_fetch_code(
        self,
        wasm_servicer,
    ):
        access_config = wasm_types_pb.AccessConfig(
            permission=0,
            addresses=["inj1ady3s7whq30l4fx8sj3x6muv5mx4dfdlcpv8n7"],
        )
        code_info_response = wasm_query_pb.CodeInfoResponse(
            code_id=290,
            creator="inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku",
            data_hash="0xf8e7689e23ac0c9d53f44a8fd98c686c20b0140a8d76d600e2c546bfbba7758d".encode(),
            instantiate_permission=access_config,
        )
        data = "code".encode()
        wasm_servicer.code_responses.append(
            wasm_query_pb.QueryCodeResponse(
                code_info=code_info_response,
                data=data,
            )
        )

        api = self._api_instance(servicer=wasm_servicer)

        info = await api.fetch_code(code_id=code_info_response.code_id)
        expected_contract_info = {
            "codeInfo": {
                "codeId": str(code_info_response.code_id),
                "creator": code_info_response.creator,
                "dataHash": base64.b64encode(code_info_response.data_hash).decode(),
                "instantiatePermission": {
                    "permission": wasm_types_pb.AccessType.Name(access_config.permission),
                    "addresses": access_config.addresses,
                },
            },
            "data": base64.b64encode(data).decode(),
        }

        assert info == expected_contract_info

    @pytest.mark.asyncio
    async def test_fetch_codes(
        self,
        wasm_servicer,
    ):
        access_config = wasm_types_pb.AccessConfig(
            permission=0,
            addresses=["inj1ady3s7whq30l4fx8sj3x6muv5mx4dfdlcpv8n7"],
        )
        code_info_response = wasm_query_pb.CodeInfoResponse(
            code_id=290,
            creator="inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku",
            data_hash="0xf8e7689e23ac0c9d53f44a8fd98c686c20b0140a8d76d600e2c546bfbba7758d".encode(),
            instantiate_permission=access_config,
        )
        pagination = pagination_pb.PageResponse(
            next_key=(
                "factory/inj1vkrp72xd67plcggcfjtjelqa4t5a093xljf2vj/" "inj1spw6nd0pj3kd3fgjljhuqpc8tv72a9v89myuja"
            ).encode(),
            total=179,
        )

        wasm_servicer.codes_responses.append(
            wasm_query_pb.QueryCodesResponse(
                code_infos=[code_info_response],
                pagination=pagination,
            )
        )

        api = self._api_instance(servicer=wasm_servicer)

        codes = await api.fetch_codes(
            pagination=PaginationOption(
                skip=0,
                limit=100,
            ),
        )
        expected_codes = {
            "codeInfos": [
                {
                    "codeId": str(code_info_response.code_id),
                    "creator": code_info_response.creator,
                    "dataHash": base64.b64encode(code_info_response.data_hash).decode(),
                    "instantiatePermission": {
                        "permission": wasm_types_pb.AccessType.Name(access_config.permission),
                        "addresses": access_config.addresses,
                    },
                },
            ],
            "pagination": {
                "nextKey": base64.b64encode(pagination.next_key).decode(),
                "total": "179",
            },
        }

        assert codes == expected_codes

    @pytest.mark.asyncio
    async def test_fetch_pinned_codes(
        self,
        wasm_servicer,
    ):
        code_id = 290
        pagination = pagination_pb.PageResponse(
            next_key=(
                "factory/inj1vkrp72xd67plcggcfjtjelqa4t5a093xljf2vj/" "inj1spw6nd0pj3kd3fgjljhuqpc8tv72a9v89myuja"
            ).encode(),
            total=179,
        )

        wasm_servicer.pinned_codes_responses.append(
            wasm_query_pb.QueryPinnedCodesResponse(
                code_ids=[code_id],
                pagination=pagination,
            )
        )

        api = self._api_instance(servicer=wasm_servicer)

        codes = await api.fetch_pinned_codes(
            pagination=PaginationOption(
                skip=0,
                limit=100,
            ),
        )
        expected_codes = {
            "codeIds": [str(code_id)],
            "pagination": {
                "nextKey": base64.b64encode(pagination.next_key).decode(),
                "total": "179",
            },
        }

        assert codes == expected_codes

    @pytest.mark.asyncio
    async def test_contracts_by_creator(
        self,
        wasm_servicer,
    ):
        contract_address = "inj1ady3s7whq30l4fx8sj3x6muv5mx4dfdlcpv8n7"
        pagination = pagination_pb.PageResponse(
            next_key=(
                "factory/inj1vkrp72xd67plcggcfjtjelqa4t5a093xljf2vj/" "inj1spw6nd0pj3kd3fgjljhuqpc8tv72a9v89myuja"
            ).encode(),
            total=179,
        )

        wasm_servicer.contracts_by_creator_responses.append(
            wasm_query_pb.QueryContractsByCreatorResponse(
                contract_addresses=[contract_address],
                pagination=pagination,
            )
        )

        api = self._api_instance(servicer=wasm_servicer)

        codes = await api.fetch_contracts_by_creator(
            creator_address="inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku",
            pagination=PaginationOption(
                skip=0,
                limit=100,
            ),
        )
        expected_codes = {
            "contractAddresses": [contract_address],
            "pagination": {
                "nextKey": base64.b64encode(pagination.next_key).decode(),
                "total": "179",
            },
        }

        assert codes == expected_codes

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = ChainGrpcWasmApi(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer

        return api
