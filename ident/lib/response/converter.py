from cattrs import Converter, register_unstructure_hook
from cattrs.strategies import configure_tagged_union
from typing import Any, TypeVar, Callable

T = TypeVar('T')

from . import unstructures

converter = Converter(
    omit_if_default=True
)

unstructures.apply_to(converter)

def serialize(data: Any, target: type):
    return converter.unstructure(
        data,
        unstructure_as=target
    )

def union(
    target: type,
    tag: str,
    mapping: dict[type, str]
):
    mapping = { value: key for key, value in mapping.items() }

    configure_tagged_union(
        target,
        converter=converter,
        tag_generator=mapping.get,
        tag_name=tag
    )

def unstructurer(target: T, fn: Callable[[T], Any]):
    converter.register_unstructure_hook(
        target,
        fn
    )

def to_serialized_form(data: Any, from_: Any) -> Any:
    return converter.unstructure(data, unstructure_as=from_)