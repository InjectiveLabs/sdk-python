import grpc
import pytest

from pyinjective.client.chain.grpc.chain_grpc_txfees_api import ChainGrpcTxfeesApi
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.injective.txfees.v1beta1 import query_pb2 as txfees_query_pb, txfees_pb2 as txfees_pb
from tests.client.chain.grpc.configurable_txfees_query_servicer import ConfigurableTxfeesQueryServicer


@pytest.fixture
def txfees_query_servicer():
    return ConfigurableTxfeesQueryServicer()


class TestChainGrpcTxfeesApi:
    @pytest.mark.asyncio
    async def test_fetch_module_params(
        self,
        txfees_query_servicer,
    ):
        params = txfees_pb.Params(
            max_gas_wanted_per_tx=10,
            high_gas_tx_threshold=20,
            min_gas_price_for_high_gas_tx="30",
            mempool1559_enabled=True,
            min_gas_price="40",
            default_base_fee_multiplier="1.5",
            max_base_fee_multiplier="1.9",
            reset_interval=100,
            max_block_change_rate="0.75",
            target_block_space_percent_rate="0.4",
            recheck_fee_low_base_fee="0.15",
            recheck_fee_high_base_fee="0.25",
            recheck_fee_base_fee_threshold_multiplier="0.9",
        )
        txfees_query_servicer.params_responses.append(txfees_query_pb.QueryParamsResponse(params=params))

        api = self._api_instance(servicer=txfees_query_servicer)

        module_params = await api.fetch_module_params()
        expected_params = {
            "params": {
                "maxGasWantedPerTx": str(params.max_gas_wanted_per_tx),
                "highGasTxThreshold": str(params.high_gas_tx_threshold),
                "minGasPriceForHighGasTx": str(params.min_gas_price_for_high_gas_tx),
                "mempool1559Enabled": params.mempool1559_enabled,
                "minGasPrice": str(params.min_gas_price),
                "defaultBaseFeeMultiplier": str(params.default_base_fee_multiplier),
                "maxBaseFeeMultiplier": str(params.max_base_fee_multiplier),
                "resetInterval": str(params.reset_interval),
                "maxBlockChangeRate": str(params.max_block_change_rate),
                "targetBlockSpacePercentRate": str(params.target_block_space_percent_rate),
                "recheckFeeLowBaseFee": str(params.recheck_fee_low_base_fee),
                "recheckFeeHighBaseFee": str(params.recheck_fee_high_base_fee),
                "recheckFeeBaseFeeThresholdMultiplier": str(params.recheck_fee_base_fee_threshold_multiplier),
            }
        }

        assert module_params == expected_params

    @pytest.mark.asyncio
    async def test_fetch_eip_base_fee(self, txfees_query_servicer):
        eip_base_fee = txfees_query_pb.EipBaseFee(
            base_fee="1000000000000000000",
        )
        txfees_query_servicer.eip_base_fee_responses.append(
            txfees_query_pb.QueryEipBaseFeeResponse(base_fee=eip_base_fee)
        )

        api = self._api_instance(servicer=txfees_query_servicer)

        eip_base_fee_response = await api.fetch_eip_base_fee()
        expected_eip_base_fee = {"baseFee": {"baseFee": str(eip_base_fee.base_fee)}}

        assert eip_base_fee_response == expected_eip_base_fee

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = ChainGrpcTxfeesApi(channel=channel, cookie_assistant=cookie_assistant)
        api._query_stub = servicer

        return api
