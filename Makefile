all:

EXCHANGE_PROTO_FILES=$(shell find ../injective-indexer/api/gen/grpc -type f -name '*.proto')
PROTO_DIRS=$(shell find ./proto -path -prune -o -name '*.proto' -print0 | xargs -0 -n1 dirname | sort | uniq)
gen: gen-client

gen-client: copy-proto
	@for dir in $(PROTO_DIRS); do \
		mkdir -p ./pyinjective/$${dir}; \
		python3.10 -m grpc_tools.protoc \
		-I proto \
		--python_out=./pyinjective/proto \
		--grpc_python_out=./pyinjective/proto \
		$$(find ./$${dir} -type f -name '*.proto'); \
	done; \
	rm -rf proto
	echo "import os\nimport sys\n\nsys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))" > pyinjective/proto/__init__.py

copy-proto:
	rm -rf pyinjective/proto
	mkdir -p proto/exchange
	buf export buf.build/cosmos/cosmos-sdk:v0.47.0 --output=third_party
	buf export https://github.com/cosmos/ibc-go.git --exclude-imports --output=third_party
	buf export https://github.com/tendermint/tendermint.git --exclude-imports --output=third_party
	buf export https://github.com/CosmWasm/wasmd.git --exclude-imports --output=./third_party
	buf export https://github.com/cosmos/ics23.git --exclude-imports --output=./third_party

	cp -r ../injective-core/proto/injective proto/
	cp -r ./third_party/* proto/

	rm -rf ./third_party

	@for file in $(EXCHANGE_PROTO_FILES); do \
		cp "$${file}" proto/exchange/; \
  done

.PHONY: all gen gen-client copy-proto
