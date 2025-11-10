all:

gen: gen-client

gen-client: clone-all copy-proto
	mkdir -p ./pyinjective/proto
	buf generate --template buf.gen.yaml
	rm -rf proto
	$(call clean_repos)
	$(MAKE) fix-generated-proto-imports

PROTO_MODULES := cosmwasm exchange gogoproto cosmos_proto cosmos testpb ibc amino tendermint cometbft injective

fix-generated-proto-imports:
	@touch pyinjective/proto/__init__.py
	@for module in $(PROTO_MODULES); do \
  		find ./pyinjective/proto -type f -name "*.py" -exec sed -i "" -e "s/from $${module}/from pyinjective.proto.$${module}/g" {} \; ; \
	done
	@find ./pyinjective/proto -type f -name "*.py" -exec sed -i "" -e "s/from google.api/from pyinjective.proto.google.api/g" {} \;

define clean_repos
	rm -Rf injective-indexer
endef

clean-all:
	$(call clean_repos)

clone-injective-indexer:
	git clone https://github.com/InjectiveLabs/injective-indexer.git -b v1.17.16 --depth 1 --single-branch

clone-all: clone-injective-indexer

copy-proto:
	rm -rf pyinjective/proto
	mkdir -p proto/exchange
	find ./injective-indexer/api/gen/grpc -type f -name "*.proto" -exec cp {} ./proto/exchange/ \;

tests:
	poetry run pytest -v

.PHONY: all gen gen-client copy-proto tests
