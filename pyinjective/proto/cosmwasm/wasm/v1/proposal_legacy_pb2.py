# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmwasm/wasm/v1/proposal_legacy.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from pyinjective.proto.cosmwasm.wasm.v1 import types_pb2 as cosmwasm_dot_wasm_dot_v1_dot_types__pb2
from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&cosmwasm/wasm/v1/proposal_legacy.proto\x12\x10\x63osmwasm.wasm.v1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1c\x63osmwasm/wasm/v1/types.proto\x1a\x11\x61mino/amino.proto\"\xdc\x02\n\x11StoreCodeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12(\n\x06run_as\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12(\n\x0ewasm_byte_code\x18\x04 \x01(\x0c\x42\x10\xe2\xde\x1f\x0cWASMByteCode\x12>\n\x16instantiate_permission\x18\x07 \x01(\x0b\x32\x1e.cosmwasm.wasm.v1.AccessConfig\x12\x12\n\nunpin_code\x18\x08 \x01(\x08\x12\x0e\n\x06source\x18\t \x01(\t\x12\x0f\n\x07\x62uilder\x18\n \x01(\t\x12\x11\n\tcode_hash\x18\x0b \x01(\x0c:;\x18\x01\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\x8a\xe7\xb0*\x16wasm/StoreCodeProposalJ\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07\"\x8d\x03\n\x1bInstantiateContractProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12(\n\x06run_as\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\'\n\x05\x61\x64min\x18\x04 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x1b\n\x07\x63ode_id\x18\x05 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeID\x12\r\n\x05label\x18\x06 \x01(\t\x12#\n\x03msg\x18\x07 \x01(\x0c\x42\x16\xfa\xde\x1f\x12RawContractMessage\x12_\n\x05\x66unds\x18\x08 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB5\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xa8\xe7\xb0*\x01:E\x18\x01\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\x8a\xe7\xb0* wasm/InstantiateContractProposal\"\xae\x03\n\x1cInstantiateContract2Proposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12(\n\x06run_as\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\'\n\x05\x61\x64min\x18\x04 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x1b\n\x07\x63ode_id\x18\x05 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeID\x12\r\n\x05label\x18\x06 \x01(\t\x12#\n\x03msg\x18\x07 \x01(\x0c\x42\x16\xfa\xde\x1f\x12RawContractMessage\x12_\n\x05\x66unds\x18\x08 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB5\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xa8\xe7\xb0*\x01\x12\x0c\n\x04salt\x18\t \x01(\x0c\x12\x0f\n\x07\x66ix_msg\x18\n \x01(\x08:F\x18\x01\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\x8a\xe7\xb0*!wasm/InstantiateContract2Proposal\"\xee\x01\n\x17MigrateContractProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12*\n\x08\x63ontract\x18\x04 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x1b\n\x07\x63ode_id\x18\x05 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeID\x12#\n\x03msg\x18\x06 \x01(\x0c\x42\x16\xfa\xde\x1f\x12RawContractMessage:A\x18\x01\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\x8a\xe7\xb0*\x1cwasm/MigrateContractProposal\"\xcb\x01\n\x14SudoContractProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12*\n\x08\x63ontract\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12#\n\x03msg\x18\x04 \x01(\x0c\x42\x16\xfa\xde\x1f\x12RawContractMessage:>\x18\x01\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\x8a\xe7\xb0*\x19wasm/SudoContractProposal\"\xdc\x02\n\x17\x45xecuteContractProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12(\n\x06run_as\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12*\n\x08\x63ontract\x18\x04 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12#\n\x03msg\x18\x05 \x01(\x0c\x42\x16\xfa\xde\x1f\x12RawContractMessage\x12_\n\x05\x66unds\x18\x06 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB5\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xa8\xe7\xb0*\x01:A\x18\x01\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\x8a\xe7\xb0*\x1cwasm/ExecuteContractProposal\"\xe5\x01\n\x13UpdateAdminProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12?\n\tnew_admin\x18\x03 \x01(\tB,\xf2\xde\x1f\x10yaml:\"new_admin\"\xd2\xb4-\x14\x63osmos.AddressString\x12*\n\x08\x63ontract\x18\x04 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:=\x18\x01\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\x8a\xe7\xb0*\x18wasm/UpdateAdminProposal\"\xa2\x01\n\x12\x43learAdminProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12*\n\x08\x63ontract\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:<\x18\x01\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\x8a\xe7\xb0*\x17wasm/ClearAdminProposal\"\xa4\x01\n\x10PinCodesProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x30\n\x08\x63ode_ids\x18\x03 \x03(\x04\x42\x1e\xe2\xde\x1f\x07\x43odeIDs\xf2\xde\x1f\x0fyaml:\"code_ids\"::\x18\x01\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\x8a\xe7\xb0*\x15wasm/PinCodesProposal\"\xa8\x01\n\x12UnpinCodesProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x30\n\x08\x63ode_ids\x18\x03 \x03(\x04\x42\x1e\xe2\xde\x1f\x07\x43odeIDs\xf2\xde\x1f\x0fyaml:\"code_ids\":<\x18\x01\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\x8a\xe7\xb0*\x17wasm/UnpinCodesProposal\"|\n\x12\x41\x63\x63\x65ssConfigUpdate\x12\x1b\n\x07\x63ode_id\x18\x01 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeID\x12I\n\x16instantiate_permission\x18\x02 \x01(\x0b\x32\x1e.cosmwasm.wasm.v1.AccessConfigB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\"\x8a\x02\n\x1fUpdateInstantiateConfigProposal\x12\x1f\n\x05title\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:\"title\"\x12+\n\x0b\x64\x65scription\x18\x02 \x01(\tB\x16\xf2\xde\x1f\x12yaml:\"description\"\x12N\n\x15\x61\x63\x63\x65ss_config_updates\x18\x03 \x03(\x0b\x32$.cosmwasm.wasm.v1.AccessConfigUpdateB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:I\x18\x01\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\x8a\xe7\xb0*$wasm/UpdateInstantiateConfigProposal\"\x98\x04\n#StoreAndInstantiateContractProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12(\n\x06run_as\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12(\n\x0ewasm_byte_code\x18\x04 \x01(\x0c\x42\x10\xe2\xde\x1f\x0cWASMByteCode\x12>\n\x16instantiate_permission\x18\x05 \x01(\x0b\x32\x1e.cosmwasm.wasm.v1.AccessConfig\x12\x12\n\nunpin_code\x18\x06 \x01(\x08\x12\r\n\x05\x61\x64min\x18\x07 \x01(\t\x12\r\n\x05label\x18\x08 \x01(\t\x12#\n\x03msg\x18\t \x01(\x0c\x42\x16\xfa\xde\x1f\x12RawContractMessage\x12_\n\x05\x66unds\x18\n \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB5\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xa8\xe7\xb0*\x01\x12\x0e\n\x06source\x18\x0b \x01(\t\x12\x0f\n\x07\x62uilder\x18\x0c \x01(\t\x12\x11\n\tcode_hash\x18\r \x01(\x0c:M\x18\x01\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\x8a\xe7\xb0*(wasm/StoreAndInstantiateContractProposalB4Z&github.com/CosmWasm/wasmd/x/wasm/types\xc8\xe1\x1e\x00\xd8\xe1\x1e\x00\xa8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmwasm.wasm.v1.proposal_legacy_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z&github.com/CosmWasm/wasmd/x/wasm/types\310\341\036\000\330\341\036\000\250\342\036\001'
  _globals['_STORECODEPROPOSAL'].fields_by_name['run_as']._options = None
  _globals['_STORECODEPROPOSAL'].fields_by_name['run_as']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_STORECODEPROPOSAL'].fields_by_name['wasm_byte_code']._options = None
  _globals['_STORECODEPROPOSAL'].fields_by_name['wasm_byte_code']._serialized_options = b'\342\336\037\014WASMByteCode'
  _globals['_STORECODEPROPOSAL']._options = None
  _globals['_STORECODEPROPOSAL']._serialized_options = b'\030\001\312\264-\032cosmos.gov.v1beta1.Content\212\347\260*\026wasm/StoreCodeProposal'
  _globals['_INSTANTIATECONTRACTPROPOSAL'].fields_by_name['run_as']._options = None
  _globals['_INSTANTIATECONTRACTPROPOSAL'].fields_by_name['run_as']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_INSTANTIATECONTRACTPROPOSAL'].fields_by_name['admin']._options = None
  _globals['_INSTANTIATECONTRACTPROPOSAL'].fields_by_name['admin']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_INSTANTIATECONTRACTPROPOSAL'].fields_by_name['code_id']._options = None
  _globals['_INSTANTIATECONTRACTPROPOSAL'].fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _globals['_INSTANTIATECONTRACTPROPOSAL'].fields_by_name['msg']._options = None
  _globals['_INSTANTIATECONTRACTPROPOSAL'].fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage'
  _globals['_INSTANTIATECONTRACTPROPOSAL'].fields_by_name['funds']._options = None
  _globals['_INSTANTIATECONTRACTPROPOSAL'].fields_by_name['funds']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\250\347\260*\001'
  _globals['_INSTANTIATECONTRACTPROPOSAL']._options = None
  _globals['_INSTANTIATECONTRACTPROPOSAL']._serialized_options = b'\030\001\312\264-\032cosmos.gov.v1beta1.Content\212\347\260* wasm/InstantiateContractProposal'
  _globals['_INSTANTIATECONTRACT2PROPOSAL'].fields_by_name['run_as']._options = None
  _globals['_INSTANTIATECONTRACT2PROPOSAL'].fields_by_name['run_as']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_INSTANTIATECONTRACT2PROPOSAL'].fields_by_name['admin']._options = None
  _globals['_INSTANTIATECONTRACT2PROPOSAL'].fields_by_name['admin']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_INSTANTIATECONTRACT2PROPOSAL'].fields_by_name['code_id']._options = None
  _globals['_INSTANTIATECONTRACT2PROPOSAL'].fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _globals['_INSTANTIATECONTRACT2PROPOSAL'].fields_by_name['msg']._options = None
  _globals['_INSTANTIATECONTRACT2PROPOSAL'].fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage'
  _globals['_INSTANTIATECONTRACT2PROPOSAL'].fields_by_name['funds']._options = None
  _globals['_INSTANTIATECONTRACT2PROPOSAL'].fields_by_name['funds']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\250\347\260*\001'
  _globals['_INSTANTIATECONTRACT2PROPOSAL']._options = None
  _globals['_INSTANTIATECONTRACT2PROPOSAL']._serialized_options = b'\030\001\312\264-\032cosmos.gov.v1beta1.Content\212\347\260*!wasm/InstantiateContract2Proposal'
  _globals['_MIGRATECONTRACTPROPOSAL'].fields_by_name['contract']._options = None
  _globals['_MIGRATECONTRACTPROPOSAL'].fields_by_name['contract']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MIGRATECONTRACTPROPOSAL'].fields_by_name['code_id']._options = None
  _globals['_MIGRATECONTRACTPROPOSAL'].fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _globals['_MIGRATECONTRACTPROPOSAL'].fields_by_name['msg']._options = None
  _globals['_MIGRATECONTRACTPROPOSAL'].fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage'
  _globals['_MIGRATECONTRACTPROPOSAL']._options = None
  _globals['_MIGRATECONTRACTPROPOSAL']._serialized_options = b'\030\001\312\264-\032cosmos.gov.v1beta1.Content\212\347\260*\034wasm/MigrateContractProposal'
  _globals['_SUDOCONTRACTPROPOSAL'].fields_by_name['contract']._options = None
  _globals['_SUDOCONTRACTPROPOSAL'].fields_by_name['contract']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_SUDOCONTRACTPROPOSAL'].fields_by_name['msg']._options = None
  _globals['_SUDOCONTRACTPROPOSAL'].fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage'
  _globals['_SUDOCONTRACTPROPOSAL']._options = None
  _globals['_SUDOCONTRACTPROPOSAL']._serialized_options = b'\030\001\312\264-\032cosmos.gov.v1beta1.Content\212\347\260*\031wasm/SudoContractProposal'
  _globals['_EXECUTECONTRACTPROPOSAL'].fields_by_name['run_as']._options = None
  _globals['_EXECUTECONTRACTPROPOSAL'].fields_by_name['run_as']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_EXECUTECONTRACTPROPOSAL'].fields_by_name['contract']._options = None
  _globals['_EXECUTECONTRACTPROPOSAL'].fields_by_name['contract']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_EXECUTECONTRACTPROPOSAL'].fields_by_name['msg']._options = None
  _globals['_EXECUTECONTRACTPROPOSAL'].fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage'
  _globals['_EXECUTECONTRACTPROPOSAL'].fields_by_name['funds']._options = None
  _globals['_EXECUTECONTRACTPROPOSAL'].fields_by_name['funds']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\250\347\260*\001'
  _globals['_EXECUTECONTRACTPROPOSAL']._options = None
  _globals['_EXECUTECONTRACTPROPOSAL']._serialized_options = b'\030\001\312\264-\032cosmos.gov.v1beta1.Content\212\347\260*\034wasm/ExecuteContractProposal'
  _globals['_UPDATEADMINPROPOSAL'].fields_by_name['new_admin']._options = None
  _globals['_UPDATEADMINPROPOSAL'].fields_by_name['new_admin']._serialized_options = b'\362\336\037\020yaml:\"new_admin\"\322\264-\024cosmos.AddressString'
  _globals['_UPDATEADMINPROPOSAL'].fields_by_name['contract']._options = None
  _globals['_UPDATEADMINPROPOSAL'].fields_by_name['contract']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_UPDATEADMINPROPOSAL']._options = None
  _globals['_UPDATEADMINPROPOSAL']._serialized_options = b'\030\001\312\264-\032cosmos.gov.v1beta1.Content\212\347\260*\030wasm/UpdateAdminProposal'
  _globals['_CLEARADMINPROPOSAL'].fields_by_name['contract']._options = None
  _globals['_CLEARADMINPROPOSAL'].fields_by_name['contract']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_CLEARADMINPROPOSAL']._options = None
  _globals['_CLEARADMINPROPOSAL']._serialized_options = b'\030\001\312\264-\032cosmos.gov.v1beta1.Content\212\347\260*\027wasm/ClearAdminProposal'
  _globals['_PINCODESPROPOSAL'].fields_by_name['code_ids']._options = None
  _globals['_PINCODESPROPOSAL'].fields_by_name['code_ids']._serialized_options = b'\342\336\037\007CodeIDs\362\336\037\017yaml:\"code_ids\"'
  _globals['_PINCODESPROPOSAL']._options = None
  _globals['_PINCODESPROPOSAL']._serialized_options = b'\030\001\312\264-\032cosmos.gov.v1beta1.Content\212\347\260*\025wasm/PinCodesProposal'
  _globals['_UNPINCODESPROPOSAL'].fields_by_name['code_ids']._options = None
  _globals['_UNPINCODESPROPOSAL'].fields_by_name['code_ids']._serialized_options = b'\342\336\037\007CodeIDs\362\336\037\017yaml:\"code_ids\"'
  _globals['_UNPINCODESPROPOSAL']._options = None
  _globals['_UNPINCODESPROPOSAL']._serialized_options = b'\030\001\312\264-\032cosmos.gov.v1beta1.Content\212\347\260*\027wasm/UnpinCodesProposal'
  _globals['_ACCESSCONFIGUPDATE'].fields_by_name['code_id']._options = None
  _globals['_ACCESSCONFIGUPDATE'].fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _globals['_ACCESSCONFIGUPDATE'].fields_by_name['instantiate_permission']._options = None
  _globals['_ACCESSCONFIGUPDATE'].fields_by_name['instantiate_permission']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_UPDATEINSTANTIATECONFIGPROPOSAL'].fields_by_name['title']._options = None
  _globals['_UPDATEINSTANTIATECONFIGPROPOSAL'].fields_by_name['title']._serialized_options = b'\362\336\037\014yaml:\"title\"'
  _globals['_UPDATEINSTANTIATECONFIGPROPOSAL'].fields_by_name['description']._options = None
  _globals['_UPDATEINSTANTIATECONFIGPROPOSAL'].fields_by_name['description']._serialized_options = b'\362\336\037\022yaml:\"description\"'
  _globals['_UPDATEINSTANTIATECONFIGPROPOSAL'].fields_by_name['access_config_updates']._options = None
  _globals['_UPDATEINSTANTIATECONFIGPROPOSAL'].fields_by_name['access_config_updates']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_UPDATEINSTANTIATECONFIGPROPOSAL']._options = None
  _globals['_UPDATEINSTANTIATECONFIGPROPOSAL']._serialized_options = b'\030\001\312\264-\032cosmos.gov.v1beta1.Content\212\347\260*$wasm/UpdateInstantiateConfigProposal'
  _globals['_STOREANDINSTANTIATECONTRACTPROPOSAL'].fields_by_name['run_as']._options = None
  _globals['_STOREANDINSTANTIATECONTRACTPROPOSAL'].fields_by_name['run_as']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_STOREANDINSTANTIATECONTRACTPROPOSAL'].fields_by_name['wasm_byte_code']._options = None
  _globals['_STOREANDINSTANTIATECONTRACTPROPOSAL'].fields_by_name['wasm_byte_code']._serialized_options = b'\342\336\037\014WASMByteCode'
  _globals['_STOREANDINSTANTIATECONTRACTPROPOSAL'].fields_by_name['msg']._options = None
  _globals['_STOREANDINSTANTIATECONTRACTPROPOSAL'].fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage'
  _globals['_STOREANDINSTANTIATECONTRACTPROPOSAL'].fields_by_name['funds']._options = None
  _globals['_STOREANDINSTANTIATECONTRACTPROPOSAL'].fields_by_name['funds']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\250\347\260*\001'
  _globals['_STOREANDINSTANTIATECONTRACTPROPOSAL']._options = None
  _globals['_STOREANDINSTANTIATECONTRACTPROPOSAL']._serialized_options = b'\030\001\312\264-\032cosmos.gov.v1beta1.Content\212\347\260*(wasm/StoreAndInstantiateContractProposal'
  _globals['_STORECODEPROPOSAL']._serialized_start=191
  _globals['_STORECODEPROPOSAL']._serialized_end=539
  _globals['_INSTANTIATECONTRACTPROPOSAL']._serialized_start=542
  _globals['_INSTANTIATECONTRACTPROPOSAL']._serialized_end=939
  _globals['_INSTANTIATECONTRACT2PROPOSAL']._serialized_start=942
  _globals['_INSTANTIATECONTRACT2PROPOSAL']._serialized_end=1372
  _globals['_MIGRATECONTRACTPROPOSAL']._serialized_start=1375
  _globals['_MIGRATECONTRACTPROPOSAL']._serialized_end=1613
  _globals['_SUDOCONTRACTPROPOSAL']._serialized_start=1616
  _globals['_SUDOCONTRACTPROPOSAL']._serialized_end=1819
  _globals['_EXECUTECONTRACTPROPOSAL']._serialized_start=1822
  _globals['_EXECUTECONTRACTPROPOSAL']._serialized_end=2170
  _globals['_UPDATEADMINPROPOSAL']._serialized_start=2173
  _globals['_UPDATEADMINPROPOSAL']._serialized_end=2402
  _globals['_CLEARADMINPROPOSAL']._serialized_start=2405
  _globals['_CLEARADMINPROPOSAL']._serialized_end=2567
  _globals['_PINCODESPROPOSAL']._serialized_start=2570
  _globals['_PINCODESPROPOSAL']._serialized_end=2734
  _globals['_UNPINCODESPROPOSAL']._serialized_start=2737
  _globals['_UNPINCODESPROPOSAL']._serialized_end=2905
  _globals['_ACCESSCONFIGUPDATE']._serialized_start=2907
  _globals['_ACCESSCONFIGUPDATE']._serialized_end=3031
  _globals['_UPDATEINSTANTIATECONFIGPROPOSAL']._serialized_start=3034
  _globals['_UPDATEINSTANTIATECONFIGPROPOSAL']._serialized_end=3300
  _globals['_STOREANDINSTANTIATECONTRACTPROPOSAL']._serialized_start=3303
  _globals['_STOREANDINSTANTIATECONTRACTPROPOSAL']._serialized_end=3839
# @@protoc_insertion_point(module_scope)
