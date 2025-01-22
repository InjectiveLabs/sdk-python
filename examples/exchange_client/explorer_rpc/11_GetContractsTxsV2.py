import asyncio
import time

from pyinjective.async_client import AsyncClient
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network


async def main() -> None:
    # Select network: local, testnet, mainnet, or custom
    network = Network.testnet()

    # Initialize client
    client = AsyncClient(network)

    try:
        # Example parameters for fetching contract transactions
        address = "inj1ady3s7whq30l4fx8sj3x6muv5mx4dfdlcpv8n7"  # Replace with actual contract address

        # Optional pagination and filtering parameters
        pagination = PaginationOption(
            limit=10,
            start_time=int((time.time() - 100) * 1000),
            end_time=int(time.time() * 1000),
        )

        # Fetch contract transactions V2
        response = await client.fetch_contract_txs_v2(address=address, height=60_000_000, pagination=pagination)

        # Print the results
        print("Contract Transactions V2:")
        print("Total Transactions:", len(response["data"]))

        for tx in response["data"]:
            print("\nTransaction Details:")
            print("ID:", tx["id"])
            print("Block Number:", tx["blockNumber"])
            print("Timestamp:", tx["blockTimestamp"])
            print("Hash:", tx["hash"])
            print("Tx Number:", tx["txNumber"])

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
