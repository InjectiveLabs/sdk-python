import warnings
from unittest.mock import MagicMock, patch

from pyinjective.core.network import Network


class TestAsyncClientDeprecationWarnings:
    @patch("pyinjective.async_client.asyncio.get_event_loop")
    @patch("pyinjective.async_client.ChainGrpcChainStream")
    @patch("pyinjective.async_client.ChainGrpcExchangeApi")
    @patch("pyinjective.async_client.ChainGrpcDistributionApi")
    @patch("pyinjective.async_client.ChainGrpcAuthZApi")
    @patch("pyinjective.async_client.ChainGrpcAuthApi")
    @patch("pyinjective.async_client.ChainGrpcBankApi")
    @patch("pyinjective.async_client.IndexerClient")
    def test_async_client_deprecation_warning(self, *mocks):
        """Test that creating an AsyncClient instance raises a deprecation warning with correct details."""
        # Create a mock network to avoid actual network initialization
        mock_network = MagicMock(spec=Network)
        mock_network.chain_cookie_assistant = MagicMock()
        mock_network.create_chain_grpc_channel = MagicMock()
        mock_network.create_chain_stream_grpc_channel = MagicMock()
        mock_network.official_tokens_list_url = "https://example.com/tokens.json"

        # Import here to avoid early import issues
        from pyinjective.async_client import AsyncClient

        # Capture warnings
        with warnings.catch_warnings(record=True) as warning_list:
            warnings.simplefilter("always")  # Ensure all warnings are captured

            # Create AsyncClient instance - this should trigger the deprecation warning
            client = AsyncClient(network=mock_network)

            # Find the AsyncClient deprecation warning
            async_client_warnings = [
                w
                for w in warning_list
                if issubclass(w.category, DeprecationWarning)
                and "AsyncClient from pyinjective.async_client is deprecated" in str(w.message)
            ]

            # Should have exactly one warning
            assert len(async_client_warnings) == 1

            warning = async_client_warnings[0]
            # Check warning message contains migration advice
            assert "Please use AsyncClient from pyinjective.async_client_v2 instead" in str(warning.message)
            # Check warning category
            assert warning.category == DeprecationWarning
            # Check stacklevel is working correctly (should point to this test file)
            assert "test_async_client_deprecation_warnings.py" in warning.filename

            # Verify the client was still created successfully
            assert client is not None
            assert hasattr(client, "network")
            assert client.network == mock_network
