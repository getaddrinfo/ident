from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Webhook(_message.Message):
    __slots__ = ["filters", "id", "url"]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    filters: _containers.RepeatedCompositeFieldContainer[WebhookFilter]
    id: int
    url: str
    def __init__(self, id: _Optional[int] = ..., url: _Optional[str] = ..., filters: _Optional[_Iterable[_Union[WebhookFilter, _Mapping]]] = ...) -> None: ...

class WebhookFilter(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
