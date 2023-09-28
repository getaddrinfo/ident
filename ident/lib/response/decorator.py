from flask import jsonify
from functools import wraps

from attrs import has as is_attrs_class
from .converter import serialize

def returns(ty: type, status_code: int = 200, skip_instance_check: bool = False):
    def wrapper(f):
        @wraps(f)
        def real_impl(*args, **kwargs):
            res = f(*args, **kwargs)

            if not skip_instance_check:
                assert is_attrs_class(res), f'@returns({ty}): return type not an attrs class (expected: {ty}, got: {type(res)})'
                assert isinstance(res, ty), f'@returns({ty}): return type not {ty} (got: {type(res)})'

            return jsonify(serialize(res, ty)), status_code
        
        return real_impl
    
    return wrapper