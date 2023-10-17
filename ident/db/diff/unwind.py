from google.protobuf.any_pb2 import Any as AnyPB
from google.protobuf.wrappers_pb2 import BoolValue, BytesValue, FloatValue, Int64Value, StringValue
from google.protobuf.message import Message

from ident.db.models import ActionLogChange, ActionLogKeyChange, ActionLogFieldChange

from dataclasses import dataclass
from typing import Any

__all__ = ("try_unwind", "unwind")

@dataclass
# Any encloses None, but better to be explicit about possibilities
class UnwoundChange:
    key: str
    before: Any | None
    after: Any | None 

def try_unwind(message: Message):
    if not hasattr(message, "changes"):
        return None
    
    return unwind(getattr(message, "changes"))

def unwind(changes: list[ActionLogChange]) -> list[UnwoundChange]:
    out = []

    for change in changes:
        value = getattr(change, change.WhichOneof("change"))
        out.append(_map_change_to_unwinder[type(value)](value))

    return out

@dataclass
class UnwoundKeyChange(UnwoundChange):
    pass

@dataclass
class UnwoundFieldChange(UnwoundChange):
    pass

def _unwind_key_change(change: ActionLogKeyChange):
    return UnwoundKeyChange(
        key=change.key,
        before=_any_to_concrete_type(change.before),
        after=_any_to_concrete_type(change.after)
    )

def _unwind_field_change(change: ActionLogFieldChange):
    return UnwoundFieldChange(
        key=change.key,
        before=_any_to_concrete_type(change.before),
        after=_any_to_concrete_type(change.after)
    )

def _any_to_concrete_type(any: AnyPB):
    name = any.TypeName()

    # unset
    if name == "":
        return None

    # unexpected primitive in any
    if name not in _map_type_name_to_concrete_unwrapper:
        raise ValueError(f'unknown name: {name}')

    return _map_type_name_to_concrete_unwrapper[name](any.value)

# map of oneof type -> unwinder
_map_change_to_unwinder = {
    ActionLogKeyChange: _unwind_key_change,
    ActionLogFieldChange: _unwind_field_change
}

# represents all primitives used in audit logging
_primitives = (
    StringValue,
    FloatValue, 
    BoolValue,
    BytesValue,
    Int64Value
)

def _make_concrete_unwrapper(ty):
    """
    Takes a primitive wrapper, and returns a function
    that can be called with bytes that returns the concrete type
    in python
    """

    def concrete_unwrapper_for_given_ty(raw: bytes):
        return ty.FromString(raw).value    

    return concrete_unwrapper_for_given_ty

# map of type_name (`type.googleapis.com/{type_name}` in Any) -> unwrapper func
_map_type_name_to_concrete_unwrapper = {
    prim.DESCRIPTOR.full_name: _make_concrete_unwrapper(prim)
    for prim in _primitives
}


