import asyncio
import os

import dotenv

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    dotenv.load_dotenv()
    granter = os.getenv("INJECTIVE_GRANTER_PUBLIC_ADDRESS")
    grantee = os.getenv("INJECTIVE_GRANTEE_PUBLIC_ADDRESS")

    network = Network.testnet()
    client = AsyncClient(network)
    msg_type_url = "/injective.exchange.v1beta1.MsgCreateDerivativeLimitOrder"
    authorizations = await client.fetch_grants(granter=granter, grantee=grantee, msg_type_url=msg_type_url)
    print(authorizations)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
