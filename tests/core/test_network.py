import pytest

from pyinjective.core.network import BareMetalLoadBalancedCookieAssistant, KubernetesLoadBalancedCookieAssistant


class TestBareMetalLoadBalancedCookieAssistant:
    @pytest.mark.asyncio
    async def test_chain_metadata(self):
        assistant = BareMetalLoadBalancedCookieAssistant()
        dummy_metadata = [("set-cookie", "expected_cookie")]

        async def dummy_metadata_provider():
            return dummy_metadata

        metadata = await assistant.chain_metadata(metadata_query_provider=dummy_metadata_provider)
        expected_metadata = (("cookie", "expected_cookie"),)

        assert expected_metadata == metadata

    @pytest.mark.asyncio
    async def test_chain_metadata_fails_when_cookie_info_not_included_in_server_response(self):
        assistant = BareMetalLoadBalancedCookieAssistant()
        dummy_metadata = [("invalid_key", "invalid_value")]

        async def dummy_metadata_provider():
            return dummy_metadata

        with pytest.raises(RuntimeError, match=f"Error fetching chain cookie ({dummy_metadata})"):
            await assistant.chain_metadata(metadata_query_provider=dummy_metadata_provider)

    @pytest.mark.asyncio
    async def test_exchange_metadata(self):
        assistant = BareMetalLoadBalancedCookieAssistant()
        dummy_metadata = [("set-cookie", "expected_cookie")]

        async def dummy_metadata_provider():
            return dummy_metadata

        metadata = await assistant.exchange_metadata(metadata_query_provider=dummy_metadata_provider)
        expected_metadata = (("cookie", "expected_cookie"),)

        assert expected_metadata == metadata

    @pytest.mark.asyncio
    async def test_exchange_metadata_is_none_when_cookie_info_not_included_in_server_response(self):
        assistant = BareMetalLoadBalancedCookieAssistant()
        dummy_metadata = [("invalid_key", "invalid_value")]

        async def dummy_metadata_provider():
            return dummy_metadata

        metadata = await assistant.exchange_metadata(metadata_query_provider=dummy_metadata_provider)

        assert metadata is None


class TestKubernetesLoadBalancedCookieAssistant:
    @pytest.mark.asyncio
    async def test_chain_metadata(self):
        assistant = KubernetesLoadBalancedCookieAssistant()
        dummy_metadata = [("set-cookie", "expected_cookie")]

        async def dummy_metadata_provider():
            return dummy_metadata

        metadata = await assistant.chain_metadata(metadata_query_provider=dummy_metadata_provider)
        expected_metadata = (("cookie", "expected_cookie"),)

        assert expected_metadata == metadata

    @pytest.mark.asyncio
    async def test_chain_metadata_fails_when_cookie_info_not_included_in_server_response(self):
        assistant = KubernetesLoadBalancedCookieAssistant()
        dummy_metadata = [("invalid_key", "invalid_value")]

        async def dummy_metadata_provider():
            return dummy_metadata

        with pytest.raises(RuntimeError, match=f"Error fetching chain cookie ({dummy_metadata})"):
            await assistant.chain_metadata(metadata_query_provider=dummy_metadata_provider)

    @pytest.mark.asyncio
    async def test_exchange_metadata(self):
        assistant = KubernetesLoadBalancedCookieAssistant()
        dummy_metadata = [("set-cookie", "expected_cookie")]

        async def dummy_metadata_provider():
            return dummy_metadata

        metadata = await assistant.exchange_metadata(metadata_query_provider=dummy_metadata_provider)
        expected_metadata = (("cookie", "expected_cookie"),)

        assert expected_metadata == metadata

    @pytest.mark.asyncio
    async def test_exchange_metadata_is_none_when_cookie_info_not_included_in_server_response(self):
        assistant = KubernetesLoadBalancedCookieAssistant()
        dummy_metadata = [("invalid_key", "invalid_value")]

        async def dummy_metadata_provider():
            return dummy_metadata

        metadata = await assistant.exchange_metadata(metadata_query_provider=dummy_metadata_provider)

        assert metadata is None
