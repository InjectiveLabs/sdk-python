import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.composer import Composer
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    composer = Composer(network=network.string())
    tx_hash = "0F3EBEC1882E1EEAC5B7BDD836E976250F1CD072B79485877CEACCB92ACDDF52"
    transaction_response = await client.get_tx_by_hash(tx_hash=tx_hash)
    print(transaction_response)

    transaction_messages = composer.UnpackTransactionMessages(transaction=transaction_response.data)
    print(transaction_messages)
    first_message = transaction_messages[0]
    print(first_message)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
