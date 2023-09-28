from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
NPRTAllow: NetworkPolicyType
NPRTDeny: NetworkPolicyType

class NetworkPolicy(_message.Message):
    __slots__ = ["id", "selector", "type"]
    ID_FIELD_NUMBER: _ClassVar[int]
    SELECTOR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    selector: str
    type: NetworkPolicyType
    def __init__(self, id: _Optional[int] = ..., type: _Optional[_Union[NetworkPolicyType, str]] = ..., selector: _Optional[str] = ...) -> None: ...

class NetworkPolicyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
