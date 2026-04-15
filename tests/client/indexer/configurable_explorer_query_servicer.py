from collections import deque

from pyinjective.proto.exchange import (
    injective_explorer_rpc_pb2 as exchange_explorer_pb,
    injective_explorer_rpc_pb2_grpc as exchange_explorer_grpc,
)


class ConfigurableExplorerQueryServicer(exchange_explorer_grpc.InjectiveExplorerRPCServicer):
    def __init__(self):
        super().__init__()
        self.account_txs_responses = deque()
        self.contract_txs_responses = deque()
        self.blocks_responses = deque()
        self.block_responses = deque()
        self.validators_responses = deque()
        self.validator_responses = deque()
        self.validator_uptime_responses = deque()
        self.txs_responses = deque()
        self.tx_by_tx_hash_responses = deque()
        self.peggy_deposit_txs_responses = deque()
        self.peggy_withdrawal_txs_responses = deque()
        self.ibc_transfer_txs_responses = deque()
        self.wasm_codes_responses = deque()
        self.wasm_code_by_id_responses = deque()
        self.wasm_contracts_responses = deque()
        self.wasm_contract_by_address_responses = deque()
        self.cw20_balance_responses = deque()
        self.relayers_responses = deque()
        self.bank_transfers_responses = deque()

        self.stream_txs_responses = deque()
        self.stream_blocks_responses = deque()

        # Add new attribute for contract_txs_v2_responses
        self.contract_txs_v2_responses = deque()

    async def GetAccountTxs(self, request: exchange_explorer_pb.GetAccountTxsRequest, context=None, metadata=None):
        return self.account_txs_responses.pop()

    async def GetContractTxs(self, request: exchange_explorer_pb.GetContractTxsRequest, context=None, metadata=None):
        return self.contract_txs_responses.pop()

    async def GetBlocks(self, request: exchange_explorer_pb.GetBlocksRequest, context=None, metadata=None):
        return self.blocks_responses.pop()

    async def GetBlock(self, request: exchange_explorer_pb.GetBlockRequest, context=None, metadata=None):
        return self.block_responses.pop()

    async def GetValidators(self, request: exchange_explorer_pb.GetValidatorsRequest, context=None, metadata=None):
        return self.validators_responses.pop()

    async def GetValidator(self, request: exchange_explorer_pb.GetValidatorRequest, context=None, metadata=None):
        return self.validator_responses.pop()

    async def GetValidatorUptime(
        self, request: exchange_explorer_pb.GetValidatorUptimeRequest, context=None, metadata=None
    ):
        return self.validator_uptime_responses.pop()

    async def GetTxs(self, request: exchange_explorer_pb.GetTxsRequest, context=None, metadata=None):
        return self.txs_responses.pop()

    async def GetTxByTxHash(self, request: exchange_explorer_pb.GetTxByTxHashRequest, context=None, metadata=None):
        return self.tx_by_tx_hash_responses.pop()

    async def GetPeggyDepositTxs(
        self, request: exchange_explorer_pb.GetPeggyDepositTxsRequest, context=None, metadata=None
    ):
        return self.peggy_deposit_txs_responses.pop()

    async def GetPeggyWithdrawalTxs(
        self, request: exchange_explorer_pb.GetPeggyWithdrawalTxsRequest, context=None, metadata=None
    ):
        return self.peggy_withdrawal_txs_responses.pop()

    async def GetIBCTransferTxs(
        self, request: exchange_explorer_pb.GetIBCTransferTxsRequest, context=None, metadata=None
    ):
        return self.ibc_transfer_txs_responses.pop()

    async def GetWasmCodes(self, request: exchange_explorer_pb.GetWasmCodesRequest, context=None, metadata=None):
        return self.wasm_codes_responses.pop()

    async def GetWasmCodeByID(self, request: exchange_explorer_pb.GetWasmCodeByIDRequest, context=None, metadata=None):
        return self.wasm_code_by_id_responses.pop()

    async def GetWasmContracts(
        self, request: exchange_explorer_pb.GetWasmContractsRequest, context=None, metadata=None
    ):
        return self.wasm_contracts_responses.pop()

    async def GetWasmContractByAddress(
        self, request: exchange_explorer_pb.GetWasmContractByAddressRequest, context=None, metadata=None
    ):
        return self.wasm_contract_by_address_responses.pop()

    async def GetCw20Balance(self, request: exchange_explorer_pb.GetCw20BalanceRequest, context=None, metadata=None):
        return self.cw20_balance_responses.pop()

    async def Relayers(self, request: exchange_explorer_pb.RelayersRequest, context=None, metadata=None):
        return self.relayers_responses.pop()

    async def GetBankTransfers(
        self, request: exchange_explorer_pb.GetBankTransfersRequest, context=None, metadata=None
    ):
        return self.bank_transfers_responses.pop()

    async def StreamTxs(self, request: exchange_explorer_pb.StreamTxsRequest, context=None, metadata=None):
        for event in self.stream_txs_responses:
            yield event

    async def StreamBlocks(self, request: exchange_explorer_pb.StreamBlocksRequest, context=None, metadata=None):
        for event in self.stream_blocks_responses:
            yield event

    async def GetContractTxsV2(
        self, request: exchange_explorer_pb.GetContractTxsV2Request, context=None, metadata=None
    ):
        return self.contract_txs_v2_responses.pop()
