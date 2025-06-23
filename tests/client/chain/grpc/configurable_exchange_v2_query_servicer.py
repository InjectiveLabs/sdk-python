from collections import deque

from pyinjective.proto.injective.exchange.v2 import (
    query_pb2 as exchange_query_pb,
    query_pb2_grpc as exchange_query_grpc,
)


class ConfigurableExchangeV2QueryServicer(exchange_query_grpc.QueryServicer):
    def __init__(self):
        super().__init__()
        self.exchange_params = deque()
        self.subaccount_deposits_responses = deque()
        self.subaccount_deposit_responses = deque()
        self.exchange_balances_responses = deque()
        self.aggregate_volume_responses = deque()
        self.aggregate_volumes_responses = deque()
        self.aggregate_market_volume_responses = deque()
        self.aggregate_market_volumes_responses = deque()
        self.denom_decimal_responses = deque()
        self.denom_decimals_responses = deque()
        self.spot_markets_responses = deque()
        self.spot_market_responses = deque()
        self.full_spot_markets_responses = deque()
        self.full_spot_market_responses = deque()
        self.spot_orderbook_responses = deque()
        self.trader_spot_orders_responses = deque()
        self.account_address_spot_orders_responses = deque()
        self.spot_orders_by_hashes_responses = deque()
        self.subaccount_orders_responses = deque()
        self.trader_spot_transient_orders_responses = deque()
        self.spot_mid_price_and_tob_responses = deque()
        self.derivative_mid_price_and_tob_responses = deque()
        self.derivative_orderbook_responses = deque()
        self.trader_derivative_orders_responses = deque()
        self.account_address_derivative_orders_responses = deque()
        self.derivative_orders_by_hashes_responses = deque()
        self.trader_derivative_transient_orders_responses = deque()
        self.derivative_markets_responses = deque()
        self.derivative_market_responses = deque()
        self.derivative_market_address_responses = deque()
        self.subaccount_trade_nonce_responses = deque()
        self.positions_responses = deque()
        self.subaccount_positions_responses = deque()
        self.subaccount_position_in_market_responses = deque()
        self.subaccount_effective_position_in_market_responses = deque()
        self.perpetual_market_info_responses = deque()
        self.expiry_futures_market_info_responses = deque()
        self.perpetual_market_funding_responses = deque()
        self.subaccount_order_metadata_responses = deque()
        self.trade_reward_points_responses = deque()
        self.pending_trade_reward_points_responses = deque()
        self.trade_reward_campaign_responses = deque()
        self.fee_discount_account_info_responses = deque()
        self.fee_discount_schedule_responses = deque()
        self.balance_mismatches_responses = deque()
        self.balance_with_balance_holds_responses = deque()
        self.fee_discount_tier_statistics_responses = deque()
        self.mito_vault_infos_responses = deque()
        self.market_id_from_vault_responses = deque()
        self.historical_trade_records_responses = deque()
        self.is_opted_out_of_rewards_responses = deque()
        self.opted_out_of_rewards_accounts_responses = deque()
        self.market_volatility_responses = deque()
        self.binary_options_markets_responses = deque()
        self.trader_derivative_conditional_orders_responses = deque()
        self.market_atomic_execution_fee_multiplier_responses = deque()
        self.active_stake_grant_responses = deque()
        self.grant_authorization_responses = deque()
        self.grant_authorizations_responses = deque()
        self.l3_derivative_orderbook_responses = deque()
        self.l3_spot_orderbook_responses = deque()
        self.market_balance_responses = deque()
        self.market_balances_responses = deque()
        self.denom_min_notional_responses = deque()
        self.denom_min_notionals_responses = deque()

    async def QueryExchangeParams(
        self, request: exchange_query_pb.QueryExchangeParamsRequest, context=None, metadata=None
    ):
        return self.exchange_params.pop()

    async def SubaccountDeposits(
        self, request: exchange_query_pb.QuerySubaccountDepositsRequest, context=None, metadata=None
    ):
        return self.subaccount_deposits_responses.pop()

    async def SubaccountDeposit(
        self, request: exchange_query_pb.QuerySubaccountDepositRequest, context=None, metadata=None
    ):
        return self.subaccount_deposit_responses.pop()

    async def ExchangeBalances(
        self, request: exchange_query_pb.QueryExchangeBalancesRequest, context=None, metadata=None
    ):
        return self.exchange_balances_responses.pop()

    async def AggregateVolume(
        self, request: exchange_query_pb.QueryAggregateVolumeRequest, context=None, metadata=None
    ):
        return self.aggregate_volume_responses.pop()

    async def AggregateVolumes(
        self, request: exchange_query_pb.QueryAggregateVolumesRequest, context=None, metadata=None
    ):
        return self.aggregate_volumes_responses.pop()

    async def AggregateMarketVolume(
        self, request: exchange_query_pb.QueryAggregateMarketVolumeRequest, context=None, metadata=None
    ):
        return self.aggregate_market_volume_responses.pop()

    async def AggregateMarketVolumes(
        self, request: exchange_query_pb.QueryAggregateMarketVolumesRequest, context=None, metadata=None
    ):
        return self.aggregate_market_volumes_responses.pop()

    async def DenomDecimal(self, request: exchange_query_pb.QueryDenomDecimalRequest, context=None, metadata=None):
        return self.denom_decimal_responses.pop()

    async def DenomDecimals(self, request: exchange_query_pb.QueryDenomDecimalsRequest, context=None, metadata=None):
        return self.denom_decimals_responses.pop()

    async def SpotMarkets(self, request: exchange_query_pb.QuerySpotMarketsRequest, context=None, metadata=None):
        return self.spot_markets_responses.pop()

    async def SpotMarket(self, request: exchange_query_pb.QuerySpotMarketRequest, context=None, metadata=None):
        return self.spot_market_responses.pop()

    async def FullSpotMarkets(
        self, request: exchange_query_pb.QueryFullSpotMarketsRequest, context=None, metadata=None
    ):
        return self.full_spot_markets_responses.pop()

    async def FullSpotMarket(self, request: exchange_query_pb.QueryFullSpotMarketRequest, context=None, metadata=None):
        return self.full_spot_market_responses.pop()

    async def SpotOrderbook(self, request: exchange_query_pb.QuerySpotOrderbookRequest, context=None, metadata=None):
        return self.spot_orderbook_responses.pop()

    async def TraderSpotOrders(
        self, request: exchange_query_pb.QueryTraderSpotOrdersRequest, context=None, metadata=None
    ):
        return self.trader_spot_orders_responses.pop()

    async def AccountAddressSpotOrders(
        self, request: exchange_query_pb.QueryAccountAddressSpotOrdersRequest, context=None, metadata=None
    ):
        return self.account_address_spot_orders_responses.pop()

    async def SpotOrdersByHashes(
        self, request: exchange_query_pb.QuerySpotOrdersByHashesRequest, context=None, metadata=None
    ):
        return self.spot_orders_by_hashes_responses.pop()

    async def SubaccountOrders(
        self, request: exchange_query_pb.QuerySubaccountOrdersRequest, context=None, metadata=None
    ):
        return self.subaccount_orders_responses.pop()

    async def TraderSpotTransientOrders(
        self, request: exchange_query_pb.QueryTraderSpotOrdersRequest, context=None, metadata=None
    ):
        return self.trader_spot_transient_orders_responses.pop()

    async def SpotMidPriceAndTOB(
        self, request: exchange_query_pb.QuerySpotMidPriceAndTOBRequest, context=None, metadata=None
    ):
        return self.spot_mid_price_and_tob_responses.pop()

    async def DerivativeMidPriceAndTOB(
        self, request: exchange_query_pb.QueryDerivativeMidPriceAndTOBRequest, context=None, metadata=None
    ):
        return self.derivative_mid_price_and_tob_responses.pop()

    async def DerivativeOrderbook(
        self, request: exchange_query_pb.QueryDerivativeOrderbookRequest, context=None, metadata=None
    ):
        return self.derivative_orderbook_responses.pop()

    async def TraderDerivativeOrders(
        self, request: exchange_query_pb.QueryTraderDerivativeOrdersRequest, context=None, metadata=None
    ):
        return self.trader_derivative_orders_responses.pop()

    async def AccountAddressDerivativeOrders(
        self, request: exchange_query_pb.QueryAccountAddressDerivativeOrdersRequest, context=None, metadata=None
    ):
        return self.account_address_derivative_orders_responses.pop()

    async def DerivativeOrdersByHashes(
        self, request: exchange_query_pb.QueryDerivativeOrdersByHashesRequest, context=None, metadata=None
    ):
        return self.derivative_orders_by_hashes_responses.pop()

    async def TraderDerivativeTransientOrders(
        self, request: exchange_query_pb.QueryTraderDerivativeOrdersRequest, context=None, metadata=None
    ):
        return self.trader_derivative_transient_orders_responses.pop()

    async def DerivativeMarkets(
        self, request: exchange_query_pb.QueryDerivativeMarketsRequest, context=None, metadata=None
    ):
        return self.derivative_markets_responses.pop()

    async def DerivativeMarket(
        self, request: exchange_query_pb.QueryDerivativeMarketRequest, context=None, metadata=None
    ):
        return self.derivative_market_responses.pop()

    async def DerivativeMarketAddress(
        self, request: exchange_query_pb.QueryDerivativeMarketAddressRequest, context=None, metadata=None
    ):
        return self.derivative_market_address_responses.pop()

    async def SubaccountTradeNonce(
        self, request: exchange_query_pb.QuerySubaccountTradeNonceRequest, context=None, metadata=None
    ):
        return self.subaccount_trade_nonce_responses.pop()

    async def Positions(self, request: exchange_query_pb.QueryPositionsRequest, context=None, metadata=None):
        return self.positions_responses.pop()

    async def SubaccountPositions(
        self, request: exchange_query_pb.QuerySubaccountPositionsRequest, context=None, metadata=None
    ):
        return self.subaccount_positions_responses.pop()

    async def SubaccountPositionInMarket(
        self, request: exchange_query_pb.QuerySubaccountPositionInMarketRequest, context=None, metadata=None
    ):
        return self.subaccount_position_in_market_responses.pop()

    async def SubaccountEffectivePositionInMarket(
        self, request: exchange_query_pb.QuerySubaccountEffectivePositionInMarketRequest, context=None, metadata=None
    ):
        return self.subaccount_effective_position_in_market_responses.pop()

    async def PerpetualMarketInfo(
        self, request: exchange_query_pb.QueryPerpetualMarketInfoRequest, context=None, metadata=None
    ):
        return self.perpetual_market_info_responses.pop()

    async def ExpiryFuturesMarketInfo(
        self, request: exchange_query_pb.QueryExpiryFuturesMarketInfoRequest, context=None, metadata=None
    ):
        return self.expiry_futures_market_info_responses.pop()

    async def PerpetualMarketFunding(
        self, request: exchange_query_pb.QueryPerpetualMarketFundingRequest, context=None, metadata=None
    ):
        return self.perpetual_market_funding_responses.pop()

    async def SubaccountOrderMetadata(
        self, request: exchange_query_pb.QuerySubaccountOrderMetadataRequest, context=None, metadata=None
    ):
        return self.subaccount_order_metadata_responses.pop()

    async def TradeRewardPoints(
        self, request: exchange_query_pb.QueryTradeRewardPointsRequest, context=None, metadata=None
    ):
        return self.trade_reward_points_responses.pop()

    async def PendingTradeRewardPoints(
        self, request: exchange_query_pb.QueryTradeRewardPointsRequest, context=None, metadata=None
    ):
        return self.pending_trade_reward_points_responses.pop()

    async def TradeRewardCampaign(
        self, request: exchange_query_pb.QueryTradeRewardCampaignRequest, context=None, metadata=None
    ):
        return self.trade_reward_campaign_responses.pop()

    async def FeeDiscountAccountInfo(
        self, request: exchange_query_pb.QueryFeeDiscountAccountInfoRequest, context=None, metadata=None
    ):
        return self.fee_discount_account_info_responses.pop()

    async def FeeDiscountSchedule(
        self, request: exchange_query_pb.QueryFeeDiscountScheduleRequest, context=None, metadata=None
    ):
        return self.fee_discount_schedule_responses.pop()

    async def BalanceMismatches(
        self, request: exchange_query_pb.QueryBalanceMismatchesRequest, context=None, metadata=None
    ):
        return self.balance_mismatches_responses.pop()

    async def BalanceWithBalanceHolds(
        self, request: exchange_query_pb.QueryBalanceWithBalanceHoldsRequest, context=None, metadata=None
    ):
        return self.balance_with_balance_holds_responses.pop()

    async def FeeDiscountTierStatistics(
        self, request: exchange_query_pb.QueryFeeDiscountTierStatisticsRequest, context=None, metadata=None
    ):
        return self.fee_discount_tier_statistics_responses.pop()

    async def MitoVaultInfos(self, request: exchange_query_pb.MitoVaultInfosRequest, context=None, metadata=None):
        return self.mito_vault_infos_responses.pop()

    async def QueryMarketIDFromVault(
        self, request: exchange_query_pb.QueryMarketIDFromVaultRequest, context=None, metadata=None
    ):
        return self.market_id_from_vault_responses.pop()

    async def HistoricalTradeRecords(
        self, request: exchange_query_pb.QueryHistoricalTradeRecordsRequest, context=None, metadata=None
    ):
        return self.historical_trade_records_responses.pop()

    async def IsOptedOutOfRewards(
        self, request: exchange_query_pb.QueryIsOptedOutOfRewardsRequest, context=None, metadata=None
    ):
        return self.is_opted_out_of_rewards_responses.pop()

    async def OptedOutOfRewardsAccounts(
        self, request: exchange_query_pb.QueryOptedOutOfRewardsAccountsRequest, context=None, metadata=None
    ):
        return self.opted_out_of_rewards_accounts_responses.pop()

    async def MarketVolatility(
        self, request: exchange_query_pb.QueryMarketVolatilityRequest, context=None, metadata=None
    ):
        return self.market_volatility_responses.pop()

    async def BinaryOptionsMarkets(
        self, request: exchange_query_pb.QueryBinaryMarketsRequest, context=None, metadata=None
    ):
        return self.binary_options_markets_responses.pop()

    async def TraderDerivativeConditionalOrders(
        self, request: exchange_query_pb.QueryTraderDerivativeConditionalOrdersRequest, context=None, metadata=None
    ):
        return self.trader_derivative_conditional_orders_responses.pop()

    async def MarketAtomicExecutionFeeMultiplier(
        self, request: exchange_query_pb.QueryMarketAtomicExecutionFeeMultiplierRequest, context=None, metadata=None
    ):
        return self.market_atomic_execution_fee_multiplier_responses.pop()

    async def ActiveStakeGrant(
        self, request: exchange_query_pb.QueryActiveStakeGrantRequest, context=None, metadata=None
    ):
        return self.active_stake_grant_responses.pop()

    async def GrantAuthorization(
        self, request: exchange_query_pb.QueryGrantAuthorizationRequest, context=None, metadata=None
    ):
        return self.grant_authorization_responses.pop()

    async def GrantAuthorizations(
        self, request: exchange_query_pb.QueryGrantAuthorizationsRequest, context=None, metadata=None
    ):
        return self.grant_authorizations_responses.pop()

    async def L3DerivativeOrderBook(
        self, request: exchange_query_pb.QueryFullDerivativeOrderbookRequest, context=None, metadata=None
    ):
        return self.l3_derivative_orderbook_responses.pop()

    async def L3SpotOrderBook(
        self, request: exchange_query_pb.QueryFullSpotOrderbookRequest, context=None, metadata=None
    ):
        return self.l3_spot_orderbook_responses.pop()

    async def MarketBalance(self, request: exchange_query_pb.QueryMarketBalanceRequest, context=None, metadata=None):
        return self.market_balance_responses.pop()

    async def MarketBalances(self, request: exchange_query_pb.QueryMarketBalancesRequest, context=None, metadata=None):
        return self.market_balances_responses.pop()

    async def DenomMinNotional(
        self, request: exchange_query_pb.QueryDenomMinNotionalRequest, context=None, metadata=None
    ):
        return self.denom_min_notional_responses.pop()

    async def DenomMinNotionals(
        self, request: exchange_query_pb.QueryDenomMinNotionalsRequest, context=None, metadata=None
    ):
        return self.denom_min_notionals_responses.pop()
