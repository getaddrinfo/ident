from flask import current_app
from ident.lib.id import EPOCH

from . import models, responses

_already_calculated_endpoints = None

def get() -> responses.GetMeta:
    return responses.GetMeta(
        snowflake_epoch_millis=EPOCH,
        routes=_read_routes()
    )

def _read_routes():
    global _already_calculated_endpoints
    
    if _already_calculated_endpoints is not None:
        return _already_calculated_endpoints

    endpoints = dict()
    
    for rule in current_app.url_map.iter_rules():
        parts = []

        for is_dynamic, data in rule._trace:
            if is_dynamic:
                dyn_url_part = "{"
                dyn_url_part += data
                dyn_url_part += "}"

                parts.append(dyn_url_part)
            else:
                parts.append(data)

        parts = "".join(parts).lstrip("|")
        name = rule.endpoint.split(".")
        method = _get_endpoint_method(rule.methods.copy())

        item = f'{method} {parts}'

        _put(endpoints, name, item)

    _already_calculated_endpoints = endpoints

    return endpoints

def _get_endpoint_method(methods: set[str]):
    methods.discard('HEAD')
    methods.discard('OPTIONS')
    
    return methods.pop()

def _put(d, keys, item):
    if len(keys) > 1:
        key, *rest = keys
        
        if key not in d:
            d[key] = dict()

        _put(d[key], rest, item)
    else:
        d[keys[0]] = item