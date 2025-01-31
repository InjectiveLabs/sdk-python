all: gen

gen: gen-client

gen-client:
	mkdir -p ./pyinjective/proto
	buf generate --template buf.gen.yaml
	rm -rf proto
	$(call clean_repos)
	$(MAKE) fix-generated-proto-imports-1

PROTO_MODULES := cosmwasm gogoproto cosmos_proto cosmos testpb ibc amino tendermint injective

fix-generated-proto-imports-1:
	@touch pyinjective/proto/__init__.py
	@for module in $(PROTO_MODULES); do \
		find ./pyinjective/proto -type f -name "*.py" -exec sed -i "s/from $${module}/from pyinjective.proto.$${module}/g" {} \; ; \
	done
	@find ./pyinjective/proto -type f -name "*.py" -exec sed -i "s/from google.api/from pyinjective.proto.google.api/g" {} \;
fix-generated-proto-imports:
	@echo "Listing all Python files in pyinjective/proto:"
	@find ./pyinjective/proto -type f -name "*.py" -ls
	@echo "\nModules that will be processed:"
	@for module in $(PROTO_MODULES); do \
		echo "$$module"; \
	done

define clean_repos
	rm -Rf cosmos-sdk
	rm -Rf ibc-go
	rm -Rf cometbft
	rm -Rf wasmd
	rm -Rf injective-core
endef

clean-all:
	$(call clean_repos)
tests:
	poetry run pytest -v

.PHONY: all gen gen-client copy-proto tests
