import asyncio
from copy import deepcopy
from decimal import Decimal
from typing import Any, Callable, Dict, List, Optional, Tuple

from google.protobuf import json_format

from pyinjective.client.chain.grpc.chain_grpc_auth_api import ChainGrpcAuthApi
from pyinjective.client.chain.grpc.chain_grpc_authz_api import ChainGrpcAuthZApi
from pyinjective.client.chain.grpc.chain_grpc_bank_api import ChainGrpcBankApi
from pyinjective.client.chain.grpc.chain_grpc_distribution_api import ChainGrpcDistributionApi
from pyinjective.client.chain.grpc.chain_grpc_erc20_api import ChainGrpcERC20Api
from pyinjective.client.chain.grpc.chain_grpc_evm_api import ChainGrpcEVMApi
from pyinjective.client.chain.grpc.chain_grpc_exchange_v2_api import ChainGrpcExchangeV2Api
from pyinjective.client.chain.grpc.chain_grpc_permissions_api import ChainGrpcPermissionsApi
from pyinjective.client.chain.grpc.chain_grpc_token_factory_api import ChainGrpcTokenFactoryApi
from pyinjective.client.chain.grpc.chain_grpc_txfees_api import ChainGrpcTxfeesApi
from pyinjective.client.chain.grpc.chain_grpc_wasm_api import ChainGrpcWasmApi
from pyinjective.client.chain.grpc_stream.chain_grpc_chain_stream import ChainGrpcChainStream
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.composer_v2 import Composer
from pyinjective.constant import GAS_PRICE
from pyinjective.core.ibc.channel.grpc.ibc_channel_grpc_api import IBCChannelGrpcApi
from pyinjective.core.ibc.client.grpc.ibc_client_grpc_api import IBCClientGrpcApi
from pyinjective.core.ibc.connection.grpc.ibc_connection_grpc_api import IBCConnectionGrpcApi
from pyinjective.core.ibc.transfer.grpc.ibc_transfer_grpc_api import IBCTransferGrpcApi
from pyinjective.core.market_v2 import BinaryOptionMarket, DerivativeMarket, SpotMarket
from pyinjective.core.network import Network
from pyinjective.core.tendermint.grpc.tendermint_grpc_api import TendermintGrpcApi
from pyinjective.core.token import Token
from pyinjective.core.tokens_file_loader import TokensFileLoader
from pyinjective.core.tx.grpc.tx_grpc_api import TxGrpcApi
from pyinjective.exceptions import NotFoundError
from pyinjective.proto.cosmos.auth.v1beta1 import query_pb2_grpc as auth_query_grpc
from pyinjective.proto.cosmos.authz.v1beta1 import query_pb2_grpc as authz_query_grpc
from pyinjective.proto.cosmos.bank.v1beta1 import query_pb2_grpc as bank_query_grpc
from pyinjective.proto.cosmos.base.tendermint.v1beta1 import query_pb2_grpc as tendermint_query_grpc
from pyinjective.proto.cosmos.crypto.ed25519 import keys_pb2 as ed25519_keys  # noqa: F401 for validator set responses
from pyinjective.proto.cosmos.tx.v1beta1 import service_pb2 as tx_service, service_pb2_grpc as tx_service_grpc
from pyinjective.proto.ibc.lightclients.tendermint.v1 import (  # noqa: F401 for validator set responses
    tendermint_pb2 as ibc_tendermint,
)
from pyinjective.proto.injective.stream.v2 import query_pb2 as chain_stream_v2_query
from pyinjective.proto.injective.types.v1beta1 import account_pb2
from pyinjective.utils.logger import LoggerProvider

DEFAULT_TIMEOUTHEIGHT_SYNC_INTERVAL = 20  # seconds
DEFAULT_TIMEOUTHEIGHT = 30  # blocks
DEFAULT_SESSION_RENEWAL_OFFSET = 120  # seconds
DEFAULT_BLOCK_TIME = 2  # seconds


