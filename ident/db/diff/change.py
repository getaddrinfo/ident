from dataclasses import dataclass
from typing import Any

from ident.db.models import ActionLogChange, ActionLogFieldChange, ActionLogKeyChange
from google.protobuf.any_pb2 import Any as AnyPB
from google.protobuf.wrappers_pb2 import BoolValue, BytesValue, FloatValue, StringValue, Int64Value

__all__ = (
    "FieldBase",
    "Unchanged",
    "ValueAdded",
    "ValueRemoved",
    "ValueChanged"
)

Path = tuple[str, ...]

@dataclass
class Base:
    path: Path

    def to_proto(self) -> ActionLogChange | None:
        ...

@dataclass
class FieldBase(Base):

    def to_proto(self) -> ActionLogChange | None:
        if isinstance(self, Unchanged):
            return None
        
        before = getattr(self, "before", None)
        after = getattr(self, "after", None)

        return ActionLogChange(
            field=ActionLogFieldChange(
                after=_pack(after),
                before=_pack(before),
                key=".".join(self.path)
            )
        )

@dataclass
class Unchanged(FieldBase):
    def to_proto(self):
        return None

@dataclass
class ValueAdded(FieldBase):
    after: Any

@dataclass
class ValueRemoved(FieldBase):
    before: Any

@dataclass
class ValueChanged(FieldBase):
    before: Any
    after: Any


@dataclass
class MapBase(Base):
    def to_proto(self) -> ActionLogChange | None:
        before = getattr(self, "before", None)
        after = getattr(self, "after", None)

        return ActionLogChange(
            key=ActionLogKeyChange(
                before=_pack(before),
                after=_pack(after)
            )
        )


@dataclass
class MapKeyRenamed(MapBase):
    before: Any
    after: Any

@dataclass
class MapKeyAdded(MapBase):
    after: Any

@dataclass
class MapKeyRemoved(MapBase):
    before: Any

# utils    
def _pack(value):
    if value is None:
        return None

    any = AnyPB()
    any.Pack(_to_well_known(value))

    return any

def _to_well_known(prim):
    ty = type(prim)

    if ty not in _prim_to_well_known:
        raise ValueError(f'unknown primitive: {ty}')
        
    return _prim_to_well_known[ty](prim)

_prim_to_well_known = {
    int: lambda i: Int64Value(value=i),
    str: lambda s: StringValue(value=s),
    bytes: lambda b: BytesValue(value=b),
    bool: lambda b: BoolValue(value=b),
    float: lambda f: FloatValue(value=f)
}