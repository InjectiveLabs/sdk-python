# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/insurance/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from injective.insurance.v1beta1 import insurance_pb2 as injective_dot_insurance_dot_v1beta1_dot_insurance__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from injective.insurance.v1beta1 import genesis_pb2 as injective_dot_insurance_dot_v1beta1_dot_genesis__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='injective/insurance/v1beta1/query.proto',
  package='injective.insurance.v1beta1',
  syntax='proto3',
  serialized_options=b'ZOgithub.com/InjectiveLabs/injective-core/injective-chain/modules/insurance/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'injective/insurance/v1beta1/query.proto\x12\x1binjective.insurance.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a+injective/insurance/v1beta1/insurance.proto\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a)injective/insurance/v1beta1/genesis.proto\"\x1d\n\x1bQueryInsuranceParamsRequest\"Y\n\x1cQueryInsuranceParamsResponse\x12\x39\n\x06params\x18\x01 \x01(\x0b\x32#.injective.insurance.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\".\n\x19QueryInsuranceFundRequest\x12\x11\n\tmarket_id\x18\x01 \x01(\t\"V\n\x1aQueryInsuranceFundResponse\x12\x38\n\x04\x66und\x18\x01 \x01(\x0b\x32*.injective.insurance.v1beta1.InsuranceFund\"\x1c\n\x1aQueryInsuranceFundsRequest\"^\n\x1bQueryInsuranceFundsResponse\x12?\n\x05\x66unds\x18\x01 \x03(\x0b\x32*.injective.insurance.v1beta1.InsuranceFundB\x04\xc8\xde\x1f\x00\"E\n QueryEstimatedRedemptionsRequest\x12\x10\n\x08marketId\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\"T\n!QueryEstimatedRedemptionsResponse\x12/\n\x06\x61mount\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"C\n\x1eQueryPendingRedemptionsRequest\x12\x10\n\x08marketId\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\"R\n\x1fQueryPendingRedemptionsResponse\x12/\n\x06\x61mount\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"\x19\n\x17QueryModuleStateRequest\"T\n\x18QueryModuleStateResponse\x12\x38\n\x05state\x18\x01 \x01(\x0b\x32).injective.insurance.v1beta1.GenesisState2\x96\t\n\x05Query\x12\xb3\x01\n\x0fInsuranceParams\x12\x38.injective.insurance.v1beta1.QueryInsuranceParamsRequest\x1a\x39.injective.insurance.v1beta1.QueryInsuranceParamsResponse\"+\x82\xd3\xe4\x93\x02%\x12#/injective/insurance/v1beta1/params\x12\xc1\x01\n\rInsuranceFund\x12\x36.injective.insurance.v1beta1.QueryInsuranceFundRequest\x1a\x37.injective.insurance.v1beta1.QueryInsuranceFundResponse\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/injective/insurance/v1beta1/insurance_fund/{market_id}\x12\xb9\x01\n\x0eInsuranceFunds\x12\x37.injective.insurance.v1beta1.QueryInsuranceFundsRequest\x1a\x38.injective.insurance.v1beta1.QueryInsuranceFundsResponse\"4\x82\xd3\xe4\x93\x02.\x12,/injective/insurance/v1beta1/insurance_funds\x12\xd1\x01\n\x14\x45stimatedRedemptions\x12=.injective.insurance.v1beta1.QueryEstimatedRedemptionsRequest\x1a>.injective.insurance.v1beta1.QueryEstimatedRedemptionsResponse\":\x82\xd3\xe4\x93\x02\x34\x12\x32/injective/insurance/v1beta1/estimated_redemptions\x12\xc9\x01\n\x12PendingRedemptions\x12;.injective.insurance.v1beta1.QueryPendingRedemptionsRequest\x1a<.injective.insurance.v1beta1.QueryPendingRedemptionsResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/injective/insurance/v1beta1/pending_redemptions\x12\xb6\x01\n\x14InsuranceModuleState\x12\x34.injective.insurance.v1beta1.QueryModuleStateRequest\x1a\x35.injective.insurance.v1beta1.QueryModuleStateResponse\"1\x82\xd3\xe4\x93\x02+\x12)/injective/insurance/v1beta1/module_stateBQZOgithub.com/InjectiveLabs/injective-core/injective-chain/modules/insurance/typesb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,injective_dot_insurance_dot_v1beta1_dot_insurance__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,injective_dot_insurance_dot_v1beta1_dot_genesis__pb2.DESCRIPTOR,])




_QUERYINSURANCEPARAMSREQUEST = _descriptor.Descriptor(
  name='QueryInsuranceParamsRequest',
  full_name='injective.insurance.v1beta1.QueryInsuranceParamsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=244,
  serialized_end=273,
)


