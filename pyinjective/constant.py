import os
from configparser import ConfigParser

MAX_CLIENT_ID_LENGTH = 128
MAX_DATA_SIZE = 256
MAX_MEMO_CHARACTERS = 256

testnet_config = ConfigParser()
testnet_config.read(os.path.join(os.path.dirname(__file__), 'testnet_denoms.ini'))

mainnet_config = ConfigParser()
mainnet_config.read(os.path.join(os.path.dirname(__file__), 'mainnet_denoms.ini'))

class Denoms:
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
        if network == 'testnet':
            config = testnet_config
        if network == 'mainnet':
            config =mainnet_config

        return cls(
            description=config._sections[market_id]['description'],
            base=int(config._sections[market_id]['base']),
            quote=int(config._sections[market_id]['quote']),
            min_price_tick_size=str(config._sections[market_id]['min_price_tick_size']),
            min_quantity_tick_size=str(config._sections[market_id]['min_quantity_tick_size']),
        )

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
    def local(cls):
        return cls(
            lcd_endpoint='localhost:10337',
            grpc_endpoint='localhost:9900',
            grpc_exchange_endpoint='localhost:9110',
            chain_id='injective-1',
            fee_denom='inj',
            env = 'local'
        )

    @classmethod
    def testnet(cls):
        return cls(
            lcd_endpoint='staking-lcd-testnet.injective.network',
            grpc_endpoint='testnet-sentry0.injective.network:9900',
            grpc_exchange_endpoint='testnet-sentry0.injective.network:9910',
            chain_id='injective-888',
            fee_denom='inj',
            env = 'testnet'
        )

    @classmethod
    def mainnet(cls):
        return cls(
            lcd_endpoint='staking-lcd.injective.network',
            grpc_endpoint='sentry0.injective.network:9900',
            grpc_exchange_endpoint='sentry0.injective.network:9910',
            chain_id='injective-1',
            fee_denom='inj',
            env = 'mainnet'
        )

    def string(self):
        return self.env
