import grpc
import pytest
from google.protobuf import any_pb2

from pyinjective.client.chain.grpc.chain_grpc_authz_api import ChainGrpcAuthZApi
from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.cosmos.authz.v1beta1 import authz_pb2, query_pb2 as authz_query
from pyinjective.proto.cosmos.base.query.v1beta1 import pagination_pb2 as pagination_pb
from tests.client.chain.grpc.configurable_authz_query_servicer import ConfigurableAuthZQueryServicer


@pytest.fixture
def authz_servicer():
    return ConfigurableAuthZQueryServicer()


class TestChainGrpcAuthZApi:
    @pytest.mark.asyncio
    async def test_fetch_grants(
        self,
        authz_servicer,
    ):
        authorization = any_pb2.Any(
            type_url="/injective.exchange.v1beta1.CreateSpotMarketOrderAuthz",
            value=(
                "\nB0xf5099d25e6e7e8c6584b67826127b04c9de3e554000000000000000000000000\022"
                "B0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
            ).encode(),
        )

        grant = authz_pb2.Grant(authorization=authorization)

        page_response = pagination_pb.PageResponse(total=1)

        authz_servicer.grants_responses.append(
            authz_query.QueryGrantsResponse(
                grants=[grant],
                pagination=page_response,
            )
        )

        pagination_option = PaginationOption(
            skip=10,
            limit=30,
            reverse=False,
            count_total=True,
        )

        api = self._api_instance(servicer=authz_servicer)

        result_grants = await api.fetch_grants(
            granter="inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku",
            grantee="inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r",
            msg_type_url="/injective.exchange.v1beta1.MsgCreateDerivativeLimitOrder",
            pagination=pagination_option,
        )
        expected_grants = {
            "grants": [
                {
                    "authorization": {
                        "@type": authorization.type_url,
                        "subaccountId": "0xf5099d25e6e7e8c6584b67826127b04c9de3e554000000000000000000000000",
                        "marketIds": ["0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"],
                    }
                }
            ],
            "pagination": {"nextKey": "", "total": str(page_response.total)},
        }

        assert result_grants == expected_grants

    @pytest.mark.asyncio
    async def test_fetch_granter_grants(
        self,
        authz_servicer,
    ):
        authorization = any_pb2.Any(
            type_url="/injective.exchange.v1beta1.CreateSpotMarketOrderAuthz",
            value=(
                "\nB0xf5099d25e6e7e8c6584b67826127b04c9de3e554000000000000000000000000\022"
                "B0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
            ).encode(),
        )

        grant_authorization = authz_pb2.GrantAuthorization(
            granter="inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku",
            grantee="inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r",
            authorization=authorization,
        )

        page_response = pagination_pb.PageResponse(total=1)

        authz_servicer.granter_grants_responses.append(
            authz_query.QueryGranterGrantsResponse(
                grants=[grant_authorization],
                pagination=page_response,
            )
        )

        pagination_option = PaginationOption(
            skip=10,
            limit=30,
            reverse=False,
            count_total=True,
        )

        api = self._api_instance(servicer=authz_servicer)

        result_grants = await api.fetch_granter_grants(
            granter="inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku",
            pagination=pagination_option,
        )
        expected_grants = {
            "grants": [
                {
                    "grantee": grant_authorization.grantee,
                    "granter": grant_authorization.granter,
                    "authorization": {
                        "@type": authorization.type_url,
                        "subaccountId": "0xf5099d25e6e7e8c6584b67826127b04c9de3e554000000000000000000000000",
                        "marketIds": ["0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"],
                    },
                }
            ],
            "pagination": {"nextKey": "", "total": str(page_response.total)},
        }

        assert result_grants == expected_grants

    @pytest.mark.asyncio
    async def test_fetch_grantee_grants(
        self,
        authz_servicer,
    ):
        authorization = any_pb2.Any(
            type_url="/injective.exchange.v1beta1.CreateSpotMarketOrderAuthz",
            value=(
                "\nB0xf5099d25e6e7e8c6584b67826127b04c9de3e554000000000000000000000000\022"
                "B0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
            ).encode(),
        )

        grant_authorization = authz_pb2.GrantAuthorization(
            granter="inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku",
            grantee="inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r",
            authorization=authorization,
        )

        page_response = pagination_pb.PageResponse(total=1)

        authz_servicer.grantee_grants_responses.append(
            authz_query.QueryGranteeGrantsResponse(
                grants=[grant_authorization],
                pagination=page_response,
            )
        )

        pagination_option = PaginationOption(
            skip=10,
            limit=30,
            reverse=False,
            count_total=True,
        )

        api = self._api_instance(servicer=authz_servicer)

        result_grants = await api.fetch_grantee_grants(
            grantee="inj1hkhdaj2a2clmq5jq6mspsggqs32vynpk228q3r",
            pagination=pagination_option,
        )
        expected_grants = {
            "grants": [
                {
                    "grantee": grant_authorization.grantee,
                    "granter": grant_authorization.granter,
                    "authorization": {
                        "@type": authorization.type_url,
                        "subaccountId": "0xf5099d25e6e7e8c6584b67826127b04c9de3e554000000000000000000000000",
                        "marketIds": ["0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"],
                    },
                }
            ],
            "pagination": {"nextKey": "", "total": str(page_response.total)},
        }

        assert result_grants == expected_grants

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = ChainGrpcAuthZApi(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer

        return api
