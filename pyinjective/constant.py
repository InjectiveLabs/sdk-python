MAX_CLIENT_ID_LENGTH = 128
MAX_DATA_SIZE = 256
MAX_MEMO_CHARACTERS = 256

class Network:
    def __init__(
        self,
        lcd_endpoint: str = None,
        grpc_endpoint: str = None,
        chain_id: str = None,
        fee_denom: str = None
    ):
        self.lcd_endpoint = lcd_endpoint
        self.grpc_endpoint = grpc_endpoint
        self.chain_id = chain_id
        self.fee_denom = fee_denom

    @classmethod
    def local(cls):
        return cls(
            lcd_endpoint='localhost:10337',
            grpc_endpoint='localhost:9900',
            chain_id='injective-1',
            fee_denom='inj'
        )

    @classmethod
    def testnet(cls):
        return cls(
            lcd_endpoint='staking-lcd-testnet.injective.network',
            grpc_endpoint='testnet-sentry0.injective.network:9900',
            chain_id='injective-888',
            fee_denom='inj'
        )

    @classmethod
    def mainnet(cls):
        return cls(
            lcd_endpoint='staking-lcd.injective.network',
            grpc_endpoint='sentry0.injective.network:9900',
            chain_id='injective-1',
            fee_denom='inj'
        )
