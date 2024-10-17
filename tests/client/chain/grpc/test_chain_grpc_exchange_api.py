import base64

import grpc
import pytest

from pyinjective.client.chain.grpc.chain_grpc_exchange_api import ChainGrpcExchangeApi
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as coin_pb
from pyinjective.proto.injective.exchange.v1beta1 import (
    exchange_pb2 as exchange_pb,
    genesis_pb2 as genesis_pb,
    query_pb2 as exchange_query_pb,
)
from pyinjective.proto.injective.oracle.v1beta1 import oracle_pb2 as oracle_pb
from tests.client.chain.grpc.configurable_exchange_query_servicer import ConfigurableExchangeQueryServicer


@pytest.fixture
def exchange_servicer():
    return ConfigurableExchangeQueryServicer()


class TestChainGrpcBankApi:
    @pytest.mark.asyncio
    async def test_fetch_exchange_params(
        self,
        exchange_servicer,
    ):
        spot_market_instant_listing_fee = coin_pb.Coin(denom="inj", amount="10000000000000000000")
        derivative_market_instant_listing_fee = coin_pb.Coin(denom="inj", amount="2000000000000000000000")
        binary_options_market_instant_listing_fee = coin_pb.Coin(denom="inj", amount="30000000000000000000")
        admin = "inj1knhahceyp57j5x7xh69p7utegnnnfgxavmahjr"
        params = exchange_pb.Params(
            spot_market_instant_listing_fee=spot_market_instant_listing_fee,
            derivative_market_instant_listing_fee=derivative_market_instant_listing_fee,
            default_spot_maker_fee_rate="-0.000100000000000000",
            default_spot_taker_fee_rate="0.001000000000000000",
            default_derivative_maker_fee_rate="-0.000100000000000000",
            default_derivative_taker_fee_rate="0.001000000000000000",
            default_initial_margin_ratio="0.050000000000000000",
            default_maintenance_margin_ratio="0.020000000000000000",
            default_funding_interval=3600,
            funding_multiple=4600,
            relayer_fee_share_rate="0.400000000000000000",
            default_hourly_funding_rate_cap="0.000625000000000000",
            default_hourly_interest_rate="0.000004166660000000",
            max_derivative_order_side_count=20,
            inj_reward_staked_requirement_threshold="25000000000000000000",
            trading_rewards_vesting_duration=1209600,
            liquidator_reward_share_rate="0.050000000000000000",
            binary_options_market_instant_listing_fee=binary_options_market_instant_listing_fee,
            atomic_market_order_access_level=2,
            spot_atomic_market_order_fee_multiplier="2.000000000000000000",
            derivative_atomic_market_order_fee_multiplier="2.000000000000000000",
            binary_options_atomic_market_order_fee_multiplier="2.000000000000000000",
            minimal_protocol_fee_rate="0.000010000000000000",
            is_instant_derivative_market_launch_enabled=False,
            post_only_mode_height_threshold=57078000,
            margin_decrease_price_timestamp_threshold_seconds=10,
            exchange_admins=[admin],
            inj_auction_max_cap="1000000000000000000000",
        )
        exchange_servicer.exchange_params.append(exchange_query_pb.QueryExchangeParamsResponse(params=params))

        api = self._api_instance(servicer=exchange_servicer)

        module_params = await api.fetch_exchange_params()
        expected_params = {
            "params": {
                "spotMarketInstantListingFee": {
                    "amount": spot_market_instant_listing_fee.amount,
                    "denom": spot_market_instant_listing_fee.denom,
                },
                "derivativeMarketInstantListingFee": {
                    "amount": derivative_market_instant_listing_fee.amount,
                    "denom": derivative_market_instant_listing_fee.denom,
                },
                "defaultSpotMakerFeeRate": params.default_spot_maker_fee_rate,
                "defaultSpotTakerFeeRate": params.default_spot_taker_fee_rate,
                "defaultDerivativeMakerFeeRate": params.default_derivative_maker_fee_rate,
                "defaultDerivativeTakerFeeRate": params.default_derivative_taker_fee_rate,
                "defaultInitialMarginRatio": params.default_initial_margin_ratio,
                "defaultMaintenanceMarginRatio": params.default_maintenance_margin_ratio,
                "defaultFundingInterval": str(params.default_funding_interval),
                "fundingMultiple": str(params.funding_multiple),
                "relayerFeeShareRate": params.relayer_fee_share_rate,
                "defaultHourlyFundingRateCap": params.default_hourly_funding_rate_cap,
                "defaultHourlyInterestRate": params.default_hourly_interest_rate,
                "maxDerivativeOrderSideCount": params.max_derivative_order_side_count,
                "injRewardStakedRequirementThreshold": params.inj_reward_staked_requirement_threshold,
                "tradingRewardsVestingDuration": str(params.trading_rewards_vesting_duration),
                "liquidatorRewardShareRate": "0.050000000000000000",
                "binaryOptionsMarketInstantListingFee": {
                    "amount": binary_options_market_instant_listing_fee.amount,
                    "denom": binary_options_market_instant_listing_fee.denom,
                },
                "atomicMarketOrderAccessLevel": exchange_pb.AtomicMarketOrderAccessLevel.Name(
                    params.atomic_market_order_access_level
                ),
                "spotAtomicMarketOrderFeeMultiplier": params.spot_atomic_market_order_fee_multiplier,
                "derivativeAtomicMarketOrderFeeMultiplier": params.derivative_atomic_market_order_fee_multiplier,
                "binaryOptionsAtomicMarketOrderFeeMultiplier": params.binary_options_atomic_market_order_fee_multiplier,
                "minimalProtocolFeeRate": params.minimal_protocol_fee_rate,
                "isInstantDerivativeMarketLaunchEnabled": params.is_instant_derivative_market_launch_enabled,
                "postOnlyModeHeightThreshold": str(params.post_only_mode_height_threshold),
                "marginDecreasePriceTimestampThresholdSeconds": str(
                    params.margin_decrease_price_timestamp_threshold_seconds
                ),
                "exchangeAdmins": [admin],
                "injAuctionMaxCap": params.inj_auction_max_cap,
            }
        }

        assert module_params == expected_params

    @pytest.mark.asyncio
    async def test_fetch_subaccount_deposits(
        self,
        exchange_servicer,
    ):
        deposit_denom = "inj"
        deposit = exchange_pb.Deposit(
            available_balance="1000000000000000000",
            total_balance="2000000000000000000",
        )
        exchange_servicer.subaccount_deposits_responses.append(
            exchange_query_pb.QuerySubaccountDepositsResponse(deposits={deposit_denom: deposit})
        )

        api = self._api_instance(servicer=exchange_servicer)

        deposits = await api.fetch_subaccount_deposits(
            subaccount_id="0x5303d92e49a619bb29de8fb6f59c0e7589213cc8000000000000000000000001",
            subaccount_trader="inj1ady3s7whq30l4fx8sj3x6muv5mx4dfdlcpv8n7",
            subaccount_nonce=1,
        )
        expected_deposits = {
            "deposits": {
                deposit_denom: {
                    "availableBalance": deposit.available_balance,
                    "totalBalance": deposit.total_balance,
                },
            }
        }

        assert deposits == expected_deposits

    @pytest.mark.asyncio
    async def test_fetch_subaccount_deposit(
        self,
        exchange_servicer,
    ):
        deposit = exchange_pb.Deposit(
            available_balance="1000000000000000000",
            total_balance="2000000000000000000",
        )
        exchange_servicer.subaccount_deposit_responses.append(
            exchange_query_pb.QuerySubaccountDepositResponse(deposits=deposit)
        )

        api = self._api_instance(servicer=exchange_servicer)

        deposit_response = await api.fetch_subaccount_deposit(
            subaccount_id="0x5303d92e49a619bb29de8fb6f59c0e7589213cc8000000000000000000000001",
            denom="inj",
        )
        expected_deposit = {
            "deposits": {
                "availableBalance": deposit.available_balance,
                "totalBalance": deposit.total_balance,
            }
        }

        assert deposit_response == expected_deposit

    @pytest.mark.asyncio
    async def test_fetch_exchange_balances(
        self,
        exchange_servicer,
    ):
        deposit = exchange_pb.Deposit(
            available_balance="1000000000000000000",
            total_balance="2000000000000000000",
        )
        balance = genesis_pb.Balance(
            subaccount_id="0x5303d92e49a619bb29de8fb6f59c0e7589213cc8000000000000000000000001",
            denom="inj",
            deposits=deposit,
        )
        exchange_servicer.exchange_balances_responses.append(
            exchange_query_pb.QueryExchangeBalancesResponse(balances=[balance])
        )

        api = self._api_instance(servicer=exchange_servicer)

        balances_response = await api.fetch_exchange_balances()
        expected_balances = {
            "balances": [
                {
                    "subaccountId": balance.subaccount_id,
                    "denom": balance.denom,
                    "deposits": {
                        "availableBalance": deposit.available_balance,
                        "totalBalance": deposit.total_balance,
                    },
                },
            ]
        }

        assert balances_response == expected_balances

    @pytest.mark.asyncio
    async def test_fetch_aggregate_volume(
        self,
        exchange_servicer,
    ):
        volume = exchange_pb.VolumeRecord(
            maker_volume="1000000000000000000",
            taker_volume="2000000000000000000",
        )
        market_volume = exchange_pb.MarketVolume(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            volume=volume,
        )
        exchange_servicer.aggregate_volume_responses.append(
            exchange_query_pb.QueryAggregateVolumeResponse(
                aggregate_volumes=[market_volume],
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        volume_response = await api.fetch_aggregate_volume(account="inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r")
        expected_volume = {
            "aggregateVolumes": [
                {
                    "marketId": market_volume.market_id,
                    "volume": {
                        "makerVolume": volume.maker_volume,
                        "takerVolume": volume.taker_volume,
                    },
                },
            ]
        }

        assert volume_response == expected_volume

    @pytest.mark.asyncio
    async def test_fetch_aggregate_volumes(
        self,
        exchange_servicer,
    ):
        acc_volume = exchange_pb.VolumeRecord(
            maker_volume="1000000000000000000",
            taker_volume="2000000000000000000",
        )
        account_market_volume = exchange_pb.MarketVolume(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            volume=acc_volume,
        )
        account_volume = exchange_pb.AggregateAccountVolumeRecord(
            account="inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r",
            market_volumes=[account_market_volume],
        )
        volume = exchange_pb.VolumeRecord(
            maker_volume="3000000000000000000",
            taker_volume="4000000000000000000",
        )
        market_volume = exchange_pb.MarketVolume(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            volume=volume,
        )
        exchange_servicer.aggregate_volumes_responses.append(
            exchange_query_pb.QueryAggregateVolumesResponse(
                aggregate_account_volumes=[account_volume],
                aggregate_market_volumes=[market_volume],
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        volume_response = await api.fetch_aggregate_volumes(
            accounts=[account_volume.account],
            market_ids=[account_market_volume.market_id],
        )
        expected_volume = {
            "aggregateAccountVolumes": [
                {
                    "account": account_volume.account,
                    "marketVolumes": [
                        {
                            "marketId": account_market_volume.market_id,
                            "volume": {
                                "makerVolume": acc_volume.maker_volume,
                                "takerVolume": acc_volume.taker_volume,
                            },
                        },
                    ],
                },
            ],
            "aggregateMarketVolumes": [
                {
                    "marketId": market_volume.market_id,
                    "volume": {
                        "makerVolume": volume.maker_volume,
                        "takerVolume": volume.taker_volume,
                    },
                },
            ],
        }

        assert volume_response == expected_volume

    @pytest.mark.asyncio
    async def test_fetch_aggregate_market_volume(
        self,
        exchange_servicer,
    ):
        volume = exchange_pb.VolumeRecord(
            maker_volume="1000000000000000000",
            taker_volume="2000000000000000000",
        )
        exchange_servicer.aggregate_market_volume_responses.append(
            exchange_query_pb.QueryAggregateMarketVolumeResponse(
                volume=volume,
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        volume_response = await api.fetch_aggregate_market_volume(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
        )
        expected_volume = {
            "volume": {
                "makerVolume": volume.maker_volume,
                "takerVolume": volume.taker_volume,
            }
        }

        assert volume_response == expected_volume

    @pytest.mark.asyncio
    async def test_fetch_aggregate_market_volumes(
        self,
        exchange_servicer,
    ):
        volume = exchange_pb.VolumeRecord(
            maker_volume="3000000000000000000",
            taker_volume="4000000000000000000",
        )
        market_volume = exchange_pb.MarketVolume(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            volume=volume,
        )
        exchange_servicer.aggregate_market_volumes_responses.append(
            exchange_query_pb.QueryAggregateMarketVolumesResponse(
                volumes=[market_volume],
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        volume_response = await api.fetch_aggregate_market_volumes(
            market_ids=[market_volume.market_id],
        )
        expected_volume = {
            "volumes": [
                {
                    "marketId": market_volume.market_id,
                    "volume": {
                        "makerVolume": volume.maker_volume,
                        "takerVolume": volume.taker_volume,
                    },
                },
            ],
        }

        assert volume_response == expected_volume

    @pytest.mark.asyncio
    async def test_fetch_denom_decimal(
        self,
        exchange_servicer,
    ):
        decimal = 18
        exchange_servicer.denom_decimal_responses.append(
            exchange_query_pb.QueryDenomDecimalResponse(
                decimal=decimal,
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        denom_decimal = await api.fetch_denom_decimal(denom="inj")
        expected_decimal = {"decimal": str(decimal)}

        assert denom_decimal == expected_decimal

    @pytest.mark.asyncio
    async def test_fetch_denom_decimals(
        self,
        exchange_servicer,
    ):
        denom_decimal = exchange_pb.DenomDecimals(
            denom="inj",
            decimals=18,
        )
        exchange_servicer.denom_decimals_responses.append(
            exchange_query_pb.QueryDenomDecimalsResponse(
                denom_decimals=[denom_decimal],
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        denom_decimals = await api.fetch_denom_decimals(denoms=[denom_decimal.denom])
        expected_decimals = {
            "denomDecimals": [
                {
                    "denom": denom_decimal.denom,
                    "decimals": str(denom_decimal.decimals),
                }
            ]
        }

        assert denom_decimals == expected_decimals

    @pytest.mark.asyncio
    async def test_fetch_spot_markets(
        self,
        exchange_servicer,
    ):
        market = exchange_pb.SpotMarket(
            ticker="INJ/USDT",
            base_denom="inj",
            quote_denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            maker_fee_rate="-0.0001",
            taker_fee_rate="0.001",
            relayer_fee_share_rate="0.4",
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            status=1,
            min_price_tick_size="0.000000000000001",
            min_quantity_tick_size="1000000000000000",
            min_notional="5000000000000000000",
            admin="inj1knhahceyp57j5x7xh69p7utegnnnfgxavmahjr",
            admin_permissions=1,
            base_decimals=18,
            quote_decimals=6,
        )
        exchange_servicer.spot_markets_responses.append(
            exchange_query_pb.QuerySpotMarketsResponse(
                markets=[market],
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        status_string = exchange_pb.MarketStatus.Name(market.status)
        markets = await api.fetch_spot_markets(
            status=status_string,
            market_ids=[market.market_id],
        )
        expected_markets = {
            "markets": [
                {
                    "ticker": market.ticker,
                    "baseDenom": market.base_denom,
                    "quoteDenom": market.quote_denom,
                    "makerFeeRate": market.maker_fee_rate,
                    "takerFeeRate": market.taker_fee_rate,
                    "relayerFeeShareRate": market.relayer_fee_share_rate,
                    "marketId": market.market_id,
                    "status": status_string,
                    "minPriceTickSize": market.min_price_tick_size,
                    "minQuantityTickSize": market.min_quantity_tick_size,
                    "minNotional": market.min_notional,
                    "admin": market.admin,
                    "adminPermissions": market.admin_permissions,
                    "baseDecimals": market.base_decimals,
                    "quoteDecimals": market.quote_decimals,
                }
            ]
        }

        assert markets == expected_markets

    @pytest.mark.asyncio
    async def test_fetch_spot_market(
        self,
        exchange_servicer,
    ):
        market = exchange_pb.SpotMarket(
            ticker="INJ/USDT",
            base_denom="inj",
            quote_denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            maker_fee_rate="-0.0001",
            taker_fee_rate="0.001",
            relayer_fee_share_rate="0.4",
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            status=1,
            min_price_tick_size="0.000000000000001",
            min_quantity_tick_size="1000000000000000",
            min_notional="5000000000000000000",
            admin="inj1knhahceyp57j5x7xh69p7utegnnnfgxavmahjr",
            admin_permissions=1,
            base_decimals=18,
            quote_decimals=6,
        )
        exchange_servicer.spot_market_responses.append(
            exchange_query_pb.QuerySpotMarketResponse(
                market=market,
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        response_market = await api.fetch_spot_market(
            market_id=market.market_id,
        )
        expected_market = {
            "market": {
                "ticker": market.ticker,
                "baseDenom": market.base_denom,
                "quoteDenom": market.quote_denom,
                "makerFeeRate": market.maker_fee_rate,
                "takerFeeRate": market.taker_fee_rate,
                "relayerFeeShareRate": market.relayer_fee_share_rate,
                "marketId": market.market_id,
                "status": exchange_pb.MarketStatus.Name(market.status),
                "minPriceTickSize": market.min_price_tick_size,
                "minQuantityTickSize": market.min_quantity_tick_size,
                "minNotional": market.min_notional,
                "admin": market.admin,
                "adminPermissions": market.admin_permissions,
                "baseDecimals": market.base_decimals,
                "quoteDecimals": market.quote_decimals,
            }
        }

        assert response_market == expected_market

    @pytest.mark.asyncio
    async def test_fetch_full_spot_markets(
        self,
        exchange_servicer,
    ):
        market = exchange_pb.SpotMarket(
            ticker="INJ/USDT",
            base_denom="inj",
            quote_denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            maker_fee_rate="-0.0001",
            taker_fee_rate="0.001",
            relayer_fee_share_rate="0.4",
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            status=1,
            min_price_tick_size="0.000000000000001",
            min_quantity_tick_size="1000000000000000",
            min_notional="5000000000000000000",
            admin="inj1knhahceyp57j5x7xh69p7utegnnnfgxavmahjr",
            admin_permissions=1,
            base_decimals=18,
            quote_decimals=6,
        )
        mid_price_and_tob = exchange_pb.MidPriceAndTOB(
            mid_price="2000000000000000000",
            best_buy_price="1000000000000000000",
            best_sell_price="3000000000000000000",
        )
        full_market = exchange_query_pb.FullSpotMarket(
            market=market,
            mid_price_and_tob=mid_price_and_tob,
        )
        exchange_servicer.full_spot_markets_responses.append(
            exchange_query_pb.QueryFullSpotMarketsResponse(
                markets=[full_market],
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        status_string = exchange_pb.MarketStatus.Name(market.status)
        markets = await api.fetch_full_spot_markets(
            status=status_string,
            market_ids=[market.market_id],
            with_mid_price_and_tob=True,
        )
        expected_markets = {
            "markets": [
                {
                    "market": {
                        "ticker": market.ticker,
                        "baseDenom": market.base_denom,
                        "quoteDenom": market.quote_denom,
                        "makerFeeRate": market.maker_fee_rate,
                        "takerFeeRate": market.taker_fee_rate,
                        "relayerFeeShareRate": market.relayer_fee_share_rate,
                        "marketId": market.market_id,
                        "status": status_string,
                        "minPriceTickSize": market.min_price_tick_size,
                        "minQuantityTickSize": market.min_quantity_tick_size,
                        "minNotional": market.min_notional,
                        "admin": market.admin,
                        "adminPermissions": market.admin_permissions,
                        "baseDecimals": market.base_decimals,
                        "quoteDecimals": market.quote_decimals,
                    },
                    "midPriceAndTob": {
                        "midPrice": mid_price_and_tob.mid_price,
                        "bestBuyPrice": mid_price_and_tob.best_buy_price,
                        "bestSellPrice": mid_price_and_tob.best_sell_price,
                    },
                }
            ]
        }

        assert markets == expected_markets

    @pytest.mark.asyncio
    async def test_fetch_full_spot_market(
        self,
        exchange_servicer,
    ):
        market = exchange_pb.SpotMarket(
            ticker="INJ/USDT",
            base_denom="inj",
            quote_denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            maker_fee_rate="-0.0001",
            taker_fee_rate="0.001",
            relayer_fee_share_rate="0.4",
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            status=1,
            min_price_tick_size="0.000000000000001",
            min_quantity_tick_size="1000000000000000",
            min_notional="5000000000000000000",
            admin="inj1knhahceyp57j5x7xh69p7utegnnnfgxavmahjr",
            admin_permissions=1,
            base_decimals=18,
            quote_decimals=6,
        )
        mid_price_and_tob = exchange_pb.MidPriceAndTOB(
            mid_price="2000000000000000000",
            best_buy_price="1000000000000000000",
            best_sell_price="3000000000000000000",
        )
        full_market = exchange_query_pb.FullSpotMarket(
            market=market,
            mid_price_and_tob=mid_price_and_tob,
        )
        exchange_servicer.full_spot_market_responses.append(
            exchange_query_pb.QueryFullSpotMarketResponse(
                market=full_market,
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        status_string = exchange_pb.MarketStatus.Name(market.status)
        market_response = await api.fetch_full_spot_market(
            market_id=market.market_id,
            with_mid_price_and_tob=True,
        )
        expected_market = {
            "market": {
                "market": {
                    "ticker": market.ticker,
                    "baseDenom": market.base_denom,
                    "quoteDenom": market.quote_denom,
                    "makerFeeRate": market.maker_fee_rate,
                    "takerFeeRate": market.taker_fee_rate,
                    "relayerFeeShareRate": market.relayer_fee_share_rate,
                    "marketId": market.market_id,
                    "status": status_string,
                    "minPriceTickSize": market.min_price_tick_size,
                    "minQuantityTickSize": market.min_quantity_tick_size,
                    "minNotional": market.min_notional,
                    "admin": market.admin,
                    "adminPermissions": market.admin_permissions,
                    "baseDecimals": market.base_decimals,
                    "quoteDecimals": market.quote_decimals,
                },
                "midPriceAndTob": {
                    "midPrice": mid_price_and_tob.mid_price,
                    "bestBuyPrice": mid_price_and_tob.best_buy_price,
                    "bestSellPrice": mid_price_and_tob.best_sell_price,
                },
            }
        }

        assert market_response == expected_market

    @pytest.mark.asyncio
    async def test_fetch_spot_orderbook(
        self,
        exchange_servicer,
    ):
        buy_price_level = exchange_pb.Level(
            p="1000000000000000000",
            q="1000000000000000",
        )
        sell_price_level = exchange_pb.Level(
            p="2000000000000000000",
            q="2000000000000000",
        )
        exchange_servicer.spot_orderbook_responses.append(
            exchange_query_pb.QuerySpotOrderbookResponse(
                buys_price_level=[buy_price_level],
                sells_price_level=[sell_price_level],
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        orderbook = await api.fetch_spot_orderbook(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            order_side="Side_Unspecified",
            limit_cumulative_notional="1000000000000000000",
            limit_cumulative_quantity="1000000000000000",
            pagination=PaginationOption(limit=100),
        )
        expected_orderbook = {
            "buysPriceLevel": [
                {
                    "p": buy_price_level.p,
                    "q": buy_price_level.q,
                }
            ],
            "sellsPriceLevel": [
                {
                    "p": sell_price_level.p,
                    "q": sell_price_level.q,
                }
            ],
        }

        assert orderbook == expected_orderbook

    @pytest.mark.asyncio
    async def test_fetch_trader_spot_orders(
        self,
        exchange_servicer,
    ):
        order = exchange_query_pb.TrimmedSpotLimitOrder(
            price="1000000000000000000",
            quantity="1000000000000000",
            fillable="1000000000000000",
            isBuy=True,
            order_hash="0x14e43adbb3302db28bcd0619068227ebca880cdd66cdfc8b4a662bcac0777849",
            cid="order_cid",
        )
        exchange_servicer.trader_spot_orders_responses.append(
            exchange_query_pb.QueryTraderSpotOrdersResponse(
                orders=[order],
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        orders = await api.fetch_trader_spot_orders(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            subaccount_id="0x5303d92e49a619bb29de8fb6f59c0e7589213cc8000000000000000000000001",
        )
        expected_orders = {
            "orders": [
                {
                    "price": order.price,
                    "quantity": order.quantity,
                    "fillable": order.fillable,
                    "isBuy": order.isBuy,
                    "orderHash": order.order_hash,
                    "cid": order.cid,
                }
            ]
        }

        assert orders == expected_orders

    @pytest.mark.asyncio
    async def test_fetch_account_address_spot_orders(
        self,
        exchange_servicer,
    ):
        order = exchange_query_pb.TrimmedSpotLimitOrder(
            price="1000000000000000000",
            quantity="1000000000000000",
            fillable="1000000000000000",
            isBuy=True,
            order_hash="0x14e43adbb3302db28bcd0619068227ebca880cdd66cdfc8b4a662bcac0777849",
            cid="order_cid",
        )
        exchange_servicer.account_address_spot_orders_responses.append(
            exchange_query_pb.QueryAccountAddressSpotOrdersResponse(
                orders=[order],
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        orders = await api.fetch_account_address_spot_orders(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            account_address="inj1ady3s7whq30l4fx8sj3x6muv5mx4dfdlcpv8n7",
        )
        expected_orders = {
            "orders": [
                {
                    "price": order.price,
                    "quantity": order.quantity,
                    "fillable": order.fillable,
                    "isBuy": order.isBuy,
                    "orderHash": order.order_hash,
                    "cid": order.cid,
                }
            ]
        }

        assert orders == expected_orders

    @pytest.mark.asyncio
    async def test_fetch_spot_orders_by_hashes(
        self,
        exchange_servicer,
    ):
        order = exchange_query_pb.TrimmedSpotLimitOrder(
            price="1000000000000000000",
            quantity="1000000000000000",
            fillable="1000000000000000",
            isBuy=True,
            order_hash="0x14e43adbb3302db28bcd0619068227ebca880cdd66cdfc8b4a662bcac0777849",
            cid="order_cid",
        )
        exchange_servicer.spot_orders_by_hashes_responses.append(
            exchange_query_pb.QuerySpotOrdersByHashesResponse(
                orders=[order],
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        orders = await api.fetch_spot_orders_by_hashes(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            subaccount_id="0x5303d92e49a619bb29de8fb6f59c0e7589213cc8000000000000000000000001",
            order_hashes=[order.order_hash],
        )
        expected_orders = {
            "orders": [
                {
                    "price": order.price,
                    "quantity": order.quantity,
                    "fillable": order.fillable,
                    "isBuy": order.isBuy,
                    "orderHash": order.order_hash,
                    "cid": order.cid,
                }
            ]
        }

        assert orders == expected_orders

    @pytest.mark.asyncio
    async def test_fetch_subaccount_orders(
        self,
        exchange_servicer,
    ):
        buy_subaccount_order = exchange_pb.SubaccountOrder(
            price="1000000000000000000",
            quantity="1000000000000000",
            isReduceOnly=False,
            cid="buy_cid",
        )
        buy_order = exchange_pb.SubaccountOrderData(
            order=buy_subaccount_order,
            order_hash="0x14e43adbb3302db28bcd0619068227ebca880cdd66cdfc8b4a662bcac0777849".encode(),
        )
        sell_subaccount_order = exchange_pb.SubaccountOrder(
            price="2000000000000000000",
            quantity="2000000000000000",
            isReduceOnly=False,
            cid="sell_cid",
        )
        sell_order = exchange_pb.SubaccountOrderData(
            order=sell_subaccount_order,
            order_hash="0x222daa22f60fe9f075ed0ca583459e121c23e64431c3fbffdedda04598ede0d2".encode(),
        )
        exchange_servicer.subaccount_orders_responses.append(
            exchange_query_pb.QuerySubaccountOrdersResponse(
                buy_orders=[buy_order],
                sell_orders=[sell_order],
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        orders = await api.fetch_subaccount_orders(
            subaccount_id="0x5303d92e49a619bb29de8fb6f59c0e7589213cc8000000000000000000000001",
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
        )
        expected_orders = {
            "buyOrders": [
                {
                    "order": {
                        "price": buy_subaccount_order.price,
                        "quantity": buy_subaccount_order.quantity,
                        "isReduceOnly": buy_subaccount_order.isReduceOnly,
                        "cid": buy_subaccount_order.cid,
                    },
                    "orderHash": base64.b64encode(buy_order.order_hash).decode(),
                }
            ],
            "sellOrders": [
                {
                    "order": {
                        "price": sell_subaccount_order.price,
                        "quantity": sell_subaccount_order.quantity,
                        "isReduceOnly": sell_subaccount_order.isReduceOnly,
                        "cid": sell_subaccount_order.cid,
                    },
                    "orderHash": base64.b64encode(sell_order.order_hash).decode(),
                }
            ],
        }

        assert orders == expected_orders

    @pytest.mark.asyncio
    async def test_fetch_trader_spot_transient_orders(
        self,
        exchange_servicer,
    ):
        order = exchange_query_pb.TrimmedSpotLimitOrder(
            price="1000000000000000000",
            quantity="1000000000000000",
            fillable="1000000000000000",
            isBuy=True,
            order_hash="0x14e43adbb3302db28bcd0619068227ebca880cdd66cdfc8b4a662bcac0777849",
            cid="order_cid",
        )
        exchange_servicer.trader_spot_transient_orders_responses.append(
            exchange_query_pb.QueryTraderSpotOrdersResponse(
                orders=[order],
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        orders = await api.fetch_trader_spot_transient_orders(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
            subaccount_id="0x5303d92e49a619bb29de8fb6f59c0e7589213cc8000000000000000000000001",
        )
        expected_orders = {
            "orders": [
                {
                    "price": order.price,
                    "quantity": order.quantity,
                    "fillable": order.fillable,
                    "isBuy": order.isBuy,
                    "orderHash": order.order_hash,
                    "cid": order.cid,
                }
            ]
        }

        assert orders == expected_orders

    @pytest.mark.asyncio
    async def test_fetch_spot_mid_price_and_tob(
        self,
        exchange_servicer,
    ):
        response = exchange_query_pb.QuerySpotMidPriceAndTOBResponse(
            mid_price="2000000000000000000",
            best_buy_price="1000000000000000000",
            best_sell_price="3000000000000000000",
        )
        exchange_servicer.spot_mid_price_and_tob_responses.append(response)

        api = self._api_instance(servicer=exchange_servicer)

        prices = await api.fetch_spot_mid_price_and_tob(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
        )
        expected_prices = {
            "midPrice": response.mid_price,
            "bestBuyPrice": response.best_buy_price,
            "bestSellPrice": response.best_sell_price,
        }

        assert prices == expected_prices

    @pytest.mark.asyncio
    async def test_fetch_derivative_mid_price_and_tob(
        self,
        exchange_servicer,
    ):
        response = exchange_query_pb.QueryDerivativeMidPriceAndTOBResponse(
            mid_price="2000000000000000000",
            best_buy_price="1000000000000000000",
            best_sell_price="3000000000000000000",
        )
        exchange_servicer.derivative_mid_price_and_tob_responses.append(response)

        api = self._api_instance(servicer=exchange_servicer)

        prices = await api.fetch_derivative_mid_price_and_tob(
            market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
        )
        expected_prices = {
            "midPrice": response.mid_price,
            "bestBuyPrice": response.best_buy_price,
            "bestSellPrice": response.best_sell_price,
        }

        assert prices == expected_prices

    @pytest.mark.asyncio
    async def test_fetch_derivative_orderbook(
        self,
        exchange_servicer,
    ):
        buy_price_level = exchange_pb.Level(
            p="1000000000000000000",
            q="1000000000000000",
        )
        sell_price_level = exchange_pb.Level(
            p="2000000000000000000",
            q="2000000000000000",
        )
        exchange_servicer.derivative_orderbook_responses.append(
            exchange_query_pb.QueryDerivativeOrderbookResponse(
                buys_price_level=[buy_price_level],
                sells_price_level=[sell_price_level],
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        orderbook = await api.fetch_derivative_orderbook(
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            limit_cumulative_notional="1000000000000000000",
            pagination=PaginationOption(limit=100),
        )
        expected_orderbook = {
            "buysPriceLevel": [
                {
                    "p": buy_price_level.p,
                    "q": buy_price_level.q,
                }
            ],
            "sellsPriceLevel": [
                {
                    "p": sell_price_level.p,
                    "q": sell_price_level.q,
                }
            ],
        }

        assert orderbook == expected_orderbook

    @pytest.mark.asyncio
    async def test_fetch_trader_derivative_orders(
        self,
        exchange_servicer,
    ):
        order = exchange_query_pb.TrimmedDerivativeLimitOrder(
            price="1000000000000000000",
            quantity="1000000000000000",
            margin="1000000000000000000000000000000000",
            fillable="1000000000000000",
            isBuy=True,
            order_hash="0x14e43adbb3302db28bcd0619068227ebca880cdd66cdfc8b4a662bcac0777849",
            cid="order_cid",
        )
        exchange_servicer.trader_derivative_orders_responses.append(
            exchange_query_pb.QueryTraderDerivativeOrdersResponse(
                orders=[order],
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        orders = await api.fetch_trader_derivative_orders(
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            subaccount_id="0x5303d92e49a619bb29de8fb6f59c0e7589213cc8000000000000000000000001",
        )
        expected_orders = {
            "orders": [
                {
                    "price": order.price,
                    "quantity": order.quantity,
                    "margin": order.margin,
                    "fillable": order.fillable,
                    "isBuy": order.isBuy,
                    "orderHash": order.order_hash,
                    "cid": order.cid,
                }
            ]
        }

        assert orders == expected_orders

    @pytest.mark.asyncio
    async def test_fetch_account_address_derivative_orders(
        self,
        exchange_servicer,
    ):
        order = exchange_query_pb.TrimmedDerivativeLimitOrder(
            price="1000000000000000000",
            quantity="1000000000000000",
            margin="1000000000000000000000000000000000",
            fillable="1000000000000000",
            isBuy=True,
            order_hash="0x14e43adbb3302db28bcd0619068227ebca880cdd66cdfc8b4a662bcac0777849",
            cid="order_cid",
        )
        exchange_servicer.account_address_derivative_orders_responses.append(
            exchange_query_pb.QueryAccountAddressDerivativeOrdersResponse(
                orders=[order],
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        orders = await api.fetch_account_address_derivative_orders(
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            account_address="inj1ady3s7whq30l4fx8sj3x6muv5mx4dfdlcpv8n7",
        )
        expected_orders = {
            "orders": [
                {
                    "price": order.price,
                    "quantity": order.quantity,
                    "margin": order.margin,
                    "fillable": order.fillable,
                    "isBuy": order.isBuy,
                    "orderHash": order.order_hash,
                    "cid": order.cid,
                }
            ]
        }

        assert orders == expected_orders

    @pytest.mark.asyncio
    async def test_fetch_derivative_orders_by_hashes(
        self,
        exchange_servicer,
    ):
        order = exchange_query_pb.TrimmedDerivativeLimitOrder(
            price="1000000000000000000",
            quantity="1000000000000000",
            margin="1000000000000000000000000000000000",
            fillable="1000000000000000",
            isBuy=True,
            order_hash="0x14e43adbb3302db28bcd0619068227ebca880cdd66cdfc8b4a662bcac0777849",
            cid="order_cid",
        )
        exchange_servicer.derivative_orders_by_hashes_responses.append(
            exchange_query_pb.QueryDerivativeOrdersByHashesResponse(
                orders=[order],
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        orders = await api.fetch_derivative_orders_by_hashes(
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            subaccount_id="0x5303d92e49a619bb29de8fb6f59c0e7589213cc8000000000000000000000001",
            order_hashes=[order.order_hash],
        )
        expected_orders = {
            "orders": [
                {
                    "price": order.price,
                    "quantity": order.quantity,
                    "margin": order.margin,
                    "fillable": order.fillable,
                    "isBuy": order.isBuy,
                    "orderHash": order.order_hash,
                    "cid": order.cid,
                }
            ]
        }

        assert orders == expected_orders

    @pytest.mark.asyncio
    async def test_fetch_trader_derivative_transient_orders(
        self,
        exchange_servicer,
    ):
        order = exchange_query_pb.TrimmedDerivativeLimitOrder(
            price="1000000000000000000",
            quantity="1000000000000000",
            margin="1000000000000000000000000000000000",
            fillable="1000000000000000",
            isBuy=True,
            order_hash="0x14e43adbb3302db28bcd0619068227ebca880cdd66cdfc8b4a662bcac0777849",
            cid="order_cid",
        )
        exchange_servicer.trader_derivative_transient_orders_responses.append(
            exchange_query_pb.QueryTraderDerivativeOrdersResponse(
                orders=[order],
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        orders = await api.fetch_trader_derivative_transient_orders(
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            subaccount_id="0x5303d92e49a619bb29de8fb6f59c0e7589213cc8000000000000000000000001",
        )
        expected_orders = {
            "orders": [
                {
                    "price": order.price,
                    "quantity": order.quantity,
                    "margin": order.margin,
                    "fillable": order.fillable,
                    "isBuy": order.isBuy,
                    "orderHash": order.order_hash,
                    "cid": order.cid,
                }
            ]
        }

        assert orders == expected_orders

    @pytest.mark.asyncio
    async def test_fetch_derivative_markets(
        self,
        exchange_servicer,
    ):
        market = exchange_pb.DerivativeMarket(
            ticker="20250608/USDT",
            oracle_base="0x2d9315a88f3019f8efa88dfe9c0f0843712da0bac814461e27733f6b83eb51b3",
            oracle_quote="0x1fc18861232290221461220bd4e2acd1dcdfbc89c84092c93c18bdc7756c1588",
            oracle_type=9,
            oracle_scale_factor=6,
            quote_denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            initial_margin_ratio="50000000000000000",
            maintenance_margin_ratio="20000000000000000",
            maker_fee_rate="-0.0001",
            taker_fee_rate="0.001",
            relayer_fee_share_rate="400000000000000000",
            isPerpetual=True,
            status=1,
            min_price_tick_size="100000000000000000000",
            min_quantity_tick_size="1000000000000000",
            min_notional="5000000000000000000",
            admin="inj1knhahceyp57j5x7xh69p7utegnnnfgxavmahjr",
            admin_permissions=1,
            quote_decimals=6,
        )
        market_info = exchange_pb.PerpetualMarketInfo(
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            hourly_funding_rate_cap="625000000000000",
            hourly_interest_rate="4166660000000",
            next_funding_timestamp=1708099200,
            funding_interval=3600,
        )
        funding_info = exchange_pb.PerpetualMarketFunding(
            cumulative_funding="-107853477278881692857461",
            cumulative_price="0",
            last_timestamp=1708099200,
        )
        perpetual_info = exchange_query_pb.PerpetualMarketState(
            market_info=market_info,
            funding_info=funding_info,
        )
        mid_price_and_tob = exchange_pb.MidPriceAndTOB(
            mid_price="2000000000000000000",
            best_buy_price="1000000000000000000",
            best_sell_price="3000000000000000000",
        )
        full_market = exchange_query_pb.FullDerivativeMarket(
            market=market,
            perpetual_info=perpetual_info,
            mark_price="33803835513327368963000000",
            mid_price_and_tob=mid_price_and_tob,
        )
        exchange_servicer.derivative_markets_responses.append(
            exchange_query_pb.QueryDerivativeMarketsResponse(
                markets=[full_market],
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        status_string = exchange_pb.MarketStatus.Name(market.status)
        markets = await api.fetch_derivative_markets(
            status=status_string,
            market_ids=[market.market_id],
        )
        expected_markets = {
            "markets": [
                {
                    "market": {
                        "ticker": market.ticker,
                        "oracleBase": market.oracle_base,
                        "oracleQuote": market.oracle_quote,
                        "oracleType": oracle_pb.OracleType.Name(market.oracle_type),
                        "oracleScaleFactor": market.oracle_scale_factor,
                        "quoteDenom": market.quote_denom,
                        "marketId": market.market_id,
                        "initialMarginRatio": market.initial_margin_ratio,
                        "maintenanceMarginRatio": market.maintenance_margin_ratio,
                        "makerFeeRate": market.maker_fee_rate,
                        "takerFeeRate": market.taker_fee_rate,
                        "relayerFeeShareRate": market.relayer_fee_share_rate,
                        "isPerpetual": market.isPerpetual,
                        "status": status_string,
                        "minPriceTickSize": market.min_price_tick_size,
                        "minQuantityTickSize": market.min_quantity_tick_size,
                        "minNotional": market.min_notional,
                        "admin": market.admin,
                        "adminPermissions": market.admin_permissions,
                        "quoteDecimals": market.quote_decimals,
                    },
                    "perpetualInfo": {
                        "marketInfo": {
                            "marketId": market_info.market_id,
                            "hourlyFundingRateCap": market_info.hourly_funding_rate_cap,
                            "hourlyInterestRate": market_info.hourly_interest_rate,
                            "nextFundingTimestamp": str(market_info.next_funding_timestamp),
                            "fundingInterval": str(market_info.funding_interval),
                        },
                        "fundingInfo": {
                            "cumulativeFunding": funding_info.cumulative_funding,
                            "cumulativePrice": funding_info.cumulative_price,
                            "lastTimestamp": str(funding_info.last_timestamp),
                        },
                    },
                    "markPrice": full_market.mark_price,
                    "midPriceAndTob": {
                        "midPrice": mid_price_and_tob.mid_price,
                        "bestBuyPrice": mid_price_and_tob.best_buy_price,
                        "bestSellPrice": mid_price_and_tob.best_sell_price,
                    },
                }
            ]
        }

        assert markets == expected_markets

    @pytest.mark.asyncio
    async def test_fetch_derivative_market(
        self,
        exchange_servicer,
    ):
        market = exchange_pb.DerivativeMarket(
            ticker="INJ/USDT PERP",
            oracle_base="0x2d9315a88f3019f8efa88dfe9c0f0843712da0bac814461e27733f6b83eb51b3",
            oracle_quote="0x1fc18861232290221461220bd4e2acd1dcdfbc89c84092c93c18bdc7756c1588",
            oracle_type=9,
            oracle_scale_factor=6,
            quote_denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            initial_margin_ratio="50000000000000000",
            maintenance_margin_ratio="20000000000000000",
            maker_fee_rate="-0.0001",
            taker_fee_rate="0.001",
            relayer_fee_share_rate="400000000000000000",
            isPerpetual=True,
            status=1,
            min_price_tick_size="100000000000000000000",
            min_quantity_tick_size="1000000000000000",
            min_notional="5000000000000000000",
            admin="inj1knhahceyp57j5x7xh69p7utegnnnfgxavmahjr",
            admin_permissions=1,
            quote_decimals=6,
        )
        market_info = exchange_pb.PerpetualMarketInfo(
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            hourly_funding_rate_cap="625000000000000",
            hourly_interest_rate="4166660000000",
            next_funding_timestamp=1708099200,
            funding_interval=3600,
        )
        funding_info = exchange_pb.PerpetualMarketFunding(
            cumulative_funding="-107853477278881692857461",
            cumulative_price="0",
            last_timestamp=1708099200,
        )
        perpetual_info = exchange_query_pb.PerpetualMarketState(
            market_info=market_info,
            funding_info=funding_info,
        )
        mid_price_and_tob = exchange_pb.MidPriceAndTOB(
            mid_price="2000000000000000000",
            best_buy_price="1000000000000000000",
            best_sell_price="3000000000000000000",
        )
        full_market = exchange_query_pb.FullDerivativeMarket(
            market=market,
            perpetual_info=perpetual_info,
            mark_price="33803835513327368963000000",
            mid_price_and_tob=mid_price_and_tob,
        )
        exchange_servicer.derivative_market_responses.append(
            exchange_query_pb.QueryDerivativeMarketResponse(
                market=full_market,
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        status_string = exchange_pb.MarketStatus.Name(market.status)
        market_response = await api.fetch_derivative_market(
            market_id=market.market_id,
        )
        expected_market = {
            "market": {
                "market": {
                    "ticker": market.ticker,
                    "oracleBase": market.oracle_base,
                    "oracleQuote": market.oracle_quote,
                    "oracleType": oracle_pb.OracleType.Name(market.oracle_type),
                    "oracleScaleFactor": market.oracle_scale_factor,
                    "quoteDenom": market.quote_denom,
                    "marketId": market.market_id,
                    "initialMarginRatio": market.initial_margin_ratio,
                    "maintenanceMarginRatio": market.maintenance_margin_ratio,
                    "makerFeeRate": market.maker_fee_rate,
                    "takerFeeRate": market.taker_fee_rate,
                    "relayerFeeShareRate": market.relayer_fee_share_rate,
                    "isPerpetual": market.isPerpetual,
                    "status": status_string,
                    "minPriceTickSize": market.min_price_tick_size,
                    "minQuantityTickSize": market.min_quantity_tick_size,
                    "minNotional": market.min_notional,
                    "admin": market.admin,
                    "adminPermissions": market.admin_permissions,
                    "quoteDecimals": market.quote_decimals,
                },
                "perpetualInfo": {
                    "marketInfo": {
                        "marketId": market_info.market_id,
                        "hourlyFundingRateCap": market_info.hourly_funding_rate_cap,
                        "hourlyInterestRate": market_info.hourly_interest_rate,
                        "nextFundingTimestamp": str(market_info.next_funding_timestamp),
                        "fundingInterval": str(market_info.funding_interval),
                    },
                    "fundingInfo": {
                        "cumulativeFunding": funding_info.cumulative_funding,
                        "cumulativePrice": funding_info.cumulative_price,
                        "lastTimestamp": str(funding_info.last_timestamp),
                    },
                },
                "markPrice": full_market.mark_price,
                "midPriceAndTob": {
                    "midPrice": mid_price_and_tob.mid_price,
                    "bestBuyPrice": mid_price_and_tob.best_buy_price,
                    "bestSellPrice": mid_price_and_tob.best_sell_price,
                },
            }
        }

        assert market_response == expected_market

    @pytest.mark.asyncio
    async def test_fetch_derivative_market_address(
        self,
        exchange_servicer,
    ):
        response = exchange_query_pb.QueryDerivativeMarketAddressResponse(
            address="inj1zlh5sqevkfphtwnu9cul8p89vseme2eqt0snn9",
            subaccount_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20000000000000000000000000",
        )
        exchange_servicer.derivative_market_address_responses.append(response)

        api = self._api_instance(servicer=exchange_servicer)

        address = await api.fetch_derivative_market_address(
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
        )
        expected_address = {
            "address": response.address,
            "subaccountId": response.subaccount_id,
        }

        assert address == expected_address

    @pytest.mark.asyncio
    async def test_fetch_subaccount_trade_nonce(
        self,
        exchange_servicer,
    ):
        response = exchange_query_pb.QuerySubaccountTradeNonceResponse(nonce=1234567879)
        exchange_servicer.subaccount_trade_nonce_responses.append(response)

        api = self._api_instance(servicer=exchange_servicer)

        nonce = await api.fetch_subaccount_trade_nonce(
            subaccount_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20000000000000000000000000",
        )
        expected_nonce = {
            "nonce": response.nonce,
        }

        assert nonce == expected_nonce

    @pytest.mark.asyncio
    async def test_fetch_positions(
        self,
        exchange_servicer,
    ):
        position = exchange_pb.Position(
            isLong=True,
            quantity="1000000000000000",
            entry_price="2000000000000000000",
            margin="2000000000000000000000000000000000",
            cumulative_funding_entry="4000000",
        )
        derivative_position = genesis_pb.DerivativePosition(
            subaccount_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20000000000000000000000000",
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            position=position,
        )
        exchange_servicer.positions_responses.append(
            exchange_query_pb.QueryPositionsResponse(state=[derivative_position])
        )

        api = self._api_instance(servicer=exchange_servicer)

        positions = await api.fetch_positions()
        expected_positions = {
            "state": [
                {
                    "subaccountId": derivative_position.subaccount_id,
                    "marketId": derivative_position.market_id,
                    "position": {
                        "isLong": position.isLong,
                        "quantity": position.quantity,
                        "entryPrice": position.entry_price,
                        "margin": position.margin,
                        "cumulativeFundingEntry": position.cumulative_funding_entry,
                    },
                },
            ],
        }

        assert positions == expected_positions

    @pytest.mark.asyncio
    async def test_fetch_subaccount_positions(
        self,
        exchange_servicer,
    ):
        position = exchange_pb.Position(
            isLong=True,
            quantity="1000000000000000",
            entry_price="2000000000000000000",
            margin="2000000000000000000000000000000000",
            cumulative_funding_entry="4000000",
        )
        derivative_position = genesis_pb.DerivativePosition(
            subaccount_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20000000000000000000000000",
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            position=position,
        )
        exchange_servicer.subaccount_positions_responses.append(
            exchange_query_pb.QuerySubaccountPositionsResponse(state=[derivative_position])
        )

        api = self._api_instance(servicer=exchange_servicer)

        positions = await api.fetch_subaccount_positions(subaccount_id=derivative_position.subaccount_id)
        expected_positions = {
            "state": [
                {
                    "subaccountId": derivative_position.subaccount_id,
                    "marketId": derivative_position.market_id,
                    "position": {
                        "isLong": position.isLong,
                        "quantity": position.quantity,
                        "entryPrice": position.entry_price,
                        "margin": position.margin,
                        "cumulativeFundingEntry": position.cumulative_funding_entry,
                    },
                },
            ],
        }

        assert positions == expected_positions

    @pytest.mark.asyncio
    async def test_fetch_subaccount_position_in_market(
        self,
        exchange_servicer,
    ):
        subaccount_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20000000000000000000000000"
        market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
        position = exchange_pb.Position(
            isLong=True,
            quantity="1000000000000000",
            entry_price="2000000000000000000",
            margin="2000000000000000000000000000000000",
            cumulative_funding_entry="4000000",
        )
        exchange_servicer.subaccount_position_in_market_responses.append(
            exchange_query_pb.QuerySubaccountPositionInMarketResponse(state=position)
        )

        api = self._api_instance(servicer=exchange_servicer)

        position_response = await api.fetch_subaccount_position_in_market(
            subaccount_id=subaccount_id,
            market_id=market_id,
        )
        expected_position = {
            "state": {
                "isLong": position.isLong,
                "quantity": position.quantity,
                "entryPrice": position.entry_price,
                "margin": position.margin,
                "cumulativeFundingEntry": position.cumulative_funding_entry,
            },
        }

        assert position_response == expected_position

    @pytest.mark.asyncio
    async def test_fetch_subaccount_effective_position_in_market(
        self,
        exchange_servicer,
    ):
        subaccount_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20000000000000000000000000"
        market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"

        effective_position = exchange_query_pb.EffectivePosition(
            is_long=True,
            quantity="1000000000000000",
            entry_price="2000000000000000000",
            effective_margin="2000000000000000000000000000000000",
        )
        exchange_servicer.subaccount_effective_position_in_market_responses.append(
            exchange_query_pb.QuerySubaccountEffectivePositionInMarketResponse(state=effective_position)
        )

        api = self._api_instance(servicer=exchange_servicer)

        position_response = await api.fetch_subaccount_effective_position_in_market(
            subaccount_id=subaccount_id,
            market_id=market_id,
        )
        expected_position = {
            "state": {
                "isLong": effective_position.is_long,
                "quantity": effective_position.quantity,
                "entryPrice": effective_position.entry_price,
                "effectiveMargin": effective_position.effective_margin,
            },
        }

        assert position_response == expected_position

    @pytest.mark.asyncio
    async def test_fetch_perpetual_market_info(
        self,
        exchange_servicer,
    ):
        perpetual_market_info = exchange_pb.PerpetualMarketInfo(
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            hourly_funding_rate_cap="625000000000000",
            hourly_interest_rate="4166660000000",
            next_funding_timestamp=1708099200,
            funding_interval=3600,
        )
        exchange_servicer.perpetual_market_info_responses.append(
            exchange_query_pb.QueryPerpetualMarketInfoResponse(info=perpetual_market_info)
        )

        api = self._api_instance(servicer=exchange_servicer)

        market_info = await api.fetch_perpetual_market_info(market_id=perpetual_market_info.market_id)
        expected_market_info = {
            "info": {
                "marketId": perpetual_market_info.market_id,
                "hourlyFundingRateCap": perpetual_market_info.hourly_funding_rate_cap,
                "hourlyInterestRate": perpetual_market_info.hourly_interest_rate,
                "nextFundingTimestamp": str(perpetual_market_info.next_funding_timestamp),
                "fundingInterval": str(perpetual_market_info.funding_interval),
            }
        }

        assert market_info == expected_market_info

    @pytest.mark.asyncio
    async def test_fetch_expiry_futures_market_info(
        self,
        exchange_servicer,
    ):
        expiry_futures_market_info = exchange_pb.ExpiryFuturesMarketInfo(
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            expiration_timestamp=1708099200,
            twap_start_timestamp=1705566200,
            expiration_twap_start_price_cumulative="1000000000000000000",
            settlement_price="2000000000000000000",
        )
        exchange_servicer.expiry_futures_market_info_responses.append(
            exchange_query_pb.QueryExpiryFuturesMarketInfoResponse(info=expiry_futures_market_info)
        )

        api = self._api_instance(servicer=exchange_servicer)

        market_info = await api.fetch_expiry_futures_market_info(market_id=expiry_futures_market_info.market_id)
        expected_market_info = {
            "info": {
                "marketId": expiry_futures_market_info.market_id,
                "expirationTimestamp": str(expiry_futures_market_info.expiration_timestamp),
                "twapStartTimestamp": str(expiry_futures_market_info.twap_start_timestamp),
                "expirationTwapStartPriceCumulative": expiry_futures_market_info.expiration_twap_start_price_cumulative,
                "settlementPrice": expiry_futures_market_info.settlement_price,
            }
        }

        assert market_info == expected_market_info

    @pytest.mark.asyncio
    async def test_fetch_perpetual_market_funding(
        self,
        exchange_servicer,
    ):
        perpetual_market_funding = exchange_pb.PerpetualMarketFunding(
            cumulative_funding="-107853477278881692857461",
            cumulative_price="0",
            last_timestamp=1708099200,
        )
        exchange_servicer.perpetual_market_funding_responses.append(
            exchange_query_pb.QueryPerpetualMarketFundingResponse(state=perpetual_market_funding)
        )

        api = self._api_instance(servicer=exchange_servicer)

        funding = await api.fetch_perpetual_market_funding(
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
        )
        expected_funding = {
            "state": {
                "cumulativeFunding": perpetual_market_funding.cumulative_funding,
                "cumulativePrice": perpetual_market_funding.cumulative_price,
                "lastTimestamp": str(perpetual_market_funding.last_timestamp),
            }
        }

        assert funding == expected_funding

    @pytest.mark.asyncio
    async def test_fetch_subaccount_order_metadata(
        self,
        exchange_servicer,
    ):
        metadata = exchange_pb.SubaccountOrderbookMetadata(
            vanilla_limit_order_count=1,
            reduce_only_limit_order_count=2,
            aggregate_reduce_only_quantity="1000000000000000",
            aggregate_vanilla_quantity="2000000000000000",
            vanilla_conditional_order_count=3,
            reduce_only_conditional_order_count=4,
        )
        subaccount_order_metadata = exchange_query_pb.SubaccountOrderbookMetadataWithMarket(
            metadata=metadata,
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            isBuy=True,
        )
        exchange_servicer.subaccount_order_metadata_responses.append(
            exchange_query_pb.QuerySubaccountOrderMetadataResponse(metadata=[subaccount_order_metadata])
        )

        api = self._api_instance(servicer=exchange_servicer)

        metadata_response = await api.fetch_subaccount_order_metadata(
            subaccount_id="0x5303d92e49a619bb29de8fb6f59c0e7589213cc8000000000000000000000001"
        )
        expected_metadata = {
            "metadata": [
                {
                    "metadata": {
                        "vanillaLimitOrderCount": metadata.vanilla_limit_order_count,
                        "reduceOnlyLimitOrderCount": metadata.reduce_only_limit_order_count,
                        "aggregateReduceOnlyQuantity": metadata.aggregate_reduce_only_quantity,
                        "aggregateVanillaQuantity": metadata.aggregate_vanilla_quantity,
                        "vanillaConditionalOrderCount": metadata.vanilla_conditional_order_count,
                        "reduceOnlyConditionalOrderCount": metadata.reduce_only_conditional_order_count,
                    },
                    "marketId": subaccount_order_metadata.market_id,
                    "isBuy": subaccount_order_metadata.isBuy,
                },
            ]
        }

        assert metadata_response == expected_metadata

    @pytest.mark.asyncio
    async def test_fetch_trade_reward_points(
        self,
        exchange_servicer,
    ):
        points = "40"
        response = exchange_query_pb.QueryTradeRewardPointsResponse(account_trade_reward_points=[points])
        exchange_servicer.trade_reward_points_responses.append(response)

        api = self._api_instance(servicer=exchange_servicer)

        trade_reward_points = await api.fetch_trade_reward_points(
            accounts=["inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"],
            pending_pool_timestamp=1708099200,
        )
        expected_trade_reward_points = {"accountTradeRewardPoints": [points]}

        assert trade_reward_points == expected_trade_reward_points

    @pytest.mark.asyncio
    async def test_fetch_pending_trade_reward_points(
        self,
        exchange_servicer,
    ):
        points = "40"
        response = exchange_query_pb.QueryTradeRewardPointsResponse(account_trade_reward_points=[points])
        exchange_servicer.pending_trade_reward_points_responses.append(response)

        api = self._api_instance(servicer=exchange_servicer)

        trade_reward_points = await api.fetch_pending_trade_reward_points(
            accounts=["inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"],
            pending_pool_timestamp=1708099200,
        )
        expected_trade_reward_points = {"accountTradeRewardPoints": [points]}

        assert trade_reward_points == expected_trade_reward_points

    @pytest.mark.asyncio
    async def test_fetch_trade_reward_campaign(
        self,
        exchange_servicer,
    ):
        spot_market_multiplier = exchange_pb.PointsMultiplier(
            maker_points_multiplier="10.0",
            taker_points_multiplier="5.0",
        )
        derivative_market_multiplier = exchange_pb.PointsMultiplier(
            maker_points_multiplier="9.0",
            taker_points_multiplier="6.0",
        )
        trading_reward_boost_info = exchange_pb.TradingRewardCampaignBoostInfo(
            boosted_spot_market_ids=["0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00aaf7"],
            spot_market_multipliers=[spot_market_multiplier],
            boosted_derivative_market_ids=["0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"],
            derivative_market_multipliers=[derivative_market_multiplier],
        )
        trading_reward_campaign_info = exchange_pb.TradingRewardCampaignInfo(
            campaign_duration_seconds=3600,
            quote_denoms=["peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5"],
            trading_reward_boost_info=trading_reward_boost_info,
            disqualified_market_ids=["0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00aaf7"],
        )
        reward = coin_pb.Coin(
            amount="1000000000000000000",
            denom="inj",
        )
        trading_reward_pool_campaign_schedule = exchange_pb.CampaignRewardPool(
            start_timestamp=1708099200,
            max_campaign_rewards=[reward],
        )
        total_trade_reward_points = "40"
        pending_reward = coin_pb.Coin(
            amount="2000000000000000000",
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
        )
        pending_trading_reward_pool_campaign_schedule = exchange_pb.CampaignRewardPool(
            start_timestamp=1709099200,
            max_campaign_rewards=[pending_reward],
        )
        pending_total_trade_reward_points = "80"
        response = exchange_query_pb.QueryTradeRewardCampaignResponse(
            trading_reward_campaign_info=trading_reward_campaign_info,
            trading_reward_pool_campaign_schedule=[trading_reward_pool_campaign_schedule],
            total_trade_reward_points=total_trade_reward_points,
            pending_trading_reward_pool_campaign_schedule=[pending_trading_reward_pool_campaign_schedule],
            pending_total_trade_reward_points=[pending_total_trade_reward_points],
        )
        exchange_servicer.trade_reward_campaign_responses.append(response)

        api = self._api_instance(servicer=exchange_servicer)

        trade_reward_campaign = await api.fetch_trade_reward_campaign()
        expected_campaign = {
            "tradingRewardCampaignInfo": {
                "campaignDurationSeconds": str(trading_reward_campaign_info.campaign_duration_seconds),
                "quoteDenoms": trading_reward_campaign_info.quote_denoms,
                "tradingRewardBoostInfo": {
                    "boostedSpotMarketIds": (
                        trading_reward_campaign_info.trading_reward_boost_info.boosted_spot_market_ids
                    ),
                    "spotMarketMultipliers": [
                        {
                            "makerPointsMultiplier": spot_market_multiplier.maker_points_multiplier,
                            "takerPointsMultiplier": spot_market_multiplier.taker_points_multiplier,
                        },
                    ],
                    "boostedDerivativeMarketIds": (
                        trading_reward_campaign_info.trading_reward_boost_info.boosted_derivative_market_ids
                    ),
                    "derivativeMarketMultipliers": [
                        {
                            "makerPointsMultiplier": derivative_market_multiplier.maker_points_multiplier,
                            "takerPointsMultiplier": derivative_market_multiplier.taker_points_multiplier,
                        },
                    ],
                },
                "disqualifiedMarketIds": trading_reward_campaign_info.disqualified_market_ids,
            },
            "tradingRewardPoolCampaignSchedule": [
                {
                    "startTimestamp": str(trading_reward_pool_campaign_schedule.start_timestamp),
                    "maxCampaignRewards": [
                        {
                            "amount": trading_reward_pool_campaign_schedule.max_campaign_rewards[0].amount,
                            "denom": trading_reward_pool_campaign_schedule.max_campaign_rewards[0].denom,
                        },
                    ],
                },
            ],
            "totalTradeRewardPoints": total_trade_reward_points,
            "pendingTradingRewardPoolCampaignSchedule": [
                {
                    "startTimestamp": str(pending_trading_reward_pool_campaign_schedule.start_timestamp),
                    "maxCampaignRewards": [
                        {
                            "amount": pending_trading_reward_pool_campaign_schedule.max_campaign_rewards[0].amount,
                            "denom": pending_trading_reward_pool_campaign_schedule.max_campaign_rewards[0].denom,
                        },
                    ],
                },
            ],
            "pendingTotalTradeRewardPoints": [pending_total_trade_reward_points],
        }

        assert trade_reward_campaign == expected_campaign

    @pytest.mark.asyncio
    async def test_fetch_fee_discount_account_info(
        self,
        exchange_servicer,
    ):
        account_info = exchange_pb.FeeDiscountTierInfo(
            maker_discount_rate="0.0001",
            taker_discount_rate="0.0002",
            staked_amount="1000000000",
            volume="1000000000000000000",
        )
        account_ttl = exchange_pb.FeeDiscountTierTTL(
            tier=3,
            ttl_timestamp=1708099200,
        )
        response = exchange_query_pb.QueryFeeDiscountAccountInfoResponse(
            tier_level=3,
            account_info=account_info,
            account_ttl=account_ttl,
        )
        exchange_servicer.fee_discount_account_info_responses.append(response)

        api = self._api_instance(servicer=exchange_servicer)

        fee_discount = await api.fetch_fee_discount_account_info(account="inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r")
        expected_fee_discount = {
            "tierLevel": str(response.tier_level),
            "accountInfo": {
                "makerDiscountRate": account_info.maker_discount_rate,
                "takerDiscountRate": account_info.taker_discount_rate,
                "stakedAmount": account_info.staked_amount,
                "volume": account_info.volume,
            },
            "accountTtl": {
                "tier": str(account_ttl.tier),
                "ttlTimestamp": str(account_ttl.ttl_timestamp),
            },
        }

        assert fee_discount == expected_fee_discount

    @pytest.mark.asyncio
    async def test_fetch_fee_discount_schedule(
        self,
        exchange_servicer,
    ):
        fee_discount_tier_info = exchange_pb.FeeDiscountTierInfo(
            maker_discount_rate="0.0001",
            taker_discount_rate="0.0002",
            staked_amount="1000000000",
            volume="1000000000000000000",
        )
        fee_discount_schedule = exchange_pb.FeeDiscountSchedule(
            bucket_count=3,
            bucket_duration=3600,
            quote_denoms=["peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5"],
            tier_infos=[fee_discount_tier_info],
            disqualified_market_ids=["0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"],
        )
        exchange_servicer.fee_discount_schedule_responses.append(
            exchange_query_pb.QueryFeeDiscountScheduleResponse(
                fee_discount_schedule=fee_discount_schedule,
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        schedule = await api.fetch_fee_discount_schedule()
        expected_schedule = {
            "feeDiscountSchedule": {
                "bucketCount": str(fee_discount_schedule.bucket_count),
                "bucketDuration": str(fee_discount_schedule.bucket_duration),
                "quoteDenoms": fee_discount_schedule.quote_denoms,
                "tierInfos": [
                    {
                        "makerDiscountRate": fee_discount_tier_info.maker_discount_rate,
                        "takerDiscountRate": fee_discount_tier_info.taker_discount_rate,
                        "stakedAmount": fee_discount_tier_info.staked_amount,
                        "volume": fee_discount_tier_info.volume,
                    }
                ],
                "disqualifiedMarketIds": fee_discount_schedule.disqualified_market_ids,
            },
        }

        assert schedule == expected_schedule

    @pytest.mark.asyncio
    async def test_fetch_balance_mismatches(
        self,
        exchange_servicer,
    ):
        balance_mismatch = exchange_query_pb.BalanceMismatch(
            subaccountId="0x5303d92e49a619bb29de8fb6f59c0e7589213cc8000000000000000000000001",
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            available="1000000000000000",
            total="2000000000000000",
            balance_hold="3000000000000000",
            expected_total="4000000000000000",
            difference="500000000000000",
        )
        exchange_servicer.balance_mismatches_responses.append(
            exchange_query_pb.QueryBalanceMismatchesResponse(
                balance_mismatches=[balance_mismatch],
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        mismatches = await api.fetch_balance_mismatches(dust_factor=20)
        expected_mismatches = {
            "balanceMismatches": [
                {
                    "subaccountId": balance_mismatch.subaccountId,
                    "denom": balance_mismatch.denom,
                    "available": balance_mismatch.available,
                    "total": balance_mismatch.total,
                    "balanceHold": balance_mismatch.balance_hold,
                    "expectedTotal": balance_mismatch.expected_total,
                    "difference": balance_mismatch.difference,
                }
            ],
        }

        assert mismatches == expected_mismatches

    @pytest.mark.asyncio
    async def test_fetch_balance_with_balance_holds(
        self,
        exchange_servicer,
    ):
        balance_with_balance_hold = exchange_query_pb.BalanceWithMarginHold(
            subaccountId="0x5303d92e49a619bb29de8fb6f59c0e7589213cc8000000000000000000000001",
            denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            available="1000000000000000",
            total="2000000000000000",
            balance_hold="3000000000000000",
        )
        exchange_servicer.balance_with_balance_holds_responses.append(
            exchange_query_pb.QueryBalanceWithBalanceHoldsResponse(
                balance_with_balance_holds=[balance_with_balance_hold],
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        balance = await api.fetch_balance_with_balance_holds()
        expected_balance = {
            "balanceWithBalanceHolds": [
                {
                    "subaccountId": balance_with_balance_hold.subaccountId,
                    "denom": balance_with_balance_hold.denom,
                    "available": balance_with_balance_hold.available,
                    "total": balance_with_balance_hold.total,
                    "balanceHold": balance_with_balance_hold.balance_hold,
                }
            ],
        }

        assert balance == expected_balance

    @pytest.mark.asyncio
    async def test_fetch_fee_discount_tier_statistics(
        self,
        exchange_servicer,
    ):
        tier_statistics = exchange_query_pb.TierStatistic(
            tier=3,
            count=30,
        )
        exchange_servicer.fee_discount_tier_statistics_responses.append(
            exchange_query_pb.QueryFeeDiscountTierStatisticsResponse(
                statistics=[tier_statistics],
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        statistics = await api.fetch_fee_discount_tier_statistics()
        expected_statistics = {
            "statistics": [
                {
                    "tier": str(tier_statistics.tier),
                    "count": str(tier_statistics.count),
                }
            ],
        }

        assert statistics == expected_statistics

    @pytest.mark.asyncio
    async def test_fetch_mito_vault_infos(
        self,
        exchange_servicer,
    ):
        master_address = "inj1zlh5sqevkfphtwnu9cul8p89vseme2eqt0snn9"
        derivative_address = "inj1zlh5"
        spot_address = "inj1zlh6"
        cw20_address = "inj1zlh7"
        response = exchange_query_pb.MitoVaultInfosResponse(
            master_addresses=[master_address],
            derivative_addresses=[derivative_address],
            spot_addresses=[spot_address],
            cw20_addresses=[cw20_address],
        )
        exchange_servicer.mito_vault_infos_responses.append(response)

        api = self._api_instance(servicer=exchange_servicer)

        mito_vaults = await api.fetch_mito_vault_infos()
        expected_mito_vaults = {
            "masterAddresses": [master_address],
            "derivativeAddresses": [derivative_address],
            "spotAddresses": [spot_address],
            "cw20Addresses": [cw20_address],
        }

        assert mito_vaults == expected_mito_vaults

    @pytest.mark.asyncio
    async def test_fetch_market_id_from_vault(
        self,
        exchange_servicer,
    ):
        market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
        exchange_servicer.market_id_from_vault_responses.append(
            exchange_query_pb.QueryMarketIDFromVaultResponse(
                market_id=market_id,
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        market_id_response = await api.fetch_market_id_from_vault(
            vault_address="inj1zlh5sqevkfphtwnu9cul8p89vseme2eqt0snn9"
        )
        expected_market_id = {
            "marketId": market_id,
        }

        assert market_id_response == expected_market_id

    @pytest.mark.asyncio
    async def test_fetch_historical_trade_records(
        self,
        exchange_servicer,
    ):
        latest_trade_record = exchange_pb.TradeRecord(
            timestamp=1708099200,
            price="2000000000000000000",
            quantity="1000000000000000",
        )
        trade_record = exchange_pb.TradeRecords(
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            latest_trade_records=[latest_trade_record],
        )
        exchange_servicer.historical_trade_records_responses.append(
            exchange_query_pb.QueryHistoricalTradeRecordsResponse(
                trade_records=[trade_record],
            )
        )

        api = self._api_instance(servicer=exchange_servicer)

        records = await api.fetch_historical_trade_records(market_id=trade_record.market_id)
        expected_records = {
            "tradeRecords": [
                {
                    "marketId": trade_record.market_id,
                    "latestTradeRecords": [
                        {
                            "timestamp": str(latest_trade_record.timestamp),
                            "price": latest_trade_record.price,
                            "quantity": latest_trade_record.quantity,
                        }
                    ],
                },
            ],
        }

        assert records == expected_records

    @pytest.mark.asyncio
    async def test_fetch_is_opted_out_of_rewards(
        self,
        exchange_servicer,
    ):
        response = exchange_query_pb.QueryIsOptedOutOfRewardsResponse(
            is_opted_out=False,
        )
        exchange_servicer.is_opted_out_of_rewards_responses.append(response)

        api = self._api_instance(servicer=exchange_servicer)

        is_opted_out = await api.fetch_is_opted_out_of_rewards(account="inj1zlh5sqevkfphtwnu9cul8p89vseme2eqt0snn9")
        expected_is_opted_out = {
            "isOptedOut": response.is_opted_out,
        }

        assert is_opted_out == expected_is_opted_out

    @pytest.mark.asyncio
    async def test_fetch_opted_out_of_rewards_accounts(
        self,
        exchange_servicer,
    ):
        response = exchange_query_pb.QueryOptedOutOfRewardsAccountsResponse(
            accounts=["inj1zlh5sqevkfphtwnu9cul8p89vseme2eqt0snn9"],
        )
        exchange_servicer.opted_out_of_rewards_accounts_responses.append(response)

        api = self._api_instance(servicer=exchange_servicer)

        opted_out = await api.fetch_opted_out_of_rewards_accounts()
        expected_opted_out = {
            "accounts": response.accounts,
        }

        assert opted_out == expected_opted_out

    @pytest.mark.asyncio
    async def test_fetch_market_volatility(
        self,
        exchange_servicer,
    ):
        history_metadata = oracle_pb.MetadataStatistics(
            group_count=2,
            records_sample_size=10,
            mean="0.0001",
            twap="0.0005",
            first_timestamp=1702399200,
            last_timestamp=1708099200,
            min_price="1000000000000",
            max_price="3000000000000",
            median_price="2000000000000",
        )
        trade_record = exchange_pb.TradeRecord(
            timestamp=1708099200,
            price="2000000000000000000",
            quantity="1000000000000000",
        )
        response = exchange_query_pb.QueryMarketVolatilityResponse(
            volatility="0.0001", history_metadata=history_metadata, raw_history=[trade_record]
        )
        exchange_servicer.market_volatility_responses.append(response)

        api = self._api_instance(servicer=exchange_servicer)

        volatility = await api.fetch_market_volatility(
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            trade_grouping_sec=0,
            max_age=28000000,
            include_raw_history=True,
            include_metadata=True,
        )
        expected_volatility = {
            "volatility": response.volatility,
            "historyMetadata": {
                "groupCount": history_metadata.group_count,
                "recordsSampleSize": history_metadata.records_sample_size,
                "mean": history_metadata.mean,
                "twap": history_metadata.twap,
                "firstTimestamp": str(history_metadata.first_timestamp),
                "lastTimestamp": str(history_metadata.last_timestamp),
                "minPrice": history_metadata.min_price,
                "maxPrice": history_metadata.max_price,
                "medianPrice": history_metadata.median_price,
            },
            "rawHistory": [
                {
                    "timestamp": str(trade_record.timestamp),
                    "price": trade_record.price,
                    "quantity": trade_record.quantity,
                }
            ],
        }

        assert volatility == expected_volatility

    @pytest.mark.asyncio
    async def test_fetch_binary_options_markets(
        self,
        exchange_servicer,
    ):
        market = exchange_pb.BinaryOptionsMarket(
            ticker="20250608/USDT",
            oracle_symbol="0x2d9315a88f3019f8efa88dfe9c0f0843712da0bac814461e27733f6b83eb51b3",
            oracle_provider="Pyth",
            oracle_type=9,
            oracle_scale_factor=6,
            expiration_timestamp=1708099200,
            settlement_timestamp=1707099200,
            admin="inj1zlh5sqevkfphtwnu9cul8p89vseme2eqt0snn9",
            quote_denom="peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5",
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            maker_fee_rate="-0.0001",
            taker_fee_rate="0.001",
            relayer_fee_share_rate="400000000000000000",
            status=1,
            min_price_tick_size="100000000000000000000",
            min_quantity_tick_size="1000000000000000",
            settlement_price="2000000000000000000",
            min_notional="5000000000000000000",
            admin_permissions=1,
            quote_decimals=6,
        )
        response = exchange_query_pb.QueryBinaryMarketsResponse(
            markets=[market],
        )
        exchange_servicer.binary_options_markets_responses.append(response)

        api = self._api_instance(servicer=exchange_servicer)

        markets = await api.fetch_binary_options_markets(status="Active")
        expected_markets = {
            "markets": [
                {
                    "ticker": market.ticker,
                    "oracleSymbol": market.oracle_symbol,
                    "oracleProvider": market.oracle_provider,
                    "oracleType": oracle_pb.OracleType.Name(market.oracle_type),
                    "oracleScaleFactor": market.oracle_scale_factor,
                    "expirationTimestamp": str(market.expiration_timestamp),
                    "settlementTimestamp": str(market.settlement_timestamp),
                    "admin": market.admin,
                    "quoteDenom": market.quote_denom,
                    "marketId": market.market_id,
                    "makerFeeRate": market.maker_fee_rate,
                    "takerFeeRate": market.taker_fee_rate,
                    "relayerFeeShareRate": market.relayer_fee_share_rate,
                    "status": exchange_pb.MarketStatus.Name(market.status),
                    "minPriceTickSize": market.min_price_tick_size,
                    "minQuantityTickSize": market.min_quantity_tick_size,
                    "settlementPrice": market.settlement_price,
                    "minNotional": market.min_notional,
                    "adminPermissions": market.admin_permissions,
                    "quoteDecimals": market.quote_decimals,
                },
            ]
        }

        assert markets == expected_markets

    @pytest.mark.asyncio
    async def test_fetch_trader_derivative_conditional_orders(
        self,
        exchange_servicer,
    ):
        order = exchange_query_pb.TrimmedDerivativeConditionalOrder(
            price="2000000000000000000",
            quantity="1000000000000000",
            margin="2000000000000000000000000000000000",
            triggerPrice="3000000000000000000",
            isBuy=True,
            isLimit=True,
            order_hash="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
            cid="order_cid",
        )
        response = exchange_query_pb.QueryTraderDerivativeConditionalOrdersResponse(orders=[order])
        exchange_servicer.trader_derivative_conditional_orders_responses.append(response)

        api = self._api_instance(servicer=exchange_servicer)

        orders = await api.fetch_trader_derivative_conditional_orders(
            subaccount_id="0x5303d92e49a619bb29de8fb6f59c0e7589213cc8000000000000000000000001",
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
        )
        expected_orders = {
            "orders": [
                {
                    "price": order.price,
                    "quantity": order.quantity,
                    "margin": order.margin,
                    "triggerPrice": order.triggerPrice,
                    "isBuy": order.isBuy,
                    "isLimit": order.isLimit,
                    "orderHash": order.order_hash,
                    "cid": order.cid,
                }
            ]
        }

        assert orders == expected_orders

    @pytest.mark.asyncio
    async def test_fetch_market_atomic_execution_fee_multiplier(
        self,
        exchange_servicer,
    ):
        response = exchange_query_pb.QueryMarketAtomicExecutionFeeMultiplierResponse(
            multiplier="100",
        )
        exchange_servicer.market_atomic_execution_fee_multiplier_responses.append(response)

        api = self._api_instance(servicer=exchange_servicer)

        multiplier = await api.fetch_market_atomic_execution_fee_multiplier(
            market_id="0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
        )
        expected_multiplier = {
            "multiplier": response.multiplier,
        }

        assert multiplier == expected_multiplier

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = ChainGrpcExchangeApi(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer

        return api
