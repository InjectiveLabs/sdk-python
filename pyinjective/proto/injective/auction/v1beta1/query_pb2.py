# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/auction/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from injective.auction.v1beta1 import auction_pb2 as injective_dot_auction_dot_v1beta1_dot_auction__pb2
from injective.auction.v1beta1 import genesis_pb2 as injective_dot_auction_dot_v1beta1_dot_genesis__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='injective/auction/v1beta1/query.proto',
  package='injective.auction.v1beta1',
  syntax='proto3',
  serialized_options=b'ZMgithub.com/InjectiveLabs/injective-core/injective-chain/modules/auction/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%injective/auction/v1beta1/query.proto\x12\x19injective.auction.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\'injective/auction/v1beta1/auction.proto\x1a\'injective/auction/v1beta1/genesis.proto\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\x1b\n\x19QueryAuctionParamsRequest\"U\n\x1aQueryAuctionParamsResponse\x12\x37\n\x06params\x18\x01 \x01(\x0b\x32!.injective.auction.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\"\"\n QueryCurrentAuctionBasketRequest\"\x93\x02\n!QueryCurrentAuctionBasketResponse\x12[\n\x06\x61mount\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xc8\xde\x1f\x00\x12\x14\n\x0c\x61uctionRound\x18\x02 \x01(\x04\x12\x1a\n\x12\x61uctionClosingTime\x18\x03 \x01(\x03\x12\x15\n\rhighestBidder\x18\x04 \x01(\t\x12H\n\x10highestBidAmount\x18\x05 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\"\x19\n\x17QueryModuleStateRequest\"R\n\x18QueryModuleStateResponse\x12\x36\n\x05state\x18\x01 \x01(\x0b\x32\'.injective.auction.v1beta1.GenesisState2\xa1\x04\n\x05Query\x12\xa7\x01\n\rAuctionParams\x12\x34.injective.auction.v1beta1.QueryAuctionParamsRequest\x1a\x35.injective.auction.v1beta1.QueryAuctionParamsResponse\")\x82\xd3\xe4\x93\x02#\x12!/injective/auction/v1beta1/params\x12\xbc\x01\n\x14\x43urrentAuctionBasket\x12;.injective.auction.v1beta1.QueryCurrentAuctionBasketRequest\x1a<.injective.auction.v1beta1.QueryCurrentAuctionBasketResponse\")\x82\xd3\xe4\x93\x02#\x12!/injective/auction/v1beta1/basket\x12\xae\x01\n\x12\x41uctionModuleState\x12\x32.injective.auction.v1beta1.QueryModuleStateRequest\x1a\x33.injective.auction.v1beta1.QueryModuleStateResponse\"/\x82\xd3\xe4\x93\x02)\x12\'/injective/auction/v1beta1/module_stateBOZMgithub.com/InjectiveLabs/injective-core/injective-chain/modules/auction/typesb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,injective_dot_auction_dot_v1beta1_dot_auction__pb2.DESCRIPTOR,injective_dot_auction_dot_v1beta1_dot_genesis__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,])




_QUERYAUCTIONPARAMSREQUEST = _descriptor.Descriptor(
  name='QueryAuctionParamsRequest',
  full_name='injective.auction.v1beta1.QueryAuctionParamsRequest',
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
  serialized_start=234,
  serialized_end=261,
)


_QUERYAUCTIONPARAMSRESPONSE = _descriptor.Descriptor(
  name='QueryAuctionParamsResponse',
  full_name='injective.auction.v1beta1.QueryAuctionParamsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='injective.auction.v1beta1.QueryAuctionParamsResponse.params', index=0,
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
  serialized_start=263,
  serialized_end=348,
)


_QUERYCURRENTAUCTIONBASKETREQUEST = _descriptor.Descriptor(
  name='QueryCurrentAuctionBasketRequest',
  full_name='injective.auction.v1beta1.QueryCurrentAuctionBasketRequest',
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
  serialized_start=350,
  serialized_end=384,
)


_QUERYCURRENTAUCTIONBASKETRESPONSE = _descriptor.Descriptor(
  name='QueryCurrentAuctionBasketResponse',
  full_name='injective.auction.v1beta1.QueryCurrentAuctionBasketResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='amount', full_name='injective.auction.v1beta1.QueryCurrentAuctionBasketResponse.amount', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='auctionRound', full_name='injective.auction.v1beta1.QueryCurrentAuctionBasketResponse.auctionRound', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='auctionClosingTime', full_name='injective.auction.v1beta1.QueryCurrentAuctionBasketResponse.auctionClosingTime', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='highestBidder', full_name='injective.auction.v1beta1.QueryCurrentAuctionBasketResponse.highestBidder', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='highestBidAmount', full_name='injective.auction.v1beta1.QueryCurrentAuctionBasketResponse.highestBidAmount', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=387,
  serialized_end=662,
)


_QUERYMODULESTATEREQUEST = _descriptor.Descriptor(
  name='QueryModuleStateRequest',
  full_name='injective.auction.v1beta1.QueryModuleStateRequest',
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
  serialized_start=664,
  serialized_end=689,
)


_QUERYMODULESTATERESPONSE = _descriptor.Descriptor(
  name='QueryModuleStateResponse',
  full_name='injective.auction.v1beta1.QueryModuleStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='injective.auction.v1beta1.QueryModuleStateResponse.state', index=0,
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
  serialized_start=691,
  serialized_end=773,
)

