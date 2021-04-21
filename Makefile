all:

gen: gen-client

gen-client: copy-proto
	python -m grpc_tools.protoc -I./grpc_client/pb/ \
		--python_out=./grpc_client/src/ \
		--grpc_python_out=./grpc_client/src/ \
		./grpc_client/pb/injective_exchange_rpc.proto ./grpc_client/pb/injective_spot_markets_rpc.proto		

copy-proto:
	mkdir -p grpc_client/pb/
	cp ../injective-exchange/api/gen/grpc/injective_exchange_rpc/pb/injective_exchange_rpc.proto grpc_client/pb/
	cp ../injective-exchange/api/gen/grpc/injective_spot_markets_rpc/pb/injective_spot_markets_rpc.proto grpc_client/pb/

.PHONY: gen gen-client copy-proto
