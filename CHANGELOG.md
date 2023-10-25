# Changelog

All notable changes to this project will be documented in this file.

## [0.10.0] - 2023-10-04
### Added
- Added logic to support use of Client Order ID (CID) new identifier in OrderInfo
- New chain stream support

### Changed
- Moved changelog from the README.md file to its own CHANGELOG.md file
- Remove `aiocron` dependency. Use plain asyncio tasks to solve the timeout height synchronization

## [0.9.3]
* Updated TIA/USDT-30NOV2023 market id in denoms_mainnet.ini file

## [0.9.2]
* Added fix to the grpc import error in Mac with M1 and M2 chips

## [0.9.1]
* Added new spot markets in mainnet ini file: KAVA/USDT, USDTkv/USDT
* Added new derivative markets in mainnet ini file: TIA/USDT-30NOV2023, AXL/USDT, BTC/USDTkv, ETH/USDTkv

## [0.9.0]
* Improvement in broadcaster to initialize the account sequence number and the timeout height only when required
* Replace Pipenv with Poetry
* Add pre-commit validations to the project
* Add a GitHub workflow to run all tests and calculate coverage for each PR


## [0.8.5]
* Added NEOK/USDT and ORAI/USDT spot markets to the mainnet .ini file

## [0.8.4]
* Added methods to SpotMarket, DerivativeMarket and BianaryOptionMarket to translate chain prices and quantities to human-readable format.

## [0.8.3]
* Fix dependency issue in setup.py.

## [0.8.2]
* Add web3 library as a dependency for the project.

## [0.8.1]
* Moved the configuration to use a secure or insecure connection inside the Network class. The AsyncClient's `insecure` parameter is no longer used for anything and will be removed in the future.
* Made the new load balanced bare-metal node the default one for mainnet (it is called `lb`). The legacy one (load balanced k8s node) is called `lb_k8s`

## [0.8]
* Refactor Composer to be created with all the markets and tokens. The Composer now uses the real markets and tokens to convert human-readable values to chain format
* The Composer can still be instantiated without markets and tokens. When markets and tokens are not provided the Composer loads the required information from the Denoms used in previous versions
* Change in AsyncClient to be able to create Composer instances for the client network, markets and tokens
* Examples have been adapted to create Composer instances using the AsyncClient
* Added new nodes (bare-metal load balancing nodes) for mainnet and testnet
* Deprecated the kubernetes load balanced nodes for testnet
* Refactored the cookies management logic into a cookie assistant. Added the required logic to support the new cookies format for bare-metal load balanced nodes
* Removed class Client. The only supported now is the async version called AsyncClient.

## [0.7.1.1]
* Fixed Testnet network URLs

## [0.7.2.1]
* Synchronization of denoms configuration files.

## [0.7.2]
* Added a new gas limit calculation for the TransactionBroadcaster that estimates the value based on the messages in the transaction (without running the transaction simulation).

## [0.7.1.2]
* Add NBLA

## [0.7.1.1]
* Fixed Testnet network URLs

## [0.7.1]
* Include implementation of the TransactionBroadcaster, to simplify the transaction creation and broadcasting process.

## [0.7.0.6]
* ADD SEI/USDT in metadata

## [0.7.0.5]
* Added the required logic in the MsgSubaccountTransfer message to translate amounts and token into the correct amount and token name representation for the chain

## [0.7.0.4]
* Synchronized decimals for ATOM and WETH in Testnet with the configuration provided by the indexer

## [0.7.0.3]
* Add FRCOIN testnet

## [0.7.0.2]
* Removed from AsyncClient all references to the deprecated OrderBook RPC endpoints (replaced them with OrderBookV2)
* Updated all orderbook examples

## [0.7]
* Removed references to pysha3 library (and also eip712-struct that required it) and replaced it with other implementation to allow the project to work with Python 3.11
* Updated sentry nodes LCD URL, for each sentry node to use its own service

## [0.6.5]
* Removed `k8s` from the list of supported mainnet nodes (`lb` should be used instead)

## [0.6.4]
* Change logging logic to use different loggers for each module and class
* Solved issue preventing requesting spot and derivative historical orders for more than one market_id
* Add `pytest` as a development dependency to implement and run unit tests

## [0.6.3.3]
* Update the code to the new structure of transaction responses

## [0.6.3.1]
* Update the code to the new structure of transaction simulation responses

## [0.6.2.7]
* Fix margin calculation in utils

## [0.6.2.1]
* Remove version deps from Pipfile

## [0.6.2.0]
* Add MsgUnderwrite, MsgRequestRedemption in Composer

## [0.6.1.8]
* Add MsgCreateInsuranceFund in Composer
* Re-gen mainnet denoms

## [0.6.1.5]
* Add MsgExecuteContract in Composer

## [0.6.1.4]
* Add wMATIC

## [0.6.1.2]
* Add OrderbookV2 method in async client

## [0.6.1.1]
* Add ARB/USDT

## [0.6.0.9]
* Deprecate K8S and set LB as default
* Proto re-gen

## [0.6.0.8]
* Add USDCfr

## [0.6.0.7]
* Add LDO

## [0.6.0.6]
* Set default testnet endpoints to K8S
* Remove LB config for testnet
* Fix relative imports in composer
* Add AccountPortfolio & StreamAccountPortfolio

## [0.6.0.5]
* Add new testnet endpoints
* Re-gen mainnet denoms

## [0.6.0.4]
* Remove explicit versions from protobuf and grpcio-tools dependencies

## [0.6.0.2]
* Re-gen mainnet denoms

## [0.6.0.0]
* Change default network to LB
* Re-gen mainnet denoms

## [0.5.9.7]
* Re-gen mainnet denoms

## [0.5.9.6]
* Re-gen proto

## [0.5.9.5]
* Add orderbook snaphot methods

## [0.5.9.4]
* Re-gen mainnet denoms

## [0.5.9.4]
* Re-gen mainnet denoms

## [0.5.9.2]
* Fix margin conversion for binary options

## [0.5.9.1]
* Add skip/limit to BinaryOptionsMarketsRequest

## [0.5.9.0]
* Re-gen proto
* Fix MsgRewardsOptOut
* Remove pysha3 dependency

## [0.5.8.8]
* Add grpc_explorer_endpoint in Network
* Add explorer channel and stub

*BREAKING CHANGES*

- Clients using [Custom Network](https://github.com/InjectiveLabs/sdk-python/blob/master/pyinjective/constant.py#L166) must now set grpc_explorer_endpoint during init
