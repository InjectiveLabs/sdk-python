import base64

import grpc
import pytest

from pyinjective.client.chain.grpc.chain_grpc_bank_api import ChainGrpcBankApi
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network
from pyinjective.proto.cosmos.bank.v1beta1 import bank_pb2 as bank_pb, query_pb2 as bank_query_pb
from pyinjective.proto.cosmos.base.query.v1beta1 import pagination_pb2 as pagination_pb
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as coin_pb
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
        bank_servicer.bank_params.append(bank_query_pb.QueryParamsResponse(params=params))

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = ChainGrpcBankApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = bank_servicer

        module_params = await api.fetch_module_params()
        expected_params = {
            "params": {
                "defaultSendEnabled": True,
                "sendEnabled": [],
            }
        }

        assert expected_params == module_params

    @pytest.mark.asyncio
    async def test_fetch_balance(
        self,
        bank_servicer,
    ):
        balance = coin_pb.Coin(denom="inj", amount="988987297011197594664")
        bank_servicer.balance_responses.append(bank_query_pb.QueryBalanceResponse(balance=balance))

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = ChainGrpcBankApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = bank_servicer

        bank_balance = await api.fetch_balance(
            account_address="inj1cml96vmptgw99syqrrz8az79xer2pcgp0a885r", denom="inj"
        )
        expected_balance = {"denom": "inj", "amount": "988987297011197594664"}

        assert expected_balance == bank_balance

    @pytest.mark.asyncio
    async def test_fetch_balance(
        self,
        bank_servicer,
    ):
        balance = coin_pb.Coin(denom="inj", amount="988987297011197594664")
        bank_servicer.balance_responses.append(bank_query_pb.QueryBalanceResponse(balance=balance))

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = ChainGrpcBankApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = bank_servicer

        bank_balance = await api.fetch_balance(
            account_address="inj1cml96vmptgw99syqrrz8az79xer2pcgp0a885r", denom="inj"
        )
        expected_balance = {
            "balance": {
                "denom": "inj",
                "amount": "988987297011197594664",
            }
        }

        assert expected_balance == bank_balance

    @pytest.mark.asyncio
    async def test_fetch_balances(
        self,
        bank_servicer,
    ):
        first_balance = coin_pb.Coin(denom="inj", amount="988987297011197594664")
        second_balance = coin_pb.Coin(denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5", amount="54497408")
        pagination = pagination_pb.PageResponse(total=2)

        bank_servicer.balances_responses.append(
            bank_query_pb.QueryAllBalancesResponse(
                balances=[first_balance, second_balance],
                pagination=pagination,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = ChainGrpcBankApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = bank_servicer

        bank_balances = await api.fetch_balances(
            account_address="inj1cml96vmptgw99syqrrz8az79xer2pcgp0a885r",
        )
        expected_balances = {
            "balances": [{"denom": coin.denom, "amount": coin.amount} for coin in [first_balance, second_balance]],
            "pagination": {"nextKey": "", "total": "2"},
        }

        assert expected_balances == bank_balances

    @pytest.mark.asyncio
    async def test_fetch_spendable_balances(
        self,
        bank_servicer,
    ):
        first_balance = coin_pb.Coin(denom="inj", amount="988987297011197594664")
        second_balance = coin_pb.Coin(denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5", amount="54497408")
        pagination = pagination_pb.PageResponse(total=2)

        bank_servicer.spendable_balances_responses.append(
            bank_query_pb.QuerySpendableBalancesResponse(
                balances=[first_balance, second_balance],
                pagination=pagination,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = ChainGrpcBankApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = bank_servicer

        balances = await api.fetch_spendable_balances(
            account_address="inj1cml96vmptgw99syqrrz8az79xer2pcgp0a885r",
            pagination=PaginationOption(
                skip=0,
                limit=100,
            ),
        )
        expected_balances = {
            "balances": [{"denom": coin.denom, "amount": coin.amount} for coin in [first_balance, second_balance]],
            "pagination": {"nextKey": "", "total": "2"},
        }

        assert expected_balances == balances

    @pytest.mark.asyncio
    async def test_fetch_spendable_balances_by_denom(
        self,
        bank_servicer,
    ):
        first_balance = coin_pb.Coin(denom="inj", amount="988987297011197594664")

        bank_servicer.spendable_balances_by_denom_responses.append(
            bank_query_pb.QuerySpendableBalanceByDenomResponse(balance=first_balance)
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = ChainGrpcBankApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = bank_servicer

        balances = await api.fetch_spendable_balances_by_denom(
            account_address="inj1cml96vmptgw99syqrrz8az79xer2pcgp0a885r",
            denom=first_balance.denom,
        )
        expected_balances = {
            "balance": {"denom": first_balance.denom, "amount": first_balance.amount},
        }

        assert expected_balances == balances

    @pytest.mark.asyncio
    async def test_fetch_total_supply(
        self,
        bank_servicer,
    ):
        first_supply = coin_pb.Coin(
            denom="factory/inj108t3mlej0dph8er6ca2lq5cs9pdgzva5mqsn5p/position", amount="5556700000000000000"
        )
        second_supply = coin_pb.Coin(
            denom="factory/inj10uycavvkc4uqr8tns3599r0t2xux4rz3y8apym/1684002313InjUsdt1d110C",
            amount="1123456789111100000",
        )
        pagination = pagination_pb.PageResponse(
            next_key=(
                "factory/inj1vkrp72xd67plcggcfjtjelqa4t5a093xljf2vj/" "inj1spw6nd0pj3kd3fgjljhuqpc8tv72a9v89myuja"
            ).encode(),
            total=179,
        )

        bank_servicer.total_supply_responses.append(
            bank_query_pb.QueryTotalSupplyResponse(
                supply=[first_supply, second_supply],
                pagination=pagination,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = ChainGrpcBankApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = bank_servicer

        total_supply = await api.fetch_total_supply()
        next_key = "factory/inj1vkrp72xd67plcggcfjtjelqa4t5a093xljf2vj/inj1spw6nd0pj3kd3fgjljhuqpc8tv72a9v89myuja"
        expected_supply = {
            "supply": [{"denom": coin.denom, "amount": coin.amount} for coin in [first_supply, second_supply]],
            "pagination": {
                "nextKey": base64.b64encode(next_key.encode()).decode(),
                "total": "179",
            },
        }

        assert expected_supply == total_supply

    @pytest.mark.asyncio
    async def test_fetch_supply_of(
        self,
        bank_servicer,
    ):
        first_supply = coin_pb.Coin(
            denom="factory/inj108t3mlej0dph8er6ca2lq5cs9pdgzva5mqsn5p/position", amount="5556700000000000000"
        )

        bank_servicer.supply_of_responses.append(
            bank_query_pb.QuerySupplyOfResponse(
                amount=first_supply,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = ChainGrpcBankApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = bank_servicer

        total_supply = await api.fetch_supply_of(denom=first_supply.denom)
        expected_supply = {"amount": {"denom": first_supply.denom, "amount": first_supply.amount}}

        assert expected_supply == total_supply

    @pytest.mark.asyncio
    async def test_fetch_denom_metadata(
        self,
        bank_servicer,
    ):
        first_denom_unit = bank_pb.DenomUnit(
            denom="factory/inj105ujajd95znwjvcy3hwcz80pgy8tc6v77spur0/SMART", exponent=0, aliases=["microSMART"]
        )
        second_denom_unit = bank_pb.DenomUnit(denom="SMART", exponent=6, aliases=["SMART"])
        metadata = bank_pb.Metadata(
            description="SMART",
            denom_units=[first_denom_unit, second_denom_unit],
            base="factory/inj105ujajd95znwjvcy3hwcz80pgy8tc6v77spur0/SMART",
            display="SMART",
            name="SMART",
            symbol="SMART",
            uri=(
                "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/"
                "Flag_of_the_People%27s_Republic_of_China.svg/"
                "2560px-Flag_of_the_People%27s_Republic_of_China.svg.png"
            ),
            uri_hash="",
        )

        bank_servicer.denom_metadata_responses.append(
            bank_query_pb.QueryDenomMetadataResponse(
                metadata=metadata,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = ChainGrpcBankApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = bank_servicer

        denom_metadata = await api.fetch_denom_metadata(denom=metadata.base)

        expected_denom_metadata = {
            "metadata": {
                "description": metadata.description,
                "denomUnits": [
                    {"denom": denom.denom, "exponent": denom.exponent, "aliases": denom.aliases}
                    for denom in [first_denom_unit, second_denom_unit]
                ],
                "base": metadata.base,
                "display": metadata.display,
                "name": metadata.name,
                "symbol": metadata.symbol,
                "uri": metadata.uri,
                "uriHash": metadata.uri_hash,
            }
        }

        assert expected_denom_metadata == denom_metadata

    @pytest.mark.asyncio
    async def test_fetch_denoms_metadata(
        self,
        bank_servicer,
    ):
        first_denom_unit = bank_pb.DenomUnit(
            denom="factory/inj105ujajd95znwjvcy3hwcz80pgy8tc6v77spur0/SMART", exponent=0, aliases=["microSMART"]
        )
        second_denom_unit = bank_pb.DenomUnit(denom="SMART", exponent=6, aliases=["SMART"])
        metadata = bank_pb.Metadata(
            description="SMART",
            denom_units=[first_denom_unit, second_denom_unit],
            base="factory/inj105ujajd95znwjvcy3hwcz80pgy8tc6v77spur0/SMART",
            display="SMART",
            name="SMART",
            symbol="SMART",
            uri=(
                "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/"
                "Flag_of_the_People%27s_Republic_of_China.svg/"
                "2560px-Flag_of_the_People%27s_Republic_of_China.svg.png"
            ),
            uri_hash="",
        )
        pagination = pagination_pb.PageResponse(
            next_key=(
                "factory/inj1vkrp72xd67plcggcfjtjelqa4t5a093xljf2vj/" "inj1spw6nd0pj3kd3fgjljhuqpc8tv72a9v89myuja"
            ).encode(),
            total=179,
        )

        bank_servicer.denoms_metadata_responses.append(
            bank_query_pb.QueryDenomsMetadataResponse(
                metadatas=[metadata],
                pagination=pagination,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = ChainGrpcBankApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = bank_servicer

        denoms_metadata = await api.fetch_denoms_metadata(
            pagination=PaginationOption(
                skip=0,
                limit=100,
            ),
        )
        next_key = "factory/inj1vkrp72xd67plcggcfjtjelqa4t5a093xljf2vj/inj1spw6nd0pj3kd3fgjljhuqpc8tv72a9v89myuja"
        expected_denoms_metadata = {
            "metadatas": [
                {
                    "description": metadata.description,
                    "denomUnits": [
                        {"denom": denom.denom, "exponent": denom.exponent, "aliases": denom.aliases}
                        for denom in [first_denom_unit, second_denom_unit]
                    ],
                    "base": metadata.base,
                    "display": metadata.display,
                    "name": metadata.name,
                    "symbol": metadata.symbol,
                    "uri": metadata.uri,
                    "uriHash": metadata.uri_hash,
                },
            ],
            "pagination": {
                "nextKey": base64.b64encode(next_key.encode()).decode(),
                "total": "179",
            },
        }

        assert expected_denoms_metadata == denoms_metadata

    @pytest.mark.asyncio
    async def test_fetch_denom_owners(
        self,
        bank_servicer,
    ):
        balance = coin_pb.Coin(denom="inj", amount="988987297011197594664")
        denom_owner = bank_query_pb.DenomOwner(address="inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r", balance=balance)
        pagination = pagination_pb.PageResponse(
            next_key=(
                "factory/inj1vkrp72xd67plcggcfjtjelqa4t5a093xljf2vj/" "inj1spw6nd0pj3kd3fgjljhuqpc8tv72a9v89myuja"
            ).encode(),
            total=179,
        )

        bank_servicer.denom_owners_responses.append(
            bank_query_pb.QueryDenomOwnersResponse(
                denom_owners=[denom_owner],
                pagination=pagination,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = ChainGrpcBankApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = bank_servicer

        denoms_metadata = await api.fetch_denom_owners(
            denom=balance.denom,
            pagination=PaginationOption(
                skip=0,
                limit=100,
            ),
        )
        next_key = "factory/inj1vkrp72xd67plcggcfjtjelqa4t5a093xljf2vj/inj1spw6nd0pj3kd3fgjljhuqpc8tv72a9v89myuja"
        expected_denoms_metadata = {
            "denomOwners": [
                {
                    "address": denom_owner.address,
                    "balance": {
                        "denom": balance.denom,
                        "amount": balance.amount,
                    },
                },
            ],
            "pagination": {
                "nextKey": base64.b64encode(next_key.encode()).decode(),
                "total": "179",
            },
        }

        assert expected_denoms_metadata == denoms_metadata

    @pytest.mark.asyncio
    async def test_fetch_send_enabled(
        self,
        bank_servicer,
    ):
        send_enabled = bank_pb.SendEnabled(
            denom="inj",
            enabled=True,
        )
        pagination = pagination_pb.PageResponse(
            next_key=(
                "factory/inj1vkrp72xd67plcggcfjtjelqa4t5a093xljf2vj/" "inj1spw6nd0pj3kd3fgjljhuqpc8tv72a9v89myuja"
            ).encode(),
            total=179,
        )

        bank_servicer.send_enabled_responses.append(
            bank_query_pb.QuerySendEnabledResponse(
                send_enabled=[send_enabled],
                pagination=pagination,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = ChainGrpcBankApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = bank_servicer

        denoms_metadata = await api.fetch_send_enabled(
            denoms=[send_enabled.denom],
            pagination=PaginationOption(
                skip=0,
                limit=100,
            ),
        )
        next_key = "factory/inj1vkrp72xd67plcggcfjtjelqa4t5a093xljf2vj/inj1spw6nd0pj3kd3fgjljhuqpc8tv72a9v89myuja"
        expected_denoms_metadata = {
            "sendEnabled": [
                {
                    "denom": send_enabled.denom,
                    "enabled": send_enabled.enabled,
                },
            ],
            "pagination": {
                "nextKey": base64.b64encode(next_key.encode()).decode(),
                "total": "179",
            },
        }

        assert expected_denoms_metadata == denoms_metadata

    async def _dummy_metadata_provider(self):
        return None
