import os
from configparser import ConfigParser

GAS_PRICE = 160_000_000
GAS_FEE_BUFFER_AMOUNT = 25_000
MAX_MEMO_CHARACTERS = 256
ADDITIONAL_CHAIN_FORMAT_DECIMALS = 18
TICKER_TOKENS_SEPARATOR = "/"
INJ_DENOM = "inj"
INJ_DECIMALS = 18

devnet_config = ConfigParser()
devnet_config.read(os.path.join(os.path.dirname(__file__), "denoms_devnet.ini"))

testnet_config = ConfigParser()
testnet_config.read(os.path.join(os.path.dirname(__file__), "denoms_testnet.ini"))

mainnet_config = ConfigParser()
mainnet_config.read(os.path.join(os.path.dirname(__file__), "denoms_mainnet.ini"))

CONFIGS = {
    "devnet": devnet_config,
    "testnet": testnet_config,
    "mainnet": mainnet_config,
}
