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
    await client.fetch_account(address.to_acc_bech32())

    subaccount_id = address.get_subaccount_id(index=0)

    orders = await client.fetch_chain_spot_orders_by_hashes(
        market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
        subaccount_id=subaccount_id,
        order_hashes=["0x57a01cd26f1e2080860af3264e865d7c9c034a701e30946d01c1dc7a303cf2c1"],
    )
    print(orders)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