_QUERYINSURANCEPARAMSRESPONSE = _descriptor.Descriptor(
  name='QueryInsuranceParamsResponse',
  full_name='injective.insurance.v1beta1.QueryInsuranceParamsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='injective.insurance.v1beta1.QueryInsuranceParamsResponse.params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=275,
  serialized_end=364,
)


_QUERYINSURANCEFUNDREQUEST = _descriptor.Descriptor(
  name='QueryInsuranceFundRequest',
  full_name='injective.insurance.v1beta1.QueryInsuranceFundRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='market_id', full_name='injective.insurance.v1beta1.QueryInsuranceFundRequest.market_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=366,
  serialized_end=412,
)


_QUERYINSURANCEFUNDRESPONSE = _descriptor.Descriptor(
  name='QueryInsuranceFundResponse',
  full_name='injective.insurance.v1beta1.QueryInsuranceFundResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fund', full_name='injective.insurance.v1beta1.QueryInsuranceFundResponse.fund', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=414,
  serialized_end=500,
)


_QUERYINSURANCEFUNDSREQUEST = _descriptor.Descriptor(
  name='QueryInsuranceFundsRequest',
  full_name='injective.insurance.v1beta1.QueryInsuranceFundsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=502,
  serialized_end=530,
)


_QUERYINSURANCEFUNDSRESPONSE = _descriptor.Descriptor(
  name='QueryInsuranceFundsResponse',
  full_name='injective.insurance.v1beta1.QueryInsuranceFundsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='funds', full_name='injective.insurance.v1beta1.QueryInsuranceFundsResponse.funds', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=532,
  serialized_end=626,
)


_QUERYESTIMATEDREDEMPTIONSREQUEST = _descriptor.Descriptor(
  name='QueryEstimatedRedemptionsRequest',
  full_name='injective.insurance.v1beta1.QueryEstimatedRedemptionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='marketId', full_name='injective.insurance.v1beta1.QueryEstimatedRedemptionsRequest.marketId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='injective.insurance.v1beta1.QueryEstimatedRedemptionsRequest.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=628,
  serialized_end=697,
)


_QUERYESTIMATEDREDEMPTIONSRESPONSE = _descriptor.Descriptor(
  name='QueryEstimatedRedemptionsResponse',
  full_name='injective.insurance.v1beta1.QueryEstimatedRedemptionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='amount', full_name='injective.insurance.v1beta1.QueryEstimatedRedemptionsResponse.amount', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=699,
  serialized_end=783,
)


_QUERYPENDINGREDEMPTIONSREQUEST = _descriptor.Descriptor(
  name='QueryPendingRedemptionsRequest',
  full_name='injective.insurance.v1beta1.QueryPendingRedemptionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='marketId', full_name='injective.insurance.v1beta1.QueryPendingRedemptionsRequest.marketId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='injective.insurance.v1beta1.QueryPendingRedemptionsRequest.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=785,
  serialized_end=852,
)


_QUERYPENDINGREDEMPTIONSRESPONSE = _descriptor.Descriptor(
  name='QueryPendingRedemptionsResponse',
  full_name='injective.insurance.v1beta1.QueryPendingRedemptionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='amount', full_name='injective.insurance.v1beta1.QueryPendingRedemptionsResponse.amount', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=854,
  serialized_end=936,
)


_QUERYMODULESTATEREQUEST = _descriptor.Descriptor(
  name='QueryModuleStateRequest',
  full_name='injective.insurance.v1beta1.QueryModuleStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=938,
  serialized_end=963,
)


_QUERYMODULESTATERESPONSE = _descriptor.Descriptor(
  name='QueryModuleStateResponse',
  full_name='injective.insurance.v1beta1.QueryModuleStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='injective.insurance.v1beta1.QueryModuleStateResponse.state', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=965,
  serialized_end=1049,
)