class AsyncClient:
    def __init__(
        self,
        network: Network,
    ):
        self.addr = ""
        self.number = 0
        self.sequence = 0

        self.network = network

        # chain stubs
        self.chain_channel = self.network.create_chain_grpc_channel()

        self.stubCosmosTendermint = tendermint_query_grpc.ServiceStub(self.chain_channel)
        self.stubAuth = auth_query_grpc.QueryStub(self.chain_channel)
        self.stubAuthz = authz_query_grpc.QueryStub(self.chain_channel)
        self.stubBank = bank_query_grpc.QueryStub(self.chain_channel)
        self.stubTx = tx_service_grpc.ServiceStub(self.chain_channel)

        self.timeout_height = 1

        # exchange stubs
        self.exchange_channel = self.network.create_exchange_grpc_channel()
        # explorer stubs
        self.explorer_channel = self.network.create_explorer_grpc_channel()
        self.chain_stream_channel = self.network.create_chain_stream_grpc_channel()

        self._timeout_height_sync_task = None
        self._initialize_timeout_height_sync_task()

        self._tokens_and_markets_initialization_lock = asyncio.Lock()
        self._tokens_by_denom = dict()
        self._tokens_by_symbol = dict()
        self._spot_markets: Optional[Dict[str, SpotMarket]] = None
        self._derivative_markets: Optional[Dict[str, DerivativeMarket]] = None
        self._binary_option_markets: Optional[Dict[str, BinaryOptionMarket]] = None

        self.bank_api = ChainGrpcBankApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.auth_api = ChainGrpcAuthApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.authz_api = ChainGrpcAuthZApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.distribution_api = ChainGrpcDistributionApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.chain_erc20_api = ChainGrpcERC20Api(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.chain_evm_api = ChainGrpcEVMApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.chain_exchange_v2_api = ChainGrpcExchangeV2Api(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.ibc_channel_api = IBCChannelGrpcApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.ibc_client_api = IBCClientGrpcApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.ibc_connection_api = IBCConnectionGrpcApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.ibc_transfer_api = IBCTransferGrpcApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.permissions_api = ChainGrpcPermissionsApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.tendermint_api = TendermintGrpcApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.token_factory_api = ChainGrpcTokenFactoryApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.tx_api = TxGrpcApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.txfees_api = ChainGrpcTxfeesApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )
        self.wasm_api = ChainGrpcWasmApi(
            channel=self.chain_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )

        self.chain_stream_api = ChainGrpcChainStream(
            channel=self.chain_stream_channel,
            cookie_assistant=network.chain_cookie_assistant,
        )

    def __del__(self):
        self._cancel_timeout_height_sync_task()

    async def close_chain_channel(self):
        await self.chain_channel.close()
        self._cancel_timeout_height_sync_task()

    async def close_chain_stream_channel(self):
        await self.chain_stream_channel.close()
        self._cancel_timeout_height_sync_task()

    async def all_tokens(self) -> Dict[str, Token]:
        if self._tokens_by_symbol is None:
            async with self._tokens_and_markets_initialization_lock:
                if self._tokens_by_symbol is None:
                    await self._initialize_tokens_and_markets()
        return deepcopy(self._tokens_by_symbol)

    async def all_spot_markets(self) -> Dict[str, SpotMarket]:
        if self._spot_markets is None:
            async with self._tokens_and_markets_initialization_lock:
                if self._spot_markets is None:
                    await self._initialize_tokens_and_markets()
        return deepcopy(self._spot_markets)

    async def all_derivative_markets(self) -> Dict[str, DerivativeMarket]:
        if self._derivative_markets is None:
            async with self._tokens_and_markets_initialization_lock:
                if self._derivative_markets is None:
                    await self._initialize_tokens_and_markets()
        return deepcopy(self._derivative_markets)

    async def all_binary_option_markets(self) -> Dict[str, BinaryOptionMarket]:
        if self._binary_option_markets is None:
            async with self._tokens_and_markets_initialization_lock:
                if self._binary_option_markets is None:
                    await self._initialize_tokens_and_markets()
        return deepcopy(self._binary_option_markets)

    def get_sequence(self):
        current_seq = self.sequence
        self.sequence += 1
        return current_seq

    def get_number(self):
        return self.number

    async def fetch_tx(self, hash: str) -> Dict[str, Any]:
        return await self.tx_api.fetch_tx(hash=hash)

    async def sync_timeout_height(self):
        try:
            block = await self.fetch_latest_block()
            self.timeout_height = int(block["block"]["header"]["height"]) + DEFAULT_TIMEOUTHEIGHT
        except Exception as e:
            LoggerProvider().logger_for_class(logging_class=self.__class__).debug(
                f"error while fetching latest block, setting timeout height to 0: {e}"
            )
            self.timeout_height = 0

    # default client methods

    async def fetch_account(self, address: str) -> Optional[account_pb2.EthAccount]:
        result_account = None
        try:
            account = await self.auth_api.fetch_account(address=address)
            parsed_account = account_pb2.EthAccount()
            if parsed_account.DESCRIPTOR.full_name in account["account"]["@type"]:
                json_format.ParseDict(js_dict=account["account"], message=parsed_account, ignore_unknown_fields=True)
                self.number = parsed_account.base_account.account_number
                self.sequence = parsed_account.base_account.sequence
                result_account = parsed_account
        except Exception as e:
            LoggerProvider().logger_for_class(logging_class=self.__class__).debug(
                f"error while fetching sequence and number {e}"
            )

        return result_account

    async def get_request_id_by_tx_hash(self, tx_hash: str) -> List[int]:
        tx = await self.tx_api.fetch_tx(hash=tx_hash)
        request_ids = []
        for log in tx["txResponse"].get("logs", []):
            request_event = [
                event for event in log.get("events", []) if event["type"] == "request" or event["type"] == "report"
            ]
            if len(request_event) == 1:
                attrs = request_event[0].get("attributes", [])
                attr_id = [attr for attr in attrs if attr["key"] == "id"]
                if len(attr_id) == 1:
                    request_id = attr_id[0]["value"]
                    request_ids.append(int(request_id))
        if len(request_ids) == 0:
            raise NotFoundError("Request Id is not found")
        return request_ids

    async def simulate(self, tx_bytes: bytes) -> Dict[str, Any]:
        return await self.tx_api.simulate(tx_bytes=tx_bytes)

    async def broadcast_tx_sync_mode(self, tx_bytes: bytes) -> Dict[str, Any]:
        return await self.tx_api.broadcast(tx_bytes=tx_bytes, mode=tx_service.BroadcastMode.BROADCAST_MODE_SYNC)

    async def broadcast_tx_async_mode(self, tx_bytes: bytes) -> Dict[str, Any]:
        return await self.tx_api.broadcast(tx_bytes=tx_bytes, mode=tx_service.BroadcastMode.BROADCAST_MODE_ASYNC)

    async def get_chain_id(self) -> str:
        latest_block = await self.fetch_latest_block()
        return latest_block["block"]["header"]["chainId"]

    async def fetch_grants(
        self,
        granter: str,
        grantee: str,
        msg_type_url: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.authz_api.fetch_grants(
            granter=granter,
            grantee=grantee,
            msg_type_url=msg_type_url,
            pagination=pagination,
        )

    async def fetch_bank_balances(self, address: str) -> Dict[str, Any]:
        return await self.bank_api.fetch_balances(account_address=address)

    async def fetch_bank_balance(self, address: str, denom: str) -> Dict[str, Any]:
        return await self.bank_api.fetch_balance(account_address=address, denom=denom)

    async def fetch_spendable_balances(
        self,
        address: str,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.bank_api.fetch_spendable_balances(account_address=address, pagination=pagination)

    async def fetch_spendable_balances_by_denom(
        self,
        address: str,
        denom: str,
    ) -> Dict[str, Any]:
        return await self.bank_api.fetch_spendable_balances_by_denom(account_address=address, denom=denom)

    async def fetch_total_supply(self, pagination: Optional[PaginationOption] = None) -> Dict[str, Any]:
        return await self.bank_api.fetch_total_supply(pagination=pagination)

    async def fetch_supply_of(self, denom: str) -> Dict[str, Any]:
        return await self.bank_api.fetch_supply_of(denom=denom)

    async def fetch_denom_metadata(self, denom: str) -> Dict[str, Any]:
        return await self.bank_api.fetch_denom_metadata(denom=denom)

    async def fetch_denoms_metadata(self, pagination: Optional[PaginationOption] = None) -> Dict[str, Any]:
        return await self.bank_api.fetch_denoms_metadata(pagination=pagination)

    async def fetch_denom_owners(self, denom: str, pagination: Optional[PaginationOption] = None) -> Dict[str, Any]:
        return await self.bank_api.fetch_denom_owners(denom=denom, pagination=pagination)

    async def fetch_send_enabled(
        self,
        denoms: Optional[List[str]] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.bank_api.fetch_send_enabled(denoms=denoms, pagination=pagination)

    async def fetch_validator_distribution_info(self, validator_address: str) -> Dict[str, Any]:
        return await self.distribution_api.fetch_validator_distribution_info(validator_address=validator_address)

    async def fetch_validator_outstanding_rewards(self, validator_address: str) -> Dict[str, Any]:
        return await self.distribution_api.fetch_validator_outstanding_rewards(validator_address=validator_address)

    async def fetch_validator_commission(self, validator_address: str) -> Dict[str, Any]:
        return await self.distribution_api.fetch_validator_commission(validator_address=validator_address)

    async def fetch_validator_slashes(
        self,
        validator_address: str,
        starting_height: Optional[int] = None,
        ending_height: Optional[int] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.distribution_api.fetch_validator_slashes(
            validator_address=validator_address,
            starting_height=starting_height,
            ending_height=ending_height,
            pagination=pagination,
        )

    async def fetch_delegation_rewards(
        self,
        delegator_address: str,
        validator_address: str,
    ) -> Dict[str, Any]:
        return await self.distribution_api.fetch_delegation_rewards(
            delegator_address=delegator_address,
            validator_address=validator_address,
        )

    async def fetch_delegation_total_rewards(
        self,
        delegator_address: str,
    ) -> Dict[str, Any]:
        return await self.distribution_api.fetch_delegation_total_rewards(
            delegator_address=delegator_address,
        )

    async def fetch_delegator_validators(
        self,
        delegator_address: str,
    ) -> Dict[str, Any]:
        return await self.distribution_api.fetch_delegator_validators(
            delegator_address=delegator_address,
        )

    async def fetch_delegator_withdraw_address(
        self,
        delegator_address: str,
    ) -> Dict[str, Any]:
        return await self.distribution_api.fetch_delegator_withdraw_address(
            delegator_address=delegator_address,
        )

    async def fetch_community_pool(self) -> Dict[str, Any]:
        return await self.distribution_api.fetch_community_pool()

    # Exchange module

    async def fetch_subaccount_deposits(
        self,
        subaccount_id: Optional[str] = None,
        subaccount_trader: Optional[str] = None,
        subaccount_nonce: Optional[int] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_subaccount_deposits(
            subaccount_id=subaccount_id,
            subaccount_trader=subaccount_trader,
            subaccount_nonce=subaccount_nonce,
        )

    async def fetch_subaccount_deposit(
        self,
        subaccount_id: str,
        denom: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_subaccount_deposit(
            subaccount_id=subaccount_id,
            denom=denom,
        )

    async def fetch_exchange_balances(self) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_exchange_balances()

    async def fetch_denom_decimal(self, denom: str) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_denom_decimal(denom=denom)

    async def fetch_denom_decimals(self, denoms: Optional[List[str]] = None) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_denom_decimals(denoms=denoms)

    async def fetch_derivative_market_address(self, market_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_derivative_market_address(market_id=market_id)

    async def fetch_subaccount_trade_nonce(self, subaccount_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_subaccount_trade_nonce(subaccount_id=subaccount_id)

    async def fetch_chain_perpetual_market_info(self, market_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_perpetual_market_info(market_id=market_id)

    async def fetch_trade_reward_points(
        self,
        accounts: Optional[List[str]] = None,
        pending_pool_timestamp: Optional[int] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_trade_reward_points(
            accounts=accounts,
            pending_pool_timestamp=pending_pool_timestamp,
        )

    async def fetch_pending_trade_reward_points(
        self,
        accounts: Optional[List[str]] = None,
        pending_pool_timestamp: Optional[int] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_pending_trade_reward_points(
            accounts=accounts,
            pending_pool_timestamp=pending_pool_timestamp,
        )

    async def fetch_trade_reward_campaign(self) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_trade_reward_campaign()

    async def fetch_balance_mismatches(self, dust_factor: int) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_balance_mismatches(dust_factor=dust_factor)

    async def fetch_balance_with_balance_holds(self) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_balance_with_balance_holds()

    async def fetch_fee_discount_tier_statistics(self) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_fee_discount_tier_statistics()

    async def fetch_mito_vault_infos(self) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_mito_vault_infos()

    async def fetch_market_id_from_vault(self, vault_address: str) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_market_id_from_vault(vault_address=vault_address)

    async def fetch_is_opted_out_of_rewards(self, account: str) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_is_opted_out_of_rewards(account=account)

    async def fetch_opted_out_of_rewards_accounts(self) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_opted_out_of_rewards_accounts()

    async def fetch_market_atomic_execution_fee_multiplier(
        self,
        market_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_market_atomic_execution_fee_multiplier(
            market_id=market_id,
        )

    async def fetch_active_stake_grant(self, grantee: str) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_active_stake_grant(grantee=grantee)

    async def fetch_grant_authorization(
        self,
        granter: str,
        grantee: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_grant_authorization(
            granter=granter,
            grantee=grantee,
        )

    async def fetch_grant_authorizations(self, granter: str) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_grant_authorizations(granter=granter)

    async def fetch_market_balance(self, market_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_market_balance(market_id=market_id)

    async def fetch_market_balances(self) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_market_balances()

    async def fetch_aggregate_volume(self, account: str) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_aggregate_volume(account=account)

    async def fetch_aggregate_volumes(
        self,
        accounts: Optional[List[str]] = None,
        market_ids: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_aggregate_volumes(
            accounts=accounts,
            market_ids=market_ids,
        )

    async def fetch_aggregate_market_volume(
        self,
        market_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_aggregate_market_volume(
            market_id=market_id,
        )

    async def fetch_aggregate_market_volumes(
        self,
        market_ids: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_aggregate_market_volumes(
            market_ids=market_ids,
        )

    async def fetch_chain_spot_markets(
        self,
        status: Optional[str] = None,
        market_ids: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_spot_markets(
            status=status,
            market_ids=market_ids,
        )

    async def fetch_chain_spot_market(
        self,
        market_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_spot_market(
            market_id=market_id,
        )

    async def fetch_chain_full_spot_markets(
        self,
        status: Optional[str] = None,
        market_ids: Optional[List[str]] = None,
        with_mid_price_and_tob: Optional[bool] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_full_spot_markets(
            status=status,
            market_ids=market_ids,
            with_mid_price_and_tob=with_mid_price_and_tob,
        )

    async def fetch_chain_full_spot_market(
        self,
        market_id: str,
        with_mid_price_and_tob: Optional[bool] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_full_spot_market(
            market_id=market_id,
            with_mid_price_and_tob=with_mid_price_and_tob,
        )

    async def fetch_chain_spot_orderbook(
        self,
        market_id: str,
        order_side: Optional[str] = None,
        limit_cumulative_notional: Optional[str] = None,
        limit_cumulative_quantity: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        # Order side could be "Side_Unspecified", "Buy", "Sell"
        return await self.chain_exchange_v2_api.fetch_spot_orderbook(
            market_id=market_id,
            order_side=order_side,
            limit_cumulative_notional=limit_cumulative_notional,
            limit_cumulative_quantity=limit_cumulative_quantity,
            pagination=pagination,
        )

    async def fetch_chain_trader_spot_orders(
        self,
        market_id: str,
        subaccount_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_trader_spot_orders(
            market_id=market_id,
            subaccount_id=subaccount_id,
        )

    async def fetch_chain_account_address_spot_orders(
        self,
        market_id: str,
        account_address: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_account_address_spot_orders(
            market_id=market_id,
            account_address=account_address,
        )

    async def fetch_chain_spot_orders_by_hashes(
        self,
        market_id: str,
        subaccount_id: str,
        order_hashes: List[str],
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_spot_orders_by_hashes(
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hashes=order_hashes,
        )

    async def fetch_chain_subaccount_orders(
        self,
        subaccount_id: str,
        market_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_subaccount_orders(
            subaccount_id=subaccount_id,
            market_id=market_id,
        )

    async def fetch_chain_trader_spot_transient_orders(
        self,
        market_id: str,
        subaccount_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_trader_spot_transient_orders(
            market_id=market_id,
            subaccount_id=subaccount_id,
        )

    async def fetch_spot_mid_price_and_tob(
        self,
        market_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_spot_mid_price_and_tob(
            market_id=market_id,
        )

    async def fetch_derivative_mid_price_and_tob(
        self,
        market_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_derivative_mid_price_and_tob(
            market_id=market_id,
        )

    async def fetch_chain_derivative_orderbook(
        self,
        market_id: str,
        limit_cumulative_notional: Optional[str] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_derivative_orderbook(
            market_id=market_id,
            limit_cumulative_notional=limit_cumulative_notional,
            pagination=pagination,
        )

    async def fetch_chain_trader_derivative_orders(
        self,
        market_id: str,
        subaccount_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_trader_derivative_orders(
            market_id=market_id,
            subaccount_id=subaccount_id,
        )

    async def fetch_chain_account_address_derivative_orders(
        self,
        market_id: str,
        account_address: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_account_address_derivative_orders(
            market_id=market_id,
            account_address=account_address,
        )

    async def fetch_chain_derivative_orders_by_hashes(
        self,
        market_id: str,
        subaccount_id: str,
        order_hashes: List[str],
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_derivative_orders_by_hashes(
            market_id=market_id,
            subaccount_id=subaccount_id,
            order_hashes=order_hashes,
        )

    async def fetch_chain_trader_derivative_transient_orders(
        self,
        market_id: str,
        subaccount_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_trader_derivative_transient_orders(
            market_id=market_id,
            subaccount_id=subaccount_id,
        )

    async def fetch_chain_derivative_markets(
        self,
        status: Optional[str] = None,
        market_ids: Optional[List[str]] = None,
        with_mid_price_and_tob: Optional[bool] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_derivative_markets(
            status=status,
            market_ids=market_ids,
            with_mid_price_and_tob=with_mid_price_and_tob,
        )

    async def fetch_chain_derivative_market(
        self,
        market_id: str,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_derivative_market(
            market_id=market_id,
        )

    async def fetch_chain_positions(self) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_positions()

    async def fetch_chain_positions_in_market(self, market_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_positions_in_market(market_id=market_id)

    async def fetch_chain_subaccount_positions(self, subaccount_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_subaccount_positions(subaccount_id=subaccount_id)

    async def fetch_chain_subaccount_position_in_market(self, subaccount_id: str, market_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_subaccount_position_in_market(
            subaccount_id=subaccount_id,
            market_id=market_id,
        )

    async def fetch_chain_subaccount_effective_position_in_market(
        self, subaccount_id: str, market_id: str
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_subaccount_effective_position_in_market(
            subaccount_id=subaccount_id,
            market_id=market_id,
        )

    async def fetch_chain_expiry_futures_market_info(self, market_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_expiry_futures_market_info(market_id=market_id)

    async def fetch_chain_perpetual_market_funding(self, market_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_perpetual_market_funding(market_id=market_id)

    async def fetch_subaccount_order_metadata(self, subaccount_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_subaccount_order_metadata(subaccount_id=subaccount_id)

    async def fetch_fee_discount_account_info(self, account: str) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_fee_discount_account_info(account=account)

    async def fetch_fee_discount_schedule(self) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_fee_discount_schedule()

    async def fetch_historical_trade_records(self, market_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_historical_trade_records(market_id=market_id)

    async def fetch_market_volatility(
        self,
        market_id: str,
        trade_grouping_sec: Optional[int] = None,
        max_age: Optional[int] = None,
        include_raw_history: Optional[bool] = None,
        include_metadata: Optional[bool] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_market_volatility(
            market_id=market_id,
            trade_grouping_sec=trade_grouping_sec,
            max_age=max_age,
            include_raw_history=include_raw_history,
            include_metadata=include_metadata,
        )

    async def fetch_chain_binary_options_markets(self, status: Optional[str] = None) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_binary_options_markets(status=status)

    async def fetch_trader_derivative_conditional_orders(
        self,
        subaccount_id: Optional[str] = None,
        market_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_trader_derivative_conditional_orders(
            subaccount_id=subaccount_id,
            market_id=market_id,
        )

    async def fetch_l3_derivative_orderbook(self, market_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_l3_derivative_orderbook(market_id=market_id)

    async def fetch_l3_spot_orderbook(self, market_id: str) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_l3_spot_orderbook(market_id=market_id)

    async def fetch_denom_min_notional(self, denom: str) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_denom_min_notional(denom=denom)

    async def fetch_denom_min_notionals(self) -> Dict[str, Any]:
        return await self.chain_exchange_v2_api.fetch_denom_min_notionals()

    # Wasm module
    async def fetch_contract_info(self, address: str) -> Dict[str, Any]:
        return await self.wasm_api.fetch_contract_info(address=address)

    async def fetch_contract_history(
        self,
        address: str,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.wasm_api.fetch_contract_history(
            address=address,
            pagination=pagination,
        )

    async def fetch_contracts_by_code(
        self,
        code_id: int,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.wasm_api.fetch_contracts_by_code(
            code_id=code_id,
            pagination=pagination,
        )

    async def fetch_all_contracts_state(
        self,
        address: str,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.wasm_api.fetch_all_contracts_state(
            address=address,
            pagination=pagination,
        )

    async def fetch_raw_contract_state(self, address: str, query_data: str) -> Dict[str, Any]:
        return await self.wasm_api.fetch_raw_contract_state(address=address, query_data=query_data)

    async def fetch_smart_contract_state(self, address: str, query_data: str) -> Dict[str, Any]:
        return await self.wasm_api.fetch_smart_contract_state(address=address, query_data=query_data)

    async def fetch_code(self, code_id: int) -> Dict[str, Any]:
        return await self.wasm_api.fetch_code(code_id=code_id)

    async def fetch_codes(
        self,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.wasm_api.fetch_codes(
            pagination=pagination,
        )

    async def fetch_pinned_codes(
        self,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.wasm_api.fetch_pinned_codes(
            pagination=pagination,
        )

    async def fetch_contracts_by_creator(
        self,
        creator_address: str,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.wasm_api.fetch_contracts_by_creator(
            creator_address=creator_address,
            pagination=pagination,
        )

    # Token Factory module

    async def fetch_denom_authority_metadata(
        self,
        creator: str,
        sub_denom: Optional[str] = None,
    ) -> Dict[str, Any]:
        return await self.token_factory_api.fetch_denom_authority_metadata(creator=creator, sub_denom=sub_denom)

    async def fetch_denoms_from_creator(
        self,
        creator: str,
    ) -> Dict[str, Any]:
        return await self.token_factory_api.fetch_denoms_from_creator(creator=creator)

    async def fetch_tokenfactory_module_state(self) -> Dict[str, Any]:
        return await self.token_factory_api.fetch_tokenfactory_module_state()

    # ------------------------------
    # region Tendermint module
    async def fetch_node_info(self) -> Dict[str, Any]:
        return await self.tendermint_api.fetch_node_info()

    async def fetch_syncing(self) -> Dict[str, Any]:
        return await self.tendermint_api.fetch_syncing()

    async def fetch_latest_block(self) -> Dict[str, Any]:
        return await self.tendermint_api.fetch_latest_block()

    async def fetch_block_by_height(self, height: int) -> Dict[str, Any]:
        return await self.tendermint_api.fetch_block_by_height(height=height)

    async def fetch_latest_validator_set(self) -> Dict[str, Any]:
        return await self.tendermint_api.fetch_latest_validator_set()

    async def fetch_validator_set_by_height(
        self, height: int, pagination: Optional[PaginationOption] = None
    ) -> Dict[str, Any]:
        return await self.tendermint_api.fetch_validator_set_by_height(height=height, pagination=pagination)

    async def abci_query(
        self, path: str, data: Optional[bytes] = None, height: Optional[int] = None, prove: bool = False
    ) -> Dict[str, Any]:
        return await self.tendermint_api.abci_query(path=path, data=data, height=height, prove=prove)

    # endregion

    async def listen_chain_stream_updates(
        self,
        callback: Callable,
        on_end_callback: Optional[Callable] = None,
        on_status_callback: Optional[Callable] = None,
        bank_balances_filter: Optional[chain_stream_v2_query.BankBalancesFilter] = None,
        subaccount_deposits_filter: Optional[chain_stream_v2_query.SubaccountDepositsFilter] = None,
        spot_trades_filter: Optional[chain_stream_v2_query.TradesFilter] = None,
        derivative_trades_filter: Optional[chain_stream_v2_query.TradesFilter] = None,
        spot_orders_filter: Optional[chain_stream_v2_query.OrdersFilter] = None,
        derivative_orders_filter: Optional[chain_stream_v2_query.OrdersFilter] = None,
        spot_orderbooks_filter: Optional[chain_stream_v2_query.OrderbookFilter] = None,
        derivative_orderbooks_filter: Optional[chain_stream_v2_query.OrderbookFilter] = None,
        positions_filter: Optional[chain_stream_v2_query.PositionsFilter] = None,
        oracle_price_filter: Optional[chain_stream_v2_query.OraclePriceFilter] = None,
    ):
        return await self.chain_stream_api.stream_v2(
            callback=callback,
            on_end_callback=on_end_callback,
            on_status_callback=on_status_callback,
            bank_balances_filter=bank_balances_filter,
            subaccount_deposits_filter=subaccount_deposits_filter,
            spot_trades_filter=spot_trades_filter,
            derivative_trades_filter=derivative_trades_filter,
            spot_orders_filter=spot_orders_filter,
            derivative_orders_filter=derivative_orders_filter,
            spot_orderbooks_filter=spot_orderbooks_filter,
            derivative_orderbooks_filter=derivative_orderbooks_filter,
            positions_filter=positions_filter,
            oracle_price_filter=oracle_price_filter,
        )

    # region IBC Transfer module
    async def fetch_denom_trace(self, hash: str) -> Dict[str, Any]:
        return await self.ibc_transfer_api.fetch_denom_trace(hash=hash)

    async def fetch_denom_traces(self, pagination: Optional[PaginationOption] = None) -> Dict[str, Any]:
        return await self.ibc_transfer_api.fetch_denom_traces(pagination=pagination)

    async def fetch_denom_hash(self, trace: str) -> Dict[str, Any]:
        return await self.ibc_transfer_api.fetch_denom_hash(trace=trace)

    async def fetch_escrow_address(self, port_id: str, channel_id: str) -> Dict[str, Any]:
        return await self.ibc_transfer_api.fetch_escrow_address(port_id=port_id, channel_id=channel_id)

    async def fetch_total_escrow_for_denom(self, denom: str) -> Dict[str, Any]:
        return await self.ibc_transfer_api.fetch_total_escrow_for_denom(denom=denom)

    # endregion

    # region IBC Channel module
    async def fetch_ibc_channel(self, port_id: str, channel_id: str) -> Dict[str, Any]:
        return await self.ibc_channel_api.fetch_channel(port_id=port_id, channel_id=channel_id)

    async def fetch_ibc_channels(self, pagination: Optional[PaginationOption] = None) -> Dict[str, Any]:
        return await self.ibc_channel_api.fetch_channels(pagination=pagination)

    async def fetch_ibc_connection_channels(
        self, connection: str, pagination: Optional[PaginationOption] = None
    ) -> Dict[str, Any]:
        return await self.ibc_channel_api.fetch_connection_channels(connection=connection, pagination=pagination)

    async def fetch_ibc_channel_client_state(self, port_id: str, channel_id: str) -> Dict[str, Any]:
        return await self.ibc_channel_api.fetch_channel_client_state(port_id=port_id, channel_id=channel_id)

    async def fetch_ibc_channel_consensus_state(
        self,
        port_id: str,
        channel_id: str,
        revision_number: int,
        revision_height: int,
    ) -> Dict[str, Any]:
        return await self.ibc_channel_api.fetch_channel_consensus_state(
            port_id=port_id,
            channel_id=channel_id,
            revision_number=revision_number,
            revision_height=revision_height,
        )

    async def fetch_ibc_packet_commitment(self, port_id: str, channel_id: str, sequence: int) -> Dict[str, Any]:
        return await self.ibc_channel_api.fetch_packet_commitment(
            port_id=port_id, channel_id=channel_id, sequence=sequence
        )

    async def fetch_ibc_packet_commitments(
        self, port_id: str, channel_id: str, pagination: Optional[PaginationOption] = None
    ) -> Dict[str, Any]:
        return await self.ibc_channel_api.fetch_packet_commitments(
            port_id=port_id, channel_id=channel_id, pagination=pagination
        )

    async def fetch_ibc_packet_receipt(self, port_id: str, channel_id: str, sequence: int) -> Dict[str, Any]:
        return await self.ibc_channel_api.fetch_packet_receipt(
            port_id=port_id, channel_id=channel_id, sequence=sequence
        )

    async def fetch_ibc_packet_acknowledgement(self, port_id: str, channel_id: str, sequence: int) -> Dict[str, Any]:
        return await self.ibc_channel_api.fetch_packet_acknowledgement(
            port_id=port_id, channel_id=channel_id, sequence=sequence
        )

    async def fetch_ibc_packet_acknowledgements(
        self,
        port_id: str,
        channel_id: str,
        packet_commitment_sequences: Optional[List[int]] = None,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.ibc_channel_api.fetch_packet_acknowledgements(
            port_id=port_id,
            channel_id=channel_id,
            packet_commitment_sequences=packet_commitment_sequences,
            pagination=pagination,
        )

    async def fetch_ibc_unreceived_packets(
        self, port_id: str, channel_id: str, packet_commitment_sequences: Optional[List[int]] = None
    ) -> Dict[str, Any]:
        return await self.ibc_channel_api.fetch_unreceived_packets(
            port_id=port_id, channel_id=channel_id, packet_commitment_sequences=packet_commitment_sequences
        )

    async def fetch_ibc_unreceived_acks(
        self, port_id: str, channel_id: str, packet_ack_sequences: Optional[List[int]] = None
    ) -> Dict[str, Any]:
        return await self.ibc_channel_api.fetch_unreceived_acks(
            port_id=port_id, channel_id=channel_id, packet_ack_sequences=packet_ack_sequences
        )

    async def fetch_next_sequence_receive(self, port_id: str, channel_id: str) -> Dict[str, Any]:
        return await self.ibc_channel_api.fetch_next_sequence_receive(port_id=port_id, channel_id=channel_id)

    # endregion

    # region IBC Client module
    async def fetch_ibc_client_state(self, client_id: str) -> Dict[str, Any]:
        return await self.ibc_client_api.fetch_client_state(client_id=client_id)

    async def fetch_ibc_client_states(self, pagination: Optional[PaginationOption] = None) -> Dict[str, Any]:
        return await self.ibc_client_api.fetch_client_states(pagination=pagination)

    async def fetch_ibc_consensus_state(
        self,
        client_id: str,
        revision_number: int,
        revision_height: int,
        latest_height: Optional[bool] = None,
    ) -> Dict[str, Any]:
        return await self.ibc_client_api.fetch_consensus_state(
            client_id=client_id,
            revision_number=revision_number,
            revision_height=revision_height,
            latest_height=latest_height,
        )

    async def fetch_ibc_consensus_states(
        self,
        client_id: str,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.ibc_client_api.fetch_consensus_states(client_id=client_id, pagination=pagination)

    async def fetch_ibc_consensus_state_heights(
        self,
        client_id: str,
        pagination: Optional[PaginationOption] = None,
    ) -> Dict[str, Any]:
        return await self.ibc_client_api.fetch_consensus_state_heights(client_id=client_id, pagination=pagination)

    async def fetch_ibc_client_status(self, client_id: str) -> Dict[str, Any]:
        return await self.ibc_client_api.fetch_client_status(client_id=client_id)

    async def fetch_ibc_client_params(self) -> Dict[str, Any]:
        return await self.ibc_client_api.fetch_client_params()

    async def fetch_ibc_upgraded_client_state(self) -> Dict[str, Any]:
        return await self.ibc_client_api.fetch_upgraded_client_state()

    async def fetch_ibc_upgraded_consensus_state(self) -> Dict[str, Any]:
        return await self.ibc_client_api.fetch_upgraded_consensus_state()

    # endregion

    # region IBC Connection module
    async def fetch_ibc_connection(self, connection_id: str) -> Dict[str, Any]:
        return await self.ibc_connection_api.fetch_connection(connection_id=connection_id)

    async def fetch_ibc_connections(self, pagination: Optional[PaginationOption] = None) -> Dict[str, Any]:
        return await self.ibc_connection_api.fetch_connections(pagination=pagination)

    async def fetch_ibc_client_connections(self, client_id: str) -> Dict[str, Any]:
        return await self.ibc_connection_api.fetch_client_connections(client_id=client_id)

    async def fetch_ibc_connection_client_state(self, connection_id: str) -> Dict[str, Any]:
        return await self.ibc_connection_api.fetch_connection_client_state(connection_id=connection_id)

    async def fetch_ibc_connection_consensus_state(
        self,
        connection_id: str,
        revision_number: int,
        revision_height: int,
    ) -> Dict[str, Any]:
        return await self.ibc_connection_api.fetch_connection_consensus_state(
            connection_id=connection_id, revision_number=revision_number, revision_height=revision_height
        )

    async def fetch_ibc_connection_params(self) -> Dict[str, Any]:
        return await self.ibc_connection_api.fetch_connection_params()

    # endregion

    # ------------------------------
    # region Permissions module

    async def fetch_permissions_namespace_denoms(self) -> Dict[str, Any]:
        return await self.permissions_api.fetch_namespace_denoms()

    async def fetch_permissions_namespaces(self) -> Dict[str, Any]:
        return await self.permissions_api.fetch_namespaces()

    async def fetch_permissions_namespace(self, denom: str) -> Dict[str, Any]:
        return await self.permissions_api.fetch_namespace(denom=denom)

    async def fetch_permissions_roles_by_actor(self, denom: str, actor: str) -> Dict[str, Any]:
        return await self.permissions_api.fetch_roles_by_actor(denom=denom, actor=actor)

    async def fetch_permissions_actors_by_role(self, denom: str, role: str) -> Dict[str, Any]:
        return await self.permissions_api.fetch_actors_by_role(denom=denom, role=role)

    async def fetch_permissions_role_managers(self, denom: str) -> Dict[str, Any]:
        return await self.permissions_api.fetch_role_managers(denom=denom)

    async def fetch_permissions_role_manager(self, denom: str, manager: str) -> Dict[str, Any]:
        return await self.permissions_api.fetch_role_manager(denom=denom, manager=manager)

    async def fetch_permissions_policy_statuses(self, denom: str) -> Dict[str, Any]:
        return await self.permissions_api.fetch_policy_statuses(denom=denom)

    async def fetch_permissions_policy_manager_capabilities(self, denom: str) -> Dict[str, Any]:
        return await self.permissions_api.fetch_policy_manager_capabilities(denom=denom)

    async def fetch_permissions_vouchers(self, denom: str) -> Dict[str, Any]:
        return await self.permissions_api.fetch_vouchers(denom=denom)

    async def fetch_permissions_voucher(self, denom: str, address: str) -> Dict[str, Any]:
        return await self.permissions_api.fetch_voucher(denom=denom, address=address)

    async def fetch_permissions_module_state(self) -> Dict[str, Any]:
        return await self.permissions_api.fetch_permissions_module_state()

    # endregion

    # -------------------------
    # region IBC Channel module
    async def fetch_eip_base_fee(self) -> Dict[str, Any]:
        return await self.txfees_api.fetch_eip_base_fee()

    # endregion

    # -------------------------
    # region Chain ERC20 module
    async def fetch_erc20_all_token_pairs(self, pagination: Optional[PaginationOption] = None) -> Dict[str, Any]:
        return await self.chain_erc20_api.fetch_all_token_pairs(pagination=pagination)

    async def fetch_erc20_token_pair_by_denom(self, bank_denom: str) -> Dict[str, Any]:
        return await self.chain_erc20_api.fetch_token_pair_by_denom(bank_denom=bank_denom)

    async def fetch_erc20_token_pair_by_erc20_address(self, erc20_address: str) -> Dict[str, Any]:
        return await self.chain_erc20_api.fetch_token_pair_by_erc20_address(erc20_address=erc20_address)

    # endregion

    # -------------------------
    # region Chain EVM module
    async def fetch_evm_account(self, address: str) -> Dict[str, Any]:
        return await self.chain_evm_api.fetch_account(address=address)

    async def fetch_evm_cosmos_account(self, address: str) -> Dict[str, Any]:
        return await self.chain_evm_api.fetch_cosmos_account(address=address)

    async def fetch_evm_validator_account(self, cons_address: str) -> Dict[str, Any]:
        return await self.chain_evm_api.fetch_validator_account(cons_address=cons_address)

    async def fetch_evm_balance(self, address: str) -> Dict[str, Any]:
        return await self.chain_evm_api.fetch_balance(address=address)

    async def fetch_evm_storage(self, address: str, key: Optional[str] = None) -> Dict[str, Any]:
        return await self.chain_evm_api.fetch_storage(address=address, key=key)

    async def fetch_evm_code(self, address: str) -> Dict[str, Any]:
        return await self.chain_evm_api.fetch_code(address=address)

    async def fetch_evm_base_fee(self) -> Dict[str, Any]:
        return await self.chain_evm_api.fetch_base_fee()

    # endregion

    async def composer(self):
        return Composer(
            network=self.network.string(),
        )

    async def current_chain_gas_price(self) -> int:
        gas_price = GAS_PRICE
        try:
            eip_base_fee_response = await self.fetch_eip_base_fee()
            gas_price = int(
                Token.convert_value_from_extended_decimal_format(Decimal(eip_base_fee_response["baseFee"]["baseFee"]))
            )
        except Exception as e:
            logger = LoggerProvider().logger_for_class(logging_class=self.__class__)
            logger.error("an error occurred when querying the gas price from the chain, using the default gas price")
            logger.debug(f"error querying the gas price from chain {e}")

        return gas_price

    async def initialize_tokens_from_chain_denoms(self):
        # force initialization of markets and tokens
        await self.all_tokens()

        all_denoms_metadata = []

        query_result = await self.fetch_denoms_metadata()

        all_denoms_metadata.extend(query_result.get("metadatas", []))
        next_key = query_result.get("pagination", {}).get("nextKey", "")

        while next_key != "":
            query_result = await self.fetch_denoms_metadata(pagination=PaginationOption(encoded_page_key=next_key))

            all_denoms_metadata.extend(query_result.get("metadatas", []))
            next_key = query_result.get("pagination", {}).get("nextKey", "")

        for token_metadata in all_denoms_metadata:
            symbol = token_metadata["symbol"]
            denom = token_metadata["base"]

            if denom != "" and symbol != "" and denom not in self._tokens_by_denom:
                name = token_metadata["name"] or symbol
                decimals = max({denom_unit["exponent"] for denom_unit in token_metadata["denomUnits"]})

                unique_symbol = denom
                for symbol_candidate in [symbol, name]:
                    if symbol_candidate not in self._tokens_by_symbol:
                        unique_symbol = symbol_candidate
                        break

                token = Token(
                    name=name,
                    symbol=symbol,
                    denom=denom,
                    address="",
                    decimals=decimals,
                    logo=token_metadata["uri"],
                    updated=-1,
                    unique_symbol=unique_symbol,
                )

                self._tokens_by_denom[denom] = token
                self._tokens_by_symbol[unique_symbol] = token

    async def _initialize_tokens_and_markets(self):
        spot_markets = dict()
        derivative_markets = dict()
        binary_option_markets = dict()
        tokens_by_symbol, tokens_by_denom = await self._tokens_from_official_lists(network=self.network)
        self._tokens_by_denom.update(tokens_by_denom)
        self._tokens_by_symbol.update(tokens_by_symbol)

        markets_info = (await self.fetch_chain_spot_markets(status="Active"))["markets"]
        for market_info in markets_info:
            base_token = self._tokens_by_denom.get(market_info["baseDenom"])
            quote_token = self._tokens_by_denom.get(market_info["quoteDenom"])

            market = SpotMarket(
                id=market_info["marketId"],
                status=market_info["status"],
                ticker=market_info["ticker"],
                base_token=base_token,
                quote_token=quote_token,
                maker_fee_rate=Token.convert_value_from_extended_decimal_format(Decimal(market_info["makerFeeRate"])),
                taker_fee_rate=Token.convert_value_from_extended_decimal_format(Decimal(market_info["takerFeeRate"])),
                service_provider_fee=Token.convert_value_from_extended_decimal_format(
                    Decimal(market_info["relayerFeeShareRate"])
                ),
                min_price_tick_size=Token.convert_value_from_extended_decimal_format(
                    Decimal(market_info["minPriceTickSize"])
                ),
                min_quantity_tick_size=Token.convert_value_from_extended_decimal_format(
                    Decimal(market_info["minQuantityTickSize"])
                ),
                min_notional=Token.convert_value_from_extended_decimal_format(Decimal(market_info["minNotional"])),
            )

            spot_markets[market.id] = market

        markets_info = (await self.fetch_chain_derivative_markets(status="Active", with_mid_price_and_tob=False))[
            "markets"
        ]
        for market_info in markets_info:
            market = market_info["market"]
            quote_token = self._tokens_by_denom.get(market["quoteDenom"])

            derivative_market = DerivativeMarket(
                id=market["marketId"],
                status=market["status"],
                ticker=market["ticker"],
                oracle_base=market["oracleBase"],
                oracle_quote=market["oracleQuote"],
                oracle_type=market["oracleType"],
                oracle_scale_factor=market["oracleScaleFactor"],
                initial_margin_ratio=Token.convert_value_from_extended_decimal_format(
                    Decimal(market["initialMarginRatio"])
                ),
                maintenance_margin_ratio=Token.convert_value_from_extended_decimal_format(
                    Decimal(market["maintenanceMarginRatio"])
                ),
                quote_token=quote_token,
                maker_fee_rate=Token.convert_value_from_extended_decimal_format(Decimal(market["makerFeeRate"])),
                taker_fee_rate=Token.convert_value_from_extended_decimal_format(Decimal(market["takerFeeRate"])),
                service_provider_fee=Token.convert_value_from_extended_decimal_format(
                    Decimal(market["relayerFeeShareRate"])
                ),
                min_price_tick_size=Token.convert_value_from_extended_decimal_format(
                    Decimal(market["minPriceTickSize"])
                ),
                min_quantity_tick_size=Token.convert_value_from_extended_decimal_format(
                    Decimal(market["minQuantityTickSize"])
                ),
                min_notional=Token.convert_value_from_extended_decimal_format(Decimal(market["minNotional"])),
            )

            derivative_markets[derivative_market.id] = derivative_market

        markets_info = (await self.fetch_chain_binary_options_markets(status="Active"))["markets"]
        for market_info in markets_info:
            quote_token = self._tokens_by_denom.get(market_info["quoteDenom"])

            market = BinaryOptionMarket(
                id=market_info["marketId"],
                status=market_info["status"],
                ticker=market_info["ticker"],
                oracle_symbol=market_info["oracleSymbol"],
                oracle_provider=market_info["oracleProvider"],
                oracle_type=market_info["oracleType"],
                oracle_scale_factor=market_info["oracleScaleFactor"],
                expiration_timestamp=market_info["expirationTimestamp"],
                settlement_timestamp=market_info["settlementTimestamp"],
                quote_token=quote_token,
                maker_fee_rate=Token.convert_value_from_extended_decimal_format(Decimal(market_info["makerFeeRate"])),
                taker_fee_rate=Token.convert_value_from_extended_decimal_format(Decimal(market_info["takerFeeRate"])),
                service_provider_fee=Token.convert_value_from_extended_decimal_format(
                    Decimal(market_info["relayerFeeShareRate"])
                ),
                min_price_tick_size=Token.convert_value_from_extended_decimal_format(
                    Decimal(market_info["minPriceTickSize"])
                ),
                min_quantity_tick_size=Token.convert_value_from_extended_decimal_format(
                    Decimal(market_info["minQuantityTickSize"])
                ),
                min_notional=Token.convert_value_from_extended_decimal_format(Decimal(market_info["minNotional"])),
                settlement_price=None
                if market_info["settlementPrice"] == ""
                else Token.convert_value_from_extended_decimal_format(Decimal(market_info["settlementPrice"])),
            )

            binary_option_markets[market.id] = market

        self._spot_markets = spot_markets
        self._derivative_markets = derivative_markets
        self._binary_option_markets = binary_option_markets

    def _token_representation(
        self,
        token_meta: Dict[str, Any],
        denom: str,
        tokens_by_denom: Dict[str, Token],
        tokens_by_symbol: Dict[str, Token],
    ) -> Token:
        if denom not in tokens_by_denom:
            unique_symbol = denom
            for symbol_candidate in [token_meta["symbol"], token_meta["name"]]:
                if symbol_candidate not in tokens_by_symbol:
                    unique_symbol = symbol_candidate
                    break

            token = Token(
                name=token_meta["name"],
                symbol=token_meta["symbol"],
                denom=denom,
                address=token_meta["address"],
                decimals=token_meta["decimals"],
                logo=token_meta["logo"],
                updated=int(token_meta["updatedAt"]),
                unique_symbol=unique_symbol,
            )

            tokens_by_denom[denom] = token
            tokens_by_symbol[unique_symbol] = token

        return tokens_by_denom[denom]

    async def _tokens_from_official_lists(
        self,
        network: Network,
    ) -> Tuple[Dict[str, Token], Dict[str, Token]]:
        tokens_by_symbol = dict()
        tokens_by_denom = dict()

        loader = TokensFileLoader()
        tokens = await loader.load_tokens(network.official_tokens_list_url)

        for token in tokens:
            if token.denom is not None and token.denom != "" and token.denom not in tokens_by_denom:
                unique_symbol = token.denom
                for symbol_candidate in [token.symbol, token.name]:
                    if symbol_candidate not in tokens_by_symbol:
                        unique_symbol = symbol_candidate
                        break

                new_token = Token(
                    name=token.name,
                    symbol=token.symbol,
                    denom=token.denom,
                    address=token.address,
                    decimals=token.decimals,
                    logo=token.logo,
                    updated=token.updated,
                    unique_symbol=unique_symbol,
                )

                tokens_by_denom[new_token.denom] = new_token
                tokens_by_symbol[unique_symbol] = new_token

        return tokens_by_symbol, tokens_by_denom

    def _initialize_timeout_height_sync_task(self):
        self._cancel_timeout_height_sync_task()
        self._timeout_height_sync_task = asyncio.get_event_loop().create_task(self._timeout_height_sync_process())

    async def _timeout_height_sync_process(self):
        while True:
            await self.sync_timeout_height()
            await asyncio.sleep(DEFAULT_TIMEOUTHEIGHT_SYNC_INTERVAL)

    def _cancel_timeout_height_sync_task(self):
        if self._timeout_height_sync_task is not None:
            try:
                self._timeout_height_sync_task.cancel()
                asyncio.get_event_loop().run_until_complete(asyncio.wait_for(self._timeout_height_sync_task, timeout=1))
            except Exception as e:
                logger = LoggerProvider().logger_for_class(logging_class=self.__class__)
                logger.warning("error canceling timeout height sync task")
                logger.debug("error canceling timeout height sync task", exc_info=e)
        self._timeout_height_sync_task = None
