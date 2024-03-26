import datetime
from abc import ABC, abstractmethod
from http.cookies import SimpleCookie
from typing import List, Optional

from grpc.aio import Call, Metadata


class CookieAssistant(ABC):
    @abstractmethod
    def cookie(self) -> Optional[str]:
        ...

    @abstractmethod
    async def process_response_metadata(self, grpc_call: Call):
        ...

    def metadata(self) -> Metadata:
        cookie = self.cookie()
        metadata = Metadata()
        if cookie is not None and cookie != "":
            metadata.add("cookie", cookie)
        return metadata


class BareMetalLoadBalancedCookieAssistant(CookieAssistant):
    def __init__(self):
        self._cookie: Optional[str] = None

    def cookie(self) -> Optional[str]:
        self._check_cookie_expiration()

        return self._cookie

    async def process_response_metadata(self, grpc_call: Call):
        metadata = await grpc_call.initial_metadata()
        if "set-cookie" in metadata:
            self._cookie = metadata["set-cookie"]

    def _check_cookie_expiration(self):
        if self._is_cookie_expired(cookie_data=self._cookie):
            self._cookie = None

    def _is_cookie_expired(self, cookie_data: str) -> bool:
        # The cookies for these nodes do not expire
        return False


class ExpiringCookieAssistant(CookieAssistant):
    def __init__(self, expiration_time_keys_sequence: List[str], time_format: str):
        self._cookie: Optional[str] = None
        self._expiration_time_keys_sequence = expiration_time_keys_sequence
        self._time_format = time_format

    @classmethod
    def for_kubernetes_public_server(cls):
        return cls(
            expiration_time_keys_sequence=["grpc-cookie", "expires"],
            time_format="%a, %d-%b-%Y %H:%M:%S %Z",
        )

    def cookie(self) -> Optional[str]:
        self._check_cookie_expiration()

        return self._cookie

    async def process_response_metadata(self, grpc_call: Call):
        metadata = await grpc_call.initial_metadata()
        if "set-cookie" in metadata:
            self._cookie = metadata["set-cookie"]

    def _check_cookie_expiration(self):
        if self._is_cookie_expired():
            self._cookie = None

    def _is_cookie_expired(self) -> bool:
        is_expired = False

        if self._cookie is not None:
            cookie = SimpleCookie()
            cookie.load(self._cookie)
            cookie_map = cookie

            for key in self._expiration_time_keys_sequence[:-1]:
                cookie_map = cookie.get(key, {})

            expiration_data: Optional[str] = cookie_map.get(self._expiration_time_keys_sequence[-1], None)
            if expiration_data is not None:
                expiration_time = datetime.datetime.strptime(expiration_data, self._time_format)
                is_expired = datetime.datetime.utcnow() >= expiration_time

        return is_expired


class DisabledCookieAssistant(CookieAssistant):
    def cookie(self) -> Optional[str]:
        return None

    async def process_response_metadata(self, grpc_call: Call):
        pass


