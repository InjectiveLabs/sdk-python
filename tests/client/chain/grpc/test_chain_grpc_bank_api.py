import grpc
import pytest

from pyinjective.client.chain.grpc.chain_grpc_bank_api import ChainGrpcBankApi
from pyinjective.constant import Network
from pyinjective.proto.cosmos.bank.v1beta1 import (
    bank_pb2 as bank_pb,
    query_pb2 as bank_query_pb,
)
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as coin_pb
from pyinjective.proto.cosmos.base.query.v1beta1 import pagination_pb2 as pagination_pb
from tests.client.chain.grpc.configurable_bank_query_servicer import ConfigurableBankQueryServicer


@pytest.fixture
def bank_servicer():
    return ConfigurableBankQueryServicer()


class TestChainGrpcBankApi:

    @pytest.mark.asyncio
    async def test_fetch_module_params(
            self,
            bank_servicer,
    ):
        params = bank_pb.Params(default_send_enabled=True)
        bank_servicer.bank_params.append(bank_query_pb.QueryParamsResponse(
            params=params
        ))

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = ChainGrpcBankApi(channel=channel)
        api._stub = bank_servicer

        module_params = await api.fetch_module_params()
        expected_params = {
            "default_send_enabled": True,
        }

        assert (expected_params == module_params)

    @pytest.mark.asyncio
    async def test_fetch_balance(
            self,
            bank_servicer,
    ):
        balance = coin_pb.Coin(
            denom="inj",
            amount="988987297011197594664"
        )
        bank_servicer.balance_responses.append(bank_query_pb.QueryBalanceResponse(
            balance=balance
        ))

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = ChainGrpcBankApi(channel=channel)
        api._stub = bank_servicer

        bank_balance = await api.fetch_balance(
            account_address="inj1cml96vmptgw99syqrrz8az79xer2pcgp0a885r",
            denom="inj"
        )
        expected_balance = {
            "denom": "inj",
            "amount": "988987297011197594664"
        }

        assert (expected_balance == bank_balance)

    @pytest.mark.asyncio
    async def test_fetch_balance(
            self,
            bank_servicer,
    ):
        balance = coin_pb.Coin(
            denom="inj",
            amount="988987297011197594664"
        )
        bank_servicer.balance_responses.append(bank_query_pb.QueryBalanceResponse(
            balance=balance
        ))

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = ChainGrpcBankApi(channel=channel)
        api._stub = bank_servicer

        bank_balance = await api.fetch_balance(
            account_address="inj1cml96vmptgw99syqrrz8az79xer2pcgp0a885r",
            denom="inj"
        )
        expected_balance = {
            "denom": "inj",
            "amount": "988987297011197594664"
        }

        assert (expected_balance == bank_balance)

    @pytest.mark.asyncio
    async def test_fetch_balances(
            self,
            bank_servicer,
    ):
        first_balance = coin_pb.Coin(
            denom="inj",
            amount="988987297011197594664"
        )
        second_balance = coin_pb.Coin(
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            amount="54497408"
        )
        pagination = pagination_pb.PageResponse(total=2)

        bank_servicer.balances_responses.append(bank_query_pb.QueryAllBalancesResponse(
            balances=[first_balance, second_balance],
            pagination=pagination,
        ))

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = ChainGrpcBankApi(channel=channel)
        api._stub = bank_servicer

        bank_balances = await api.fetch_balances(
            account_address="inj1cml96vmptgw99syqrrz8az79xer2pcgp0a885r",
        )
        expected_balances = {
            "balances": [{"denom": coin.denom, "amount": coin.amount} for coin in [first_balance, second_balance]],
            "pagination": {"total": 2},
        }

        assert (expected_balances == bank_balances)

    @pytest.mark.asyncio
    async def test_fetch_total_supply(
            self,
            bank_servicer,
    ):
        first_supply = coin_pb.Coin(
            denom="factory/inj108t3mlej0dph8er6ca2lq5cs9pdgzva5mqsn5p/position",
            amount="5556700000000000000"
        )
        second_supply = coin_pb.Coin(
            denom="factory/inj10uycavvkc4uqr8tns3599r0t2xux4rz3y8apym/1684002313InjUsdt1d110C",
            amount="1123456789111100000"
        )
        pagination = pagination_pb.PageResponse(
            next_key="factory/inj1vkrp72xd67plcggcfjtjelqa4t5a093xljf2vj/inj1spw6nd0pj3kd3fgjljhuqpc8tv72a9v89myuja".encode(),
            total=179
        )

        bank_servicer.total_supply_responses.append(bank_query_pb.QueryTotalSupplyResponse(
            supply=[first_supply, second_supply],
            pagination=pagination,
        ))

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = ChainGrpcBankApi(channel=channel)
        api._stub = bank_servicer

        total_supply = await api.fetch_total_supply()
        expected_supply = {
            "supply": [{"denom": coin.denom, "amount": coin.amount} for coin in [first_supply, second_supply]],
            "pagination": {
                "next": "factory/inj1vkrp72xd67plcggcfjtjelqa4t5a093xljf2vj/inj1spw6nd0pj3kd3fgjljhuqpc8tv72a9v89myuja".encode(),
                "total": 179},
        }

        assert (expected_supply == total_supply)
