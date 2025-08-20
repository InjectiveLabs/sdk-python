import warnings
from unittest.mock import MagicMock, patch

from pyinjective.core.network import Network


class TestIndexerClientDeprecationWarnings:
    @patch("pyinjective.indexer_client.IndexerGrpcSpotStream")
    @patch("pyinjective.indexer_client.IndexerGrpcPortfolioStream")
    @patch("pyinjective.indexer_client.IndexerGrpcOracleStream")
    @patch("pyinjective.indexer_client.IndexerGrpcMetaStream")
    @patch("pyinjective.indexer_client.IndexerGrpcExplorerStream")
    @patch("pyinjective.indexer_client.IndexerGrpcDerivativeStream")
    @patch("pyinjective.indexer_client.IndexerGrpcAuctionStream")
    @patch("pyinjective.indexer_client.IndexerGrpcAccountStream")
    @patch("pyinjective.indexer_client.IndexerGrpcSpotApi")
    @patch("pyinjective.indexer_client.IndexerGrpcPortfolioApi")
    @patch("pyinjective.indexer_client.IndexerGrpcOracleApi")
    @patch("pyinjective.indexer_client.IndexerGrpcMetaApi")
    @patch("pyinjective.indexer_client.IndexerGrpcInsuranceApi")
    @patch("pyinjective.indexer_client.IndexerGrpcExplorerApi")
    @patch("pyinjective.indexer_client.IndexerGrpcDerivativeApi")
    @patch("pyinjective.indexer_client.IndexerGrpcAuctionApi")
    @patch("pyinjective.indexer_client.IndexerGrpcAccountApi")
    def test_listen_derivative_positions_updates_deprecation_warning(self, *mocks):
        """Test that calling listen_derivative_positions_updates raises a deprecation warning."""
        # Create a mock network to avoid actual network initialization
        mock_network = MagicMock(spec=Network)
        mock_network.exchange_cookie_assistant = MagicMock()
        mock_network.explorer_cookie_assistant = MagicMock()
        mock_network.create_exchange_grpc_channel = MagicMock()
        mock_network.create_explorer_grpc_channel = MagicMock()

        # Import here to avoid early import issues
        from pyinjective.indexer_client import IndexerClient

        # Create IndexerClient instance
        client = IndexerClient(network=mock_network)

        # Mock the derivative_stream_api.stream_positions method to avoid actual streaming
        client.derivative_stream_api.stream_positions = MagicMock()

        # Capture warnings
        with warnings.catch_warnings(record=True) as warning_list:
            warnings.simplefilter("always")  # Ensure all warnings are captured

            # Mock callback function
            mock_callback = MagicMock()

            # Call the deprecated method - this should trigger the deprecation warning
            client.listen_derivative_positions_updates(
                callback=mock_callback, market_ids=["market_1"], subaccount_ids=["subaccount_1"]
            )

            # Find the deprecation warning
            deprecation_warnings = [
                w
                for w in warning_list
                if issubclass(w.category, DeprecationWarning)
                and "This method is deprecated. Use listen_derivative_positions_v2_updates instead" in str(w.message)
            ]

            # Should have exactly one warning
            assert len(deprecation_warnings) == 1

            warning = deprecation_warnings[0]
            # Check warning message contains migration advice
            assert "Use listen_derivative_positions_v2_updates instead" in str(warning.message)
            # Check warning category
            assert warning.category == DeprecationWarning
            # Check stacklevel is working correctly (should point to this test file)
            assert "test_indexer_client_deprecation_warnings.py" in warning.filename

            # Verify the underlying method was still called (functionality preserved)
            client.derivative_stream_api.stream_positions.assert_called_once_with(
                callback=mock_callback,
                on_end_callback=None,
                on_status_callback=None,
                market_ids=["market_1"],
                subaccount_ids=["subaccount_1"],
            )
