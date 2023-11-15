all:

gen: gen-client

gen-client: clone-all copy-proto
	@for dir in $(shell find ./proto -path -prune -o -name '*.proto' -print0 | xargs -0 -n1 dirname | sort | uniq); do \
		mkdir -p ./pyinjective/$${dir}; \
		python3 -m grpc_tools.protoc \
		-I proto \
		--python_out=./pyinjective/proto \
		--grpc_python_out=./pyinjective/proto \
		$$(find ./$${dir} -type f -name '*.proto'); \
	done; \
	rm -rf proto
	$(call clean_repos)
	echo "import os\nimport sys\n\nsys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))" > pyinjective/proto/__init__.py

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
	git clone https://github.com/InjectiveLabs/injective-core.git -b v1.12.5-testnet --depth 1 --single-branch

clone-injective-indexer:
	git clone https://github.com/InjectiveLabs/injective-indexer.git -b v1.12.45-rc5 --depth 1 --single-branch

clone-cometbft:
	git clone https://github.com/cometbft/cometbft.git -b v0.37.2 --depth 1 --single-branch

clone-wasmd:
	git clone https://github.com/InjectiveLabs/wasmd.git -b v0.40.2-inj --depth 1 --single-branch

clone-cosmos-sdk:
	git clone https://github.com/InjectiveLabs/cosmos-sdk.git -b v0.47.3-inj-6 --depth 1 --single-branch

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
