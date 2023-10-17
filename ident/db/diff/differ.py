from google.protobuf.message import Message
from google.protobuf.internal import containers
from google.protobuf.descriptor import FieldDescriptor

import google._upb._message as abi_message

from ident.db.models import ActionLogChange
from ident.db.buf.action_log_pb2 import ignored

from .change import (
    FieldBase,
    Unchanged,
    ValueAdded,
    ValueChanged,
    ValueRemoved,
    MapKeyAdded,
    MapKeyRemoved,
    Path
)

primitives = {bytes, int, str, bool, float}


def diff(before: Message | None, after: Message) -> list[ActionLogChange]:
    target = _get_type(before, after)

    if before is not None: 
        assert type(before) == target, "non-matching types"

    diffed = _diff(before, after, path=())
    diffed = list(filter(
        lambda item: not isinstance(item, Unchanged),
        diffed
    ))

    return [diff.to_proto() for diff in diffed]


def _diff(before, after, path: Path) -> list[FieldBase]:
    """
    Calculates a list of Bases (that can be converted to ActionLogChanges) from the following types:
    - primitives
    - lists
    - maps
    - nested messages
    - enums

    The type of the `before` param must equal the type of the `after` param, unless `before` is None in which case this requirement
    is not enforced. It is unlikely that we will ever need to compare two different messages.
    """

    target = _get_type(before, after)

    # if we have a before, assert they are equal types
    if target is not None and None not in [before, after]:
        assert type(before) == type(after), "non-matching types"

    # if it is a primitive, call the `_diff_primitive` method
    if target in primitives:    
        return _diff_primitive(before, after, path)
        
    return _get_differ(target)(before, after, path)

def _diff_primitive(before, after, path: Path) -> list[FieldBase]:
    return [_real_diff_primitive(before, after, path)]

# this method exists because we want to return a list[Base]
# instead of just Base, and I don't want to repeatedely wrap
# the return in square brackets
def _real_diff_primitive(before, after, path: Path) -> FieldBase:
    match (before, after):
        case (None, None):
            return Unchanged(path=path)
        
        case (None, it):
            return ValueAdded(
                after=it,
                path=path
            )
        
        case (it, None):
            return ValueRemoved(
                before=it,
                path=path
            )
        
        case (before, after):
            if before == after:
                return Unchanged(path=path)
            
            return ValueChanged(before=before, after=after, path=path)

def _diff_list(
    before: containers.RepeatedCompositeFieldContainer | containers.RepeatedScalarFieldContainer, 
    after: containers.RepeatedCompositeFieldContainer | containers.RepeatedScalarFieldContainer, 
    path: Path
) -> list[FieldBase]:
    return []

def _diff_map(
    before: containers.ScalarMap | containers.MessageMap, 
    after: containers.ScalarMap | containers.MessageMap, 
    path: Path
) -> list[FieldBase]:
    all_keys = set([
        *(before.keys() if before is not None else {}),
        *(after.keys() if after is not None else {})
    ])

    out = []

    for key in all_keys:
        before_value = before.get(key, None)
        after_value = after.get(key, None)

        path_with_key = path + (f"[{key}]",)

    
        if key not in before and key in after:
            out.append(MapKeyAdded(
                after=key,
                path=path
            ))

            out.extend(_diff(None, after_value, path=path_with_key))

            continue

        if key in before and key not in after:
            out.append(MapKeyRemoved(
                before=key,
                path=path
            ))

            out.extend(_diff(before_value, None, path=path_with_key))

            continue

   

        # diff the values
        out.extend(_diff(before_value, after_value, path=path_with_key))

    return out

# before = None in producing new item diff
# after = None in producing removed item diff (map, array[?])
def _diff_message(before: Message | None, after: Message | None, path: Path) -> list[FieldBase]:
    """
    Creates a list of diff values for the given message(s).
    """
    all_fields = [
        field.name for field in filter(
            _is_audited,
            (before or after).DESCRIPTOR.fields
        )
    ]

    # if before is None, assume the value is essentially "empty"
    before_fields = { name: getattr(before, name) for name in all_fields } if before is not None else dict()
    after_fields = { name: getattr(after, name) for name in all_fields } if after is not None else dict()

    out = []
    
    for name in all_fields:
        before_value = before_fields.get(name, None)
        after_value = after_fields.get(name, None)

        out.extend(_diff(
            before_value,
            after_value,
            path + (name,)
        ))

    return out

def _diff_noop(before, after, path):
    # return an empty list (as if no values were found)
    return []

def _is_audited(field: FieldDescriptor):
    return not field.GetOptions().Extensions[ignored]

def _get_type(before, after) -> type:
    if before is not None:
        return type(before)
    
    if after is not None:
        return type(after)
    
    return None

def _get_differ(ty):
    if ty in primitives:
        return _diff_primitive

    if ty == abi_message.RepeatedCompositeContainer:
        return _diff_list
    
    # TODO: is there a map container type for messages?
    if ty in {abi_message.ScalarMapContainer, abi_message.MessageMapContainer}:
        return _diff_map      

    if issubclass(ty, Message):
        return _diff_message

    
    # in production it is probably better to return this?
    # return _diff_noop
        
    raise ValueError(f"unknown func for type: {ty}")