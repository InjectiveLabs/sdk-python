import asyncio
from decimal import Decimal

from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


def adjusted_margin(
    quantity: Decimal, margin: Decimal, is_long: bool, cumulative_funding_entry: Decimal, cumulative_funding: Decimal
) -> Decimal:
    unrealized_funding_payment = (cumulative_funding - cumulative_funding_entry) * quantity * (-1 if is_long else 1)
    return margin + unrealized_funding_payment


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.mainnet()

    # initialize grpc client
    client = AsyncClient(network)

    positions_per_market = dict()

    positions_dict = await client.fetch_chain_positions()
    liquidable_positions = []

    for position in positions_dict["state"]:
        if position["marketId"] not in positions_per_market:
            positions_per_market[position["marketId"]] = []
        positions_per_market[position["marketId"]].append(position)

    derivative_markets = await client.fetch_chain_derivative_markets(
        status="Active",
        market_ids=list(positions_per_market.keys()),
    )

    for market in derivative_markets["markets"]:
        client_market = (await client.all_derivative_markets())[market["market"]["marketId"]]
        market_mark_price = client_market._from_extended_chain_format(Decimal(market["markPrice"]))
        for position in positions_per_market[client_market.id]:
            is_long = position["position"]["isLong"]
            quantity = client_market._from_extended_chain_format(Decimal(position["position"]["quantity"]))
            entry_price = client_market._from_extended_chain_format(Decimal(position["position"]["entryPrice"]))
            margin = client_market._from_extended_chain_format(Decimal(position["position"]["margin"]))
            cumulative_funding_entry = client_market._from_extended_chain_format(
                Decimal(position["position"]["cumulativeFundingEntry"])
            )
            market_cumulative_funding = client_market._from_extended_chain_format(
                Decimal(market["perpetualInfo"]["fundingInfo"]["cumulativeFunding"])
            )

            adj_margin = adjusted_margin(quantity, margin, is_long, cumulative_funding_entry, market_cumulative_funding)
            adjusted_unit_margin = (adj_margin / quantity) * (-1 if is_long else 1)
            maintenance_margin_ratio = client_market.maintenance_margin_ratio * (-1 if is_long else 1)

            liquidation_price = (entry_price + adjusted_unit_margin) / (Decimal(1) + maintenance_margin_ratio)

            should_be_liquidated = (is_long and market_mark_price <= liquidation_price) or (
                not is_long and market_mark_price >= liquidation_price
            )

            if should_be_liquidated:
                position_side = "Long" if is_long else "Short"
                print(
                    f"{position_side} position for market {client_market.id} and subaccount "
                    f"{position['subaccountId']} should be liquidated (liquidation price: "
                    f"{liquidation_price.normalize()} / mark price: {market_mark_price.normalize()})"
                )
                liquidable_positions.append(position)

    # print(f"\n\n\n")
    # print(json.dumps(liquidable_positions, indent=4))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
