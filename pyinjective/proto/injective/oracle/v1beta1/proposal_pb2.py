# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/oracle/v1beta1/proposal.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from injective.oracle.v1beta1 import oracle_pb2 as injective_dot_oracle_dot_v1beta1_dot_oracle__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='injective/oracle/v1beta1/proposal.proto',
  package='injective.oracle.v1beta1',
  syntax='proto3',
  serialized_options=b'ZLgithub.com/InjectiveLabs/injective-core/injective-chain/modules/oracle/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'injective/oracle/v1beta1/proposal.proto\x12\x18injective.oracle.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a%injective/oracle/v1beta1/oracle.proto\"b\n GrantBandOraclePrivilegeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x10\n\x08relayers\x18\x03 \x03(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"c\n!RevokeBandOraclePrivilegeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x10\n\x08relayers\x18\x03 \x03(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x80\x01\n!GrantPriceFeederPrivilegeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04\x62\x61se\x18\x03 \x01(\t\x12\r\n\x05quote\x18\x04 \x01(\t\x12\x10\n\x08relayers\x18\x05 \x03(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"r\n\x1eGrantProviderPrivilegeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x10\n\x08provider\x18\x03 \x01(\t\x12\x10\n\x08relayers\x18\x04 \x03(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"s\n\x1fRevokeProviderPrivilegeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x10\n\x08provider\x18\x03 \x01(\t\x12\x10\n\x08relayers\x18\x05 \x03(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x81\x01\n\"RevokePriceFeederPrivilegeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04\x62\x61se\x18\x03 \x01(\t\x12\r\n\x05quote\x18\x04 \x01(\t\x12\x10\n\x08relayers\x18\x05 \x03(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x96\x01\n\"AuthorizeBandOracleRequestProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x42\n\x07request\x18\x03 \x01(\x0b\x32+.injective.oracle.v1beta1.BandOracleRequestB\x04\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xb6\x01\n\x1fUpdateBandOracleRequestProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x19\n\x11\x64\x65lete_request_id\x18\x03 \x01(\x04\x12J\n\x15update_oracle_request\x18\x04 \x01(\x0b\x32+.injective.oracle.v1beta1.BandOracleRequest:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x8d\x01\n\x15\x45nableBandIBCProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x46\n\x0f\x62\x61nd_ibc_params\x18\x03 \x01(\x0b\x32\'.injective.oracle.v1beta1.BandIBCParamsB\x04\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x42NZLgithub.com/InjectiveLabs/injective-core/injective-chain/modules/oracle/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,injective_dot_oracle_dot_v1beta1_dot_oracle__pb2.DESCRIPTOR,])




_GRANTBANDORACLEPRIVILEGEPROPOSAL = _descriptor.Descriptor(
  name='GrantBandOraclePrivilegeProposal',
  full_name='injective.oracle.v1beta1.GrantBandOraclePrivilegeProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='injective.oracle.v1beta1.GrantBandOraclePrivilegeProposal.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='injective.oracle.v1beta1.GrantBandOraclePrivilegeProposal.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='relayers', full_name='injective.oracle.v1beta1.GrantBandOraclePrivilegeProposal.relayers', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=260,
)


_REVOKEBANDORACLEPRIVILEGEPROPOSAL = _descriptor.Descriptor(
  name='RevokeBandOraclePrivilegeProposal',
  full_name='injective.oracle.v1beta1.RevokeBandOraclePrivilegeProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='injective.oracle.v1beta1.RevokeBandOraclePrivilegeProposal.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='injective.oracle.v1beta1.RevokeBandOraclePrivilegeProposal.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='relayers', full_name='injective.oracle.v1beta1.RevokeBandOraclePrivilegeProposal.relayers', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=262,
  serialized_end=361,
)


_GRANTPRICEFEEDERPRIVILEGEPROPOSAL = _descriptor.Descriptor(
  name='GrantPriceFeederPrivilegeProposal',
  full_name='injective.oracle.v1beta1.GrantPriceFeederPrivilegeProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='injective.oracle.v1beta1.GrantPriceFeederPrivilegeProposal.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='injective.oracle.v1beta1.GrantPriceFeederPrivilegeProposal.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base', full_name='injective.oracle.v1beta1.GrantPriceFeederPrivilegeProposal.base', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quote', full_name='injective.oracle.v1beta1.GrantPriceFeederPrivilegeProposal.quote', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='relayers', full_name='injective.oracle.v1beta1.GrantPriceFeederPrivilegeProposal.relayers', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=364,
  serialized_end=492,
)


_GRANTPROVIDERPRIVILEGEPROPOSAL = _descriptor.Descriptor(
  name='GrantProviderPrivilegeProposal',
  full_name='injective.oracle.v1beta1.GrantProviderPrivilegeProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='injective.oracle.v1beta1.GrantProviderPrivilegeProposal.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='injective.oracle.v1beta1.GrantProviderPrivilegeProposal.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='provider', full_name='injective.oracle.v1beta1.GrantProviderPrivilegeProposal.provider', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='relayers', full_name='injective.oracle.v1beta1.GrantProviderPrivilegeProposal.relayers', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=494,
  serialized_end=608,
)


_REVOKEPROVIDERPRIVILEGEPROPOSAL = _descriptor.Descriptor(
  name='RevokeProviderPrivilegeProposal',
  full_name='injective.oracle.v1beta1.RevokeProviderPrivilegeProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='injective.oracle.v1beta1.RevokeProviderPrivilegeProposal.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='injective.oracle.v1beta1.RevokeProviderPrivilegeProposal.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='provider', full_name='injective.oracle.v1beta1.RevokeProviderPrivilegeProposal.provider', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='relayers', full_name='injective.oracle.v1beta1.RevokeProviderPrivilegeProposal.relayers', index=3,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=610,
  serialized_end=725,
)


_REVOKEPRICEFEEDERPRIVILEGEPROPOSAL = _descriptor.Descriptor(
  name='RevokePriceFeederPrivilegeProposal',
  full_name='injective.oracle.v1beta1.RevokePriceFeederPrivilegeProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='injective.oracle.v1beta1.RevokePriceFeederPrivilegeProposal.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='injective.oracle.v1beta1.RevokePriceFeederPrivilegeProposal.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base', full_name='injective.oracle.v1beta1.RevokePriceFeederPrivilegeProposal.base', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quote', full_name='injective.oracle.v1beta1.RevokePriceFeederPrivilegeProposal.quote', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='relayers', full_name='injective.oracle.v1beta1.RevokePriceFeederPrivilegeProposal.relayers', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=728,
  serialized_end=857,
)


_AUTHORIZEBANDORACLEREQUESTPROPOSAL = _descriptor.Descriptor(
  name='AuthorizeBandOracleRequestProposal',
  full_name='injective.oracle.v1beta1.AuthorizeBandOracleRequestProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='injective.oracle.v1beta1.AuthorizeBandOracleRequestProposal.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='injective.oracle.v1beta1.AuthorizeBandOracleRequestProposal.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request', full_name='injective.oracle.v1beta1.AuthorizeBandOracleRequestProposal.request', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=860,
  serialized_end=1010,
)


_UPDATEBANDORACLEREQUESTPROPOSAL = _descriptor.Descriptor(
  name='UpdateBandOracleRequestProposal',
  full_name='injective.oracle.v1beta1.UpdateBandOracleRequestProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='injective.oracle.v1beta1.UpdateBandOracleRequestProposal.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='injective.oracle.v1beta1.UpdateBandOracleRequestProposal.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delete_request_id', full_name='injective.oracle.v1beta1.UpdateBandOracleRequestProposal.delete_request_id', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_oracle_request', full_name='injective.oracle.v1beta1.UpdateBandOracleRequestProposal.update_oracle_request', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1013,
  serialized_end=1195,
)


_ENABLEBANDIBCPROPOSAL = _descriptor.Descriptor(
  name='EnableBandIBCProposal',
  full_name='injective.oracle.v1beta1.EnableBandIBCProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='injective.oracle.v1beta1.EnableBandIBCProposal.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='injective.oracle.v1beta1.EnableBandIBCProposal.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='band_ibc_params', full_name='injective.oracle.v1beta1.EnableBandIBCProposal.band_ibc_params', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1198,
  serialized_end=1339,
)

_AUTHORIZEBANDORACLEREQUESTPROPOSAL.fields_by_name['request'].message_type = injective_dot_oracle_dot_v1beta1_dot_oracle__pb2._BANDORACLEREQUEST
_UPDATEBANDORACLEREQUESTPROPOSAL.fields_by_name['update_oracle_request'].message_type = injective_dot_oracle_dot_v1beta1_dot_oracle__pb2._BANDORACLEREQUEST
_ENABLEBANDIBCPROPOSAL.fields_by_name['band_ibc_params'].message_type = injective_dot_oracle_dot_v1beta1_dot_oracle__pb2._BANDIBCPARAMS
DESCRIPTOR.message_types_by_name['GrantBandOraclePrivilegeProposal'] = _GRANTBANDORACLEPRIVILEGEPROPOSAL
DESCRIPTOR.message_types_by_name['RevokeBandOraclePrivilegeProposal'] = _REVOKEBANDORACLEPRIVILEGEPROPOSAL
DESCRIPTOR.message_types_by_name['GrantPriceFeederPrivilegeProposal'] = _GRANTPRICEFEEDERPRIVILEGEPROPOSAL
DESCRIPTOR.message_types_by_name['GrantProviderPrivilegeProposal'] = _GRANTPROVIDERPRIVILEGEPROPOSAL
DESCRIPTOR.message_types_by_name['RevokeProviderPrivilegeProposal'] = _REVOKEPROVIDERPRIVILEGEPROPOSAL
DESCRIPTOR.message_types_by_name['RevokePriceFeederPrivilegeProposal'] = _REVOKEPRICEFEEDERPRIVILEGEPROPOSAL
DESCRIPTOR.message_types_by_name['AuthorizeBandOracleRequestProposal'] = _AUTHORIZEBANDORACLEREQUESTPROPOSAL
DESCRIPTOR.message_types_by_name['UpdateBandOracleRequestProposal'] = _UPDATEBANDORACLEREQUESTPROPOSAL
DESCRIPTOR.message_types_by_name['EnableBandIBCProposal'] = _ENABLEBANDIBCPROPOSAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GrantBandOraclePrivilegeProposal = _reflection.GeneratedProtocolMessageType('GrantBandOraclePrivilegeProposal', (_message.Message,), {
  'DESCRIPTOR' : _GRANTBANDORACLEPRIVILEGEPROPOSAL,
  '__module__' : 'injective.oracle.v1beta1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.GrantBandOraclePrivilegeProposal)
  })
_sym_db.RegisterMessage(GrantBandOraclePrivilegeProposal)

RevokeBandOraclePrivilegeProposal = _reflection.GeneratedProtocolMessageType('RevokeBandOraclePrivilegeProposal', (_message.Message,), {
  'DESCRIPTOR' : _REVOKEBANDORACLEPRIVILEGEPROPOSAL,
  '__module__' : 'injective.oracle.v1beta1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.RevokeBandOraclePrivilegeProposal)
  })
_sym_db.RegisterMessage(RevokeBandOraclePrivilegeProposal)

GrantPriceFeederPrivilegeProposal = _reflection.GeneratedProtocolMessageType('GrantPriceFeederPrivilegeProposal', (_message.Message,), {
  'DESCRIPTOR' : _GRANTPRICEFEEDERPRIVILEGEPROPOSAL,
  '__module__' : 'injective.oracle.v1beta1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.GrantPriceFeederPrivilegeProposal)
  })
_sym_db.RegisterMessage(GrantPriceFeederPrivilegeProposal)

GrantProviderPrivilegeProposal = _reflection.GeneratedProtocolMessageType('GrantProviderPrivilegeProposal', (_message.Message,), {
  'DESCRIPTOR' : _GRANTPROVIDERPRIVILEGEPROPOSAL,
  '__module__' : 'injective.oracle.v1beta1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.GrantProviderPrivilegeProposal)
  })
_sym_db.RegisterMessage(GrantProviderPrivilegeProposal)

RevokeProviderPrivilegeProposal = _reflection.GeneratedProtocolMessageType('RevokeProviderPrivilegeProposal', (_message.Message,), {
  'DESCRIPTOR' : _REVOKEPROVIDERPRIVILEGEPROPOSAL,
  '__module__' : 'injective.oracle.v1beta1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.RevokeProviderPrivilegeProposal)
  })
_sym_db.RegisterMessage(RevokeProviderPrivilegeProposal)

RevokePriceFeederPrivilegeProposal = _reflection.GeneratedProtocolMessageType('RevokePriceFeederPrivilegeProposal', (_message.Message,), {
  'DESCRIPTOR' : _REVOKEPRICEFEEDERPRIVILEGEPROPOSAL,
  '__module__' : 'injective.oracle.v1beta1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.RevokePriceFeederPrivilegeProposal)
  })
_sym_db.RegisterMessage(RevokePriceFeederPrivilegeProposal)

AuthorizeBandOracleRequestProposal = _reflection.GeneratedProtocolMessageType('AuthorizeBandOracleRequestProposal', (_message.Message,), {
  'DESCRIPTOR' : _AUTHORIZEBANDORACLEREQUESTPROPOSAL,
  '__module__' : 'injective.oracle.v1beta1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.AuthorizeBandOracleRequestProposal)
  })
_sym_db.RegisterMessage(AuthorizeBandOracleRequestProposal)

UpdateBandOracleRequestProposal = _reflection.GeneratedProtocolMessageType('UpdateBandOracleRequestProposal', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEBANDORACLEREQUESTPROPOSAL,
  '__module__' : 'injective.oracle.v1beta1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.UpdateBandOracleRequestProposal)
  })
_sym_db.RegisterMessage(UpdateBandOracleRequestProposal)

EnableBandIBCProposal = _reflection.GeneratedProtocolMessageType('EnableBandIBCProposal', (_message.Message,), {
  'DESCRIPTOR' : _ENABLEBANDIBCPROPOSAL,
  '__module__' : 'injective.oracle.v1beta1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.EnableBandIBCProposal)
  })
_sym_db.RegisterMessage(EnableBandIBCProposal)


DESCRIPTOR._options = None
_GRANTBANDORACLEPRIVILEGEPROPOSAL._options = None
_REVOKEBANDORACLEPRIVILEGEPROPOSAL._options = None
_GRANTPRICEFEEDERPRIVILEGEPROPOSAL._options = None
_GRANTPROVIDERPRIVILEGEPROPOSAL._options = None
_REVOKEPROVIDERPRIVILEGEPROPOSAL._options = None
_REVOKEPRICEFEEDERPRIVILEGEPROPOSAL._options = None
_AUTHORIZEBANDORACLEREQUESTPROPOSAL.fields_by_name['request']._options = None
_AUTHORIZEBANDORACLEREQUESTPROPOSAL._options = None
_UPDATEBANDORACLEREQUESTPROPOSAL._options = None
_ENABLEBANDIBCPROPOSAL.fields_by_name['band_ibc_params']._options = None
_ENABLEBANDIBCPROPOSAL._options = None
# @@protoc_insertion_point(module_scope)
