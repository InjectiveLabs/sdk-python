import os
from configparser import ConfigParser

MAX_CLIENT_ID_LENGTH = 128
MAX_DATA_SIZE = 256
MAX_MEMO_CHARACTERS = 256

devnet_config = ConfigParser()
devnet_config.read(os.path.join(os.path.dirname(__file__), 'denoms_devnet.ini'))

testnet_config = ConfigParser()
testnet_config.read(os.path.join(os.path.dirname(__file__), 'denoms_testnet.ini'))

mainnet_config = ConfigParser()
mainnet_config.read(os.path.join(os.path.dirname(__file__), 'denoms_mainnet.ini'))

class Denom:
    def __init__(
        self,
        description: str,
        base: int,
        quote: int,
        min_price_tick_size: float,
        min_quantity_tick_size: float
    ):
        self.description = description
        self.base = base
        self.quote = quote
        self.min_price_tick_size = min_price_tick_size
        self.min_quantity_tick_size = min_quantity_tick_size

    @classmethod
    def load_market(cls, network, market_id):
        config = None
        if network == 'devnet':
            config = devnet_config
        if network == 'testnet':
            config = testnet_config
        if network == 'mainnet':
            config =mainnet_config

        return cls(
            description=config._sections[market_id]['description'],
            base=int(config._sections[market_id]['base']),
            quote=int(config._sections[market_id]['quote']),
            min_price_tick_size=config._sections[market_id]['min_price_tick_size'],
            min_quantity_tick_size=config._sections[market_id]['min_quantity_tick_size'],
        )

    @classmethod
    def load_peggy_denom(cls, network, symbol):
        config = None
        if network == 'devnet':
            config = devnet_config
        if network == 'testnet':
            config = testnet_config
        if network == 'mainnet':
            config = mainnet_config
        return config._sections[symbol]['peggy_denom'], int(config._sections[symbol]['decimals'])


class Network:
    def __init__(
        self,
        lcd_endpoint: str = None,
        grpc_endpoint: str = None,
        grpc_exchange_endpoint: str = None,
        chain_id: str = None,
        fee_denom: str = None,
        env: str = None
    ):
        self.lcd_endpoint = lcd_endpoint
        self.grpc_endpoint = grpc_endpoint
        self.grpc_exchange_endpoint = grpc_exchange_endpoint
        self.chain_id = chain_id
        self.fee_denom = fee_denom
        self.env = env

    @classmethod
    def devnet(cls):
        return cls(
            lcd_endpoint='https://devnet.lcd.injective.dev',
            grpc_endpoint='devnet.injective.dev:9900',
            grpc_exchange_endpoint='devnet.injective.dev:9910',
            chain_id='injective-777',
            fee_denom='inj',
            env='devnet'
        )

    @classmethod
    def testnet(cls, sentry='primary'):
        s = 'sentry0' if sentry == 'primary' else 'sentry1'

        return cls(
            lcd_endpoint='https://testnet.lcd.injective.dev',
            grpc_endpoint=f"{s}.injective.dev:9900",
            grpc_exchange_endpoint=f"{s}.injective.dev:9910",
            chain_id='injective-888',
            fee_denom='inj',
            env='testnet'
        )

    @classmethod
    def mainnet(cls, location='tokyo'):
        s = 'sentry1' if location == 'tokyo' else 'sentry0'

        return cls(
            lcd_endpoint='https://lcd.injective.network',
            grpc_endpoint=f"{s}.injective.network:9900",
            grpc_exchange_endpoint=f"{s}.injective.network:9910",
            chain_id='injective-1',
            fee_denom='inj',
            env='mainnet'
        )

    def string(self):
        return self.env
