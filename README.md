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
**0.5.8.4**
* Adjust block and timeouts to new block time
* Set explicit version for protobuf and grpcio-tool dependencies
* Add order_types as a request param for OrdersHistory
* Re-gen proto files

**0.5.8.2**
* Add global load balancer
* Refactor secure client initialization

**0.5.7.9**
* Add support for conditional orders & order mask
* Add support for custom network
* Add chain event streaming support
* Re-gen proto files

**0.5.7.8**
* Add state as a request param in OrdersHistory
* Add market_id as an optional param in Positions
* Re-gen proto files

**0.5.7.7**
* Add start_time and end_time in TradesRequest

**0.5.7.6**
* Add OrdersHistory
* Add SendToInjective
* Add MsgRewardsOptOut
* Re-gen ini files


## License

Apache Software License 2.0
