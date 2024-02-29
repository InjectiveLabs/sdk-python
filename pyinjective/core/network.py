import asyncio
import datetime
import time
from abc import ABC, abstractmethod
from http.cookies import SimpleCookie
from typing import Callable, Optional, Tuple


class CookieAssistant(ABC):
    SESSION_RENEWAL_OFFSET = 120

    @abstractmethod
    async def chain_cookie(self, metadata_query_provider: Callable) -> str:
        ...

    @abstractmethod
    async def exchange_cookie(self, metadata_query_provider: Callable) -> str:
        ...

    async def chain_metadata(self, metadata_query_provider: Callable) -> Tuple[Tuple[str, str]]:
        cookie = await self.chain_cookie(metadata_query_provider=metadata_query_provider)
        return (("cookie", cookie),)

    async def exchange_metadata(self, metadata_query_provider: Callable) -> Tuple[Tuple[str, str]]:
        cookie = await self.exchange_cookie(metadata_query_provider=metadata_query_provider)
        metadata = None
        if cookie is not None and cookie != "":
            metadata = (("cookie", cookie),)
        return metadata


class KubernetesLoadBalancedCookieAssistant(CookieAssistant):
    def __init__(self):
        self._chain_cookie: Optional[str] = None
        self._exchange_cookie: Optional[str] = None
        self._chain_cookie_initialization_lock = asyncio.Lock()
        self._exchange_cookie_initialization_lock = asyncio.Lock()

    async def chain_cookie(self, metadata_query_provider: Callable) -> str:
        if self._chain_cookie is None:
            async with self._chain_cookie_initialization_lock:
                if self._chain_cookie is None:
                    await self._fetch_chain_cookie(metadata_query_provider=metadata_query_provider)
        cookie = self._chain_cookie
        self._check_chain_cookie_expiration()

        return cookie

    async def exchange_cookie(self, metadata_query_provider: Callable) -> str:
        if self._exchange_cookie is None:
            async with self._exchange_cookie_initialization_lock:
                if self._exchange_cookie is None:
                    await self._fetch_exchange_cookie(metadata_query_provider=metadata_query_provider)
        cookie = self._exchange_cookie
        self._check_exchange_cookie_expiration()

        return cookie

    async def _fetch_chain_cookie(self, metadata_query_provider: Callable):
        metadata = await metadata_query_provider()
        cookie_info = next((value for key, value in metadata if key == "set-cookie"), None)

        if cookie_info is None:
            raise RuntimeError(f"Error fetching chain cookie ({metadata})")

        self._chain_cookie = cookie_info

    async def _fetch_exchange_cookie(self, metadata_query_provider: Callable):
        metadata = await metadata_query_provider()
        cookie_info = next((value for key, value in metadata if key == "set-cookie"), None)

        if cookie_info is None:
            cookie_info = ""

        self._exchange_cookie = cookie_info

    def _check_chain_cookie_expiration(self):
        if self._is_cookie_expired(cookie_data=self._chain_cookie):
            self._chain_cookie = None

    def _check_exchange_cookie_expiration(self):
        if self._is_cookie_expired(cookie_data=self._exchange_cookie):
            self._exchange_cookie = None

    def _is_cookie_expired(self, cookie_data: str) -> bool:
        cookie = SimpleCookie()
        cookie.load(cookie_data)

        expiration_data: Optional[str] = cookie.get("GCLB", {}).get("expires", None)
        if expiration_data is None:
            expiration_time = 0
        else:
            expiration_time = datetime.datetime.strptime(expiration_data, "%a, %d-%b-%Y %H:%M:%S %Z").timestamp()

        timestamp_diff = expiration_time - time.time()
        return timestamp_diff < self.SESSION_RENEWAL_OFFSET


