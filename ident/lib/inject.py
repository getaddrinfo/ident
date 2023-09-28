import logging
import flask

from functools import wraps
from typing import Any, TypeVar

from ident.lib.internal.types import map_type_to_kwargs, function_name

logger = logging.getLogger(__name__)

def inject(f):
    ty_to_kwargs = map_type_to_kwargs(f)

    for ty, keys in ty_to_kwargs.items():
        if len(keys) > 1:
            raise KeyError(f'{function_name(f)} has duplicate dependencies ({ty}): consider deduplicating them')
        
    ty_to_kwargs = { ty: kwargs.pop() for ty, kwargs in ty_to_kwargs.items() }

    @wraps(f)
    def injector(*args, **kwargs):
        values = InjectState.get_values()

        for type, value in values.items():
            kwargs[ty_to_kwargs[type]] = value
        
        return f(*args, **kwargs)
    
    return injector

T = TypeVar('T')

class InjectState:
    @staticmethod
    def add_target(
        ty: type
    ):
        curr = getattr(flask.g, _INJECT_TARGET_KEY, set())

        if ty in curr:
            raise KeyError('{ty} already used as dependency: consider deduplicating types')

        curr.add(ty)
        setattr(flask.g, _INJECT_TARGET_KEY, curr)

    @staticmethod
    def has_target(ty: type):
        return ty in getattr(flask.g, _INJECT_TARGET_KEY, set())

    @staticmethod
    def set_value(
        ty: type,
        value: Any
    ):
        # ignore it if we don't have it set
        if not InjectState.has_target(ty):
            logger.warn('ignoring injection of {ty}', ty)
            return

        curr = getattr(flask.g, _INJECT_VALUE_KEY, dict())
        curr[ty] = value
        setattr(flask.g, _INJECT_VALUE_KEY, curr)

    @staticmethod
    def get_value(ty: T) -> T | None:
        return getattr(flask.g, _INJECT_VALUE_KEY, dict()).get(ty, None)

    @staticmethod
    def get_values() -> dict[type, Any]:
        return getattr(flask.g, _INJECT_VALUE_KEY, dict())


_INJECT_VALUE_KEY = 'ident__inject_value'
_INJECT_TARGET_KEY = 'ident__inject_target'

__all__ = (
    'InjectState',
    'inject'
)