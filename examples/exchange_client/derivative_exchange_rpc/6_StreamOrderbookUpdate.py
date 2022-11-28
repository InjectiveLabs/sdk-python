import asyncio
import logging
from decimal import *

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network


class PriceLevel:
    def __init__(self, price: Decimal, quantity: Decimal, timestamp: int):
        self.price = price
        self.quantity = quantity
        self.timestamp = timestamp

    def __str__(self) -> str:
        return "price: {} | quantity: {} | timestamp: {}".format(self.price, self.quantity, self.timestamp)


class Orderbook:
    def __init__(self, market_id: str):
        self.market_id = market_id
        self.sequence = -1
        self.levels = {"buys": {}, "sells": {}}


async def load_orderbook_snapshot(client: AsyncClient, orderbook: Orderbook):
    # load the snapshot
    snapshots = await client.stream_derivative_orderbook_snapshot(market_ids=[orderbook.market_id])
    async for snapshot in snapshots:
        print(snapshot)
        if snapshot.market_id != orderbook.market_id:
            raise Exception("unexpected snapshot")

        orderbook.sequence = int(snapshot.orderbook.sequence)

        for buy in snapshot.orderbook.buys:
            orderbook.levels["buys"][buy.price] = PriceLevel(
                price=Decimal(buy.price),
                quantity=Decimal(buy.quantity),
                timestamp=buy.timestamp,
            )
        for sell in snapshot.orderbook.sells:
            orderbook.levels["sells"][sell.price] = PriceLevel(
                price=Decimal(sell.price),
                quantity=Decimal(sell.quantity),
                timestamp=sell.timestamp,
            )
        break


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network, insecure=True)

    market_id = "0x4ca0f92fc28be0c9761326016b5a1a2177dd6375558365116b5bdda9abc229ce"
    orderbook = Orderbook(market_id=market_id)

    # start getting price levels updates
    updates = await client.stream_derivative_orderbook_update(market_ids=[market_id])
    first_update = None
    async for update in updates:
        first_update = update.orderbook_level
        break

    # load the snapshot once we are already receiving updates, so we don't miss any
    await load_orderbook_snapshot(client=client, orderbook=orderbook)

    # start consuming updates again to process them
    apply_orderbook_update(orderbook, first_update)
    async for update in updates:
        apply_orderbook_update(orderbook, update.orderbook_level)


def apply_orderbook_update(orderbook: Orderbook, level):
    # discard old updates
    if level.sequence <= orderbook.sequence:
        return

    print(" * * * * * * * * * * * * * * * * * * *")

    # ensure we have not missed any update
    if level.sequence > (orderbook.sequence + 1):
        raise Exception("missing orderbook update events from stream, must restart: {} vs {}".format(
            level.sequence, (orderbook.sequence + 1)))

    # update orderbook
    orderbook.sequence = level.sequence
    level_side = get_level_side(level.is_buy)
    price = Decimal(level.price)
    if level.is_active:
        # upsert level
        orderbook.levels[level_side][price] = PriceLevel(
            price=price,
            quantity=Decimal(level.quantity),
            timestamp=level.updated_at,
        )
    else:
        if price in orderbook.levels[level_side]:
            del orderbook.levels[level_side][price]

    # lowest sell price should be higher than the highest buy price
    buys = orderbook.levels["buys"]
    sells = orderbook.levels["sells"]

    print("Max buy: {} > Min sell: {}".format(max(buys.keys()), min(sells.keys())))
    if len(sells) > 0 and len(buys) > 0 and min(buys.keys()) >= max(sells.keys()):
        raise Exception("crossed orderbook, must restart")

    # for the example, print the list of buys and sells orders.
    print("sells")
    for k in sorted(sells.keys()):
        print(sells[k])
    print("=========")
    print("buys")
    for k in sorted(buys.keys()):
        print(buys[k])
    print("====================================")


def get_level_side(is_buy: bool) -> str:
    if is_buy:
        return "buys"
    return "sells"


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
