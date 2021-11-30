all:

EXCHANGE_PROTO_FILES=$(shell find ../injective-exchange/api/gen/grpc -type f -name '*.proto')
PROTO_DIRS=$(shell find ./proto -path -prune -o -name '*.proto' -print0 | xargs -0 -n1 dirname | sort | uniq)
gen: gen-client

gen-client: copy-proto
	@for dir in $(PROTO_DIRS); do \
		mkdir -p ./pyinjective/$${dir}; \
		python3 -m grpc_tools.protoc \
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
	cp -r ../injective-core/proto/injective proto/
	cp -r ../injective-core/third_party/proto/* proto/
	@for file in $(EXCHANGE_PROTO_FILES); do \
		cp "$${file}" proto/exchange/; \
  done

.PHONY: all gen gen-client copy-proto