class Network:
    def __init__(
        self,
        lcd_endpoint: str,
        tm_websocket_endpoint: str,
        grpc_endpoint: str,
        grpc_exchange_endpoint: str,
        grpc_explorer_endpoint: str,
        chain_stream_endpoint: str,
        chain_id: str,
        fee_denom: str,
        env: str,
        chain_cookie_assistant: CookieAssistant,
        exchange_cookie_assistant: CookieAssistant,
        explorer_cookie_assistant: CookieAssistant,
        use_secure_connection: bool = False,
    ):
        self.lcd_endpoint = lcd_endpoint
        self.tm_websocket_endpoint = tm_websocket_endpoint
        self.grpc_endpoint = grpc_endpoint
        self.grpc_exchange_endpoint = grpc_exchange_endpoint
        self.grpc_explorer_endpoint = grpc_explorer_endpoint
        self.chain_stream_endpoint = chain_stream_endpoint
        self.chain_id = chain_id
        self.fee_denom = fee_denom
        self.env = env
        self.chain_cookie_assistant = chain_cookie_assistant
        self.exchange_cookie_assistant = exchange_cookie_assistant
        self.explorer_cookie_assistant = explorer_cookie_assistant
        self.use_secure_connection = use_secure_connection

    @classmethod
    def devnet(cls):
        return cls(
            lcd_endpoint="https://devnet.lcd.injective.dev",
            tm_websocket_endpoint="wss://devnet.tm.injective.dev/websocket",
            grpc_endpoint="devnet.injective.dev:9900",
            grpc_exchange_endpoint="devnet.injective.dev:9910",
            grpc_explorer_endpoint="devnet.injective.dev:9911",
            chain_stream_endpoint="devnet.injective.dev:9999",
            chain_id="injective-777",
            fee_denom="inj",
            env="devnet",
            chain_cookie_assistant=DisabledCookieAssistant(),
            exchange_cookie_assistant=DisabledCookieAssistant(),
            explorer_cookie_assistant=DisabledCookieAssistant(),
        )

    @classmethod
    def testnet(cls, node="lb"):
        nodes = [
            "lb",
            "sentry",
        ]
        if node not in nodes:
            raise ValueError("Must be one of {}".format(nodes))

        if node == "lb":
            lcd_endpoint = "https://testnet.sentry.lcd.injective.network:443"
            tm_websocket_endpoint = "wss://testnet.sentry.tm.injective.network:443/websocket"
            grpc_endpoint = "testnet.sentry.chain.grpc.injective.network:443"
            grpc_exchange_endpoint = "testnet.sentry.exchange.grpc.injective.network:443"
            grpc_explorer_endpoint = "testnet.sentry.explorer.grpc.injective.network:443"
            chain_stream_endpoint = "testnet.sentry.chain.stream.injective.network:443"
            chain_cookie_assistant = BareMetalLoadBalancedCookieAssistant()
            exchange_cookie_assistant = BareMetalLoadBalancedCookieAssistant()
            explorer_cookie_assistant = BareMetalLoadBalancedCookieAssistant()
            use_secure_connection = True
        else:
            lcd_endpoint = "https://testnet.lcd.injective.network:443"
            tm_websocket_endpoint = "wss://testnet.tm.injective.network:443/websocket"
            grpc_endpoint = "testnet.chain.grpc.injective.network:443"
            grpc_exchange_endpoint = "testnet.exchange.grpc.injective.network:443"
            grpc_explorer_endpoint = "testnet.explorer.grpc.injective.network:443"
            chain_stream_endpoint = "testnet.chain.stream.injective.network:443"
            chain_cookie_assistant = DisabledCookieAssistant()
            exchange_cookie_assistant = DisabledCookieAssistant()
            explorer_cookie_assistant = DisabledCookieAssistant()
            use_secure_connection = True

        return cls(
            lcd_endpoint=lcd_endpoint,
            tm_websocket_endpoint=tm_websocket_endpoint,
            grpc_endpoint=grpc_endpoint,
            grpc_exchange_endpoint=grpc_exchange_endpoint,
            grpc_explorer_endpoint=grpc_explorer_endpoint,
            chain_stream_endpoint=chain_stream_endpoint,
            chain_id="injective-888",
            fee_denom="inj",
            env="testnet",
            chain_cookie_assistant=chain_cookie_assistant,
            exchange_cookie_assistant=exchange_cookie_assistant,
            explorer_cookie_assistant=explorer_cookie_assistant,
            use_secure_connection=use_secure_connection,
        )

    @classmethod
    def mainnet(cls, node="lb"):
        nodes = [
            "lb",
        ]
        if node not in nodes:
            raise ValueError("Must be one of {}".format(nodes))

        lcd_endpoint = "https://sentry.lcd.injective.network:443"
        tm_websocket_endpoint = "wss://sentry.tm.injective.network:443/websocket"
        grpc_endpoint = "sentry.chain.grpc.injective.network:443"
        grpc_exchange_endpoint = "sentry.exchange.grpc.injective.network:443"
        grpc_explorer_endpoint = "sentry.explorer.grpc.injective.network:443"
        chain_stream_endpoint = "sentry.chain.stream.injective.network:443"
        chain_cookie_assistant = BareMetalLoadBalancedCookieAssistant()
        exchange_cookie_assistant = BareMetalLoadBalancedCookieAssistant()
        explorer_cookie_assistant = BareMetalLoadBalancedCookieAssistant()
        use_secure_connection = True

        return cls(
            lcd_endpoint=lcd_endpoint,
            tm_websocket_endpoint=tm_websocket_endpoint,
            grpc_endpoint=grpc_endpoint,
            grpc_exchange_endpoint=grpc_exchange_endpoint,
            grpc_explorer_endpoint=grpc_explorer_endpoint,
            chain_stream_endpoint=chain_stream_endpoint,
            chain_id="injective-1",
            fee_denom="inj",
            env="mainnet",
            chain_cookie_assistant=chain_cookie_assistant,
            exchange_cookie_assistant=exchange_cookie_assistant,
            explorer_cookie_assistant=explorer_cookie_assistant,
            use_secure_connection=use_secure_connection,
        )

    @classmethod
    def local(cls):
        return cls(
            lcd_endpoint="http://localhost:10337",
            tm_websocket_endpoint="ws://localhost:26657/websocket",
            grpc_endpoint="localhost:9900",
            grpc_exchange_endpoint="localhost:9910",
            grpc_explorer_endpoint="localhost:9911",
            chain_stream_endpoint="localhost:9999",
            chain_id="injective-1",
            fee_denom="inj",
            env="local",
            chain_cookie_assistant=DisabledCookieAssistant(),
            exchange_cookie_assistant=DisabledCookieAssistant(),
            explorer_cookie_assistant=DisabledCookieAssistant(),
            use_secure_connection=False,
        )

    @classmethod
    def custom(
        cls,
        lcd_endpoint,
        tm_websocket_endpoint,
        grpc_endpoint,
        grpc_exchange_endpoint,
        grpc_explorer_endpoint,
        chain_stream_endpoint,
        chain_id,
        env,
        chain_cookie_assistant: Optional[CookieAssistant] = None,
        exchange_cookie_assistant: Optional[CookieAssistant] = None,
        explorer_cookie_assistant: Optional[CookieAssistant] = None,
        use_secure_connection: bool = False,
    ):
        chain_assistant = chain_cookie_assistant or DisabledCookieAssistant()
        exchange_assistant = exchange_cookie_assistant or DisabledCookieAssistant()
        explorer_assistant = explorer_cookie_assistant or DisabledCookieAssistant()
        return cls(
            lcd_endpoint=lcd_endpoint,
            tm_websocket_endpoint=tm_websocket_endpoint,
            grpc_endpoint=grpc_endpoint,
            grpc_exchange_endpoint=grpc_exchange_endpoint,
            grpc_explorer_endpoint=grpc_explorer_endpoint,
            chain_stream_endpoint=chain_stream_endpoint,
            chain_id=chain_id,
            fee_denom="inj",
            env=env,
            chain_cookie_assistant=chain_assistant,
            exchange_cookie_assistant=exchange_assistant,
            explorer_cookie_assistant=explorer_assistant,
            use_secure_connection=use_secure_connection,
        )

    def string(self):
        return self.env
