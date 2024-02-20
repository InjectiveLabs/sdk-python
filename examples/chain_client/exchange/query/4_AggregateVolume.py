import asyncio
import os

import dotenv

from pyinjective import PrivateKey
from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    dotenv.load_dotenv()
    configured_private_key = os.getenv("INJECTIVE_PRIVATE_KEY")

    # select network: local, testnet, mainnet
    network = Network.testnet()

    # initialize grpc client
    client = AsyncClient(network)

    # load account
    priv_key = PrivateKey.from_hex(configured_private_key)
    pub_key = priv_key.to_public_key()
    address = pub_key.to_address()

    subaccount_id = address.get_subaccount_id(index=0)

    volume = await client.fetch_aggregate_volume(account=address.to_acc_bech32())
    print(volume)

    volume = await client.fetch_aggregate_volume(account=subaccount_id)
    print(volume)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
