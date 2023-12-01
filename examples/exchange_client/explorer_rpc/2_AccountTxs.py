import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.composer import Composer
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    composer = Composer(network=network.string())
    address = "inj1phd706jqzd9wznkk5hgsfkrc8jqxv0kmlj0kex"
    message_type = "cosmos.bank.v1beta1.MsgSend"
    limit = 2
    pagination = PaginationOption(limit=limit)
    transactions_response = await client.fetch_account_txs(
        address=address,
        message_type=message_type,
        pagination=pagination,
    )
    print(transactions_response)
    first_transaction_messages = composer.unpack_transaction_messages(transaction_data=transactions_response["data"][0])
    print(first_transaction_messages)
    first_message = first_transaction_messages[0]
    print(first_message)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
