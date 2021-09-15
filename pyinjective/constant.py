import os
from configparser import ConfigParser

MAX_CLIENT_ID_LENGTH = 128
MAX_DATA_SIZE = 256
MAX_MEMO_CHARACTERS = 256

config = ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'denoms.ini'))

class Denom:
    def __init__(
        self,
        base: int,
        quote: int,
        min_price_tick_size: float,
        min_quantity_tick_size: float
    ):
        self.base = base
        self.quote = quote
        self.min_price_tick_size = min_price_tick_size
        self.min_quantity_tick_size = min_quantity_tick_size

    @classmethod
    def pair(cls, ticker):
        return cls(
            base=int(config._sections[ticker]['base']),
            quote=int(config._sections[ticker]['quote']),
            min_price_tick_size=str(config._sections[ticker]['min_price_tick_size']),
            min_quantity_tick_size=str(config._sections[ticker]['min_quantity_tick_size']),
        )

class Network:
    def __init__(
        self,
        lcd_endpoint: str = None,
        grpc_endpoint: str = None,
        grpc_exchange_endpoint: str = None,
        chain_id: str = None,
        fee_denom: str = None
    ):
        self.lcd_endpoint = lcd_endpoint
        self.grpc_endpoint = grpc_endpoint
        self.grpc_exchange_endpoint = grpc_exchange_endpoint
        self.chain_id = chain_id
        self.fee_denom = fee_denom

    @classmethod
    def local(cls):
        return cls(
            lcd_endpoint='localhost:10337',
            grpc_endpoint='localhost:9900',
            grpc_exchange_endpoint='localhost:9110',
            chain_id='injective-1',
            fee_denom='inj'
        )

    @classmethod
    def testnet(cls):
        return cls(
            lcd_endpoint='staking-lcd-testnet.injective.network',
            grpc_endpoint='testnet-sentry0.injective.network:9900',
            grpc_exchange_endpoint='testnet-sentry0.injective.network:9910',
            chain_id='injective-888',
            fee_denom='inj'
        )

    @classmethod
    def mainnet(cls):
        return cls(
            lcd_endpoint='staking-lcd.injective.network',
            grpc_endpoint='sentry0.injective.network:9900',
            grpc_exchange_endpoint='sentry0.injective.network:9910',
            chain_id='injective-1',
            fee_denom='inj'
        )
