all:

gen: gen-client

gen-client: copy-proto
	python -m grpc_tools.protoc -I./exchange_api/pb/ \
		--python_out=./exchange_api/src/ \
		--grpc_python_out=./exchange_api/src/ \
		./exchange_api/pb/injective_exchange_rpc.proto ./exchange_api/pb/injective_spot_exchange_rpc.proto ./exchange_api/pb/injective_derivative_exchange_rpc.proto	

copy-proto:
	mkdir -p exchange_api/pb/
	cp ../injective-exchange/api/gen/grpc/injective_exchange_rpc/pb/injective_exchange_rpc.proto exchange_api/pb/
	cp ../injective-exchange/api/gen/grpc/injective_spot_exchange_rpc/pb/injective_spot_exchange_rpc.proto exchange_api/pb/
	cp ../injective-exchange/api/gen/grpc/injective_derivative_exchange_rpc/pb/injective_derivative_exchange_rpc.proto exchange_api/pb/

.PHONY: gen gen-client copy-proto
