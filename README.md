## Injective Python SDK

[![codecov](https://codecov.io/gh/InjectiveLabs/sdk-python/graph/badge.svg?token=RBGK98G6F1)](https://codecov.io/gh/InjectiveLabs/sdk-python)

### Dependencies

**Ubuntu**
```bash
sudo apt install python3.X-dev autoconf automake build-essential libffi-dev libtool pkg-config
```
**Fedora**
```bash
sudo dnf install python3-devel autoconf automake gcc gcc-c++ libffi-devel libtool make pkgconfig
```

**macOS**

```bash
brew install autoconf automake libtool bufbuild/buf/buf
```

### Quick Start
Installation
```bash
pip install injective-py
```

### Usage
Requires Python 3.9+
Please install `poetry` following the steps described in the [documentation](https://python-poetry.org/docs/#installation)

[Examples](https://github.com/InjectiveLabs/sdk-python/tree/master/examples)
```bash
$ poetry install

# connecting to Injective Exchange API
# and listening for new orders from a specific spot market
$ poetry run python examples/exchange_client/spot_exchange_rpc/8_StreamOrderbookUpdate.py

# sending a msg with bank transfer
# signs and posts a transaction to the Injective Chain
$ poetry run python examples/chain_client/bank/1_MsgSend.py
```
Upgrade `pip` to the latest version, if you see these warnings:
  ```
  WARNING: Value for scheme.platlib does not match. Please report this to <https://github.com/pypa/pip/issues/10151>
  WARNING: Additional context:   user = True   home = None   root = None   prefix = None
  ```

### Development
1. Generate proto binding & build
  ```
  make gen
  poetry build
  ```

2. Install pkg
  ```
  # from local build
  pip uninstall injective-py
  pip install injective-py --no-index --find-links /path/to/injective/sdk-python/dist

  # from pypi
  pip uninstall injective-py
  pip install injective-py
  ```

3. Run all unit tests in a development environment
```
poetry run pytest -v
```

---

## Choose Exchange V1 or Exchange V2 queries

The Injective Python SDK provides two different clients for interacting with the exchange:

1. **Exchange V1 Client** (`async_client` module):
   - Use this client if you need to interact with the original Injective Exchange API
   - Import using: `from injective.async_client import AsyncClient`
   - Suitable for applications that need to maintain compatibility with the original exchange interface
   - Example:
   ```python
   from injective.async_client import AsyncClient
   from injective.network import Network

   async def main():
       # Initialize client with mainnet
       client = AsyncClient(network=Network.mainnet())
       # Or use testnet
       # client = AsyncClient(network=Network.testnet())
       # Use V1 exchange queries here
   ```

2. **Exchange V2 Client** (`async_client_v2` module):
   - Use this client for the latest exchange features and improvements
   - Import using: `from injective.async_client_v2 import AsyncClient`
   - Recommended for new applications and when you need access to the latest exchange features
   - Example:
   ```python
   from injective.async_client_v2 import AsyncClient
   from injective.network import Network

   async def main():
       # Initialize client with mainnet
       client = AsyncClient(network=Network.mainnet())
       # Or use testnet
       # client = AsyncClient(network=Network.testnet())
       # Use V2 exchange queries here
   ```

Both clients provide similar interfaces but with different underlying implementations. Choose V2 for new projects unless you have specific requirements for V1 compatibility.

> **Market Format Differences**:
> - V1 AsyncClient: Markets are initialized with values in chain format (raw blockchain values)
> - V2 AsyncClient: Markets are initialized with values in human-readable format (converted to standard decimal numbers)
>
> **Exchange Endpoint Format Differences**:
> - V1 Exchange endpoints: All values (amounts, prices, margins, notionals) are returned in chain format
> - V2 Exchange endpoints:
>   - Human-readable format for: amounts, prices, margins, and notionals
>   - Chain format for: deposit-related information (to maintain consistency with the Bank module)
>
> **Important Note**: The ChainClient (V1) will not receive any new endpoints added to the Exchange module. If you need access to new exchange-related endpoints or features, you should migrate to the V2 client. The V2 client ensures you have access to all the latest exchange functionality and improvements.

___

## License

Copyright © 2021 - 2025 Injective Labs Inc. (https://injectivelabs.org/)

<a href="https://drive.google.com/uc?export=view&id=1-fPQRh_D_dnun2yTtSsPW5MypVBOVYJP"><img src="https://drive.google.com/uc?export=view&id=1-fPQRh_D_dnun2yTtSsPW5MypVBOVYJP" style="width: 300px; max-width: 100%; height: auto" />

Originally released by Injective Labs Inc. under: <br />
Apache License <br />
Version 2.0, January 2004 <br />
http://www.apache.org/licenses/
