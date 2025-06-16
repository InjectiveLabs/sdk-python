import asyncio
import json
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

    erc20_address = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
    result = await client.fetch_erc20_token_pair_by_erc20_address(erc20_address=erc20_address)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
