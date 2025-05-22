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

    volume = await client.fetch_aggregate_volumes_v2(
        accounts=[address.to_acc_bech32()],
        market_ids=["0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"],
    )
    print(volume)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
