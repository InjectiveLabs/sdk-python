import json
import requests

import asyncio
import logging

from pyinjective.constant import Network
from pyinjective.sendtocosmos import Peggo

import importlib.resources as pkg_resources
import pyinjective

async def main() -> None:
    # select network: testnet, mainnet
    network = Network.testnet()
    peggo_composer = Peggo(network=network.string())

    private_key = "5d386fbdbf11f1141010f81a46b40f94887367562bd33b452bbaa6ce1cd1381e"
    ethereum_endpoint = "https://eth-goerli.g.alchemy.com/v2/q-7JVv4mTfsNh1y_djKkKn3maRBGILLL"

    maxFeePerGas_Gwei = 4
    maxPriorityFeePerGas_Gwei = 4

    token_contract = "0xBe8d71D26525440A03311cc7fa372262c5354A3c"
    receiver = "inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku"
    amount = 1

    data = '{"@type": "/injective.exchange.v1beta1.MsgDeposit","sender": "inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku","subaccountId": "0xaf79152ac5df276d9a8e1e2e22822f9713474902000000000000000000000000","amount": {"denom": "inj","amount": "1000000000000000000"}}'

    import_peggo = pkg_resources.read_text(pyinjective, 'Peggo_ABI.json')
    peggo_abi = json.loads(import_peggo)

    peggo_composer.sendToInjective(ethereum_endpoint=ethereum_endpoint, private_key=private_key, token_contract=token_contract,
                 receiver=receiver, amount=amount, maxFeePerGas=maxFeePerGas_Gwei, maxPriorityFeePerGas=maxPriorityFeePerGas_Gwei, data=data, peggo_abi=peggo_abi)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
