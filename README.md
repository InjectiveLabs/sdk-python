## Injective Python SDK

### Dependences

**Ubuntu**
```bash
sudo apt install python3.X-dev
```
**Fedora**
```bash
sudo dnf install python3-devel
```
### Quick Start
Installation
```bash
pip install injective-py
```
Example usage
```python
from pyinjective.composer import Composer as ProtoMsgComposer
from pyinjective.client import Client
from pyinjective.transaction import Transaction
from pyinjective.constant import Network
from pyinjective.wallet import PrivateKey, PublicKey, Address

```

### Usage
Requires Python 3.7+

[Examples](https://github.com/InjectiveLabs/sdk-python/tree/master/examples)
```bash
$ pipenv shell
$ pipenv install

# connecting to Injective Exchange API
# and listening for new orders from one specific spot market
$ python examples/exchange_api_examples/spot_exchange_rpc/8_StreamOrdersRequest.py

# sending a msg with bank transfer
# signs and posts a Tx to the Injective Chain
$ python examples/chain_client_examples/1_CosmosBankMsgSend.py
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

1. Enable dev env
```
pipenv shell
pipenv install --dev
```

1. Install pkg
```
# from local build
pip uninstall injective-py
pip install injective-py --no-index --find-links /path/to/injective/sdk-python/dist

# from pypi
pip uninstall injective-py
pip install injective-py
```

1. Fetch latest denom config
```
python pyinjective/fetch_metadata.py
```

1. Run an example
```
python examples/chain_client_examples/1_CosmosBankMsgSend.py
```

## License

Apache Software License 2.0
