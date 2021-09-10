all:

EXCHANGE_PROTO_FILES=$(shell find ../injective-exchange/api/gen/grpc -type f -name '*.proto')
PROTO_DIRS=$(shell find ./proto -path -prune -o -name '*.proto' -print0 | xargs -0 -n1 dirname | sort | uniq)
gen: gen-client

gen-client: copy-proto
	@for dir in $(PROTO_DIRS); do \
		mkdir -p ./src/$${dir}; \
		python -m grpc_tools.protoc \
		-I proto \
		--python_out=./src/proto \
		--grpc_python_out=./src/proto \
		$$(find $${dir} -type file -name '*.proto'); \
	done; \
	rm -rf proto
	touch src/proto/__init__.py

# gen-client: copy-proto
# 	@for dir in $(PROTO_DIRS); do \
# 		mkdir -p ./src/$${dir}; \
# 		python -m grpc_tools.protoc \
# 		-I proto \
# 		--python_betterproto_out=./src/$${dir} \
# 		$$(find $${dir} -type file -name '*.proto'); \
# 	done; \
# 	rm -rf proto
# 	touch src/proto/__init__.py

copy-proto:
	rm -rf src/proto
	mkdir -p proto/exchange
	cp -r ../injective-core/proto/injective proto/
	cp -r ../injective-core/third_party/proto/ proto/
	@for file in $(EXCHANGE_PROTO_FILES); do \
		cp "$${file}" proto/exchange/; \
  done

.PHONY: all gen gen-client copy-proto
