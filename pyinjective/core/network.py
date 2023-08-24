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
        return (("cookie", cookie),)


class MainnetKubernetesCookieAssistant(CookieAssistant):

    def __init__(self):
        self._chain_cookie: Optional[str] = None
        self._exchange_cookie: Optional[str] = None
        self._chain_cookie_initialization_lock = asyncio.Lock()
        self._exchange_cookie_initialization_lock = asyncio.Lock()

    async def chain_cookie(self, metadata_query_provider: Callable) -> str:
        if self._chain_cookie == None:
            async with self._chain_cookie_initialization_lock:
                if self._chain_cookie == None:
                    await self._fetch_chain_cookie(metadata_query_provider=metadata_query_provider)
        cookie = self._chain_cookie
        self._check_chain_cookie_expiration()

        return cookie

    async def exchange_cookie(self, metadata_query_provider: Callable) -> str:
        if self._exchange_cookie == None:
            async with self._exchange_cookie_initialization_lock:
                if self._exchange_cookie == None:
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
            raise RuntimeError(f"Error fetching exchange cookie ({metadata})")

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

        expiration_time = datetime.datetime.strptime(cookie["GCLB"]["expires"],
                                                     "%a, %d-%b-%Y %H:%M:%S %Z").timestamp()

        timestamp_diff = expiration_time - time.time()
        return timestamp_diff < self.SESSION_RENEWAL_OFFSET


class MainnetBareMetalCookieAssistant(CookieAssistant):

    def __init__(self):
        self._chain_cookie: Optional[str] = None
        self._exchange_cookie: Optional[str] = None
        self._chain_cookie_initialization_lock = asyncio.Lock()
        self._exchange_cookie_initialization_lock = asyncio.Lock()

    async def chain_cookie(self, metadata_query_provider: Callable) -> str:
        if self._chain_cookie == None:
            async with self._chain_cookie_initialization_lock:
                if self._chain_cookie == None:
                    await self._fetch_chain_cookie(metadata_query_provider=metadata_query_provider)
        cookie = self._chain_cookie
        self._check_chain_cookie_expiration()

        return cookie

    async def exchange_cookie(self, metadata_query_provider: Callable) -> str:
        if self._exchange_cookie == None:
            async with self._exchange_cookie_initialization_lock:
                if self._exchange_cookie == None:
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
            raise RuntimeError(f"Error fetching exchange cookie ({metadata})")

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


