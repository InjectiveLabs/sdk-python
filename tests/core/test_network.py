import datetime

import pytest
from grpc.aio import Metadata

from pyinjective.core.network import (
    BareMetalLoadBalancedCookieAssistant,
    DisabledCookieAssistant,
    ExpiringCookieAssistant,
)


class DummyCall:
    def __init__(self, metadata: Metadata):
        self._metadata = metadata

    async def initial_metadata(self):
        return self._metadata


class TestBareMetalLoadBalancedCookieAssistant:
    @pytest.mark.asyncio
    async def test_metadata_access(self):
        assistant = BareMetalLoadBalancedCookieAssistant()

        assert assistant.metadata() == Metadata()

        response_cookie = "lb=205989dfdbf02c2b4b9ed656ff8a081cb146d66797f69eefb4aee61ad5f13d4e; Path=/"
        metadata = Metadata(
            ("alt-svc", 'h3=":443"; ma=2592000'),
            ("server", "Caddy"),
            ("set-cookie", response_cookie),
            ("x-cosmos-block-height", "23624674"),
            ("date", "Mon, 18 Mar 2024 18:09:42 GMT"),
        )

        grpc_call = DummyCall(metadata=metadata)
        await assistant.process_response_metadata(grpc_call=grpc_call)

        assert assistant.metadata() == Metadata(("cookie", response_cookie))


class TestExpiringCookieAssistant:
    @pytest.mark.asyncio
    async def test_cookie_expiration(self):
        time_format = "%a, %d-%b-%Y %H:%M:%S %Z"
        gmt_timezone = datetime.timezone(offset=datetime.timedelta(seconds=0), name="GMT")

        assistant = ExpiringCookieAssistant(
            expiration_time_keys_sequence=["grpc-cookie", "expires"],
            time_format=time_format,
        )

        future_time = datetime.datetime.now(tz=gmt_timezone) + datetime.timedelta(hours=1)
        formatted_time = future_time.strftime(time_format)
        cookie_value = (
            f"grpc-cookie=bb3a543cef4d9182587375c26556c15f; Expires={formatted_time};"
            f" Max-Age=172800; Path=/; Secure; HttpOnly"
        )

        metadata = Metadata(("set-cookie", cookie_value))
        grpc_call = DummyCall(metadata=metadata)

        await assistant.process_response_metadata(grpc_call=grpc_call)

        assert assistant.cookie() == cookie_value

        past_time = datetime.datetime.now(tz=gmt_timezone) + datetime.timedelta(hours=-1)
        formatted_time = past_time.strftime(time_format)
        cookie_value = (
            f"grpc-cookie=bb3a543cef4d9182587375c26556c15f; Expires={formatted_time};"
            f" Max-Age=172800; Path=/; Secure; HttpOnly"
        )

        metadata = Metadata(("set-cookie", cookie_value))
        grpc_call = DummyCall(metadata=metadata)

        await assistant.process_response_metadata(grpc_call=grpc_call)

        assert assistant.cookie() is None

    def test_instance_creation_for_kubernetes_server(self):
        assistant = ExpiringCookieAssistant.for_kubernetes_public_server()

        assert ["grpc-cookie", "expires"] == assistant._expiration_time_keys_sequence
        assert "%a, %d-%b-%Y %H:%M:%S %Z" == assistant._time_format


class TestDisabledCookieAssistant:
    @pytest.mark.asyncio
    async def test_metadata_access(self):
        assistant = DisabledCookieAssistant()

        assert assistant.metadata() == Metadata()