_QUERYAUCTIONPARAMSRESPONSE.fields_by_name['params'].message_type = injective_dot_auction_dot_v1beta1_dot_auction__pb2._PARAMS
_QUERYCURRENTAUCTIONBASKETRESPONSE.fields_by_name['amount'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_QUERYMODULESTATERESPONSE.fields_by_name['state'].message_type = injective_dot_auction_dot_v1beta1_dot_genesis__pb2._GENESISSTATE
DESCRIPTOR.message_types_by_name['QueryAuctionParamsRequest'] = _QUERYAUCTIONPARAMSREQUEST
DESCRIPTOR.message_types_by_name['QueryAuctionParamsResponse'] = _QUERYAUCTIONPARAMSRESPONSE
DESCRIPTOR.message_types_by_name['QueryCurrentAuctionBasketRequest'] = _QUERYCURRENTAUCTIONBASKETREQUEST
DESCRIPTOR.message_types_by_name['QueryCurrentAuctionBasketResponse'] = _QUERYCURRENTAUCTIONBASKETRESPONSE
DESCRIPTOR.message_types_by_name['QueryModuleStateRequest'] = _QUERYMODULESTATEREQUEST
DESCRIPTOR.message_types_by_name['QueryModuleStateResponse'] = _QUERYMODULESTATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryAuctionParamsRequest = _reflection.GeneratedProtocolMessageType('QueryAuctionParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYAUCTIONPARAMSREQUEST,
  '__module__' : 'injective.auction.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.auction.v1beta1.QueryAuctionParamsRequest)
  })
_sym_db.RegisterMessage(QueryAuctionParamsRequest)

QueryAuctionParamsResponse = _reflection.GeneratedProtocolMessageType('QueryAuctionParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYAUCTIONPARAMSRESPONSE,
  '__module__' : 'injective.auction.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.auction.v1beta1.QueryAuctionParamsResponse)
  })
_sym_db.RegisterMessage(QueryAuctionParamsResponse)

QueryCurrentAuctionBasketRequest = _reflection.GeneratedProtocolMessageType('QueryCurrentAuctionBasketRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCURRENTAUCTIONBASKETREQUEST,
  '__module__' : 'injective.auction.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.auction.v1beta1.QueryCurrentAuctionBasketRequest)
  })
_sym_db.RegisterMessage(QueryCurrentAuctionBasketRequest)

QueryCurrentAuctionBasketResponse = _reflection.GeneratedProtocolMessageType('QueryCurrentAuctionBasketResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCURRENTAUCTIONBASKETRESPONSE,
  '__module__' : 'injective.auction.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.auction.v1beta1.QueryCurrentAuctionBasketResponse)
  })
_sym_db.RegisterMessage(QueryCurrentAuctionBasketResponse)

QueryModuleStateRequest = _reflection.GeneratedProtocolMessageType('QueryModuleStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYMODULESTATEREQUEST,
  '__module__' : 'injective.auction.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.auction.v1beta1.QueryModuleStateRequest)
  })
_sym_db.RegisterMessage(QueryModuleStateRequest)

QueryModuleStateResponse = _reflection.GeneratedProtocolMessageType('QueryModuleStateResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYMODULESTATERESPONSE,
  '__module__' : 'injective.auction.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.auction.v1beta1.QueryModuleStateResponse)
  })
_sym_db.RegisterMessage(QueryModuleStateResponse)


DESCRIPTOR._options = None
_QUERYAUCTIONPARAMSRESPONSE.fields_by_name['params']._options = None
_QUERYCURRENTAUCTIONBASKETRESPONSE.fields_by_name['amount']._options = None
_QUERYCURRENTAUCTIONBASKETRESPONSE.fields_by_name['highestBidAmount']._options = None

_QUERY = _descriptor.ServiceDescriptor(
  name='Query',
  full_name='injective.auction.v1beta1.Query',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=776,
  serialized_end=1321,
  methods=[
  _descriptor.MethodDescriptor(
    name='AuctionParams',
    full_name='injective.auction.v1beta1.Query.AuctionParams',
    index=0,
    containing_service=None,
    input_type=_QUERYAUCTIONPARAMSREQUEST,
    output_type=_QUERYAUCTIONPARAMSRESPONSE,
    serialized_options=b'\202\323\344\223\002#\022!/injective/auction/v1beta1/params',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CurrentAuctionBasket',
    full_name='injective.auction.v1beta1.Query.CurrentAuctionBasket',
    index=1,
    containing_service=None,
    input_type=_QUERYCURRENTAUCTIONBASKETREQUEST,
    output_type=_QUERYCURRENTAUCTIONBASKETRESPONSE,
    serialized_options=b'\202\323\344\223\002#\022!/injective/auction/v1beta1/basket',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AuctionModuleState',
    full_name='injective.auction.v1beta1.Query.AuctionModuleState',
    index=2,
    containing_service=None,
    input_type=_QUERYMODULESTATEREQUEST,
    output_type=_QUERYMODULESTATERESPONSE,
    serialized_options=b'\202\323\344\223\002)\022\'/injective/auction/v1beta1/module_state',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERY)

DESCRIPTOR.services_by_name['Query'] = _QUERY

# @@protoc_insertion_point(module_scope)
