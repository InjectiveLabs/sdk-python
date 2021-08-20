# from etherscan.io
DECIMALS_DICT = {
    "INJ": 18,  # uint8
    "USDT": 6,  # uint256
    "BNB": 18,  # uint8
    "LINK": 18,  # uint8
    "UNI": 18,  # uint8
    "AAVE": 18,  # uint8 from https://etherscan.io/token/0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9#readProxyContract
    "MATIC": 18,  # uint8
    "ZRX": 18,  # uint8
    "USDC": 6,  # uint8 from https://etherscan.io/token/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48#readProxyContract
}


ORDERTYPE_DICT = {"UNSPECIFIED": 0, "BUY": 1, "SELL": 2,
                  "STOP_BUY": 3, "STOP_SELL": 4, "TAKE_BUY": 5, "TAKE_SELL": 6}
