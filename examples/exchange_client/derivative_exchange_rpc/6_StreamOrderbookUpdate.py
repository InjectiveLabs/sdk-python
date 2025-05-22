import asyncio
from decimal import Decimal
from typing import Any, Dict

from grpc import RpcError

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


def stream_error_processor(exception: RpcError):
    print(f"There was an error listening to derivative orderbook updates ({exception})")


def stream_closed_processor():
    print("The derivative orderbook updates stream has been closed")


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


async def load_orderbook_snapshot(async_client: AsyncClient, orderbook: Orderbook):
    # load the snapshot
    res = await async_client.fetch_derivative_orderbooks_v2(market_ids=[orderbook.market_id], depth=1)
    for snapshot in res["orderbooks"]:
        if snapshot["marketId"] != orderbook.market_id:
            raise Exception("unexpected snapshot")

        orderbook.sequence = int(snapshot["orderbook"]["sequence"])

        for buy in snapshot["orderbook"]["buys"]:
            orderbook.levels["buys"][buy["price"]] = PriceLevel(
                price=Decimal(buy["price"]),
                quantity=Decimal(buy["quantity"]),
                timestamp=int(buy["timestamp"]),
            )
        for sell in snapshot["orderbook"]["sells"]:
            orderbook.levels["sells"][sell["price"]] = PriceLevel(
                price=Decimal(sell["price"]),
                quantity=Decimal(sell["quantity"]),
                timestamp=int(sell["timestamp"]),
            )
        break


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    async_client = AsyncClient(network)

    market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
    orderbook = Orderbook(market_id=market_id)
    updates_queue = asyncio.Queue()
    tasks = []

    async def queue_event(event: Dict[str, Any]):
        await updates_queue.put(event)

    # start getting price levels updates
    task = asyncio.get_event_loop().create_task(
        async_client.listen_derivative_orderbook_updates(
            market_ids=[market_id],
            callback=queue_event,
            on_end_callback=stream_closed_processor,
            on_status_callback=stream_error_processor,
        )
    )
    tasks.append(task)

    # load the snapshot once we are already receiving updates, so we don't miss any
    await load_orderbook_snapshot(async_client=async_client, orderbook=orderbook)

    task = asyncio.get_event_loop().create_task(
        apply_orderbook_update(orderbook=orderbook, updates_queue=updates_queue)
    )
    tasks.append(task)

    await asyncio.sleep(delay=60)
    for task in tasks:
        task.cancel()


async def apply_orderbook_update(orderbook: Orderbook, updates_queue: asyncio.Queue):
    while True:
        updates = await updates_queue.get()
        update = updates["orderbookLevelUpdates"]

        # discard updates older than the snapshot
        if int(update["sequence"]) <= orderbook.sequence:
            return

        print(" * * * * * * * * * * * * * * * * * * *")

        # ensure we have not missed any update
        if int(update["sequence"]) > (orderbook.sequence + 1):
            raise Exception(
                "missing orderbook update events from stream, must restart: {} vs {}".format(
                    update["sequence"], (orderbook.sequence + 1)
                )
            )

        print("updating orderbook with updates at sequence {}".format(update["sequence"]))

        # update orderbook
        orderbook.sequence = int(update["sequence"])
        for direction, levels in {"buys": update["buys"], "sells": update["sells"]}.items():
            for level in levels:
                if level["isActive"]:
                    # upsert level
                    orderbook.levels[direction][level["price"]] = PriceLevel(
                        price=Decimal(level["price"]), quantity=Decimal(level["quantity"]), timestamp=level["timestamp"]
                    )
                else:
                    if level["price"] in orderbook.levels[direction]:
                        del orderbook.levels[direction][level["price"]]

        # sort the level numerically
        buys = sorted(orderbook.levels["buys"].values(), key=lambda x: x.price, reverse=True)
        sells = sorted(orderbook.levels["sells"].values(), key=lambda x: x.price, reverse=True)

        # lowest sell price should be higher than the highest buy price
        if len(buys) > 0 and len(sells) > 0:
            highest_buy = buys[0].price
            lowest_sell = sells[-1].price
            print("Max buy: {} - Min sell: {}".format(highest_buy, lowest_sell))
            if highest_buy >= lowest_sell:
                raise Exception("crossed orderbook, must restart")

        # for the example, print the list of buys and sells orders.
        print("sells")
        for k in sells:
            print(k)
        print("=========")
        print("buys")
        for k in buys:
            print(k)
        print("====================================")


if __name__ == "__main__":
    asyncio.run(main())
