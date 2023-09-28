import ident.apis.session.service as service

from functools import wraps
from flask import request, abort

from ident.lib.internal.types import map_type_to_kwargs
from ident.db.models import User, Session

from ident.lib.inject import InjectState

def authenticate(f):
    # TODO: lookup value to insert

    ty_to_kwargs = map_type_to_kwargs(f)

    # if the user is present in the function args,
    # load it when looking up the session
    want_user = User in ty_to_kwargs
    want_session = Session in ty_to_kwargs

    @wraps(f)
    def real_impl(*args, **kwargs):
        if want_user:
            InjectState.add_target(User)

        if want_session:
            InjectState.add_target(Session)

        if not 'authorization' in request.headers:
            abort(401)

        value = try_parse_header(request.headers.get('authorization'))
        result = service.lookup(value, load_user=want_user, load_session=want_session)

        if result is None:
            abort(401)

        (session, user) = result

        InjectState.set_value(User, user)
        InjectState.set_value(Session, session)
        
        return f(*args, **kwargs)
    
    return real_impl
    

def try_parse_header(raw: str) -> str:
    split = raw.split(' ')

    if len(split) != 2:
        abort(401)

    [prefix, value] = split

    if prefix != "Bearer":
        abort(401)

    return value