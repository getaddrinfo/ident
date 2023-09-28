from typing import TypeVar, Generic
from .attrs import define

T = TypeVar('T')

@define
class Paginable(Generic[T]):
    url: str
    data: list[T]
    has_more: bool