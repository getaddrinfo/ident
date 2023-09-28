import flask

from ident.lib.inject import InjectState

from typing import Any
from functools import wraps
from pydantic import ValidationError

from .transform import ValidationException, transform
from .base import Strict, Lax

def parser(
    errors: list
):
    def try_parse(
        data: Any,
        target: Strict | Lax,
        is_json: bool = False
    ):
        try:
            out = target.model_validate(data) if not is_json else target.model_validate_json(data)

            InjectState.set_value(target, out)
        except ValidationError as e:
            errors.extend(transform(e))

    return try_parse

def validate(
    body: Strict | None = None,
    query: Lax | None = None,
    path: Strict | None = None,
    headers: Lax | None = None
):
    pairs = [
        ("body", body),
        ("query", query),
        ("path", path),
        ("headers", headers)
    ]

    present = list(filter(
        lambda it: it[1] is not None,
        pairs
    ))

    def impl(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            for _, type in present:
                InjectState.add_target(type)

            errors = []
            try_parse = parser(errors)

            for key in flask.request.view_args.keys():
                del kwargs[key]

            if body is not None:
                try_parse(
                    flask.request.get_data(as_text=True),
                    target=body,
                    is_json=True
                )

                pass

            if query is not None:
                try_parse(
                    flask.request.args,
                    target=query
                )

            if headers is not None:
                # we need to normalise from e.g., X-Header-Custom-Name to x_header_custom_name
                try_parse(
                    { key.lower().replace("-", "_"): value for key, value in flask.request.headers },
                    target=headers
                )

            if path is not None:
                try_parse(
                    flask.request.view_args,
                    target=path
                )

            if len(errors) > 0:
                raise ValidationException(errors)

            return f(*args, **kwargs)
        
        return wrapper
    
    return impl