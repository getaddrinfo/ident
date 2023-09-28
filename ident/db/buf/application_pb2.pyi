from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

ARTAllow: AccessRuleType
ARTDeny: AccessRuleType
DESCRIPTOR: _descriptor.FileDescriptor

class Application(_message.Message):
    __slots__ = ["id", "name", "rules"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    rules: _containers.RepeatedCompositeFieldContainer[Rule]
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., rules: _Optional[_Iterable[_Union[Rule, _Mapping]]] = ...) -> None: ...

class Rule(_message.Message):
    __slots__ = ["group_id", "id", "type", "user_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    id: int
    type: AccessRuleType
    user_id: int
    def __init__(self, id: _Optional[int] = ..., type: _Optional[_Union[AccessRuleType, str]] = ..., user_id: _Optional[int] = ..., group_id: _Optional[int] = ...) -> None: ...

class AccessRuleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
