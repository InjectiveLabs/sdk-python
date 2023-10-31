from warnings import catch_warnings

import pytest

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network
from pyinjective.proto.cosmos.authz.v1beta1 import query_pb2 as authz_query
from pyinjective.proto.cosmos.bank.v1beta1 import query_pb2 as bank_query_pb
from pyinjective.proto.cosmos.tx.v1beta1 import service_pb2 as tx_service
from pyinjective.proto.exchange import (
    injective_accounts_rpc_pb2 as exchange_accounts_pb,
    injective_meta_rpc_pb2 as exchange_meta_pb,
    injective_oracle_rpc_pb2 as exchange_oracle_pb,
)
from pyinjective.proto.injective.types.v1beta1 import account_pb2 as account_pb
from tests.client.chain.grpc.configurable_auth_query_servicer import ConfigurableAuthQueryServicer
from tests.client.chain.grpc.configurable_autz_query_servicer import ConfigurableAuthZQueryServicer
from tests.client.chain.grpc.configurable_bank_query_servicer import ConfigurableBankQueryServicer
from tests.client.indexer.configurable_account_query_servicer import ConfigurableAccountQueryServicer
from tests.client.indexer.configurable_meta_query_servicer import ConfigurableMetaQueryServicer
from tests.client.indexer.configurable_oracle_query_servicer import ConfigurableOracleQueryServicer
from tests.core.tx.grpc.configurable_tx_query_servicer import ConfigurableTxQueryServicer


@pytest.fixture
def account_servicer():
    return ConfigurableAccountQueryServicer()


@pytest.fixture
def auth_servicer():
    return ConfigurableAuthQueryServicer()


@pytest.fixture
def authz_servicer():
    return ConfigurableAuthZQueryServicer()


@pytest.fixture
def bank_servicer():
    return ConfigurableBankQueryServicer()


@pytest.fixture
def meta_servicer():
    return ConfigurableMetaQueryServicer()


@pytest.fixture
def oracle_servicer():
    return ConfigurableOracleQueryServicer()


@pytest.fixture
def tx_servicer():
    return ConfigurableTxQueryServicer()


