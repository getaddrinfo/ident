from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Session(_message.Message):
    __slots__ = ["expires_in", "id", "token_hash", "user_id"]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_HASH_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    expires_in: _duration_pb2.Duration
    id: int
    token_hash: bytes
    user_id: int
    def __init__(self, id: _Optional[int] = ..., user_id: _Optional[int] = ..., expires_in: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., token_hash: _Optional[bytes] = ...) -> None: ...
