import asyncio
import json

from pyinjective.client.model.pagination import PaginationOption
from pyinjective.composer_v2 import Composer
from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = IndexerClient(network=network)
    composer = Composer(network=network)

    address = "inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex"
    message_type = "cosmos.bank.v1beta1.MsgSend"
    limit = 2
    pagination = PaginationOption(limit=limit)
    transactions_response = await client.fetch_account_txs(
        address=address,
        message_type=message_type,
        pagination=pagination,
    )
    print("Transactions response:")
    print(f"{json.dumps(transactions_response, indent=2)}\n")
    first_transaction_messages = composer.unpack_transaction_messages(transaction_data=transactions_response["data"][0])
    print("First transaction messages:")
    print(f"{json.dumps(first_transaction_messages, indent=2)}\n")
    first_message = first_transaction_messages[0]
    print("First message:")
    print(f"{json.dumps(first_message, indent=2)}\n")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
