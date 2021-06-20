all:

gen: gen-client

gen-client: copy-proto
	python -m grpc_tools.protoc -I./exchange_api/pb/ \
		--python_out=./exchange_api/ \
		--grpc_python_out=./exchange_api/ \
		$(shell find ./exchange_api/pb -type f -name '*.proto')

SRC_PROTO_FILES = $(shell find ../injective-exchange/api/gen/grpc -type f -name '*.proto')

copy-proto:
	mkdir -p exchange_api/pb/
	@for file in $(SRC_PROTO_FILES) ; do \
  		cp "$${file}" exchange_api/pb/ ;\
  	done

.PHONY: all gen gen-client copy-proto
