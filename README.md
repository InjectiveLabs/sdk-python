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

For installing `bip32` module specifically:

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
$ python examples/sync/exchange_client/spot_exchange_rpc/8_StreamOrders.py

# sending a msg with bank transfer
# signs and posts a transaction to the Injective Chain
$ python examples/sync/chain_client/1_MsgSend.py
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


### Changelogs
**0.5.6.3**
* Update the testnet ini file

**0.5.6.2**
* Add authz support in composer and client
* Add historical rewards for Trade & Earn

**0.5.6.1**
* Add devnet ini to local env

**0.5.6.0**
* Add local env in networks

**0.5.5.9**
* Add MsgBatchUpdateOrders to the composer
* Add skip/limit parameters to funding payments

**0.5.5.8**
* Fix stream_bids in async client
* Add more messages in MsgResponses for simulation

**0.5.5.5**
* Refactor LCD endpoints
* Regen ini files

**0.5.5.1**
* Add ATOM back to denoms_mainnet.ini

**0.5.5**
* Added MsgBid to the Composer and provided an example
* Refactored the clients and composer with kwargs for optional arguments

**0.5.4**
* Added PortfolioRequest, GetTxByHashRequest, AuctionRequest, AuctionsRequest, StreamBidsRequest and provided examples
* Updated the composer with MsgIncreasePosition and MsgLiquidatePosition
* Added reduce-only orders to the composer and updated examples

**0.5.3**
* Add skip, and limit to trade request

**0.5.2**
* Add sync init_num_seq, changed previous init_num_seq to async_init_num_seq
* Add staging mainnet endpoint, update market metadata
* Protobuf regen
* Response parser improvements
* Fix type hints

**0.5.1**
* Add AsyncClient
* Add MetaRPC API

**0.4.8**
* Add tokyo as optional API node option for mainnet
* Improve conversion utils, include gas estimation in simulation response
* Update exchange client
* Add display fields, update ini files, fix derv quantity conversion
* Minor format fixes

**0.4.5**
* Wrap exchange grpc client into Client class.
* Add Single-threaded pending sequence management.

**0.4.4**
* Allow to parse one or multiple exchange responses in simulation/tx response data.
* Add simulation before broadcasting tx for gas estimation and error preview.
* Add devnet to network options.




## License

Apache Software License 2.0
