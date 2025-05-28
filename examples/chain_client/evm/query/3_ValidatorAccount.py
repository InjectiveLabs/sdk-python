import asyncio
import json
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

    cons_address = "injvalcons1h5u937etuat5hnr2s34yaaalfpkkscl5ndadqm"
    result = await client.fetch_evm_validator_account(cons_address=cons_address)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
