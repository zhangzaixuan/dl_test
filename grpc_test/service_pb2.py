# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\".\n\nAddRequest\x12\x0f\n\x07number1\x18\x01 \x01(\x05\x12\x0f\n\x07number2\x18\x02 \x01(\x05\"3\n\x0fMultiplyRequest\x12\x0f\n\x07number1\x18\x01 \x01(\x05\x12\x0f\n\x07number2\x18\x02 \x01(\x05\"\x1d\n\x0bResultReply\x12\x0e\n\x06number\x18\x01 \x01(\x05\x32W\n\x03\x43\x61l\x12\"\n\x03\x41\x64\x64\x12\x0b.AddRequest\x1a\x0c.ResultReply\"\x00\x12,\n\x08Multiply\x12\x10.MultiplyRequest\x1a\x0c.ResultReply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ADDREQUEST._serialized_start=17
  _ADDREQUEST._serialized_end=63
  _MULTIPLYREQUEST._serialized_start=65
  _MULTIPLYREQUEST._serialized_end=116
  _RESULTREPLY._serialized_start=118
  _RESULTREPLY._serialized_end=147
  _CAL._serialized_start=149
  _CAL._serialized_end=236
# @@protoc_insertion_point(module_scope)
