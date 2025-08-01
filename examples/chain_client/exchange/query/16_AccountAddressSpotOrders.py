import asyncio
import os

import dotenv

from pyinjective import PrivateKey
from pyinjective.async_client_v2 import AsyncClient
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

    orders = await client.fetch_chain_account_address_spot_orders(
        market_id="0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe",
        account_address=address.to_acc_bech32(),
    )
    print(orders)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