_QUERYINSURANCEPARAMSRESPONSE.fields_by_name['params'].message_type = injective_dot_insurance_dot_v1beta1_dot_insurance__pb2._PARAMS
_QUERYINSURANCEFUNDRESPONSE.fields_by_name['fund'].message_type = injective_dot_insurance_dot_v1beta1_dot_insurance__pb2._INSURANCEFUND
_QUERYINSURANCEFUNDSRESPONSE.fields_by_name['funds'].message_type = injective_dot_insurance_dot_v1beta1_dot_insurance__pb2._INSURANCEFUND
_QUERYESTIMATEDREDEMPTIONSRESPONSE.fields_by_name['amount'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_QUERYPENDINGREDEMPTIONSRESPONSE.fields_by_name['amount'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_QUERYMODULESTATERESPONSE.fields_by_name['state'].message_type = injective_dot_insurance_dot_v1beta1_dot_genesis__pb2._GENESISSTATE
DESCRIPTOR.message_types_by_name['QueryInsuranceParamsRequest'] = _QUERYINSURANCEPARAMSREQUEST
DESCRIPTOR.message_types_by_name['QueryInsuranceParamsResponse'] = _QUERYINSURANCEPARAMSRESPONSE
DESCRIPTOR.message_types_by_name['QueryInsuranceFundRequest'] = _QUERYINSURANCEFUNDREQUEST
DESCRIPTOR.message_types_by_name['QueryInsuranceFundResponse'] = _QUERYINSURANCEFUNDRESPONSE
DESCRIPTOR.message_types_by_name['QueryInsuranceFundsRequest'] = _QUERYINSURANCEFUNDSREQUEST
DESCRIPTOR.message_types_by_name['QueryInsuranceFundsResponse'] = _QUERYINSURANCEFUNDSRESPONSE
DESCRIPTOR.message_types_by_name['QueryEstimatedRedemptionsRequest'] = _QUERYESTIMATEDREDEMPTIONSREQUEST
DESCRIPTOR.message_types_by_name['QueryEstimatedRedemptionsResponse'] = _QUERYESTIMATEDREDEMPTIONSRESPONSE
DESCRIPTOR.message_types_by_name['QueryPendingRedemptionsRequest'] = _QUERYPENDINGREDEMPTIONSREQUEST
DESCRIPTOR.message_types_by_name['QueryPendingRedemptionsResponse'] = _QUERYPENDINGREDEMPTIONSRESPONSE
DESCRIPTOR.message_types_by_name['QueryModuleStateRequest'] = _QUERYMODULESTATEREQUEST
DESCRIPTOR.message_types_by_name['QueryModuleStateResponse'] = _QUERYMODULESTATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryInsuranceParamsRequest = _reflection.GeneratedProtocolMessageType('QueryInsuranceParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYINSURANCEPARAMSREQUEST,
  '__module__' : 'injective.insurance.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.insurance.v1beta1.QueryInsuranceParamsRequest)
  })
_sym_db.RegisterMessage(QueryInsuranceParamsRequest)

QueryInsuranceParamsResponse = _reflection.GeneratedProtocolMessageType('QueryInsuranceParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYINSURANCEPARAMSRESPONSE,
  '__module__' : 'injective.insurance.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.insurance.v1beta1.QueryInsuranceParamsResponse)
  })
_sym_db.RegisterMessage(QueryInsuranceParamsResponse)

QueryInsuranceFundRequest = _reflection.GeneratedProtocolMessageType('QueryInsuranceFundRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYINSURANCEFUNDREQUEST,
  '__module__' : 'injective.insurance.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.insurance.v1beta1.QueryInsuranceFundRequest)
  })
_sym_db.RegisterMessage(QueryInsuranceFundRequest)

QueryInsuranceFundResponse = _reflection.GeneratedProtocolMessageType('QueryInsuranceFundResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYINSURANCEFUNDRESPONSE,
  '__module__' : 'injective.insurance.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.insurance.v1beta1.QueryInsuranceFundResponse)
  })
_sym_db.RegisterMessage(QueryInsuranceFundResponse)

QueryInsuranceFundsRequest = _reflection.GeneratedProtocolMessageType('QueryInsuranceFundsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYINSURANCEFUNDSREQUEST,
  '__module__' : 'injective.insurance.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.insurance.v1beta1.QueryInsuranceFundsRequest)
  })
_sym_db.RegisterMessage(QueryInsuranceFundsRequest)

QueryInsuranceFundsResponse = _reflection.GeneratedProtocolMessageType('QueryInsuranceFundsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYINSURANCEFUNDSRESPONSE,
  '__module__' : 'injective.insurance.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.insurance.v1beta1.QueryInsuranceFundsResponse)
  })
_sym_db.RegisterMessage(QueryInsuranceFundsResponse)

QueryEstimatedRedemptionsRequest = _reflection.GeneratedProtocolMessageType('QueryEstimatedRedemptionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYESTIMATEDREDEMPTIONSREQUEST,
  '__module__' : 'injective.insurance.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.insurance.v1beta1.QueryEstimatedRedemptionsRequest)
  })
_sym_db.RegisterMessage(QueryEstimatedRedemptionsRequest)

QueryEstimatedRedemptionsResponse = _reflection.GeneratedProtocolMessageType('QueryEstimatedRedemptionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYESTIMATEDREDEMPTIONSRESPONSE,
  '__module__' : 'injective.insurance.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.insurance.v1beta1.QueryEstimatedRedemptionsResponse)
  })
