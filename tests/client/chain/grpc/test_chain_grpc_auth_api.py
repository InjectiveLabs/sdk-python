import base64

import grpc
import pytest
from google.protobuf import any_pb2

from pyinjective.client.chain.grpc.chain_grpc_auth_api import ChainGrpcAuthApi
from pyinjective.client.model import PaginationOption
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.cosmos.auth.v1beta1 import auth_pb2 as auth_pb, query_pb2 as auth_query_pb
from pyinjective.proto.cosmos.base.query.v1beta1 import pagination_pb2 as pagination_pb
from pyinjective.proto.injective.crypto.v1beta1.ethsecp256k1 import keys_pb2 as keys_pb
from pyinjective.proto.injective.types.v1beta1 import account_pb2 as account_pb
from tests.client.chain.grpc.configurable_auth_query_servicer import ConfigurableAuthQueryServicer


@pytest.fixture
def auth_servicer():
    return ConfigurableAuthQueryServicer()


class TestChainGrpcAuthApi:
    @pytest.mark.asyncio
    async def test_fetch_module_params(
        self,
        auth_servicer,
    ):
        params = auth_pb.Params(
            max_memo_characters=256,
            tx_sig_limit=7,
            tx_size_cost_per_byte=10,
            sig_verify_cost_ed25519=590,
            sig_verify_cost_secp256k1=1000,
        )
        auth_servicer.auth_params.append(auth_query_pb.QueryParamsResponse(params=params))

        api = self._api_instance(servicer=auth_servicer)

        module_params = await api.fetch_module_params()
        expected_params = {
            "params": {
                "maxMemoCharacters": "256",
                "sigVerifyCostEd25519": "590",
                "sigVerifyCostSecp256k1": "1000",
                "txSigLimit": "7",
                "txSizeCostPerByte": "10",
            }
        }

        assert expected_params == module_params

    @pytest.mark.asyncio
    async def test_fetch_account(
        self,
        auth_servicer,
    ):
        pub_key = keys_pb.PubKey(key=b"\002\200T< /\340\341IC\260n\372\373\314&\3751A\034HfMk\255[ai\334\3303t\375")
        any_pub_key = any_pb2.Any()
        any_pub_key.Pack(pub_key, type_url_prefix="")

        base_account = auth_pb.BaseAccount(
            address="inj1knhahceyp57j5x7xh69p7utegnnnfgxavmahjr",
            pub_key=any_pub_key,
            account_number=39,
            sequence=697457,
        )
        account = account_pb.EthAccount(
            base_account=base_account,
            code_hash=b"\305\322F\001\206\367#<\222~}\262\334\307\003\300\345\000\266S\312\202';{"
            b"\372\330\004]\205\244p",
        )

        any_account = any_pb2.Any()
        any_account.Pack(account, type_url_prefix="")
        auth_servicer.account_responses.append(auth_query_pb.QueryAccountResponse(account=any_account))

        api = self._api_instance(servicer=auth_servicer)

        response_account = await api.fetch_account(address="inj1knhahceyp57j5x7xh69p7utegnnnfgxavmahjr")
        expected_account = {
            "account": {
                "@type": "/injective.types.v1beta1.EthAccount",
                "baseAccount": {
                    "accountNumber": str(base_account.account_number),
                    "address": base_account.address,
                    "pubKey": {
                        "@type": "/injective.crypto.v1beta1.ethsecp256k1.PubKey",
                        "key": base64.b64encode(pub_key.key).decode(),
                    },
                    "sequence": str(base_account.sequence),
                },
                "codeHash": base64.b64encode(account.code_hash).decode(),
            }
        }

        assert expected_account == response_account

    @pytest.mark.asyncio
    async def test_fetch_accounts(
        self,
        auth_servicer,
    ):
        pub_key = keys_pb.PubKey(key=b"\002\200T< /\340\341IC\260n\372\373\314&\3751A\034HfMk\255[ai\334\3303t\375")
        any_pub_key = any_pb2.Any()
        any_pub_key.Pack(pub_key, type_url_prefix="")

        base_account = auth_pb.BaseAccount(
            address="inj1knhahceyp57j5x7xh69p7utegnnnfgxavmahjr",
            pub_key=any_pub_key,
            account_number=39,
            sequence=697457,
        )
        account = account_pb.EthAccount(
            base_account=base_account,
            code_hash=b"\305\322F\001\206\367#<\222~}\262\334\307\003\300\345\000\266S\312\202';{"
            b"\372\330\004]\205\244p",
        )

        result_pagination = pagination_pb.PageResponse(
            next_key=b"\001\032\264\007Z\224$]\377s8\343\004-\265\267\314?B\341",
            total=16036,
        )

        any_account = any_pb2.Any()
        any_account.Pack(account, type_url_prefix="")
        auth_servicer.accounts_responses.append(
            auth_query_pb.QueryAccountsResponse(
                accounts=[any_account],
                pagination=result_pagination,
            )
        )

        api = self._api_instance(servicer=auth_servicer)

        pagination_option = PaginationOption(
            encoded_page_key="011ab4075a94245dff7338e3042db5b7cc3f42e1",
            skip=10,
            limit=30,
            reverse=False,
            count_total=True,
        )

        response = await api.fetch_accounts(pagination_option=pagination_option)
        response_accounts = response["accounts"]
        response_pagination = response["pagination"]

        assert 1 == len(response_accounts)

        response_account = response_accounts[0]

        assert account.code_hash == base64.b64decode(response_account["codeHash"])
        assert base_account.address == response_account["baseAccount"]["address"]
        assert any_pub_key.type_url == response_account["baseAccount"]["pubKey"]["@type"]
        assert pub_key.key == base64.b64decode(response_account["baseAccount"]["pubKey"]["key"])
        assert base_account.account_number == int(response_account["baseAccount"]["accountNumber"])
        assert base_account.sequence == int(response_account["baseAccount"]["sequence"])

        assert result_pagination.next_key == base64.b64decode(response_pagination["nextKey"])
        assert result_pagination.total == int(response_pagination["total"])

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = ChainGrpcAuthApi(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer

        return api
