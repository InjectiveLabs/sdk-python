import asyncio
import json

from pyinjective.composer_v2 import Composer
from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = IndexerClient(network=network)
    composer = Composer(network=network)

    tx_hash = "0F3EBEC1882E1EEAC5B7BDD836E976250F1CD072B79485877CEACCB92ACDDF52"
    transaction_response = await client.fetch_tx_by_tx_hash(tx_hash=tx_hash)
    print("Transaction response:")
    print(f"{json.dumps(transaction_response, indent=2)}\n")

    transaction_messages = composer.unpack_transaction_messages(transaction_data=transaction_response["data"])
    print("Transaction messages:")
    print(f"{json.dumps(transaction_messages, indent=2)}\n")
    first_message = transaction_messages[0]
    print("First message:")
    print(f"{json.dumps(first_message, indent=2)}\n")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
