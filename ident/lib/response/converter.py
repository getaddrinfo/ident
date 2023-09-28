from cattrs import Converter
from cattrs.strategies import configure_tagged_union
from typing import Any

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