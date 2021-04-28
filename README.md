## Injective Python SDK

WIP

### Usage

```
$ pipenv shell
$ pipenv install

$ python exchange_api/src/main.py
```

### Development

To copy proto schemas and regenerate GRPC clients:

```
$ pipenv shell
$ pipenv install --dev

$ make copy-proto
$ make gen
```

## License

Apache 2.0