class BareMetalLoadBalancedCookieAssistant(CookieAssistant):
    def __init__(self):
        self._chain_cookie: Optional[str] = None
        self._exchange_cookie: Optional[str] = None
        self._chain_cookie_initialization_lock = asyncio.Lock()
        self._exchange_cookie_initialization_lock = asyncio.Lock()

    async def chain_cookie(self, metadata_query_provider: Callable) -> str:
        if self._chain_cookie is None:
            async with self._chain_cookie_initialization_lock:
                if self._chain_cookie is None:
                    await self._fetch_chain_cookie(metadata_query_provider=metadata_query_provider)
        cookie = self._chain_cookie
        self._check_chain_cookie_expiration()

        return cookie

    async def exchange_cookie(self, metadata_query_provider: Callable) -> str:
        if self._exchange_cookie is None:
            async with self._exchange_cookie_initialization_lock:
                if self._exchange_cookie is None:
                    await self._fetch_exchange_cookie(metadata_query_provider=metadata_query_provider)
        cookie = self._exchange_cookie
        self._check_exchange_cookie_expiration()

        return cookie

    async def _fetch_chain_cookie(self, metadata_query_provider: Callable):
        metadata = await metadata_query_provider()
        cookie_info = next((value for key, value in metadata if key == "set-cookie"), None)

        if cookie_info is None:
            raise RuntimeError(f"Error fetching chain cookie ({metadata})")

        self._chain_cookie = cookie_info

    async def _fetch_exchange_cookie(self, metadata_query_provider: Callable):
        metadata = await metadata_query_provider()
        cookie_info = next((value for key, value in metadata if key == "set-cookie"), None)

        if cookie_info is None:
            cookie_info = ""

        self._exchange_cookie = cookie_info

    def _check_chain_cookie_expiration(self):
        if self._is_cookie_expired(cookie_data=self._chain_cookie):
            self._chain_cookie = None

    def _check_exchange_cookie_expiration(self):
        if self._is_cookie_expired(cookie_data=self._exchange_cookie):
            self._exchange_cookie = None

    def _is_cookie_expired(self, cookie_data: str) -> bool:
        # The cookies for these nodes do not expire
        return False


class DisabledCookieAssistant(CookieAssistant):
    async def chain_cookie(self, metadata_query_provider: Callable) -> str:
        pass

    async def exchange_cookie(self, metadata_query_provider: Callable) -> str:
        pass

    async def chain_metadata(self, metadata_query_provider: Callable) -> Tuple[Tuple[str, str]]:
        return None

    async def exchange_metadata(self, metadata_query_provider: Callable) -> Tuple[Tuple[str, str]]:
        return None


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
        cookie_assistant: CookieAssistant,
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
        self.cookie_assistant = cookie_assistant
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
            cookie_assistant=DisabledCookieAssistant(),
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
            cookie_assistant = BareMetalLoadBalancedCookieAssistant()
            use_secure_connection = True
        else:
            lcd_endpoint = "https://testnet.lcd.injective.network:443"
            tm_websocket_endpoint = "wss://testnet.tm.injective.network:443/websocket"
            grpc_endpoint = "testnet.chain.grpc.injective.network:443"
            grpc_exchange_endpoint = "testnet.exchange.grpc.injective.network:443"
            grpc_explorer_endpoint = "testnet.explorer.grpc.injective.network:443"
            chain_stream_endpoint = "testnet.chain.stream.injective.network:443"
            cookie_assistant = DisabledCookieAssistant()
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
            cookie_assistant=cookie_assistant,
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
        cookie_assistant = BareMetalLoadBalancedCookieAssistant()
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
            cookie_assistant=cookie_assistant,
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
            cookie_assistant=DisabledCookieAssistant(),
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
        cookie_assistant: Optional[CookieAssistant] = None,
        use_secure_connection: bool = False,
    ):
        assistant = cookie_assistant or DisabledCookieAssistant()
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
            cookie_assistant=assistant,
            use_secure_connection=use_secure_connection,
        )

    def string(self):
        return self.env

    async def chain_metadata(self, metadata_query_provider: Callable) -> Tuple[Tuple[str, str]]:
        return await self.cookie_assistant.chain_metadata(metadata_query_provider=metadata_query_provider)

    async def exchange_metadata(self, metadata_query_provider: Callable) -> Tuple[Tuple[str, str]]:
        return await self.cookie_assistant.exchange_metadata(metadata_query_provider=metadata_query_provider)
