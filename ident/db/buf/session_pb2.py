# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: session.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
import action_log_pb2 as action__log__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rsession.proto\x12\rident.session\x1a\x1egoogle/protobuf/duration.proto\x1a\x10\x61\x63tion_log.proto\"o\n\x07Session\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0f\n\x07user_id\x18\x02 \x01(\x04\x12-\n\nexpires_in\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x18\n\ntoken_hash\x18\x04 \x01(\x0c\x42\x04\xc8\xa6+\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'session_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SESSION.fields_by_name['token_hash']._options = None
  _SESSION.fields_by_name['token_hash']._serialized_options = b'\310\246+\001'
  _SESSION._serialized_start=82
  _SESSION._serialized_end=193
# @@protoc_insertion_point(module_scope)
