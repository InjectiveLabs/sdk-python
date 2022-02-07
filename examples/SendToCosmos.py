import json
import requests

import asyncio
import logging

from pyinjective.constant import Network
from pyinjective.composer import Composer as ProtoMsgComposer

import importlib.resources as pkg_resources
import pyinjective

async def main() -> None:
    # select network: testnet, mainnet
    network = Network.testnet()
    composer = ProtoMsgComposer(network=network.string())

    private_key = "f9db9bf330e23cb7839039e944adef6e9df447b90b503d5b4464c90bea9022f3"
    ethereum_endpoint = "https://kovan.infura.io/v3/c518f454950e48aeab12161c49f26e30"

    maxFeePerGas_Gwei = 4
    maxPriorityFeePerGas_Gwei = 4

    token_contract = "0x36b3d7ace7201e28040eff30e815290d7b37ffad"
    receiver = "inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku"
    amount = 1

    import_peggo = pkg_resources.read_text(pyinjective, 'Peggo_ABI.json')
    peggo_abi = json.loads(import_peggo)

    composer.SendToCosmos(ethereum_endpoint=ethereum_endpoint, private_key=private_key, token_contract=token_contract,
                 receiver=receiver, amount=amount, maxFeePerGas=maxFeePerGas_Gwei, maxPriorityFeePerGas=maxPriorityFeePerGas_Gwei, peggo_abi=peggo_abi)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())