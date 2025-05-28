import grpc
import pytest

from pyinjective.client.chain.grpc.chain_grpc_erc20_api import ChainGrpcERC20Api
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.injective.erc20.v1beta1 import (
    erc20_pb2 as erc20_pb,
    params_pb2 as erc20_params_pb,
    query_pb2 as erc20_query_pb,
)
from tests.client.chain.grpc.configurable_erc20_query_servicer import ConfigurableERC20QueryServicer


@pytest.fixture
def erc20_servicer():
    return ConfigurableERC20QueryServicer()


class TestChainGrpcBankApi:
    @pytest.mark.asyncio
    async def test_fetch_erc20_params(
        self,
        erc20_servicer,
    ):
        params = erc20_params_pb.Params()

        erc20_servicer.erc20_params_responses.append(
            erc20_query_pb.QueryParamsResponse(
                params=params,
            )
        )

        api = self._api_instance(erc20_servicer)
        response = await api.fetch_erc20_params()

        expected_params = {"params": {}}

        assert response == expected_params

    @pytest.mark.asyncio
    async def test_fetch_all_token_pairs(self, erc20_servicer):
        token_pair = erc20_pb.TokenPair(
            bank_denom="denom",
            erc20_address="0xd2C6753F6B1783EF0a3857275e16e79D91b539a3",
        )
        erc20_servicer.all_token_pairs_responses.append(
            erc20_query_pb.QueryAllTokenPairsResponse(token_pairs=[token_pair])
        )

        api = self._api_instance(erc20_servicer)
        response = await api.fetch_all_token_pairs()

        expected_token_pairs = {
            "tokenPairs": [
                {
                    "bankDenom": token_pair.bank_denom,
                    "erc20Address": token_pair.erc20_address,
                }
            ]
        }

        assert response == expected_token_pairs

    @pytest.mark.asyncio
    async def test_fetch_token_pair_by_denom(self, erc20_servicer):
        token_pair = erc20_pb.TokenPair(
            bank_denom="denom",
            erc20_address="0xd2C6753F6B1783EF0a3857275e16e79D91b539a3",
        )
        erc20_servicer.token_pair_by_denom_responses.append(
            erc20_query_pb.QueryTokenPairByDenomResponse(token_pair=token_pair)
        )

        api = self._api_instance(erc20_servicer)
        response = await api.fetch_token_pair_by_denom(bank_denom=token_pair.bank_denom)

        expected_token_pair = {
            "tokenPair": {
                "bankDenom": token_pair.bank_denom,
                "erc20Address": token_pair.erc20_address,
            }
        }

        assert response == expected_token_pair

    @pytest.mark.asyncio
    async def test_fetch_token_pair_by_erc20_address(self, erc20_servicer):
        token_pair = erc20_pb.TokenPair(
            bank_denom="denom",
            erc20_address="0xd2C6753F6B1783EF0a3857275e16e79D91b539a3",
        )
        erc20_servicer.token_pair_by_erc20_address_responses.append(
            erc20_query_pb.QueryTokenPairByERC20AddressResponse(token_pair=token_pair)
        )

        api = self._api_instance(erc20_servicer)
        response = await api.fetch_token_pair_by_erc20_address(erc20_address=token_pair.erc20_address)

        expected_token_pair = {
            "tokenPair": {
                "bankDenom": token_pair.bank_denom,
                "erc20Address": token_pair.erc20_address,
            }
        }

        assert response == expected_token_pair

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = ChainGrpcERC20Api(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer

        return api
