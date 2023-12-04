import base64

import grpc
import pytest
from google.protobuf import any_pb2

from pyinjective.core.network import Network
from pyinjective.core.tx.grpc.tx_grpc_api import TxGrpcApi
from pyinjective.proto.cosmos.base.abci.v1beta1 import abci_pb2 as abci_type
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as coin_pb
from pyinjective.proto.cosmos.tx.v1beta1 import service_pb2 as tx_service, tx_pb2
from pyinjective.proto.injective.crypto.v1beta1.ethsecp256k1 import keys_pb2 as keys_pb
from tests.core.tx.grpc.configurable_tx_query_servicer import ConfigurableTxQueryServicer


@pytest.fixture
def tx_servicer():
    return ConfigurableTxQueryServicer()


class TestTxGrpcApi:
    @pytest.mark.asyncio
    async def test_simulate(
        self,
        tx_servicer,
    ):
        gas_info = abci_type.GasInfo(
            gas_wanted=130000,
            gas_used=120000,
        )
        simulation_result = abci_type.Result(log="Result log")

        tx_servicer.simulate_responses.append(
            tx_service.SimulateResponse(
                gas_info=gas_info,
                result=simulation_result,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = TxGrpcApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = tx_servicer

        result_simulate = await api.simulate(tx_bytes="Transaction content".encode())
        expected_simulate = {
            "gasInfo": {"gasUsed": str(gas_info.gas_used), "gasWanted": str(gas_info.gas_wanted)},
            "result": {
                "data": "",
                "events": [],
                "log": simulation_result.log,
                "msgResponses": [],
            },
        }

        assert result_simulate == expected_simulate

    @pytest.mark.asyncio
    async def test_get_tx(
        self,
        tx_servicer,
    ):
        tx_body = tx_pb2.TxBody(
            memo="test memo",
            timeout_height=17518637,
        )

        pub_key = keys_pb.PubKey(key=b"\002\200T< /\340\341IC\260n\372\373\314&\3751A\034HfMk\255[ai\334\3303t\375")
        any_pub_key = any_pb2.Any()
        any_pub_key.Pack(pub_key, type_url_prefix="")

        signer_info = tx_pb2.SignerInfo(
            public_key=any_pub_key,
            sequence=211255,
        )
        fee = tx_pb2.Fee(
            amount=[coin_pb.Coin(denom="inj", amount="988987297011197594664")],
            gas_limit=104757,
        )
        auth_info = tx_pb2.AuthInfo(
            signer_infos=[signer_info],
            fee=fee,
        )
        signature = (
            "\036~\024\202^t\252\346KB\377\333\266jV\030\300\353\340^\021_\227\236hc\010m\316U\314-:kK\0"
            "07\337$K\275\303O\310\007\016\r\305c1\rcl\204L\323T\230\222\373\266\007/\261'"
        ).encode()
        transaction = tx_pb2.Tx(body=tx_body, auth_info=auth_info, signatures=[signature])

        transaction_response = abci_type.TxResponse(
            height=17518608,
            txhash="D265527E3171C47D01D7EC9B839A95F8F794D4E683F26F5564025961C96EFDDA",
            data=(
                "126F0A252F636F736D6F732E617574687A2E763162657461312E4D736745786563526573706F6E736512460A440A42307834"
                "3166303165366232666464336234633036316638343232356661656530333335366462386431376562653736313566613932"
                "32663132363861666434316136"
            ),
        )

        tx_servicer.get_tx_responses.append(tx_service.GetTxResponse(tx=transaction, tx_response=transaction_response))

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = TxGrpcApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = tx_servicer

        result_tx = await api.fetch_tx(hash=transaction_response.txhash)
        expected_tx = {
            "tx": {
                "authInfo": {
                    "fee": {
                        "amount": [{"amount": fee.amount[0].amount, "denom": fee.amount[0].denom}],
                        "gasLimit": str(fee.gas_limit),
                        "granter": "",
                        "payer": "",
                    },
                    "signerInfos": [
                        {
                            "publicKey": {
                                "@type": "/injective.crypto.v1beta1.ethsecp256k1.PubKey",
                                "key": base64.b64encode(pub_key.key).decode(),
                            },
                            "sequence": str(signer_info.sequence),
                        }
                    ],
                },
                "body": {
                    "extensionOptions": [],
                    "memo": tx_body.memo,
                    "messages": [],
                    "nonCriticalExtensionOptions": [],
                    "timeoutHeight": str(tx_body.timeout_height),
                },
                "signatures": [base64.b64encode(signature).decode()],
            },
            "txResponse": {
                "code": 0,
                "codespace": "",
                "data": transaction_response.data,
                "events": [],
                "gasUsed": "0",
                "gasWanted": "0",
                "height": str(transaction_response.height),
                "info": "",
                "logs": [],
                "rawLog": "",
                "timestamp": "",
                "txhash": transaction_response.txhash,
            },
        }

        assert result_tx == expected_tx

    @pytest.mark.asyncio
    async def test_broadcast(
        self,
        tx_servicer,
    ):
        transaction_response = abci_type.TxResponse(
            height=17518608,
            txhash="D265527E3171C47D01D7EC9B839A95F8F794D4E683F26F5564025961C96EFDDA",
            data=(
                "126F0A252F636F736D6F732E617574687A2E763162657461312E4D736745786563526573706F6E736512460A440A42307834"
                "3166303165366232666464336234633036316638343232356661656530333335366462386431376562653736313566613932"
                "32663132363861666434316136"
            ),
        )

        tx_servicer.broadcast_responses.append(
            tx_service.BroadcastTxResponse(
                tx_response=transaction_response,
            )
        )

        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)

        api = TxGrpcApi(channel=channel, metadata_provider=lambda: self._dummy_metadata_provider())
        api._stub = tx_servicer

        result_broadcast = await api.broadcast(
            tx_bytes="Transaction content".encode(),
            mode=tx_service.BroadcastMode.BROADCAST_MODE_SYNC,
        )
        expected_broadcast = {
            "txResponse": {
                "code": 0,
                "codespace": "",
                "data": transaction_response.data,
                "events": [],
                "gasUsed": "0",
                "gasWanted": "0",
                "height": str(transaction_response.height),
                "info": "",
                "logs": [],
                "rawLog": "",
                "timestamp": "",
                "txhash": transaction_response.txhash,
            }
        }

        assert result_broadcast == expected_broadcast

    async def _dummy_metadata_provider(self):
        return None
