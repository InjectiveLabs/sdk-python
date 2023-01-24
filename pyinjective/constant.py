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
        if network == 'devnet':
            config = devnet_config
        elif network == 'testnet':
            config = testnet_config
        else:
            config =mainnet_config

        return cls(
            description=config[market_id]['description'],
            base=int(config[market_id]['base']),
            quote=int(config[market_id]['quote']),
            min_price_tick_size=float(config[market_id]['min_price_tick_size']),
            min_quantity_tick_size=float(config[market_id]['min_quantity_tick_size']),
        )

    @classmethod
    def load_peggy_denom(cls, network, symbol):
        if network == 'devnet':
            config = devnet_config
        elif network == 'local':
            config = devnet_config
        elif network == 'testnet':
            config = testnet_config
        else:
            config = mainnet_config
        return config[symbol]['peggy_denom'], int(config[symbol]['decimals'])


class Network:
    def __init__(
        self,
        lcd_endpoint: str ,
        tm_websocket_endpoint: str,
        grpc_endpoint: str ,
        grpc_exchange_endpoint: str ,
        grpc_explorer_endpoint: str ,
        chain_id: str ,
        fee_denom: str ,
        env: str
    ):
        self.lcd_endpoint = lcd_endpoint
        self.tm_websocket_endpoint = tm_websocket_endpoint
        self.grpc_endpoint = grpc_endpoint
        self.grpc_exchange_endpoint = grpc_exchange_endpoint
        self.grpc_explorer_endpoint = grpc_explorer_endpoint
        self.chain_id = chain_id
        self.fee_denom = fee_denom
        self.env = env

    @classmethod
    def devnet(cls):
        return cls(
            lcd_endpoint='https://devnet.lcd.injective.dev',
            tm_websocket_endpoint='wss://devnet.tm.injective.dev/websocket',
            grpc_endpoint='devnet.injective.dev:9900',
            grpc_exchange_endpoint='devnet.injective.dev:9910',
            grpc_explorer_endpoint='devnet.injective.dev:9911',
            chain_id='injective-777',
            fee_denom='inj',
            env='devnet'
        )

    @classmethod
    def testnet(cls):
        return cls(
            lcd_endpoint='https://k8s.testnet.lcd.injective.network',
            tm_websocket_endpoint='wss://k8s.testnet.tm.injective.network/websocket',
            grpc_endpoint='k8s.testnet.chain.grpc.injective.network:443',
            grpc_exchange_endpoint='k8s.testnet.exchange.grpc.injective.network:443',
            grpc_explorer_endpoint='k8s.testnet.explorer.grpc.injective.network:443',
            chain_id='injective-888',
            fee_denom='inj',
            env='testnet'
        )

    @classmethod
    def mainnet(cls, node='lb'):
        nodes = [
            'k8s',
            'lb',
            'sentry0',  # us, prod
            'sentry1',  # us, prod
            'sentry2',  # us, staging
            'sentry3',  # tokyo, prod
        ]
        if node not in nodes:
            raise ValueError('Must be one of {}'.format(nodes))

        if node == 'k8s':
            lcd_endpoint='https://k8s.mainnet.lcd.injective.network:443'
            tm_websocket_endpoint='wss://k8s.mainnet.tm.injective.network:443/websocket'
            grpc_endpoint='k8s.mainnet.chain.grpc.injective.network:443'
            grpc_exchange_endpoint='k8s.mainnet.exchange.grpc.injective.network:443'
            grpc_explorer_endpoint='k8s.mainnet.explorer.grpc.injective.network:443'
        elif node == 'lb':
            lcd_endpoint = 'https://k8s.global.mainnet.lcd.injective.network:443'
            tm_websocket_endpoint = 'wss://k8s.global.mainnet.tm.injective.network:443/websocket'
            grpc_endpoint = 'k8s.global.mainnet.chain.grpc.injective.network:443'
            grpc_exchange_endpoint = 'k8s.global.mainnet.exchange.grpc.injective.network:443'
            grpc_explorer_endpoint = 'k8s.global.mainnet.explorer.grpc.injective.network:443'
        else:
            lcd_endpoint='https://lcd.injective.network'
            tm_websocket_endpoint=f'ws://{node}.injective.network:26657/websocket'
            grpc_endpoint=f'{node}.injective.network:9900'
            grpc_exchange_endpoint=f'{node}.injective.network:9910'
            grpc_explorer_endpoint=f'{node}.injective.network:9911'

        return cls(
            lcd_endpoint=lcd_endpoint,
            tm_websocket_endpoint=tm_websocket_endpoint,
            grpc_endpoint=grpc_endpoint,
            grpc_exchange_endpoint=grpc_exchange_endpoint,
            grpc_explorer_endpoint=grpc_explorer_endpoint,
            chain_id='injective-1',
            fee_denom='inj',
            env='mainnet'
        )

    @classmethod
    def local(cls):
        return cls(
            lcd_endpoint='http://localhost:10337',
            tm_websocket_endpoint='ws://localost:26657/websocket',
            grpc_endpoint='localhost:9900',
            grpc_exchange_endpoint='localhost:9910',
            grpc_explorer_endpoint='localhost:9911',
            chain_id='injective-1',
            fee_denom='inj',
            env='local'
        )

    @classmethod
    def custom(cls, lcd_endpoint, tm_websocket_endpoint, grpc_endpoint, grpc_exchange_endpoint, grpc_explorer_endpoint, chain_id, env):
        return cls(
            lcd_endpoint=lcd_endpoint,
            tm_websocket_endpoint=tm_websocket_endpoint,
            grpc_endpoint=grpc_endpoint,
            grpc_exchange_endpoint=grpc_exchange_endpoint,
            grpc_explorer_endpoint=grpc_explorer_endpoint,
            chain_id=chain_id,
            fee_denom='inj',
            env=env
        )

    def string(self):
        return self.env
