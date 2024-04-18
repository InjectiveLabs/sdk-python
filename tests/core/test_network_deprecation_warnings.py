from warnings import catch_warnings

from pyinjective.core.network import DisabledCookieAssistant, Network


class TestNetworkDeprecationWarnings:
    def test_use_secure_connection_parameter_deprecation_warning(self):
        with catch_warnings(record=True) as all_warnings:
            Network(
                lcd_endpoint="lcd_endpoint",
                tm_websocket_endpoint="tm_websocket_endpoint",
                grpc_endpoint="grpc_endpoint",
                grpc_exchange_endpoint="grpc_exchange_endpoint",
                grpc_explorer_endpoint="grpc_explorer_endpoint",
                chain_stream_endpoint="chain_stream_endpoint",
                chain_id="chain_id",
                fee_denom="fee_denom",
                env="env",
                chain_cookie_assistant=DisabledCookieAssistant(),
                exchange_cookie_assistant=DisabledCookieAssistant(),
                explorer_cookie_assistant=DisabledCookieAssistant(),
                use_secure_connection=True,
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "use_secure_connection parameter in Network is no longer used and will be deprecated"
        )

    def test_use_secure_connection_parameter_in_custom_network_deprecation_warning(self):
        with catch_warnings(record=True) as all_warnings:
            Network.custom(
                lcd_endpoint="lcd_endpoint",
                tm_websocket_endpoint="tm_websocket_endpoint",
                grpc_endpoint="grpc_endpoint",
                grpc_exchange_endpoint="grpc_exchange_endpoint",
                grpc_explorer_endpoint="grpc_explorer_endpoint",
                chain_stream_endpoint="chain_stream_endpoint",
                chain_id="chain_id",
                env="env",
                chain_cookie_assistant=DisabledCookieAssistant(),
                exchange_cookie_assistant=DisabledCookieAssistant(),
                explorer_cookie_assistant=DisabledCookieAssistant(),
                use_secure_connection=True,
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "use_secure_connection parameter in Network is no longer used and will be deprecated"
        )
