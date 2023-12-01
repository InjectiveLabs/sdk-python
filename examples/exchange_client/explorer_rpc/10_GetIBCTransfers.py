import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    sender = "inj1cll5cv3ezgal30gagkhnq2um6zf6qrmhw4r6c8"
    receiver = "cosmos1usr9g5a4s2qrwl63sdjtrs2qd4a7huh622pg82"
    src_channel = "channel-2"
    src_port = "transfer"
    destination_channel = "channel-30"
    dest_port = "transfer"
    limit = 1
    skip = 10
    pagination = PaginationOption(limit=limit, skip=skip)
    ibc_transfers = await client.fetch_ibc_transfer_txs(
        sender=sender,
        receiver=receiver,
        src_channel=src_channel,
        src_port=src_port,
        dest_channel=destination_channel,
        dest_port=dest_port,
        pagination=pagination,
    )
    print(ibc_transfers)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
