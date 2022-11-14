import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    granter = "inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku"
    grantee = "inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r"
    msg_type_url = "/injective.exchange.v1beta1.MsgCreateDerivativeLimitOrder"
    authorizations = await client.get_grants(granter=granter, grantee=grantee, msg_type_url=msg_type_url)
    print(authorizations)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())