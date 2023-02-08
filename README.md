## Injective Python SDK

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
brew install autoconf automake libtool
```

### Quick Start
Installation
```bash
pip install injective-py
```

### Usage
Requires Python 3.7+

[Examples](https://github.com/InjectiveLabs/sdk-python/tree/master/examples)
```bash
$ pipenv shell
$ pipenv install

# connecting to Injective Exchange API
# and listening for new orders from a specific spot market
$ python examples/exchange_client/spot_exchange_rpc/8_StreamOrders.py

# sending a msg with bank transfer
# signs and posts a transaction to the Injective Chain
$ python examples/chain_client/1_MsgSend.py
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
  python -m build
  ```

2. Enable dev env
  ```
  pipenv shell
  pipenv install --dev
  ```

3. Install pkg
  ```
  # from local build
  pip uninstall injective-py
  pip install injective-py --no-index --find-links /path/to/injective/sdk-python/dist

  # from pypi
  pip uninstall injective-py
  pip install injective-py
  ```

4. Fetch latest denom config
```
python pyinjective/fetch_metadata.py
```

Note that the [sync client](https://github.com/InjectiveLabs/sdk-python/blob/master/pyinjective/client.py) has been deprecated as of April 18, 2022. If you are using the sync client please make sure to transition to the [async client](https://github.com/InjectiveLabs/sdk-python/blob/master/pyinjective/async_client.py), for more information read [here](https://github.com/InjectiveLabs/sdk-python/issues/101)


### Changelogs
**0.6.0.0**
* Change default network to LB
* Re-gen denoms mainnet

**0.5.9.7**
* Re-gen denoms mainnet

**0.5.9.6**
* Re-gen proto

**0.5.9.5**
* Add orderbook snaphot methods

**0.5.9.4**
* Re-gen mainnet denoms

**0.5.9.4**
* Re-gen mainnet denoms

**0.5.9.2**
* Fix margin conversion for binary options

**0.5.9.1**
* Add skip/limit to BinaryOptionsMarketsRequest

**0.5.9.0**
* Re-gen proto
* Fix MsgRewardsOptOut
* Remove pysha3 dependency

**0.5.8.8**
* Add grpc_explorer_endpoint in Network
* Add explorer channel and stub

*BREAKING CHANGES*

- Clients using [Custom Network](https://github.com/InjectiveLabs/sdk-python/blob/master/pyinjective/constant.py#L166) must now set grpc_explorer_endpoint during init


## License

Copyright © 2021 - 2022 Injective Labs Inc. (https://injectivelabs.org/)

<a href="https://drive.google.com/uc?export=view&id=1-fPQRh_D_dnun2yTtSsPW5MypVBOVYJP"><img src="https://drive.google.com/uc?export=view&id=1-fPQRh_D_dnun2yTtSsPW5MypVBOVYJP" style="width: 300px; max-width: 100%; height: auto" />

Originally released by Injective Labs Inc. under: <br />
Apache License <br />
Version 2.0, January 2004 <br />
http://www.apache.org/licenses/ 

