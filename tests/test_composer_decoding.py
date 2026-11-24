import json
from types import SimpleNamespace

import pytest
from google.protobuf import any_pb2, json_format, symbol_database

from pyinjective.composer_v2 import Composer
from pyinjective.proto.cosmos.authz.v1beta1 import tx_pb2 as authz_tx_pb
from pyinjective.proto.cosmos.base.abci.v1beta1 import abci_pb2
from pyinjective.proto.exchange import injective_explorer_rpc_pb2 as explorer_pb
from pyinjective.proto.injective.exchange.v2 import tx_pb2 as exchange_tx_pb
from pyinjective.proto.injective.oracle.v1beta1 import tx_pb2 as oracle_tx_pb


@pytest.fixture(
    params=[
        ("msg_cancel_post_only_mode", {"sender": "inj1test"}),
        (
            "msg_offset_position",
            {
                "sender": "inj1test",
                "subaccount_id": "0x123",
                "market_id": "0x456",
                "offsetting_subaccount_ids": ["0x789"],
            },
        ),
        (
            "msg_create_token_pair",
            {"sender": "inj1test", "bank_denom": "inj", "erc20_address": "0x123"},
        ),
        ("msg_delete_token_pair", {"sender": "inj1test", "bank_denom": "inj"}),
        ("msg_vote", {"proposal_id": 17, "voter": "inj1test", "option": 1}),
        ("msg_auction_claim_voucher", {"sender": "inj1test", "denom": "inj"}),
        ("msg_insurance_claim_voucher", {"sender": "inj1test", "denom": "inj"}),
        ("msg_claim_voucher", {"sender": "inj1test", "denom": "inj"}),
        ("msg_execute_contract", {"sender": "inj1test", "contract": "inj1contract", "msg": "{}"}),
    ],
    ids=lambda case: case[0],
)
def composed_message(request):
    method_name, arguments = request.param
    return getattr(Composer(network="testnet"), method_name)(**arguments)


@pytest.mark.parametrize("legacy", [False, True], ids=["json", "protobuf"])
def test_unpack_composed_transaction_message(composed_message, legacy):
    composer = Composer(network="testnet")
    messages = [
        composed_message,
        composer.msg_send(from_address="inj1sender", to_address="inj1receiver", amount=100, denom="inj"),
    ]
    message_data = [
        {
            "type": "/" + message.DESCRIPTOR.full_name,
            "value": json_format.MessageToDict(message=message, always_print_fields_with_no_presence=True),
        }
        for message in messages
    ]
    transaction = explorer_pb.TxDetailData(messages=json.dumps(message_data).encode())

    if legacy:
        assert Composer.UnpackTransactionMessages(transaction) == messages
    else:
        transaction_data = json_format.MessageToDict(transaction)
        assert Composer.unpack_transaction_messages(transaction_data) == message_data


@pytest.mark.parametrize("legacy", [False, True], ids=["json", "protobuf"])
def test_unpack_composed_message_exec_response(composed_message, legacy):
    response_type = symbol_database.Default().GetSymbol(composed_message.DESCRIPTOR.full_name + "Response")
    response = response_type()
    exec_response = authz_tx_pb.MsgExecResponse(results=[response.SerializeToString()])
    message_type = "/" + composed_message.DESCRIPTOR.full_name

    if legacy:
        assert Composer.UnpackMsgExecResponse(message_type, exec_response) == [response]
    else:
        assert Composer.unpack_msg_exec_response(message_type, json_format.MessageToDict(exec_response)) == [
            json_format.MessageToDict(response, always_print_fields_with_no_presence=True)
        ]


@pytest.mark.parametrize(
    "response",
    [
        exchange_tx_pb.MsgCreateSpotLimitOrderResponse(order_hash="0x123"),
        exchange_tx_pb.MsgCancelPostOnlyModeResponse(),
    ],
    ids=lambda response: response.DESCRIPTOR.name,
)
def test_unpack_exchange_exec_response_by_short_name(response):
    message_name = response.DESCRIPTOR.name.removesuffix("Response")
    exec_response = authz_tx_pb.MsgExecResponse(results=[response.SerializeToString()])

    assert Composer.UnpackMsgExecResponse(message_name, exec_response) == [response]


def test_oracle_response_is_decoded_as_response():
    response = oracle_tx_pb.MsgRelayProviderPricesResponse()
    packed_response = any_pb2.Any()
    packed_response.Pack(response, type_url_prefix="")
    tx_data = abci_pb2.TxMsgData(msg_responses=[packed_response])

    assert Composer.MsgResponses(SimpleNamespace(result=tx_data), simulation=True) == [response]