class TestnetCookieAssistant(CookieAssistant):

    def __init__(self):
        self._chain_cookie: Optional[str] = None
        self._exchange_cookie: Optional[str] = None
        self._chain_cookie_initialization_lock = asyncio.Lock()
        self._exchange_cookie_initialization_lock = asyncio.Lock()

    async def chain_cookie(self, metadata_query_provider: Callable) -> str:
        if self._chain_cookie == None:
            async with self._chain_cookie_initialization_lock:
                if self._chain_cookie == None:
                    await self._fetch_chain_cookie(metadata_query_provider=metadata_query_provider)
        cookie = self._chain_cookie
        self._check_chain_cookie_expiration()

        return cookie

    async def exchange_cookie(self, metadata_query_provider: Callable) -> str:
        if self._exchange_cookie == None:
            async with self._exchange_cookie_initialization_lock:
                if self._exchange_cookie == None:
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
            raise RuntimeError(f"Error fetching exchange cookie ({metadata})")

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

        expiration_time = datetime.datetime.strptime(cookie["grpc-cookie"]["expires"],
                                                     "%a, %d-%b-%y %H:%M:%S %Z").timestamp()

        timestamp_diff = expiration_time - time.time()
        return timestamp_diff < self.SESSION_RENEWAL_OFFSET


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
        chain_id: str,
        fee_denom: str,
        env: str,
        cookie_assistant: CookieAssistant,
    ):
        self.lcd_endpoint = lcd_endpoint
        self.tm_websocket_endpoint = tm_websocket_endpoint
        self.grpc_endpoint = grpc_endpoint
        self.grpc_exchange_endpoint = grpc_exchange_endpoint
        self.grpc_explorer_endpoint = grpc_explorer_endpoint
        self.chain_id = chain_id
        self.fee_denom = fee_denom
        self.env = env
        self.cookie_assistant = cookie_assistant

    @classmethod
    def devnet(cls):
        return cls(
            lcd_endpoint="https://devnet.lcd.injective.dev",
            tm_websocket_endpoint="wss://devnet.tm.injective.dev/websocket",
            grpc_endpoint="devnet.injective.dev:9900",
            grpc_exchange_endpoint="devnet.injective.dev:9910",
            grpc_explorer_endpoint="devnet.injective.dev:9911",
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
            lcd_endpoint = "https://k8s.testnet.lcd.injective.network"
            tm_websocket_endpoint = "wss://k8s.testnet.tm.injective.network/websocket"
            grpc_endpoint = "k8s.testnet.chain.grpc.injective.network:443"
            grpc_exchange_endpoint = "k8s.testnet.exchange.grpc.injective.network:443"
            grpc_explorer_endpoint = "k8s.testnet.explorer.grpc.injective.network:443"
        else:
            lcd_endpoint = "https://testnet.lcd.injective.network"
            tm_websocket_endpoint = "wss://testnet.tm.injective.network/websocket"
            grpc_endpoint = "testnet.chain.grpc.injective.network"
            grpc_exchange_endpoint = "testnet.exchange.grpc.injective.network"
            grpc_explorer_endpoint = "testnet.explorer.grpc.injective.network"

        return cls(
            lcd_endpoint=lcd_endpoint,
            tm_websocket_endpoint=tm_websocket_endpoint,
            grpc_endpoint=grpc_endpoint,
            grpc_exchange_endpoint=grpc_exchange_endpoint,
            grpc_explorer_endpoint=grpc_explorer_endpoint,
            chain_id="injective-888",
            fee_denom="inj",
            env="testnet",
            cookie_assistant=TestnetCookieAssistant()
        )

    @classmethod
    def mainnet(cls, node="lb"):
        nodes = [
            "lb", # us, asia, prod
            "lb_bare_metal",
            "sentry0",  # ca, prod
            "sentry1",  # ca, prod
            "sentry3",  # us, prod
        ]
        if node not in nodes:
            raise ValueError("Must be one of {}".format(nodes))

        if node == "lb":
            lcd_endpoint = "https://k8s.global.mainnet.lcd.injective.network:443"
            tm_websocket_endpoint = "wss://k8s.global.mainnet.tm.injective.network:443/websocket"
            grpc_endpoint = "k8s.global.mainnet.chain.grpc.injective.network:443"
            grpc_exchange_endpoint = "k8s.global.mainnet.exchange.grpc.injective.network:443"
            grpc_explorer_endpoint = "k8s.global.mainnet.explorer.grpc.injective.network:443"
            cookie_assistant = MainnetKubernetesCookieAssistant()
        elif node == "lb_bare_metal":
            lcd_endpoint = "https://sentry.lcd.injective.network:443"
            tm_websocket_endpoint = "wss://sentry.tm.injective.network:443/websocket"
            grpc_endpoint = "sentry.chain.grpc.injective.network:443"
            grpc_exchange_endpoint = "sentry.exchange.grpc.injective.network:443"
            grpc_explorer_endpoint = "sentry.explorer.grpc.injective.network:443"
            cookie_assistant = MainnetBareMetalCookieAssistant()
        else:
            lcd_endpoint = f"http://{node}.injective.network:10337"
            tm_websocket_endpoint = f"ws://{node}.injective.network:26657/websocket"
            grpc_endpoint = f"{node}.injective.network:9900"
            grpc_exchange_endpoint = f"{node}.injective.network:9910"
            grpc_explorer_endpoint = f"{node}.injective.network:9911"
            cookie_assistant = DisabledCookieAssistant()

        return cls(
            lcd_endpoint=lcd_endpoint,
            tm_websocket_endpoint=tm_websocket_endpoint,
            grpc_endpoint=grpc_endpoint,
            grpc_exchange_endpoint=grpc_exchange_endpoint,
            grpc_explorer_endpoint=grpc_explorer_endpoint,
            chain_id="injective-1",
            fee_denom="inj",
            env="mainnet",
            cookie_assistant=cookie_assistant,
        )

    @classmethod
    def local(cls):
        return cls(
            lcd_endpoint="http://localhost:10337",
            tm_websocket_endpoint="ws://localhost:26657/websocket",
            grpc_endpoint="localhost:9900",
            grpc_exchange_endpoint="localhost:9910",
            grpc_explorer_endpoint="localhost:9911",
            chain_id="injective-1",
            fee_denom="inj",
            env="local",
            cookie_assistant=DisabledCookieAssistant(),
        )

    @classmethod
    def custom(
            cls,
            lcd_endpoint,
            tm_websocket_endpoint,
            grpc_endpoint,
            grpc_exchange_endpoint,
            grpc_explorer_endpoint,
            chain_id,
            env,
            cookie_assistant: CookieAssistant,
    ):
        return cls(
            lcd_endpoint=lcd_endpoint,
            tm_websocket_endpoint=tm_websocket_endpoint,
            grpc_endpoint=grpc_endpoint,
            grpc_exchange_endpoint=grpc_exchange_endpoint,
            grpc_explorer_endpoint=grpc_explorer_endpoint,
            chain_id=chain_id,
            fee_denom="inj",
            env=env,
            cookie_assistant=cookie_assistant
        )

    def string(self):
        return self.env

    async def chain_metadata(self, metadata_query_provider: Callable) -> Tuple[Tuple[str, str]]:
        return await self.cookie_assistant.chain_metadata(metadata_query_provider=metadata_query_provider)

    async def exchange_metadata(self, metadata_query_provider: Callable) -> Tuple[Tuple[str, str]]:
        return await self.cookie_assistant.exchange_metadata(metadata_query_provider=metadata_query_provider)
