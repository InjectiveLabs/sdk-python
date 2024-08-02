from pyinjective.constant import devnet_config, mainnet_config, testnet_config


class Denom:
    def __init__(
        self,
        description: str,
        base: int,
        quote: int,
        min_price_tick_size: float,
        min_quantity_tick_size: float,
        min_notional: float,
    ):
        self.description = description
        self.base = base
        self.quote = quote
        self.min_price_tick_size = min_price_tick_size
        self.min_quantity_tick_size = min_quantity_tick_size
        self.min_notional = min_notional

    @classmethod
    def load_market(cls, network, market_id):
        if network == "devnet":
            config = devnet_config
        elif network == "testnet":
            config = testnet_config
        else:
            config = mainnet_config

        return cls(
            description=config[market_id]["description"],
            base=int(config[market_id]["base"]),
            quote=int(config[market_id]["quote"]),
            min_price_tick_size=float(config[market_id]["min_price_tick_size"]),
            min_quantity_tick_size=float(config[market_id]["min_quantity_tick_size"]),
            min_notional=float(config[market_id]["min_notional"]),
        )

    @classmethod
    def load_peggy_denom(cls, network, symbol):
        if network == "devnet":
            config = devnet_config
        elif network == "local":
            config = devnet_config
        elif network == "testnet":
            config = testnet_config
        else:
            config = mainnet_config
        return config[symbol]["peggy_denom"], int(config[symbol]["decimals"])
