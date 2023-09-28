from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActionLog(_message.Message):
    __slots__ = ["id", "sign_in", "sign_out", "user_id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    SIGN_IN_FIELD_NUMBER: _ClassVar[int]
    SIGN_OUT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    sign_in: ActionSignIn
    sign_out: ActionSignOut
    user_id: int
    def __init__(self, id: _Optional[int] = ..., user_id: _Optional[int] = ..., sign_in: _Optional[_Union[ActionSignIn, _Mapping]] = ..., sign_out: _Optional[_Union[ActionSignOut, _Mapping]] = ...) -> None: ...

class ActionSignIn(_message.Message):
    __slots__ = ["source_ip"]
    SOURCE_IP_FIELD_NUMBER: _ClassVar[int]
    source_ip: str
    def __init__(self, source_ip: _Optional[str] = ...) -> None: ...

class ActionSignOut(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
