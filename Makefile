all:

gen: gen-client

gen-client:
	git clone --depth 1 --branch v1.13.2 https://github.com/InjectiveLabs/injective-core
	mkdir -p proto
	
	cp -r injective-core/proto/* proto/
	mkdir -p ./pyinjective/proto
	buf generate --template buf.gen.yaml
	rm -rf proto
	$(call clean_repos)
	$(MAKE) fix-generated-proto-imports

PROTO_MODULES := cosmwasm gogoproto cosmos_proto cosmos testpb ibc amino tendermint injective

fix-generated-proto-imports:
	@touch pyinjective/proto/__init__.py
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
tests:
	poetry run pytest -v

.PHONY: all gen gen-client copy-proto tests
