# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/evm/v1/chain_config.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#injective/evm/v1/chain_config.proto\x12\x10injective.evm.v1\x1a\x14gogoproto/gogo.proto\"\xa7\x11\n\x0b\x43hainConfig\x12\\\n\x0fhomestead_block\x18\x01 \x01(\tB3\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xf2\xde\x1f\x16yaml:\"homestead_block\"R\x0ehomesteadBlock\x12h\n\x0e\x64\x61o_fork_block\x18\x02 \x01(\tBB\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xe2\xde\x1f\x0c\x44\x41OForkBlock\xf2\xde\x1f\x15yaml:\"dao_fork_block\"R\x0c\x64\x61oForkBlock\x12W\n\x10\x64\x61o_fork_support\x18\x03 \x01(\x08\x42-\xe2\xde\x1f\x0e\x44\x41OForkSupport\xf2\xde\x1f\x17yaml:\"dao_fork_support\"R\x0e\x64\x61oForkSupport\x12\x62\n\x0c\x65ip150_block\x18\x04 \x01(\tB?\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xe2\xde\x1f\x0b\x45IP150Block\xf2\xde\x1f\x13yaml:\"eip150_block\"R\x0b\x65ip150Block\x12I\n\x0b\x65ip150_hash\x18\x05 \x01(\tB(\xe2\xde\x1f\nEIP150Hash\xf2\xde\x1f\x16yaml:\"byzantium_block\"R\neip150Hash\x12\x62\n\x0c\x65ip155_block\x18\x06 \x01(\tB?\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xe2\xde\x1f\x0b\x45IP155Block\xf2\xde\x1f\x13yaml:\"eip155_block\"R\x0b\x65ip155Block\x12\x62\n\x0c\x65ip158_block\x18\x07 \x01(\tB?\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xe2\xde\x1f\x0b\x45IP158Block\xf2\xde\x1f\x13yaml:\"eip158_block\"R\x0b\x65ip158Block\x12\\\n\x0f\x62yzantium_block\x18\x08 \x01(\tB3\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xf2\xde\x1f\x16yaml:\"byzantium_block\"R\x0e\x62yzantiumBlock\x12k\n\x14\x63onstantinople_block\x18\t \x01(\tB8\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xf2\xde\x1f\x1byaml:\"constantinople_block\"R\x13\x63onstantinopleBlock\x12_\n\x10petersburg_block\x18\n \x01(\tB4\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xf2\xde\x1f\x17yaml:\"petersburg_block\"R\x0fpetersburgBlock\x12Y\n\x0eistanbul_block\x18\x0b \x01(\tB2\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xf2\xde\x1f\x15yaml:\"istanbul_block\"R\ristanbulBlock\x12\x64\n\x12muir_glacier_block\x18\x0c \x01(\tB6\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xf2\xde\x1f\x19yaml:\"muir_glacier_block\"R\x10muirGlacierBlock\x12S\n\x0c\x62\x65rlin_block\x18\r \x01(\tB0\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xf2\xde\x1f\x13yaml:\"berlin_block\"R\x0b\x62\x65rlinBlock\x12S\n\x0clondon_block\x18\x11 \x01(\tB0\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xf2\xde\x1f\x13yaml:\"london_block\"R\x0blondonBlock\x12g\n\x13\x61rrow_glacier_block\x18\x12 \x01(\tB7\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xf2\xde\x1f\x1ayaml:\"arrow_glacier_block\"R\x11\x61rrowGlacierBlock\x12\x64\n\x12gray_glacier_block\x18\x14 \x01(\tB6\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xf2\xde\x1f\x19yaml:\"gray_glacier_block\"R\x10grayGlacierBlock\x12j\n\x14merge_netsplit_block\x18\x15 \x01(\tB8\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xf2\xde\x1f\x1byaml:\"merge_netsplit_block\"R\x12mergeNetsplitBlock\x12V\n\rshanghai_time\x18\x16 \x01(\tB1\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xf2\xde\x1f\x14yaml:\"shanghai_time\"R\x0cshanghaiTime\x12P\n\x0b\x63\x61ncun_time\x18\x17 \x01(\tB/\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xf2\xde\x1f\x12yaml:\"cancun_time\"R\ncancunTime\x12P\n\x0bprague_time\x18\x18 \x01(\tB/\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xf2\xde\x1f\x12yaml:\"prague_time\"R\npragueTime\x12\x63\n\x0f\x65ip155_chain_id\x18\x19 \x01(\tB;\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xe2\xde\x1f\rEIP155ChainID\xea\xde\x1f\reip155ChainIDR\reip155ChainId\x12w\n\x14\x62lob_schedule_config\x18\x1a \x01(\x0b\x32$.injective.evm.v1.BlobScheduleConfigB\x1f\xf2\xde\x1f\x1byaml:\"blob_schedule_config\"R\x12\x62lobScheduleConfigJ\x04\x08\x0e\x10\x0fJ\x04\x08\x0f\x10\x10J\x04\x08\x10\x10\x11J\x04\x08\x13\x10\x14R\ryolo_v3_blockR\x0b\x65wasm_blockR\x0e\x63\x61talyst_blockR\x10merge_fork_block\"\xea\x01\n\x12\x42lobScheduleConfig\x12\x34\n\x06\x63\x61ncun\x18\x01 \x01(\x0b\x32\x1c.injective.evm.v1.BlobConfigR\x06\x63\x61ncun\x12\x34\n\x06prague\x18\x02 \x01(\x0b\x32\x1c.injective.evm.v1.BlobConfigR\x06prague\x12\x32\n\x05osaka\x18\x03 \x01(\x0b\x32\x1c.injective.evm.v1.BlobConfigR\x05osaka\x12\x34\n\x06verkle\x18\x04 \x01(\x0b\x32\x1c.injective.evm.v1.BlobConfigR\x06verkle\"\x94\x01\n\nBlobConfig\x12\x16\n\x06target\x18\x01 \x01(\x04R\x06target\x12\x10\n\x03max\x18\x02 \x01(\x04R\x03max\x12\\\n\x18\x62\x61se_fee_update_fraction\x18\x03 \x01(\x04\x42#\xf2\xde\x1f\x1fyaml:\"base_fee_update_fraction\"R\x15\x62\x61seFeeUpdateFractionB\xd5\x01\n\x14\x63om.injective.evm.v1B\x10\x43hainConfigProtoP\x01ZIgithub.com/InjectiveLabs/injective-core/injective-chain/modules/evm/types\xa2\x02\x03IEX\xaa\x02\x10Injective.Evm.V1\xca\x02\x10Injective\\Evm\\V1\xe2\x02\x1cInjective\\Evm\\V1\\GPBMetadata\xea\x02\x12Injective::Evm::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.evm.v1.chain_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.injective.evm.v1B\020ChainConfigProtoP\001ZIgithub.com/InjectiveLabs/injective-core/injective-chain/modules/evm/types\242\002\003IEX\252\002\020Injective.Evm.V1\312\002\020Injective\\Evm\\V1\342\002\034Injective\\Evm\\V1\\GPBMetadata\352\002\022Injective::Evm::V1'
  _globals['_CHAINCONFIG'].fields_by_name['homestead_block']._loaded_options = None
  _globals['_CHAINCONFIG'].fields_by_name['homestead_block']._serialized_options = b'\332\336\037\025cosmossdk.io/math.Int\362\336\037\026yaml:\"homestead_block\"'
  _globals['_CHAINCONFIG'].fields_by_name['dao_fork_block']._loaded_options = None
  _globals['_CHAINCONFIG'].fields_by_name['dao_fork_block']._serialized_options = b'\332\336\037\025cosmossdk.io/math.Int\342\336\037\014DAOForkBlock\362\336\037\025yaml:\"dao_fork_block\"'
  _globals['_CHAINCONFIG'].fields_by_name['dao_fork_support']._loaded_options = None
  _globals['_CHAINCONFIG'].fields_by_name['dao_fork_support']._serialized_options = b'\342\336\037\016DAOForkSupport\362\336\037\027yaml:\"dao_fork_support\"'
  _globals['_CHAINCONFIG'].fields_by_name['eip150_block']._loaded_options = None
  _globals['_CHAINCONFIG'].fields_by_name['eip150_block']._serialized_options = b'\332\336\037\025cosmossdk.io/math.Int\342\336\037\013EIP150Block\362\336\037\023yaml:\"eip150_block\"'
  _globals['_CHAINCONFIG'].fields_by_name['eip150_hash']._loaded_options = None
  _globals['_CHAINCONFIG'].fields_by_name['eip150_hash']._serialized_options = b'\342\336\037\nEIP150Hash\362\336\037\026yaml:\"byzantium_block\"'
  _globals['_CHAINCONFIG'].fields_by_name['eip155_block']._loaded_options = None
  _globals['_CHAINCONFIG'].fields_by_name['eip155_block']._serialized_options = b'\332\336\037\025cosmossdk.io/math.Int\342\336\037\013EIP155Block\362\336\037\023yaml:\"eip155_block\"'
  _globals['_CHAINCONFIG'].fields_by_name['eip158_block']._loaded_options = None
  _globals['_CHAINCONFIG'].fields_by_name['eip158_block']._serialized_options = b'\332\336\037\025cosmossdk.io/math.Int\342\336\037\013EIP158Block\362\336\037\023yaml:\"eip158_block\"'
  _globals['_CHAINCONFIG'].fields_by_name['byzantium_block']._loaded_options = None
  _globals['_CHAINCONFIG'].fields_by_name['byzantium_block']._serialized_options = b'\332\336\037\025cosmossdk.io/math.Int\362\336\037\026yaml:\"byzantium_block\"'
  _globals['_CHAINCONFIG'].fields_by_name['constantinople_block']._loaded_options = None
  _globals['_CHAINCONFIG'].fields_by_name['constantinople_block']._serialized_options = b'\332\336\037\025cosmossdk.io/math.Int\362\336\037\033yaml:\"constantinople_block\"'
  _globals['_CHAINCONFIG'].fields_by_name['petersburg_block']._loaded_options = None
  _globals['_CHAINCONFIG'].fields_by_name['petersburg_block']._serialized_options = b'\332\336\037\025cosmossdk.io/math.Int\362\336\037\027yaml:\"petersburg_block\"'
  _globals['_CHAINCONFIG'].fields_by_name['istanbul_block']._loaded_options = None
  _globals['_CHAINCONFIG'].fields_by_name['istanbul_block']._serialized_options = b'\332\336\037\025cosmossdk.io/math.Int\362\336\037\025yaml:\"istanbul_block\"'
  _globals['_CHAINCONFIG'].fields_by_name['muir_glacier_block']._loaded_options = None
  _globals['_CHAINCONFIG'].fields_by_name['muir_glacier_block']._serialized_options = b'\332\336\037\025cosmossdk.io/math.Int\362\336\037\031yaml:\"muir_glacier_block\"'
  _globals['_CHAINCONFIG'].fields_by_name['berlin_block']._loaded_options = None
  _globals['_CHAINCONFIG'].fields_by_name['berlin_block']._serialized_options = b'\332\336\037\025cosmossdk.io/math.Int\362\336\037\023yaml:\"berlin_block\"'
  _globals['_CHAINCONFIG'].fields_by_name['london_block']._loaded_options = None
  _globals['_CHAINCONFIG'].fields_by_name['london_block']._serialized_options = b'\332\336\037\025cosmossdk.io/math.Int\362\336\037\023yaml:\"london_block\"'
  _globals['_CHAINCONFIG'].fields_by_name['arrow_glacier_block']._loaded_options = None
  _globals['_CHAINCONFIG'].fields_by_name['arrow_glacier_block']._serialized_options = b'\332\336\037\025cosmossdk.io/math.Int\362\336\037\032yaml:\"arrow_glacier_block\"'
  _globals['_CHAINCONFIG'].fields_by_name['gray_glacier_block']._loaded_options = None
  _globals['_CHAINCONFIG'].fields_by_name['gray_glacier_block']._serialized_options = b'\332\336\037\025cosmossdk.io/math.Int\362\336\037\031yaml:\"gray_glacier_block\"'
  _globals['_CHAINCONFIG'].fields_by_name['merge_netsplit_block']._loaded_options = None
  _globals['_CHAINCONFIG'].fields_by_name['merge_netsplit_block']._serialized_options = b'\332\336\037\025cosmossdk.io/math.Int\362\336\037\033yaml:\"merge_netsplit_block\"'
  _globals['_CHAINCONFIG'].fields_by_name['shanghai_time']._loaded_options = None
  _globals['_CHAINCONFIG'].fields_by_name['shanghai_time']._serialized_options = b'\332\336\037\025cosmossdk.io/math.Int\362\336\037\024yaml:\"shanghai_time\"'
  _globals['_CHAINCONFIG'].fields_by_name['cancun_time']._loaded_options = None
  _globals['_CHAINCONFIG'].fields_by_name['cancun_time']._serialized_options = b'\332\336\037\025cosmossdk.io/math.Int\362\336\037\022yaml:\"cancun_time\"'
  _globals['_CHAINCONFIG'].fields_by_name['prague_time']._loaded_options = None
  _globals['_CHAINCONFIG'].fields_by_name['prague_time']._serialized_options = b'\332\336\037\025cosmossdk.io/math.Int\362\336\037\022yaml:\"prague_time\"'
  _globals['_CHAINCONFIG'].fields_by_name['eip155_chain_id']._loaded_options = None
  _globals['_CHAINCONFIG'].fields_by_name['eip155_chain_id']._serialized_options = b'\332\336\037\025cosmossdk.io/math.Int\342\336\037\rEIP155ChainID\352\336\037\reip155ChainID'
  _globals['_CHAINCONFIG'].fields_by_name['blob_schedule_config']._loaded_options = None
  _globals['_CHAINCONFIG'].fields_by_name['blob_schedule_config']._serialized_options = b'\362\336\037\033yaml:\"blob_schedule_config\"'
  _globals['_BLOBCONFIG'].fields_by_name['base_fee_update_fraction']._loaded_options = None
  _globals['_BLOBCONFIG'].fields_by_name['base_fee_update_fraction']._serialized_options = b'\362\336\037\037yaml:\"base_fee_update_fraction\"'
  _globals['_CHAINCONFIG']._serialized_start=80
  _globals['_CHAINCONFIG']._serialized_end=2295
  _globals['_BLOBSCHEDULECONFIG']._serialized_start=2298
  _globals['_BLOBSCHEDULECONFIG']._serialized_end=2532
  _globals['_BLOBCONFIG']._serialized_start=2535
  _globals['_BLOBCONFIG']._serialized_end=2683
# @@protoc_insertion_point(module_scope)
