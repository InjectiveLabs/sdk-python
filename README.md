## Injective Python SDK

WIP

Note: Apple `M1` processor is not supported

### Dependences

**Ubuntu**
```bash
sudo apt install python3.9-dev
```
**Fedora**
```bash
sudo dnf install python3-devel
```
### Quick Start
```bash
pip install injective-py
```

### Usage
Requires Python 3.9+

```bash
$ pipenv shell
$ pipenv install

# connecting to Injective Exchange API
# and listening for new orders
$ python src/exchange_api/examples/example.py

# sending a msg with bank transfer
# signs and posts a Tx to the Injective Chain
$ python src/chainclient/examples/example.py
```
Upgrade `pip` to the latest version, if you see these warnings:
```
WARNING: Value for scheme.platlib does not match. Please report this to <https://github.com/pypa/pip/issues/10151>    
WARNING: Additional context:   user = True   home = None   root = None   prefix = None
```

### Development

To copy proto schemas and regenerate GRPC clients:

```bash
$ pipenv shell
$ pipenv install --dev

$ make copy-proto
$ make gen
```

### Quick Start
```python
import injective.chain_client
import injective.exchange_api
```
## License

Apache Software License 2.0
