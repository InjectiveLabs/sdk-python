all:

gen: gen-client

gen-client: clone-all copy-proto
	mkdir -p ./pyinjective/proto
	cd ./proto && buf generate --template ../buf.gen.yaml
	rm -rf proto
	$(call clean_repos)
	touch pyinjective/proto/__init__.py
	$(MAKE) fix-proto-imports

PROTO_MODULES := cosmwasm exchange gogoproto cosmos_proto cosmos testpb ibc amino tendermint injective
fix-proto-imports:
	@for module in $(PROTO_MODULES); do \
  		find ./pyinjective/proto -type f -name "*.py" -exec sed -i "" -e "s/from $${module}/from pyinjective.proto.$${module}/g" {} \; ; \
	done
	@find ./pyinjective/proto -type f -name "*.py" -exec sed -i "" -e "s/from google.api/from pyinjective.proto.google.api/g" {} \;

define clean_repos
	rm -Rf cosmos-sdk
	rm -Rf ibc-go
	rm -Rf cometbft
	rm -Rf wasmd
	rm -Rf injective-core
	rm -Rf injective-indexer
endef

clean-all:
	$(call clean_repos)

clone-injective-core:
	git clone https://github.com/InjectiveLabs/injective-core.git -b v1.12.1 --depth 1 --single-branch

clone-injective-indexer:
	git clone https://github.com/InjectiveLabs/injective-indexer.git -b v1.12.79.1 --depth 1 --single-branch

clone-cometbft:
	git clone https://github.com/InjectiveLabs/cometbft.git -b v0.37.2-inj --depth 1 --single-branch
	rm cometbft/buf.yaml

clone-wasmd:
	git clone https://github.com/InjectiveLabs/wasmd.git -b v0.45.0-inj --depth 1 --single-branch

clone-cosmos-sdk:
	git clone https://github.com/InjectiveLabs/cosmos-sdk.git -b v0.47.3-inj-9 --depth 1 --single-branch

clone-ibc-go:
	git clone https://github.com/InjectiveLabs/ibc-go.git -b v7.2.0-inj --depth 1 --single-branch

clone-all: clone-cosmos-sdk clone-cometbft clone-ibc-go clone-wasmd clone-injective-core clone-injective-indexer

copy-proto:
	rm -rf pyinjective/proto
	mkdir -p proto/exchange
	buf export ./cosmos-sdk --output=third_party
	buf export ./ibc-go --exclude-imports --output=third_party
	buf export ./cometbft --exclude-imports --output=third_party
	buf export ./wasmd --exclude-imports --output=third_party
	buf export https://github.com/cosmos/ics23.git --exclude-imports --output=third_party
	cp -r injective-core/proto/injective proto/
	cp -r third_party/* proto/

	rm -rf ./third_party

	find ./injective-indexer/api/gen/grpc -type f -name "*.proto" -exec cp {} ./proto/exchange/ \;

tests:
	poetry run pytest -v

.PHONY: all gen gen-client copy-proto tests
