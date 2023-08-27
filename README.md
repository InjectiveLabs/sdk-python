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

5. Install the development environment (requires `pipenv`)
```
pipenv install -d
```

6. Run all unit tests in a development environment
```
make tests
```

### Changelogs
**0.7.2.1**
* Synchronization of denoms configuration files.

**0.7.2**
* Added a new gas limit calculation for the TransactionBroadcaster that estimates the value based on the messages in the transaction (without running the transaction simulation).

**0.7.1.2**
* Add NBLA

**0.7.1.1**
* Fixed Testnet network URLs

**0.7.1**
* Include implementation of the TransactionBroadcaster, to simplify the transaction creation and broadcasting process.

**0.7.0.6**
* ADD SEI/USDT in metadata

**0.7.0.5**
* Added the required logic in the MsgSubaccountTransfer message to translate amounts and token into the correct amount and token name representation for the chain

**0.7.0.4**
* Synchronized decimals for ATOM and WETH in Testnet with the configuration provided by the indexer

**0.7.0.3**
* Add FRCOIN testnet

**0.7.0.2**
* Removed from AsyncClient all references to the deprecated OrderBook RPC endpoints (replaced them with OrderBookV2)
* Updated all orderbook examples

**0.7**
* Removed references to pysha3 library (and also eip712-struct that required it) and replaced it with other implementation to allow the project to work with Python 3.11
* Updated sentry nodes LCD URL, for each sentry node to use its own service

**0.6.5**
* Removed `k8s` from the list of supported mainnet nodes (`lb` should be used instead)

**0.6.4**
* Change logging logic to use different loggers for each module and class
* Solved issue preventing requesting spot and derivative historical orders for more than one market_id
* Add `pytest` as a development dependency to implement and run unit tests

**0.6.3.3**
* Update the code to the new structure of transaction responses

**0.6.3.1**
* Update the code to the new structure of transaction simulation responses

**0.6.2.7**
* Fix margin calculation in utils

**0.6.2.1**
* Remove version deps from Pipfile

**0.6.2.0**
* Add MsgUnderwrite, MsgRequestRedemption in Composer

**0.6.1.8**
* Add MsgCreateInsuranceFund in Composer
* Re-gen mainnet denoms

**0.6.1.5**
* Add MsgExecuteContract in Composer

**0.6.1.4**
* Add wMATIC

**0.6.1.2**
* Add OrderbookV2 method in async client

**0.6.1.1**
* Add ARB/USDT

**0.6.0.9**
* Deprecate K8S and set LB as default
* Proto re-gen

**0.6.0.8**
* Add USDCfr

**0.6.0.7**
* Add LDO

**0.6.0.6**
* Set default testnet endpoints to K8S
* Remove LB config for testnet
* Fix relative imports in composer
* Add AccountPortfolio & StreamAccountPortfolio

**0.6.0.5**
* Add new testnet endpoints
* Re-gen mainnet denoms

**0.6.0.4**
* Remove explicit versions from protobuf and grpcio-tools dependencies

**0.6.0.2**
* Re-gen mainnet denoms

**0.6.0.0**
* Change default network to LB
* Re-gen mainnet denoms

**0.5.9.7**
* Re-gen mainnet denoms

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