_sym_db.RegisterMessage(QueryEstimatedRedemptionsResponse)

QueryPendingRedemptionsRequest = _reflection.GeneratedProtocolMessageType('QueryPendingRedemptionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPENDINGREDEMPTIONSREQUEST,
  '__module__' : 'injective.insurance.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.insurance.v1beta1.QueryPendingRedemptionsRequest)
  })
_sym_db.RegisterMessage(QueryPendingRedemptionsRequest)

QueryPendingRedemptionsResponse = _reflection.GeneratedProtocolMessageType('QueryPendingRedemptionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPENDINGREDEMPTIONSRESPONSE,
  '__module__' : 'injective.insurance.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.insurance.v1beta1.QueryPendingRedemptionsResponse)
  })
_sym_db.RegisterMessage(QueryPendingRedemptionsResponse)

QueryModuleStateRequest = _reflection.GeneratedProtocolMessageType('QueryModuleStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYMODULESTATEREQUEST,
  '__module__' : 'injective.insurance.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.insurance.v1beta1.QueryModuleStateRequest)
  })
_sym_db.RegisterMessage(QueryModuleStateRequest)

QueryModuleStateResponse = _reflection.GeneratedProtocolMessageType('QueryModuleStateResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYMODULESTATERESPONSE,
  '__module__' : 'injective.insurance.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.insurance.v1beta1.QueryModuleStateResponse)
  })
_sym_db.RegisterMessage(QueryModuleStateResponse)


DESCRIPTOR._options = None
_QUERYINSURANCEPARAMSRESPONSE.fields_by_name['params']._options = None
_QUERYINSURANCEFUNDSRESPONSE.fields_by_name['funds']._options = None
_QUERYESTIMATEDREDEMPTIONSRESPONSE.fields_by_name['amount']._options = None
_QUERYPENDINGREDEMPTIONSRESPONSE.fields_by_name['amount']._options = None

_QUERY = _descriptor.ServiceDescriptor(
  name='Query',
  full_name='injective.insurance.v1beta1.Query',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1052,
  serialized_end=2226,
  methods=[
  _descriptor.MethodDescriptor(
    name='InsuranceParams',
    full_name='injective.insurance.v1beta1.Query.InsuranceParams',
    index=0,
    containing_service=None,
    input_type=_QUERYINSURANCEPARAMSREQUEST,
    output_type=_QUERYINSURANCEPARAMSRESPONSE,
    serialized_options=b'\202\323\344\223\002%\022#/injective/insurance/v1beta1/params',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='InsuranceFund',
    full_name='injective.insurance.v1beta1.Query.InsuranceFund',
    index=1,
    containing_service=None,
    input_type=_QUERYINSURANCEFUNDREQUEST,
    output_type=_QUERYINSURANCEFUNDRESPONSE,
    serialized_options=b'\202\323\344\223\0029\0227/injective/insurance/v1beta1/insurance_fund/{market_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='InsuranceFunds',
    full_name='injective.insurance.v1beta1.Query.InsuranceFunds',
    index=2,
    containing_service=None,
    input_type=_QUERYINSURANCEFUNDSREQUEST,
    output_type=_QUERYINSURANCEFUNDSRESPONSE,
    serialized_options=b'\202\323\344\223\002.\022,/injective/insurance/v1beta1/insurance_funds',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='EstimatedRedemptions',
    full_name='injective.insurance.v1beta1.Query.EstimatedRedemptions',
    index=3,
    containing_service=None,
    input_type=_QUERYESTIMATEDREDEMPTIONSREQUEST,
    output_type=_QUERYESTIMATEDREDEMPTIONSRESPONSE,
    serialized_options=b'\202\323\344\223\0024\0222/injective/insurance/v1beta1/estimated_redemptions',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PendingRedemptions',
    full_name='injective.insurance.v1beta1.Query.PendingRedemptions',
    index=4,
    containing_service=None,
    input_type=_QUERYPENDINGREDEMPTIONSREQUEST,
    output_type=_QUERYPENDINGREDEMPTIONSRESPONSE,
    serialized_options=b'\202\323\344\223\0022\0220/injective/insurance/v1beta1/pending_redemptions',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='InsuranceModuleState',
    full_name='injective.insurance.v1beta1.Query.InsuranceModuleState',
    index=5,
    containing_service=None,
    input_type=_QUERYMODULESTATEREQUEST,
    output_type=_QUERYMODULESTATERESPONSE,
    serialized_options=b'\202\323\344\223\002+\022)/injective/insurance/v1beta1/module_state',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERY)

DESCRIPTOR.services_by_name['Query'] = _QUERY

# @@protoc_insertion_point(module_scope)
