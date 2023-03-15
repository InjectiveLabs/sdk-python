# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/wasmx/v1/proposal.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmwasm.wasm.v1 import proposal_pb2 as cosmwasm_dot_wasm_dot_v1_dot_proposal__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!injective/wasmx/v1/proposal.proto\x12\x12injective.wasmx.v1\x1a\x14gogoproto/gogo.proto\x1a\x1f\x63osmwasm/wasm/v1/proposal.proto\"\xb1\x01\n#ContractRegistrationRequestProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\\\n\x1d\x63ontract_registration_request\x18\x03 \x01(\x0b\x32/.injective.wasmx.v1.ContractRegistrationRequestB\x04\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xb7\x01\n(BatchContractRegistrationRequestProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12]\n\x1e\x63ontract_registration_requests\x18\x03 \x03(\x0b\x32/.injective.wasmx.v1.ContractRegistrationRequestB\x04\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"l\n#BatchContractDeregistrationProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x17\n\tcontracts\x18\x03 \x03(\tB\x04\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xc0\x01\n\x1b\x43ontractRegistrationRequest\x12\x18\n\x10\x63ontract_address\x18\x01 \x01(\t\x12\x11\n\tgas_limit\x18\x02 \x01(\x04\x12\x11\n\tgas_price\x18\x03 \x01(\x04\x12\x1b\n\x13should_pin_contract\x18\x04 \x01(\x08\x12\x1c\n\x14is_migration_allowed\x18\x05 \x01(\x08\x12\x0f\n\x07\x63ode_id\x18\x06 \x01(\x04\x12\x15\n\radmin_address\x18\x07 \x01(\t\"\x84\x01\n\x16\x42\x61tchStoreCodeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12<\n\tproposals\x18\x03 \x03(\x0b\x32#.cosmwasm.wasm.v1.StoreCodeProposalB\x04\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x42MZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/wasmx/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.wasmx.v1.proposal_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/wasmx/types'
  _CONTRACTREGISTRATIONREQUESTPROPOSAL.fields_by_name['contract_registration_request']._options = None
  _CONTRACTREGISTRATIONREQUESTPROPOSAL.fields_by_name['contract_registration_request']._serialized_options = b'\310\336\037\000'
  _CONTRACTREGISTRATIONREQUESTPROPOSAL._options = None
  _CONTRACTREGISTRATIONREQUESTPROPOSAL._serialized_options = b'\350\240\037\000\210\240\037\000'
  _BATCHCONTRACTREGISTRATIONREQUESTPROPOSAL.fields_by_name['contract_registration_requests']._options = None
  _BATCHCONTRACTREGISTRATIONREQUESTPROPOSAL.fields_by_name['contract_registration_requests']._serialized_options = b'\310\336\037\000'
  _BATCHCONTRACTREGISTRATIONREQUESTPROPOSAL._options = None
  _BATCHCONTRACTREGISTRATIONREQUESTPROPOSAL._serialized_options = b'\350\240\037\000\210\240\037\000'
  _BATCHCONTRACTDEREGISTRATIONPROPOSAL.fields_by_name['contracts']._options = None
  _BATCHCONTRACTDEREGISTRATIONPROPOSAL.fields_by_name['contracts']._serialized_options = b'\310\336\037\000'
  _BATCHCONTRACTDEREGISTRATIONPROPOSAL._options = None
  _BATCHCONTRACTDEREGISTRATIONPROPOSAL._serialized_options = b'\350\240\037\000\210\240\037\000'
  _BATCHSTORECODEPROPOSAL.fields_by_name['proposals']._options = None
  _BATCHSTORECODEPROPOSAL.fields_by_name['proposals']._serialized_options = b'\310\336\037\000'
  _BATCHSTORECODEPROPOSAL._options = None
  _BATCHSTORECODEPROPOSAL._serialized_options = b'\350\240\037\000\210\240\037\000'
  _CONTRACTREGISTRATIONREQUESTPROPOSAL._serialized_start=113
  _CONTRACTREGISTRATIONREQUESTPROPOSAL._serialized_end=290
  _BATCHCONTRACTREGISTRATIONREQUESTPROPOSAL._serialized_start=293
  _BATCHCONTRACTREGISTRATIONREQUESTPROPOSAL._serialized_end=476
  _BATCHCONTRACTDEREGISTRATIONPROPOSAL._serialized_start=478
  _BATCHCONTRACTDEREGISTRATIONPROPOSAL._serialized_end=586
  _CONTRACTREGISTRATIONREQUEST._serialized_start=589
  _CONTRACTREGISTRATIONREQUEST._serialized_end=781
  _BATCHSTORECODEPROPOSAL._serialized_start=784
  _BATCHSTORECODEPROPOSAL._serialized_end=916
# @@protoc_insertion_point(module_scope)
