import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    address = "inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex"
    type = "cosmos.bank.v1beta1.MsgSend"
    account = await client.get_account_txs(address=address, type=type)
    print(account)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
