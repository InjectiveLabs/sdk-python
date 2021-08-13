## Injective Python SDK

WIP

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

### Development

To copy proto schemas and regenerate GRPC clients:

```bash
$ pipenv shell
$ pipenv install --dev

$ make copy-proto
$ make gen
```

## License

Apache 2.0