class TestAsyncClientDeprecationWarnings:
    def test_insecure_parameter_deprecation_warning(
        self,
        auth_servicer,
    ):
        with catch_warnings(record=True) as all_warnings:
            AsyncClient(
                network=Network.local(),
                insecure=False,
            )

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert (
            str(all_warnings[0].message) == "insecure parameter in AsyncClient is no longer used and will be deprecated"
        )

    @pytest.mark.asyncio
    async def test_get_account_deprecation_warning(
        self,
        auth_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubAuth = auth_servicer
        auth_servicer.account_responses.append(account_pb.EthAccount())

        with catch_warnings(record=True) as all_warnings:
            await client.get_account(address="")

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_account instead"

    @pytest.mark.asyncio
    async def test_get_bank_balance_deprecation_warning(
        self,
        bank_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubBank = bank_servicer
        bank_servicer.balance_responses.append(bank_query_pb.QueryBalanceResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_bank_balance(address="", denom="inj")

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_bank_balance instead"

    @pytest.mark.asyncio
    async def test_get_bank_balances_deprecation_warning(
        self,
        bank_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubBank = bank_servicer
        bank_servicer.balances_responses.append(bank_query_pb.QueryAllBalancesResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_bank_balances(address="")

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_bank_balances instead"

    @pytest.mark.asyncio
    async def test_get_order_states_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.order_states_responses.append(exchange_accounts_pb.OrderStatesResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_order_states(spot_order_hashes=["hash1"], derivative_order_hashes=["hash2"])

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_order_states instead"

    @pytest.mark.asyncio
    async def test_get_subaccount_list_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.subaccounts_list_responses.append(exchange_accounts_pb.SubaccountsListResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_subaccount_list(account_address="")

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_subaccounts_list instead"

    @pytest.mark.asyncio
    async def test_get_subaccount_balances_list_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.subaccount_balances_list_responses.append(
            exchange_accounts_pb.SubaccountBalancesListResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.get_subaccount_balances_list(subaccount_id="", denoms=[])

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_subaccount_balances_list instead"

    @pytest.mark.asyncio
    async def test_get_subaccount_balance_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.subaccount_balance_responses.append(exchange_accounts_pb.SubaccountBalanceEndpointResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_subaccount_balance(subaccount_id="", denom="")

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_subaccount_balance instead"

    @pytest.mark.asyncio
    async def test_get_subaccount_history_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.subaccount_history_responses.append(exchange_accounts_pb.SubaccountHistoryResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_subaccount_history(subaccount_id="")

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_subaccount_history instead"

    @pytest.mark.asyncio
    async def test_get_subaccount_order_summary_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.subaccount_order_summary_responses.append(
            exchange_accounts_pb.SubaccountOrderSummaryResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.get_subaccount_order_summary(subaccount_id="")

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_subaccount_order_summary instead"

    @pytest.mark.asyncio
    async def test_get_portfolio_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.portfolio_responses.append(exchange_accounts_pb.PortfolioResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_portfolio(account_address="")

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_portfolio instead"

    @pytest.mark.asyncio
    async def test_get_rewards_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.rewards_responses.append(exchange_accounts_pb.RewardsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_rewards(account_address="")

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_rewards instead"

    @pytest.mark.asyncio
    async def test_stream_subaccount_balance_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.stream_subaccount_balance_responses.append(
            exchange_accounts_pb.StreamSubaccountBalanceResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.stream_subaccount_balance(subaccount_id="")

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert (
            str(all_warnings[0].message) == "This method is deprecated. Use listen_subaccount_balance_updates instead"
        )

    @pytest.mark.asyncio
    async def test_get_grants_deprecation_warning(
        self,
        authz_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubAuthz = authz_servicer
        authz_servicer.grants_responses.append(authz_query.QueryGrantsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_grants(granter="granter", grantee="grantee")

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_grants instead"

    @pytest.mark.asyncio
    async def test_simulate_deprecation_warning(
        self,
        tx_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubTx = tx_servicer
        tx_servicer.simulate_responses.append(tx_service.SimulateResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.simulate_tx(tx_byte="".encode())

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use simulate instead"

    @pytest.mark.asyncio
    async def test_get_tx_deprecation_warning(
        self,
        tx_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubTx = tx_servicer
        tx_servicer.get_tx_responses.append(tx_service.GetTxResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_tx(tx_hash="")

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_tx instead"

    @pytest.mark.asyncio
    async def test_send_tx_sync_mode_deprecation_warning(
        self,
        tx_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubTx = tx_servicer
        tx_servicer.broadcast_responses.append(tx_service.BroadcastTxResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.send_tx_sync_mode(tx_byte="".encode())

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use broadcast_tx_sync_mode instead"

    @pytest.mark.asyncio
    async def test_send_tx_async_mode_deprecation_warning(
        self,
        tx_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubTx = tx_servicer
        tx_servicer.broadcast_responses.append(tx_service.BroadcastTxResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.send_tx_async_mode(tx_byte="".encode())

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use broadcast_tx_async_mode instead"

    @pytest.mark.asyncio
    async def test_send_tx_block_mode_deprecation_warning(
        self,
        tx_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubTx = tx_servicer
        tx_servicer.broadcast_responses.append(tx_service.BroadcastTxResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.send_tx_block_mode(tx_byte="".encode())

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. BLOCK broadcast mode should not be used"

    @pytest.mark.asyncio
    async def test_ping_deprecation_warning(
        self,
        meta_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubMeta = meta_servicer
        meta_servicer.ping_responses.append(exchange_meta_pb.PingResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.ping()

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_ping instead"

    @pytest.mark.asyncio
    async def test_version_deprecation_warning(
        self,
        meta_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubMeta = meta_servicer
        meta_servicer.version_responses.append(exchange_meta_pb.VersionResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.version()

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_version instead"

    @pytest.mark.asyncio
    async def test_info_deprecation_warning(
        self,
        meta_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubMeta = meta_servicer
        meta_servicer.info_responses.append(exchange_meta_pb.InfoResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.info()

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_info instead"

    @pytest.mark.asyncio
    async def test_stream_keepalive_deprecation_warning(
        self,
        meta_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExchangeAccount = account_servicer
        meta_servicer.stream_keepalive_responses.append(exchange_meta_pb.StreamKeepaliveResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.stream_keepalive()

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use listen_keepalive instead"

    @pytest.mark.asyncio
    async def test_oracle_list_deprecation_warning(
        self,
        oracle_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubOracle = oracle_servicer
        oracle_servicer.oracle_list_responses.append(exchange_oracle_pb.OracleListResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_oracle_list()

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_oracle_list instead"

    @pytest.mark.asyncio
    async def test_get_oracle_list_deprecation_warning(
        self,
        oracle_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubOracle = oracle_servicer
        oracle_servicer.oracle_list_responses.append(exchange_oracle_pb.OracleListResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_oracle_list()

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_oracle_list instead"

    @pytest.mark.asyncio
    async def test_get_oracle_prices_deprecation_warning(
        self,
        oracle_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubOracle = oracle_servicer
        oracle_servicer.price_responses.append(exchange_oracle_pb.PriceResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_oracle_prices(
                base_symbol="Gold",
                quote_symbol="USDT",
                oracle_type="pricefeed",
                oracle_scale_factor=6,
            )

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_oracle_price instead"

    @pytest.mark.asyncio
    async def test_stream_keepalive_deprecation_warning(
        self,
        oracle_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubOracle = oracle_servicer
        oracle_servicer.stream_prices_responses.append(exchange_oracle_pb.StreamPricesResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.stream_oracle_prices(
                base_symbol="Gold",
                quote_symbol="USDT",
                oracle_type="pricefeed",
            )

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use listen_oracle_prices_updates instead"
