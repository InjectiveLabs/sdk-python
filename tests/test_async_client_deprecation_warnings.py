from warnings import catch_warnings

import pytest

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


class TestAsyncClientDeprecationWarnings:
    @pytest.mark.asyncio
    async def test_listen_derivative_positions_updates_deprecation(self):
        # Create a mock AsyncClient (you might need to adjust this based on your actual implementation)
        client = AsyncClient(network=Network.local())

        # Expect a DeprecationWarning to be raised
        with catch_warnings(record=True) as captured_warnings:
            # Mock callback and other required parameters
            async def mock_callback(update):
                pass

            # Call the deprecated method
            await client.listen_derivative_positions_updates(
                callback=mock_callback, market_ids=["test_market"], subaccount_ids=["test_subaccount"]
            )

            # Assert that a DeprecationWarning was raised
            assert len(captured_warnings) > 0
            assert issubclass(captured_warnings[-1].category, DeprecationWarning)
            assert "deprecated. Use listen_derivative_positions_v2_updates" in str(captured_warnings[-1].message)
