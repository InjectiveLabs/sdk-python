# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/staking/v1beta1/staking.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2
from pyinjective.proto.cometbft.types.v1 import types_pb2 as cometbft_dot_types_dot_v1_dot_types__pb2
from pyinjective.proto.cometbft.abci.v1 import types_pb2 as cometbft_dot_abci_dot_v1_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/staking/v1beta1/staking.proto\x12\x16\x63osmos.staking.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x11\x61mino/amino.proto\x1a\x1d\x63ometbft/types/v1/types.proto\x1a\x1c\x63ometbft/abci/v1/types.proto\"\x94\x01\n\x0eHistoricalInfo\x12<\n\x06header\x18\x01 \x01(\x0b\x32\x19.cometbft.types.v1.HeaderB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06header\x12\x44\n\x06valset\x18\x02 \x03(\x0b\x32!.cosmos.staking.v1beta1.ValidatorB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06valset\"\x96\x02\n\x0f\x43ommissionRates\x12J\n\x04rate\x18\x01 \x01(\tB6\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01R\x04rate\x12Q\n\x08max_rate\x18\x02 \x01(\tB6\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01R\x07maxRate\x12^\n\x0fmax_change_rate\x18\x03 \x01(\tB6\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01R\rmaxChangeRate:\x04\xe8\xa0\x1f\x01\"\xc1\x01\n\nCommission\x12\x61\n\x10\x63ommission_rates\x18\x01 \x01(\x0b\x32\'.cosmos.staking.v1beta1.CommissionRatesB\r\xc8\xde\x1f\x00\xd0\xde\x1f\x01\xa8\xe7\xb0*\x01R\x0f\x63ommissionRates\x12J\n\x0bupdate_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01R\nupdateTime:\x04\xe8\xa0\x1f\x01\"\xa8\x01\n\x0b\x44\x65scription\x12\x18\n\x07moniker\x18\x01 \x01(\tR\x07moniker\x12\x1a\n\x08identity\x18\x02 \x01(\tR\x08identity\x12\x18\n\x07website\x18\x03 \x01(\tR\x07website\x12)\n\x10security_contact\x18\x04 \x01(\tR\x0fsecurityContact\x12\x18\n\x07\x64\x65tails\x18\x05 \x01(\tR\x07\x64\x65tails:\x04\xe8\xa0\x1f\x01\"\x8a\x07\n\tValidator\x12\x43\n\x10operator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x0foperatorAddress\x12Y\n\x10\x63onsensus_pubkey\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyB\x18\xca\xb4-\x14\x63osmos.crypto.PubKeyR\x0f\x63onsensusPubkey\x12\x16\n\x06jailed\x18\x03 \x01(\x08R\x06jailed\x12:\n\x06status\x18\x04 \x01(\x0e\x32\".cosmos.staking.v1beta1.BondStatusR\x06status\x12\x43\n\x06tokens\x18\x05 \x01(\tB+\xc8\xde\x1f\x00\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xd2\xb4-\ncosmos.IntR\x06tokens\x12\\\n\x10\x64\x65legator_shares\x18\x06 \x01(\tB1\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.DecR\x0f\x64\x65legatorShares\x12P\n\x0b\x64\x65scription\x18\x07 \x01(\x0b\x32#.cosmos.staking.v1beta1.DescriptionB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x0b\x64\x65scription\x12)\n\x10unbonding_height\x18\x08 \x01(\x03R\x0funbondingHeight\x12P\n\x0eunbonding_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01R\runbondingTime\x12M\n\ncommission\x18\n \x01(\x0b\x32\".cosmos.staking.v1beta1.CommissionB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\ncommission\x12[\n\x13min_self_delegation\x18\x0b \x01(\tB+\xc8\xde\x1f\x00\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xd2\xb4-\ncosmos.IntR\x11minSelfDelegation\x12<\n\x1bunbonding_on_hold_ref_count\x18\x0c \x01(\x03R\x17unbondingOnHoldRefCount\x12#\n\runbonding_ids\x18\r \x03(\x04R\x0cunbondingIds:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\"F\n\x0cValAddresses\x12\x36\n\taddresses\x18\x01 \x03(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\taddresses\"\xa9\x01\n\x06\x44VPair\x12\x45\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x10\x64\x65legatorAddress\x12N\n\x11validator_address\x18\x02 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ValidatorAddressStringR\x10validatorAddress:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\"J\n\x07\x44VPairs\x12?\n\x05pairs\x18\x01 \x03(\x0b\x32\x1e.cosmos.staking.v1beta1.DVPairB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x05pairs\"\x8b\x02\n\nDVVTriplet\x12\x45\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x10\x64\x65legatorAddress\x12U\n\x15validator_src_address\x18\x02 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ValidatorAddressStringR\x13validatorSrcAddress\x12U\n\x15validator_dst_address\x18\x03 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ValidatorAddressStringR\x13validatorDstAddress:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\"X\n\x0b\x44VVTriplets\x12I\n\x08triplets\x18\x01 \x03(\x0b\x32\".cosmos.staking.v1beta1.DVVTripletB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x08triplets\"\xf8\x01\n\nDelegation\x12\x45\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x10\x64\x65legatorAddress\x12N\n\x11validator_address\x18\x02 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ValidatorAddressStringR\x10validatorAddress\x12I\n\x06shares\x18\x03 \x01(\tB1\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.DecR\x06shares:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\"\x8d\x02\n\x13UnbondingDelegation\x12\x45\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x10\x64\x65legatorAddress\x12N\n\x11validator_address\x18\x02 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ValidatorAddressStringR\x10validatorAddress\x12U\n\x07\x65ntries\x18\x03 \x03(\x0b\x32\x30.cosmos.staking.v1beta1.UnbondingDelegationEntryB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x07\x65ntries:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\"\x9b\x03\n\x18UnbondingDelegationEntry\x12\'\n\x0f\x63reation_height\x18\x01 \x01(\x03R\x0e\x63reationHeight\x12R\n\x0f\x63ompletion_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01R\x0e\x63ompletionTime\x12T\n\x0finitial_balance\x18\x03 \x01(\tB+\xc8\xde\x1f\x00\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xd2\xb4-\ncosmos.IntR\x0einitialBalance\x12\x45\n\x07\x62\x61lance\x18\x04 \x01(\tB+\xc8\xde\x1f\x00\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xd2\xb4-\ncosmos.IntR\x07\x62\x61lance\x12!\n\x0cunbonding_id\x18\x05 \x01(\x04R\x0bunbondingId\x12<\n\x1bunbonding_on_hold_ref_count\x18\x06 \x01(\x03R\x17unbondingOnHoldRefCount:\x04\xe8\xa0\x1f\x01\"\x9f\x03\n\x11RedelegationEntry\x12\'\n\x0f\x63reation_height\x18\x01 \x01(\x03R\x0e\x63reationHeight\x12R\n\x0f\x63ompletion_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01R\x0e\x63ompletionTime\x12T\n\x0finitial_balance\x18\x03 \x01(\tB+\xc8\xde\x1f\x00\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xd2\xb4-\ncosmos.IntR\x0einitialBalance\x12P\n\nshares_dst\x18\x04 \x01(\tB1\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.DecR\tsharesDst\x12!\n\x0cunbonding_id\x18\x05 \x01(\x04R\x0bunbondingId\x12<\n\x1bunbonding_on_hold_ref_count\x18\x06 \x01(\x03R\x17unbondingOnHoldRefCount:\x04\xe8\xa0\x1f\x01\"\xdd\x02\n\x0cRedelegation\x12\x45\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x10\x64\x65legatorAddress\x12U\n\x15validator_src_address\x18\x02 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ValidatorAddressStringR\x13validatorSrcAddress\x12U\n\x15validator_dst_address\x18\x03 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ValidatorAddressStringR\x13validatorDstAddress\x12N\n\x07\x65ntries\x18\x04 \x03(\x0b\x32).cosmos.staking.v1beta1.RedelegationEntryB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x07\x65ntries:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\"\x9c\x03\n\x06Params\x12O\n\x0eunbonding_time\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\r\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xa8\xe7\xb0*\x01R\runbondingTime\x12%\n\x0emax_validators\x18\x02 \x01(\rR\rmaxValidators\x12\x1f\n\x0bmax_entries\x18\x03 \x01(\rR\nmaxEntries\x12-\n\x12historical_entries\x18\x04 \x01(\rR\x11historicalEntries\x12\x1d\n\nbond_denom\x18\x05 \x01(\tR\tbondDenom\x12\x84\x01\n\x13min_commission_rate\x18\x06 \x01(\tBT\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xf2\xde\x1f\x1ayaml:\"min_commission_rate\"\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01R\x11minCommissionRate:$\xe8\xa0\x1f\x01\x8a\xe7\xb0*\x1b\x63osmos-sdk/x/staking/Params\"\xa9\x01\n\x12\x44\x65legationResponse\x12M\n\ndelegation\x18\x01 \x01(\x0b\x32\".cosmos.staking.v1beta1.DelegationB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\ndelegation\x12>\n\x07\x62\x61lance\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x07\x62\x61lance:\x04\xe8\xa0\x1f\x00\"\xcd\x01\n\x19RedelegationEntryResponse\x12\x63\n\x12redelegation_entry\x18\x01 \x01(\x0b\x32).cosmos.staking.v1beta1.RedelegationEntryB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x11redelegationEntry\x12\x45\n\x07\x62\x61lance\x18\x04 \x01(\tB+\xc8\xde\x1f\x00\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xd2\xb4-\ncosmos.IntR\x07\x62\x61lance:\x04\xe8\xa0\x1f\x01\"\xc9\x01\n\x14RedelegationResponse\x12S\n\x0credelegation\x18\x01 \x01(\x0b\x32$.cosmos.staking.v1beta1.RedelegationB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x0credelegation\x12V\n\x07\x65ntries\x18\x02 \x03(\x0b\x32\x31.cosmos.staking.v1beta1.RedelegationEntryResponseB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x07\x65ntries:\x04\xe8\xa0\x1f\x00\"\xeb\x01\n\x04Pool\x12q\n\x11not_bonded_tokens\x18\x01 \x01(\tBE\xc8\xde\x1f\x00\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xea\xde\x1f\x11not_bonded_tokens\xd2\xb4-\ncosmos.Int\xa8\xe7\xb0*\x01R\x0fnotBondedTokens\x12\x66\n\rbonded_tokens\x18\x02 \x01(\tBA\xc8\xde\x1f\x00\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xea\xde\x1f\rbonded_tokens\xd2\xb4-\ncosmos.Int\xa8\xe7\xb0*\x01R\x0c\x62ondedTokens:\x08\xe8\xa0\x1f\x01\xf0\xa0\x1f\x01\"Z\n\x10ValidatorUpdates\x12\x46\n\x07updates\x18\x01 \x03(\x0b\x32!.cometbft.abci.v1.ValidatorUpdateB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x07updates*\xb6\x01\n\nBondStatus\x12,\n\x17\x42OND_STATUS_UNSPECIFIED\x10\x00\x1a\x0f\x8a\x9d \x0bUnspecified\x12&\n\x14\x42OND_STATUS_UNBONDED\x10\x01\x1a\x0c\x8a\x9d \x08Unbonded\x12(\n\x15\x42OND_STATUS_UNBONDING\x10\x02\x1a\r\x8a\x9d \tUnbonding\x12\"\n\x12\x42OND_STATUS_BONDED\x10\x03\x1a\n\x8a\x9d \x06\x42onded\x1a\x04\x88\xa3\x1e\x00*]\n\nInfraction\x12\x1a\n\x16INFRACTION_UNSPECIFIED\x10\x00\x12\x1a\n\x16INFRACTION_DOUBLE_SIGN\x10\x01\x12\x17\n\x13INFRACTION_DOWNTIME\x10\x02\x42\xd2\x01\n\x1a\x63om.cosmos.staking.v1beta1B\x0cStakingProtoP\x01Z,github.com/cosmos/cosmos-sdk/x/staking/types\xa2\x02\x03\x43SX\xaa\x02\x16\x43osmos.Staking.V1beta1\xca\x02\x16\x43osmos\\Staking\\V1beta1\xe2\x02\"Cosmos\\Staking\\V1beta1\\GPBMetadata\xea\x02\x18\x43osmos::Staking::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.staking.v1beta1.staking_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.cosmos.staking.v1beta1B\014StakingProtoP\001Z,github.com/cosmos/cosmos-sdk/x/staking/types\242\002\003CSX\252\002\026Cosmos.Staking.V1beta1\312\002\026Cosmos\\Staking\\V1beta1\342\002\"Cosmos\\Staking\\V1beta1\\GPBMetadata\352\002\030Cosmos::Staking::V1beta1'
  _globals['_BONDSTATUS']._loaded_options = None
  _globals['_BONDSTATUS']._serialized_options = b'\210\243\036\000'
  _globals['_BONDSTATUS'].values_by_name["BOND_STATUS_UNSPECIFIED"]._loaded_options = None
  _globals['_BONDSTATUS'].values_by_name["BOND_STATUS_UNSPECIFIED"]._serialized_options = b'\212\235 \013Unspecified'
  _globals['_BONDSTATUS'].values_by_name["BOND_STATUS_UNBONDED"]._loaded_options = None
  _globals['_BONDSTATUS'].values_by_name["BOND_STATUS_UNBONDED"]._serialized_options = b'\212\235 \010Unbonded'
  _globals['_BONDSTATUS'].values_by_name["BOND_STATUS_UNBONDING"]._loaded_options = None
  _globals['_BONDSTATUS'].values_by_name["BOND_STATUS_UNBONDING"]._serialized_options = b'\212\235 \tUnbonding'
  _globals['_BONDSTATUS'].values_by_name["BOND_STATUS_BONDED"]._loaded_options = None
  _globals['_BONDSTATUS'].values_by_name["BOND_STATUS_BONDED"]._serialized_options = b'\212\235 \006Bonded'
  _globals['_HISTORICALINFO'].fields_by_name['header']._loaded_options = None
  _globals['_HISTORICALINFO'].fields_by_name['header']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_HISTORICALINFO'].fields_by_name['valset']._loaded_options = None
  _globals['_HISTORICALINFO'].fields_by_name['valset']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_COMMISSIONRATES'].fields_by_name['rate']._loaded_options = None
  _globals['_COMMISSIONRATES'].fields_by_name['rate']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\322\264-\ncosmos.Dec\250\347\260*\001'
  _globals['_COMMISSIONRATES'].fields_by_name['max_rate']._loaded_options = None
  _globals['_COMMISSIONRATES'].fields_by_name['max_rate']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\322\264-\ncosmos.Dec\250\347\260*\001'
  _globals['_COMMISSIONRATES'].fields_by_name['max_change_rate']._loaded_options = None
  _globals['_COMMISSIONRATES'].fields_by_name['max_change_rate']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\322\264-\ncosmos.Dec\250\347\260*\001'
  _globals['_COMMISSIONRATES']._loaded_options = None
  _globals['_COMMISSIONRATES']._serialized_options = b'\350\240\037\001'
  _globals['_COMMISSION'].fields_by_name['commission_rates']._loaded_options = None
  _globals['_COMMISSION'].fields_by_name['commission_rates']._serialized_options = b'\310\336\037\000\320\336\037\001\250\347\260*\001'
  _globals['_COMMISSION'].fields_by_name['update_time']._loaded_options = None
  _globals['_COMMISSION'].fields_by_name['update_time']._serialized_options = b'\310\336\037\000\220\337\037\001\250\347\260*\001'
  _globals['_COMMISSION']._loaded_options = None
  _globals['_COMMISSION']._serialized_options = b'\350\240\037\001'
  _globals['_DESCRIPTION']._loaded_options = None
  _globals['_DESCRIPTION']._serialized_options = b'\350\240\037\001'
  _globals['_VALIDATOR'].fields_by_name['operator_address']._loaded_options = None
  _globals['_VALIDATOR'].fields_by_name['operator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_VALIDATOR'].fields_by_name['consensus_pubkey']._loaded_options = None
  _globals['_VALIDATOR'].fields_by_name['consensus_pubkey']._serialized_options = b'\312\264-\024cosmos.crypto.PubKey'
  _globals['_VALIDATOR'].fields_by_name['tokens']._loaded_options = None
  _globals['_VALIDATOR'].fields_by_name['tokens']._serialized_options = b'\310\336\037\000\332\336\037\025cosmossdk.io/math.Int\322\264-\ncosmos.Int'
  _globals['_VALIDATOR'].fields_by_name['delegator_shares']._loaded_options = None
  _globals['_VALIDATOR'].fields_by_name['delegator_shares']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\322\264-\ncosmos.Dec'
  _globals['_VALIDATOR'].fields_by_name['description']._loaded_options = None
  _globals['_VALIDATOR'].fields_by_name['description']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_VALIDATOR'].fields_by_name['unbonding_time']._loaded_options = None
  _globals['_VALIDATOR'].fields_by_name['unbonding_time']._serialized_options = b'\310\336\037\000\220\337\037\001\250\347\260*\001'
  _globals['_VALIDATOR'].fields_by_name['commission']._loaded_options = None
  _globals['_VALIDATOR'].fields_by_name['commission']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_VALIDATOR'].fields_by_name['min_self_delegation']._loaded_options = None
  _globals['_VALIDATOR'].fields_by_name['min_self_delegation']._serialized_options = b'\310\336\037\000\332\336\037\025cosmossdk.io/math.Int\322\264-\ncosmos.Int'
  _globals['_VALIDATOR']._loaded_options = None
  _globals['_VALIDATOR']._serialized_options = b'\210\240\037\000\350\240\037\000'
  _globals['_VALADDRESSES'].fields_by_name['addresses']._loaded_options = None
  _globals['_VALADDRESSES'].fields_by_name['addresses']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_DVPAIR'].fields_by_name['delegator_address']._loaded_options = None
  _globals['_DVPAIR'].fields_by_name['delegator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_DVPAIR'].fields_by_name['validator_address']._loaded_options = None
  _globals['_DVPAIR'].fields_by_name['validator_address']._serialized_options = b'\322\264-\035cosmos.ValidatorAddressString'
  _globals['_DVPAIR']._loaded_options = None
  _globals['_DVPAIR']._serialized_options = b'\210\240\037\000\350\240\037\000'
  _globals['_DVPAIRS'].fields_by_name['pairs']._loaded_options = None
  _globals['_DVPAIRS'].fields_by_name['pairs']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_DVVTRIPLET'].fields_by_name['delegator_address']._loaded_options = None
  _globals['_DVVTRIPLET'].fields_by_name['delegator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_DVVTRIPLET'].fields_by_name['validator_src_address']._loaded_options = None
  _globals['_DVVTRIPLET'].fields_by_name['validator_src_address']._serialized_options = b'\322\264-\035cosmos.ValidatorAddressString'
  _globals['_DVVTRIPLET'].fields_by_name['validator_dst_address']._loaded_options = None
  _globals['_DVVTRIPLET'].fields_by_name['validator_dst_address']._serialized_options = b'\322\264-\035cosmos.ValidatorAddressString'
  _globals['_DVVTRIPLET']._loaded_options = None
  _globals['_DVVTRIPLET']._serialized_options = b'\210\240\037\000\350\240\037\000'
  _globals['_DVVTRIPLETS'].fields_by_name['triplets']._loaded_options = None
  _globals['_DVVTRIPLETS'].fields_by_name['triplets']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_DELEGATION'].fields_by_name['delegator_address']._loaded_options = None
  _globals['_DELEGATION'].fields_by_name['delegator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_DELEGATION'].fields_by_name['validator_address']._loaded_options = None
  _globals['_DELEGATION'].fields_by_name['validator_address']._serialized_options = b'\322\264-\035cosmos.ValidatorAddressString'
  _globals['_DELEGATION'].fields_by_name['shares']._loaded_options = None
  _globals['_DELEGATION'].fields_by_name['shares']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\322\264-\ncosmos.Dec'
  _globals['_DELEGATION']._loaded_options = None
  _globals['_DELEGATION']._serialized_options = b'\210\240\037\000\350\240\037\000'
  _globals['_UNBONDINGDELEGATION'].fields_by_name['delegator_address']._loaded_options = None
  _globals['_UNBONDINGDELEGATION'].fields_by_name['delegator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_UNBONDINGDELEGATION'].fields_by_name['validator_address']._loaded_options = None
  _globals['_UNBONDINGDELEGATION'].fields_by_name['validator_address']._serialized_options = b'\322\264-\035cosmos.ValidatorAddressString'
  _globals['_UNBONDINGDELEGATION'].fields_by_name['entries']._loaded_options = None
  _globals['_UNBONDINGDELEGATION'].fields_by_name['entries']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_UNBONDINGDELEGATION']._loaded_options = None
  _globals['_UNBONDINGDELEGATION']._serialized_options = b'\210\240\037\000\350\240\037\000'
  _globals['_UNBONDINGDELEGATIONENTRY'].fields_by_name['completion_time']._loaded_options = None
  _globals['_UNBONDINGDELEGATIONENTRY'].fields_by_name['completion_time']._serialized_options = b'\310\336\037\000\220\337\037\001\250\347\260*\001'
  _globals['_UNBONDINGDELEGATIONENTRY'].fields_by_name['initial_balance']._loaded_options = None
  _globals['_UNBONDINGDELEGATIONENTRY'].fields_by_name['initial_balance']._serialized_options = b'\310\336\037\000\332\336\037\025cosmossdk.io/math.Int\322\264-\ncosmos.Int'
  _globals['_UNBONDINGDELEGATIONENTRY'].fields_by_name['balance']._loaded_options = None
  _globals['_UNBONDINGDELEGATIONENTRY'].fields_by_name['balance']._serialized_options = b'\310\336\037\000\332\336\037\025cosmossdk.io/math.Int\322\264-\ncosmos.Int'
  _globals['_UNBONDINGDELEGATIONENTRY']._loaded_options = None
  _globals['_UNBONDINGDELEGATIONENTRY']._serialized_options = b'\350\240\037\001'
  _globals['_REDELEGATIONENTRY'].fields_by_name['completion_time']._loaded_options = None
  _globals['_REDELEGATIONENTRY'].fields_by_name['completion_time']._serialized_options = b'\310\336\037\000\220\337\037\001\250\347\260*\001'
  _globals['_REDELEGATIONENTRY'].fields_by_name['initial_balance']._loaded_options = None
  _globals['_REDELEGATIONENTRY'].fields_by_name['initial_balance']._serialized_options = b'\310\336\037\000\332\336\037\025cosmossdk.io/math.Int\322\264-\ncosmos.Int'
  _globals['_REDELEGATIONENTRY'].fields_by_name['shares_dst']._loaded_options = None
  _globals['_REDELEGATIONENTRY'].fields_by_name['shares_dst']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\322\264-\ncosmos.Dec'
  _globals['_REDELEGATIONENTRY']._loaded_options = None
  _globals['_REDELEGATIONENTRY']._serialized_options = b'\350\240\037\001'
  _globals['_REDELEGATION'].fields_by_name['delegator_address']._loaded_options = None
  _globals['_REDELEGATION'].fields_by_name['delegator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_REDELEGATION'].fields_by_name['validator_src_address']._loaded_options = None
  _globals['_REDELEGATION'].fields_by_name['validator_src_address']._serialized_options = b'\322\264-\035cosmos.ValidatorAddressString'
  _globals['_REDELEGATION'].fields_by_name['validator_dst_address']._loaded_options = None
  _globals['_REDELEGATION'].fields_by_name['validator_dst_address']._serialized_options = b'\322\264-\035cosmos.ValidatorAddressString'
  _globals['_REDELEGATION'].fields_by_name['entries']._loaded_options = None
  _globals['_REDELEGATION'].fields_by_name['entries']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_REDELEGATION']._loaded_options = None
  _globals['_REDELEGATION']._serialized_options = b'\210\240\037\000\350\240\037\000'
  _globals['_PARAMS'].fields_by_name['unbonding_time']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['unbonding_time']._serialized_options = b'\310\336\037\000\230\337\037\001\250\347\260*\001'
  _globals['_PARAMS'].fields_by_name['min_commission_rate']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['min_commission_rate']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\362\336\037\032yaml:\"min_commission_rate\"\322\264-\ncosmos.Dec\250\347\260*\001'
  _globals['_PARAMS']._loaded_options = None
  _globals['_PARAMS']._serialized_options = b'\350\240\037\001\212\347\260*\033cosmos-sdk/x/staking/Params'
  _globals['_DELEGATIONRESPONSE'].fields_by_name['delegation']._loaded_options = None
  _globals['_DELEGATIONRESPONSE'].fields_by_name['delegation']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_DELEGATIONRESPONSE'].fields_by_name['balance']._loaded_options = None
  _globals['_DELEGATIONRESPONSE'].fields_by_name['balance']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_DELEGATIONRESPONSE']._loaded_options = None
  _globals['_DELEGATIONRESPONSE']._serialized_options = b'\350\240\037\000'
  _globals['_REDELEGATIONENTRYRESPONSE'].fields_by_name['redelegation_entry']._loaded_options = None
  _globals['_REDELEGATIONENTRYRESPONSE'].fields_by_name['redelegation_entry']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_REDELEGATIONENTRYRESPONSE'].fields_by_name['balance']._loaded_options = None
  _globals['_REDELEGATIONENTRYRESPONSE'].fields_by_name['balance']._serialized_options = b'\310\336\037\000\332\336\037\025cosmossdk.io/math.Int\322\264-\ncosmos.Int'
  _globals['_REDELEGATIONENTRYRESPONSE']._loaded_options = None
  _globals['_REDELEGATIONENTRYRESPONSE']._serialized_options = b'\350\240\037\001'
  _globals['_REDELEGATIONRESPONSE'].fields_by_name['redelegation']._loaded_options = None
  _globals['_REDELEGATIONRESPONSE'].fields_by_name['redelegation']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_REDELEGATIONRESPONSE'].fields_by_name['entries']._loaded_options = None
  _globals['_REDELEGATIONRESPONSE'].fields_by_name['entries']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_REDELEGATIONRESPONSE']._loaded_options = None
  _globals['_REDELEGATIONRESPONSE']._serialized_options = b'\350\240\037\000'
  _globals['_POOL'].fields_by_name['not_bonded_tokens']._loaded_options = None
  _globals['_POOL'].fields_by_name['not_bonded_tokens']._serialized_options = b'\310\336\037\000\332\336\037\025cosmossdk.io/math.Int\352\336\037\021not_bonded_tokens\322\264-\ncosmos.Int\250\347\260*\001'
  _globals['_POOL'].fields_by_name['bonded_tokens']._loaded_options = None
  _globals['_POOL'].fields_by_name['bonded_tokens']._serialized_options = b'\310\336\037\000\332\336\037\025cosmossdk.io/math.Int\352\336\037\rbonded_tokens\322\264-\ncosmos.Int\250\347\260*\001'
  _globals['_POOL']._loaded_options = None
  _globals['_POOL']._serialized_options = b'\350\240\037\001\360\240\037\001'
  _globals['_VALIDATORUPDATES'].fields_by_name['updates']._loaded_options = None
  _globals['_VALIDATORUPDATES'].fields_by_name['updates']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_BONDSTATUS']._serialized_start=5742
  _globals['_BONDSTATUS']._serialized_end=5924
  _globals['_INFRACTION']._serialized_start=5926
  _globals['_INFRACTION']._serialized_end=6019
  _globals['_HISTORICALINFO']._serialized_start=318
  _globals['_HISTORICALINFO']._serialized_end=466
  _globals['_COMMISSIONRATES']._serialized_start=469
  _globals['_COMMISSIONRATES']._serialized_end=747
  _globals['_COMMISSION']._serialized_start=750
  _globals['_COMMISSION']._serialized_end=943
  _globals['_DESCRIPTION']._serialized_start=946
  _globals['_DESCRIPTION']._serialized_end=1114
  _globals['_VALIDATOR']._serialized_start=1117
  _globals['_VALIDATOR']._serialized_end=2023
  _globals['_VALADDRESSES']._serialized_start=2025
  _globals['_VALADDRESSES']._serialized_end=2095
  _globals['_DVPAIR']._serialized_start=2098
  _globals['_DVPAIR']._serialized_end=2267
  _globals['_DVPAIRS']._serialized_start=2269
  _globals['_DVPAIRS']._serialized_end=2343
  _globals['_DVVTRIPLET']._serialized_start=2346
  _globals['_DVVTRIPLET']._serialized_end=2613
  _globals['_DVVTRIPLETS']._serialized_start=2615
  _globals['_DVVTRIPLETS']._serialized_end=2703
  _globals['_DELEGATION']._serialized_start=2706
  _globals['_DELEGATION']._serialized_end=2954
  _globals['_UNBONDINGDELEGATION']._serialized_start=2957
  _globals['_UNBONDINGDELEGATION']._serialized_end=3226
  _globals['_UNBONDINGDELEGATIONENTRY']._serialized_start=3229
  _globals['_UNBONDINGDELEGATIONENTRY']._serialized_end=3640
  _globals['_REDELEGATIONENTRY']._serialized_start=3643
  _globals['_REDELEGATIONENTRY']._serialized_end=4058
  _globals['_REDELEGATION']._serialized_start=4061
  _globals['_REDELEGATION']._serialized_end=4410
  _globals['_PARAMS']._serialized_start=4413
  _globals['_PARAMS']._serialized_end=4825
  _globals['_DELEGATIONRESPONSE']._serialized_start=4828
  _globals['_DELEGATIONRESPONSE']._serialized_end=4997
  _globals['_REDELEGATIONENTRYRESPONSE']._serialized_start=5000
  _globals['_REDELEGATIONENTRYRESPONSE']._serialized_end=5205
  _globals['_REDELEGATIONRESPONSE']._serialized_start=5208
  _globals['_REDELEGATIONRESPONSE']._serialized_end=5409
  _globals['_POOL']._serialized_start=5412
  _globals['_POOL']._serialized_end=5647
  _globals['_VALIDATORUPDATES']._serialized_start=5649
  _globals['_VALIDATORUPDATES']._serialized_end=5739
# @@protoc_insertion_point(module_scope)
