import base64

import grpc
import pytest

from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.core.tx.grpc.ibc_transfer_grpc_api import IBCTransferGrpcApi
from pyinjective.proto.cosmos.base.query.v1beta1 import pagination_pb2 as pagination_pb
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as coin_pb
from pyinjective.proto.ibc.applications.transfer.v1 import query_pb2 as ibc_transfer_query, transfer_pb2 as ibc_transfer
from tests.core.tx.grpc.configurable_ibc_transfer_query_servicer import ConfigurableIBCTransferQueryServicer


@pytest.fixture
def ibc_transfer_servicer():
    return ConfigurableIBCTransferQueryServicer()


class TestTxGrpcApi:
    @pytest.mark.asyncio
    async def test_fetch_params(
        self,
        ibc_transfer_servicer,
    ):
        params = ibc_transfer.Params(
            send_enabled=True,
            receive_enabled=False,
        )

        ibc_transfer_servicer.params_responses.append(
            ibc_transfer_query.QueryParamsResponse(
                params=params,
            )
        )

        api = self._api_instance(servicer=ibc_transfer_servicer)

        result_params = await api.fetch_params()
        expected_params = {"params": {"sendEnabled": params.send_enabled, "receiveEnabled": params.receive_enabled}}

        assert result_params == expected_params

    @pytest.mark.asyncio
    async def test_fetch_denom_trace(
        self,
        ibc_transfer_servicer,
    ):
        denom_trace = ibc_transfer.DenomTrace(
            path="transfer/channel-126",
            base_denom="uluna",
        )

        ibc_transfer_servicer.denom_trace_responses.append(
            ibc_transfer_query.QueryDenomTraceResponse(
                denom_trace=denom_trace,
            )
        )

        api = self._api_instance(servicer=ibc_transfer_servicer)

        result_trace = await api.fetch_denom_trace(hash=denom_trace.base_denom)
        expected_trace = {
            "denomTrace": {
                "path": denom_trace.path,
                "baseDenom": denom_trace.base_denom,
            }
        }

        assert result_trace == expected_trace

    @pytest.mark.asyncio
    async def test_fetch_denom_traces(
        self,
        ibc_transfer_servicer,
    ):
        denom_trace = ibc_transfer.DenomTrace(
            path="transfer/channel-126",
            base_denom="uluna",
        )
        result_pagination = pagination_pb.PageResponse(
            next_key=b"\001\032\264\007Z\224$]\377s8\343\004-\265\267\314?B\341",
            total=16036,
        )

        ibc_transfer_servicer.denom_traces_responses.append(
            ibc_transfer_query.QueryDenomTracesResponse(
                denom_traces=[denom_trace],
                pagination=result_pagination,
            )
        )

        api = self._api_instance(servicer=ibc_transfer_servicer)

        pagination_option = PaginationOption(
            skip=10,
            limit=30,
            reverse=False,
            count_total=True,
        )

        result_traces = await api.fetch_denom_traces(pagination=pagination_option)
        expected_traces = {
            "denomTraces": [
                {
                    "path": denom_trace.path,
                    "baseDenom": denom_trace.base_denom,
                }
            ],
            "pagination": {
                "nextKey": base64.b64encode(result_pagination.next_key).decode(),
                "total": str(result_pagination.total),
            },
        }

        assert result_traces == expected_traces

    @pytest.mark.asyncio
    async def test_fetch_denom_hash(
        self,
        ibc_transfer_servicer,
    ):
        denom_hash = "97498452BF27CC90656FD7D6EFDA287FA2BFFFF3E84691C84CB9E0451F6DF0A4"

        ibc_transfer_servicer.denom_hash_responses.append(
            ibc_transfer_query.QueryDenomHashResponse(
                hash=denom_hash,
            )
        )

        api = self._api_instance(servicer=ibc_transfer_servicer)

        result_hash = await api.fetch_denom_hash(trace="transfer/channel-126/uluna")
        expected_hash = {"hash": denom_hash}

        assert result_hash == expected_hash

    @pytest.mark.asyncio
    async def test_fetch_escrow_address(
        self,
        ibc_transfer_servicer,
    ):
        address = "inj1w8ent9jwwqy2d5s8grq6muk2hqa6kj2863m3mg"

        ibc_transfer_servicer.escrow_address_responses.append(
            ibc_transfer_query.QueryEscrowAddressResponse(
                escrow_address=address,
            )
        )

        api = self._api_instance(servicer=ibc_transfer_servicer)

        result_escrow = await api.fetch_escrow_address(port_id="port", channel_id="channel")
        expected_escrow = {"escrowAddress": address}

        assert result_escrow == expected_escrow

    @pytest.mark.asyncio
    async def test_fetch_total_escrow_for_denom(
        self,
        ibc_transfer_servicer,
    ):
        coin = coin_pb.Coin(denom="inj", amount="988987297011197594664")

        ibc_transfer_servicer.total_escrow_for_denom_responses.append(
            ibc_transfer_query.QueryTotalEscrowForDenomResponse(
                amount=coin,
            )
        )

        api = self._api_instance(servicer=ibc_transfer_servicer)

        result_escrow = await api.fetch_total_escrow_for_denom(denom="inj")
        expected_escrow = {
            "amount": {
                "denom": coin.denom,
                "amount": coin.amount,
            }
        }

        assert result_escrow == expected_escrow

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = IBCTransferGrpcApi(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer

        return api
