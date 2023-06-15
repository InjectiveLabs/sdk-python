import logging

import pytest
from pyinjective.constant import Network

from pyinjective.async_client import AsyncClient


class TestAsyncClient:

    def test_instance_creation_logs_session_cookie_load_info(self, caplog):
        caplog.set_level(logging.INFO)

        AsyncClient(
            network=Network.local(),
            insecure=False,
        )

        expected_log_message_prefix = "chain session cookie loaded from disk: "
        found_log = next(
            (record for record in caplog.record_tuples if record[2].startswith(expected_log_message_prefix)),
            None,
        )
        assert(found_log is not None)
        assert(found_log[0] == "pyinjective.async_client.AsyncClient")
        assert(found_log[1] == logging.INFO)


    @pytest.mark.asyncio
    async def test_sync_timeout_height_logs_exception(self, caplog):
        client = AsyncClient(
            network=Network.local(),
            insecure=False,
        )

        with caplog.at_level(logging.DEBUG):
            await client.sync_timeout_height()

        expected_log_message_prefix = "error while fetching latest block, setting timeout height to 0: "
        found_log = next(
            (record for record in caplog.record_tuples if record[2].startswith(expected_log_message_prefix)),
            None,
        )
        assert (found_log is not None)
        assert (found_log[0] == "pyinjective.async_client.AsyncClient")
        assert (found_log[1] == logging.DEBUG)

    def test_set_cookie_logs_chain_session_cookie_saved(self, caplog):
        caplog.set_level(logging.INFO)

        client = AsyncClient(
            network=Network.local(),
            insecure=False,
        )

        client.set_cookie(metadata=[("set-cookie", "test-value")], type="chain")

        expected_log_message_prefix = "chain session cookie saved to disk"
        found_log = next(
            (record for record in caplog.record_tuples if record[2].startswith(expected_log_message_prefix)),
            None,
        )
        assert (found_log is not None)
        assert (found_log[0] == "pyinjective.async_client.AsyncClient")
        assert (found_log[1] == logging.INFO)

    @pytest.mark.asyncio
    async def test_get_account_logs_exception(self, caplog):
        client = AsyncClient(
            network=Network.local(),
            insecure=False,
        )

        with caplog.at_level(logging.DEBUG):
            await client.get_account(address="")

        expected_log_message_prefix = "error while fetching sequence and number "
        found_log = next(
            (record for record in caplog.record_tuples if record[2].startswith(expected_log_message_prefix)),
            None,
        )
        assert (found_log is not None)
        assert (found_log[0] == "pyinjective.async_client.AsyncClient")
        assert (found_log[1] == logging.DEBUG)