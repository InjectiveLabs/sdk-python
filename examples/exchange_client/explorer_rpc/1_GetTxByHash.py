import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.composer import Composer
from pyinjective.constant import Network

async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.mainnet()
    client = AsyncClient(network, insecure=False)
    composer = Composer(network=network.string())
    tx_hash = "50DD80270052D85835939A393127B5626917007E71A7ABD5205F1A094B976C1B"
    transaction_response = await client.get_tx_by_hash(tx_hash=tx_hash)
    print(transaction_response)

    transaction_messages = composer.UnpackTransactionMessages(transaction=transaction_response.data)
    print(transaction_messages)
    first_message = transaction_messages[0]
    print(first_message)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
