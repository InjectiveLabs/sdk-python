import base64

import grpc
import pytest

from pyinjective.client.chain.grpc.chain_grpc_evm_api import ChainGrpcEVMApi
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.injective.evm.v1 import (
    chain_config_pb2 as evm_chain_config_pb,
    params_pb2 as evm_params_pb,
    query_pb2 as evm_query_pb,
)
from tests.client.chain.grpc.configurable_evm_query_servicer import ConfigurableEVMQueryServicer


@pytest.fixture
def evm_servicer():
    return ConfigurableEVMQueryServicer()


class TestChainGrpcEVMApi:
    @pytest.mark.asyncio
    async def test_fetch_evm_params(
        self,
        evm_servicer,
    ):
        # Create a chain_config with different values for each variable
        chain_config = evm_chain_config_pb.ChainConfig(
            homestead_block="1000000",
            dao_fork_block="1500000",
            dao_fork_support=True,
            eip150_block="2000000",
            eip150_hash="0x2086799aeebeae135c246c65021c82b4e15a2c451340993aacfd2751886514f0",
            eip155_block="2500000",
            eip158_block="3000000",
            byzantium_block="4000000",
            constantinople_block="5000000",
            petersburg_block="6000000",
            istanbul_block="7000000",
            muir_glacier_block="8000000",
            berlin_block="9000000",
            london_block="10000000",
            arrow_glacier_block="11000000",
            gray_glacier_block="12000000",
            merge_netsplit_block="13000000",
            shanghai_time="14000000",
            cancun_time="15000000",
            prague_time="16000000",
            eip155_chain_id="1337",  # Common test chain ID
        )

        params = evm_params_pb.Params(
            evm_denom="inj",
            enable_create=True,
            enable_call=False,
            extra_eips=[11, 12],
            chain_config=chain_config,
            allow_unprotected_txs=True,
            authorized_deployers=["inj1ady3s7whq30l4fx8sj3x6muv5mx4dfdlcpv8n7"],
            permissioned=False,
        )

        evm_servicer.params_responses.append(
            evm_query_pb.QueryParamsResponse(
                params=params,
            )
        )

        api = self._api_instance(evm_servicer)
        response = await api.fetch_params()

        expected_params = {
            "params": {
                "evmDenom": "inj",
                "enableCreate": True,
                "enableCall": False,
                "extraEips": ["11", "12"],
                "chainConfig": {
                    "homesteadBlock": "1000000",
                    "daoForkBlock": "1500000",
                    "daoForkSupport": True,
                    "eip150Block": "2000000",
                    "eip150Hash": "0x2086799aeebeae135c246c65021c82b4e15a2c451340993aacfd2751886514f0",
                    "eip155Block": "2500000",
                    "eip158Block": "3000000",
                    "byzantiumBlock": "4000000",
                    "constantinopleBlock": "5000000",
                    "petersburgBlock": "6000000",
                    "istanbulBlock": "7000000",
                    "muirGlacierBlock": "8000000",
                    "berlinBlock": "9000000",
                    "londonBlock": "10000000",
                    "arrowGlacierBlock": "11000000",
                    "grayGlacierBlock": "12000000",
                    "mergeNetsplitBlock": "13000000",
                    "shanghaiTime": "14000000",
                    "cancunTime": "15000000",
                    "pragueTime": "16000000",
                    "eip155ChainId": "1337",
                },
                "allowUnprotectedTxs": True,
                "authorizedDeployers": ["inj1ady3s7whq30l4fx8sj3x6muv5mx4dfdlcpv8n7"],
                "permissioned": False,
            }
        }

        assert response == expected_params

    @pytest.mark.asyncio
    async def test_fetch_account(self, evm_servicer):
        evm_servicer.account_responses.append(
            evm_query_pb.QueryAccountResponse(
                balance="1500.123",
                code_hash="0x0000000000000000000000000000000000000000000000000000000000000000",
                nonce=1234567890,
            )
        )

        api = self._api_instance(evm_servicer)
        response = await api.fetch_account(address="0xe28b3B32B6c345A34Ff64674606124Dd5Aceca30")

        expected_response = {
            "balance": "1500.123",
            "codeHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
            "nonce": "1234567890",
        }

        assert response == expected_response

    @pytest.mark.asyncio
    async def test_fetch_cosmos_account(self, evm_servicer):
        evm_servicer.cosmos_account_responses.append(
            evm_query_pb.QueryCosmosAccountResponse(
                cosmos_address="inj1234567890abcdefghijklmnopqrstuvwxyz",
                sequence=1234567890,
                account_number=12344321,
            )
        )

        api = self._api_instance(evm_servicer)
        response = await api.fetch_cosmos_account(address="0xe28b3B32B6c345A34Ff64674606124Dd5Aceca30")

        expected_response = {
            "cosmosAddress": "inj1234567890abcdefghijklmnopqrstuvwxyz",
            "sequence": "1234567890",
            "accountNumber": "12344321",
        }

        assert response == expected_response

    @pytest.mark.asyncio
    async def test_fetch_validator_account(self, evm_servicer):
        evm_servicer.validator_account_responses.append(
            evm_query_pb.QueryValidatorAccountResponse(
                account_address="inj1234567890abcdefghijklmnopqrstuvwxyz",
                sequence=1234567890,
                account_number=12344321,
            )
        )

        api = self._api_instance(evm_servicer)
        response = await api.fetch_validator_account(cons_address="injvalcons1h5u937etuat5hnr2s34yaaalfpkkscl5ndadqm")

        expected_response = {
            "accountAddress": "inj1234567890abcdefghijklmnopqrstuvwxyz",
            "sequence": "1234567890",
            "accountNumber": "12344321",
        }

        assert response == expected_response

    @pytest.mark.asyncio
    async def test_fetch_balance(self, evm_servicer):
        evm_servicer.balance_responses.append(
            evm_query_pb.QueryBalanceResponse(
                balance="1500.123",
            )
        )

        api = self._api_instance(evm_servicer)
        response = await api.fetch_balance(address="0xe28b3B32B6c345A34Ff64674606124Dd5Aceca30")

        expected_response = {
            "balance": "1500.123",
        }

        assert response == expected_response

    @pytest.mark.asyncio
    async def test_fetch_storage(self, evm_servicer):
        evm_servicer.storage_responses.append(
            evm_query_pb.QueryStorageResponse(
                value="0x0000000000000000000000000000000000000000000000000000000000000000",
            )
        )

        api = self._api_instance(evm_servicer)
        response = await api.fetch_storage(
            address="0xe28b3B32B6c345A34Ff64674606124Dd5Aceca30",
            key="0x0000000000000000000000000000000000000000000000000000000000000000",
        )

        expected_response = {
            "value": "0x0000000000000000000000000000000000000000000000000000000000000000",
        }

        assert response == expected_response

    @pytest.mark.asyncio
    async def test_fetch_code(self, evm_servicer):
        code_response = evm_query_pb.QueryCodeResponse(
            code=b"\305\322F\001\206\367#<\222~}\262\334\307\003\300\345\000\266S\312\202';{\372\330\004]\205\244p",
        )
        evm_servicer.code_responses.append(code_response)

        api = self._api_instance(evm_servicer)
        response = await api.fetch_code(address="0xe28b3B32B6c345A34Ff64674606124Dd5Aceca30")

        expected_response = {
            "code": base64.b64encode(code_response.code).decode(),
        }

        assert response == expected_response

    @pytest.mark.asyncio
    async def test_fetch_base_fee(self, evm_servicer):
        evm_servicer.base_fee_responses.append(
            evm_query_pb.QueryBaseFeeResponse(
                base_fee="160000000",
            )
        )

        api = self._api_instance(evm_servicer)
        response = await api.fetch_base_fee()

        expected_response = {
            "baseFee": "160000000",
        }

        assert response == expected_response

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = ChainGrpcEVMApi(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer

        return api
