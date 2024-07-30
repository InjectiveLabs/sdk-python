import grpc
import pytest

from pyinjective.client.indexer.grpc.indexer_grpc_meta_api import IndexerGrpcMetaApi
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.exchange import injective_meta_rpc_pb2 as exchange_meta_pb
from tests.client.indexer.configurable_meta_query_servicer import ConfigurableMetaQueryServicer


@pytest.fixture
def meta_servicer():
    return ConfigurableMetaQueryServicer()


class TestIndexerGrpcMetaApi:
    @pytest.mark.asyncio
    async def test_fetch_portfolio(
        self,
        meta_servicer,
    ):
        meta_servicer.ping_responses.append(exchange_meta_pb.PingResponse())

        api = self._api_instance(servicer=meta_servicer)

        result_ping = await api.fetch_ping()
        expected_ping = {}

        assert result_ping == expected_ping

    @pytest.mark.asyncio
    async def test_fetch_version(
        self,
        meta_servicer,
    ):
        version = "v1.12.28"
        build = {
            "GoVersion": "go1.20.5",
            "GoArch": "amd64",
        }
        meta_servicer.version_responses.append(
            exchange_meta_pb.VersionResponse(
                version=version,
                build=build,
            )
        )

        api = self._api_instance(servicer=meta_servicer)

        result_version = await api.fetch_version()
        expected_version = {"build": build, "version": version}

        assert result_version == expected_version

    @pytest.mark.asyncio
    async def test_fetch_info(
        self,
        meta_servicer,
    ):
        timestamp = 1698440196320
        server_time = 1698440197744
        version = "v1.12.28"
        build = {
            "GoVersion": "go1.20.5",
            "GoArch": "amd64",
        }
        region = "test region"
        meta_servicer.info_responses.append(
            exchange_meta_pb.InfoResponse(
                timestamp=timestamp, server_time=server_time, version=version, build=build, region=region
            )
        )

        api = self._api_instance(servicer=meta_servicer)

        result_info = await api.fetch_info()
        expected_info = {
            "timestamp": str(timestamp),
            "serverTime": str(server_time),
            "version": version,
            "build": build,
            "region": region,
        }

        assert result_info == expected_info

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = IndexerGrpcMetaApi(channel=channel, cookie_assistant=cookie_assistant)
        api._stub = servicer

        return api
