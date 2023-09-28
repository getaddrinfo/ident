from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
UTAdmin: UserType
UTUser: UserType

class User(_message.Message):
    __slots__ = ["attributes", "avatar_url", "email", "id", "password", "type", "username"]
    class AttributesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    AVATAR_URL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.ScalarMap[str, str]
    avatar_url: str
    email: str
    id: int
    password: bytes
    type: UserType
    username: str
    def __init__(self, id: _Optional[int] = ..., type: _Optional[_Union[UserType, str]] = ..., username: _Optional[str] = ..., email: _Optional[str] = ..., avatar_url: _Optional[str] = ..., attributes: _Optional[_Mapping[str, str]] = ..., password: _Optional[bytes] = ...) -> None: ...

class UserType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
