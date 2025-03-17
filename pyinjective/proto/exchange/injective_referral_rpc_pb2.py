# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exchange/injective_referral_rpc.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%exchange/injective_referral_rpc.proto\x12\x16injective_referral_rpc\"F\n\x19GetReferrerDetailsRequest\x12)\n\x10referrer_address\x18\x01 \x01(\tR\x0freferrerAddress\"\xe3\x01\n\x1aGetReferrerDetailsResponse\x12\x43\n\x08invitees\x18\x01 \x03(\x0b\x32\'.injective_referral_rpc.ReferralInviteeR\x08invitees\x12)\n\x10total_commission\x18\x02 \x01(\tR\x0ftotalCommission\x12\x30\n\x14total_trading_volume\x18\x03 \x01(\tR\x12totalTradingVolume\x12#\n\rreferrer_code\x18\x04 \x01(\tR\x0creferrerCode\"\x8f\x01\n\x0fReferralInvitee\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\x12\x1e\n\ncommission\x18\x02 \x01(\tR\ncommission\x12%\n\x0etrading_volume\x18\x03 \x01(\tR\rtradingVolume\x12\x1b\n\tjoin_date\x18\x04 \x01(\tR\x08joinDate\"C\n\x18GetInviteeDetailsRequest\x12\'\n\x0finvitee_address\x18\x01 \x01(\tR\x0einviteeAddress\"\xb0\x01\n\x19GetInviteeDetailsResponse\x12\x1a\n\x08referrer\x18\x01 \x01(\tR\x08referrer\x12\x1b\n\tused_code\x18\x02 \x01(\tR\x08usedCode\x12%\n\x0etrading_volume\x18\x03 \x01(\tR\rtradingVolume\x12\x1b\n\tjoined_at\x18\x04 \x01(\tR\x08joinedAt\x12\x16\n\x06\x61\x63tive\x18\x05 \x01(\x08R\x06\x61\x63tive\"?\n\x18GetReferrerByCodeRequest\x12#\n\rreferral_code\x18\x01 \x01(\tR\x0creferralCode\"F\n\x19GetReferrerByCodeResponse\x12)\n\x10referrer_address\x18\x01 \x01(\tR\x0freferrerAddress2\x87\x03\n\x14InjectiveReferralRPC\x12{\n\x12GetReferrerDetails\x12\x31.injective_referral_rpc.GetReferrerDetailsRequest\x1a\x32.injective_referral_rpc.GetReferrerDetailsResponse\x12x\n\x11GetInviteeDetails\x12\x30.injective_referral_rpc.GetInviteeDetailsRequest\x1a\x31.injective_referral_rpc.GetInviteeDetailsResponse\x12x\n\x11GetReferrerByCode\x12\x30.injective_referral_rpc.GetReferrerByCodeRequest\x1a\x31.injective_referral_rpc.GetReferrerByCodeResponseB\xc2\x01\n\x1a\x63om.injective_referral_rpcB\x19InjectiveReferralRpcProtoP\x01Z\x19/injective_referral_rpcpb\xa2\x02\x03IXX\xaa\x02\x14InjectiveReferralRpc\xca\x02\x14InjectiveReferralRpc\xe2\x02 InjectiveReferralRpc\\GPBMetadata\xea\x02\x14InjectiveReferralRpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exchange.injective_referral_rpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.injective_referral_rpcB\031InjectiveReferralRpcProtoP\001Z\031/injective_referral_rpcpb\242\002\003IXX\252\002\024InjectiveReferralRpc\312\002\024InjectiveReferralRpc\342\002 InjectiveReferralRpc\\GPBMetadata\352\002\024InjectiveReferralRpc'
  _globals['_GETREFERRERDETAILSREQUEST']._serialized_start=65
  _globals['_GETREFERRERDETAILSREQUEST']._serialized_end=135
  _globals['_GETREFERRERDETAILSRESPONSE']._serialized_start=138
  _globals['_GETREFERRERDETAILSRESPONSE']._serialized_end=365
  _globals['_REFERRALINVITEE']._serialized_start=368
  _globals['_REFERRALINVITEE']._serialized_end=511
  _globals['_GETINVITEEDETAILSREQUEST']._serialized_start=513
  _globals['_GETINVITEEDETAILSREQUEST']._serialized_end=580
  _globals['_GETINVITEEDETAILSRESPONSE']._serialized_start=583
  _globals['_GETINVITEEDETAILSRESPONSE']._serialized_end=759
  _globals['_GETREFERRERBYCODEREQUEST']._serialized_start=761
  _globals['_GETREFERRERBYCODEREQUEST']._serialized_end=824
  _globals['_GETREFERRERBYCODERESPONSE']._serialized_start=826
  _globals['_GETREFERRERBYCODERESPONSE']._serialized_end=896
  _globals['_INJECTIVEREFERRALRPC']._serialized_start=899
  _globals['_INJECTIVEREFERRALRPC']._serialized_end=1290
# @@protoc_insertion_point(module_scope)
